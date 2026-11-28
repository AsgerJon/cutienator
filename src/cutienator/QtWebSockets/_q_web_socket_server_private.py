"""
QWebSocketServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketserver_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWebSocketServerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate, QStringList
from ..QtNetwork import QAbstractSocket
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtNetwork import QHostAddress, QNetworkProxy, QSslConfiguration
  from ..QtNetwork import QTcpSocket
  from . import QWebSocket, QWebSocketServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QTcpSocket = WAIT['QTcpSocket']
  QWebSocket = WAIT['QWebSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebSocketServerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWebSocketServerPrivate: a plain Python object
  standing in front of one C++ QWebSocketServerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWebSocketServerPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocketServerPrivate that has a ritual and that
  Python can call so far, 34 names in all: 'q_func', 'close', 'errorString',
  'hasPendingConnections', 'isListening', 'listen', 'maxPendingConnections',
  'handshakeTimeout', 'nextPendingConnection', 'pauseAccepting', 'proxy',
  'setProxy', 'resumeAccepting', 'serverAddress', 'serverError',
  'serverPort', 'setMaxPendingConnections', 'setHandshakeTimeout',
  'setSocketDescriptor', 'socketDescriptor', 'setSupportedSubprotocols',
  'supportedSubprotocols', 'supportedExtensions', 'setServerName',
  'serverName', 'secureMode', 'setSslConfiguration', 'sslConfiguration',
  'setError', 'startHandshakeTimeout', 'addPendingConnection',
  'setErrorFromSocketError', 'onSocketDisconnected',
  'finishHandshakeTimeout'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWebSocketServer *QWebSocketServerPrivate::q_func() const':
    takes in Python what 'QWebSocketServer
    *QWebSocketServerPrivate::q_func()' takes.
  - Qt's 'QWebSocketServerPrivate::~QWebSocketServerPrivate()': the
    destructor: Python never removes a C++ QWebSocketServerPrivate.
  - Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketServerPrivate::supportedVersions() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  6 of the 44 functions Qt declares: 4 leans on 'operator<<(QTextStream&,
  QWebSocketHandshakeResponse const&)', which Qt's source does not mark for
  use from outside Qt and has no code for that could be taken; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebSocketServerPrivate is created at the first use, not by
    'QWebSocketServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketServerPrivate.
  - Each name of Qt's QWebSocketServerPrivate that has no cute function yet,
    'handleConnection', 'handshakeReceived', 'init', 'onNewConnection',
    'supportedVersions', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QWebSocketServerPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class SslMode(CuteNum):
    """
    The enum 'QWebSocketServerPrivate::SslMode' of Qt, with the 2 names Qt
    gives in it.
    """

    SecureMode = Kee[int](1)
    NonSecureMode = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketServerPrivate'

  #  A C++ QWebSocketServerPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebSocketServerPrivate'

  #  The functions Qt calls itself that QWebSocketServerPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'nextPendingConnection': (
          ('_ZN23QWebSocketServerPrivate21nextPendingConnectionEv',
           ('address', 'address', 'QtWebSockets:QWebSocket'),
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

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebSocketServerPrivate::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketServerPrivate::errorString() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate11errorStringEv',
    )

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketServerPrivate::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#hasPendingConnections
    """
    #  bool QWebSocketServerPrivate::hasPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate21hasPendingConnectionsEv',
    )

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketServerPrivate::isListening() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#isListening
    """
    #  bool QWebSocketServerPrivate::isListening() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate11isListeningEv',
    )

  def maxPendingConnections(self) -> int:
    """
    Calls Qt's 'int QWebSocketServerPrivate::maxPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#maxPendingConnections
    """
    #  int QWebSocketServerPrivate::maxPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate21maxPendingConnectionsEv',
    )

  def handshakeTimeout(self) -> int:
    """
    Calls Qt's 'int QWebSocketServerPrivate::handshakeTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#handshakeTimeout
    """
    #  int QWebSocketServerPrivate::handshakeTimeout() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate16handshakeTimeoutEv',
    )

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QWebSocketServerPrivate::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserverprivate.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QWebSocketServerPrivate::proxy() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate5proxyEv',
    )
    from ..QtNetwork import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def serverAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QWebSocketServerPrivate::serverAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#serverAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QWebSocketServerPrivate::serverAddress() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate13serverAddressEv',
    )
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def serverError(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode
    QWebSocketServerPrivate::serverError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#serverError

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocketServerPrivate::serverError()
    #      const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate11serverErrorEv',
    ))

  def serverPort(self) -> int:
    """
    Calls Qt's 'quint16 QWebSocketServerPrivate::serverPort() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#serverPort
    """
    #  quint16 QWebSocketServerPrivate::serverPort() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate10serverPortEv',
    )

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QWebSocketServerPrivate::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#socketDescriptor
    """
    #  qintptr QWebSocketServerPrivate::socketDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate16socketDescriptorEv',
    )

  def supportedSubprotocols(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebSocketServerPrivate::supportedSubprotocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#supportedSubprotocols

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebSocketServerPrivate::supportedSubprotocols() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate21supportedSubprotocolsEv',
    )
    return QStringList._cuteOwning(address)

  def supportedExtensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebSocketServerPrivate::supportedExtensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#supportedExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebSocketServerPrivate::supportedExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate19supportedExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  def serverName(self) -> str:
    """
    Calls Qt's 'QString QWebSocketServerPrivate::serverName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#serverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketServerPrivate::serverName() const
    return self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate10serverNameEv',
    )

  def secureMode(self) -> SslMode:
    """
    Calls Qt's 'SslMode QWebSocketServerPrivate::secureMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#secureMode

    Returns
    -------

    SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SslMode(number)' gives.
    """
    #  SslMode QWebSocketServerPrivate::secureMode() const
    return QWebSocketServerPrivate.SslMode(self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate10secureModeEv',
    ))

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QWebSocketServerPrivate::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QWebSocketServerPrivate::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate16sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QWebSocketServerPrivate::setProxy(const QNetworkProxy
    #      &networkProxy)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(int)
  def setMaxPendingConnections(self, numConnections: int) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setMaxPendingConnections(int
    numConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html

    Parameters
    ----------

    numConnections : int
      Passed on as it is.
    """
    #  void QWebSocketServerPrivate::setMaxPendingConnections(int
    #      numConnections)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate24setMaxPendingConnectionsEi',
        numConnections,
    )

  @overload(int)
  def setHandshakeTimeout(self, msec: int) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setHandshakeTimeout(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setHandshakeTimeout

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QWebSocketServerPrivate::setHandshakeTimeout(int msec)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate19setHandshakeTimeoutEi', msec,
    )

  @overload(int)
  def setSocketDescriptor(self, socketDescriptor: int) -> bool:
    """
    Calls Qt's 'bool QWebSocketServerPrivate::setSocketDescriptor(qintptr
    socketDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  bool QWebSocketServerPrivate::setSocketDescriptor(qintptr
    #      socketDescriptor)
    return self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate19setSocketDescriptorEx',
        socketDescriptor,
    )

  @overload(QStringList)
  def setSupportedSubprotocols(self, protocols: QStringList) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setSupportedSubprotocols(const
    QStringList &protocols)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html

    Parameters
    ----------

    protocols : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketServerPrivate::setSupportedSubprotocols(const
    #      QStringList &protocols)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate24setSupportedSubprotocolsERK5QL'
        'istI7QStringE',
        self._valueOf(protocols),
    )

  @overload(str)
  def setServerName(self, serverName: str) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setServerName(const QString
    &serverName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setServerName

    Parameters
    ----------

    serverName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServerPrivate::setServerName(const QString &serverName)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate13setServerNameERK7QString',
        serverName,
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::setSslConfiguration(const
    QSslConfiguration &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QWebSocketServerPrivate::setSslConfiguration(const
    #      QSslConfiguration &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate19setSslConfigurationERK17QSslCo'
        'nfiguration',
        self._valueOf(sslConfiguration),
    )

  @overload(QWebSocketProtocol.CloseCode, str)
  def setError(
      self,
      code: QWebSocketProtocol.CloseCode,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QWebSocketServerPrivate::setError(QWebSocketProtocol::CloseCode code,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#setError

    Parameters
    ----------

    code : QWebSocketProtocol.CloseCode
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServerPrivate::setError(QWebSocketProtocol::CloseCode
    #      code, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate8setErrorEN18QWebSocketProtocol9'
        'CloseCodeERK7QString',
        code.value, errorString,
    )

  @overload(QAbstractSocket.SocketError, str)
  def setErrorFromSocketError(
      self,
      error: QAbstractSocket.SocketError,
      errorDescription: str,
  ) -> None:
    """
    Calls Qt's 'void
    QWebSocketServerPrivate::setErrorFromSocketError(QAbstractSocket::
    SocketError error, const QString &errorDescription)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.

    errorDescription : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServerPrivate::setErrorFromSocketError(
    #      QAbstractSocket::SocketError error, const QString
    #      &errorDescription)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate23setErrorFromSocketErrorEN15QAb'
        'stractSocket11SocketErrorERK7QString',
        error.value, errorDescription,
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

  @overload(str, SslMode)
  def __init__(self, serverName: str, secureMode: SslMode) -> None:
    """
    Notes what was given, for Qt's
    'QWebSocketServerPrivate::QWebSocketServerPrivate(const QString
    &serverName, SslMode secureMode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html

    Parameters
    ----------

    serverName : str
      Passed on as it is: a QString is made of it for the call.

    secureMode : SslMode
      Passed on as its number.
    """
    #  QWebSocketServerPrivate::QWebSocketServerPrivate(const QString
    #      &serverName, SslMode secureMode)
    self._noteCreation(QWebSocketServerPrivate, lambda: Rituals.call(
        'ritual_ZN23QWebSocketServerPrivateC1ERK7QStringNS_7SslModeE',
        serverName, secureMode.value,
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

  def q_func(self) -> Optional[QWebSocketServer]:
    """
    Calls Qt's 'QWebSocketServer *QWebSocketServerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#q_func

    Returns
    -------

    Optional[QWebSocketServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocketServer *QWebSocketServerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate6q_funcEv',
    )
    from . import QWebSocketServer
    return QWebSocketServer._cuteAt(address)

  @overload()
  @overload(bool)
  def close(self, aboutToDestroy: bool = False) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::close(bool aboutToDestroy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserverprivate.html#close

    Parameters
    ----------

    aboutToDestroy : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QWebSocketServerPrivate::close(bool aboutToDestroy)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate5closeEb', aboutToDestroy,
    )

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  def listen(self, address: QHostAddress, port: int = 0) -> bool:
    """
    Calls Qt's 'bool QWebSocketServerPrivate::listen(const QHostAddress
    &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#listen

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QWebSocketServerPrivate::listen(const QHostAddress &address,
    #      quint16 port)
    return self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate6listenERK12QHostAddresst',
        self._valueOf(address), port,
    )

  def nextPendingConnection(self) -> Optional[QWebSocket]:
    """
    Calls Qt's 'QWebSocket
    *QWebSocketServerPrivate::nextPendingConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#nextPendingConnection

    Returns
    -------

    Optional[QWebSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocket *QWebSocketServerPrivate::nextPendingConnection()
    ritual = 'ritual_ZN23QWebSocketServerPrivate21nextPendingConnectionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QWebSocketServerPrivate21nextPendingConnectionEv')
    address = self.uglySide.call(ritual)
    from . import QWebSocket
    return QWebSocket._cuteAt(address)

  def pauseAccepting(self) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::pauseAccepting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#pauseAccepting
    """
    #  void QWebSocketServerPrivate::pauseAccepting()
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate14pauseAcceptingEv',
    )

  def resumeAccepting(self) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::resumeAccepting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#resumeAccepting
    """
    #  void QWebSocketServerPrivate::resumeAccepting()
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate15resumeAcceptingEv',
    )

  @overload(QTcpSocket)
  @overload(NoneType)
  def startHandshakeTimeout(self, pTcpSocket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void
    QWebSocketServerPrivate::startHandshakeTimeout(QTcpSocket *pTcpSocket)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#startHandshakeTimeout

    Parameters
    ----------

    pTcpSocket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServerPrivate::startHandshakeTimeout(QTcpSocket
    #      *pTcpSocket) const
    self.uglySide.call(
        'ritual_ZNK23QWebSocketServerPrivate21startHandshakeTimeoutEP10QTcp'
        'Socket',
        self._addressOf(pTcpSocket),
    )

  @overload(QWebSocket)
  @overload(NoneType)
  def addPendingConnection(self, pWebSocket: Optional[QWebSocket]) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::addPendingConnection(QWebSocket
    *pWebSocket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#addPendingConnection

    Parameters
    ----------

    pWebSocket : Optional[QWebSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServerPrivate::addPendingConnection(QWebSocket
    #      *pWebSocket)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate20addPendingConnectionEP10QWebSo'
        'cket',
        self._addressOf(pWebSocket),
    )

  def onSocketDisconnected(self) -> None:
    """
    Calls Qt's 'void QWebSocketServerPrivate::onSocketDisconnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html#onSocketDisconnected
    """
    #  void QWebSocketServerPrivate::onSocketDisconnected()
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate20onSocketDisconnectedEv',
    )

  @overload(QTcpSocket)
  @overload(NoneType)
  def finishHandshakeTimeout(self, pTcpSocket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void
    QWebSocketServerPrivate::finishHandshakeTimeout(QTcpSocket *pTcpSocket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserverprivate.html

    Parameters
    ----------

    pTcpSocket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServerPrivate::finishHandshakeTimeout(QTcpSocket
    #      *pTcpSocket)
    self.uglySide.call(
        'ritual_ZN23QWebSocketServerPrivate22finishHandshakeTimeoutEP10QTcp'
        'Socket',
        self._addressOf(pTcpSocket),
    )

  @staticmethod
  def handleConnection(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketServerPrivate::handleConnection(QTcpSocket
    *pTcpSocket) const': leans on 'operator<<(QTextStream&,
    QWebSocketHandshakeResponse const&)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketServerPrivate.handleConnection' has no cute function "
        "yet. Qt's 'void "
        "QWebSocketServerPrivate::handleConnection(QTcpSocket *pTcpSocket) "
        "const': leans on 'operator<<(QTextStream&, "
        "QWebSocketHandshakeResponse const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def handshakeReceived(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketServerPrivate::handshakeReceived()': leans on
    'operator<<(QTextStream&, QWebSocketHandshakeResponse const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketServerPrivate.handshakeReceived' has no cute function "
        "yet. Qt's 'void QWebSocketServerPrivate::handshakeReceived()': "
        "leans on 'operator<<(QTextStream&, QWebSocketHandshakeResponse "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketServerPrivate::init()': leans on
    'operator<<(QTextStream&, QWebSocketHandshakeResponse const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketServerPrivate.init' has no cute function yet. Qt's "
        "'void QWebSocketServerPrivate::init()': leans on "
        "'operator<<(QTextStream&, QWebSocketHandshakeResponse const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def onNewConnection(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketServerPrivate::onNewConnection()': leans on
    'operator<<(QTextStream&, QWebSocketHandshakeResponse const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketServerPrivate.onNewConnection' has no cute function "
        "yet. Qt's 'void QWebSocketServerPrivate::onNewConnection()': leans "
        "on 'operator<<(QTextStream&, QWebSocketHandshakeResponse const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def supportedVersions(*__, **_) -> Never:
    """
    Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketServerPrivate::supportedVersions() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebSocketServerPrivate.supportedVersions' has no cute function "
        "yet. Qt's 'QList<QWebSocketProtocol::Version> "
        "QWebSocketServerPrivate::supportedVersions() const': gives a type "
        "Python has no way to take yet.")
