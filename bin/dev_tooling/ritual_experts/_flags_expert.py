"""FlagsExpert says how the combinations of a flags enum cross: as the
number of the combination."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class FlagsExpert(TypeExpert):
  """
  Says how flags cross: the type Qt names for the combinations of a
  flags enum, as 'Qt::WindowFlags', which C++ reads as
  'QFlags<Qt::WindowType>'. The ritual takes and gives the number of
  the combination as an 'int'.

  Qt keeps the combinations of a flags enum in a number as wide as an
  'int', with a sign on one system and without on another, so the
  ritual hands the 32 bits over as an 'int' on every system. Qt keeps
  the combinations of a wider enum in a wider number, which no 'int'
  holds: those have no word.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  How C++ reads the type of the combinations of a flags enum, as
  #  'QFlags<Qt::WindowType>', with the enum in the brackets. The same
  #  type taken to be read only, as 'const QFlags<Qt::WindowType> &',
  #  crosses the same way.
  __flags_pattern__ = re.compile(
      r'(?:const )?QFlags<([A-Za-z_]\w*(?:::[A-Za-z_]\w*)*)>(?: &)?')
  #  The number types Qt keeps such combinations in a number as wide as
  #  an 'int' for: every number type of an enum that is no wider.
  __flags_enum_types__ = (
      'bool', 'char', 'signed char', 'unsigned char', 'short',
      'unsigned short', 'int', 'unsigned int',
  )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('flags',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def findFlagsEnum(self, plain: str) -> str:
    """
    Gives the flags enum whose combinations a type holds:
    'Qt::WindowType' for 'QFlags<Qt::WindowType>', also when the type
    is taken to be read only, as 'const QFlags<Qt::WindowType> &'. Gives
    '' for any other type, and for an enum the dependency tree does not
    know.
    """
    match = self.__flags_pattern__.fullmatch(plain)
    if match is None:
      return ''
    enumName = match.group(1)
    if enumName in self.getGenerator()._getTypeTables()['enums']:
      return enumName
    return ''

  def claims(self, written: str, plain: str) -> bool:
    """Claims the combinations of a flags enum; see 'findFlagsEnum'."""
    return True if self.findFlagsEnum(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says how the combination crosses, with the type as C++ reads it
    as 'className', as 'QFlags<Qt::WindowType>'."""
    generator = self.getGenerator()
    flagsEnum = self.findFlagsEnum(plain)
    tables = generator._getTypeTables()
    fixedPlain = tables['enumTypes'].get(flagsEnum, ('int',) * 2)[1]
    fixedPlain = generator._followAliases(fixedPlain)
    #  Qt keeps the combinations of a wider enum in a wider number,
    #  which no 'int' holds.
    word = 'int' if fixedPlain in self.__flags_enum_types__ else ''
    flagsType = 'QFlags<%s>' % flagsEnum
    return dict(kind='flags', word=word, className=flagsType)

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The combination is made from its number for the call."""
    return 'int', '%s::fromInt(%s)' % (passing['className'], name), ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The number of the combination is what goes back."""
    return 'int', 'return static_cast<int>(', ').toInt());', ()

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """The number of the combination is handed over, and Python makes
    the combination of it again."""
    if not passing['word']:
      return None
    enumName = passing['className'][len('QFlags<'):-1]
    handed = 'static_cast<int>(%s.toInt())' % name
    return 'int', handed, ('int', 'flags', enumName)

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """The number Python gives is made the combination again."""
    if not giving['word']:
      return None
    enumName = giving['className'][len('QFlags<'):-1]
    given = '%s::fromInt(given)' % giving['className']
    return 'int', ('int', 'flags', enumName), given
