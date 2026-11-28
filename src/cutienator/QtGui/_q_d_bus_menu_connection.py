"""
QDBusMenuConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qdbusmenuconnection_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDBusMenuConnection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtDBus import QDBusConnection, QDBusError, QDBusServiceWatcher
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusError = WAIT['QDBusError']


class QDBusMenuConnection(QObject):
  """
  The cute side of Qt's QDBusMenuConnection: a plain Python object standing
  in front of one C++ QDBusMenuConnection.

  It is built on the cute 'QObject', as Qt's QDBusMenuConnection is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusMenuConnection that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'connection',
  'dbusWatcher', 'isWatcherRegistered', 'trayIconRegistered', 'dbusError'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusMenuConnection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusMenuConnection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusMenuConnection::~QDBusMenuConnection()': the destructor:
    Python never removes a C++ QDBusMenuConnection.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'QDBusMenuConnection.

  What to expect
  --------------

  - The C++ QDBusMenuConnection is created at the first use, not by
    'QDBusMenuConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusMenuConnection.
  - Qt tells when it has removed the C++ QDBusMenuConnection. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusMenuConnection that has no cute function yet,
    '__init__', 'registerTrayIcon', 'registerTrayIconMenu',
    'registerTrayIconWithWatcher', 'unregisterTrayIcon',
    'unregisterTrayIconMenu', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMenuConnection'

  #  A C++ QDBusMenuConnection Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusMenuConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusMenuConnection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusMenuConnection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusMenuConnection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def connection(self) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusMenuConnection::connection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuconnection.html#connection

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusMenuConnection::connection() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusMenuConnection10connectionEv',
    )
    from ..QtDBus import QDBusConnection
    return QDBusConnection._cuteOwning(address)

  def dbusWatcher(self) -> Optional[QDBusServiceWatcher]:
    """
    Calls Qt's 'QDBusServiceWatcher *QDBusMenuConnection::dbusWatcher()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuconnection.html#dbusWatcher

    Returns
    -------

    Optional[QDBusServiceWatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusServiceWatcher *QDBusMenuConnection::dbusWatcher() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusMenuConnection11dbusWatcherEv',
    )
    from ..QtDBus import QDBusServiceWatcher
    return QDBusServiceWatcher._cuteAt(address)

  def isWatcherRegistered(self) -> bool:
    """
    Calls Qt's 'bool QDBusMenuConnection::isWatcherRegistered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuconnection.html#isWatcherRegistered
    """
    #  bool QDBusMenuConnection::isWatcherRegistered() const
    return self.uglySide.call(
        'ritual_ZNK19QDBusMenuConnection19isWatcherRegisteredEv',
    )

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
    Qt's 'QDBusMenuConnection::QDBusMenuConnection(QObject *parent, const
    QString &serviceName)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'StatusNotifierWatcherService'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.__init__' has no cute function yet. Qt's "
        "'QDBusMenuConnection::QDBusMenuConnection(QObject *parent, const "
        "QString &serviceName)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'StatusNotifierWatcherService'.")

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

  def trayIconRegistered(self) -> None:
    """
    Calls Qt's 'void QDBusMenuConnection::trayIconRegistered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmenuconnection.html#trayIconRegistered
    """
    #  void QDBusMenuConnection::trayIconRegistered()
    self.uglySide.call(
        'ritual_ZN19QDBusMenuConnection18trayIconRegisteredEv',
    )

  @overload(QDBusError)
  def dbusError(self, error: QDBusError) -> None:
    """
    Calls Qt's 'void QDBusMenuConnection::dbusError(const QDBusError
    &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmenuconnection.html#dbusError

    Parameters
    ----------

    error : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.
    """
    #  void QDBusMenuConnection::dbusError(const QDBusError &error)
    self.uglySide.call(
        'ritual_ZN19QDBusMenuConnection9dbusErrorERK10QDBusError',
        self._valueOf(error),
    )

  @staticmethod
  def registerTrayIcon(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMenuConnection::registerTrayIcon(QDBusTrayIcon *item)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'StatusNotifierItemPath'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.registerTrayIcon' has no cute function yet. "
        "Qt's 'bool QDBusMenuConnection::registerTrayIcon(QDBusTrayIcon "
        "*item)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'StatusNotifierItemPath'.")

  @staticmethod
  def registerTrayIconMenu(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMenuConnection::registerTrayIconMenu(QDBusTrayIcon
    *item)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'MenuBarPath'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.registerTrayIconMenu' has no cute function "
        "yet. Qt's 'bool "
        "QDBusMenuConnection::registerTrayIconMenu(QDBusTrayIcon *item)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'MenuBarPath'.")

  @staticmethod
  def registerTrayIconWithWatcher(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMenuConnection::registerTrayIconWithWatcher(QDBusTrayIcon
    *item)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'StatusNotifierWatcherService'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.registerTrayIconWithWatcher' has no cute "
        "function yet. Qt's 'bool "
        "QDBusMenuConnection::registerTrayIconWithWatcher(QDBusTrayIcon "
        "*item)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'StatusNotifierWatcherService'.")

  @staticmethod
  def unregisterTrayIcon(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuConnection::unregisterTrayIcon(QDBusTrayIcon *item)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'StatusNotifierItemPath'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.unregisterTrayIcon' has no cute function yet. "
        "Qt's 'void QDBusMenuConnection::unregisterTrayIcon(QDBusTrayIcon "
        "*item)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'StatusNotifierItemPath'.")

  @staticmethod
  def unregisterTrayIconMenu(*__, **_) -> Never:
    """
    Qt's 'void QDBusMenuConnection::unregisterTrayIconMenu(QDBusTrayIcon
    *item)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'MenuBarPath'.
    """
    raise NotImplementedError(
        "'QDBusMenuConnection.unregisterTrayIconMenu' has no cute function "
        "yet. Qt's 'void "
        "QDBusMenuConnection::unregisterTrayIconMenu(QDBusTrayIcon *item)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'MenuBarPath'.")
