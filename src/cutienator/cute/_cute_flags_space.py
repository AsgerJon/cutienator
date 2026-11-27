"""
CuteFlagsSpace is the namespace the body of a flags class runs in.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.mcls import BaseSpace

from . import CuteFlagsHook

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, Optional, Tuple


class CuteFlagsSpace(BaseSpace):
  """
  Keeps the name and the number of each flag that the body of a flags
  class declares, and knows which C++ number the class is. You never
  make one; 'MetaCuteFlags' does, at every class statement of a flags
  class.

  What to expect
  --------------

  - 'cuteFlagsHook' hands every flag of the body to 'addFlagNumber', in
    the order written. 'CuteFlags' reads them with 'getFlagNumbers' once
    the class is made.
  - The class statement may name the C++ number the flags are, with the
    words the sigil files of the rituals use:

      class KeyboardModifier(CuteFlags, number='unsigned int'):

    Without it the number is 'int', which most flags of Qt are.
    'getNumberLayout' gives how many bits that number has and whether it
    has a sign, which decides what '~' gives.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  For each C++ number a flags class may be: how many bits it has, and
  #  whether it has a sign. 'char', 'long' and 'unsigned long' are left
  #  out on purpose: they are not the same on every system.
  __number_layouts__ = {
    'signed char'       : (8, True),
    'unsigned char'     : (8, False),
    'short'             : (16, True),
    'unsigned short'    : (16, False),
    'int'               : (32, True),
    'unsigned int'      : (32, False),
    'long long'         : (64, True),
    'unsigned long long': (64, False),
  }

  cuteFlagsHook = CuteFlagsHook()

  #  Private Variables
  #  The number of each flag of this body by its name, in the order
  #  written.
  __flag_numbers__: Optional[Dict[str, int]] = None

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getFlagNumbers(self) -> Dict[str, int]:
    """
    Gives the number of each flag the body declared, by its name, in the
    order written. The dictionary is a new one each time.
    """
    if self.__flag_numbers__ is None:
      return dict()
    return {**self.__flag_numbers__, }

  def hasFlagNumber(self, name: str) -> bool:
    """Says whether the body declared a flag at the name."""
    if self.__flag_numbers__ is None:
      return False
    return True if name in self.__flag_numbers__ else False

  def getNumberName(self) -> str:
    """
    Gives the C++ number the class statement names with 'number=', or
    'int' when it names none.
    """
    return self.getKwargs().get('number', 'int')

  def getNumberLayout(self) -> Tuple[int, bool]:
    """
    Gives how many bits the C++ number of the class has, and whether it
    has a sign.

    Raises
    ------

    ValueError
      The class statement names a C++ number that is not in the table.
    """
    numberName = self.getNumberName()
    try:
      return self.__number_layouts__[numberName]
    except (KeyError, TypeError):
      infoSpec = """The flags class '%s' says it is the C++ number %r.
      A flags class is one of: %s."""
      words = ["""'%s'""" % word for word in self.__number_layouts__]
      known = ', '.join(words)
      info = infoSpec % (self.getClassName(), numberName, known)
      raise ValueError(' '.join(info.split()))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def addFlagNumber(self, name: str, number: int) -> None:
    """
    Puts one flag of the body on record. 'cuteFlagsHook' calls this at
    the line that declares the flag.

    Parameters
    ----------

    name : str
      The name the body binds.

    number : int
      The number it binds there.

    Raises
    ------

    SyntaxError
      The body declared a flag at the name already, or the name is
      'NULL' and the number is not 0.
    """
    className = self.getClassName()
    numbers = self.getFlagNumbers()
    if name in numbers:
      infoSpec = """'%s.%s' is declared twice. A second name for the
      same number is fine; a second number for the same name is not."""
      info = infoSpec % (className, name)
      raise SyntaxError(' '.join(info.split()))
    if name == 'NULL' and number:
      infoSpec = """'%s.NULL' is bound to %d. 'NULL' is the name of no
      flag at all, and its number is 0 in every flags class."""
      info = infoSpec % (className, number)
      raise SyntaxError(' '.join(info.split()))
    numbers[name] = number
    self.__flag_numbers__ = numbers
