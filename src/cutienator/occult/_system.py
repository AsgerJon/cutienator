"""System says what differs between the operating systems."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os

import sys
from abc import abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional, Tuple

  Paths = Tuple[str, ...]


class System:
  """
  Says what differs from one operating system to the next when ritual
  files are compiled and the result is opened. 'Build', 'Rituals' and
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
  - 'System' itself answers none of the four: asked of it and not of a
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
      objects, which 'Build.getQtSharedObjectFolder' gives.
    """
    raise self._refuse('getQtFileName')

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
  def prepareOpening(self) -> None:
    """
    Does what this system needs done in Python before a built file can
    be opened and find its Qt. 'Rituals' calls it right before it opens
    the shared object of rituals.
    """
    raise self._refuse('prepareOpening')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
