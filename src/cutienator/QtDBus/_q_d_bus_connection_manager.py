"""
QDBusConnectionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusconnectionmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDBusConnectionManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QDaemonThread, QStringList
from . import QDBusConnectionPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusConnectionManager(QDaemonThread):
  """
  The cute side of Qt's QDBusConnectionManager: a plain Python object
  standing in front of one C++ QDBusConnectionManager.

  It is built on the cute 'QDaemonThread', as Qt's QDBusConnectionManager is
  built on Qt's QDaemonThread, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusConnectionManager that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'existingConnection',
  'removeConnections', 'disconnectFrom', 'addConnection', 'run',
  'connection', 'removeConnection', 'setConnection'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusConnectionManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusConnectionManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusConnectionManager::~QDBusConnectionManager()': the destructor:
    Python never removes a C++ QDBusConnectionManager.

  What has no ritual
  ------------------

  13 of the 25 functions Qt declares: 8 leans on 'qdbus_resolve_me(char
  const*)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 2 not a gap; 2 leans on
  'QDBusConnectionManager; 1 Qt's library has no name for it, and its code in
  Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDBusConnectionManager is created at the first use, not by
    'QDBusConnectionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusConnectionManager.
  - Qt tells when it has removed the C++ QDBusConnectionManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusConnectionManager that has no cute function yet,
    '__init__', 'busConnection', 'connectToBus', 'connectToPeer',
    'createServer', 'doConnectToBus', 'doConnectToPeer',
    'doConnectToStandardBus', 'instance', holds a function that raises
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
  __qt_class__ = 'QDBusConnectionManager'

  #  A C++ QDBusConnectionManager Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusConnectionManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusConnectionManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusConnectionManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusConnectionManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(str)
  def existingConnection(
      self,
      name: str,
  ) -> Optional[QDBusConnectionPrivate]:
    """
    Calls Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::existingConnection(const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#existingConnection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDBusConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusConnectionPrivate
    #      *QDBusConnectionManager::existingConnection(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusConnectionManager18existingConnectionERK7QString',
        name,
    )
    return QDBusConnectionPrivate._cuteAt(address)

  @overload(str)
  def connection(self, name: str) -> Optional[QDBusConnectionPrivate]:
    """
    Calls Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::connection(const QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#connection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QDBusConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDBusConnectionPrivate *QDBusConnectionManager::connection(const
    #      QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK22QDBusConnectionManager10connectionERK7QString', name,
    )
    return QDBusConnectionPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QDBusConnectionPrivate)
  @overload(str, NoneType)
  def setConnection(
      self,
      name: str,
      c: Optional[QDBusConnectionPrivate],
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::setConnection(const QString
    &name, QDBusConnectionPrivate *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#setConnection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    c : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusConnectionManager::setConnection(const QString &name,
    #      QDBusConnectionPrivate *c)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionManager13setConnectionERK7QStringP22QDBu'
        'sConnectionPrivate',
        name, self._addressOf(c),
    )

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
    Qt's 'QDBusConnectionManager::QDBusConnectionManager()': leans on
    'QDBusConnectionManager::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.__init__' has no cute function yet. Qt's "
        "'QDBusConnectionManager::QDBusConnectionManager()': leans on "
        "'QDBusConnectionManager::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QStringList)
  def removeConnections(self, names: QStringList) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::removeConnections(const
    QStringList &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#removeConnections

    Parameters
    ----------

    names : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusConnectionManager::removeConnections(const QStringList
    #      &names)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionManager17removeConnectionsERK5QListI7QSt'
        'ringE',
        self._valueOf(names),
    )

  @overload(str, QDBusConnectionPrivate.ConnectionMode)
  def disconnectFrom(
      self,
      name: str,
      mode: QDBusConnectionPrivate.ConnectionMode,
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::disconnectFrom(const QString
    &name, QDBusConnectionPrivate::ConnectionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#disconnectFrom

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    mode : QDBusConnectionPrivate.ConnectionMode
      Passed on as its number.
    """
    #  void QDBusConnectionManager::disconnectFrom(const QString &name,
    #      QDBusConnectionPrivate::ConnectionMode mode)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionManager14disconnectFromERK7QStringN22QDB'
        'usConnectionPrivate14ConnectionModeE',
        name, mode.value,
    )

  @overload(str, QDBusConnectionPrivate)
  @overload(str, NoneType)
  def addConnection(
      self,
      name: str,
      c: Optional[QDBusConnectionPrivate],
  ) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::addConnection(const QString
    &name, QDBusConnectionPrivate *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#addConnection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    c : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusConnectionManager::addConnection(const QString &name,
    #      QDBusConnectionPrivate *c)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionManager13addConnectionERK7QStringP22QDBu'
        'sConnectionPrivate',
        name, self._addressOf(c),
    )

  def run(self) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusconnectionmanager.html#run
    """
    #  void QDBusConnectionManager::run()
    self.uglySide.call('ritual_ZN22QDBusConnectionManager3runEv')

  @overload(str)
  def removeConnection(self, name: str) -> None:
    """
    Calls Qt's 'void QDBusConnectionManager::removeConnection(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusconnectionmanager.html#removeConnection

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusConnectionManager::removeConnection(const QString &name)
    self.uglySide.call(
        'ritual_ZN22QDBusConnectionManager16removeConnectionERK7QString',
        name,
    )

  @staticmethod
  def busConnection(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::busConnection(QDBusConnection::BusType type)':
    leans on 'qdbus_resolve_me(char const*)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.busConnection' has no cute function yet. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::busConnection(QDBusConnection::BusType "
        "type)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def connectToBus(*__, **_) -> Never:
    """
    - Qt's 'QDBusConnectionPrivate
      *QDBusConnectionManager::connectToBus(QDBusConnection::BusType type,
      const QString &name, bool suspendedDelivery)': leans on
      'qdbus_resolve_me(char const*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'QDBusConnectionPrivate
      *QDBusConnectionManager::connectToBus(const QString &address, const
      QString &name)': leans on 'qdbus_resolve_me(char const*)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.connectToBus' has no cute function yet. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::connectToBus(QDBusConnection::BusType "
        "type, const QString &name, bool suspendedDelivery)': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::connectToBus(const QString &address, "
        "const QString &name)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def connectToPeer(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate *QDBusConnectionManager::connectToPeer(const
    QString &address, const QString &name)': leans on 'qdbus_resolve_me(char
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.connectToPeer' has no cute function yet. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::connectToPeer(const QString &address, "
        "const QString &name)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def createServer(*__, **_) -> Never:
    """
    Qt's 'void QDBusConnectionManager::createServer(const QString &address,
    QDBusServer *server)': leans on 'qdbus_resolve_me(char const*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.createServer' has no cute function yet. "
        "Qt's 'void QDBusConnectionManager::createServer(const QString "
        "&address, QDBusServer *server)': leans on 'qdbus_resolve_me(char "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def doConnectToBus(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::doConnectToBus(const QString &address, const
    QString &name)': leans on 'qdbus_resolve_me(char const*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.doConnectToBus' has no cute function yet. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::doConnectToBus(const QString &address, "
        "const QString &name)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def doConnectToPeer(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::doConnectToPeer(const QString &address, const
    QString &name)': leans on 'qdbus_resolve_me(char const*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.doConnectToPeer' has no cute function yet. "
        "Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::doConnectToPeer(const QString &address, "
        "const QString &name)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def doConnectToStandardBus(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionPrivate
    *QDBusConnectionManager::doConnectToStandardBus(QDBusConnection::BusType
    type, const QString &name, bool suspendedDelivery)': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.doConnectToStandardBus' has no cute "
        "function yet. Qt's 'QDBusConnectionPrivate "
        "*QDBusConnectionManager::doConnectToStandardBus(QDBusConnection::Bu"
        "sType type, const QString &name, bool suspendedDelivery)': leans "
        "on 'qdbus_resolve_me(char const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QDBusConnectionManager *QDBusConnectionManager::instance()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier '_q_manager'.
    """
    raise NotImplementedError(
        "'QDBusConnectionManager.instance' has no cute function yet. Qt's "
        "'QDBusConnectionManager *QDBusConnectionManager::instance()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'_q_manager'.")
