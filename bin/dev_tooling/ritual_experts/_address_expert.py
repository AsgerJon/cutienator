"""AddressExpert says how the address of anything crosses: as an
address."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class AddressExpert(TypeExpert):
  """
  Says how the address of anything crosses: of an object, as
  'QThread *' and 'const QObject *'; of numbers Qt reads or fills, as
  'const GLfloat *'; or of a thing of the system, as 'GLsync'. It
  crosses as an address, and what lies there is for the Python side to
  know.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('address',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims a type written as an address, as 'QThread *'."""
    return plain.endswith(' *')

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address crosses as it is."""
    return dict(kind='address', word='address')

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """The address goes to Python, with the class of what lies there."""
    pointed = written.replace('const ', '').replace('*', '').strip()
    return written, name, ('address', 'address', pointed)

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """The address Python gives is what goes back."""
    pointed = written.replace('const ', '').replace('*', '').strip()
    given = 'static_cast<%s>(given)' % written
    return 'void *', ('address', 'address', pointed), given
