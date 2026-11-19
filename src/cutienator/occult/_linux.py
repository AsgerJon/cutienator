"""Linux says how ritual files are compiled and opened on Linux."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple

  Paths = Tuple[str, ...]


class Linux(System):
  """
  Answers for Linux what 'System' asks of every system.

  You do not make one: 'System.getHere()' gives it when Python runs on
  Linux, and 'Build', 'Rituals' and the judge of the trials ask it.

  What Linux is like
  ------------------

  - Qt keeps each of its parts in one shared object, named as
    'libQt6Core.so.6' for 'QtCore'.
  - A built file can carry the folder of the Qt it was built against.
    The linker writes it in, so nothing has to be done in Python before
    the file is opened.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What 'sys.platform' is on Linux.
  __platform_name__ = 'linux'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def getQtFileName(self, part: str) -> str:
    """
    Gives the shared object of one part of Qt, as 'libQt6Core.so.6' for
    'QtCore'. It lies right in the folder where Qt keeps its shared
    objects.
    """
    return 'lib%s.so.6' % part.replace('Qt', 'Qt6', 1)

  def getCompilerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what 'clang++' is told on Linux. The folder of Qt's shared
    objects is of no use for it.

    Returns
    -------

    Paths
      '-fPIC', so the code can sit at any address;
      '-fvisibility=hidden', so the built file offers only what is
      marked for it, which is the rituals. Without it the functions
      the compiler makes from Qt's patterns leave their scrambled
      names in the file;
      '-fvisibility-inlines-hidden', so Qt's inline code leaves none
      either. The first flag does not reach it: Qt marks its classes
      as offered, and that mark covers their inline functions.
    """
    return ('-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden',)

  def getLinkerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what the linker is told on Linux.

    Returns
    -------

    Paths
      '-Wl,--no-undefined', so a ritual calling a function that no Qt
      shared object offers stops the build, and not the first program
      that opens the built file;
      '-Wl,-rpath,' with the folder of Qt's shared objects, so the built
      file opens the Qt it was built against. Without it the built file
      looks only where the machine keeps its own shared objects, as
      '/usr/lib': a Qt installed elsewhere is not found there, and
      another Qt that is there would be opened instead.
    """
    return ('-Wl,--no-undefined', '-Wl,-rpath,%s' % qtFolder,)

  def prepareOpening(self) -> None:
    """
    Does nothing: on Linux the built file carries the folder of its Qt,
    which 'getLinkerFlags' had the linker write into it.
    """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
