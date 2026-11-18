"""
CuteFlagsHook takes the flags out of the body of a flags class.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls.space_hooks import AbstractSpaceHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any

  from . import CuteFlagsSpace


class CuteFlagsHook(AbstractSpaceHook):
  """
  Takes every number that the body of a flags class binds at a name, and
  hands it to the namespace as a flag. You never call it; worktoy does,
  at each line of the body.

  Why it exists
  -------------

  A flags class is written the way the header of Qt writes the enum:

    class AlignmentFlag(CuteFlags):
      AlignLeft = 0x0001
      AlignLeading = AlignLeft
      AlignCenter = AlignVCenter | AlignHCenter

  Each of those names must hold a value of the class once the class is
  made, not the bare number. So the numbers never reach the dictionary
  of the class: this hook claims them, and 'CuteFlags' binds a value at
  each name instead.

  What to expect
  --------------

  - Every 'int' bound at a name is a flag. A 'bool' is not, and a name
    with two underscores at each end is left alone, so a class may keep
    a number of its own under such a name.
  - While the body runs, a name of a flag reads back as its number, so
    a later line may combine earlier ones with '|'.
  - A name bound twice is refused at its line, and so is a name bound
    both to a number and to anything else, in either order. Either
    would lose one of the two without a word.
  - 'NULL' is the name of no flag at all, so 'NULL' bound to any number
    but 0 is refused.
  - A class statement naming a C++ number that 'CuteFlags' does not
    know is refused before its body runs.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def preparePhase(self, space: CuteFlagsSpace) -> None:
    """
    Checks the C++ number the class statement names, before the body
    runs.

    Raises
    ------

    ValueError
      The class statement names a C++ number that 'CuteFlags' does not
      know.
    """
    space.getNumberLayout()

  def setItemPhase(self, key: str, val: Any, old: Any = None, ) -> bool:
    """
    Claims a number bound at a name, and refuses a line that would lose
    a flag or a plain value.

    Returns
    -------

    bool
      True for a number that is now a flag, so the namespace does not
      store it. False for anything else.

    Raises
    ------

    SyntaxError
      The name is a flag already, or holds a plain value already, or
      is 'NULL' with a number that is not 0.
    """
    if key.startswith('__') and key.endswith('__'):
      return False
    className = self.space.getClassName()
    if type(val) is int:
      if dict.__contains__(self.space, key):
        infoSpec = """'%s.%s' is bound to a plain value and then to the
        number of a flag. One name holds one of the two."""
        info = infoSpec % (className, key)
        raise SyntaxError(' '.join(info.split()))
      self.space.addFlagNumber(key, val)
      return True
    if self.space.hasFlagNumber(key):
      infoSpec = """'%s.%s' is a flag and is then bound to a plain value.
      One name holds one of the two."""
      info = infoSpec % (className, key)
      raise SyntaxError(' '.join(info.split()))
    return False
