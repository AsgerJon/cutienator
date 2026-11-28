"""
QStandardPaths binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qstandardpaths.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute
from ..occult import Rituals
from . import QStringList


class QStandardPaths(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStandardPaths: a plain Python object standing in
  front of one C++ QStandardPaths.

  What exists
  -----------

  Every function of Qt's QStandardPaths that has a ritual and that Python can
  call so far, 8 names in all: 'writableLocation', 'standardLocations',
  'locate', 'locateAll', 'displayName', 'findExecutable',
  'setTestModeEnabled', 'isTestModeEnabled'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 5 not a gap.

  What to expect
  --------------

  - The C++ QStandardPaths is created at the first use, not by
    'QStandardPaths(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStandardPaths.
  """

  #  The enums Qt writes inside QStandardPaths, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class LocateOption(CuteFlags):
    """
    The flags enum 'QStandardPaths::LocateOption' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QStandardPaths::LocateOptions'.
    """

    LocateFile = 0x0
    LocateDirectory = 0x1

  LocateOptions = LocateOption

  class StandardLocation(CuteNum):
    """
    The enum 'QStandardPaths::StandardLocation' of Qt, with the 23 names Qt
    gives in it.
    """

    DesktopLocation = Kee[int](0)
    DocumentsLocation = Kee[int](1)
    FontsLocation = Kee[int](2)
    ApplicationsLocation = Kee[int](3)
    MusicLocation = Kee[int](4)
    MoviesLocation = Kee[int](5)
    PicturesLocation = Kee[int](6)
    TempLocation = Kee[int](7)
    HomeLocation = Kee[int](8)
    AppLocalDataLocation = Kee[int](9)
    CacheLocation = Kee[int](10)
    GenericDataLocation = Kee[int](11)
    RuntimeLocation = Kee[int](12)
    ConfigLocation = Kee[int](13)
    DownloadLocation = Kee[int](14)
    GenericCacheLocation = Kee[int](15)
    GenericConfigLocation = Kee[int](16)
    AppDataLocation = Kee[int](17)
    AppConfigLocation = Kee[int](18)
    PublicShareLocation = Kee[int](19)
    TemplatesLocation = Kee[int](20)
    StateLocation = Kee[int](21)
    GenericStateLocation = Kee[int](22)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(StandardLocation)
  def writableLocation(type: StandardLocation) -> str:
    """
    Calls Qt's 'QString QStandardPaths::writableLocation(StandardLocation
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#writableLocation

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::writableLocation(StandardLocation type)
    return Rituals.call(
        'ritual_ZN14QStandardPaths16writableLocationENS_16StandardLocationE',
        type.value,
    )

  @staticmethod
  @overload(StandardLocation)
  def standardLocations(type: StandardLocation) -> QStringList:
    """
    Calls Qt's 'QStringList
    QStandardPaths::standardLocations(StandardLocation type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#standardLocations

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QStandardPaths::standardLocations(StandardLocation type)
    address = Rituals.call(
        'ritual_ZN14QStandardPaths17standardLocationsENS_16StandardLocation'
        'E',
        type.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(StandardLocation, str)
  @overload(StandardLocation, str, LocateOptions)
  def locate(
      type: StandardLocation,
      fileName: str,
      options: LocateOptions = LocateOptions.LocateFile,
  ) -> str:
    """
    Calls Qt's 'QString QStandardPaths::locate(StandardLocation type, const
    QString &fileName, LocateOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#locate

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    options : LocateOptions
      Passed on as its number. May be left out, as in Qt: it is then
      LocateOptions.LocateFile.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::locate(StandardLocation type, const QString
    #      &fileName, LocateOptions options)
    return Rituals.call(
        'ritual_ZN14QStandardPaths6locateENS_16StandardLocationERK7QString6'
        'QFlagsINS_12LocateOptionEE',
        type.value, fileName, options.value,
    )

  @staticmethod
  @overload(StandardLocation, str)
  @overload(StandardLocation, str, LocateOptions)
  def locateAll(
      type: StandardLocation,
      fileName: str,
      options: LocateOptions = LocateOptions.LocateFile,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QStandardPaths::locateAll(StandardLocation type,
    const QString &fileName, LocateOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#locateAll

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    options : LocateOptions
      Passed on as its number. May be left out, as in Qt: it is then
      LocateOptions.LocateFile.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QStandardPaths::locateAll(StandardLocation type, const
    #      QString &fileName, LocateOptions options)
    address = Rituals.call(
        'ritual_ZN14QStandardPaths9locateAllENS_16StandardLocationERK7QStri'
        'ng6QFlagsINS_12LocateOptionEE',
        type.value, fileName, options.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(StandardLocation)
  def displayName(type: StandardLocation) -> str:
    """
    Calls Qt's 'QString QStandardPaths::displayName(StandardLocation type)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#displayName

    Parameters
    ----------

    type : StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::displayName(StandardLocation type)
    return Rituals.call(
        'ritual_ZN14QStandardPaths11displayNameENS_16StandardLocationE',
        type.value,
    )

  @staticmethod
  @overload(str, QStringList)
  def findExecutable(executableName: str, paths: QStringList) -> str:
    """
    Calls Qt's 'QString QStandardPaths::findExecutable(const QString
    &executableName, const QStringList &paths)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandardpaths.html#findExecutable

    Parameters
    ----------

    executableName : str
      Passed on as it is: a QString is made of it for the call.

    paths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStandardPaths::findExecutable(const QString &executableName,
    #      const QStringList &paths)
    return Rituals.call(
        'ritual_ZN14QStandardPaths14findExecutableERK7QStringRK5QListIS0_E',
        executableName, CuteMixin._valueOf(paths),
    )

  @staticmethod
  @overload(bool)
  def setTestModeEnabled(testMode: bool) -> None:
    """
    Calls Qt's 'void QStandardPaths::setTestModeEnabled(bool testMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#setTestModeEnabled

    Parameters
    ----------

    testMode : bool
      Passed on as it is.
    """
    #  void QStandardPaths::setTestModeEnabled(bool testMode)
    Rituals.call('ritual_ZN14QStandardPaths18setTestModeEnabledEb', testMode)

  @staticmethod
  def isTestModeEnabled() -> bool:
    """
    Calls Qt's 'bool QStandardPaths::isTestModeEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandardpaths.html#isTestModeEnabled
    """
    #  bool QStandardPaths::isTestModeEnabled()
    return Rituals.call('ritual_ZN14QStandardPaths17isTestModeEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStandardPaths'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
