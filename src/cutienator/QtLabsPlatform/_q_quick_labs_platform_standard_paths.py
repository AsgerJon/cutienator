"""
QQuickLabsPlatformStandardPaths binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformstandardpaths_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformStandardPaths to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList, QStandardPaths, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl


class QQuickLabsPlatformStandardPaths(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformStandardPaths: a plain Python
  object standing in front of one C++ QQuickLabsPlatformStandardPaths.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformStandardPaths that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject',
  'qmlExtendedNamespace', 'displayName', 'findExecutable', 'locate',
  'locateAll', 'setTestModeEnabled', 'writableLocation'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformStandardPaths::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformStandardPaths::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLabsPlatformStandardPaths::qt_qmlMarker_singleton()':
    one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformStandardPaths::qt_qmlMarker_extendedNamespace()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 20 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'vtable for QQuickLabsPlatformStandardPaths', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 leans on 'QQuickLabsPlatformStandardPaths.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformStandardPaths is created at the first use, not
    by 'QQuickLabsPlatformStandardPaths(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformStandardPaths.
  - Qt tells when it has removed the C++ QQuickLabsPlatformStandardPaths.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformStandardPaths that has no cute
    function yet, '__init__', 'create', 'standardLocations', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformStandardPaths::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformStandardPaths::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QStandardPaths.StandardLocation)
  def displayName(type: QStandardPaths.StandardLocation) -> str:
    """
    Calls Qt's 'QString
    QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::
    StandardLocation type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html#displayName

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformStandardPaths::displayName(QStandardPaths::
    #      StandardLocation type)
    return Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths11displayNameEN14QStanda'
        'rdPaths16StandardLocationE',
        type.value,
    )

  @staticmethod
  @overload(str, QStringList)
  def findExecutable(executableName: str, paths: QStringList) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickLabsPlatformStandardPaths::findExecutable(const
    QString &executableName, const QStringList &paths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html

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

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformStandardPaths::findExecutable(const QString
    #      &executableName, const QStringList &paths)
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths14findExecutableERK7QStr'
        'ingRK5QListIS0_E',
        executableName, CuteMixin._valueOf(paths),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(QStandardPaths.StandardLocation, str)
  @overload(
      QStandardPaths.StandardLocation, str, QStandardPaths.LocateOptions,
  )
  def locate(
      type: QStandardPaths.StandardLocation,
      fileName: str,
      options: QStandardPaths.LocateOptions = (
          QStandardPaths.LocateOptions.LocateFile),
  ) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQuickLabsPlatformStandardPaths::locate(QStandardPaths::StandardLocation
    type, const QString &fileName, QStandardPaths::LocateOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html#locate

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    options : QStandardPaths.LocateOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QStandardPaths.LocateOptions.LocateFile.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformStandardPaths::locate(QStandardPaths::
    #      StandardLocation type, const QString &fileName,
    #      QStandardPaths::LocateOptions options)
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths6locateEN14QStandardPath'
        's16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE',
        type.value, fileName, options.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(QStandardPaths.StandardLocation, str)
  @overload(
      QStandardPaths.StandardLocation, str, QStandardPaths.LocateOptions,
  )
  def locateAll(
      type: QStandardPaths.StandardLocation,
      fileName: str,
      options: QStandardPaths.LocateOptions = (
          QStandardPaths.LocateOptions.LocateFile),
  ) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl>
    QQuickLabsPlatformStandardPaths::locateAll(QStandardPaths::
    StandardLocation type, const QString &fileName,
    QStandardPaths::LocateOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html#locateAll

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    options : QStandardPaths.LocateOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QStandardPaths.LocateOptions.LocateFile.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl>
    #      QQuickLabsPlatformStandardPaths::locateAll(QStandardPaths::
    #      StandardLocation type, const QString &fileName,
    #      QStandardPaths::LocateOptions options)
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths9locateAllEN14QStandardP'
        'aths16StandardLocationERK7QString6QFlagsINS0_12LocateOptionEE',
        type.value, fileName, options.value,
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @staticmethod
  @overload(bool)
  def setTestModeEnabled(testMode: bool) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool
    testMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html

    Parameters
    ----------

    testMode : bool
      Passed on as it is.
    """
    #  void QQuickLabsPlatformStandardPaths::setTestModeEnabled(bool
    #      testMode)
    Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths18setTestModeEnabledEb',
        testMode,
    )

  @staticmethod
  @overload(QStandardPaths.StandardLocation)
  def writableLocation(type: QStandardPaths.StandardLocation) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQuickLabsPlatformStandardPaths::writableLocation(QStandardPaths::
    StandardLocation type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickLabsPlatformStandardPaths::writableLocation(
    #      QStandardPaths::StandardLocation type)
    address = Rituals.call(
        'ritual_ZN31QQuickLabsPlatformStandardPaths16writableLocationEN14QS'
        'tandardPaths16StandardLocationE',
        type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformStandardPaths'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformStandardPaths::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformstandardpaths.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformStandardPaths::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickLabsPlatformStandardPaths10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQuickLabsPlatformStandardPaths::QQuickLabsPlatformStandardPaths(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformStandardPaths', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformStandardPaths.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformStandardPaths::QQuickLabsPlatformStandardPaths(Q"
        "Object *parent)': leans on 'vtable for "
        "QQuickLabsPlatformStandardPaths', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickLabsPlatformStandardPaths::create(QQmlEngine
    *engine, QJSEngine *scriptEngine)': leans on 'vtable for
    QQuickLabsPlatformStandardPaths', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformStandardPaths.create' has no cute function yet. "
        "Qt's 'QObject *QQuickLabsPlatformStandardPaths::create(QQmlEngine "
        "*engine, QJSEngine *scriptEngine)': leans on 'vtable for "
        "QQuickLabsPlatformStandardPaths', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def standardLocations(*__, **_) -> Never:
    """
    Qt's 'QList<QUrl>
    QQuickLabsPlatformStandardPaths::standardLocations(QStandardPaths::
    StandardLocation type)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'toUrlList'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformStandardPaths.standardLocations' has no cute "
        "function yet. Qt's 'QList<QUrl> "
        "QQuickLabsPlatformStandardPaths::standardLocations(QStandardPaths::"
        "StandardLocation type)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'toUrlList'.")
