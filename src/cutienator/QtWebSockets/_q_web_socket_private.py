"""
QWebSocketPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWebSocketPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObjectPrivate, QStringList
from ..QtNetwork import QAbstractSocket
from . import QWebSocketProtocol

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from ..QtNetwork import QNetworkRequest, QSslConfiguration, QSslError
  from . import QWebSocket, QWebSocketHandshakeOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNetworkRequest = WAIT['QNetworkRequest']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QWebSocketHandshakeOptions = WAIT['QWebSocketHandshakeOptions']


class QWebSocketPrivate(QObjectPrivate):
  """
  The cute side of Qt's QWebSocketPrivate: a plain Python object standing in
  front of one C++ QWebSocketPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QWebSocketPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebSocketPrivate that has a ritual and that Python
  can call so far, 32 names in all: 'q_func', 'abort', 'error',
  'errorString', 'flush', 'version', 'resourceName', 'request', 'origin',
  'handshakeOptions', 'protocol', 'extension', 'closeCode', 'closeReason',
  'ignoreSslErrors', 'continueInterruptedHandshake', 'setSslConfiguration',
  'sslConfiguration', '_q_updateSslConfiguration', 'setVersion',
  'setResourceName', 'setRequest', 'setOrigin', 'setProtocol',
  'setExtension', 'enableMasking', 'requestedSubProtocols',
  'calculateAcceptKey', 'generateMaskingKey', 'generateKey', 'writeFrames',
  'writeFrame'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWebSocket *QWebSocketPrivate::q_func() const': takes in
    Python what 'QWebSocket *QWebSocketPrivate::q_func()' takes.
  - Qt's 'QWebSocketPrivate::~QWebSocketPrivate()': the destructor: Python
    never removes a C++ QWebSocketPrivate.
  - Qt's 'QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *tcpSocket,
    const QWebSocketHandshakeRequest &request, const
    QWebSocketHandshakeResponse &response, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  53 of the 89 functions Qt declares: 40 cannot be called and cannot be
  called through the meta-object and cannot be copied; 7 leans on
  'QWebSocketPrivate; 3 Qt's library has no name for it, and its code in Qt's
  source does not compile apart from its file; 2 forbidden; 1 leans on
  'QWebSocketDataProcessor.

  What to expect
  --------------

  - The C++ QWebSocketPrivate is created at the first use, not by
    'QWebSocketPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebSocketPrivate.
  - Each name of Qt's QWebSocketPrivate that has no cute function yet,
    '__init__', 'close', 'closeGoingAway', 'createHandShakeRequest',
    'doClose', 'doWriteFrames', 'emitErrorOccurred', 'getFrameHeader',
    'init', 'isValid', 'localAddress', 'localPort', 'makeConnections',
    'maskGenerator', 'maxAllowedIncomingFrameSize',
    'maxAllowedIncomingMessageSize', 'maxIncomingFrameSize',
    'maxIncomingMessageSize', 'maxOutgoingFrameSize', 'open',
    'outgoingFrameSize', 'pauseMode', 'peerAddress', 'peerName', 'peerPort',
    'ping', 'processClose', 'processData', 'processError',
    'processHandshake', 'processPing', 'processPong', 'processStateChanged',
    'proxy', 'readBufferSize', 'releaseConnections', 'resume',
    'sendBinaryMessage', 'sendTextMessage', 'setErrorString',
    'setMaskGenerator', 'setMaxAllowedIncomingFrameSize',
    'setMaxAllowedIncomingMessageSize', 'setOutgoingFrameSize',
    'setPauseMode', 'setProxy', 'setReadBufferSize', 'setSocketState',
    'socketDestroyed', 'state', 'upgradeFrom', holds a function that raises
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
  __qt_class__ = 'QWebSocketPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def error(self) -> QAbstractSocket.SocketError:
    """
    Calls Qt's 'QAbstractSocket::SocketError QWebSocketPrivate::error()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#error

    Returns
    -------

    QAbstractSocket.SocketError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractSocket.SocketError(number)' gives.
    """
    #  QAbstractSocket::SocketError QWebSocketPrivate::error() const
    return QAbstractSocket.SocketError(self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::errorString() const
    return self.uglySide.call('ritual_ZNK17QWebSocketPrivate11errorStringEv')

  def version(self) -> QWebSocketProtocol.Version:
    """
    Calls Qt's 'QWebSocketProtocol::Version QWebSocketPrivate::version()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#version

    Returns
    -------

    QWebSocketProtocol.Version
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.Version(number)' gives.
    """
    #  QWebSocketProtocol::Version QWebSocketPrivate::version() const
    return QWebSocketProtocol.Version(self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate7versionEv',
    ))

  def resourceName(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::resourceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#resourceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::resourceName() const
    return self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate12resourceNameEv',
    )

  def request(self) -> QNetworkRequest:
    """
    Calls Qt's 'QNetworkRequest QWebSocketPrivate::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#request

    Returns
    -------

    QNetworkRequest
      A new cute QNetworkRequest around the copy Qt gave back. Python owns
      it.
    """
    #  QNetworkRequest QWebSocketPrivate::request() const
    address = self.uglySide.call('ritual_ZNK17QWebSocketPrivate7requestEv')
    from ..QtNetwork import QNetworkRequest
    return QNetworkRequest._cuteOwning(address)

  def origin(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#origin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::origin() const
    return self.uglySide.call('ritual_ZNK17QWebSocketPrivate6originEv')

  def handshakeOptions(self) -> QWebSocketHandshakeOptions:
    """
    Calls Qt's 'QWebSocketHandshakeOptions
    QWebSocketPrivate::handshakeOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#handshakeOptions

    Returns
    -------

    QWebSocketHandshakeOptions
      A new cute QWebSocketHandshakeOptions around the copy Qt gave back.
      Python owns it.
    """
    #  QWebSocketHandshakeOptions QWebSocketPrivate::handshakeOptions() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate16handshakeOptionsEv',
    )
    from . import QWebSocketHandshakeOptions
    return QWebSocketHandshakeOptions._cuteOwning(address)

  def protocol(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::protocol() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#protocol

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::protocol() const
    return self.uglySide.call('ritual_ZNK17QWebSocketPrivate8protocolEv')

  def extension(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::extension() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#extension

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::extension() const
    return self.uglySide.call('ritual_ZNK17QWebSocketPrivate9extensionEv')

  def closeCode(self) -> QWebSocketProtocol.CloseCode:
    """
    Calls Qt's 'QWebSocketProtocol::CloseCode QWebSocketPrivate::closeCode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#closeCode

    Returns
    -------

    QWebSocketProtocol.CloseCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QWebSocketProtocol.CloseCode(number)' gives.
    """
    #  QWebSocketProtocol::CloseCode QWebSocketPrivate::closeCode() const
    return QWebSocketProtocol.CloseCode(self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate9closeCodeEv',
    ))

  def closeReason(self) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::closeReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#closeReason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::closeReason() const
    return self.uglySide.call('ritual_ZNK17QWebSocketPrivate11closeReasonEv')

  def sslConfiguration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QWebSocketPrivate::sslConfiguration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#sslConfiguration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QWebSocketPrivate::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate16sslConfigurationEv',
    )
    from ..QtNetwork import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def requestedSubProtocols(self) -> QStringList:
    """
    Calls Qt's 'QStringList QWebSocketPrivate::requestedSubProtocols()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#requestedSubProtocols

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QWebSocketPrivate::requestedSubProtocols() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate21requestedSubProtocolsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QByteArray)
  def calculateAcceptKey(self, key: QByteArray) -> str:
    """
    Calls Qt's 'QString QWebSocketPrivate::calculateAcceptKey(const
    QByteArray &key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#calculateAcceptKey

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWebSocketPrivate::calculateAcceptKey(const QByteArray &key)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate18calculateAcceptKeyERK10QByteArray',
        self._valueOf(key),
    )

  def generateMaskingKey(self) -> int:
    """
    Calls Qt's 'quint32 QWebSocketPrivate::generateMaskingKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#generateMaskingKey
    """
    #  quint32 QWebSocketPrivate::generateMaskingKey() const
    return self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate18generateMaskingKeyEv',
    )

  def generateKey(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWebSocketPrivate::generateKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#generateKey

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWebSocketPrivate::generateKey() const
    address = self.uglySide.call(
        'ritual_ZNK17QWebSocketPrivate11generateKeyEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslConfiguration)
  def setSslConfiguration(self, sslConfiguration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setSslConfiguration(const
    QSslConfiguration &sslConfiguration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#setSslConfiguration

    Parameters
    ----------

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QWebSocketPrivate::setSslConfiguration(const QSslConfiguration
    #      &sslConfiguration)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate19setSslConfigurationERK17QSslConfigur'
        'ation',
        self._valueOf(sslConfiguration),
    )

  @overload(QWebSocketProtocol.Version)
  def setVersion(self, version: QWebSocketProtocol.Version) -> None:
    """
    Calls Qt's 'void
    QWebSocketPrivate::setVersion(QWebSocketProtocol::Version version)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#setVersion

    Parameters
    ----------

    version : QWebSocketProtocol.Version
      Passed on as its number.
    """
    #  void QWebSocketPrivate::setVersion(QWebSocketProtocol::Version
    #      version)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate10setVersionEN18QWebSocketProtocol7Ver'
        'sionE',
        version.value,
    )

  @overload(str)
  def setResourceName(self, resourceName: str) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setResourceName(const QString
    &resourceName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#setResourceName

    Parameters
    ----------

    resourceName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketPrivate::setResourceName(const QString &resourceName)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate15setResourceNameERK7QString',
        resourceName,
    )

  @overload(QNetworkRequest)
  @overload(QNetworkRequest, QWebSocketHandshakeOptions)
  def setRequest(
      self,
      request: QNetworkRequest,
      options: Optional[QWebSocketHandshakeOptions] = None,
  ) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setRequest(const QNetworkRequest
    &request, const QWebSocketHandshakeOptions &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#setRequest

    Parameters
    ----------

    request : QNetworkRequest
      Passed on as a value: Qt reads the C++ QNetworkRequest, which stays
      Python's own.

    options : Optional[QWebSocketHandshakeOptions]
      Passed on as a value: Qt reads the C++ QWebSocketHandshakeOptions,
      which stays Python's own. May be left out, as in Qt: a new
      'QWebSocketHandshakeOptions()' is then passed on.
    """
    #  void QWebSocketPrivate::setRequest(const QNetworkRequest &request,
    #      const QWebSocketHandshakeOptions &options)
    if options is None:
      from . import QWebSocketHandshakeOptions
      options = QWebSocketHandshakeOptions()
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate10setRequestERK15QNetworkRequestRK26QW'
        'ebSocketHandshakeOptions',
        self._valueOf(request), self._valueOf(options),
    )

  @overload(str)
  def setOrigin(self, origin: str) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setOrigin(const QString &origin)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#setOrigin

    Parameters
    ----------

    origin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketPrivate::setOrigin(const QString &origin)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate9setOriginERK7QString', origin,
    )

  @overload(str)
  def setProtocol(self, protocol: str) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setProtocol(const QString
    &protocol)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#setProtocol

    Parameters
    ----------

    protocol : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketPrivate::setProtocol(const QString &protocol)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate11setProtocolERK7QString', protocol,
    )

  @overload(str)
  def setExtension(self, extension: str) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::setExtension(const QString
    &extension)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#setExtension

    Parameters
    ----------

    extension : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWebSocketPrivate::setExtension(const QString &extension)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate12setExtensionERK7QString', extension,
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
    - Qt's 'QWebSocketPrivate::QWebSocketPrivate(QTcpSocket *pTcpSocket,
      QWebSocketProtocol::Version version)': Qt's library has no name for it,
      and its code in Qt's source does not compile apart from its file: use
      of undeclared identifier 'DEFAULT_OUTGOING_FRAME_SIZE_IN_BYTES'.
    - Qt's 'QWebSocketPrivate::QWebSocketPrivate(const QString &origin,
      QWebSocketProtocol::Version version)': leans on
      'QWebSocketDataProcessor::staticMetaObject', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.__init__' has no cute function yet. Qt's "
        "'QWebSocketPrivate::QWebSocketPrivate(QTcpSocket *pTcpSocket, "
        "QWebSocketProtocol::Version version)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier "
        "'DEFAULT_OUTGOING_FRAME_SIZE_IN_BYTES'. Qt's "
        "'QWebSocketPrivate::QWebSocketPrivate(const QString &origin, "
        "QWebSocketProtocol::Version version)': leans on "
        "'QWebSocketDataProcessor::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def q_func(self) -> Optional[QWebSocket]:
    """
    Calls Qt's 'QWebSocket *QWebSocketPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#q_func

    Returns
    -------

    Optional[QWebSocket]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebSocket *QWebSocketPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QWebSocketPrivate6q_funcEv')
    from . import QWebSocket
    return QWebSocket._cuteAt(address)

  def abort(self) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#abort
    """
    #  void QWebSocketPrivate::abort()
    self.uglySide.call('ritual_ZN17QWebSocketPrivate5abortEv')

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QWebSocketPrivate::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#flush
    """
    #  bool QWebSocketPrivate::flush()
    return self.uglySide.call('ritual_ZN17QWebSocketPrivate5flushEv')

  @overload(QList[QSslError])
  def ignoreSslErrors(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::ignoreSslErrors(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QWebSocketPrivate::ignoreSslErrors(const QList<QSslError>
    #      &errors)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate15ignoreSslErrorsERK5QListI9QSslErrorE',
        self._valueOf(errors),
    )

  @overload()
  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#ignoreSslErrors
    """
    #  void QWebSocketPrivate::ignoreSslErrors()
    self.uglySide.call('ritual_ZN17QWebSocketPrivate15ignoreSslErrorsEv')

  def continueInterruptedHandshake(self) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::continueInterruptedHandshake()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html
    """
    #  void QWebSocketPrivate::continueInterruptedHandshake()
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate28continueInterruptedHandshakeEv',
    )

  def _q_updateSslConfiguration(self) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::_q_updateSslConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#_q_updateSslConfiguration
    """
    #  void QWebSocketPrivate::_q_updateSslConfiguration()
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate25_q_updateSslConfigurationEv',
    )

  @overload(bool)
  def enableMasking(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWebSocketPrivate::enableMasking(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebsocketprivate.html#enableMasking

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWebSocketPrivate::enableMasking(bool enable)
    self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate13enableMaskingEb', enable,
    )

  @overload(QList[QByteArray])
  def writeFrames(self, frames: QList[QByteArray]) -> int:
    """
    Calls Qt's 'qint64 QWebSocketPrivate::writeFrames(const QList<QByteArray>
    &frames)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#writeFrames

    Parameters
    ----------

    frames : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  qint64 QWebSocketPrivate::writeFrames(const QList<QByteArray> &frames)
    return self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate11writeFramesERK5QListI10QByteArrayE',
        self._valueOf(frames),
    )

  @overload(QByteArray)
  def writeFrame(self, frame: QByteArray) -> int:
    """
    Calls Qt's 'qint64 QWebSocketPrivate::writeFrame(const QByteArray
    &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebsocketprivate.html#writeFrame

    Parameters
    ----------

    frame : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  qint64 QWebSocketPrivate::writeFrame(const QByteArray &frame)
    return self.uglySide.call(
        'ritual_ZN17QWebSocketPrivate10writeFrameERK10QByteArray',
        self._valueOf(frame),
    )

  @staticmethod
  def close(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::close(QWebSocketProtocol::CloseCode
    closeCode, QString reason)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.close' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::close(QWebSocketProtocol::CloseCode closeCode, "
        "QString reason)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def closeGoingAway(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::closeGoingAway()': leans on
    'QWebSocketPrivate::socketDestroyed(QObject*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.closeGoingAway' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::closeGoingAway()': leans on "
        "'QWebSocketPrivate::socketDestroyed(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def createHandShakeRequest(*__, **_) -> Never:
    """
    Qt's 'QString QWebSocketPrivate::createHandShakeRequest(QString
    resourceName, QString host, QString origin, QString extensions, const
    QStringList &options, QByteArray key, const QList<QPair<QString,
    QString>> &headers)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.createHandShakeRequest' has no cute function "
        "yet. Qt's 'QString "
        "QWebSocketPrivate::createHandShakeRequest(QString resourceName, "
        "QString host, QString origin, QString extensions, const "
        "QStringList &options, QByteArray key, const QList<QPair<QString, "
        "QString>> &headers)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def doClose(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::doClose(QWebSocketProtocol::CloseCode
    closeCode, QString reason, bool isFailed)': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.doClose' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::doClose(QWebSocketProtocol::CloseCode "
        "closeCode, QString reason, bool isFailed)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def doWriteFrames(*__, **_) -> Never:
    """
    Qt's 'qint64 QWebSocketPrivate::doWriteFrames(const QByteArray &data,
    bool isBinary)': leans on 'QWebSocketPrivate::setErrorString(QString
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.doWriteFrames' has no cute function yet. Qt's "
        "'qint64 QWebSocketPrivate::doWriteFrames(const QByteArray &data, "
        "bool isBinary)': leans on "
        "'QWebSocketPrivate::setErrorString(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def emitErrorOccurred(*__, **_) -> Never:
    """
    Qt's 'void
    QWebSocketPrivate::emitErrorOccurred(QAbstractSocket::SocketError
    error)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.emitErrorOccurred' has no cute function yet. "
        "Qt's 'void "
        "QWebSocketPrivate::emitErrorOccurred(QAbstractSocket::SocketError "
        "error)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def getFrameHeader(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    QWebSocketPrivate::getFrameHeader(QWebSocketProtocol::OpCode opCode,
    quint64 payloadLength, quint32 maskingKey, bool lastFrame)': leans on
    'QWebSocketPrivate::setErrorString(QString const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.getFrameHeader' has no cute function yet. Qt's "
        "'QByteArray "
        "QWebSocketPrivate::getFrameHeader(QWebSocketProtocol::OpCode "
        "opCode, quint64 payloadLength, quint32 maskingKey, bool "
        "lastFrame)': leans on 'QWebSocketPrivate::setErrorString(QString "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::init()': leans on
    'QWebSocketPrivate::processData()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.init' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::init()': leans on "
        "'QWebSocketPrivate::processData()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QWebSocketPrivate::isValid() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'm_socketContext'.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.isValid' has no cute function yet. Qt's 'bool "
        "QWebSocketPrivate::isValid() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'm_socketContext'.")

  @staticmethod
  def localAddress(*__, **_) -> Never:
    """
    Qt's 'QHostAddress QWebSocketPrivate::localAddress() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.localAddress' has no cute function yet. Qt's "
        "'QHostAddress QWebSocketPrivate::localAddress() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def localPort(*__, **_) -> Never:
    """
    Qt's 'quint16 QWebSocketPrivate::localPort() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.localPort' has no cute function yet. Qt's "
        "'quint16 QWebSocketPrivate::localPort() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def makeConnections(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::makeConnections(QTcpSocket *pTcpSocket)':
    leans on 'QWebSocketPrivate::processData()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.makeConnections' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::makeConnections(QTcpSocket *pTcpSocket)': "
        "leans on 'QWebSocketPrivate::processData()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def maskGenerator(*__, **_) -> Never:
    """
    Qt's 'const QMaskGenerator *QWebSocketPrivate::maskGenerator() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maskGenerator' has no cute function yet. Qt's "
        "'const QMaskGenerator *QWebSocketPrivate::maskGenerator() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def maxAllowedIncomingFrameSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::maxAllowedIncomingFrameSize() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maxAllowedIncomingFrameSize' has no cute "
        "function yet. Qt's 'quint64 "
        "QWebSocketPrivate::maxAllowedIncomingFrameSize() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def maxAllowedIncomingMessageSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::maxAllowedIncomingMessageSize() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maxAllowedIncomingMessageSize' has no cute "
        "function yet. Qt's 'quint64 "
        "QWebSocketPrivate::maxAllowedIncomingMessageSize() const': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def maxIncomingFrameSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::maxIncomingFrameSize()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maxIncomingFrameSize' has no cute function yet. "
        "Qt's 'quint64 QWebSocketPrivate::maxIncomingFrameSize()': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def maxIncomingMessageSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::maxIncomingMessageSize()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maxIncomingMessageSize' has no cute function "
        "yet. Qt's 'quint64 QWebSocketPrivate::maxIncomingMessageSize()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def maxOutgoingFrameSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::maxOutgoingFrameSize()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.maxOutgoingFrameSize' has no cute function yet. "
        "Qt's 'quint64 QWebSocketPrivate::maxOutgoingFrameSize()': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::open(const QNetworkRequest &request, const
    QWebSocketHandshakeOptions &options, bool mask)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.open' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::open(const QNetworkRequest &request, const "
        "QWebSocketHandshakeOptions &options, bool mask)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def outgoingFrameSize(*__, **_) -> Never:
    """
    Qt's 'quint64 QWebSocketPrivate::outgoingFrameSize() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.outgoingFrameSize' has no cute function yet. "
        "Qt's 'quint64 QWebSocketPrivate::outgoingFrameSize() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def pauseMode(*__, **_) -> Never:
    """
    Qt's 'QAbstractSocket::PauseModes QWebSocketPrivate::pauseMode() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.pauseMode' has no cute function yet. Qt's "
        "'QAbstractSocket::PauseModes QWebSocketPrivate::pauseMode() "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def peerAddress(*__, **_) -> Never:
    """
    Qt's 'QHostAddress QWebSocketPrivate::peerAddress() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.peerAddress' has no cute function yet. Qt's "
        "'QHostAddress QWebSocketPrivate::peerAddress() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def peerName(*__, **_) -> Never:
    """
    Qt's 'QString QWebSocketPrivate::peerName() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.peerName' has no cute function yet. Qt's "
        "'QString QWebSocketPrivate::peerName() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def peerPort(*__, **_) -> Never:
    """
    Qt's 'quint16 QWebSocketPrivate::peerPort() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.peerPort' has no cute function yet. Qt's "
        "'quint16 QWebSocketPrivate::peerPort() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def ping(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::ping(const QByteArray &payload)': leans on
    'QWebSocketPrivate::setErrorString(QString const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.ping' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::ping(const QByteArray &payload)': leans on "
        "'QWebSocketPrivate::setErrorString(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def processClose(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processClose(QWebSocketProtocol::CloseCode
    closeCode, QString closeReason)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processClose' has no cute function yet. Qt's "
        "'void "
        "QWebSocketPrivate::processClose(QWebSocketProtocol::CloseCode "
        "closeCode, QString closeReason)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def processData(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processData()': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processData' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::processData()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def processError(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processError(QWebSocketProtocol::CloseCode
    closeCode, QString reason)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processError' has no cute function yet. Qt's "
        "'void "
        "QWebSocketPrivate::processError(QWebSocketProtocol::CloseCode "
        "closeCode, QString reason)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def processHandshake(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processHandshake(QTcpSocket *pSocket)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: redefinition of 'isValid'.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processHandshake' has no cute function yet. "
        "Qt's 'void QWebSocketPrivate::processHandshake(QTcpSocket "
        "*pSocket)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: redefinition of "
        "'isValid'.")

  @staticmethod
  def processPing(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processPing(const QByteArray &data)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processPing' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::processPing(const QByteArray &data)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def processPong(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::processPong(const QByteArray &data)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processPong' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::processPong(const QByteArray &data)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def processStateChanged(*__, **_) -> Never:
    """
    Qt's 'void
    QWebSocketPrivate::processStateChanged(QAbstractSocket::SocketState
    socketState)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.processStateChanged' has no cute function yet. "
        "Qt's 'void "
        "QWebSocketPrivate::processStateChanged(QAbstractSocket::SocketState"
        " socketState)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def proxy(*__, **_) -> Never:
    """
    Qt's 'QNetworkProxy QWebSocketPrivate::proxy() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.proxy' has no cute function yet. Qt's "
        "'QNetworkProxy QWebSocketPrivate::proxy() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def readBufferSize(*__, **_) -> Never:
    """
    Qt's 'qint64 QWebSocketPrivate::readBufferSize() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.readBufferSize' has no cute function yet. Qt's "
        "'qint64 QWebSocketPrivate::readBufferSize() const': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def releaseConnections(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::releaseConnections(const QTcpSocket
    *pTcpSocket)': leans on 'QWebSocketPrivate::socketDestroyed(QObject*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.releaseConnections' has no cute function yet. "
        "Qt's 'void QWebSocketPrivate::releaseConnections(const QTcpSocket "
        "*pTcpSocket)': leans on "
        "'QWebSocketPrivate::socketDestroyed(QObject*)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def resume(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::resume()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.resume' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::resume()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def sendBinaryMessage(*__, **_) -> Never:
    """
    Qt's 'qint64 QWebSocketPrivate::sendBinaryMessage(const QByteArray
    &data)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.sendBinaryMessage' has no cute function yet. "
        "Qt's 'qint64 QWebSocketPrivate::sendBinaryMessage(const QByteArray "
        "&data)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def sendTextMessage(*__, **_) -> Never:
    """
    Qt's 'qint64 QWebSocketPrivate::sendTextMessage(const QString &message)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.sendTextMessage' has no cute function yet. Qt's "
        "'qint64 QWebSocketPrivate::sendTextMessage(const QString "
        "&message)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setErrorString(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setErrorString(const QString
    &errorString)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setErrorString' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::setErrorString(const QString "
        "&errorString)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setMaskGenerator(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setMaskGenerator(const QMaskGenerator
    *maskGenerator)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setMaskGenerator' has no cute function yet. "
        "Qt's 'void QWebSocketPrivate::setMaskGenerator(const "
        "QMaskGenerator *maskGenerator)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setMaxAllowedIncomingFrameSize(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setMaxAllowedIncomingFrameSize(quint64
    maxAllowedIncomingFrameSize)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setMaxAllowedIncomingFrameSize' has no cute "
        "function yet. Qt's 'void "
        "QWebSocketPrivate::setMaxAllowedIncomingFrameSize(quint64 "
        "maxAllowedIncomingFrameSize)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setMaxAllowedIncomingMessageSize(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setMaxAllowedIncomingMessageSize(quint64
    maxAllowedIncomingMessageSize)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setMaxAllowedIncomingMessageSize' has no cute "
        "function yet. Qt's 'void "
        "QWebSocketPrivate::setMaxAllowedIncomingMessageSize(quint64 "
        "maxAllowedIncomingMessageSize)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def setOutgoingFrameSize(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setOutgoingFrameSize(quint64
    outgoingFrameSize)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setOutgoingFrameSize' has no cute function yet. "
        "Qt's 'void QWebSocketPrivate::setOutgoingFrameSize(quint64 "
        "outgoingFrameSize)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setPauseMode(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setPauseMode(QAbstractSocket::PauseModes
    pauseMode)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setPauseMode' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::setPauseMode(QAbstractSocket::PauseModes "
        "pauseMode)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def setProxy(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setProxy(const QNetworkProxy
    &networkProxy)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setProxy' has no cute function yet. Qt's 'void "
        "QWebSocketPrivate::setProxy(const QNetworkProxy &networkProxy)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setReadBufferSize(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setReadBufferSize(qint64 size)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setReadBufferSize' has no cute function yet. "
        "Qt's 'void QWebSocketPrivate::setReadBufferSize(qint64 size)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setSocketState(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::setSocketState(QAbstractSocket::SocketState
    state)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.setSocketState' has no cute function yet. Qt's "
        "'void "
        "QWebSocketPrivate::setSocketState(QAbstractSocket::SocketState "
        "state)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def socketDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWebSocketPrivate::socketDestroyed(QObject *socket)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.socketDestroyed' has no cute function yet. Qt's "
        "'void QWebSocketPrivate::socketDestroyed(QObject *socket)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def state(*__, **_) -> Never:
    """
    Qt's 'QAbstractSocket::SocketState QWebSocketPrivate::state() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.state' has no cute function yet. Qt's "
        "'QAbstractSocket::SocketState QWebSocketPrivate::state() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def upgradeFrom(*__, **_) -> Never:
    """
    Qt's 'QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *tcpSocket,
    const QWebSocketHandshakeRequest &request, const
    QWebSocketHandshakeResponse &response, QObject *parent)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebSocketPrivate.upgradeFrom' has no cute function yet. Qt's "
        "'QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *tcpSocket, "
        "const QWebSocketHandshakeRequest &request, const "
        "QWebSocketHandshakeResponse &response, QObject *parent)': takes a "
        "type Python has no way to hand over yet.")
