"""TypeExpert is what every way a type crosses between Python and C++ is
built on."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class TypeExpert(RitualExpert):
  """
  What every way a type crosses between Python and C++ is built on:
  numbers, text, addresses, values, enums, flags, lists and so on,
  one expert each.

  The generator asks its type experts in turn, in the order of
  'RitualGenerator.__type_experts__', and the first that claims a type
  says how it crosses. A type no expert claims cannot be passed yet,
  and a function naming it is not written.

  How a type crosses is a record, as 'findPassing' gives it, whose
  'kind' names it, as 'number' or 'list'; 'getKinds' says which kinds
  an expert gives, and the generator finds the expert of a record by
  its kind.

  Each expert says
  ----------------

  - 'claims': whether a type is its own.
  - 'findPassing': how one of its types crosses, or None when it claims
    the type and still cannot pass it.
  - 'writeTaken': what a ritual takes for an argument of the type and
    what it hands Qt.
  - 'canGiveBack' and 'writeGiven': whether a ritual can give a value
    of the type back, and how.
  - 'handOver' and 'handBack': how a function Python takes over in a
    cute class hands an argument of the type to Python, and takes one
    back from it; None where it cannot.

  What is not said here is the plainest way: the ritual takes the type
  as the header writes it and hands it on, and gives it back with
  'return'. An expert says only where its kind does more.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the kinds of the records 'findPassing' gives, as
    ('number',)."""
    infoSpec = """'%s' does not say which kinds it gives."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """
    Says whether a type is this expert's own.

    Parameters
    ----------

    written : str
      The type as the header writes it, with every name in full.

    plain : str
      The same type as the compiler reads it, second names followed.
    """
    infoSpec = """'%s' does not say which types it claims."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """
    Says how a type this expert claims crosses: a record with 'kind',
    one of 'getKinds', and 'word', its word in the sigil, '' for a number
    with no word that is right on every system; and what the kind
    needs besides. None when the expert claims the type and still
    cannot pass it.
    """
    infoSpec = """'%s' does not say how its types cross."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  def isTakenFromPython(self) -> bool:
    """Says whether Python hands something for an argument of the type.
    A type that holds one value only, as 'std::nullptr_t', is made by
    the ritual itself: it takes nothing for it, and its sigil has no word
    for it."""
    return True

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """
    Says what a ritual takes for an argument of the type, and what it
    hands Qt for it.

    Parameters
    ----------

    name : str
      The name of the argument, as 'parent'.

    written : str
      The type as the header writes it, with every name in full.

    passing : Record
      How the type crosses, as 'findPassing' gave it.

    Returns
    -------

    Taken
      The type the ritual takes, as 'const QSize *'; what it hands Qt,
      as '*size'; and the classes whose header files it needs for that,
      in order.
    """
    return written, name, ()

  def canGiveBack(self) -> bool:
    """Says whether a ritual can give a value of the type back."""
    return True

  def writeGiven(self, given: str, giving: Record) -> Given:
    """
    Says how a ritual gives back what Qt gives of the type.

    Parameters
    ----------

    given : str
      The type as the header writes it, with every name in full.

    giving : Record
      How the type crosses, as 'findPassing' gave it.

    Returns
    -------

    Given
      The type the ritual gives; what stands before the call of Qt's
      function, as 'return '; what stands after it, as ');'; and the
      classes whose header files it needs for that, in order.
    """
    return given, 'return ', ');', ()

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """
    Says how a function Python takes over in a cute class hands an
    argument of the type to the Python function: the C++ type handed
    over, what is handed, and, for Python, its word with what it is,
    as ('address', 'value', 'QSize'). None where it cannot be handed
    over yet.
    """
    return None

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """
    Says how a function Python takes over in a cute class takes back
    what the Python function gives of the type: the C++ type taken, its
    word with what it is, and what the function gives Qt made of
    'given'. None where it cannot be taken back yet.
    """
    return None

  def settle(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """
    Does, after every function of the class has its plan, and before
    the ways of reaching them settle, what this kind still has to do:
    it may add rituals of its own, or move a ritual from 'written' to
    'unwritten', with the reason. Most kinds have nothing to do.
    """
