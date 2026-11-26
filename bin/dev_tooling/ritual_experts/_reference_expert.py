"""ReferenceExpert says how an object Qt reads or changes where it is
crosses: by its address."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class ReferenceExpert(TypeExpert):
  """
  Says how an object crosses that Qt reads, or changes where it is, as
  'QString &' or 'const QVectorPath &' of a class C++ cannot copy: the
  ritual takes its address and hands Qt the object. An object Qt gives
  this way is where it is: its address goes back, and Qt keeps owning
  it.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('reference',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims a reference, as 'QString &'."""
    return plain.endswith(' &')

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address of the object crosses."""
    return dict(kind='reference', word='address')

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """Qt is handed the object at the address."""
    return '%s *' % written[:-2].strip(), '*%s' % name, ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The address of the object Qt gives is what goes back."""
    return '%s *' % given[:-2].strip(), 'return &(', '));', ()
