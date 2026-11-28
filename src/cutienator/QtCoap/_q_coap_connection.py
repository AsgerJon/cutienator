"""
QCoapConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCoapConnection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject
from ..QtNetwork import QAbstractSocket
from . import QtCoap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtNetwork import QHostAddress, QNetworkInterface
  from . import QCoapConnectionPrivate, QCoapSecurityConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QCoapSecurityConfiguration = WAIT['QCoapSecurityConfiguration']
  QHostAddress = WAIT['QHostAddress']
  QNetworkInterface = WAIT['QNetworkInterface']


class QCoapConnection(QObject):
  """
  The cute side of Qt's QCoapConnection: a plain Python object standing in
  front of one C++ QCoapConnection.

  It is built on the cute 'QObject', as Qt's QCoapConnection is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapConnection that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'isSecure', 'securityMode',
  'state', 'securityConfiguration', 'setSecurityConfiguration', 'disconnect',
  'setUdpNetworkInterface', 'udpNetworkInterface', 'error', 'readyRead',
  'bound', 'securityConfigurationChanged', 'startToSendRequest', 'bind',
  'writeData', 'close', 'd_func'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapConnection::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCoapConnection::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapConnection::~QCoapConnection()': the destructor: Python never
    removes a C++ QCoapConnection.
  - Qt's 'const QCoapConnectionPrivate *QCoapConnection::d_func() const':
    takes in Python what 'QCoapConnectionPrivate *QCoapConnection::d_func()'
    takes.

  What has no ritual
  ------------------

  5 of the 27 functions Qt declares: 3 leans on 'QCoapConnection; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QCoapConnection is created at the first use, not by
    'QCoapConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapConnection.
  - Qt tells when it has removed the C++ QCoapConnection. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapConnection that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QCoapConnection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ConnectionState(CuteNum, scoped=True):
    """
    The enum 'QCoapConnection::ConnectionState' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unconnected = Kee[int](0)
    Bound = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapConnection'

  #  A C++ QCoapConnection Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapConnection'

  #  The functions Qt calls itself that QCoapConnection is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'bind': (
          ('_ZN15QCoapConnection4bindERK7QStringt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('unsigned short', 'number', ''),
           )),
      ),
      'writeData': (
          ('_ZN15QCoapConnection9writeDataERK10QByteArrayRK7QStringt',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'text', ''),
               ('unsigned short', 'number', ''),
           )),
      ),
      'close': (
          ('_ZN15QCoapConnection5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapConnection::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapConnection::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCoapConnection10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isSecure(self) -> bool:
    """
    Calls Qt's 'bool QCoapConnection::isSecure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#isSecure
    """
    #  bool QCoapConnection::isSecure() const
    return self.uglySide.call('ritual_ZNK15QCoapConnection8isSecureEv')

  def securityMode(self) -> QtCoap.SecurityMode:
    """
    Calls Qt's 'QtCoap::SecurityMode QCoapConnection::securityMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#securityMode

    Returns
    -------

    QtCoap.SecurityMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtCoap.SecurityMode(number)' gives.
    """
    #  QtCoap::SecurityMode QCoapConnection::securityMode() const
    return QtCoap.SecurityMode(self.uglySide.call(
        'ritual_ZNK15QCoapConnection12securityModeEv',
    ))

  def state(self) -> ConnectionState:
    """
    Calls Qt's 'ConnectionState QCoapConnection::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#state

    Returns
    -------

    ConnectionState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ConnectionState(number)'
      gives.
    """
    #  ConnectionState QCoapConnection::state() const
    return QCoapConnection.ConnectionState(self.uglySide.call(
        'ritual_ZNK15QCoapConnection5stateEv',
    ))

  def securityConfiguration(self) -> QCoapSecurityConfiguration:
    """
    Calls Qt's 'QCoapSecurityConfiguration
    QCoapConnection::securityConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#securityConfiguration

    Returns
    -------

    QCoapSecurityConfiguration
      A new cute QCoapSecurityConfiguration around the copy Qt gave back.
      Python owns it.
    """
    #  QCoapSecurityConfiguration QCoapConnection::securityConfiguration()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QCoapConnection21securityConfigurationEv',
    )
    from . import QCoapSecurityConfiguration
    return QCoapSecurityConfiguration._cuteOwning(address)

  def udpNetworkInterface(self) -> QNetworkInterface:
    """
    Calls Qt's 'QNetworkInterface QCoapConnection::udpNetworkInterface()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#udpNetworkInterface

    Returns
    -------

    QNetworkInterface
      A new cute QNetworkInterface around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkInterface QCoapConnection::udpNetworkInterface() const
    address = self.uglySide.call(
        'ritual_ZNK15QCoapConnection19udpNetworkInterfaceEv',
    )
    from ..QtNetwork import QNetworkInterface
    return QNetworkInterface._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCoapSecurityConfiguration)
  def setSecurityConfiguration(
      self,
      configuration: QCoapSecurityConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QCoapConnection::setSecurityConfiguration(const
    QCoapSecurityConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#setSecurityConfiguration

    Parameters
    ----------

    configuration : QCoapSecurityConfiguration
      Passed on as a value: Qt reads the C++ QCoapSecurityConfiguration,
      which stays Python's own.
    """
    #  void QCoapConnection::setSecurityConfiguration(const
    #      QCoapSecurityConfiguration &configuration)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection24setSecurityConfigurationERK26QCoapSecu'
        'rityConfiguration',
        self._valueOf(configuration),
    )

  @overload(QNetworkInterface)
  def setUdpNetworkInterface(self, iface: QNetworkInterface) -> None:
    """
    Calls Qt's 'void QCoapConnection::setUdpNetworkInterface(const
    QNetworkInterface &iface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#setUdpNetworkInterface

    Parameters
    ----------

    iface : QNetworkInterface
      Passed on as a value: Qt reads the C++ QNetworkInterface, which stays
      Python's own.
    """
    #  void QCoapConnection::setUdpNetworkInterface(const QNetworkInterface
    #      &iface)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection22setUdpNetworkInterfaceERK17QNetworkInt'
        'erface',
        self._valueOf(iface),
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
    - Qt's 'QCoapConnection::QCoapConnection(QtCoap::SecurityMode
      securityMode, QObject *parent)': leans on
      'QCoapConnection::qt_metacall(QMetaObject::Call, int, void**)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'QCoapConnection::QCoapConnection(QObjectPrivate &dd, QObject
      *parent)': leans on 'QCoapConnection::qt_metacall(QMetaObject::Call,
      int, void**)', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapConnection.__init__' has no cute function yet. Qt's "
        "'QCoapConnection::QCoapConnection(QtCoap::SecurityMode "
        "securityMode, QObject *parent)': leans on "
        "'QCoapConnection::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'QCoapConnection::QCoapConnection(QObjectPrivate &dd, QObject "
        "*parent)': leans on "
        "'QCoapConnection::qt_metacall(QMetaObject::Call, int, void**)', "
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

  def disconnect(self) -> None:
    """
    Calls Qt's 'void QCoapConnection::disconnect()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#disconnect
    """
    #  void QCoapConnection::disconnect()
    self.uglySide.call('ritual_ZN15QCoapConnection10disconnectEv')

  @overload(QAbstractSocket.SocketError)
  def error(self, error: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QCoapConnection::error(QAbstractSocket::SocketError
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#error

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QCoapConnection::error(QAbstractSocket::SocketError error)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection5errorEN15QAbstractSocket11SocketErrorE',
        error.value,
    )

  @overload(QByteArray, QHostAddress)
  def readyRead(self, data: QByteArray, sender: QHostAddress) -> None:
    """
    Calls Qt's 'void QCoapConnection::readyRead(const QByteArray &data, const
    QHostAddress &sender)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#readyRead

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    sender : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  void QCoapConnection::readyRead(const QByteArray &data, const
    #      QHostAddress &sender)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection9readyReadERK10QByteArrayRK12QHostAddres'
        's',
        self._valueOf(data), self._valueOf(sender),
    )

  def bound(self) -> None:
    """
    Calls Qt's 'void QCoapConnection::bound()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#bound
    """
    #  void QCoapConnection::bound()
    self.uglySide.call('ritual_ZN15QCoapConnection5boundEv')

  def securityConfigurationChanged(self) -> None:
    """
    Calls Qt's 'void QCoapConnection::securityConfigurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#securityConfigurationChanged
    """
    #  void QCoapConnection::securityConfigurationChanged()
    self.uglySide.call(
        'ritual_ZN15QCoapConnection28securityConfigurationChangedEv',
    )

  def startToSendRequest(self) -> None:
    """
    Calls Qt's 'void QCoapConnection::startToSendRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapconnection.html#startToSendRequest
    """
    #  void QCoapConnection::startToSendRequest()
    self.uglySide.call('ritual_ZN15QCoapConnection18startToSendRequestEv')

  @overload(str, int)
  def bind(self, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapConnection::bind(const QString &host, quint16
    port)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#bind

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QCoapConnection::bind(const QString &host, quint16 port)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection4bindERK7QStringt', host, port,
    )

  @overload(QByteArray, str, int)
  def writeData(self, data: QByteArray, host: str, port: int) -> None:
    """
    Calls Qt's 'void QCoapConnection::writeData(const QByteArray &data, const
    QString &host, quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#writeData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    host : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QCoapConnection::writeData(const QByteArray &data, const QString
    #      &host, quint16 port)
    self.uglySide.call(
        'ritual_ZN15QCoapConnection9writeDataERK10QByteArrayRK7QStringt',
        self._valueOf(data), host, port,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QCoapConnection::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#close
    """
    #  void QCoapConnection::close()
    self.uglySide.call('ritual_ZN15QCoapConnection5closeEv')

  def d_func(self) -> Optional[QCoapConnectionPrivate]:
    """
    Calls Qt's 'QCoapConnectionPrivate *QCoapConnection::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapconnection.html#d_func

    Returns
    -------

    Optional[QCoapConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapConnectionPrivate *QCoapConnection::d_func()
    address = self.uglySide.call('ritual_ZN15QCoapConnection6d_funcEv')
    from . import QCoapConnectionPrivate
    return QCoapConnectionPrivate._cuteAt(address)
