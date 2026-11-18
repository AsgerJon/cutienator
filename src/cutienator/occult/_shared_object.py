"""SharedObject reads the list of names a shared object offers."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
from typing import TYPE_CHECKING

from . import Symbol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Iterator, Tuple, Union

  Path = Union[str, os.PathLike]
  Symbols = Tuple[Symbol, ...]
  Parsed = Tuple[int, str, str, str]


class SharedObject:
  """
  A shared object, such as '/usr/lib/libQt6Core.so.6', offers thousands
  of functions, but Python can only look one up by a name it already
  knows, in the spelling the C++ compiler stored, and cannot ask the file
  what it holds. Code binding Qt must be able to list everything a file
  offers, find an entry by the name a person would write,
  'QTimer::start()', and get from it the stored spelling 'ctypes' needs.
  One readable name may belong to several entries, as C++ stores more
  than one function for a constructor; choosing among them silently
  would call the wrong one, so such a lookup must fail and show them.

  Implementation
  --------------

  '__init__' runs the program 'nm' on the file for its list, then the
  program 'c++filt' once for the readable spelling of every name. Both
  come with the compiler tools of the system. Each line of the list
  becomes a 'Symbol', kept in the order 'nm' gave. A name starting with
  '_Z' is a C++ name, and one 'c++filt' gives back unchanged is refused.
  Nothing is read again afterwards, so a file replaced on disk needs a
  new instance.

  Attributes
  ----------

  path : str
    The path of the file, as given.

  Raises
  ------

  FileNotFoundError
    The file does not exist, or 'nm' or 'c++filt' is not installed.

  RuntimeError
    One of the two programs failed, as 'nm' does for a file that is no
    shared object.

  ValueError
    A program gave output of an unexpected shape, or 'c++filt' could not
    read a C++ name.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _run(*command: str, **kwargs: Any) -> str:
    """
    Runs a program and gives what it printed.

    Parameters
    ----------

    *command : str
      The program, then its arguments.

    **kwargs
      feed : str, optional
        Text for the program to read.

    Returns
    -------

    str
      What the program printed.

    Raises
    ------

    FileNotFoundError
      The program is not installed.

    RuntimeError
      The program reported a failure.
    """
    try:
      done = subprocess.run(
          command, input=kwargs.get('feed'), capture_output=True,
          text=True,
      )
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program '%s' is needed and is not installed."""
      raise FileNotFoundError(infoSpec % command[0]) from fileNotFoundError
    if done.returncode:
      infoSpec = """The program '%s' failed: %s"""
      raise RuntimeError(infoSpec % (command[0], done.stderr.strip()))
    return done.stdout

  @staticmethod
  def _parseLine(line: str) -> Parsed:
    """
    Takes apart one line of the list 'nm' prints.

    Parameters
    ----------

    line : str
      A line such as '0000000000208140 T _ZN6QTimer5startEv@@Qt_6'.

    Returns
    -------

    Parsed
      A 'tuple[int, str, str, str]' of the position, the kind letter, the
      stored spelling and the version tag, which is '' when absent.

    Raises
    ------

    ValueError
      The line does not have exactly three fields.
    """
    fields = line.split()
    if len(fields) != 3:
      infoSpec = """Expected a position, a kind and a name from 'nm', but
      received the line: '%s'"""
      raise ValueError(' '.join((infoSpec % line).split()))
    position, kind, name = fields
    mangled, _, version = name.partition('@')
    return int(position, 16), kind, mangled, version.lstrip('@')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __listed_symbols__ = None
  __by_readable__ = None

  #  Public Variables
  path = None

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __len__(self) -> int:
    return len(self.__listed_symbols__)

  def __iter__(self) -> Iterator[Symbol]:
    yield from self.__listed_symbols__

  def __contains__(self, readable: object) -> bool:
    return readable in self.__by_readable__

  def __getitem__(self, readable: str) -> Symbol:
    """
    Gives the one entry whose readable spelling is exactly 'readable'.

    Parameters
    ----------

    readable : str
      The name as C++ source writes it, as 'QTimer::start()'.

    Returns
    -------

    Symbol
      The entry.

    Raises
    ------

    LookupError
      The file offers no entry of that name, or several; the several
      are listed, and 'named' gives them all.
    """
    found = self.named(readable)
    if not found:
      infoSpec = """'%s' offers nothing named '%s'."""
      raise LookupError(infoSpec % (self.path, readable))
    if len(found) > 1:
      stored = ', '.join(symbol.mangled for symbol in found)
      infoSpec = """'%s' offers %d entries named '%s', stored as: %s. The
      method 'named' gives them all."""
      info = infoSpec % (self.path, len(found), readable, stored)
      raise LookupError(' '.join(info.split()))
    return found[0]

  def __str__(self) -> str:
    infoSpec = """<%s '%s' offering %d names>"""
    return infoSpec % (type(self).__name__, self.path, len(self))

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __init__(self, path: Path) -> None:
    path = os.fspath(path)
    if not os.path.isfile(path):
      infoSpec = """There is no file at '%s'."""
      raise FileNotFoundError(infoSpec % path)
    listed = self._run('nm', '-D', '--defined-only', path).splitlines()
    parsed = [self._parseLine(line) for line in listed]
    feed = ''.join('%s\n' % mangled for _, _, mangled, _ in parsed)
    readables = self._run('c++filt', feed=feed).splitlines()
    if len(readables) != len(parsed):
      infoSpec = """'c++filt' received %d names from '%s' and gave back
      %d."""
      info = infoSpec % (len(parsed), path, len(readables))
      raise ValueError(' '.join(info.split()))
    symbols, byReadable = [], dict()
    for (position, kind, mangled, version), readable in zip(
        parsed, readables,
    ):
      if mangled.startswith('_Z') and readable == mangled:
        infoSpec = """'c++filt' could not read the C++ name '%s' offered
        by '%s'."""
        raise ValueError(' '.join((infoSpec % (mangled, path)).split()))
      symbol = Symbol(mangled, readable, kind, position, version)
      symbols.append(symbol)
      byReadable.setdefault(readable, []).append(symbol)
    self.path = path
    self.__listed_symbols__ = (*symbols,)
    self.__by_readable__ = {
        readable: (*found,) for readable, found in byReadable.items()
    }

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

  def named(self, readable: str) -> Symbols:
    """Gives every entry whose readable spelling is exactly 'readable'."""
    return self.__by_readable__.get(readable, ())

  def search(self, text: str) -> Symbols:
    """Gives every entry whose readable spelling contains 'text'."""
    return (*(s for s in self.__listed_symbols__ if text in s.readable),)

  def functions(self) -> Symbols:
    """Gives every entry that is a function, leaving out the data."""
    return (*(s for s in self.__listed_symbols__ if s.isFunction()),)
