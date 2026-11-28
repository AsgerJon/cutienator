"""
QLibraryInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlibraryinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QVersionNumber


class QLibraryInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLibraryInfo: a plain Python object standing in front
  of one C++ QLibraryInfo.

  C++ hands a QLibraryInfo around as a copy, so every C++ QLibraryInfo behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLibraryInfo that has a ritual and that Python can
  call so far, 8 names in all: 'build', 'isDebugBuild', 'isSharedBuild',
  'version', 'path', 'paths', 'location', 'platformPluginArguments'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLibraryInfo::~QLibraryInfo()': the destructor: Python removes its
    C++ QLibraryInfo by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QLibraryInfo is created at the first use, not by
    'QLibraryInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLibraryInfo back gives a copy the ritual made for
    Python, in a new cute QLibraryInfo.
  """

  #  The enums Qt writes inside QLibraryInfo, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LibraryPath(CuteNum):
    """
    The enum 'QLibraryInfo::LibraryPath' of Qt, with the 15 names Qt gives in
    it.
    """

    PrefixPath = Kee[int](0)
    DocumentationPath = Kee[int](1)
    HeadersPath = Kee[int](2)
    LibrariesPath = Kee[int](3)
    LibraryExecutablesPath = Kee[int](4)
    BinariesPath = Kee[int](5)
    PluginsPath = Kee[int](6)
    QmlImportsPath = Kee[int](7)
    Qml2ImportsPath = Kee[int](7)
    ArchDataPath = Kee[int](8)
    DataPath = Kee[int](9)
    TranslationsPath = Kee[int](10)
    ExamplesPath = Kee[int](11)
    TestsPath = Kee[int](12)
    SettingsPath = Kee[int](100)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def build() -> Optional[str]:
    """
    Calls Qt's 'const char *QLibraryInfo::build()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#build

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QLibraryInfo::build()
    chars = Rituals.call('ritual_ZN12QLibraryInfo5buildEv')
    return None if chars is None else chars.decode()

  @staticmethod
  def isDebugBuild() -> bool:
    """
    Calls Qt's 'bool QLibraryInfo::isDebugBuild()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#isDebugBuild
    """
    #  bool QLibraryInfo::isDebugBuild()
    return Rituals.call('ritual_ZN12QLibraryInfo12isDebugBuildEv')

  @staticmethod
  def isSharedBuild() -> bool:
    """
    Calls Qt's 'bool QLibraryInfo::isSharedBuild()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#isSharedBuild
    """
    #  bool QLibraryInfo::isSharedBuild()
    return Rituals.call('ritual_ZN12QLibraryInfo13isSharedBuildEv')

  @staticmethod
  def version() -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QLibraryInfo::version()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#version

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QLibraryInfo::version()
    address = Rituals.call('ritual_ZN12QLibraryInfo7versionEv')
    from . import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  @staticmethod
  @overload(LibraryPath)
  def path(p: LibraryPath) -> str:
    """
    Calls Qt's 'QString QLibraryInfo::path(LibraryPath p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#path

    Parameters
    ----------

    p : LibraryPath
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibraryInfo::path(LibraryPath p)
    return Rituals.call(
        'ritual_ZN12QLibraryInfo4pathENS_11LibraryPathE', p.value,
    )

  @staticmethod
  @overload(LibraryPath)
  def paths(p: LibraryPath) -> QStringList:
    """
    Calls Qt's 'QStringList QLibraryInfo::paths(LibraryPath p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#paths

    Parameters
    ----------

    p : LibraryPath
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfo::paths(LibraryPath p)
    address = Rituals.call(
        'ritual_ZN12QLibraryInfo5pathsENS_11LibraryPathE', p.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(LibraryPath)
  def location(location: LibraryPath) -> str:
    """
    Calls Qt's 'QString QLibraryInfo::location(LibraryLocation location)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#location

    Parameters
    ----------

    location : LibraryPath
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibraryInfo::location(LibraryLocation location)
    return Rituals.call(
        'ritual_ZN12QLibraryInfo8locationENS_11LibraryPathE', location.value,
    )

  @staticmethod
  @overload(str)
  def platformPluginArguments(platformName: str) -> QStringList:
    """
    Calls Qt's 'QStringList QLibraryInfo::platformPluginArguments(const
    QString &platformName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfo.html#platformPluginArguments

    Parameters
    ----------

    platformName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfo::platformPluginArguments(const QString
    #      &platformName)
    address = Rituals.call(
        'ritual_ZN12QLibraryInfo23platformPluginArgumentsERK7QString',
        platformName,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLibraryInfo'

  #  Qt's '~QLibraryInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QLibraryInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLibraryInfoD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLibraryInfo::QLibraryInfo()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfo.html#QLibraryInfo
    """
    #  QLibraryInfo::QLibraryInfo()
    self._noteCreation(QLibraryInfo, lambda: Rituals.call(
        'ritual_ZN12QLibraryInfoC1Ev',
    ))

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
