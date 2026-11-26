"""NullExpert says how 'std::nullptr_t' crosses: it does not, the
ritual makes it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import CppText, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]


class NullExpert(TypeExpert):
  """
  Says how 'std::nullptr_t' crosses, the type of 'nullptr' alone, as in
  'QByteArrayView(std::nullptr_t)': it does not. It holds one value
  only, so the ritual hands Qt 'nullptr' itself, takes nothing for it,
  and its row has no word for it; Python hands nothing. A function
  giving one back is not written.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The names of the type of 'nullptr'.
  __null_names__ = ('std::nullptr_t', 'nullptr_t', 'decltype(nullptr)')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('null',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims the type of 'nullptr', also as 'const std::nullptr_t &'."""
    return CppText.stripReadOnly(plain) in self.__null_names__

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that nothing crosses: Python hands nothing for it."""
    return dict(kind='null', word='nothing')

  def isTakenFromPython(self) -> bool:
    """The ritual makes 'nullptr' itself; Python hands nothing."""
    return False

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """Qt is handed 'nullptr', and the ritual takes nothing for it."""
    return '', 'nullptr', ()

  def canGiveBack(self) -> bool:
    """A value that can only be 'nullptr' tells Python nothing."""
    return False
