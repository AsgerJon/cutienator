"""ReachExpert is what every way of reaching a function of Qt from a
ritual is built on."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Tuple

  Record = Dict[str, Any]


class ReachExpert(RitualExpert):
  """
  What every way of reaching a function of Qt from a ritual is built
  on. A ritual calls the function where Qt's library offers it
  ('CallExpert'), or carries a copy of Qt's code for it where it does
  not ('CopyExpert').

  The generator asks its reach experts in turn, in the order of
  'RitualGenerator.__reach_experts__', and the first that can reach a
  function has it. Where none can, the function is not written, and
  the reason names every way and why each could not.

  Each way says
  -------------

  - 'canReach': whether it can reach one function of the class.
  - 'getWay': what it does, in words, as 'be called'.
  - 'getRefusal': why it cannot, in words, when it cannot.
  - 'adopt': for a function it reached, the ritual written its own way,
    where that is not the call by name.
  - 'settle': after every function has its plan, what the way still
    has to do for the rituals it reached; most ways have nothing.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canReach(self, member: Record) -> bool:
    """
    Says whether this way reaches a function of the class.

    Parameters
    ----------

    member : Record
      What the compiler wrote down about the function, with its own
      name for it under 'mangledName'.
    """
    infoSpec = """'%s' does not say whether it reaches a function."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  def getWay(self) -> str:
    """Says what this way does to reach a function, as 'be called'."""
    infoSpec = """'%s' does not say what it does."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  def getRefusal(self) -> str:
    """Says why this way does not reach a function 'canReach' said no
    to, in words."""
    infoSpec = """'%s' does not say why it does not reach a function."""
    raise NotImplementedError(infoSpec % type(self).__name__)

  def adopt(self, plan: Record, member: Record) -> None:
    """
    Takes on a function this way reached, once nothing else stands in
    the way of writing it, and writes its ritual anew where this way
    calls it otherwise than by its name. The plan as worked out calls
    it by its name; most ways leave it so.
    """

  def settle(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """
    Does, after every function of the class has its plan, what this way
    still has to do for the rituals it reached. It may move a ritual
    from 'written' to 'unwritten', with the reason. Nothing to do here;
    a way that has something to do says so itself.
    """
