"""
QHttpNetworkConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkConnection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHttp2Configuration, QHttpNetworkConnectionChannel
  from . import QHttpNetworkConnectionPrivate, QHttpNetworkReply
  from . import QHttpNetworkRequest, QNetworkProxy, QSslConfiguration
  from . import QSslError, QTcpKeepAliveConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHttp2Configuration = WAIT['QHttp2Configuration']
  QHttpNetworkRequest = WAIT['QHttpNetworkRequest']
  QNetworkProxy = WAIT['QNetworkProxy']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']
  QTcpKeepAliveConfiguration = WAIT['QTcpKeepAliveConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpNetworkConnection(QObject):
  """
  The cute side of Qt's QHttpNetworkConnection: a plain Python object
  standing in front of one C++ QHttpNetworkConnection.

  It is built on the cute 'QObject', as Qt's QHttpNetworkConnection is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpNetworkConnection that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'hostName',
  'port', 'sendRequest', 'fillHttp2Queue', 'setCacheProxy', 'cacheProxy',
  'setTransparentProxy', 'transparentProxy', 'isSsl', 'channels',
  'connectionType', 'setConnectionType', 'http2Parameters',
  'setHttp2Parameters', 'tcpKeepAliveParameters',
  'setTcpKeepAliveParameters', 'setSslConfiguration', 'ignoreSslErrors',
  'preConnectFinished', 'peerVerifyName', 'setPeerVerifyName',
  'onlineStateChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpNetworkConnection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHttpNetworkConnection::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHttpNetworkConnection::~QHttpNetworkConnection()': the destructor:
    Python never removes a C++ QHttpNetworkConnection.
  - Qt's 'std::shared_ptr<QSslContext> QHttpNetworkConnection::sslContext()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    QHttpNetworkConnection::setSslContext(std::shared_ptr<QSslContext>
    context)': takes a type Python has no way to hand over yet.
  - Qt's 'const QHttpNetworkConnectionPrivate
    *QHttpNetworkConnection::d_func() const': takes in Python what
    'QHttpNetworkConnectionPrivate *QHttpNetworkConnection::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 39 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QHttpNetworkConnection is created at the first use, not by
    'QHttpNetworkConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpNetworkConnection.
  - Qt tells when it has removed the C++ QHttpNetworkConnection. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHttpNetworkConnection that has no cute function yet,
    'setSslContext', 'sslContext', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHttpNetworkConnection, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ConnectionType(CuteNum):
    """
    The enum 'QHttpNetworkConnection::ConnectionType' of Qt, with the 3 names
    Qt gives in it.
    """

    ConnectionTypeHTTP = Kee[int](0)
    ConnectionTypeHTTP2 = Kee[int](1)
    ConnectionTypeHTTP2Direct = Kee[int](2)

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
    Calls Qt's 'QString QHttpNetworkConnection::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkconnection.html#tr

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
    #  QString QHttpNetworkConnection::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QHttpNetworkConnection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkConnection'

  #  A C++ QHttpNetworkConnection Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpNetworkConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpNetworkConnection::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpNetworkConnection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hostName(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkConnection::hostName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#hostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkConnection::hostName() const
    return self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection8hostNameEv',
    )

  def port(self) -> int:
    """
    Calls Qt's 'quint16 QHttpNetworkConnection::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkconnection.html#port
    """
    #  quint16 QHttpNetworkConnection::port() const
    return self.uglySide.call('ritual_ZNK22QHttpNetworkConnection4portEv')

  def cacheProxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QHttpNetworkConnection::cacheProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#cacheProxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QHttpNetworkConnection::cacheProxy() const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection10cacheProxyEv',
    )
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def transparentProxy(self) -> QNetworkProxy:
    """
    Calls Qt's 'QNetworkProxy QHttpNetworkConnection::transparentProxy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#transparentProxy

    Returns
    -------

    QNetworkProxy
      A new cute QNetworkProxy around the copy Qt gave back. Python owns it.
    """
    #  QNetworkProxy QHttpNetworkConnection::transparentProxy() const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection16transparentProxyEv',
    )
    from . import QNetworkProxy
    return QNetworkProxy._cuteOwning(address)

  def isSsl(self) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkConnection::isSsl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkconnection.html#isSsl
    """
    #  bool QHttpNetworkConnection::isSsl() const
    return self.uglySide.call('ritual_ZNK22QHttpNetworkConnection5isSslEv')

  def channels(self) -> Optional[QHttpNetworkConnectionChannel]:
    """
    Calls Qt's 'QHttpNetworkConnectionChannel
    *QHttpNetworkConnection::channels() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#channels

    Returns
    -------

    Optional[QHttpNetworkConnectionChannel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkConnectionChannel *QHttpNetworkConnection::channels()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection8channelsEv',
    )
    from . import QHttpNetworkConnectionChannel
    return QHttpNetworkConnectionChannel._cuteAt(address)

  def connectionType(self) -> ConnectionType:
    """
    Calls Qt's 'ConnectionType QHttpNetworkConnection::connectionType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#connectionType

    Returns
    -------

    ConnectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ConnectionType(number)'
      gives.
    """
    #  ConnectionType QHttpNetworkConnection::connectionType() const
    return QHttpNetworkConnection.ConnectionType(self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection14connectionTypeEv',
    ))

  def http2Parameters(self) -> QHttp2Configuration:
    """
    Calls Qt's 'QHttp2Configuration QHttpNetworkConnection::http2Parameters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#http2Parameters

    Returns
    -------

    QHttp2Configuration
      A new cute QHttp2Configuration around the copy Qt gave back. Python
      owns it.
    """
    #  QHttp2Configuration QHttpNetworkConnection::http2Parameters() const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection15http2ParametersEv',
    )
    from . import QHttp2Configuration
    return QHttp2Configuration._cuteOwning(address)

  def tcpKeepAliveParameters(self) -> QTcpKeepAliveConfiguration:
    """
    Calls Qt's 'QTcpKeepAliveConfiguration
    QHttpNetworkConnection::tcpKeepAliveParameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#tcpKeepAliveParameters

    Returns
    -------

    QTcpKeepAliveConfiguration
      A new cute QTcpKeepAliveConfiguration around the copy Qt gave back.
      Python owns it.
    """
    #  QTcpKeepAliveConfiguration
    #      QHttpNetworkConnection::tcpKeepAliveParameters() const
    address = self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection22tcpKeepAliveParametersEv',
    )
    from . import QTcpKeepAliveConfiguration
    return QTcpKeepAliveConfiguration._cuteOwning(address)

  def peerVerifyName(self) -> str:
    """
    Calls Qt's 'QString QHttpNetworkConnection::peerVerifyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#peerVerifyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHttpNetworkConnection::peerVerifyName() const
    return self.uglySide.call(
        'ritual_ZNK22QHttpNetworkConnection14peerVerifyNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QNetworkProxy)
  def setCacheProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setCacheProxy(const
    QNetworkProxy &networkProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setCacheProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QHttpNetworkConnection::setCacheProxy(const QNetworkProxy
    #      &networkProxy)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection13setCacheProxyERK13QNetworkProxy',
        self._valueOf(networkProxy),
    )

  @overload(QNetworkProxy)
  def setTransparentProxy(self, networkProxy: QNetworkProxy) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setTransparentProxy(const
    QNetworkProxy &networkProxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setTransparentProxy

    Parameters
    ----------

    networkProxy : QNetworkProxy
      Passed on as a value: Qt reads the C++ QNetworkProxy, which stays
      Python's own.
    """
    #  void QHttpNetworkConnection::setTransparentProxy(const QNetworkProxy
    #      &networkProxy)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection19setTransparentProxyERK13QNetwor'
        'kProxy',
        self._valueOf(networkProxy),
    )

  @overload(ConnectionType)
  def setConnectionType(self, type: ConnectionType) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setConnectionType(ConnectionType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setConnectionType

    Parameters
    ----------

    type : ConnectionType
      Passed on as its number.
    """
    #  void QHttpNetworkConnection::setConnectionType(ConnectionType type)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection17setConnectionTypeENS_14Connecti'
        'onTypeE',
        type.value,
    )

  @overload(QHttp2Configuration)
  def setHttp2Parameters(self, params: QHttp2Configuration) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setHttp2Parameters(const
    QHttp2Configuration &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setHttp2Parameters

    Parameters
    ----------

    params : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  void QHttpNetworkConnection::setHttp2Parameters(const
    #      QHttp2Configuration &params)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection18setHttp2ParametersERK19QHttp2Co'
        'nfiguration',
        self._valueOf(params),
    )

  @overload(QTcpKeepAliveConfiguration)
  def setTcpKeepAliveParameters(
      self,
      config: QTcpKeepAliveConfiguration,
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setTcpKeepAliveParameters(
    QTcpKeepAliveConfiguration config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html

    Parameters
    ----------

    config : QTcpKeepAliveConfiguration
      Passed on as a value: Qt reads the C++ QTcpKeepAliveConfiguration,
      which stays Python's own.
    """
    #  void QHttpNetworkConnection::setTcpKeepAliveParameters(
    #      QTcpKeepAliveConfiguration config)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection25setTcpKeepAliveParametersE26QTc'
        'pKeepAliveConfiguration',
        self._valueOf(config),
    )

  @overload(QSslConfiguration)
  def setSslConfiguration(self, config: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setSslConfiguration(const
    QSslConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setSslConfiguration

    Parameters
    ----------

    config : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QHttpNetworkConnection::setSslConfiguration(const
    #      QSslConfiguration &config)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection19setSslConfigurationERK17QSslCon'
        'figuration',
        self._valueOf(config),
    )

  @overload(str)
  def setPeerVerifyName(self, peerName: str) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::setPeerVerifyName(const QString
    &peerName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#setPeerVerifyName

    Parameters
    ----------

    peerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHttpNetworkConnection::setPeerVerifyName(const QString
    #      &peerName)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection17setPeerVerifyNameERK7QString',
        peerName,
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

  @overload(int, str)
  @overload(int, str, int)
  @overload(int, str, int, bool)
  @overload(int, str, int, bool, bool)
  @overload(int, str, int, bool, bool, QObject)
  @overload(int, str, int, bool, bool, NoneType)
  @overload(int, str, int, bool, bool, QObject, ConnectionType)
  @overload(int, str, int, bool, bool, NoneType, ConnectionType)
  def __init__(
      self,
      channelCount: int,
      hostName: str,
      port: int = 80,
      encrypt: bool = False,
      isLocalSocket: bool = False,
      parent: Optional[QObject] = None,
      connectionType: ConnectionType = ConnectionType.ConnectionTypeHTTP,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkConnection::QHttpNetworkConnection(quint16 channelCount,
    const QString &hostName, quint16 port, bool encrypt, bool isLocalSocket,
    QObject *parent, ConnectionType connectionType)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#QHttpNetworkConnection

    Parameters
    ----------

    channelCount : int
      Passed on as it is.

    hostName : str
      Passed on as it is: a QString is made of it for the call.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 80.

    encrypt : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    isLocalSocket : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    connectionType : ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      ConnectionType.ConnectionTypeHTTP.
    """
    #  QHttpNetworkConnection::QHttpNetworkConnection(quint16 channelCount,
    #      const QString &hostName, quint16 port, bool encrypt, bool
    #      isLocalSocket, QObject *parent, ConnectionType connectionType)
    self._noteCreation(QHttpNetworkConnection, lambda: Rituals.call(
        'ritual_ZN22QHttpNetworkConnectionC1EtRK7QStringtbbP7QObjectNS_14Co'
        'nnectionTypeE',
        channelCount, hostName, port, encrypt, isLocalSocket,
        self._addressOf(parent, 'QObject'), connectionType.value,
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

  @overload(QHttpNetworkRequest)
  def sendRequest(
      self,
      request: QHttpNetworkRequest,
  ) -> Optional[QHttpNetworkReply]:
    """
    Calls Qt's 'QHttpNetworkReply *QHttpNetworkConnection::sendRequest(const
    QHttpNetworkRequest &request)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#sendRequest

    Parameters
    ----------

    request : QHttpNetworkRequest
      Passed on as a value: Qt reads the C++ QHttpNetworkRequest, which stays
      Python's own.

    Returns
    -------

    Optional[QHttpNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkReply *QHttpNetworkConnection::sendRequest(const
    #      QHttpNetworkRequest &request)
    address = self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection11sendRequestERK19QHttpNetworkReq'
        'uest',
        self._valueOf(request),
    )
    from . import QHttpNetworkReply
    return QHttpNetworkReply._cuteAt(address)

  def fillHttp2Queue(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::fillHttp2Queue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#fillHttp2Queue
    """
    #  void QHttpNetworkConnection::fillHttp2Queue()
    self.uglySide.call('ritual_ZN22QHttpNetworkConnection14fillHttp2QueueEv')

  @overload()
  @overload(int)
  def ignoreSslErrors(self, channel: int = -1) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::ignoreSslErrors(int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#ignoreSslErrors

    Parameters
    ----------

    channel : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QHttpNetworkConnection::ignoreSslErrors(int channel)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection15ignoreSslErrorsEi', channel,
    )

  @overload(QList[QSslError])
  @overload(QList[QSslError], int)
  def ignoreSslErrors(
      self,
      errors: QList[QSslError],
      channel: int = -1,
  ) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::ignoreSslErrors(const
    QList<QSslError> &errors, int channel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#ignoreSslErrors

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    channel : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QHttpNetworkConnection::ignoreSslErrors(const QList<QSslError>
    #      &errors, int channel)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection15ignoreSslErrorsERK5QListI9QSslE'
        'rrorEi',
        self._valueOf(errors), channel,
    )

  def preConnectFinished(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::preConnectFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#preConnectFinished
    """
    #  void QHttpNetworkConnection::preConnectFinished()
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection18preConnectFinishedEv',
    )

  @overload(bool)
  def onlineStateChanged(self, isOnline: bool) -> None:
    """
    Calls Qt's 'void QHttpNetworkConnection::onlineStateChanged(bool
    isOnline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkconnection.html#onlineStateChanged

    Parameters
    ----------

    isOnline : bool
      Passed on as it is.
    """
    #  void QHttpNetworkConnection::onlineStateChanged(bool isOnline)
    self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection18onlineStateChangedEb', isOnline,
    )

  def d_func(self) -> Optional[QHttpNetworkConnectionPrivate]:
    """
    Calls Qt's 'QHttpNetworkConnectionPrivate
    *QHttpNetworkConnection::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpnetworkconnection.html#d_func

    Returns
    -------

    Optional[QHttpNetworkConnectionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkConnectionPrivate *QHttpNetworkConnection::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QHttpNetworkConnection6d_funcEv',
    )
    from . import QHttpNetworkConnectionPrivate
    return QHttpNetworkConnectionPrivate._cuteAt(address)

  @staticmethod
  def setSslContext(*__, **_) -> Never:
    """
    Qt's 'void
    QHttpNetworkConnection::setSslContext(std::shared_ptr<QSslContext>
    context)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnection.setSslContext' has no cute function yet. "
        "Qt's 'void "
        "QHttpNetworkConnection::setSslContext(std::shared_ptr<QSslContext> "
        "context)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def sslContext(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QSslContext> QHttpNetworkConnection::sslContext()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHttpNetworkConnection.sslContext' has no cute function yet. Qt's "
        "'std::shared_ptr<QSslContext> QHttpNetworkConnection::sslContext() "
        "const': gives a type Python has no way to take yet.")
