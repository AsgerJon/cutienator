"""
CuteNum is the one base of every enum of Qt that is no flags enum.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import KeeMeta, KeeBase

from . import DoorNumber, CuteFlags, Cute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any


class CuteNum(Cute.keeNum, strictCase=False):
  """
  The base of every enum of Qt that is no flags enum. It is a 'KeeNum'
  of worktoy: a subclass names its members with 'Kee', as Qt names
  them:

    class AspectRatioMode(CuteNum):
      IgnoreAspectRatio = Kee[int](0)
      KeepAspectRatio = Kee[int](1)
      KeepAspectRatioByExpanding = Kee[int](2)

  What to expect
  --------------

  - A is A: a member is only itself. It is never an 'int', and its
    number is 'member.value'. Two names for one number are two members.
  - Names are written as Qt writes them, in any case, 'Key_Dead_a'
    beside 'Key_Dead_A' included; see 'Cute'. Where Qt's name is a word
    of Python, the word of C stands in: 'NULL', 'TRUE', 'FALSE'.
  - 'AspectRatioMode(1)' and "AspectRatioMode('KeepAspectRatio')" give
    the member. A number Qt gave no name gives a member without a
    name, as 'QEvent.Type(1001)'; see 'Cute'.
  - Tolerance: '==' and '+' answer for the number, so
    'dialog.exec() == DialogCode.Accepted' holds and
    'ItemDataRole.UserRole + 1' is 257, a plain number. The hash
    follows the number, as it has to. Among members A is still A: two
    members are equal only when they are one.
  - In a signature, as '@overload(AspectRatioMode)', a member is
    taken, and so is a number or a name that Qt gave a name; any other
    number is said out loud: 'setMode(AspectRatioMode(77))'.

  Everything else is worktoy's 'KeeNum': members are made once and
  never changed, the enum is gone through in the order written, and an
  enum based on another holds its members.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __eq__(self, other: Any) -> Any:
    """
    A is A: among the members of enums and the values of flags, a
    member is equal to itself alone. Tolerance: against anything else
    it answers as its number does, so
    'dialog.exec() == DialogCode.Accepted' holds. A 'bool' is no number
    of it.
    """
    if isinstance(type(other), KeeMeta) or isinstance(other, CuteFlags):
      return True if self is other else False
    if type(other) is bool:
      return False
    return self.value == other

  def __hash__(self) -> int:
    """The hash of the number, since a member is equal to its number."""
    return hash(self.value)

  def __add__(self, other: Any) -> Any:
    """Tolerance: a member plus a number is a plain number."""
    return self.value + other

  def __radd__(self, other: Any) -> Any:
    return other + self.value

  def __reduce__(self) -> tuple:
    """
    Says how a member is stored and read back as itself: one Qt named
    by its name, as worktoy has it, and one without a name by its
    number.
    """
    cls = type(self)
    if cls.isNameless(self):
      return cls, (self.value,)
    return KeeBase.__reduce__(self)

  @classmethod
  def __cast_as__(cls, value: Any) -> Any:
    """
    Says what a signature naming the enum takes in the place of a
    member: a number Qt gave a name, or such a name. worktoy asks this
    when a call gives something else than a member of the enum.

    Returns
    -------

    Any
      The member, or 'NotImplemented' for anything the enum does not
      take: a number Qt gave no name, a name it does not have, and the
      number of a member that came in through a door; see 'DoorNumber'.
    """
    if isinstance(value, DoorNumber):
      return NotImplemented
    if type(value) is int and value not in cls.valuedMembers:
      return NotImplemented
    return super().__cast_as__(value)
