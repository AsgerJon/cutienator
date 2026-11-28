"""
QAbstractSocketPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qabstractsocket_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractSocketPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QIODevicePrivate
from . import QAbstractSocket, QAbstractSocketEngineReceiver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractSocketEngine, QAuthenticator, QHostAddress
  from . import QHostInfo, QNetworkInterface, QNetworkProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QHostAddress = WAIT['QHostAddress']
  QHostInfo = WAIT['QHostInfo']
  QNetworkInterface = WAIT['QNetworkInterface']
  QNetworkProxy = WAIT['QNetworkProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSocketPrivate(QIODevicePrivate, QAbstractSocketEngineReceiver):
  """
  The cute side of Qt's QAbstractSocketPrivate: a plain Python object
  standing in front of one C++ QAbstractSocketPrivate.

  It is built on the cute 'QIODevicePrivate', as Qt's QAbstractSocketPrivate
  is built on Qt's QIODevicePrivate, and has everything that class has. It is
  built on the cute 'QAbstractSocketEngineReceiver' as well, as Qt's
  QAbstractSocketPrivate is built on Qt's QAbstractSocketEngineReceiver too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractSocketPrivate that has a ritual and that
  Python can call so far, 31 names in all: 'q_func', 'readNotification',
  'writeNotification', 'exceptionNotification', 'closeNotification',
  'connectionNotification', 'proxyAuthenticationRequired', 'bind',
  'canReadNotification', 'canWriteNotification', 'canCloseNotification',
  '_q_connectToNextAddress', '_q_startConnecting', '_q_testConnection',
  '_q_abortConnectionAttempt', 'resolveProxy', 'resetSocketLayer', 'flush',
  'initSocketLayer', 'configureCreatedSocket', 'startConnectingByName',
  'fetchConnectionParameters', 'readFromSocket', 'writeToSocket',
  'emitReadyRead', 'emitBytesWritten', 'setError', 'setErrorAndEmit',
  'pauseSocketNotifiers', 'resumeSocketNotifiers', 'getSocketEngine'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractSocket *QAbstractSocketPrivate::q_func() const':
    takes in Python what 'QAbstractSocket *QAbstractSocketPrivate::q_func()'
    takes.
  - Qt's 'QAbstractSocketPrivate::QAbstractSocketPrivate(decltype(
    QObjectPrivateVersion) version)': names the enum 'QtPrivate_6_12_0',
    whose class cannot be named here.
  - Qt's 'QAbstractSocketPrivate::~QAbstractSocketPrivate()': the destructor:
    Python never removes a C++ QAbstractSocketPrivate.

  What to expect
  --------------

  - The C++ QAbstractSocketPrivate is created at the first use, not by
    'QAbstractSocketPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractSocketPrivate.
  - Each name of Qt's QAbstractSocketPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QAbstractSocket)
  @overload(NoneType)
  def pauseSocketNotifiers(a0: Optional[QAbstractSocket]) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketPrivate::pauseSocketNotifiers(QAbstractSocket *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#pauseSocketNotifiers

    Parameters
    ----------

    a0 : Optional[QAbstractSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocketPrivate::pauseSocketNotifiers(QAbstractSocket *a0)
    Rituals.call(
        'ritual_ZN22QAbstractSocketPrivate20pauseSocketNotifiersEP15QAbstra'
        'ctSocket',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QAbstractSocket)
  @overload(NoneType)
  def resumeSocketNotifiers(a0: Optional[QAbstractSocket]) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketPrivate::resumeSocketNotifiers(QAbstractSocket *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#resumeSocketNotifiers

    Parameters
    ----------

    a0 : Optional[QAbstractSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocketPrivate::resumeSocketNotifiers(QAbstractSocket
    #      *a0)
    Rituals.call(
        'ritual_ZN22QAbstractSocketPrivate21resumeSocketNotifiersEP15QAbstr'
        'actSocket',
        CuteMixin._addressOf(a0),
    )

  @staticmethod
  @overload(QAbstractSocket)
  @overload(NoneType)
  def getSocketEngine(
      a0: Optional[QAbstractSocket],
  ) -> Optional[QAbstractSocketEngine]:
    """
    Calls Qt's 'QAbstractSocketEngine
    *QAbstractSocketPrivate::getSocketEngine(QAbstractSocket *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#getSocketEngine

    Parameters
    ----------

    a0 : Optional[QAbstractSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractSocketEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocketEngine
    #      *QAbstractSocketPrivate::getSocketEngine(QAbstractSocket *a0)
    address = Rituals.call(
        'ritual_ZN22QAbstractSocketPrivate15getSocketEngineEP15QAbstractSoc'
        'ket',
        CuteMixin._addressOf(a0),
    )
    from . import QAbstractSocketEngine
    return QAbstractSocketEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractSocketPrivate'

  #  Qt's QAbstractSocketPrivate is built on more than one class. The part of
  #  a C++ QAbstractSocketPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractSocketEngineReceiver':
          'ritual_cast_QAbstractSocketPrivate_QAbstractSocketEngineReceiver',
  }

  #  A C++ QAbstractSocketPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractSocketPrivate'

  #  The functions Qt calls itself that QAbstractSocketPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'bind': (
          ('_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QA'
           'bstractSocket8BindFlagEEPK17QNetworkInterface',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
               ('int', 'flags', 'QtNetwork:QAbstractSocket.BindFlag'),
               ('address', 'address', 'QtNetwork:QNetworkInterface'),
           )),
      ),
      'canReadNotification': (
          ('_ZN22QAbstractSocketPrivate19canReadNotificationEv',
           ('bool', 'number', ''),
           ()),
      ),
      'flush': (
          ('_ZN22QAbstractSocketPrivate5flushEv',
           ('bool', 'number', ''),
           ()),
      ),
      'configureCreatedSocket': (
          ('_ZN22QAbstractSocketPrivate22configureCreatedSocketEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'writeToSocket': (
          ('_ZN22QAbstractSocketPrivate13writeToSocketEv',
           ('bool', 'number', ''),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractSocket.SocketError, str)
  def setError(
      self,
      errorCode: QAbstractSocket.SocketError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketPrivate::setError(QAbstractSocket::SocketError errorCode,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#setError

    Parameters
    ----------

    errorCode : QAbstractSocket.SocketError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocketPrivate::setError(QAbstractSocket::SocketError
    #      errorCode, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate8setErrorEN15QAbstractSocket11Soc'
        'ketErrorERK7QString',
        errorCode.value, errorString,
    )

  @overload(QAbstractSocket.SocketError, str)
  def setErrorAndEmit(
      self,
      errorCode: QAbstractSocket.SocketError,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketPrivate::setErrorAndEmit(QAbstractSocket::SocketError
    errorCode, const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#setErrorAndEmit

    Parameters
    ----------

    errorCode : QAbstractSocket.SocketError
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocketPrivate::setErrorAndEmit(QAbstractSocket::
    #      SocketError errorCode, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate15setErrorAndEmitEN15QAbstractSoc'
        'ket11SocketErrorERK7QString',
        errorCode.value, errorString,
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
    Qt's 'QAbstractSocketPrivate::QAbstractSocketPrivate(decltype(
    QObjectPrivateVersion) version)': names the enum 'QtPrivate_6_12_0',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractSocketPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstractSocketPrivate::QAbstractSocketPrivate(decltype(QObjectPri"
        "vateVersion) version)': names the enum 'QtPrivate_6_12_0', whose "
        "class cannot be named here.")

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

  def q_func(self) -> Optional[QAbstractSocket]:
    """
    Calls Qt's 'QAbstractSocket *QAbstractSocketPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketprivate.html#q_func

    Returns
    -------

    Optional[QAbstractSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSocket *QAbstractSocketPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate6q_funcEv',
    )
    return QAbstractSocket._cuteAt(address)

  def readNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::readNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#readNotification
    """
    #  void QAbstractSocketPrivate::readNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate16readNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate16readNotificationEv'
    self.uglySide.call(ritual)

  def writeNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::writeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#writeNotification
    """
    #  void QAbstractSocketPrivate::writeNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate17writeNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate17writeNotificationEv'
    self.uglySide.call(ritual)

  def exceptionNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::exceptionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#exceptionNotification
    """
    #  void QAbstractSocketPrivate::exceptionNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate21exceptionNotificationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSocketPrivate21exceptionNotificationEv')
    self.uglySide.call(ritual)

  def closeNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::closeNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#closeNotification
    """
    #  void QAbstractSocketPrivate::closeNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate17closeNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate17closeNotificationEv'
    self.uglySide.call(ritual)

  def connectionNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::connectionNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#connectionNotification
    """
    #  void QAbstractSocketPrivate::connectionNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate22connectionNotificationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSocketPrivate22connectionNotificationEv')
    self.uglySide.call(ritual)

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractSocketPrivate::proxyAuthenticationRequired(const QNetworkProxy
    &proxy, QAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
    #      QNetworkProxy &proxy, QAuthenticator *authenticator)
    ritual = (
        'ritual_ZN22QAbstractSocketPrivate27proxyAuthenticationRequiredERK1'
        '3QNetworkProxyP14QAuthenticator')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSocketPrivate27proxyAuthenticationRequir'
          'edERK13QNetworkProxyP14QAuthenticator')
    self.uglySide.call(
        ritual, self._valueOf(proxy), self._addressOf(authenticator),
    )

  @overload(QHostAddress, int, QAbstractSocket.BindMode)
  @overload(QHostAddress, int, QAbstractSocket.BindMode, QNetworkInterface)
  @overload(QHostAddress, int, QAbstractSocket.BindMode, NoneType)
  def bind(
      self,
      address: QHostAddress,
      port: int,
      mode: QAbstractSocket.BindMode,
      iface: Optional[QNetworkInterface] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::bind(const QHostAddress
    &address, quint16 port, QAbstractSocket::BindMode mode, const
    QNetworkInterface *iface)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketprivate.html#bind

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.

    mode : QAbstractSocket.BindMode
      Passed on as its number.

    iface : Optional[QNetworkInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QAbstractSocketPrivate::bind(const QHostAddress &address, quint16
    #      port, QAbstractSocket::BindMode mode, const QNetworkInterface
    #      *iface)
    ritual = (
        'ritual_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN1'
        '5QAbstractSocket8BindFlagEEPK17QNetworkInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFl'
          'agsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface')
    return self.uglySide.call(
        ritual,
        self._valueOf(address), port, mode.value, self._addressOf(iface),
    )

  def canReadNotification(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::canReadNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#canReadNotification
    """
    #  bool QAbstractSocketPrivate::canReadNotification()
    ritual = 'ritual_ZN22QAbstractSocketPrivate19canReadNotificationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate19canReadNotificationEv'
    return self.uglySide.call(ritual)

  def canWriteNotification(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::canWriteNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#canWriteNotification
    """
    #  bool QAbstractSocketPrivate::canWriteNotification()
    return self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate20canWriteNotificationEv',
    )

  def canCloseNotification(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::canCloseNotification()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#canCloseNotification
    """
    #  void QAbstractSocketPrivate::canCloseNotification()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate20canCloseNotificationEv',
    )

  def _q_connectToNextAddress(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::_q_connectToNextAddress()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html
    """
    #  void QAbstractSocketPrivate::_q_connectToNextAddress()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate23_q_connectToNextAddressEv',
    )

  @overload(QHostInfo)
  def _q_startConnecting(self, hostInfo: QHostInfo) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::_q_startConnecting(const
    QHostInfo &hostInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#_q_startConnecting

    Parameters
    ----------

    hostInfo : QHostInfo
      Passed on as a value: Qt reads the C++ QHostInfo, which stays Python's
      own.
    """
    #  void QAbstractSocketPrivate::_q_startConnecting(const QHostInfo
    #      &hostInfo)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate18_q_startConnectingERK9QHostInfo',
        self._valueOf(hostInfo),
    )

  def _q_testConnection(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::_q_testConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#_q_testConnection
    """
    #  void QAbstractSocketPrivate::_q_testConnection()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate17_q_testConnectionEv',
    )

  def _q_abortConnectionAttempt(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::_q_abortConnectionAttempt()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html
    """
    #  void QAbstractSocketPrivate::_q_abortConnectionAttempt()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate25_q_abortConnectionAttemptEv',
    )

  @overload(str, int)
  def resolveProxy(self, hostName: str, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::resolveProxy(const QString
    &hostName, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#resolveProxy

    Parameters
    ----------

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocketPrivate::resolveProxy(const QString &hostName,
    #      quint16 port)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate12resolveProxyERK7QStringt',
        hostName, port,
    )

  @overload(int)
  def resolveProxy(self, port: int) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::resolveProxy(quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#resolveProxy

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QAbstractSocketPrivate::resolveProxy(quint16 port)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate12resolveProxyEt', port,
    )

  def resetSocketLayer(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::resetSocketLayer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#resetSocketLayer
    """
    #  void QAbstractSocketPrivate::resetSocketLayer()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate16resetSocketLayerEv',
    )

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractsocketprivate.html#flush
    """
    #  bool QAbstractSocketPrivate::flush()
    ritual = 'ritual_ZN22QAbstractSocketPrivate5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate5flushEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractSocket.NetworkLayerProtocol)
  def initSocketLayer(
      self,
      protocol: QAbstractSocket.NetworkLayerProtocol,
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractSocketPrivate::initSocketLayer(QAbstractSocket::
    NetworkLayerProtocol protocol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#initSocketLayer

    Parameters
    ----------

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number.
    """
    #  bool QAbstractSocketPrivate::initSocketLayer(QAbstractSocket::
    #      NetworkLayerProtocol protocol)
    return self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate15initSocketLayerEN15QAbstractSoc'
        'ket20NetworkLayerProtocolE',
        protocol.value,
    )

  def configureCreatedSocket(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::configureCreatedSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#configureCreatedSocket
    """
    #  void QAbstractSocketPrivate::configureCreatedSocket()
    ritual = 'ritual_ZN22QAbstractSocketPrivate22configureCreatedSocketEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAbstractSocketPrivate22configureCreatedSocketEv')
    self.uglySide.call(ritual)

  @overload(str)
  def startConnectingByName(self, host: str) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::startConnectingByName(const
    QString &host)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#startConnectingByName

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractSocketPrivate::startConnectingByName(const QString
    #      &host)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate21startConnectingByNameERK7QStrin'
        'g',
        host,
    )

  def fetchConnectionParameters(self) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::fetchConnectionParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html
    """
    #  void QAbstractSocketPrivate::fetchConnectionParameters()
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate25fetchConnectionParametersEv',
    )

  def readFromSocket(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::readFromSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#readFromSocket
    """
    #  bool QAbstractSocketPrivate::readFromSocket()
    return self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate14readFromSocketEv',
    )

  def writeToSocket(self) -> bool:
    """
    Calls Qt's 'bool QAbstractSocketPrivate::writeToSocket()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#writeToSocket
    """
    #  bool QAbstractSocketPrivate::writeToSocket()
    ritual = 'ritual_ZN22QAbstractSocketPrivate13writeToSocketEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAbstractSocketPrivate13writeToSocketEv'
    return self.uglySide.call(ritual)

  @overload()
  @overload(int)
  def emitReadyRead(self, channel: int = 0) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::emitReadyRead(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#emitReadyRead

    Parameters
    ----------

    channel : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QAbstractSocketPrivate::emitReadyRead(int channel)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate13emitReadyReadEi', channel,
    )

  @overload(int)
  @overload(int, int)
  def emitBytesWritten(self, bytes: int, channel: int = 0) -> None:
    """
    Calls Qt's 'void QAbstractSocketPrivate::emitBytesWritten(qint64 bytes,
    int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractsocketprivate.html#emitBytesWritten

    Parameters
    ----------

    bytes : int
      Passed on as it is.

    channel : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QAbstractSocketPrivate::emitBytesWritten(qint64 bytes, int
    #      channel)
    self.uglySide.call(
        'ritual_ZN22QAbstractSocketPrivate16emitBytesWrittenExi',
        bytes, channel,
    )
