"""NothingExpert says how 'void' crosses: as nothing."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Given = Tuple[str, str, str, Tuple[str, ...]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class NothingExpert(TypeExpert):
  """
  Says how 'void' crosses: a function giving back 'void' gives nothing,
  and its sigil says 'nothing'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('nothing',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims 'void'."""
    return plain == 'void'

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that nothing crosses."""
    return dict(kind='nothing', word='nothing')

  def writeGiven(self, given: str, giving: Record) -> Given:
    """Calls Qt's function and gives nothing back."""
    return given, '', ');', ()

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """The Python function gives nothing back either."""
    return 'void', ('nothing', 'nothing', ''), ''
