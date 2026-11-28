"""
QQmlStandardPaths binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCore/6.12.0/QtQmlCore/private/qqmlstandardpaths_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlStandardPaths to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QList, QObject, QStandardPaths, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlStandardPaths(QObject):
  """
  The cute side of Qt's QQmlStandardPaths: a plain Python object standing in
  front of one C++ QQmlStandardPaths.

  It is built on the cute 'QObject', as Qt's QQmlStandardPaths is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlStandardPaths that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'displayName', 'findExecutable', 'locate',
  'locateAll', 'standardLocations', 'writableLocation'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlStandardPaths::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlStandardPaths::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlStandardPaths::qt_qmlMarker_singleton()': one of Qt's own
    inner workings.
  - Qt's 'void QQmlStandardPaths::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlStandardPaths is created at the first use, not by
    'QQmlStandardPaths(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlStandardPaths.
  - Qt tells when it has removed the C++ QQmlStandardPaths. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQmlStandardPaths::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstandardpaths.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlStandardPaths::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQmlStandardPaths2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlStandardPaths::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstandardpaths.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlStandardPaths::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN17QQmlStandardPaths20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlStandardPaths'

  #  A C++ QQmlStandardPaths Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlStandardPaths'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlStandardPaths::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstandardpaths.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlStandardPaths::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStandardPaths.StandardLocation)
  def displayName(self, type: QStandardPaths.StandardLocation) -> str:
    """
    Calls Qt's 'QString
    QQmlStandardPaths::displayName(QStandardPaths::StandardLocation type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstandardpaths.html#displayName

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      QQmlStandardPaths::displayName(QStandardPaths::StandardLocation
    #      type) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths11displayNameEN14QStandardPaths16Stan'
        'dardLocationE',
        type.value,
    )

  @overload(str, QStringList)
  def findExecutable(self, executableName: str, paths: QStringList) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlStandardPaths::findExecutable(const QString
    &executableName, const QStringList &paths) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstandardpaths.html#findExecutable

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
    #  QUrl QQmlStandardPaths::findExecutable(const QString &executableName,
    #      const QStringList &paths) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths14findExecutableERK7QStringRK5QListIS'
        '0_E',
        executableName, self._valueOf(paths),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QStandardPaths.StandardLocation, str)
  @overload(
      QStandardPaths.StandardLocation, str, QStandardPaths.LocateOptions,
  )
  def locate(
      self,
      type: QStandardPaths.StandardLocation,
      fileName: str,
      options: QStandardPaths.LocateOptions = (
          QStandardPaths.LocateOptions.LocateFile),
  ) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQmlStandardPaths::locate(QStandardPaths::StandardLocation type, const
    QString &fileName, QStandardPaths::LocateOptions options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstandardpaths.html#locate

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
    #  QUrl QQmlStandardPaths::locate(QStandardPaths::StandardLocation type,
    #      const QString &fileName, QStandardPaths::LocateOptions options)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths6locateEN14QStandardPaths16StandardLo'
        'cationERK7QString6QFlagsINS0_12LocateOptionEE',
        type.value, fileName, options.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QStandardPaths.StandardLocation, str)
  @overload(
      QStandardPaths.StandardLocation, str, QStandardPaths.LocateOptions,
  )
  def locateAll(
      self,
      type: QStandardPaths.StandardLocation,
      fileName: str,
      options: QStandardPaths.LocateOptions = (
          QStandardPaths.LocateOptions.LocateFile),
  ) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl>
    QQmlStandardPaths::locateAll(QStandardPaths::StandardLocation type, const
    QString &fileName, QStandardPaths::LocateOptions options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlstandardpaths.html#locateAll

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
    #      QQmlStandardPaths::locateAll(QStandardPaths::StandardLocation
    #      type, const QString &fileName, QStandardPaths::LocateOptions
    #      options) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths9locateAllEN14QStandardPaths16Standar'
        'dLocationERK7QString6QFlagsINS0_12LocateOptionEE',
        type.value, fileName, options.value,
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(QStandardPaths.StandardLocation)
  def standardLocations(
      self,
      type: QStandardPaths.StandardLocation,
  ) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl>
    QQmlStandardPaths::standardLocations(QStandardPaths::StandardLocation
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstandardpaths.html#standardLocations

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQmlStandardPaths::standardLocations(QStandardPaths::
    #      StandardLocation type) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths17standardLocationsEN14QStandardPaths'
        '16StandardLocationE',
        type.value,
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  @overload(QStandardPaths.StandardLocation)
  def writableLocation(self, type: QStandardPaths.StandardLocation) -> QUrl:
    """
    Calls Qt's 'QUrl
    QQmlStandardPaths::writableLocation(QStandardPaths::StandardLocation
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstandardpaths.html#writableLocation

    Parameters
    ----------

    type : QStandardPaths.StandardLocation
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlStandardPaths::writableLocation(QStandardPaths::
    #      StandardLocation type) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlStandardPaths16writableLocationEN14QStandardPaths1'
        '6StandardLocationE',
        type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlStandardPaths::QQmlStandardPaths(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlstandardpaths.html#QQmlStandardPaths

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlStandardPaths::QQmlStandardPaths(QObject *parent)
    self._noteCreation(QQmlStandardPaths, lambda: Rituals.call(
        'ritual_ZN17QQmlStandardPathsC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
