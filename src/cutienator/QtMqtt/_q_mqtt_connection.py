"""
QMqttConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/6.12.0/QtMqtt/private/qmqttconnection_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMqttConnection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QObject
from ..QtNetwork import QAbstractSocket
from . import QMqttClient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice, QMetaObject, QTimerEvent
  from . import QMqttClientPrivate, QMqttSubscription, QMqttTopicFilter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMqttClientPrivate = WAIT['QMqttClientPrivate']
  QMqttSubscription = WAIT['QMqttSubscription']
  QMqttTopicFilter = WAIT['QMqttTopicFilter']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMqttConnection(QObject):
  """
  The cute side of Qt's QMqttConnection: a plain Python object standing in
  front of one C++ QMqttConnection.

  It is built on the cute 'QObject', as Qt's QMqttConnection is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMqttConnection that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'transport',
  'setClientPrivate', 'unusedPacketIdentifier', 'internalState',
  'setClientDestruction', 'cleanSubscriptions', 'transportConnectionClosed',
  'transportError', 'timerEvent', 'closeConnection', 'readBuffer',
  'isPendingUnsubscribe', 'findActiveSubscription'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMqttConnection::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QMqttConnection::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMqttConnection::~QMqttConnection()': the destructor: Python never
    removes a C++ QMqttConnection.
  - Qt's 'bool QMqttConnection::readBuffer(char *data, quint64 size)': names
    'char', which has no cute class yet.

  What has no ritual
  ------------------

  47 of the 65 functions Qt declares: 17 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 10 leans on
  'QMqttControlPacket; 9 leans on 'QMqttConnection; 3 leans on 'QByteArray
  QMqttConnection; 2 not a gap; 2 forbidden; 2 leans on 'QString
  QMqttConnection; 1 a template; 1 leans on 'unsigned char QMqttConnection.

  What to expect
  --------------

  - The C++ QMqttConnection is created at the first use, not by
    'QMqttConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMqttConnection.
  - Qt tells when it has removed the C++ QMqttConnection. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMqttConnection that has no cute function yet,
    '__init__', 'connectTransport', 'disconnectAndResetTransport',
    'ensureTransport', 'ensureTransportOpen', 'finalize_auth',
    'finalize_connack', 'finalize_pingresp', 'finalize_pubAckRecRelComp',
    'finalize_publish', 'finalize_suback', 'finalize_unsuback',
    'processData', 'processDataHelper', 'readAuthProperties',
    'readBufferTyped', 'readConnackProperties',
    'readMessageStatusProperties', 'readPublishProperties',
    'readSubscriptionProperties', 'readVariableByteInteger',
    'sendControlAuthenticate', 'sendControlConnect', 'sendControlDisconnect',
    'sendControlPingRequest', 'sendControlPublish',
    'sendControlPublishAcknowledge', 'sendControlPublishComp',
    'sendControlPublishReceive', 'sendControlPublishRelease',
    'sendControlSubscribe', 'sendControlUnsubscribe', 'setTransport',
    'transportConnectionEstablished', 'transportReadyRead',
    'writeAuthenticationProperties', 'writeConnectProperties',
    'writeLastWillProperties', 'writePacketToTransport',
    'writePublishProperties', 'writeSubscriptionProperties',
    'writeUnsubscriptionProperties', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMqttConnection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InternalConnectionState(CuteNum):
    """
    The enum 'QMqttConnection::InternalConnectionState' of Qt, with the 5
    names Qt gives in it.
    """

    BrokerDisconnected = Kee[int](0)
    BrokerConnecting = Kee[int](1)
    BrokerWaitForConnectAck = Kee[int](2)
    BrokerConnected = Kee[int](3)
    ClientDestruction = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttConnection'

  #  A C++ QMqttConnection Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMqttConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMqttConnection::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttconnection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMqttConnection::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QMqttConnection10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def transport(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QMqttConnection::transport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttconnection.html#transport

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QMqttConnection::transport() const
    address = self.uglySide.call('ritual_ZNK15QMqttConnection9transportEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def unusedPacketIdentifier(self) -> int:
    """
    Calls Qt's 'quint16 QMqttConnection::unusedPacketIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#unusedPacketIdentifier
    """
    #  quint16 QMqttConnection::unusedPacketIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK15QMqttConnection22unusedPacketIdentifierEv',
    )

  def internalState(self) -> InternalConnectionState:
    """
    Calls Qt's 'InternalConnectionState QMqttConnection::internalState()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttconnection.html#internalState

    Returns
    -------

    InternalConnectionState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InternalConnectionState(number)' gives.
    """
    #  InternalConnectionState QMqttConnection::internalState() const
    return QMqttConnection.InternalConnectionState(self.uglySide.call(
        'ritual_ZNK15QMqttConnection13internalStateEv',
    ))

  @overload(QMqttSubscription)
  @overload(NoneType)
  def isPendingUnsubscribe(self, a0: Optional[QMqttSubscription]) -> bool:
    """
    Calls Qt's 'bool QMqttConnection::isPendingUnsubscribe(QMqttSubscription
    *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#isPendingUnsubscribe

    Parameters
    ----------

    a0 : Optional[QMqttSubscription]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMqttConnection::isPendingUnsubscribe(QMqttSubscription *a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QMqttConnection20isPendingUnsubscribeEP17QMqttSubscrip'
        'tion',
        self._addressOf(a0),
    )

  @overload(QMqttTopicFilter)
  def findActiveSubscription(
      self,
      topic: QMqttTopicFilter,
  ) -> Optional[QMqttSubscription]:
    """
    Calls Qt's 'QMqttSubscription
    *QMqttConnection::findActiveSubscription(const QMqttTopicFilter &topic)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#findActiveSubscription

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.

    Returns
    -------

    Optional[QMqttSubscription]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttSubscription *QMqttConnection::findActiveSubscription(const
    #      QMqttTopicFilter &topic) const
    address = self.uglySide.call(
        'ritual_ZNK15QMqttConnection22findActiveSubscriptionERK16QMqttTopic'
        'Filter',
        self._valueOf(topic),
    )
    from . import QMqttSubscription
    return QMqttSubscription._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMqttClientPrivate)
  @overload(NoneType)
  def setClientPrivate(
      self,
      clientPrivate: Optional[QMqttClientPrivate],
  ) -> None:
    """
    Calls Qt's 'void QMqttConnection::setClientPrivate(QMqttClientPrivate
    *clientPrivate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#setClientPrivate

    Parameters
    ----------

    clientPrivate : Optional[QMqttClientPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMqttConnection::setClientPrivate(QMqttClientPrivate
    #      *clientPrivate)
    self.uglySide.call(
        'ritual_ZN15QMqttConnection16setClientPrivateEP18QMqttClientPrivate',
        self._addressOf(clientPrivate),
    )

  def setClientDestruction(self) -> None:
    """
    Calls Qt's 'void QMqttConnection::setClientDestruction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#setClientDestruction
    """
    #  void QMqttConnection::setClientDestruction()
    self.uglySide.call('ritual_ZN15QMqttConnection20setClientDestructionEv')

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
    Qt's 'QMqttConnection::QMqttConnection(QObject *parent)': leans on
    'QMqttConnection::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.__init__' has no cute function yet. Qt's "
        "'QMqttConnection::QMqttConnection(QObject *parent)': leans on "
        "'QMqttConnection::qt_metacall(QMetaObject::Call, int, void**)', "
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

  def cleanSubscriptions(self) -> None:
    """
    Calls Qt's 'void QMqttConnection::cleanSubscriptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#cleanSubscriptions
    """
    #  void QMqttConnection::cleanSubscriptions()
    self.uglySide.call('ritual_ZN15QMqttConnection18cleanSubscriptionsEv')

  def transportConnectionClosed(self) -> None:
    """
    Calls Qt's 'void QMqttConnection::transportConnectionClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#transportConnectionClosed
    """
    #  void QMqttConnection::transportConnectionClosed()
    self.uglySide.call(
        'ritual_ZN15QMqttConnection25transportConnectionClosedEv',
    )

  @overload(QAbstractSocket.SocketError)
  def transportError(self, e: QAbstractSocket.SocketError) -> None:
    """
    Calls Qt's 'void
    QMqttConnection::transportError(QAbstractSocket::SocketError e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#transportError

    Parameters
    ----------

    e : QAbstractSocket.SocketError
      Passed on as its number.
    """
    #  void QMqttConnection::transportError(QAbstractSocket::SocketError e)
    self.uglySide.call(
        'ritual_ZN15QMqttConnection14transportErrorEN15QAbstractSocket11Soc'
        'ketErrorE',
        e.value,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMqttConnection::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttconnection.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMqttConnection::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN15QMqttConnection10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  @overload(QMqttClient.ClientError)
  def closeConnection(self, error: QMqttClient.ClientError) -> None:
    """
    Calls Qt's 'void
    QMqttConnection::closeConnection(QMqttClient::ClientError error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttconnection.html#closeConnection

    Parameters
    ----------

    error : QMqttClient.ClientError
      Passed on as its number.
    """
    #  void QMqttConnection::closeConnection(QMqttClient::ClientError error)
    self.uglySide.call(
        'ritual_ZN15QMqttConnection15closeConnectionEN11QMqttClient11Client'
        'ErrorE',
        error.value,
    )

  @overload(int)
  def readBuffer(self, size: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttConnection::readBuffer(quint64 size)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttconnection.html#readBuffer

    Parameters
    ----------

    size : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttConnection::readBuffer(quint64 size)
    address = self.uglySide.call(
        'ritual_ZN15QMqttConnection10readBufferEy', size,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def connectTransport(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::connectTransport(QMqttClient::TransportType
    transport, const std::shared_ptr<QIODevice> &device)': leans on
    'QMqttConnection::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.connectTransport' has no cute function yet. Qt's "
        "'void QMqttConnection::connectTransport(QMqttClient::TransportType "
        "transport, const std::shared_ptr<QIODevice> &device)': leans on "
        "'QMqttConnection::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def disconnectAndResetTransport(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::disconnectAndResetTransport()': leans on
    'QMqttConnection::transportReadyRead()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.disconnectAndResetTransport' has no cute function "
        "yet. Qt's 'void QMqttConnection::disconnectAndResetTransport()': "
        "leans on 'QMqttConnection::transportReadyRead()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def ensureTransport(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::ensureTransport(bool createSecureIfNeeded)':
    leans on 'QMqttConnection::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.ensureTransport' has no cute function yet. Qt's "
        "'bool QMqttConnection::ensureTransport(bool "
        "createSecureIfNeeded)': leans on "
        "'QMqttConnection::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def ensureTransportOpen(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::ensureTransportOpen(const QString
    &sslPeerName)': leans on 'QMqttControlPacket::append(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.ensureTransportOpen' has no cute function yet. "
        "Qt's 'bool QMqttConnection::ensureTransportOpen(const QString "
        "&sslPeerName)': leans on 'QMqttControlPacket::append(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def finalize_auth(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_auth()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_auth' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_auth()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'lcMqttConnectionVerbose'; "
        "did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_connack(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_connack()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_connack' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_connack()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_pingresp(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_pingresp()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'lcMqttConnectionVerbose'; did you
    mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_pingresp' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_pingresp()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_pubAckRecRelComp(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_pubAckRecRelComp()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcMqttConnectionVerbose';
    did you mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_pubAckRecRelComp' has no cute function "
        "yet. Qt's 'void QMqttConnection::finalize_pubAckRecRelComp()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_publish(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_publish()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_publish' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_publish()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_suback(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_suback()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_suback' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_suback()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def finalize_unsuback(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::finalize_unsuback()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'lcMqttConnectionVerbose'; did you
    mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.finalize_unsuback' has no cute function yet. Qt's "
        "'void QMqttConnection::finalize_unsuback()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def processData(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::processData()': leans on
    'QMqttConnection::processDataHelper()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.processData' has no cute function yet. Qt's 'void "
        "QMqttConnection::processData()': leans on "
        "'QMqttConnection::processDataHelper()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def processDataHelper(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::processDataHelper()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'lcMqttConnectionVerbose'; did you
    mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.processDataHelper' has no cute function yet. Qt's "
        "'bool QMqttConnection::processDataHelper()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def readAuthProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QMqttConnection::readAuthProperties(QMqttAuthenticationProperties
    &properties)': leans on 'QByteArray
    QMqttConnection::readBufferTyped<QByteArray>(long long*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readAuthProperties' has no cute function yet. "
        "Qt's 'void "
        "QMqttConnection::readAuthProperties(QMqttAuthenticationProperties "
        "&properties)': leans on 'QByteArray "
        "QMqttConnection::readBufferTyped<QByteArray>(long long*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def readBufferTyped(*__, **_) -> Never:
    """
    Qt's 'QMqttConnection::readBufferTyped': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QMqttConnection.readBufferTyped' has no cute function yet. Qt's "
        "'QMqttConnection::readBufferTyped': a template: a pattern and no "
        "single function.")

  @staticmethod
  def readConnackProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QMqttConnection::readConnackProperties(QMqttServerConnectionProperties
    &properties)': leans on 'QByteArray
    QMqttConnection::readBufferTyped<QByteArray>(long long*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readConnackProperties' has no cute function yet. "
        "Qt's 'void "
        "QMqttConnection::readConnackProperties(QMqttServerConnectionPropert"
        "ies &properties)': leans on 'QByteArray "
        "QMqttConnection::readBufferTyped<QByteArray>(long long*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def readMessageStatusProperties(*__, **_) -> Never:
    """
    Qt's 'void
    QMqttConnection::readMessageStatusProperties(QMqttMessageStatusProperties
    &properties)': leans on 'QString
    QMqttConnection::readBufferTyped<QString>(long long*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readMessageStatusProperties' has no cute function "
        "yet. Qt's 'void "
        "QMqttConnection::readMessageStatusProperties(QMqttMessageStatusProp"
        "erties &properties)': leans on 'QString "
        "QMqttConnection::readBufferTyped<QString>(long long*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def readPublishProperties(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::readPublishProperties(QMqttPublishProperties
    &properties)': leans on 'QByteArray
    QMqttConnection::readBufferTyped<QByteArray>(long long*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readPublishProperties' has no cute function yet. "
        "Qt's 'void "
        "QMqttConnection::readPublishProperties(QMqttPublishProperties "
        "&properties)': leans on 'QByteArray "
        "QMqttConnection::readBufferTyped<QByteArray>(long long*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def readSubscriptionProperties(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::readSubscriptionProperties(QMqttSubscription
    *sub)': leans on 'QString QMqttConnection::readBufferTyped<QString>(long
    long*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readSubscriptionProperties' has no cute function "
        "yet. Qt's 'void "
        "QMqttConnection::readSubscriptionProperties(QMqttSubscription "
        "*sub)': leans on 'QString "
        "QMqttConnection::readBufferTyped<QString>(long long*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def readVariableByteInteger(*__, **_) -> Never:
    """
    Qt's 'qint32 QMqttConnection::readVariableByteInteger(qint64 *dataSize)':
    leans on 'unsigned char QMqttConnection::readBufferTyped<unsigned
    char>(long long*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.readVariableByteInteger' has no cute function "
        "yet. Qt's 'qint32 QMqttConnection::readVariableByteInteger(qint64 "
        "*dataSize)': leans on 'unsigned char "
        "QMqttConnection::readBufferTyped<unsigned char>(long long*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def sendControlAuthenticate(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlAuthenticate(const
    QMqttAuthenticationProperties &properties)': leans on
    'QMqttControlPacket::append(char)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlAuthenticate' has no cute function "
        "yet. Qt's 'bool QMqttConnection::sendControlAuthenticate(const "
        "QMqttAuthenticationProperties &properties)': leans on "
        "'QMqttControlPacket::append(char)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def sendControlConnect(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlConnect()': leans on
    'QMqttControlPacket::append(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlConnect' has no cute function yet. "
        "Qt's 'bool QMqttConnection::sendControlConnect()': leans on "
        "'QMqttControlPacket::append(QByteArray const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sendControlDisconnect(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlDisconnect()': leans on
    'QMqttConnection::writePacketToTransport(QMqttControlPacket const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlDisconnect' has no cute function yet. "
        "Qt's 'bool QMqttConnection::sendControlDisconnect()': leans on "
        "'QMqttConnection::writePacketToTransport(QMqttControlPacket "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sendControlPingRequest(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlPingRequest(bool isAuto)': leans
    on 'QMqttConnection::writePacketToTransport(QMqttControlPacket const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPingRequest' has no cute function yet. "
        "Qt's 'bool QMqttConnection::sendControlPingRequest(bool isAuto)': "
        "leans on "
        "'QMqttConnection::writePacketToTransport(QMqttControlPacket "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sendControlPublish(*__, **_) -> Never:
    """
    Qt's 'qint32 QMqttConnection::sendControlPublish(const QMqttTopicName
    &topic, const QByteArray &message, quint8 qos, bool retain, const
    QMqttPublishProperties &properties)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPublish' has no cute function yet. "
        "Qt's 'qint32 QMqttConnection::sendControlPublish(const "
        "QMqttTopicName &topic, const QByteArray &message, quint8 qos, bool "
        "retain, const QMqttPublishProperties &properties)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def sendControlPublishAcknowledge(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlPublishAcknowledge(quint16 id)':
    leans on 'QMqttControlPacket::append(unsigned short)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPublishAcknowledge' has no cute "
        "function yet. Qt's 'bool "
        "QMqttConnection::sendControlPublishAcknowledge(quint16 id)': leans "
        "on 'QMqttControlPacket::append(unsigned short)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def sendControlPublishComp(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlPublishComp(quint16 id)': leans on
    'QMqttControlPacket::append(unsigned short)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPublishComp' has no cute function yet. "
        "Qt's 'bool QMqttConnection::sendControlPublishComp(quint16 id)': "
        "leans on 'QMqttControlPacket::append(unsigned short)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def sendControlPublishReceive(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlPublishReceive(quint16 id)': leans
    on 'QMqttControlPacket::append(unsigned short)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPublishReceive' has no cute function "
        "yet. Qt's 'bool QMqttConnection::sendControlPublishReceive(quint16 "
        "id)': leans on 'QMqttControlPacket::append(unsigned short)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendControlPublishRelease(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlPublishRelease(quint16 id)': leans
    on 'QMqttControlPacket::append(unsigned short)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlPublishRelease' has no cute function "
        "yet. Qt's 'bool QMqttConnection::sendControlPublishRelease(quint16 "
        "id)': leans on 'QMqttControlPacket::append(unsigned short)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def sendControlSubscribe(*__, **_) -> Never:
    """
    Qt's 'QMqttSubscription *QMqttConnection::sendControlSubscribe(const
    QMqttTopicFilter &topic, quint8 qos, const QMqttSubscriptionProperties
    &properties)': leans on 'QMqttControlPacket::append(QByteArray const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlSubscribe' has no cute function yet. "
        "Qt's 'QMqttSubscription "
        "*QMqttConnection::sendControlSubscribe(const QMqttTopicFilter "
        "&topic, quint8 qos, const QMqttSubscriptionProperties "
        "&properties)': leans on 'QMqttControlPacket::append(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def sendControlUnsubscribe(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::sendControlUnsubscribe(const QMqttTopicFilter
    &topic, const QMqttUnsubscriptionProperties &properties)': leans on
    'QMqttControlPacket::append(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.sendControlUnsubscribe' has no cute function yet. "
        "Qt's 'bool QMqttConnection::sendControlUnsubscribe(const "
        "QMqttTopicFilter &topic, const QMqttUnsubscriptionProperties "
        "&properties)': leans on 'QMqttControlPacket::append(QByteArray "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setTransport(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::setTransport(QIODevice *device,
    QMqttClient::TransportType transport)': leans on
    'QMqttConnection::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.setTransport' has no cute function yet. Qt's "
        "'void QMqttConnection::setTransport(QIODevice *device, "
        "QMqttClient::TransportType transport)': leans on "
        "'QMqttConnection::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def transportConnectionEstablished(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::transportConnectionEstablished()': leans on
    'QMqttControlPacket::append(QByteArray const&)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMqttConnection.transportConnectionEstablished' has no cute "
        "function yet. Qt's 'void "
        "QMqttConnection::transportConnectionEstablished()': leans on "
        "'QMqttControlPacket::append(QByteArray const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def transportReadyRead(*__, **_) -> Never:
    """
    Qt's 'void QMqttConnection::transportReadyRead()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'lcMqttConnectionVerbose'; did you
    mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.transportReadyRead' has no cute function yet. "
        "Qt's 'void QMqttConnection::transportReadyRead()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def writeAuthenticationProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writeAuthenticationProperties(const
    QMqttAuthenticationProperties &properties)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'lcMqttConnectionVerbose'.
    """
    raise NotImplementedError(
        "'QMqttConnection.writeAuthenticationProperties' has no cute "
        "function yet. Qt's 'QByteArray "
        "QMqttConnection::writeAuthenticationProperties(const "
        "QMqttAuthenticationProperties &properties)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'.")

  @staticmethod
  def writeConnectProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writeConnectProperties()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcMqttConnectionVerbose';
    did you mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.writeConnectProperties' has no cute function yet. "
        "Qt's 'QByteArray QMqttConnection::writeConnectProperties()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.")

  @staticmethod
  def writeLastWillProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writeLastWillProperties() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'lcMqttConnectionVerbose'; did you mean 'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.writeLastWillProperties' has no cute function "
        "yet. Qt's 'QByteArray QMqttConnection::writeLastWillProperties() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'lcMqttConnectionVerbose'; did you mean "
        "'lcMqttConnection'?.")

  @staticmethod
  def writePacketToTransport(*__, **_) -> Never:
    """
    Qt's 'bool QMqttConnection::writePacketToTransport(const
    QMqttControlPacket &p)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'lcMqttConnectionVerbose'.
    """
    raise NotImplementedError(
        "'QMqttConnection.writePacketToTransport' has no cute function yet. "
        "Qt's 'bool QMqttConnection::writePacketToTransport(const "
        "QMqttControlPacket &p)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcMqttConnectionVerbose'.")

  @staticmethod
  def writePublishProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writePublishProperties(const
    QMqttPublishProperties &properties)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'lcMqttConnectionVerbose'; did you mean
    'lcMqttConnection'?.
    """
    raise NotImplementedError(
        "'QMqttConnection.writePublishProperties' has no cute function yet. "
        "Qt's 'QByteArray QMqttConnection::writePublishProperties(const "
        "QMqttPublishProperties &properties)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'lcMqttConnectionVerbose'; did "
        "you mean 'lcMqttConnection'?.")

  @staticmethod
  def writeSubscriptionProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writeSubscriptionProperties(const
    QMqttSubscriptionProperties &properties)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'lcMqttConnectionVerbose'.
    """
    raise NotImplementedError(
        "'QMqttConnection.writeSubscriptionProperties' has no cute function "
        "yet. Qt's 'QByteArray "
        "QMqttConnection::writeSubscriptionProperties(const "
        "QMqttSubscriptionProperties &properties)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'.")

  @staticmethod
  def writeUnsubscriptionProperties(*__, **_) -> Never:
    """
    Qt's 'QByteArray QMqttConnection::writeUnsubscriptionProperties(const
    QMqttUnsubscriptionProperties &properties)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'lcMqttConnectionVerbose'.
    """
    raise NotImplementedError(
        "'QMqttConnection.writeUnsubscriptionProperties' has no cute "
        "function yet. Qt's 'QByteArray "
        "QMqttConnection::writeUnsubscriptionProperties(const "
        "QMqttUnsubscriptionProperties &properties)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'lcMqttConnectionVerbose'.")
