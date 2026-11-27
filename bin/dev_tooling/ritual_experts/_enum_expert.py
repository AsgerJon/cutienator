"""EnumExpert says how an enum crosses: as the number it is kept as."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import NumberExpert, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class EnumExpert(TypeExpert):
  """
  Says how an enum crosses, as 'Qt::TimerType': as the number type it
  is kept as, and by that number's word in the sigil. An enum kept as a
  type that is no number cannot be passed.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('enum',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims every enum Python has something for; see
    'RitualGenerator._getTypeTables'."""
    return plain in self.getGenerator()._getTypeTables()['enums']

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says how the enum crosses, or None for one kept as a type that
    is no number."""
    generator = self.getGenerator()
    tables = generator._getTypeTables()
    fixedWritten, fixedPlain = tables['enumTypes'].get(plain, ('int',) * 2)
    fixedPlain = generator._followAliases(fixedPlain)
    if fixedPlain not in NumberExpert.getNumberTypes():
      return None
    word = NumberExpert.findNumberWord(fixedWritten, fixedPlain)
    return dict(kind='enum', word=word)

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """The enum goes to Python as its number."""
    return 'int', 'static_cast<int>(%s)' % name, ('int', 'enum', written)

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """The number Python gives is made the enum again."""
    given = 'static_cast<%s>(given)' % written
    return 'int', ('int', 'enum', written), given
