"""
Cute is the metaclass of the enums of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import KeeMeta, Kee
from worktoy.waitaminute.keenum import KeeResolveError

from . import CuteNumSpace, ShortNameMeta

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional


class Cute(ShortNameMeta, KeeMeta):
  """
  The 'KeeMeta' of worktoy, taught the two things Qt needs of an enum
  that worktoy refuses. You never use it by name: an enum of Qt is
  based on 'CuteNum'.

  Why it is named 'Cute'
  ----------------------

  worktoy builds the root of a metaclass itself and names it after the
  metaclass with 'Num' put behind. For 'Cute' that gives 'CuteNum',
  which is what the text of every enum of Qt then says:
  "<CuteNum 'AspectRatioMode': 3 members>".

  What it changes
  ---------------

  - Names that differ by case alone. Qt has 'Key_Dead_a' beside
    'Key_Dead_A'. A name is found as it is written first. In another
    case it is still found where one name fits, as worktoy has it, and
    refused where two fit.
  - The names of an enum are names of the class that holds the enum
    as well, as 'QEvent.Timer'; see 'ShortNameMeta'.
  - A number Qt gave no name. Qt hands whole ranges of numbers to the
    programmer: 'QEvent.Type(1001)' is the type of an event of your
    own. Calling an enum with such a number gives a member without a
    name. It is made the first time and kept, so one number is one
    member. It is in the enum, 'isinstance' says so, but it is not
    listed and not counted: going through the enum gives the members
    Qt named.

  Everything else is worktoy's 'KeeMeta', unchanged.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Private Variables
  #  The members of an enum by their names as written.
  __exact_members__: Optional[Dict[str, Any]] = None
  #  The members of an enum that Qt gave no name, by their numbers.
  __nameless_members__: Optional[Dict[int, Any]] = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getShortNames(cls) -> dict:
    """
    Gives each name Qt wrote in the enum with its member, in the order
    written.
    """
    return {member.name: member for member in cls}

  def isNameless(cls, member: Any) -> bool:
    """
    Says whether a member of the enum is one Qt gave no name, as
    'QEvent.Type(1001)' is.
    """
    nameless = cls.__nameless_members__
    if nameless is None:
      return False
    return True if nameless.get(member.value, None) is member else False

  def _getNameless(cls, number: int) -> Any:
    """
    Gives the one member of a number Qt gave no name, making it the
    first time.

    It is made the way worktoy makes every member: from a 'Kee' of its
    number. Its name is the number written out, and it has no place in
    the order of the enum.
    """
    nameless = cls.__nameless_members__
    try:
      return nameless[number]
    except KeyError:
      kee = Kee[int](number)
      kee.name = str(number)
      kee._setIndex(-1)
      member = type.__call__(cls, kee)
      member._addOwner(cls)
      nameless[number] = member
      return member

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def __prepare__(mcls, name: str, bases: tuple, **kwargs) -> CuteNumSpace:
    """
    Gives the namespace the body of an enum of Qt runs in: a new
    'CuteNumSpace'. Python calls this at every class statement of such
    an enum, before the body runs.
    """
    return CuteNumSpace(mcls, name, bases, **kwargs)

  def _createNamedMembers(cls) -> None:
    """
    Makes the tables a member is found in by its name. worktoy calls
    this once, as the enum is made.

    worktoy keeps one table, by the name in lower case. Here a second
    one holds the names as written, and the first leaves out a name in
    lower case that two members share, since it could not say which of
    the two is meant.
    """
    exact, lowered, shared = dict(), dict(), set()
    for member in cls._getMembers():
      exact[member.name] = member
      key = member.name.lower()
      if key in lowered:
        shared.add(key)
      lowered[key] = member
    for key in shared:
      del lowered[key]
    type.__setattr__(cls, '__named_members__', lowered)
    type.__setattr__(cls, '__exact_members__', exact)
    type.__setattr__(cls, '__nameless_members__', dict())

  def _resolveFromName(cls, identifier: str) -> Any:
    """
    Finds a member by its name: as written first, then in any case
    where one name fits. worktoy calls this when the enum is called
    with a text.

    Returns
    -------

    Any
      The member, or 'NotImplemented' when no name fits, or when two
      names fit that differ by case alone.
    """
    exact = cls.__exact_members__
    if identifier in exact:
      return exact[identifier]
    return KeeMeta._resolveFromName(cls, identifier)

  def _resolveMember(cls, identifier: Any, allowIndex: bool = False) -> Any:
    """
    Finds the member something stands for, as worktoy does, and gives
    a member without a name for a number that stands for none.

    worktoy calls this for 'Type(x)' and for 'Type[x]'. Only an 'int'
    gets a member without a name, and only in an enum that has members,
    whose numbers are 'int'. Anything else worktoy refuses is refused.

    Raises
    ------

    KeeResolveError
      Nothing fits, and what was given is no number.
    """
    try:
      return KeeMeta._resolveMember(cls, identifier, allowIndex)
    except KeeResolveError:
      if type(identifier) is not int or not cls._getMembers():
        raise
      if cls.valueType is not int:
        raise
      return cls._getNameless(identifier)
