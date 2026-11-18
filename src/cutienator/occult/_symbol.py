"""Symbol is one entry in the list of names a shared object offers."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Never


class Symbol:
  """
  A shared object lists what it offers one entry at a time, and each
  entry is spelled the way the C++ compiler stores it,
  '_ZN6QTimer5startEv', which no person can read. Code that calls into
  the shared object needs that stored spelling; a person choosing what to
  call needs the readable one, 'QTimer::start()'. Both must travel
  together, along with what else the entry says: what kind of thing it
  is, where it starts, and which version of the library it belongs to.
  An entry describes a file on disk, so nothing may change it once read.

  Implementation
  --------------

  '__init__' stores the five values in slots through
  'object.__setattr__'; setting or deleting an attribute afterwards
  raises 'AttributeError'. Two symbols are equal when all five values
  are, and hash accordingly.

  Attributes
  ----------

  mangled : str
    The spelling stored in the file, the one 'ctypes' looks up.

  readable : str
    The same name as C++ source writes it. A name that is no C++ name,
    such as 'qVersion', reads the same in both spellings.

  kind : str
    The letter 'nm' prints for the entry: 'T' for a function, and 'D',
    'R' or 'B' for data.

  position : int
    Where the entry starts once the file is in memory, counted in bytes
    from the start of the file's place there.

  version : str
    The version tag of the entry, as 'Qt_6', or '' when it has none.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  __slots__ = ('mangled', 'readable', 'kind', 'position', 'version')

  #  The letters 'nm' prints for an entry that is code.
  __function_kinds__ = ('T', 't', 'W', 'w', 'i')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _getValues(self) -> tuple:
    return (
        self.mangled, self.readable, self.kind, self.position,
        self.version,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __setattr__(self, name: str, value: Any) -> Never:
    infoSpec = """A Symbol describes a file on disk and cannot be changed:
    '%s' was not set."""
    raise AttributeError(' '.join((infoSpec % name).split()))

  def __delattr__(self, name: str) -> Never:
    infoSpec = """A Symbol describes a file on disk and cannot be changed:
    '%s' was not deleted."""
    raise AttributeError(' '.join((infoSpec % name).split()))

  def __eq__(self, other: object) -> bool:
    if not isinstance(other, Symbol):
      return NotImplemented
    return self._getValues() == other._getValues()

  def __hash__(self) -> int:
    return hash(self._getValues())

  def __str__(self) -> str:
    return self.readable

  def __repr__(self) -> str:
    infoSpec = """<%s '%s' stored as '%s'>"""
    return infoSpec % (type(self).__name__, self.readable, self.mangled)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __init__(
      self,
      mangled: str,
      readable: str,
      kind: str,
      position: int,
      version: str,
  ) -> None:
    object.__setattr__(self, 'mangled', mangled)
    object.__setattr__(self, 'readable', readable)
    object.__setattr__(self, 'kind', kind)
    object.__setattr__(self, 'position', position)
    object.__setattr__(self, 'version', version)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isFunction(self) -> bool:
    """Whether the entry is code that can be run, and not data."""
    return self.kind in self.__function_kinds__
