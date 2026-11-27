"""System says what differs between the operating systems."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os

import sys
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Optional, Tuple

  Paths = Tuple[str, ...]


class System:
  """
  Says what differs from one operating system to the next when ritual
  files are compiled and the result is opened. 'Summon', 'Rituals' and
  the judge of the trials ask it, so none of them names a system.

    system = System.getHere()
    system.getQtFileName('QtCore')   # 'libQt6Core.so.6' on Linux

  Terms
  -----

  - A part of Qt is one of the libraries Qt is divided into, named as
    its header folder is: 'QtCore', 'QtGui', 'QtWidgets'.
  - A built file is what 'clang++' makes from our C++: the shared object
    of rituals, or the C++ half of a trial.

  You provide
  -----------

  Nothing. 'System.getHere()' gives the one object for the system this
  Python runs on. It is a 'Linux', a 'MacOS' or a 'Windows'; each of the
  three is a class in a file of its own, and each has a docstring
  saying what its system is like.

  What every system answers
  -------------------------

  - 'getQtFileName': which file of Qt the linker is handed for one part
    of Qt.
  - 'getQtStaticFileName' and 'getQtPrlFileName': the file of a part
    Qt builds as a static library, as ActiveQt's 'QtAxContainer', and
    the file in which Qt lists what that library needs beside it.
  - 'getCompilerFlags': what 'clang++' is told there besides what it is
    told everywhere.
  - 'getLinkerFlags': how a missing name is refused, and how a built
    file is told where its Qt is.
  - 'prepareOpening': what has to be done in Python before a built file
    is opened.

  What to expect
  --------------

  - On any other system 'getHere' raises 'NotImplementedError', with
    the name Python has for that system.
  - 'isQtStaticLibrary' and 'readStaticDependencies' are the same on
    every system: whether Qt builds a part as a static library, and
    what such a library needs on the line that joins a built file, as
    its '.prl' file says them.
  - 'System' itself answers none of the others: asked of it and not of a
    'Linux', a 'MacOS' or a 'Windows', each raises 'NotImplementedError'.
  - To teach cutienator a new system, write one more subclass in a file
    of its own, with '__platform_name__' set to what 'sys.platform' is
    there, and import it in the '__init__' of this package.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  What 'sys.platform' is on the system a subclass is for, as 'linux'.
  __platform_name__ = None  # type: Optional[str]

  #  The one object for the system this Python runs on, or None until
  #  the first call of 'getHere'.
  __system_here__ = None  # type: Optional[System]

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _createHere(cls) -> None:
    """Makes the object of the subclass whose system Python runs on."""
    for system in System.__subclasses__():
      if system.__platform_name__ == sys.platform:
        System.__system_here__ = system()
        return
    infoSpec = """cutienator can build on Linux, on macOS and on Windows.
    This Python says its system is '%s', and no subclass of 'System' is
    written for that."""
    raise NotImplementedError(' '.join((infoSpec % sys.platform).split()))

  @classmethod
  def getHere(cls, **kwargs) -> System:
    """
    Gives the object that answers for the system this Python runs on.

    Found for you: the first call looks at 'sys.platform' and makes the
    one object, which is kept for every later call. Call it on 'System'
    with no arguments; the keyword is for the method's own use.

    Returns
    -------

    System
      A 'Linux', a 'MacOS' or a 'Windows'.

    Raises
    ------

    NotImplementedError
      Python runs on a system that none of the three is written for.
    """
    if System.__system_here__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      cls._createHere()
      return cls.getHere(_recursion=True)
    return System.__system_here__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which system the object answers for, as '<Linux>'."""
    return '<%s>' % type(self).__name__

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _refuse(self, methodName: str) -> NotImplementedError:
    """Gives the error for a question that only a subclass answers."""
    infoSpec = """'%s.%s' is answered by 'Linux', 'MacOS' and 'Windows',
    each for its own system. Ask the object 'System.getHere()' gives."""
    info = infoSpec % (type(self).__name__, methodName)
    return NotImplementedError(' '.join(info.split()))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @abstractmethod
  def getQtFileName(self, part: str) -> str:
    """
    Gives the file of Qt that the linker is handed for one part of Qt.

    Parameters
    ----------

    part : str
      The part of Qt, as 'QtCore'.

    Returns
    -------

    str
      The path of the file from the folder where Qt keeps its shared
      objects, which 'Summon.getQtSharedObjectFolder' gives.
    """
    raise self._refuse('getQtFileName')

  @abstractmethod
  def getQtStaticFileName(self, part: str) -> str:
    """
    Gives the file of a part of Qt that Qt builds as a static library,
    as ActiveQt's 'QtAxContainer', in the folder where Qt keeps its
    shared objects.

    Parameters
    ----------

    part : str
      The part of Qt, as 'QtAxContainer'.

    Returns
    -------

    str
      The path of the file from that folder.
    """
    raise self._refuse('getQtStaticFileName')

  @abstractmethod
  def getQtPrlFileName(self, part: str) -> str:
    """
    Gives the file in which Qt lists, for one part, whether it is a
    static library and what it needs beside it: its '.prl' file, in the
    folder where Qt keeps its shared objects.

    Parameters
    ----------

    part : str
      The part of Qt, as 'QtAxContainer'.

    Returns
    -------

    str
      The path of the file from that folder.
    """
    raise self._refuse('getQtPrlFileName')

  def _readPrlFile(self, qtFolder: str, part: str) -> Dict[str, str]:
    """Gives each line of the '.prl' file of a part as its key and its
    value, as 'QMAKE_PRL_CONFIG' and 'static'; empty for a part with no
    '.prl' file."""
    path = os.path.join(qtFolder, self.getQtPrlFileName(part))
    if not os.path.isfile(path):
      return {}
    values = {}  # type: Dict[str, str]
    with open(path, encoding='utf-8') as file:
      for line in file:
        key, _, value = line.partition('=')
        values[key.strip()] = value.strip()
    return values

  def isQtStaticLibrary(self, qtFolder: str, part: str) -> bool:
    """
    Says whether Qt builds a part as a static library, as ActiveQt's
    'QtAxServer' on Windows: its '.prl' file says 'static' under
    'QMAKE_PRL_CONFIG'. On Windows the static library has the name the
    list of a DLL has, so the name of the file cannot tell.

    Parameters
    ----------

    qtFolder : str
      The folder where Qt keeps its shared objects.

    part : str
      The part of Qt, as 'QtAxServer'.

    Returns
    -------

    bool
      False for a part with no '.prl' file, and for one Qt builds as a
      shared object.
    """
    values = self._readPrlFile(qtFolder, part)
    config = values.get('QMAKE_PRL_CONFIG', '').split()
    return True if 'static' in config else False

  def readStaticDependencies(self, qtFolder: str, part: str) -> Paths:
    """
    Gives what the line joining a built file needs beside a part of Qt
    that Qt builds as a static library: the libraries its own code
    calls into, which a shared object would bring by itself and a
    static library does not.

    Qt writes them in the part's '.prl' file: 'QMAKE_PRL_CONFIG' holds
    'static' for a static library, and 'QMAKE_PRL_LIBS' the words, as
    '$$[QT_INSTALL_LIBS]/Qt6AxBase.lib -lole32' on Windows, where
    '$$[QT_INSTALL_LIBS]' stands for the folder of Qt's shared objects.

    Parameters
    ----------

    qtFolder : str
      The folder where Qt keeps its shared objects.

    part : str
      The part of Qt, as 'QtAxContainer'.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry, '-framework' and its
      name as two. Empty for a part with no '.prl' file, and for one Qt
      builds as a shared object.
    """
    if not self.isQtStaticLibrary(qtFolder, part):
      return ()
    values = self._readPrlFile(qtFolder, part)
    libraries = values.get('QMAKE_PRL_LIBS', '')
    words = libraries.replace('$$[QT_INSTALL_LIBS]', qtFolder).split()
    return (*words,)

  @abstractmethod
  def getCompilerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what 'clang++' is told on this system besides what it is told
    on every system.

    Parameters
    ----------

    qtFolder : str
      The folder where Qt keeps its shared objects. Only macOS has a use
      for it here.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry.
    """
    raise self._refuse('getCompilerFlags')

  def getPrivateFolders(
      self,
      headerFolder: str,
      qtFolder: str,
      version: str,
      part: str,
  ) -> Paths:
    """
    Gives the folders 'clang++' has to look in for the headers of one
    part of Qt that Qt calls private. Qt means by the word that it may
    change them without telling; cutienator takes them all the same.

    Parameters
    ----------

    headerFolder : str
      The folder where Qt keeps its headers.

    qtFolder : str
      The folder where Qt keeps its shared objects. Only macOS has a use
      for it here.

    version : str
      The version of Qt, as '6.12.0': Qt keeps these headers in a folder
      of that name.

    part : str
      The part of Qt, as 'QtCore'.

    Returns
    -------

    Paths
      Four folders, as '/usr/include/qt6/QtCore',
      '/usr/include/qt6/QtCore/6.12.0',
      '/usr/include/qt6/QtCore/6.12.0/QtCore' and the folder 'private'
      in that one: a header names another as '"qglobal.h"', as
      '<private/qobject_p.h>', as '<QtCore/private/qobject_p.h>' or
      barely as '"qobject_p.h"'.
    """
    partFolder = os.path.join(headerFolder, part)
    inner = os.path.join(partFolder, version, part)
    return (
        partFolder, os.path.join(partFolder, version), inner,
        os.path.join(inner, 'private'),
    )

  @abstractmethod
  def getLinkerFlags(self, qtFolder: str) -> Paths:
    """
    Gives what the linker is told on this system: to refuse a name that
    no Qt shared object offers, and where the built file is to look for
    its Qt once a program opens it.

    Parameters
    ----------

    qtFolder : str
      The folder where Qt keeps its shared objects.

    Returns
    -------

    Paths
      A 'Tuple[str, ...]', one argument per entry.
    """
    raise self._refuse('getLinkerFlags')

  @abstractmethod
  def buildsObjectiveC(self) -> bool:
    """
    Says whether a ritual file of Objective-C++, ending in '.mm', is
    built on this system. Qt writes some of its code for Apple's systems
    only in that language, and a ritual file carrying a copy of it can
    be compiled there only; elsewhere it is passed over, and its rituals
    raise when called, as those of a part the machine's Qt lacks do.
    """
    raise self._refuse('buildsObjectiveC')

  @abstractmethod
  def prepareOpening(self, *qtFiles: str) -> None:
    """
    Does what this system needs done in Python before a built file can
    be opened and find its Qt. 'Rituals' calls it right before it opens
    the shared object of rituals of a part.

    Parameters
    ----------

    *qtFiles : str
      The full path of the Qt shared object of the part, and of each
      part it sees first, found where 'Summon.getQtSharedObjectFolder'
      says Qt is.
    """
    raise self._refuse('prepareOpening')

  @abstractmethod
  def getUsualQtFolders(self) -> Paths:
    """
    Gives the folders where a usual install of Qt keeps its shared
    objects on this system, in the order they are looked in when
    'qmake6' is not there to say; see
    'Summon.getQtSharedObjectFolder'. A folder that is not there is not
    given.
    """
    raise self._refuse('getUsualQtFolders')

  @staticmethod
  def _findInstallerFolders(kitName: str, *roots: str) -> Paths:
    """
    Gives the folders Qt's own installer puts a Qt into, as
    '~/Qt/6.12.0/gcc_64', for one kit of Qt: under each root, each
    version that is there, the newest first.
    """
    found = []  # type: List[str]
    for root in roots:
      root = os.path.expanduser(root)
      if not os.path.isdir(root):
        continue
      versions = []
      for name in os.listdir(root):
        pieces = name.split('.')
        if all(piece.isdigit() for piece in pieces):
          folder = os.path.join(root, name, kitName)
          if os.path.isdir(folder):
            versions.append(((*(int(p) for p in pieces),), folder))
      found.extend(folder for _, folder in sorted(versions, reverse=True))
    return (*found,)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
