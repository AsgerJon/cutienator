"""Windows says how ritual files are compiled and opened on Windows."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

from . import System, Summon

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Tuple

  Paths = Tuple[str, ...]


class Windows(System):
  """
  Answers for Windows what 'System' asks of every system. The Qt it
  knows is the kind built with Microsoft's Visual Studio, in the folder
  'msvc2022_64' of a Qt installation, and 'clang++' must be one that
  builds for Visual Studio, which needs Visual Studio installed.

  The two must fit together: the C++ library of a Visual Studio refuses
  a 'clang++' that is too old for it, and says which it wants, as
  "expected Clang 22 or newer" from Visual Studio 2026. A build then
  fails with those words. The 'clang++' that the installer of Visual
  Studio offers always fits, since Microsoft keeps it in step with that
  library. It lies in 'VC/Tools/Llvm/x64/bin' of the Visual Studio
  folder, and it is the one used when that folder comes first in
  'PATH'.

  You do not make one: 'System.getHere()' gives it when Python runs on
  Windows, and 'Summon', 'Rituals' and the judge of the trials ask it.

  What Windows is like
  --------------------

  - A shared object is called a DLL there. Qt keeps the DLL of each of
    its parts with its programs, as 'Qt6Core.dll' beside 'qmake6.exe'.
  - The linker is not handed the DLL. It is handed a second file that
    lists what the DLL offers, as 'Qt6Core.lib', and that one lies in
    the folder where the other systems keep the shared object.
  - A DLL offers only the functions marked for it. Every ritual carries
    that mark, Qt's 'Q_DECL_EXPORT', which changes nothing on the other
    systems.
  - A DLL cannot carry the folder of the Qt it was built against. Python
    has to be told that folder before the built file is opened, which
    is what 'prepareOpening' does.
  - The target files keep their names, as 'libcutienator_QtCore.so'.
    Windows opens a DLL of any name.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What 'sys.platform' is on Windows, also on a 64-bit one.
  __platform_name__ = 'win32'

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
    Gives the file the linker is handed for one part of Qt, as
    'Qt6Core.lib' for 'QtCore'. It is not the DLL: it lists what the DLL
    offers, and it lies right in the folder where Qt keeps its shared
    objects on the other systems.
    """
    return '%s.lib' % part.replace('Qt', 'Qt6', 1)

  def getQtStaticFileName(self, part: str) -> str:
    """Gives the static library of one part of Qt, which on Windows
    has the name the list of a DLL has: 'Qt6AxContainer.lib' for
    'QtAxContainer'. Its '.prl' file tells the two apart."""
    return '%s.lib' % part.replace('Qt', 'Qt6', 1)

  def getQtPrlFileName(self, part: str) -> str:
    """Gives the '.prl' file of one part of Qt, as 'Qt6Core.prl' for
    'QtCore'."""
    return '%s.prl' % part.replace('Qt', 'Qt6', 1)

  def getCompilerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what 'clang++' is told on Windows. The folder of Qt's shared
    objects is of no use for it.

    Returns
    -------

    Paths
      '-fms-runtime-lib=dll', so the built file uses the C++ runtime
      library Qt uses, which is a DLL of Microsoft's, and brings no
      second copy of it built into the file. The two have to be one,
      since what a ritual makes with 'new', Qt may delete.
      '-DNOMINMAX', as Qt tells the compiler for everything it builds
      on Windows ('PlatformCommonInternal' in Qt's
      'QtInternalTargets.cmake'): without it 'windows.h' makes 'min'
      and 'max' macros, and the code taken from Qt's source, as
      'std::numeric_limits<quint64>::max()', no longer compiles.

    Left out, though the other systems are told them: '-fPIC', which
    'clang++' refuses for Windows, where code can sit at any address as
    it is; and the two '-fvisibility' flags, since a DLL offers only
    what is marked for it anyway.
    """
    return ('-fms-runtime-lib=dll', '-DNOMINMAX')

  def getLinkerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what the linker is told on Windows, which is nothing. It
    refuses a name that no Qt shared object offers without being told,
    and a DLL cannot carry the folder of its Qt: 'prepareOpening' sees
    to that when the built file is opened.
    """
    return ()

  def prepareOpening(self) -> None:
    """
    Tells Python where the DLLs of Qt are, so that the built file finds
    the Qt it was built against once it is opened.

    The folder is the one where Qt keeps its programs, which
    'Summon.getQtProgramFolder' asks 'qmake6' for. From Python 3.8 on,
    Python looks for the DLLs a DLL needs only in folders it was told
    of, and 'os.add_dll_directory' tells it. Python 3.7 has no such
    function and looks through the folders of 'PATH' instead, so there
    the folder is put first in 'PATH' for this Python and the programs
    it starts.

    Raises
    ------

    FileNotFoundError
      'qmake6' is not installed.
    """
    folder = os.path.normpath(Summon.getQtProgramFolder())
    if sys.version_info >= (3, 8):
      os.add_dll_directory(folder)
    else:
      known = os.environ.get('PATH', '')
      os.environ['PATH'] = os.pathsep.join((folder, known))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
