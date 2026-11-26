"""NumberAddressExpert says how a number Qt may change crosses: by its
address."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import NumberExpert, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]


class NumberAddressExpert(TypeExpert):
  """
  Says how a number crosses that Qt may change, taken as 'int &' or
  'int *': the ritual takes the address of the number and hands Qt the
  number there. Giving one back is not written.

  The number has to be as wide on every system as its name says, or
  the address would be read wrongly on one of them; see
  'NumberExpert.findNumberWord'. A 'char *' is no number to change but
  an address of text, and is left to the others.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('number address',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findChanged(self, plain: str) -> str:
    """Gives the number type built into C++ at the address or the
    reference, or '' for a type that is no address or reference of a
    number."""
    if plain[-2:] not in (' &', ' *'):
      return ''
    changed = self.getGenerator()._followAliases(plain[:-2])
    if changed in NumberExpert.getNumberTypes() and changed != 'char':
      return changed
    return ''

  def claims(self, written: str, plain: str) -> bool:
    """Claims the address of a number, or a reference to one, as
    'int *' and 'int &'."""
    return True if self._findChanged(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """
    Says how the number crosses, with the number type built into C++
    it is as 'className', and as 'pointed' whether the header writes
    the address itself, as 'int *', and not the number, as 'int &'.
    """
    changed = self._findChanged(plain)
    word = NumberExpert.findNumberWord(written[:-2].strip(), changed)
    return dict(
        kind='number address', word='address' if word else '',
        className=changed, pointed=plain.endswith(' *'),
    )

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """Qt is handed the number at the address, which it may change."""
    taken = '%s *' % written[:-2].strip()
    return taken, name if passing['pointed'] else '*%s' % name, ()

  def canGiveBack(self) -> bool:
    """The number itself, to be changed where it is, is not given back:
    its address would outlive nothing it is known by."""
    return False
