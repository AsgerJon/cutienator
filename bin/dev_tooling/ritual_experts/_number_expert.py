"""NumberExpert says how a number Qt reads crosses: as itself."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import CppText, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class NumberExpert(TypeExpert):
  """
  Says how a number crosses that Qt takes to read only: 'bool' and the
  numbers built into C++, as 'int' and 'double', also under a second
  name, as 'qsizetype', and taken as 'const bool' or 'const int &'. It
  crosses as a copy, and goes by the name C++ has for it in the sigil, as
  'int', 'bool' and 'long long'.

  'long' and 'unsigned long' are 64 bits wide on Linux and macOS and 32
  on Windows, so the sigil would be right on one of them only: such a
  number has a word only where the header writes 'long' itself, or a
  name known to follow the system, as 'size_t'; see 'findNumberWord'.
  Other experts ask that of this one as well.

  A number of no word, as 'GLsizeiptr' or 'qintptr', which is as wide
  as an address on each system, crosses widened: as a 'long long', or
  an 'unsigned long long' where it has no sign. The ritual itself takes
  and gives that, and C++ turns it into the number Qt has, on every
  system alike; 'widened' says so in the record.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getNumberTypes() -> Tuple[str, ...]:
    """Gives the numbers built into C++, as the compiler writes them."""
    return NumberExpert.__number_types__

  @staticmethod
  def findNumberWord(written: str, plain: str) -> str:
    """
    Gives the word a number goes by in a sigil, or '' when no word is
    right on every system.

    Parameters
    ----------

    written : str
      The type as the header writes it, as 'qsizetype' or 'size_t'.

    plain : str
      The number type built into C++ that it ends as on this system, as
      'long long' or 'unsigned long'.

    Returns
    -------

    str
      'plain' for every type but 'long' and 'unsigned long'. Those two
      are 64 bits wide on Linux and macOS and 32 on Windows, so they
      are given only when the header writes 'long' itself. A name known
      to follow the system, as 'size_t', gives its own word. Any other
      name gives ''.
    """
    if plain not in ('long', 'unsigned long'):
      return plain
    if written.startswith('const '):
      written = written[6:]
    if written in NumberExpert.__long_names__:
      return plain
    return NumberExpert.__size_names__.get(written, '')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The numbers built into C++, as the compiler writes them.
  __number_types__ = (
      'bool', 'char', 'signed char', 'unsigned char', 'short',
      'unsigned short', 'int', 'unsigned int', 'long', 'unsigned long',
      'long long', 'unsigned long long', 'float', 'double',
  )
  #  The names a header writes 'long' itself by. A number that ends as
  #  'long' under any other name is as wide as its system makes it.
  __long_names__ = ('long', 'unsigned long', 'ulong')
  #  The names that end as 'long' on Linux and macOS and as another type
  #  on Windows, each with the word it goes by in a sigil.
  __size_names__ = {'size_t': 'size_t', 'std::size_t': 'size_t'}
  #  The widest number of each sign, which a number of no word crosses
  #  as; see 'findPassing'.
  __widened_numbers__ = {
      'long': 'long long', 'unsigned long': 'unsigned long long'}

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('number',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def findReadOnlyNumber(self, plain: str) -> str:
    """
    Gives the number type built into C++ that a type hands around as a
    copy: 'int' for 'int', 'const int' and 'const int &'. Gives '' for
    any other type, as 'int &', which the function may change.
    """
    generator = self.getGenerator()
    number = generator._followAliases(CppText.stripReadOnly(plain))
    if number in self.__number_types__:
      return number
    return ''

  def claims(self, written: str, plain: str) -> bool:
    """Claims a number taken to be read only; see
    'findReadOnlyNumber'."""
    return True if self.findReadOnlyNumber(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says how the number crosses, with the number type built into
    C++ it is as 'className'. A number of no word crosses widened; see
    the class."""
    readOnly = self.findReadOnlyNumber(plain)
    word = self.findNumberWord(CppText.stripReadOnly(written), readOnly)
    if not word and readOnly in self.__widened_numbers__:
      widened = self.__widened_numbers__[readOnly]
      return dict(
          kind='number', word=widened, className=widened, widened=True)
    return dict(kind='number', word=word, className=readOnly)

  def _findOwnType(self, written: str, record: Record) -> str:
    """Gives the type the ritual itself takes or gives for the number:
    as the header writes it, or the widened one."""
    if record.get('widened'):
      return record['className']
    return CppText.stripReadOnly(written)

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """A number taken to be read only is handed over as a copy."""
    return self._findOwnType(written, passing), name, ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The number goes back as a copy."""
    return self._findOwnType(given, giving), 'return ', ');', ()

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """The number goes to Python as a copy."""
    taken = self._findOwnType(written, passing)
    return taken, name, (passing['word'], 'number', '')

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """The number Python gives is what goes back."""
    given = self._findOwnType(written, giving)
    return given, (giving['word'], 'number', ''), 'given'
