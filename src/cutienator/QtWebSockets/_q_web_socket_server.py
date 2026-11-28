"""
QWebSocketServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/qwebsocketserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QStringList
from ..QtNetwork import QSsl, QAbstractSocket
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtNetwork import QHostAddress, QNetworkProxy, QSslConfiguration
  from ..QtNetwork import QSslError, QSslPreSharedKeyAuthenticator
  from ..QtNetwork import QSslSocket, QTcpSocket
  from . import QWebSocket, QWebSocketCorsAuthenticator
  from . import QWebSocketServerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QSslSocket = WAIT['QSslSocket']
  QTcpSocket = WAIT['QTcpSocket']
  QWebSocketCorsAuthenticator = WAIT['QWebSocketCorsAuthenticator']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebSocketServer(QObject):
  """
  The cute side of Qt's QWebSocketServer: a plain Python object standing in
  front of one C++ QWebSocketServer.

  It is built on the cute 'QObject', as Qt's QWebSocketServer is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocketServer that has a ritual and that Python
  can call so far, 45 names in all: 'metaObject', 'tr', 'd_func', 'listen',
  'close', 'isListening', 'setMaxPendingConnections',
  'maxPendingConnections', 'setHandshakeTimeout', 'handshakeTimeoutMS',
  'serverPort', 'serverAddress', 'serverUrl', 'secureMode',
  'setSocketDescriptor', 'socketDescriptor', 'setNativeDescriptor',
  'nativeDescriptor', 'hasPendingConnections', 'nextPendingConnection',
  'error', 'errorString', 'pauseAccepting', 'resumeAccepting',
  'setServerName', 'serverName', 'setSupportedSubprotocols',
  'supportedSubprotocols', 'setProxy', 'proxy', 'setSslConfiguration',
  'sslConfiguration', 'handleConnection', 'acceptError', 'serverError',
  'originAuthenticationRequired', 'newConnection', 'peerVerifyError',
  'sslErrors', 'sslErrorsOccurred', 'preSharedKeyAuthenticationRequired',
  'alertSent', 'alertReceived', 'handshakeInterruptedOnError', 'closed'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebSocketServer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWebSocketServer::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWebSocketServerPrivate *QWebSocketServer::d_func() const':
    takes in Python what 'QWebSocketServerPrivate
    *QWebSocketServer::d_func()' takes.
  - Qt's 'QWebSocketServer::~QWebSocketServer()': the destructor: Python
    never removes a C++ QWebSocketServer.
  - Qt's 'void
    QWebSocketServer::setHandshakeTimeout(std::chrono::milliseconds msec)':
    takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QWebSocketServer::handshakeTimeout()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketServer::supportedVersions() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  4 of the 57 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebSocketServer is created at the first use, not by
    'QWebSocketServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketServer.
  - Qt tells when it has removed the C++ QWebSocketServer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebSocketServer that has no cute function yet,
    'handshakeTimeout', 'supportedVersions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWebSocketServer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SslMode(CuteNum):
    """
    The enum 'QWebSocketServer::SslMode' of Qt, with the 2 names Qt gives in
    it.
    """

    SecureMode = Kee[int](0)
    NonSecureMode = Kee[int](1)

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
    Calls Qt's 'QString QWebSocketServer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#tr

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
    #  QString QWebSocketServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QWebSocketServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocketServer'

  #  A C++ QWebSocketServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebSocketServer'

  #  The functions Qt calls itself that QWebSocketServer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'nextPendingConnection': (
          ('_ZN16QWebSocketServer21nextPendingConnectionEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebSocketServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebSocketServer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QWebSocketServer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isListening(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketServer::isListening() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#isListening
    """
    #  bool QWebSocketServer::isListening() const
    return self.uglySide.call('ritual_ZNK16QWebSocketServer11isListeningEv')

  def maxPendingConnections(self) -> int:
    """
    Calls Qt's 'int QWebSocketServer::maxPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#maxPendingConnections
    """
    #  int QWebSocketServer::maxPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK16QWebSocketServer21maxPendingConnectionsEv',
    )

  def handshakeTimeoutMS(self) -> int:
    """
    Calls Qt's 'int QWebSocketServer::handshakeTimeoutMS() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#handshakeTimeoutMS
    """
    #  int QWebSocketServer::handshakeTimeoutMS() const
    return self.uglySide.call(
        'ritual_ZNK16QWebSocketServer18handshakeTimeoutMSEv',
    )

  def serverPort(self) -> int:
    """
    Calls Qt's 'quint16 QWebSocketServer::serverPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#serverPort
    """
    #  quint16 QWebSocketServer::serverPort() const
    return self.uglySide.call('ritual_ZNK16QWebSocketServer10serverPortEv')

  def serverAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QWebSocketServer::serverAddress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#serverAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QWebSocketServer::serverAddress() const
    address = self.uglySide.call(
        'ritual_ZNK16QWebSocketServer13serverAddressEv',
    )
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def serverUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebSocketServer::serverUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#serverUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebSocketServer::serverUrl() const
    address = self.uglySide.call('ritual_ZNK16QWebSocketServer9serverUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def secureMode(self) -> SslMode:
    """
    Calls Qt's 'SslMode QWebSocketServer::secureMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#secureMode

    Returns
    -------

    SslMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SslMode(number)' gives.
    """
    #  SslMode QWebSocketServer::secureMode() const
    return QWebSocketServer.SslMode(self.uglySide.call(
        'ritual_ZNK16QWebSocketServer10secureModeEv',
    ))

  def socketDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QWebSocketServer::socketDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#socketDescriptor
    """
    #  qintptr QWebSocketServer::socketDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK16QWebSocketServer16socketDescriptorEv',
    )

  def nativeDescriptor(self) -> int:
    """
    Calls Qt's 'qintptr QWebSocketServer::nativeDescriptor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#nativeDescriptor
    """
    #  qintptr QWebSocketServer::nativeDescriptor() const
    return self.uglySide.call(
        'ritual_ZNK16QWebSocketServer16nativeDescriptorEv',
    )

  def hasPendingConnections(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketServer::hasPendingConnections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#hasPendingConnections
    """
    #  bool QWebSocketServer::hasPendingConnections() const
    return self.uglySide.call(
        'ritual_ZNK16QWebSocketServer21hasPendingConnectionsEv',
    )

  def error(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode QWebSocketServer::error()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#error

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocketServer::error() const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK16QWebSocketServer5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebSocketServer::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketServer::errorString() const
    return self.uglySide.call('ritual_ZNK16QWebSocketServer11errorStringEv')

  def serverName(self) -> str:
    """
    Calls Qt's 'QString QWebSocketServer::serverName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#serverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketServer::serverName() const
    return self.uglySide.call('ritual_ZNK16QWebSocketServer10serverNameEv')

  def supportedSubprotocols(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebSocketServer::supportedSubprotocols() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#supportedSubprotocols

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebSocketServer::supportedSubprotocols() const
    address = self.uglySide.call(
        'ritual_ZNK16QWebSocketServer21supportedSubprotocolsEv',
    )
    return QStringList._cuteOwning(address)

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QWebSocketServer::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QWebSocketServer::proxy() const
    address = self.uglySide.call('ritual_ZNK16QWebSocketServer5proxyEv')
    from ..QtNetwork import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QWebSocketServer::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QWebSocketServer::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK16QWebSocketServer16sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxPendingConnections(self, numConnections: int) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setMaxPendingConnections(int
    numConnections)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setMaxPendingConnections

    Parameters
    ----------

    numConnections : int
      Passed on as it is.
    """
    #  void QWebSocketServer::setMaxPendingConnections(int numConnections)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer24setMaxPendingConnectionsEi',
        numConnections,
    )

  @overload(int)
  def setHandshakeTimeout(self, msec: int) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setHandshakeTimeout(int msec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setHandshakeTimeout

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QWebSocketServer::setHandshakeTimeout(int msec)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer19setHandshakeTimeoutEi', msec,
    )

  @overload(int)
  def setSocketDescriptor(self, socketDescriptor: int) -> bool:
    """
    Calls Qt's 'bool QWebSocketServer::setSocketDescriptor(qintptr
    socketDescriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setSocketDescriptor

    Parameters
    ----------

    socketDescriptor : int
      Passed on as it is.
    """
    #  bool QWebSocketServer::setSocketDescriptor(qintptr socketDescriptor)
    return self.uglySide.call(
        'ritual_ZN16QWebSocketServer19setSocketDescriptorEx',
        socketDescriptor,
    )

  @overload(int)
  def setNativeDescriptor(self, descriptor: int) -> bool:
    """
    Calls Qt's 'bool QWebSocketServer::setNativeDescriptor(qintptr
    descriptor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setNativeDescriptor

    Parameters
    ----------

    descriptor : int
      Passed on as it is.
    """
    #  bool QWebSocketServer::setNativeDescriptor(qintptr descriptor)
    return self.uglySide.call(
        'ritual_ZN16QWebSocketServer19setNativeDescriptorEx', descriptor,
    )

  @overload(str)
  def setServerName(self, serverName: str) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setServerName(const QString
    &serverName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setServerName

    Parameters
    ----------

    serverName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServer::setServerName(const QString &serverName)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer13setServerNameERK7QString', serverName,
    )

  @overload(QStringList)
  def setSupportedSubprotocols(self, protocols: QStringList) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setSupportedSubprotocols(const
    QStringList &protocols)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setSupportedSubprotocols

    Parameters
    ----------

    protocols : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketServer::setSupportedSubprotocols(const QStringList
    #      &protocols)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer24setSupportedSubprotocolsERK5QListI7QS'
        'tringE',
        self._valueOf(protocols),
    )

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QWebSocketServer::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QWebSocketServer::setSslConfiguration(const
    QSslConfiguration &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QWebSocketServer::setSslConfiguration(const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer19setSslConfigurationERK17QSslConfigura'
        'tion',
        self._valueOf(sslConfiguration),
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
  @overload(str, SslMode, QObject)
  @overload(str, SslMode, NoneType)
  def __init__(
      self,
      serverName: str,
      secureMode: SslMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWebSocketServer::QWebSocketServer(const
    QString &serverName, SslMode secureMode, QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#QWebSocketServer

    Parameters
    ----------

    serverName : str
      Passed on as it is: a QString is made of it for the call.

    secureMode : SslMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebSocketServer::QWebSocketServer(const QString &serverName, SslMode
    #      secureMode, QObject *parent)
    self._noteCreation(QWebSocketServer, lambda: Rituals.call(
        'ritual_ZN16QWebSocketServerC1ERK7QStringNS_7SslModeEP7QObject',
        serverName, secureMode.value, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QWebSocketServerPrivate]:
    """
    Calls Qt's 'QWebSocketServerPrivate *QWebSocketServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#d_func

    Returns
    -------

    Optional[QWebSocketServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocketServerPrivate *QWebSocketServer::d_func()
    address = self.uglySide.call('ritual_ZN16QWebSocketServer6d_funcEv')
    from . import QWebSocketServerPrivate
    return QWebSocketServerPrivate._cuteAt(address)

  @overload(QHostAddress)
  @overload(QHostAddress, int)
  def listen(self, address: QHostAddress, port: int = 0) -> bool:
    """
    Calls Qt's 'bool QWebSocketServer::listen(const QHostAddress &address,
    quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#listen

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QWebSocketServer::listen(const QHostAddress &address, quint16
    #      port)
    return self.uglySide.call(
        'ritual_ZN16QWebSocketServer6listenERK12QHostAddresst',
        self._valueOf(address), port,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QWebSocketServer::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#close
    """
    #  void QWebSocketServer::close()
    self.uglySide.call('ritual_ZN16QWebSocketServer5closeEv')

  def nextPendingConnection(self) -> Optional[QWebSocket]:
    """
    Calls Qt's 'QWebSocket *QWebSocketServer::nextPendingConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#nextPendingConnection

    Returns
    -------

    Optional[QWebSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocket *QWebSocketServer::nextPendingConnection()
    ritual = 'ritual_ZN16QWebSocketServer21nextPendingConnectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWebSocketServer21nextPendingConnectionEv'
    address = self.uglySide.call(ritual)
    from . import QWebSocket
    return QWebSocket._cuteAt(address)

  def pauseAccepting(self) -> None:
    """
    Calls Qt's 'void QWebSocketServer::pauseAccepting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#pauseAccepting
    """
    #  void QWebSocketServer::pauseAccepting()
    self.uglySide.call('ritual_ZN16QWebSocketServer14pauseAcceptingEv')

  def resumeAccepting(self) -> None:
    """
    Calls Qt's 'void QWebSocketServer::resumeAccepting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#resumeAccepting
    """
    #  void QWebSocketServer::resumeAccepting()
    self.uglySide.call('ritual_ZN16QWebSocketServer15resumeAcceptingEv')

  @overload(QTcpSocket)
  @overload(NoneType)
  def handleConnection(self, socket: Optional[QTcpSocket]) -> None:
    """
    Calls Qt's 'void QWebSocketServer::handleConnection(QTcpSocket *socket)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#handleConnection

    Parameters
    ----------

    socket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServer::handleConnection(QTcpSocket *socket) const
    self.uglySide.call(
        'ritual_ZNK16QWebSocketServer16handleConnectionEP10QTcpSocket',
        self._addressOf(socket),
    )

  @overload(QAbstractSocket.SocketError)
  def acceptError(self, socketError: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void
    QWebSocketServer::acceptError(QAbstractSocket::SocketError socketError)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#acceptError

    Parameters
    ----------

    socketError : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QWebSocketServer::acceptError(QAbstractSocket::SocketError
    #      socketError)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer11acceptErrorEN15QAbstractSocket11Socke'
        'tErrorE',
        socketError.value,
    )

  @overload(QWebSocketProtocol.CloseCode)
  def serverError(self, closeCode: QWebSocketProtocol.CloseCode) -> None:
    """
    Calls Qt's 'void
    QWebSocketServer::serverError(QWebSocketProtocol::CloseCode closeCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#serverError

    Parameters
    ----------

    closeCode : QWebSocketProtocol.CloseCode
      Passed on as its number.
    """
    #  void QWebSocketServer::serverError(QWebSocketProtocol::CloseCode
    #      closeCode)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer11serverErrorEN18QWebSocketProtocol9Clo'
        'seCodeE',
        closeCode.value,
    )

  @overload(QWebSocketCorsAuthenticator)
  @overload(NoneType)
  def originAuthenticationRequired(
      self,
      pAuthenticator: Optional[QWebSocketCorsAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocketServer::originAuthenticationRequired(
    QWebSocketCorsAuthenticator *pAuthenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#originAuthenticationRequired

    Parameters
    ----------

    pAuthenticator : Optional[QWebSocketCorsAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServer::originAuthenticationRequired(
    #      QWebSocketCorsAuthenticator *pAuthenticator)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer28originAuthenticationRequiredEP27QWebS'
        'ocketCorsAuthenticator',
        self._addressOf(pAuthenticator),
    )

  def newConnection(self) -> None:
    """
    Calls Qt's 'void QWebSocketServer::newConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#newConnection
    """
    #  void QWebSocketServer::newConnection()
    self.uglySide.call('ritual_ZN16QWebSocketServer13newConnectionEv')

  @overload(QSslError)
  def peerVerifyError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QWebSocketServer::peerVerifyError(const QSslError
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#peerVerifyError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QWebSocketServer::peerVerifyError(const QSslError &error)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer15peerVerifyErrorERK9QSslError',
        self._valueOf(error),
    )

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QWebSocketServer::sslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketServer::sslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslSocket, QList[QSslError])
  @overload(NoneType, QList[QSslError])
  def sslErrorsOccurred(
      self,
      socket: Optional[QSslSocket],
      errors: QList[QSslError],
  ) -> None:
    """
    Calls Qt's 'void QWebSocketServer::sslErrorsOccurred(QSslSocket *socket,
    const QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#sslErrorsOccurred

    Parameters
    ----------

    socket : Optional[QSslSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketServer::sslErrorsOccurred(QSslSocket *socket, const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer17sslErrorsOccurredEP10QSslSocketRK5QLi'
        'stI9QSslErrorE',
        self._addressOf(socket), self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocketServer::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocketServer::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer34preSharedKeyAuthenticationRequiredEP2'
        '9QSslPreSharedKeyAuthenticator',
        self._addressOf(authenticator),
    )

  @overload(QSsl.AlertLevel, QSsl.AlertType, str)
  def alertSent(
      self,
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QWebSocketServer::alertSent(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#alertSent

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServer::alertSent(QSsl::AlertLevel level,
    #      QSsl::AlertType type, const QString &description)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer9alertSentEN4QSsl10AlertLevelENS0_9Aler'
        'tTypeERK7QString',
        level.value, type.value, description,
    )

  @overload(QSsl.AlertLevel, QSsl.AlertType, str)
  def alertReceived(
      self,
      level: QSsl.AlertLevel,
      type: QSsl.AlertType,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QWebSocketServer::alertReceived(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#alertReceived

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketServer::alertReceived(QSsl::AlertLevel level,
    #      QSsl::AlertType type, const QString &description)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer13alertReceivedEN4QSsl10AlertLevelENS0_'
        '9AlertTypeERK7QString',
        level.value, type.value, description,
    )

  @overload(QSslError)
  def handshakeInterruptedOnError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QWebSocketServer::handshakeInterruptedOnError(const
    QSslError &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketserver.html#handshakeInterruptedOnError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QWebSocketServer::handshakeInterruptedOnError(const QSslError
    #      &error)
    self.uglySide.call(
        'ritual_ZN16QWebSocketServer27handshakeInterruptedOnErrorERK9QSslEr'
        'ror',
        self._valueOf(error),
    )

  def closed(self) -> None:
    """
    Calls Qt's 'void QWebSocketServer::closed()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketserver.html#closed
    """
    #  void QWebSocketServer::closed()
    self.uglySide.call('ritual_ZN16QWebSocketServer6closedEv')

  @staticmethod
  def handshakeTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QWebSocketServer::handshakeTimeout()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWebSocketServer.handshakeTimeout' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QWebSocketServer::handshakeTimeout() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def supportedVersions(*__, **_) -> Never:
    """
    Qt's 'QList<QWebSocketProtocol::Version>
    QWebSocketServer::supportedVersions() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QWebSocketServer.supportedVersions' has no cute function yet. "
        "Qt's 'QList<QWebSocketProtocol::Version> "
        "QWebSocketServer::supportedVersions() const': gives a type Python "
        "has no way to take yet.")
