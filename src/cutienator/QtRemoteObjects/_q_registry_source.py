"""
QRegistrySource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectregistrysource_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QRegistrySource to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QRemoteObjectSourceLocationInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QRegistrySource(QObject):
  """
  The cute side of Qt's QRegistrySource: a plain Python object standing in
  front of one C++ QRegistrySource.

  It is built on the cute 'QObject', as Qt's QRegistrySource is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRegistrySource that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'sourceLocations',
  'removeServer'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRegistrySource::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QRegistrySource::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QRegistrySource::~QRegistrySource()': the destructor: Python never
    removes a C++ QRegistrySource.
  - Qt's 'void QRegistrySource::remoteObjectAdded(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRegistrySource::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QRegistrySource::addSource(const QRemoteObjectSourceLocation
    &entry)': takes a type Python has no way to hand over yet.
  - Qt's 'void QRegistrySource::removeSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QRegistrySource.

  What to expect
  --------------

  - The C++ QRegistrySource is created at the first use, not by
    'QRegistrySource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRegistrySource.
  - Qt tells when it has removed the C++ QRegistrySource. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QRegistrySource that has no cute function yet,
    '__init__', 'addSource', 'remoteObjectAdded', 'remoteObjectRemoved',
    'removeSource', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRegistrySource'

  #  A C++ QRegistrySource Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRegistrySource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QRegistrySource::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qregistrysource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRegistrySource::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QRegistrySource10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceLocations(self) -> QHash[str, QRemoteObjectSourceLocationInfo]:
    """
    Calls Qt's 'QRemoteObjectSourceLocations
    QRegistrySource::sourceLocations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qregistrysource.html#sourceLocations

    Returns
    -------

    QHash[str, QRemoteObjectSourceLocationInfo]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QRemoteObjectSourceLocations QRegistrySource::sourceLocations() const
    address = self.uglySide.call(
        'ritual_ZNK15QRegistrySource15sourceLocationsEv',
    )
    from . import QRemoteObjectSourceLocationInfo
    return QHash[str, QRemoteObjectSourceLocationInfo]._cuteOwning(address)

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
    Qt's 'QRegistrySource::QRegistrySource(QObject *parent)': leans on
    'QRegistrySource::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QRegistrySource.__init__' has no cute function yet. Qt's "
        "'QRegistrySource::QRegistrySource(QObject *parent)': leans on "
        "'QRegistrySource::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QUrl)
  def removeServer(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QRegistrySource::removeServer(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qregistrysource.html#removeServer

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QRegistrySource::removeServer(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN15QRegistrySource12removeServerERK4QUrl',
        self._valueOf(url),
    )

  @staticmethod
  def addSource(*__, **_) -> Never:
    """
    Qt's 'void QRegistrySource::addSource(const QRemoteObjectSourceLocation
    &entry)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QRegistrySource.addSource' has no cute function yet. Qt's 'void "
        "QRegistrySource::addSource(const QRemoteObjectSourceLocation "
        "&entry)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def remoteObjectAdded(*__, **_) -> Never:
    """
    Qt's 'void QRegistrySource::remoteObjectAdded(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRegistrySource.remoteObjectAdded' has no cute function yet. Qt's "
        "'void QRegistrySource::remoteObjectAdded(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def remoteObjectRemoved(*__, **_) -> Never:
    """
    Qt's 'void QRegistrySource::remoteObjectRemoved(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRegistrySource.remoteObjectRemoved' has no cute function yet. "
        "Qt's 'void QRegistrySource::remoteObjectRemoved(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def removeSource(*__, **_) -> Never:
    """
    Qt's 'void QRegistrySource::removeSource(const
    QRemoteObjectSourceLocation &entry)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QRegistrySource.removeSource' has no cute function yet. Qt's "
        "'void QRegistrySource::removeSource(const "
        "QRemoteObjectSourceLocation &entry)': takes a type Python has no "
        "way to hand over yet.")
