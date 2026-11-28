"""
QLibraryInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlibraryinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLibraryInfoPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QLibraryInfo, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSettings, QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLibraryInfoPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLibraryInfoPrivate: a plain Python object standing
  in front of one C++ QLibraryInfoPrivate.

  C++ hands a QLibraryInfoPrivate around as a copy, so every C++
  QLibraryInfoPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLibraryInfoPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'configuration',
  'setQtconfManualPath', 'expandEnvVariables', 'reload', 'locationInfo',
  'path', 'paths', 'qtConfPaths', 'appPaths', 'qtPaths'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLibraryInfoPrivate::~QLibraryInfoPrivate()': the destructor:
    Python removes its C++ QLibraryInfoPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLibraryInfoPrivate is created at the first use, not by
    'QLibraryInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLibraryInfoPrivate back gives a copy the ritual made
    for Python, in a new cute QLibraryInfoPrivate.
  """

  #  The classes Qt writes inside QLibraryInfoPrivate, each a class in here
  #  as in C++.

  class LocationInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLibraryInfoPrivate::LocationInfo: a plain Python
    object standing in front of one C++ QLibraryInfoPrivate::LocationInfo.

    C++ hands a QLibraryInfoPrivate::LocationInfo around as a copy, so every
    C++ QLibraryInfoPrivate::LocationInfo behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QLibraryInfoPrivate::LocationInfo yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLibraryInfoPrivate::LocationInfo::~LocationInfo()': the
      destructor: Python removes its C++ QLibraryInfoPrivate::LocationInfo by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QLibraryInfoPrivate::LocationInfo is created at the first use,
      not by 'QLibraryInfoPrivate::LocationInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLibraryInfoPrivate::LocationInfo back gives a copy
      the ritual made for Python, in a new cute
      QLibraryInfoPrivate::LocationInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLibraryInfoPrivate::LocationInfo'

    #  Qt's '~QLibraryInfoPrivate::LocationInfo()'. Naming it makes this a
    #  value class: Python owns every C++ QLibraryInfoPrivate::LocationInfo
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QLibraryInfoPrivate12LocationInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def configuration() -> Optional[QSettings]:
    """
    Calls Qt's 'QSettings *QLibraryInfoPrivate::configuration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfoprivate.html#configuration

    Returns
    -------

    Optional[QSettings]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSettings *QLibraryInfoPrivate::configuration()
    address = Rituals.call('ritual_ZN19QLibraryInfoPrivate13configurationEv')
    from . import QSettings
    return QSettings._cuteAt(address)

  @staticmethod
  @overload(QString)
  @overload(NoneType)
  def setQtconfManualPath(qtconfManualPath: Optional[QString]) -> None:
    """
    Calls Qt's 'void QLibraryInfoPrivate::setQtconfManualPath(const QString
    *qtconfManualPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfoprivate.html#setQtconfManualPath

    Parameters
    ----------

    qtconfManualPath : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLibraryInfoPrivate::setQtconfManualPath(const QString
    #      *qtconfManualPath)
    Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate19setQtconfManualPathEPK7QString',
        CuteMixin._addressOf(qtconfManualPath),
    )

  @staticmethod
  @overload(str)
  def expandEnvVariables(path: str) -> str:
    """
    Calls Qt's 'QString QLibraryInfoPrivate::expandEnvVariables(QString
    path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfoprivate.html#expandEnvVariables

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibraryInfoPrivate::expandEnvVariables(QString path)
    return Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate18expandEnvVariablesE7QString', path,
    )

  @staticmethod
  def reload() -> None:
    """
    Calls Qt's 'void QLibraryInfoPrivate::reload()'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfoprivate.html#reload
    """
    #  void QLibraryInfoPrivate::reload()
    Rituals.call('ritual_ZN19QLibraryInfoPrivate6reloadEv')

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def locationInfo(loc: QLibraryInfo.LibraryPath) -> LocationInfo:
    """
    Calls Qt's 'LocationInfo
    QLibraryInfoPrivate::locationInfo(QLibraryInfo::LibraryPath loc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfoprivate.html#locationInfo

    Parameters
    ----------

    loc : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    LocationInfo
      A new cute QLibraryInfoPrivate::LocationInfo around the copy Qt gave
      back. Python owns it.
    """
    #  LocationInfo
    #      QLibraryInfoPrivate::locationInfo(QLibraryInfo::LibraryPath loc)
    address = Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate12locationInfoEN12QLibraryInfo11Libr'
        'aryPathE',
        loc.value,
    )
    return QLibraryInfoPrivate.LocationInfo._cuteOwning(address)

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def path(p: QLibraryInfo.LibraryPath) -> str:
    """
    Calls Qt's 'QString QLibraryInfoPrivate::path(QLibraryInfo::LibraryPath
    p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfoprivate.html#path

    Parameters
    ----------

    p : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLibraryInfoPrivate::path(QLibraryInfo::LibraryPath p)
    return Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate4pathEN12QLibraryInfo11LibraryPathE',
        p.value,
    )

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def paths(p: QLibraryInfo.LibraryPath) -> QStringList:
    """
    Calls Qt's 'QStringList
    QLibraryInfoPrivate::paths(QLibraryInfo::LibraryPath p)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfoprivate.html#paths

    Parameters
    ----------

    p : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfoPrivate::paths(QLibraryInfo::LibraryPath p)
    address = Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate5pathsEN12QLibraryInfo11LibraryPathE',
        p.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def qtConfPaths(location: QLibraryInfo.LibraryPath) -> QStringList:
    """
    Calls Qt's 'QStringList
    QLibraryInfoPrivate::qtConfPaths(QLibraryInfo::LibraryPath location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlibraryinfoprivate.html#qtConfPaths

    Parameters
    ----------

    location : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfoPrivate::qtConfPaths(QLibraryInfo::LibraryPath
    #      location)
    address = Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate11qtConfPathsEN12QLibraryInfo11Libra'
        'ryPathE',
        location.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def appPaths(location: QLibraryInfo.LibraryPath) -> QStringList:
    """
    Calls Qt's 'QStringList
    QLibraryInfoPrivate::appPaths(QLibraryInfo::LibraryPath location)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfoprivate.html#appPaths

    Parameters
    ----------

    location : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfoPrivate::appPaths(QLibraryInfo::LibraryPath
    #      location)
    address = Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate8appPathsEN12QLibraryInfo11LibraryPa'
        'thE',
        location.value,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QLibraryInfo.LibraryPath)
  def qtPaths(location: QLibraryInfo.LibraryPath) -> QStringList:
    """
    Calls Qt's 'QStringList
    QLibraryInfoPrivate::qtPaths(QLibraryInfo::LibraryPath location)'.

    Qt's own words: https://doc.qt.io/qt-6/qlibraryinfoprivate.html#qtPaths

    Parameters
    ----------

    location : QLibraryInfo.LibraryPath
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QLibraryInfoPrivate::qtPaths(QLibraryInfo::LibraryPath
    #      location)
    address = Rituals.call(
        'ritual_ZN19QLibraryInfoPrivate7qtPathsEN12QLibraryInfo11LibraryPat'
        'hE',
        location.value,
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLibraryInfoPrivate'

  #  Qt's '~QLibraryInfoPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QLibraryInfoPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QLibraryInfoPrivateD1Ev'

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
