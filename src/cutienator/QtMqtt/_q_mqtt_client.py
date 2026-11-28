"""
QMqttClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttclient.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QMqtt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject
  from ..QtNetwork import QSslConfiguration
  from . import QMqttAuthenticationProperties, QMqttClientPrivate
  from . import QMqttConnectionProperties, QMqttLastWillProperties
  from . import QMqttMessageStatusProperties, QMqttPublishProperties
  from . import QMqttServerConnectionProperties, QMqttSubscription
  from . import QMqttSubscriptionProperties, QMqttTopicFilter, QMqttTopicName
  from . import QMqttUnsubscriptionProperties
  from ..QtWebSockets import QWebSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']
  QMqttAuthenticationProperties = WAIT['QMqttAuthenticationProperties']
  QMqttConnectionProperties = WAIT['QMqttConnectionProperties']
  QMqttLastWillProperties = WAIT['QMqttLastWillProperties']
  QMqttMessageStatusProperties = WAIT['QMqttMessageStatusProperties']
  QMqttPublishProperties = WAIT['QMqttPublishProperties']
  QMqttSubscriptionProperties = WAIT['QMqttSubscriptionProperties']
  QMqttTopicFilter = WAIT['QMqttTopicFilter']
  QMqttTopicName = WAIT['QMqttTopicName']
  QMqttUnsubscriptionProperties = WAIT['QMqttUnsubscriptionProperties']
  QSslConfiguration = WAIT['QSslConfiguration']
  QWebSocket = WAIT['QWebSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMqttClient(QObject):
  """
  The cute side of Qt's QMqttClient: a plain Python object standing in front
  of one C++ QMqttClient.

  It is built on the cute 'QObject', as Qt's QMqttClient is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMqttClient that has a ritual and that Python can
  call so far, 74 names in all: 'metaObject', 'tr', 'setTransport',
  'transport', 'subscribe', 'unsubscribe', 'publish', 'requestPing',
  'hostname', 'port', 'clientId', 'keepAlive', 'protocolVersion',
  'connectToHost', 'connectToHostEncrypted', 'connectToHostWebSocket',
  'connectToHostWebSocketEncrypted', 'disconnectFromHost', 'state', 'error',
  'username', 'password', 'cleanSession', 'willTopic', 'willQoS',
  'willMessage', 'willRetain', 'autoKeepAlive', 'setConnectionProperties',
  'connectionProperties', 'setLastWillProperties', 'lastWillProperties',
  'serverConnectionProperties', 'authenticate', 'connected', 'disconnected',
  'messageReceived', 'messageStatusChanged', 'messageSent',
  'pingResponseReceived', 'brokerSessionRestored', 'hostnameChanged',
  'portChanged', 'clientIdChanged', 'keepAliveChanged',
  'protocolVersionChanged', 'stateChanged', 'errorChanged',
  'usernameChanged', 'passwordChanged', 'cleanSessionChanged',
  'willTopicChanged', 'willQoSChanged', 'willMessageChanged',
  'willRetainChanged', 'autoKeepAliveChanged', 'authenticationRequested',
  'authenticationFinished', 'setHostname', 'setPort', 'setClientId',
  'setKeepAlive', 'setProtocolVersion', 'setState', 'setError',
  'setUsername', 'setPassword', 'setCleanSession', 'setWillTopic',
  'setWillQoS', 'setWillMessage', 'setWillRetain', 'setAutoKeepAlive',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMqttClient::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMqttClient::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMqttClient::~QMqttClient()': the destructor: Python never removes
    a C++ QMqttClient.
  - Qt's 'const QMqttClientPrivate *QMqttClient::d_func() const': takes in
    Python what 'QMqttClientPrivate *QMqttClient::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 87 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMqttClient is created at the first use, not by
    'QMqttClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMqttClient.
  - Qt tells when it has removed the C++ QMqttClient. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMqttClient, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ClientError(CuteNum):
    """
    The enum 'QMqttClient::ClientError' of Qt, with the 10 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    InvalidProtocolVersion = Kee[int](1)
    IdRejected = Kee[int](2)
    ServerUnavailable = Kee[int](3)
    BadUsernameOrPassword = Kee[int](4)
    NotAuthorized = Kee[int](5)
    TransportInvalid = Kee[int](256)
    ProtocolViolation = Kee[int](257)
    UnknownError = Kee[int](258)
    Mqtt5SpecificError = Kee[int](259)

  class ClientState(CuteNum):
    """
    The enum 'QMqttClient::ClientState' of Qt, with the 3 names Qt gives in
    it.
    """

    Disconnected = Kee[int](0)
    Connecting = Kee[int](1)
    Connected = Kee[int](2)

  class ProtocolVersion(CuteNum):
    """
    The enum 'QMqttClient::ProtocolVersion' of Qt, with the 3 names Qt gives
    in it.
    """

    MQTT_3_1 = Kee[int](3)
    MQTT_3_1_1 = Kee[int](4)
    MQTT_5_0 = Kee[int](5)

  class TransportType(CuteNum):
    """
    The enum 'QMqttClient::TransportType' of Qt, with the 5 names Qt gives in
    it.
    """

    IODevice = Kee[int](0)
    AbstractSocket = Kee[int](1)
    SecureSocket = Kee[int](2)
    WebSocket = Kee[int](3)
    SecureWebSocket = Kee[int](4)

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
    Calls Qt's 'QString QMqttClient::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#tr

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
    #  QString QMqttClient::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QMqttClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttClient'

  #  A C++ QMqttClient Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMqttClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMqttClient::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMqttClient::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QMqttClient10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def transport(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QMqttClient::transport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#transport

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QMqttClient::transport() const
    address = self.uglySide.call('ritual_ZNK11QMqttClient9transportEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def hostname(self) -> str:
    """
    Calls Qt's 'QString QMqttClient::hostname() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#hostname

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttClient::hostname() const
    return self.uglySide.call('ritual_ZNK11QMqttClient8hostnameEv')

  def port(self) -> int:
    """
    Calls Qt's 'quint16 QMqttClient::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#port
    """
    #  quint16 QMqttClient::port() const
    return self.uglySide.call('ritual_ZNK11QMqttClient4portEv')

  def clientId(self) -> str:
    """
    Calls Qt's 'QString QMqttClient::clientId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#clientId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttClient::clientId() const
    return self.uglySide.call('ritual_ZNK11QMqttClient8clientIdEv')

  def keepAlive(self) -> int:
    """
    Calls Qt's 'quint16 QMqttClient::keepAlive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#keepAlive
    """
    #  quint16 QMqttClient::keepAlive() const
    return self.uglySide.call('ritual_ZNK11QMqttClient9keepAliveEv')

  def protocolVersion(self) -> ProtocolVersion:
    """
    Calls Qt's 'ProtocolVersion QMqttClient::protocolVersion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#protocolVersion

    Returns
    -------

    ProtocolVersion
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProtocolVersion(number)'
      gives.
    """
    #  ProtocolVersion QMqttClient::protocolVersion() const
    return QMqttClient.ProtocolVersion(self.uglySide.call(
        'ritual_ZNK11QMqttClient15protocolVersionEv',
    ))

  def state(self) -> ClientState:
    """
    Calls Qt's 'ClientState QMqttClient::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#state

    Returns
    -------

    ClientState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClientState(number)'
      gives.
    """
    #  ClientState QMqttClient::state() const
    return QMqttClient.ClientState(self.uglySide.call(
        'ritual_ZNK11QMqttClient5stateEv',
    ))

  def error(self) -> ClientError:
    """
    Calls Qt's 'ClientError QMqttClient::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#error

    Returns
    -------

    ClientError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ClientError(number)'
      gives.
    """
    #  ClientError QMqttClient::error() const
    return QMqttClient.ClientError(self.uglySide.call(
        'ritual_ZNK11QMqttClient5errorEv',
    ))

  def username(self) -> str:
    """
    Calls Qt's 'QString QMqttClient::username() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#username

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttClient::username() const
    return self.uglySide.call('ritual_ZNK11QMqttClient8usernameEv')

  def password(self) -> str:
    """
    Calls Qt's 'QString QMqttClient::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttClient::password() const
    return self.uglySide.call('ritual_ZNK11QMqttClient8passwordEv')

  def cleanSession(self) -> bool:
    """
    Calls Qt's 'bool QMqttClient::cleanSession() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#cleanSession
    """
    #  bool QMqttClient::cleanSession() const
    return self.uglySide.call('ritual_ZNK11QMqttClient12cleanSessionEv')

  def willTopic(self) -> str:
    """
    Calls Qt's 'QString QMqttClient::willTopic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willTopic

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttClient::willTopic() const
    return self.uglySide.call('ritual_ZNK11QMqttClient9willTopicEv')

  def willQoS(self) -> int:
    """
    Calls Qt's 'quint8 QMqttClient::willQoS() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willQoS
    """
    #  quint8 QMqttClient::willQoS() const
    return self.uglySide.call('ritual_ZNK11QMqttClient7willQoSEv')

  def willMessage(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttClient::willMessage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willMessage

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttClient::willMessage() const
    address = self.uglySide.call('ritual_ZNK11QMqttClient11willMessageEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def willRetain(self) -> bool:
    """
    Calls Qt's 'bool QMqttClient::willRetain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willRetain
    """
    #  bool QMqttClient::willRetain() const
    return self.uglySide.call('ritual_ZNK11QMqttClient10willRetainEv')

  def autoKeepAlive(self) -> bool:
    """
    Calls Qt's 'bool QMqttClient::autoKeepAlive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#autoKeepAlive
    """
    #  bool QMqttClient::autoKeepAlive() const
    return self.uglySide.call('ritual_ZNK11QMqttClient13autoKeepAliveEv')

  def connectionProperties(self) -> QMqttConnectionProperties:
    """
    Calls Qt's 'QMqttConnectionProperties QMqttClient::connectionProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#connectionProperties

    Returns
    -------

    QMqttConnectionProperties
      A new cute QMqttConnectionProperties around the copy Qt gave back.
      Python owns it.
    """
    #  QMqttConnectionProperties QMqttClient::connectionProperties() const
    address = self.uglySide.call(
        'ritual_ZNK11QMqttClient20connectionPropertiesEv',
    )
    from . import QMqttConnectionProperties
    return QMqttConnectionProperties._cuteOwning(address)

  def lastWillProperties(self) -> QMqttLastWillProperties:
    """
    Calls Qt's 'QMqttLastWillProperties QMqttClient::lastWillProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#lastWillProperties

    Returns
    -------

    QMqttLastWillProperties
      A new cute QMqttLastWillProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttLastWillProperties QMqttClient::lastWillProperties() const
    address = self.uglySide.call(
        'ritual_ZNK11QMqttClient18lastWillPropertiesEv',
    )
    from . import QMqttLastWillProperties
    return QMqttLastWillProperties._cuteOwning(address)

  def serverConnectionProperties(self) -> QMqttServerConnectionProperties:
    """
    Calls Qt's 'QMqttServerConnectionProperties
    QMqttClient::serverConnectionProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#serverConnectionProperties

    Returns
    -------

    QMqttServerConnectionProperties
      A new cute QMqttServerConnectionProperties around the copy Qt gave
      back. Python owns it.
    """
    #  QMqttServerConnectionProperties
    #      QMqttClient::serverConnectionProperties() const
    address = self.uglySide.call(
        'ritual_ZNK11QMqttClient26serverConnectionPropertiesEv',
    )
    from . import QMqttServerConnectionProperties
    return QMqttServerConnectionProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice, TransportType)
  @overload(NoneType, TransportType)
  def setTransport(
      self,
      device: Optional[QIODevice],
      transport: TransportType,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::setTransport(QIODevice *device,
    TransportType transport)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setTransport

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    transport : TransportType
      Passed on as its number.
    """
    #  void QMqttClient::setTransport(QIODevice *device, TransportType
    #      transport)
    self.uglySide.call(
        'ritual_ZN11QMqttClient12setTransportEP9QIODeviceNS_13TransportType'
        'E',
        self._addressOf(device), transport.value,
    )

  @overload(QMqttConnectionProperties)
  def setConnectionProperties(self, prop: QMqttConnectionProperties) -> None:
    """
    Calls Qt's 'void QMqttClient::setConnectionProperties(const
    QMqttConnectionProperties &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#setConnectionProperties

    Parameters
    ----------

    prop : QMqttConnectionProperties
      Passed on as a value: Qt reads the C++ QMqttConnectionProperties, which
      stays Python's own.
    """
    #  void QMqttClient::setConnectionProperties(const
    #      QMqttConnectionProperties &prop)
    self.uglySide.call(
        'ritual_ZN11QMqttClient23setConnectionPropertiesERK25QMqttConnectio'
        'nProperties',
        self._valueOf(prop),
    )

  @overload(QMqttLastWillProperties)
  def setLastWillProperties(self, prop: QMqttLastWillProperties) -> None:
    """
    Calls Qt's 'void QMqttClient::setLastWillProperties(const
    QMqttLastWillProperties &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#setLastWillProperties

    Parameters
    ----------

    prop : QMqttLastWillProperties
      Passed on as a value: Qt reads the C++ QMqttLastWillProperties, which
      stays Python's own.
    """
    #  void QMqttClient::setLastWillProperties(const QMqttLastWillProperties
    #      &prop)
    self.uglySide.call(
        'ritual_ZN11QMqttClient21setLastWillPropertiesERK23QMqttLastWillPro'
        'perties',
        self._valueOf(prop),
    )

  @overload(str)
  def setHostname(self, hostname: str) -> None:
    """
    Calls Qt's 'void QMqttClient::setHostname(const QString &hostname)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setHostname

    Parameters
    ----------

    hostname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::setHostname(const QString &hostname)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11setHostnameERK7QString', hostname,
    )

  @overload(int)
  def setPort(self, port: int) -> None:
    """
    Calls Qt's 'void QMqttClient::setPort(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setPort

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QMqttClient::setPort(quint16 port)
    self.uglySide.call('ritual_ZN11QMqttClient7setPortEt', port)

  @overload(str)
  def setClientId(self, clientId: str) -> None:
    """
    Calls Qt's 'void QMqttClient::setClientId(const QString &clientId)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setClientId

    Parameters
    ----------

    clientId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::setClientId(const QString &clientId)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11setClientIdERK7QString', clientId,
    )

  @overload(int)
  def setKeepAlive(self, keepAlive: int) -> None:
    """
    Calls Qt's 'void QMqttClient::setKeepAlive(quint16 keepAlive)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setKeepAlive

    Parameters
    ----------

    keepAlive : int
      Passed on as it is.
    """
    #  void QMqttClient::setKeepAlive(quint16 keepAlive)
    self.uglySide.call('ritual_ZN11QMqttClient12setKeepAliveEt', keepAlive)

  @overload(ProtocolVersion)
  def setProtocolVersion(self, protocolVersion: ProtocolVersion) -> None:
    """
    Calls Qt's 'void QMqttClient::setProtocolVersion(ProtocolVersion
    protocolVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#setProtocolVersion

    Parameters
    ----------

    protocolVersion : ProtocolVersion
      Passed on as its number.
    """
    #  void QMqttClient::setProtocolVersion(ProtocolVersion protocolVersion)
    self.uglySide.call(
        'ritual_ZN11QMqttClient18setProtocolVersionENS_15ProtocolVersionE',
        protocolVersion.value,
    )

  @overload(ClientState)
  def setState(self, state: ClientState) -> None:
    """
    Calls Qt's 'void QMqttClient::setState(ClientState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setState

    Parameters
    ----------

    state : ClientState
      Passed on as its number.
    """
    #  void QMqttClient::setState(ClientState state)
    self.uglySide.call(
        'ritual_ZN11QMqttClient8setStateENS_11ClientStateE', state.value,
    )

  @overload(ClientError)
  def setError(self, error: ClientError) -> None:
    """
    Calls Qt's 'void QMqttClient::setError(ClientError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setError

    Parameters
    ----------

    error : ClientError
      Passed on as its number.
    """
    #  void QMqttClient::setError(ClientError error)
    self.uglySide.call(
        'ritual_ZN11QMqttClient8setErrorENS_11ClientErrorE', error.value,
    )

  @overload(str)
  def setUsername(self, username: str) -> None:
    """
    Calls Qt's 'void QMqttClient::setUsername(const QString &username)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setUsername

    Parameters
    ----------

    username : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::setUsername(const QString &username)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11setUsernameERK7QString', username,
    )

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QMqttClient::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11setPasswordERK7QString', password,
    )

  @overload(bool)
  def setCleanSession(self, cleanSession: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::setCleanSession(bool cleanSession)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setCleanSession

    Parameters
    ----------

    cleanSession : bool
      Passed on as it is.
    """
    #  void QMqttClient::setCleanSession(bool cleanSession)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15setCleanSessionEb', cleanSession,
    )

  @overload(str)
  def setWillTopic(self, willTopic: str) -> None:
    """
    Calls Qt's 'void QMqttClient::setWillTopic(const QString &willTopic)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setWillTopic

    Parameters
    ----------

    willTopic : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::setWillTopic(const QString &willTopic)
    self.uglySide.call(
        'ritual_ZN11QMqttClient12setWillTopicERK7QString', willTopic,
    )

  @overload(int)
  def setWillQoS(self, willQoS: int) -> None:
    """
    Calls Qt's 'void QMqttClient::setWillQoS(quint8 willQoS)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setWillQoS

    Parameters
    ----------

    willQoS : int
      Passed on as it is.
    """
    #  void QMqttClient::setWillQoS(quint8 willQoS)
    self.uglySide.call('ritual_ZN11QMqttClient10setWillQoSEh', willQoS)

  @overload(QByteArray)
  def setWillMessage(self, willMessage: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttClient::setWillMessage(const QByteArray
    &willMessage)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setWillMessage

    Parameters
    ----------

    willMessage : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttClient::setWillMessage(const QByteArray &willMessage)
    self.uglySide.call(
        'ritual_ZN11QMqttClient14setWillMessageERK10QByteArray',
        self._valueOf(willMessage),
    )

  @overload(bool)
  def setWillRetain(self, willRetain: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::setWillRetain(bool willRetain)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setWillRetain

    Parameters
    ----------

    willRetain : bool
      Passed on as it is.
    """
    #  void QMqttClient::setWillRetain(bool willRetain)
    self.uglySide.call('ritual_ZN11QMqttClient13setWillRetainEb', willRetain)

  @overload(bool)
  def setAutoKeepAlive(self, autoKeepAlive: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::setAutoKeepAlive(bool autoKeepAlive)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#setAutoKeepAlive

    Parameters
    ----------

    autoKeepAlive : bool
      Passed on as it is.
    """
    #  void QMqttClient::setAutoKeepAlive(bool autoKeepAlive)
    self.uglySide.call(
        'ritual_ZN11QMqttClient16setAutoKeepAliveEb', autoKeepAlive,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QMqttClient::QMqttClient(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#QMqttClient

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMqttClient::QMqttClient(QObject *parent)
    self._noteCreation(QMqttClient, lambda: Rituals.call(
        'ritual_ZN11QMqttClientC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMqttTopicFilter)
  @overload(QMqttTopicFilter, int)
  def subscribe(
      self,
      topic: QMqttTopicFilter,
      qos: int = 0,
  ) -> Optional[QMqttSubscription]:
    """
    Calls Qt's 'QMqttSubscription *QMqttClient::subscribe(const
    QMqttTopicFilter &topic, quint8 qos)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#subscribe

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.

    qos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QMqttSubscription]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttSubscription *QMqttClient::subscribe(const QMqttTopicFilter
    #      &topic, quint8 qos)
    address = self.uglySide.call(
        'ritual_ZN11QMqttClient9subscribeERK16QMqttTopicFilterh',
        self._valueOf(topic), qos,
    )
    from . import QMqttSubscription
    return QMqttSubscription._cuteAt(address)

  @overload(QMqttTopicFilter, QMqttSubscriptionProperties)
  @overload(QMqttTopicFilter, QMqttSubscriptionProperties, int)
  def subscribe(
      self,
      topic: QMqttTopicFilter,
      properties: QMqttSubscriptionProperties,
      qos: int = 0,
  ) -> Optional[QMqttSubscription]:
    """
    Calls Qt's 'QMqttSubscription *QMqttClient::subscribe(const
    QMqttTopicFilter &topic, const QMqttSubscriptionProperties &properties,
    quint8 qos)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#subscribe

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.

    properties : QMqttSubscriptionProperties
      Passed on as a value: Qt reads the C++ QMqttSubscriptionProperties,
      which stays Python's own.

    qos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QMqttSubscription]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttSubscription *QMqttClient::subscribe(const QMqttTopicFilter
    #      &topic, const QMqttSubscriptionProperties &properties, quint8 qos)
    address = self.uglySide.call(
        'ritual_ZN11QMqttClient9subscribeERK16QMqttTopicFilterRK27QMqttSubs'
        'criptionPropertiesh',
        self._valueOf(topic), self._valueOf(properties), qos,
    )
    from . import QMqttSubscription
    return QMqttSubscription._cuteAt(address)

  @overload(QMqttTopicFilter)
  def unsubscribe(self, topic: QMqttTopicFilter) -> None:
    """
    Calls Qt's 'void QMqttClient::unsubscribe(const QMqttTopicFilter
    &topic)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#unsubscribe

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  void QMqttClient::unsubscribe(const QMqttTopicFilter &topic)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11unsubscribeERK16QMqttTopicFilter',
        self._valueOf(topic),
    )

  @overload(QMqttTopicFilter, QMqttUnsubscriptionProperties)
  def unsubscribe(
      self,
      topic: QMqttTopicFilter,
      properties: QMqttUnsubscriptionProperties,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::unsubscribe(const QMqttTopicFilter &topic,
    const QMqttUnsubscriptionProperties &properties)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#unsubscribe

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.

    properties : QMqttUnsubscriptionProperties
      Passed on as a value: Qt reads the C++ QMqttUnsubscriptionProperties,
      which stays Python's own.
    """
    #  void QMqttClient::unsubscribe(const QMqttTopicFilter &topic, const
    #      QMqttUnsubscriptionProperties &properties)
    self.uglySide.call(
        'ritual_ZN11QMqttClient11unsubscribeERK16QMqttTopicFilterRK29QMqttU'
        'nsubscriptionProperties',
        self._valueOf(topic), self._valueOf(properties),
    )

  @overload(QMqttTopicName)
  @overload(QMqttTopicName, QByteArray)
  @overload(QMqttTopicName, QByteArray, int)
  @overload(QMqttTopicName, QByteArray, int, bool)
  def publish(
      self,
      topic: QMqttTopicName,
      message: Optional[QByteArray] = None,
      qos: int = 0,
      retain: bool = False,
  ) -> int:
    """
    Calls Qt's 'qint32 QMqttClient::publish(const QMqttTopicName &topic,
    const QByteArray &message, quint8 qos, bool retain)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#publish

    Parameters
    ----------

    topic : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.

    message : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    qos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    retain : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  qint32 QMqttClient::publish(const QMqttTopicName &topic, const
    #      QByteArray &message, quint8 qos, bool retain)
    if message is None:
      from ..QtCore import QByteArray
      message = QByteArray()
    return self.uglySide.call(
        'ritual_ZN11QMqttClient7publishERK14QMqttTopicNameRK10QByteArrayhb',
        self._valueOf(topic), self._valueOf(message), qos, retain,
    )

  @overload(QMqttTopicName, QMqttPublishProperties)
  @overload(QMqttTopicName, QMqttPublishProperties, QByteArray)
  @overload(QMqttTopicName, QMqttPublishProperties, QByteArray, int)
  @overload(QMqttTopicName, QMqttPublishProperties, QByteArray, int, bool)
  def publish(
      self,
      topic: QMqttTopicName,
      properties: QMqttPublishProperties,
      message: Optional[QByteArray] = None,
      qos: int = 0,
      retain: bool = False,
  ) -> int:
    """
    Calls Qt's 'qint32 QMqttClient::publish(const QMqttTopicName &topic,
    const QMqttPublishProperties &properties, const QByteArray &message,
    quint8 qos, bool retain)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#publish

    Parameters
    ----------

    topic : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.

    properties : QMqttPublishProperties
      Passed on as a value: Qt reads the C++ QMqttPublishProperties, which
      stays Python's own.

    message : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    qos : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    retain : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  qint32 QMqttClient::publish(const QMqttTopicName &topic, const
    #      QMqttPublishProperties &properties, const QByteArray &message,
    #      quint8 qos, bool retain)
    if message is None:
      from ..QtCore import QByteArray
      message = QByteArray()
    return self.uglySide.call(
        'ritual_ZN11QMqttClient7publishERK14QMqttTopicNameRK22QMqttPublishP'
        'ropertiesRK10QByteArrayhb',
        self._valueOf(topic), self._valueOf(properties),
        self._valueOf(message), qos, retain,
    )

  def requestPing(self) -> bool:
    """
    Calls Qt's 'bool QMqttClient::requestPing()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#requestPing
    """
    #  bool QMqttClient::requestPing()
    return self.uglySide.call('ritual_ZN11QMqttClient11requestPingEv')

  @overload()
  def connectToHost(self) -> None:
    """
    Calls Qt's 'void QMqttClient::connectToHost()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#connectToHost
    """
    #  void QMqttClient::connectToHost()
    self.uglySide.call('ritual_ZN11QMqttClient13connectToHostEv')

  @overload(bool, str)
  def connectToHost(self, encrypted: bool, sslPeerName: str) -> None:
    """
    Calls Qt's 'void QMqttClient::connectToHost(bool encrypted, const QString
    &sslPeerName)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#connectToHost

    Parameters
    ----------

    encrypted : bool
      Passed on as it is.

    sslPeerName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::connectToHost(bool encrypted, const QString
    #      &sslPeerName)
    self.uglySide.call(
        'ritual_ZN11QMqttClient13connectToHostEbRK7QString',
        encrypted, sslPeerName,
    )

  @overload(QSslConfiguration)
  def connectToHostEncrypted(self, conf: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QMqttClient::connectToHostEncrypted(const
    QSslConfiguration &conf)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#connectToHostEncrypted

    Parameters
    ----------

    conf : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QMqttClient::connectToHostEncrypted(const QSslConfiguration
    #      &conf)
    self.uglySide.call(
        'ritual_ZN11QMqttClient22connectToHostEncryptedERK17QSslConfigurati'
        'on',
        self._valueOf(conf),
    )

  @overload()
  @overload(QWebSocket)
  @overload(NoneType)
  def connectToHostWebSocket(
      self,
      webSocket: Optional[QWebSocket] = None,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::connectToHostWebSocket(QWebSocket
    *webSocket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#connectToHostWebSocket

    Parameters
    ----------

    webSocket : Optional[QWebSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QMqttClient::connectToHostWebSocket(QWebSocket *webSocket)
    self.uglySide.call(
        'ritual_ZN11QMqttClient22connectToHostWebSocketEP10QWebSocket',
        self._addressOf(webSocket),
    )

  @overload()
  @overload(QWebSocket)
  @overload(NoneType)
  def connectToHostWebSocketEncrypted(
      self,
      webSocket: Optional[QWebSocket] = None,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::connectToHostWebSocketEncrypted(QWebSocket
    *webSocket)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#connectToHostWebSocketEncrypted

    Parameters
    ----------

    webSocket : Optional[QWebSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QMqttClient::connectToHostWebSocketEncrypted(QWebSocket
    #      *webSocket)
    self.uglySide.call(
        'ritual_ZN11QMqttClient31connectToHostWebSocketEncryptedEP10QWebSoc'
        'ket',
        self._addressOf(webSocket),
    )

  def disconnectFromHost(self) -> None:
    """
    Calls Qt's 'void QMqttClient::disconnectFromHost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#disconnectFromHost
    """
    #  void QMqttClient::disconnectFromHost()
    self.uglySide.call('ritual_ZN11QMqttClient18disconnectFromHostEv')

  @overload(QMqttAuthenticationProperties)
  def authenticate(self, prop: QMqttAuthenticationProperties) -> None:
    """
    Calls Qt's 'void QMqttClient::authenticate(const
    QMqttAuthenticationProperties &prop)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#authenticate

    Parameters
    ----------

    prop : QMqttAuthenticationProperties
      Passed on as a value: Qt reads the C++ QMqttAuthenticationProperties,
      which stays Python's own.
    """
    #  void QMqttClient::authenticate(const QMqttAuthenticationProperties
    #      &prop)
    self.uglySide.call(
        'ritual_ZN11QMqttClient12authenticateERK29QMqttAuthenticationProper'
        'ties',
        self._valueOf(prop),
    )

  def connected(self) -> None:
    """
    Calls Qt's 'void QMqttClient::connected()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#connected
    """
    #  void QMqttClient::connected()
    self.uglySide.call('ritual_ZN11QMqttClient9connectedEv')

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QMqttClient::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#disconnected
    """
    #  void QMqttClient::disconnected()
    self.uglySide.call('ritual_ZN11QMqttClient12disconnectedEv')

  @overload(QByteArray, QMqttTopicName)
  def messageReceived(
      self,
      message: QByteArray,
      topic: QMqttTopicName,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::messageReceived(const QByteArray &message,
    const QMqttTopicName &topic)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#messageReceived

    Parameters
    ----------

    message : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    topic : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.
    """
    #  void QMqttClient::messageReceived(const QByteArray &message, const
    #      QMqttTopicName &topic)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15messageReceivedERK10QByteArrayRK14QMqttTop'
        'icName',
        self._valueOf(message), self._valueOf(topic),
    )

  @overload(int, QMqtt.MessageStatus, QMqttMessageStatusProperties)
  def messageStatusChanged(
      self,
      id: int,
      s: QMqtt.MessageStatus,
      properties: QMqttMessageStatusProperties,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::messageStatusChanged(qint32 id,
    QMqtt::MessageStatus s, const QMqttMessageStatusProperties &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#messageStatusChanged

    Parameters
    ----------

    id : int
      Passed on as it is.

    s : QMqtt.MessageStatus
      Passed on as its number.

    properties : QMqttMessageStatusProperties
      Passed on as a value: Qt reads the C++ QMqttMessageStatusProperties,
      which stays Python's own.
    """
    #  void QMqttClient::messageStatusChanged(qint32 id, QMqtt::MessageStatus
    #      s, const QMqttMessageStatusProperties &properties)
    self.uglySide.call(
        'ritual_ZN11QMqttClient20messageStatusChangedEiN5QMqtt13MessageStat'
        'usERK28QMqttMessageStatusProperties',
        id, s.value, self._valueOf(properties),
    )

  @overload(int)
  def messageSent(self, id: int) -> None:
    """
    Calls Qt's 'void QMqttClient::messageSent(qint32 id)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#messageSent

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QMqttClient::messageSent(qint32 id)
    self.uglySide.call('ritual_ZN11QMqttClient11messageSentEi', id)

  def pingResponseReceived(self) -> None:
    """
    Calls Qt's 'void QMqttClient::pingResponseReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#pingResponseReceived
    """
    #  void QMqttClient::pingResponseReceived()
    self.uglySide.call('ritual_ZN11QMqttClient20pingResponseReceivedEv')

  def brokerSessionRestored(self) -> None:
    """
    Calls Qt's 'void QMqttClient::brokerSessionRestored()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#brokerSessionRestored
    """
    #  void QMqttClient::brokerSessionRestored()
    self.uglySide.call('ritual_ZN11QMqttClient21brokerSessionRestoredEv')

  @overload(str)
  def hostnameChanged(self, hostname: str) -> None:
    """
    Calls Qt's 'void QMqttClient::hostnameChanged(QString hostname)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#hostnameChanged

    Parameters
    ----------

    hostname : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::hostnameChanged(QString hostname)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15hostnameChangedE7QString', hostname,
    )

  @overload(int)
  def portChanged(self, port: int) -> None:
    """
    Calls Qt's 'void QMqttClient::portChanged(quint16 port)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#portChanged

    Parameters
    ----------

    port : int
      Passed on as it is.
    """
    #  void QMqttClient::portChanged(quint16 port)
    self.uglySide.call('ritual_ZN11QMqttClient11portChangedEt', port)

  @overload(str)
  def clientIdChanged(self, clientId: str) -> None:
    """
    Calls Qt's 'void QMqttClient::clientIdChanged(QString clientId)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#clientIdChanged

    Parameters
    ----------

    clientId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::clientIdChanged(QString clientId)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15clientIdChangedE7QString', clientId,
    )

  @overload(int)
  def keepAliveChanged(self, keepAlive: int) -> None:
    """
    Calls Qt's 'void QMqttClient::keepAliveChanged(quint16 keepAlive)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#keepAliveChanged

    Parameters
    ----------

    keepAlive : int
      Passed on as it is.
    """
    #  void QMqttClient::keepAliveChanged(quint16 keepAlive)
    self.uglySide.call(
        'ritual_ZN11QMqttClient16keepAliveChangedEt', keepAlive,
    )

  @overload(ProtocolVersion)
  def protocolVersionChanged(self, protocolVersion: ProtocolVersion) -> None:
    """
    Calls Qt's 'void QMqttClient::protocolVersionChanged(ProtocolVersion
    protocolVersion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#protocolVersionChanged

    Parameters
    ----------

    protocolVersion : ProtocolVersion
      Passed on as its number.
    """
    #  void QMqttClient::protocolVersionChanged(ProtocolVersion
    #      protocolVersion)
    self.uglySide.call(
        'ritual_ZN11QMqttClient22protocolVersionChangedENS_15ProtocolVersio'
        'nE',
        protocolVersion.value,
    )

  @overload(ClientState)
  def stateChanged(self, state: ClientState) -> None:
    """
    Calls Qt's 'void QMqttClient::stateChanged(ClientState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#stateChanged

    Parameters
    ----------

    state : ClientState
      Passed on as its number.
    """
    #  void QMqttClient::stateChanged(ClientState state)
    self.uglySide.call(
        'ritual_ZN11QMqttClient12stateChangedENS_11ClientStateE',
        state.value,
    )

  @overload(ClientError)
  def errorChanged(self, error: ClientError) -> None:
    """
    Calls Qt's 'void QMqttClient::errorChanged(ClientError error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#errorChanged

    Parameters
    ----------

    error : ClientError
      Passed on as its number.
    """
    #  void QMqttClient::errorChanged(ClientError error)
    self.uglySide.call(
        'ritual_ZN11QMqttClient12errorChangedENS_11ClientErrorE',
        error.value,
    )

  @overload(str)
  def usernameChanged(self, username: str) -> None:
    """
    Calls Qt's 'void QMqttClient::usernameChanged(QString username)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#usernameChanged

    Parameters
    ----------

    username : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::usernameChanged(QString username)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15usernameChangedE7QString', username,
    )

  @overload(str)
  def passwordChanged(self, password: str) -> None:
    """
    Calls Qt's 'void QMqttClient::passwordChanged(QString password)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#passwordChanged

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::passwordChanged(QString password)
    self.uglySide.call(
        'ritual_ZN11QMqttClient15passwordChangedE7QString', password,
    )

  @overload(bool)
  def cleanSessionChanged(self, cleanSession: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::cleanSessionChanged(bool cleanSession)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#cleanSessionChanged

    Parameters
    ----------

    cleanSession : bool
      Passed on as it is.
    """
    #  void QMqttClient::cleanSessionChanged(bool cleanSession)
    self.uglySide.call(
        'ritual_ZN11QMqttClient19cleanSessionChangedEb', cleanSession,
    )

  @overload(str)
  def willTopicChanged(self, willTopic: str) -> None:
    """
    Calls Qt's 'void QMqttClient::willTopicChanged(QString willTopic)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willTopicChanged

    Parameters
    ----------

    willTopic : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttClient::willTopicChanged(QString willTopic)
    self.uglySide.call(
        'ritual_ZN11QMqttClient16willTopicChangedE7QString', willTopic,
    )

  @overload(int)
  def willQoSChanged(self, willQoS: int) -> None:
    """
    Calls Qt's 'void QMqttClient::willQoSChanged(quint8 willQoS)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willQoSChanged

    Parameters
    ----------

    willQoS : int
      Passed on as it is.
    """
    #  void QMqttClient::willQoSChanged(quint8 willQoS)
    self.uglySide.call('ritual_ZN11QMqttClient14willQoSChangedEh', willQoS)

  @overload(QByteArray)
  def willMessageChanged(self, willMessage: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttClient::willMessageChanged(QByteArray
    willMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#willMessageChanged

    Parameters
    ----------

    willMessage : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttClient::willMessageChanged(QByteArray willMessage)
    self.uglySide.call(
        'ritual_ZN11QMqttClient18willMessageChangedE10QByteArray',
        self._valueOf(willMessage),
    )

  @overload(bool)
  def willRetainChanged(self, willRetain: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::willRetainChanged(bool willRetain)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#willRetainChanged

    Parameters
    ----------

    willRetain : bool
      Passed on as it is.
    """
    #  void QMqttClient::willRetainChanged(bool willRetain)
    self.uglySide.call(
        'ritual_ZN11QMqttClient17willRetainChangedEb', willRetain,
    )

  @overload(bool)
  def autoKeepAliveChanged(self, autoKeepAlive: bool) -> None:
    """
    Calls Qt's 'void QMqttClient::autoKeepAliveChanged(bool autoKeepAlive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#autoKeepAliveChanged

    Parameters
    ----------

    autoKeepAlive : bool
      Passed on as it is.
    """
    #  void QMqttClient::autoKeepAliveChanged(bool autoKeepAlive)
    self.uglySide.call(
        'ritual_ZN11QMqttClient20autoKeepAliveChangedEb', autoKeepAlive,
    )

  @overload(QMqttAuthenticationProperties)
  def authenticationRequested(
      self,
      p: QMqttAuthenticationProperties,
  ) -> None:
    """
    Calls Qt's 'void QMqttClient::authenticationRequested(const
    QMqttAuthenticationProperties &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#authenticationRequested

    Parameters
    ----------

    p : QMqttAuthenticationProperties
      Passed on as a value: Qt reads the C++ QMqttAuthenticationProperties,
      which stays Python's own.
    """
    #  void QMqttClient::authenticationRequested(const
    #      QMqttAuthenticationProperties &p)
    self.uglySide.call(
        'ritual_ZN11QMqttClient23authenticationRequestedERK29QMqttAuthentic'
        'ationProperties',
        self._valueOf(p),
    )

  @overload(QMqttAuthenticationProperties)
  def authenticationFinished(self, p: QMqttAuthenticationProperties) -> None:
    """
    Calls Qt's 'void QMqttClient::authenticationFinished(const
    QMqttAuthenticationProperties &p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttclient.html#authenticationFinished

    Parameters
    ----------

    p : QMqttAuthenticationProperties
      Passed on as a value: Qt reads the C++ QMqttAuthenticationProperties,
      which stays Python's own.
    """
    #  void QMqttClient::authenticationFinished(const
    #      QMqttAuthenticationProperties &p)
    self.uglySide.call(
        'ritual_ZN11QMqttClient22authenticationFinishedERK29QMqttAuthentica'
        'tionProperties',
        self._valueOf(p),
    )

  def d_func(self) -> Optional[QMqttClientPrivate]:
    """
    Calls Qt's 'QMqttClientPrivate *QMqttClient::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttclient.html#d_func

    Returns
    -------

    Optional[QMqttClientPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttClientPrivate *QMqttClient::d_func()
    address = self.uglySide.call('ritual_ZN11QMqttClient6d_funcEv')
    from . import QMqttClientPrivate
    return QMqttClientPrivate._cuteAt(address)
