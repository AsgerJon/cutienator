"""MovedExpert says how a value Qt may take over crosses: by its
address, moved to Qt."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]


class MovedExpert(TypeExpert):
  """
  Says how a value Qt may take over crosses, 'T &&': the ritual takes
  its address and moves it to Qt, leaving the object it was empty. A
  value about to be thrown away has no address to give back, so giving
  one back is not written.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('moved',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims a value about to be thrown away, as 'QString &&'."""
    return plain.endswith(' &&')

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address of the value crosses."""
    return dict(kind='moved', word='address')

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The value at the address is moved to Qt."""
    taken = '%s *' % written[:-3].strip()
    return taken, 'std::move(*%s)' % name, ()

  def canGiveBack(self) -> bool:
    """A value about to be thrown away has no address to give back."""
    return False
