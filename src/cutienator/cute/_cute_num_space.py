"""
CuteNumSpace is the namespace the body of an enum of Qt runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import KeeSpace

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple

  from worktoy.keenum import Kee


class CuteNumSpace(KeeSpace):
  """
  The 'KeeSpace' of worktoy, with one difference: two names are one
  name only when they are written alike. You never make one; 'Cute'
  does, at every class statement of an enum of Qt.

  Why it exists
  -------------

  worktoy finds a member by its name in any case, so it refuses two
  names that differ by case alone. Qt has such names: 'Key_Dead_a' and
  'Key_Dead_A' are two keys of 'Qt::Key'. 'Cute' finds a name as it is
  written first, so both can be members, and this namespace lets the
  second one in.

  The same name written twice in a body is refused as before.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getNumsIgnoringCase(self, name: str) -> Tuple[Kee, ...]:
    """
    Says which members on record have the name already. worktoy asks
    this before it puts a member on record, and refuses the member when
    the answer is not empty.

    Here only the very name counts, where worktoy counts a name in any
    case.

    Parameters
    ----------

    name : str
      The name the body binds a member at.

    Returns
    -------

    Tuple[Kee, ...]
      The declaration on record under exactly that name, or nothing.
    """
    members = self.__enumeration_members__
    if name in members:
      return (members[name],)
    return ()
