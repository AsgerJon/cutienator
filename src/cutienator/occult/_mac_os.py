"""MacOS says how ritual files are compiled and opened on macOS."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os

from typing import TYPE_CHECKING

from . import System

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple

  Paths = Tuple[str, ...]


class MacOS(System):
  """
  Answers for macOS what 'System' asks of every system, on Apple
  silicon and on Intel chips alike.

  You do not make one: 'System.getHere()' gives it when Python runs on
  macOS, and 'Summon', 'Rituals' and the judge of the trials ask it.

  What macOS is like
  ------------------

  - Qt keeps each of its parts in a folder of its own, called a
    framework, as 'QtCore.framework'. The shared object lies inside it
    and has no ending: 'QtCore.framework/Versions/A/QtCore'. The same
    file serves both kinds of chip.
  - The headers of a part lie inside its framework as well. Qt's header
    folder holds only a stand-in for each, one line long, that sends
    the compiler on to the header of that name in a framework. So the
    compiler has to be told the folder of the frameworks too.
  - A built file can carry the folder of the Qt it was built against,
    as on Linux, so nothing has to be done in Python before the file is
    opened.
  - 'clang++' is Apple's own there, and its linker has other words for
    some things than the one on Linux.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What 'sys.platform' is on macOS.
  __platform_name__ = 'darwin'

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
    Gives the shared object of one part of Qt, which on macOS lies inside
    the framework of the part: 'QtCore.framework/Versions/A/QtCore' for
    'QtCore'.
    """
    return '%s.framework/Versions/A/%s' % (part, part)

  def getQtStaticFileName(self, part: str) -> str:
    """Gives the static library of one part of Qt, which on macOS is
    no framework: 'libQt6AxContainer.a' for 'QtAxContainer'."""
    return 'lib%s.a' % part.replace('Qt', 'Qt6', 1)

  def getQtPrlFileName(self, part: str) -> str:
    """Gives the '.prl' file of one part of Qt, as 'libQt6Core.prl'
    for 'QtCore', beside the frameworks."""
    return 'lib%s.prl' % part.replace('Qt', 'Qt6', 1)

  def getCompilerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what 'clang++' is told on macOS: what it is told on Linux, and
    where the frameworks are.

    Returns
    -------

    Paths
      '-fPIC', so the code can sit at any address;
      '-fvisibility=hidden' and '-fvisibility-inlines-hidden', so the
      built file offers only the rituals, and nothing of Qt's own;
      '-F' with the folder of Qt's shared objects, which on macOS is the
      folder of the frameworks, so that 'QtCore/qobject.h' is found
      inside 'QtCore.framework'. Without it the compiler finds only the
      stand-in of that name in Qt's header folder, which sends it on to
      the framework and nowhere else.
    """
    return (
        '-fPIC', '-fvisibility=hidden', '-fvisibility-inlines-hidden',
        '-F%s' % qtFolder,
    )

  def getPrivateFolders(
      self,
      headerFolder: str,
      qtFolder: str,
      version: str,
      part: str,
  ) -> Paths:
    """
    Gives the folders 'clang++' has to look in for the headers of one
    part of Qt that Qt calls private. On macOS they lie inside the
    framework of the part, as
    'QtCore.framework/Headers/6.12.0/QtCore/private'. A part Qt builds
    as a static library has no framework: its headers lie in Qt's
    header folder, as they do on Linux and Windows, as those of
    'QtFreetype', FreeType as Qt carries it, in 'include/QtFreetype'.
    """
    partFolder = os.path.join(
        qtFolder, '%s.framework' % part, 'Headers')
    if not os.path.isdir(partFolder):
      return System.getPrivateFolders(
          self, headerFolder, qtFolder, version, part)
    inner = os.path.join(partFolder, version, part)
    return (
        partFolder, os.path.join(partFolder, version), inner,
        os.path.join(inner, 'private'),
    )

  def getLinkerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what the linker is told on macOS.

    Returns
    -------

    Paths
      '-Wl,-rpath,' with the folder of Qt's shared objects, so the built
      file opens the Qt it was built against. Qt's shared objects on macOS
      name themselves from that folder on, as
      'QtCore.framework/Versions/A/QtCore', so it is that folder and not
      the framework that the built file has to carry.

    Nothing more: Apple's linker refuses a function no Qt shared object
    offers by itself, what '-Wl,--no-undefined' asks on Linux, and
    warns that its own word for it, '-undefined error', is deprecated.
    """
    return ('-Wl,-rpath,%s' % qtFolder,)

  def prepareOpening(self) -> None:
    """
    Does nothing: on macOS the built file carries the folder of its Qt,
    which 'getLinkerFlags' had the linker write into it.
    """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
