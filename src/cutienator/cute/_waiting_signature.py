"""
WaitingSignature is one signature of a class body that names a late
class, kept until the late class is made.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from types import FunctionType
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Callable, Optional, Tuple


class WaitingSignature:
  """
  Holds one signature that names a late class, together with the
  function it belongs to, until the late class is made. See 'WAIT' for
  the whole story; this is step 4 of it.

  You never make one yourself. 'CuteSpace' makes one for each waiting
  signature of a 'WaitingOverload' the class body binds, and keeps it:

    @overload(QIcon, str)                    # waits for 'QIcon'
    @overload(str)                           # on record at once
    def setText(self, *args): ...

    space.getWaitingSignatures()             # (('setText', <the first>),)

  Provided by 'CuteSpace'
  -----------------------

  - 'setSignatureEntries': what stood between the brackets. Required.
  - 'setFunction': the function under the decorators. Required.

  What to expect
  --------------

  - It only holds. It checks nothing and calls nothing.
  - 'CuteSpace' replaces the entries as late classes are made, through
    'setSignatureEntries', until no 'WAIT' is left among them. The
    signature is then put on record and this object is let go.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __signature_entries__: Optional[Tuple[Any, ...]] = None
  __waiting_function__: Optional[Callable] = None

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getSignatureEntries(self) -> Tuple[Any, ...]:
    """
    Gives the entries of the signature, in the order they were written:
    classes, 'THIS', and at least one 'WAIT' until the last late class
    among them is made.

    Raises
    ------

    MissingVariable
      'setSignatureEntries' has not been called.
    """
    if self.__signature_entries__ is None:
      raise MissingVariable(self, '__signature_entries__', tuple)
    return self.__signature_entries__

  def getFunction(self) -> Callable:
    """
    Gives the function the signature belongs to, without any
    'classmethod' or 'staticmethod' around it.

    Raises
    ------

    MissingVariable
      'setFunction' has not been called.
    """
    if self.__waiting_function__ is None:
      raise MissingVariable(self, '__waiting_function__', FunctionType)
    return self.__waiting_function__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setSignatureEntries(self, *signatureEntries: Any) -> None:
    """
    Tells which entries the signature has. Required. Calling it again
    replaces the entries, which is how 'CuteSpace' puts a class in the
    place of its 'WAIT'.

    Raises
    ------

    ValueError
      Called with no entry at all. A signature without entries names no
      late class and has no reason to wait.
    """
    if not signatureEntries:
      infoSpec = """A waiting signature has at least one entry, and none
      was given."""
      raise ValueError(' '.join(infoSpec.split()))
    self.__signature_entries__ = (*signatureEntries,)

  def setFunction(self, function: Callable) -> None:
    """
    Tells which function the signature belongs to. Required.

    Raises
    ------

    TypeException
      'function' cannot be called.
    """
    if not callable(function):
      raise TypeException('function', function, FunctionType)
    self.__waiting_function__ = function

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which function waits, and for which signature."""
    clsName = type(self).__name__
    if self.__waiting_function__ is None:
      return '<%s with no function yet>' % clsName
    name = getattr(self.__waiting_function__, '__name__', '?')
    entries = self.__signature_entries__ or ()
    shown = ', '.join(
        getattr(entry, '__name__', None) or str(entry) for entry in entries
    )
    return "<%s of '%s', waiting as (%s)>" % (clsName, name, shown)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
