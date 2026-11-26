"""TextsAddressExpert says how the texts a program was started with
cross: 'char **'."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]


class TextsAddressExpert(TypeExpert):
  """
  Says how the texts a program was started with cross, 'char **': the
  ritual takes the address of the first and hands it on. Giving such
  back is not written.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('texts address',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims 'char **'."""
    return plain == 'char **'

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the address of the first text crosses."""
    return dict(kind='texts address', word='address')

  def canGiveBack(self) -> bool:
    """The texts themselves are not given back: their address would
    outlive nothing they are known by."""
    return False
