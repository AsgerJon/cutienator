"""FunctionAddressExpert says how the address of a function crosses:
as an address."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from . import CppText, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class FunctionAddressExpert(TypeExpert):
  """
  Says how the address of a function crosses, as 'void (*)(void *)' or
  Qt's 'QFunctionPointer': the ritual takes it as 'void *', and hands
  Qt the address made the function's type again; a function Qt gives
  goes back the same way. Python hands over the address of a function
  it made, as 'ctypes' makes one. Its word in the row is 'address'.

  The address of a function of a class, as 'void (QObject::*)()', is
  no plain address: C++ keeps more in it, and it cannot be handed over
  as one. This expert claims it, so no other does, and does not pass
  it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The address of a function, as the compiler writes one:
  #  'void (*)(int)', and of a function of a class, 'void (QObject::*)()'.
  __function_address__ = re.compile(r'\(\s*\*\s*\)\s*\(')
  __member_address__ = re.compile(r'\(\s*[A-Za-z_][\w:<>, ]*::\s*\*\s*\)')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('function address',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims the address of a function, and of a function of a
    class."""
    bare = CppText.stripReadOnly(plain)
    if self.__member_address__.search(bare):
      return True
    return True if self.__function_address__.search(bare) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address of a function crosses as an address, or
    None for the address of a function of a class."""
    if self.__member_address__.search(CppText.stripReadOnly(plain)):
      return None
    return dict(kind='function address', word='address')

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The address is made the function's type again for Qt."""
    own = CppText.stripReadOnly(written)
    return 'void *', 'reinterpret_cast<%s>(%s)' % (own, name), ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The address of the function Qt gives goes back as an address."""
    return 'void *', 'return reinterpret_cast<void *>(', '));', ()
