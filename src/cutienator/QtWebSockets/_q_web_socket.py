"""
QWebSocket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/qwebsocket.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtNetwork import QSsl, QAbstractSocket
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from ..QtNetwork import QAuthenticator, QHostAddress, QNetworkProxy
  from ..QtNetwork import QNetworkRequest, QSslConfiguration, QSslError
  from ..QtNetwork import QSslPreSharedKeyAuthenticator, QTcpSocket
  from . import QMaskGenerator, QWebSocketHandshakeOptions, QWebSocketPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAuthenticator = WAIT['QAuthenticator']
  QByteArray = WAIT['QByteArray']
  QMaskGenerator = WAIT['QMaskGenerator']
  QNetworkProxy = WAIT['QNetworkProxy']
  QNetworkRequest = WAIT['QNetworkRequest']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QSslPreSharedKeyAuthenticator = WAIT['QSslPreSharedKeyAuthenticator']
  QTcpSocket = WAIT['QTcpSocket']
  QUrl = WAIT['QUrl']
  QWebSocketHandshakeOptions = WAIT['QWebSocketHandshakeOptions']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebSocket(QObject):
  """
  The cute side of Qt's QWebSocket: a plain Python object standing in front
  of one C++ QWebSocket.

  It is built on the cute 'QObject', as Qt's QWebSocket is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocket that has a ritual and that Python can
  call so far, 71 names in all: 'metaObject', 'tr', 'd_func', 'abort',
  'error', 'errorString', 'flush', 'isValid', 'localAddress', 'localPort',
  'pauseMode', 'peerAddress', 'peerName', 'peerPort', 'proxy', 'setProxy',
  'setMaskGenerator', 'maskGenerator', 'readBufferSize', 'setReadBufferSize',
  'resume', 'setPauseMode', 'state', 'version', 'resourceName', 'requestUrl',
  'request', 'handshakeOptions', 'origin', 'subprotocol', 'closeCode',
  'closeReason', 'sendTextMessage', 'sendBinaryMessage', 'ignoreSslErrors',
  'continueInterruptedHandshake', 'setSslConfiguration', 'sslConfiguration',
  'bytesToWrite', 'setMaxAllowedIncomingFrameSize',
  'maxAllowedIncomingFrameSize', 'setMaxAllowedIncomingMessageSize',
  'maxAllowedIncomingMessageSize', 'maxIncomingMessageSize',
  'maxIncomingFrameSize', 'setOutgoingFrameSize', 'outgoingFrameSize',
  'maxOutgoingFrameSize', 'close', 'open', 'ping', 'aboutToClose',
  'connected', 'disconnected', 'stateChanged', 'proxyAuthenticationRequired',
  'authenticationRequired', 'readChannelFinished', 'textFrameReceived',
  'binaryFrameReceived', 'textMessageReceived', 'binaryMessageReceived',
  'errorOccurred', 'pong', 'bytesWritten', 'peerVerifyError', 'sslErrors',
  'preSharedKeyAuthenticationRequired', 'alertSent', 'alertReceived',
  'handshakeInterruptedOnError'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebSocket::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWebSocket::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QWebSocketPrivate *QWebSocket::d_func() const': takes in
    Python what 'QWebSocketPrivate *QWebSocket::d_func()' takes.
  - Qt's 'QWebSocket::~QWebSocket()': the destructor: Python never removes a
    C++ QWebSocket.

  What has no ritual
  ------------------

  4 of the 86 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebSocket is created at the first use, not by 'QWebSocket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocket.
  - Qt tells when it has removed the C++ QWebSocket. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QWebSocket::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#tr

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
    #  QString QWebSocket::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QWebSocket2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def maxIncomingMessageSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocket::maxIncomingMessageSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#maxIncomingMessageSize
    """
    #  quint64 QWebSocket::maxIncomingMessageSize()
    return Rituals.call('ritual_ZN10QWebSocket22maxIncomingMessageSizeEv')

  @staticmethod
  def maxIncomingFrameSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocket::maxIncomingFrameSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#maxIncomingFrameSize
    """
    #  quint64 QWebSocket::maxIncomingFrameSize()
    return Rituals.call('ritual_ZN10QWebSocket20maxIncomingFrameSizeEv')

  @staticmethod
  def maxOutgoingFrameSize() -> int:
    """
    Calls Qt's 'quint64 QWebSocket::maxOutgoingFrameSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#maxOutgoingFrameSize
    """
    #  quint64 QWebSocket::maxOutgoingFrameSize()
    return Rituals.call('ritual_ZN10QWebSocket20maxOutgoingFrameSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebSocket'

  #  A C++ QWebSocket Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWebSocket'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebSocket::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebSocket::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  def error(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QWebSocket::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#error

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QWebSocket::error() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK10QWebSocket5errorEv',
    ))

  @overload(QAbstractSocket.SocketError)
  def error(self, error: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QWebSocket::error(QAbstractSocket::SocketError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#error

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QWebSocket::error(QAbstractSocket::SocketError error)
    self.uglySide.call(
        'ritual_ZN10QWebSocket5errorEN15QAbstractSocket11SocketErrorE',
        error.value,
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::errorString() const
    return self.uglySide.call('ritual_ZNK10QWebSocket11errorStringEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebSocket::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#isValid
    """
    #  bool QWebSocket::isValid() const
    return self.uglySide.call('ritual_ZNK10QWebSocket7isValidEv')

  def localAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QWebSocket::localAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#localAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QWebSocket::localAddress() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket12localAddressEv')
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def localPort(self) -> int:
    """
    Calls Qt's 'quint16 QWebSocket::localPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#localPort
    """
    #  quint16 QWebSocket::localPort() const
    return self.uglySide.call('ritual_ZNK10QWebSocket9localPortEv')

  def pauseMode(self) -> QAbstractSocket.PauseModes:
    """
    Calls Qt's 'QAbstractSocket::PauseModes QWebSocket::pauseMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#pauseMode

    Returns
    -------

    QAbstractSocket.PauseModes
      The value standing for the combination Qt gave back.
    """
    #  QAbstractSocket::PauseModes QWebSocket::pauseMode() const
    return QAbstractSocket.PauseModes(self.uglySide.call(
        'ritual_ZNK10QWebSocket9pauseModeEv',
    ))

  def peerAddress(self) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress QWebSocket::peerAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#peerAddress

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QWebSocket::peerAddress() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket11peerAddressEv')
    from ..QtNetwork import QHostAddress
    return QHostAddress._cuteOwning(address)

  def peerName(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::peerName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#peerName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::peerName() const
    return self.uglySide.call('ritual_ZNK10QWebSocket8peerNameEv')

  def peerPort(self) -> int:
    """
    Calls Qt's 'quint16 QWebSocket::peerPort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#peerPort
    """
    #  quint16 QWebSocket::peerPort() const
    return self.uglySide.call('ritual_ZNK10QWebSocket8peerPortEv')

  def proxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QWebSocket::proxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#proxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QWebSocket::proxy() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket5proxyEv')
    from ..QtNetwork import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def maskGenerator(self) -> Optional[QMaskGenerator]:
    """
    Calls Qt's 'const QMaskGenerator *QWebSocket::maskGenerator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#maskGenerator

    Returns
    -------

    Optional[QMaskGenerator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMaskGenerator *QWebSocket::maskGenerator() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket13maskGeneratorEv')
    from . import QMaskGenerator
    return QMaskGenerator._cuteAt(address)

  def readBufferSize(self) -> int:
    """
    Calls Qt's 'qint64 QWebSocket::readBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#readBufferSize
    """
    #  qint64 QWebSocket::readBufferSize() const
    return self.uglySide.call('ritual_ZNK10QWebSocket14readBufferSizeEv')

  def state(self) -> QAbstractSocket.SocketState:
    """
    Calls Qt's 'QAbstractSocket::SocketState QWebSocket::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#state

    Returns
    -------

    QAbstractSocket.SocketState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketState(number)' gives.
    """
    #  QAbstractSocket::SocketState QWebSocket::state() const
    return QAbstractSocket.SocketState(self.uglySide.call(
        'ritual_ZNK10QWebSocket5stateEv',
    ))

  def version(self) -> QWebSocketProtocol.Version:
    """
    Calls Qt's 'QWebSocketProtocol::Version QWebSocket::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#version

    Returns
    -------

    QWebSocketProtocol.Version
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.Version(number)' gives.
    """
    #  QWebSocketProtocol::Version QWebSocket::version() const
    return QWebSocketProtocol.Version(self.uglySide.call(
        'ritual_ZNK10QWebSocket7versionEv',
    ))

  def resourceName(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::resourceName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#resourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::resourceName() const
    return self.uglySide.call('ritual_ZNK10QWebSocket12resourceNameEv')

  def requestUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebSocket::requestUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#requestUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebSocket::requestUrl() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket10requestUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def request(self) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QWebSocket::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#request

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QWebSocket::request() const
    address = self.uglySide.call('ritual_ZNK10QWebSocket7requestEv')
    from ..QtNetwork import QNetworkRequest
    return QNetworkRequest._cuteOwning(address)

  def handshakeOptions(self) -> QWebSocketHandshakeOptions:
    """
    Calls Qt's 'QWebSocketHandshakeOptions QWebSocket::handshakeOptions()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#handshakeOptions

    Returns
    -------

    QWebSocketHandshakeOptions
      A new cute QWebSocketHandshakeOptions around the copy Qt gave back.
      Python owns it.
    """
    #  QWebSocketHandshakeOptions QWebSocket::handshakeOptions() const
    address = self.uglySide.call(
        'ritual_ZNK10QWebSocket16handshakeOptionsEv',
    )
    from . import QWebSocketHandshakeOptions
    return QWebSocketHandshakeOptions._cuteOwning(address)

  def origin(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::origin() const
    return self.uglySide.call('ritual_ZNK10QWebSocket6originEv')

  def subprotocol(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::subprotocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#subprotocol

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::subprotocol() const
    return self.uglySide.call('ritual_ZNK10QWebSocket11subprotocolEv')

  def closeCode(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode QWebSocket::closeCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#closeCode

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocket::closeCode() const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK10QWebSocket9closeCodeEv',
    ))

  def closeReason(self) -> str:
    """
    Calls Qt's 'QString QWebSocket::closeReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#closeReason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocket::closeReason() const
    return self.uglySide.call('ritual_ZNK10QWebSocket11closeReasonEv')

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QWebSocket::sslConfiguration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QWebSocket::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK10QWebSocket16sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def bytesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QWebSocket::bytesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#bytesToWrite
    """
    #  qint64 QWebSocket::bytesToWrite() const
    return self.uglySide.call('ritual_ZNK10QWebSocket12bytesToWriteEv')

  def maxAllowedIncomingFrameSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocket::maxAllowedIncomingFrameSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#maxAllowedIncomingFrameSize
    """
    #  quint64 QWebSocket::maxAllowedIncomingFrameSize() const
    return self.uglySide.call(
        'ritual_ZNK10QWebSocket27maxAllowedIncomingFrameSizeEv',
    )

  def maxAllowedIncomingMessageSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocket::maxAllowedIncomingMessageSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#maxAllowedIncomingMessageSize
    """
    #  quint64 QWebSocket::maxAllowedIncomingMessageSize() const
    return self.uglySide.call(
        'ritual_ZNK10QWebSocket29maxAllowedIncomingMessageSizeEv',
    )

  def outgoingFrameSize(self) -> int:
    """
    Calls Qt's 'quint64 QWebSocket::outgoingFrameSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#outgoingFrameSize
    """
    #  quint64 QWebSocket::outgoingFrameSize() const
    return self.uglySide.call('ritual_ZNK10QWebSocket17outgoingFrameSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QWebSocket::setProxy(const QNetworkProxy
    &networkProxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#setProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QWebSocket::setProxy(const QNetworkProxy &networkProxy)
    self.uglySide.call(
        'ritual_ZN10QWebSocket8setProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(QMaskGenerator)
  @overload(NoneType)
  def setMaskGenerator(
      self,
      maskGenerator: Optional[QMaskGenerator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::setMaskGenerator(const QMaskGenerator
    *maskGenerator)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#setMaskGenerator

    Parameters
    ----------

    maskGenerator : Optional[QMaskGenerator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocket::setMaskGenerator(const QMaskGenerator *maskGenerator)
    self.uglySide.call(
        'ritual_ZN10QWebSocket16setMaskGeneratorEPK14QMaskGenerator',
        self._addressOf(maskGenerator),
    )

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QWebSocket::setReadBufferSize(qint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QWebSocket::setReadBufferSize(qint64 size)
    self.uglySide.call('ritual_ZN10QWebSocket17setReadBufferSizeEx', size)

  @overload(QAbstractSocket.PauseModes)
  def setPauseMode(self, pauseMode: QAbstractSocket.PauseModes) -> None:
    """
    Calls Qt's 'void QWebSocket::setPauseMode(QAbstractSocket::PauseModes
    pauseMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#setPauseMode

    Parameters
    ----------

    pauseMode : QAbstractSocket.PauseModes
      Passed on as its number.
    """
    #  void QWebSocket::setPauseMode(QAbstractSocket::PauseModes pauseMode)
    self.uglySide.call(
        'ritual_ZN10QWebSocket12setPauseModeE6QFlagsIN15QAbstractSocket9Pau'
        'seModeEE',
        pauseMode.value,
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QWebSocket::setSslConfiguration(const QSslConfiguration
    &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QWebSocket::setSslConfiguration(const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN10QWebSocket19setSslConfigurationERK17QSslConfiguration',
        self._valueOf(sslConfiguration),
    )

  @overload(int)
  def setMaxAllowedIncomingFrameSize(
      self,
      maxAllowedIncomingFrameSize: int,
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::setMaxAllowedIncomingFrameSize(quint64
    maxAllowedIncomingFrameSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#setMaxAllowedIncomingFrameSize

    Parameters
    ----------

    maxAllowedIncomingFrameSize : int
      Passed on as it is.
    """
    #  void QWebSocket::setMaxAllowedIncomingFrameSize(quint64
    #      maxAllowedIncomingFrameSize)
    self.uglySide.call(
        'ritual_ZN10QWebSocket30setMaxAllowedIncomingFrameSizeEy',
        maxAllowedIncomingFrameSize,
    )

  @overload(int)
  def setMaxAllowedIncomingMessageSize(
      self,
      maxAllowedIncomingMessageSize: int,
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::setMaxAllowedIncomingMessageSize(quint64
    maxAllowedIncomingMessageSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#setMaxAllowedIncomingMessageSize

    Parameters
    ----------

    maxAllowedIncomingMessageSize : int
      Passed on as it is.
    """
    #  void QWebSocket::setMaxAllowedIncomingMessageSize(quint64
    #      maxAllowedIncomingMessageSize)
    self.uglySide.call(
        'ritual_ZN10QWebSocket32setMaxAllowedIncomingMessageSizeEy',
        maxAllowedIncomingMessageSize,
    )

  @overload(int)
  def setOutgoingFrameSize(self, outgoingFrameSize: int) -> None:
    """
    Calls Qt's 'void QWebSocket::setOutgoingFrameSize(quint64
    outgoingFrameSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#setOutgoingFrameSize

    Parameters
    ----------

    outgoingFrameSize : int
      Passed on as it is.
    """
    #  void QWebSocket::setOutgoingFrameSize(quint64 outgoingFrameSize)
    self.uglySide.call(
        'ritual_ZN10QWebSocket20setOutgoingFrameSizeEy', outgoingFrameSize,
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

  @overload()
  @overload(str)
  @overload(str, QWebSocketProtocol.Version)
  @overload(str, QWebSocketProtocol.Version, QObject)
  @overload(str, QWebSocketProtocol.Version, NoneType)
  def __init__(
      self,
      origin: str = '',
      version: QWebSocketProtocol.Version = (
          QWebSocketProtocol.Version.VersionLatest),
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWebSocket::QWebSocket(const QString
    &origin, QWebSocketProtocol::Version version, QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#QWebSocket

    Parameters
    ----------

    origin : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    version : QWebSocketProtocol.Version
      Passed on as its number. May be left out, as in Qt: it is then
      QWebSocketProtocol.Version.VersionLatest.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebSocket::QWebSocket(const QString &origin,
    #      QWebSocketProtocol::Version version, QObject *parent)
    self._noteCreation(QWebSocket, lambda: Rituals.call(
        'ritual_ZN10QWebSocketC1ERK7QStringN18QWebSocketProtocol7VersionEP7'
        'QObject',
        origin, version.value, self._addressOf(parent, 'QObject'),
    ))

  @overload(QTcpSocket, QWebSocketProtocol.Version)
  @overload(NoneType, QWebSocketProtocol.Version)
  @overload(QTcpSocket, QWebSocketProtocol.Version, QObject)
  @overload(QTcpSocket, QWebSocketProtocol.Version, NoneType)
  @overload(NoneType, QWebSocketProtocol.Version, QObject)
  @overload(NoneType, QWebSocketProtocol.Version, NoneType)
  def __init__(
      self,
      pTcpSocket: Optional[QTcpSocket],
      version: QWebSocketProtocol.Version,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWebSocket::QWebSocket(QTcpSocket
    *pTcpSocket, QWebSocketProtocol::Version version, QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#QWebSocket

    Parameters
    ----------

    pTcpSocket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : QWebSocketProtocol.Version
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWebSocket::QWebSocket(QTcpSocket *pTcpSocket,
    #      QWebSocketProtocol::Version version, QObject *parent)
    self._noteCreation(QWebSocket, lambda: Rituals.call(
        'ritual_ZN10QWebSocketC1EP10QTcpSocketN18QWebSocketProtocol7Version'
        'EP7QObject',
        self._addressOf(pTcpSocket), version.value, self._addressOf(parent,
        'QObject'),
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

  def d_func(self) -> Optional[QWebSocketPrivate]:
    """
    Calls Qt's 'QWebSocketPrivate *QWebSocket::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#d_func

    Returns
    -------

    Optional[QWebSocketPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocketPrivate *QWebSocket::d_func()
    address = self.uglySide.call('ritual_ZN10QWebSocket6d_funcEv')
    from . import QWebSocketPrivate
    return QWebSocketPrivate._cuteAt(address)

  def abort(self) -> None:
    """
    Calls Qt's 'void QWebSocket::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#abort
    """
    #  void QWebSocket::abort()
    self.uglySide.call('ritual_ZN10QWebSocket5abortEv')

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QWebSocket::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#flush
    """
    #  bool QWebSocket::flush()
    return self.uglySide.call('ritual_ZN10QWebSocket5flushEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QWebSocket::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#resume
    """
    #  void QWebSocket::resume()
    self.uglySide.call('ritual_ZN10QWebSocket6resumeEv')

  @overload(str)
  def sendTextMessage(self, message: str) -> int:
    """
    Calls Qt's 'qint64 QWebSocket::sendTextMessage(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#sendTextMessage

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qint64 QWebSocket::sendTextMessage(const QString &message)
    return self.uglySide.call(
        'ritual_ZN10QWebSocket15sendTextMessageERK7QString', message,
    )

  @overload(QByteArray)
  def sendBinaryMessage(self, data: QByteArray) -> int:
    """
    Calls Qt's 'qint64 QWebSocket::sendBinaryMessage(const QByteArray
    &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#sendBinaryMessage

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  qint64 QWebSocket::sendBinaryMessage(const QByteArray &data)
    return self.uglySide.call(
        'ritual_ZN10QWebSocket17sendBinaryMessageERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QWebSocket::ignoreSslErrors(const QList<QSslError>
    &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocket::ignoreSslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN10QWebSocket15ignoreSslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QWebSocket::ignoreSslErrors()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#ignoreSslErrors
    """
    #  void QWebSocket::ignoreSslErrors()
    self.uglySide.call('ritual_ZN10QWebSocket15ignoreSslErrorsEv')

  def continueInterruptedHandshake(self) -> None:
    """
    Calls Qt's 'void QWebSocket::continueInterruptedHandshake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#continueInterruptedHandshake
    """
    #  void QWebSocket::continueInterruptedHandshake()
    self.uglySide.call(
        'ritual_ZN10QWebSocket28continueInterruptedHandshakeEv',
    )

  @overload()
  @overload(QWebSocketProtocol.CloseCode)
  @overload(QWebSocketProtocol.CloseCode, str)
  def close(
      self,
      closeCode: QWebSocketProtocol.CloseCode = (
          QWebSocketProtocol.CloseCode.CloseCodeNormal),
      reason: str = '',
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::close(QWebSocketProtocol::CloseCode
    closeCode, const QString &reason)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#close

    Parameters
    ----------

    closeCode : QWebSocketProtocol.CloseCode
      Passed on as its number. May be left out, as in Qt: it is then
      QWebSocketProtocol.CloseCode.CloseCodeNormal.

    reason : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QWebSocket::close(QWebSocketProtocol::CloseCode closeCode, const
    #      QString &reason)
    self.uglySide.call(
        'ritual_ZN10QWebSocket5closeEN18QWebSocketProtocol9CloseCodeERK7QSt'
        'ring',
        closeCode.value, reason,
    )

  @overload(QUrl)
  def open(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QWebSocket::open(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#open

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QWebSocket::open(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN10QWebSocket4openERK4QUrl', self._valueOf(url),
    )

  @overload(QNetworkRequest)
  def open(self, request: QNetworkRequest) -> None:
    """
    Calls Qt's 'void QWebSocket::open(const QNetworkRequest &request)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#open

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.
    """
    #  void QWebSocket::open(const QNetworkRequest &request)
    self.uglySide.call(
        'ritual_ZN10QWebSocket4openERK15QNetworkRequest',
        self._valueOf(request),
    )

  @overload(QUrl, QWebSocketHandshakeOptions)
  def open(self, url: QUrl, options: QWebSocketHandshakeOptions) -> None:
    """
    Calls Qt's 'void QWebSocket::open(const QUrl &url, const
    QWebSocketHandshakeOptions &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#open

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    options : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  void QWebSocket::open(const QUrl &url, const
    #      QWebSocketHandshakeOptions &options)
    self.uglySide.call(
        'ritual_ZN10QWebSocket4openERK4QUrlRK26QWebSocketHandshakeOptions',
        self._valueOf(url), self._valueOf(options),
    )

  @overload(QNetworkRequest, QWebSocketHandshakeOptions)
  def open(
      self,
      request: QNetworkRequest,
      options: QWebSocketHandshakeOptions,
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::open(const QNetworkRequest &request, const
    QWebSocketHandshakeOptions &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#open

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    options : QWebSocketHandshakeOptions
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own.
    """
    #  void QWebSocket::open(const QNetworkRequest &request, const
    #      QWebSocketHandshakeOptions &options)
    self.uglySide.call(
        'ritual_ZN10QWebSocket4openERK15QNetworkRequestRK26QWebSocketHandsh'
        'akeOptions',
        self._valueOf(request), self._valueOf(options),
    )

  @overload()
  @overload(QByteArray)
  def ping(self, payload: Optional[QByteArray] = None) -> None:
    """
    Calls Qt's 'void QWebSocket::ping(const QByteArray &payload)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#ping

    Parameters
    ----------

    payload : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QWebSocket::ping(const QByteArray &payload)
    if payload is None:
      from ..QtCore import QByteArray
      payload = QByteArray()
    self.uglySide.call(
        'ritual_ZN10QWebSocket4pingERK10QByteArray', self._valueOf(payload),
    )

  def aboutToClose(self) -> None:
    """
    Calls Qt's 'void QWebSocket::aboutToClose()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#aboutToClose
    """
    #  void QWebSocket::aboutToClose()
    self.uglySide.call('ritual_ZN10QWebSocket12aboutToCloseEv')

  def connected(self) -> None:
    """
    Calls Qt's 'void QWebSocket::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#connected
    """
    #  void QWebSocket::connected()
    self.uglySide.call('ritual_ZN10QWebSocket9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QWebSocket::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#disconnected
    """
    #  void QWebSocket::disconnected()
    self.uglySide.call('ritual_ZN10QWebSocket12disconnectedEv')

  @overload(QAbstractSocket.SocketState)
  def stateChanged(self, state: QAbstractSocket.SocketState) -> None:
    """
    Calls Qt's 'void QWebSocket::stateChanged(QAbstractSocket::SocketState
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#stateChanged

    Parameters
    ----------

    state : QAbstractSocket.SocketState
      Passed on as its number.
    """
    #  void QWebSocket::stateChanged(QAbstractSocket::SocketState state)
    self.uglySide.call(
        'ritual_ZN10QWebSocket12stateChangedEN15QAbstractSocket11SocketStat'
        'eE',
        state.value,
    )

  @overload(QNetworkProxy, QAuthenticator)
  @overload(QNetworkProxy, NoneType)
  def proxyAuthenticationRequired(
      self,
      proxy: QNetworkProxy,
      pAuthenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::proxyAuthenticationRequired(const
    QNetworkProxy &proxy, QAuthenticator *pAuthenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#proxyAuthenticationRequired

    Parameters
    ----------

    proxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.

    pAuthenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocket::proxyAuthenticationRequired(const QNetworkProxy
    #      &proxy, QAuthenticator *pAuthenticator)
    self.uglySide.call(
        'ritual_ZN10QWebSocket27proxyAuthenticationRequiredERK13QNetworkPro'
        'xyP14QAuthenticator',
        self._valueOf(proxy), self._addressOf(pAuthenticator),
    )

  @overload(QAuthenticator)
  @overload(NoneType)
  def authenticationRequired(
      self,
      authenticator: Optional[QAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::authenticationRequired(QAuthenticator
    *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#authenticationRequired

    Parameters
    ----------

    authenticator : Optional[QAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocket::authenticationRequired(QAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN10QWebSocket22authenticationRequiredEP14QAuthenticator',
        self._addressOf(authenticator),
    )

  def readChannelFinished(self) -> None:
    """
    Calls Qt's 'void QWebSocket::readChannelFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#readChannelFinished
    """
    #  void QWebSocket::readChannelFinished()
    self.uglySide.call('ritual_ZN10QWebSocket19readChannelFinishedEv')

  @overload(str, bool)
  def textFrameReceived(self, frame: str, isLastFrame: bool) -> None:
    """
    Calls Qt's 'void QWebSocket::textFrameReceived(const QString &frame, bool
    isLastFrame)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#textFrameReceived

    Parameters
    ----------

    frame : str
      Passed on as it is: a QString is made of it for the call.

    isLastFrame : bool
      Passed on as it is.
    """
    #  void QWebSocket::textFrameReceived(const QString &frame, bool
    #      isLastFrame)
    self.uglySide.call(
        'ritual_ZN10QWebSocket17textFrameReceivedERK7QStringb',
        frame, isLastFrame,
    )

  @overload(QByteArray, bool)
  def binaryFrameReceived(
      self,
      frame: QByteArray,
      isLastFrame: bool,
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::binaryFrameReceived(const QByteArray &frame,
    bool isLastFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#binaryFrameReceived

    Parameters
    ----------

    frame : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    isLastFrame : bool
      Passed on as it is.
    """
    #  void QWebSocket::binaryFrameReceived(const QByteArray &frame, bool
    #      isLastFrame)
    self.uglySide.call(
        'ritual_ZN10QWebSocket19binaryFrameReceivedERK10QByteArrayb',
        self._valueOf(frame), isLastFrame,
    )

  @overload(str)
  def textMessageReceived(self, message: str) -> None:
    """
    Calls Qt's 'void QWebSocket::textMessageReceived(const QString
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#textMessageReceived

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocket::textMessageReceived(const QString &message)
    self.uglySide.call(
        'ritual_ZN10QWebSocket19textMessageReceivedERK7QString', message,
    )

  @overload(QByteArray)
  def binaryMessageReceived(self, message: QByteArray) -> None:
    """
    Calls Qt's 'void QWebSocket::binaryMessageReceived(const QByteArray
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#binaryMessageReceived

    Parameters
    ----------

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebSocket::binaryMessageReceived(const QByteArray &message)
    self.uglySide.call(
        'ritual_ZN10QWebSocket21binaryMessageReceivedERK10QByteArray',
        self._valueOf(message),
    )

  @overload(QAbstractSocket.SocketError)
  def errorOccurred(self, error: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void QWebSocket::errorOccurred(QAbstractSocket::SocketError
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#errorOccurred

    Parameters
    ----------

    error : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QWebSocket::errorOccurred(QAbstractSocket::SocketError error)
    self.uglySide.call(
        'ritual_ZN10QWebSocket13errorOccurredEN15QAbstractSocket11SocketErr'
        'orE',
        error.value,
    )

  @overload(int, QByteArray)
  def pong(self, elapsedTime: int, payload: QByteArray) -> None:
    """
    Calls Qt's 'void QWebSocket::pong(quint64 elapsedTime, const QByteArray
    &payload)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#pong

    Parameters
    ----------

    elapsedTime : int
      Passed on as it is.

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWebSocket::pong(quint64 elapsedTime, const QByteArray &payload)
    self.uglySide.call(
        'ritual_ZN10QWebSocket4pongEyRK10QByteArray',
        elapsedTime, self._valueOf(payload),
    )

  @overload(int)
  def bytesWritten(self, bytes: int) -> None:
    """
    Calls Qt's 'void QWebSocket::bytesWritten(qint64 bytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#bytesWritten

    Parameters
    ----------

    bytes : int
      Passed on as it is.
    """
    #  void QWebSocket::bytesWritten(qint64 bytes)
    self.uglySide.call('ritual_ZN10QWebSocket12bytesWrittenEx', bytes)

  @overload(QSslError)
  def peerVerifyError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QWebSocket::peerVerifyError(const QSslError &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#peerVerifyError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QWebSocket::peerVerifyError(const QSslError &error)
    self.uglySide.call(
        'ritual_ZN10QWebSocket15peerVerifyErrorERK9QSslError',
        self._valueOf(error),
    )

  @overload(QList[QSslError])
  def sslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QWebSocket::sslErrors(const QList<QSslError> &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#sslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocket::sslErrors(const QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN10QWebSocket9sslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload(QSslPreSharedKeyAuthenticator)
  @overload(NoneType)
  def preSharedKeyAuthenticationRequired(
      self,
      authenticator: Optional[QSslPreSharedKeyAuthenticator],
  ) -> None:
    """
    Calls Qt's 'void QWebSocket::preSharedKeyAuthenticationRequired(
    QSslPreSharedKeyAuthenticator *authenticator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#preSharedKeyAuthenticationRequired

    Parameters
    ----------

    authenticator : Optional[QSslPreSharedKeyAuthenticator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebSocket::preSharedKeyAuthenticationRequired(
    #      QSslPreSharedKeyAuthenticator *authenticator)
    self.uglySide.call(
        'ritual_ZN10QWebSocket34preSharedKeyAuthenticationRequiredEP29QSslP'
        'reSharedKeyAuthenticator',
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
    Calls Qt's 'void QWebSocket::alertSent(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#alertSent

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocket::alertSent(QSsl::AlertLevel level, QSsl::AlertType
    #      type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QWebSocket9alertSentEN4QSsl10AlertLevelENS0_9AlertTypeE'
        'RK7QString',
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
    Calls Qt's 'void QWebSocket::alertReceived(QSsl::AlertLevel level,
    QSsl::AlertType type, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocket.html#alertReceived

    Parameters
    ----------

    level : QSsl.AlertLevel
      Passed on as its number.

    type : QSsl.AlertType
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocket::alertReceived(QSsl::AlertLevel level, QSsl::AlertType
    #      type, const QString &description)
    self.uglySide.call(
        'ritual_ZN10QWebSocket13alertReceivedEN4QSsl10AlertLevelENS0_9Alert'
        'TypeERK7QString',
        level.value, type.value, description,
    )

  @overload(QSslError)
  def handshakeInterruptedOnError(self, error: QSslError) -> None:
    """
    Calls Qt's 'void QWebSocket::handshakeInterruptedOnError(const QSslError
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocket.html#handshakeInterruptedOnError

    Parameters
    ----------

    error : QSslError
      Passed on as a value: Qt reads the C++ QSslError, which stays Python's
      own.
    """
    #  void QWebSocket::handshakeInterruptedOnError(const QSslError &error)
    self.uglySide.call(
        'ritual_ZN10QWebSocket27handshakeInterruptedOnErrorERK9QSslError',
        self._valueOf(error),
    )
