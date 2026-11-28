"""
QMqttSubscription binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttsubscription.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QMetaObject
  from . import QMqttClient, QMqttMessage, QMqttSubscriptionPrivate
  from . import QMqttTopicFilter, QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMqttClient = WAIT['QMqttClient']
  QMqttMessage = WAIT['QMqttMessage']
  QMqttTopicFilter = WAIT['QMqttTopicFilter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMqttSubscription(QObject):
  """
  The cute side of Qt's QMqttSubscription: a plain Python object standing in
  front of one C++ QMqttSubscription.

  It is built on the cute 'QObject', as Qt's QMqttSubscription is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMqttSubscription that has a ritual and that Python
  can call so far, 21 names in all: 'metaObject', 'tr', 'state', 'topic',
  'qos', 'reason', 'reasonCode', 'userProperties', 'isSharedSubscription',
  'sharedSubscriptionName', 'stateChanged', 'qosChanged', 'messageReceived',
  'unsubscribe', 'd_func', 'setState', 'setTopic', 'setClient', 'setQos',
  'setSharedSubscription', 'setSharedSubscriptionName'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMqttSubscription::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QMqttSubscription::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QMqttSubscription::~QMqttSubscription()': the destructor: Python
    never removes a C++ QMqttSubscription.
  - Qt's 'const QMqttSubscriptionPrivate *QMqttSubscription::d_func() const':
    takes in Python what 'QMqttSubscriptionPrivate
    *QMqttSubscription::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMqttSubscription is created at the first use, not by
    'QMqttSubscription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMqttSubscription.
  - Qt tells when it has removed the C++ QMqttSubscription. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QMqttSubscription, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SubscriptionState(CuteNum):
    """
    The enum 'QMqttSubscription::SubscriptionState' of Qt, with the 5 names
    Qt gives in it.
    """

    Unsubscribed = Kee[int](0)
    SubscriptionPending = Kee[int](1)
    Subscribed = Kee[int](2)
    UnsubscriptionPending = Kee[int](3)
    Error = Kee[int](4)

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
    Calls Qt's 'QString QMqttSubscription::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#tr

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
    #  QString QMqttSubscription::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QMqttSubscription2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttSubscription'

  #  A C++ QMqttSubscription Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMqttSubscription'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMqttSubscription::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMqttSubscription::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QMqttSubscription10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> SubscriptionState:
    """
    Calls Qt's 'SubscriptionState QMqttSubscription::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#state

    Returns
    -------

    SubscriptionState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SubscriptionState(number)' gives.
    """
    #  SubscriptionState QMqttSubscription::state() const
    return QMqttSubscription.SubscriptionState(self.uglySide.call(
        'ritual_ZNK17QMqttSubscription5stateEv',
    ))

  def topic(self) -> QMqttTopicFilter:
    """
    Calls Qt's 'QMqttTopicFilter QMqttSubscription::topic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#topic

    Returns
    -------

    QMqttTopicFilter
      A new cute QMqttTopicFilter around the copy Qt gave back. Python owns
      it.
    """
    #  QMqttTopicFilter QMqttSubscription::topic() const
    address = self.uglySide.call('ritual_ZNK17QMqttSubscription5topicEv')
    from . import QMqttTopicFilter
    return QMqttTopicFilter._cuteOwning(address)

  def qos(self) -> int:
    """
    Calls Qt's 'quint8 QMqttSubscription::qos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#qos
    """
    #  quint8 QMqttSubscription::qos() const
    return self.uglySide.call('ritual_ZNK17QMqttSubscription3qosEv')

  def reason(self) -> str:
    """
    Calls Qt's 'QString QMqttSubscription::reason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#reason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttSubscription::reason() const
    return self.uglySide.call('ritual_ZNK17QMqttSubscription6reasonEv')

  def reasonCode(self) -> QMqtt.ReasonCode:
    """
    Calls Qt's 'QMqtt::ReasonCode QMqttSubscription::reasonCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#reasonCode

    Returns
    -------

    QMqtt.ReasonCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QMqtt.ReasonCode(number)'
      gives.
    """
    #  QMqtt::ReasonCode QMqttSubscription::reasonCode() const
    return QMqtt.ReasonCode(self.uglySide.call(
        'ritual_ZNK17QMqttSubscription10reasonCodeEv',
    ))

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties QMqttSubscription::userProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttSubscription::userProperties() const
    address = self.uglySide.call(
        'ritual_ZNK17QMqttSubscription14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  def isSharedSubscription(self) -> bool:
    """
    Calls Qt's 'bool QMqttSubscription::isSharedSubscription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#isSharedSubscription
    """
    #  bool QMqttSubscription::isSharedSubscription() const
    return self.uglySide.call(
        'ritual_ZNK17QMqttSubscription20isSharedSubscriptionEv',
    )

  def sharedSubscriptionName(self) -> str:
    """
    Calls Qt's 'QString QMqttSubscription::sharedSubscriptionName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#sharedSubscriptionName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttSubscription::sharedSubscriptionName() const
    return self.uglySide.call(
        'ritual_ZNK17QMqttSubscription22sharedSubscriptionNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SubscriptionState)
  def setState(self, state: SubscriptionState) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setState(SubscriptionState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#setState

    Parameters
    ----------

    state : SubscriptionState
      Passed on as its number.
    """
    #  void QMqttSubscription::setState(SubscriptionState state)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription8setStateENS_17SubscriptionStateE',
        state.value,
    )

  @overload(QMqttTopicFilter)
  def setTopic(self, topic: QMqttTopicFilter) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setTopic(const QMqttTopicFilter
    &topic)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#setTopic

    Parameters
    ----------

    topic : QMqttTopicFilter
      Passed on as a value: Qt reads the C++ QMqttTopicFilter, which stays
      Python's own.
    """
    #  void QMqttSubscription::setTopic(const QMqttTopicFilter &topic)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription8setTopicERK16QMqttTopicFilter',
        self._valueOf(topic),
    )

  @overload(QMqttClient)
  @overload(NoneType)
  def setClient(self, client: Optional[QMqttClient]) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setClient(QMqttClient *client)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#setClient

    Parameters
    ----------

    client : Optional[QMqttClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMqttSubscription::setClient(QMqttClient *client)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription9setClientEP11QMqttClient',
        self._addressOf(client),
    )

  @overload(int)
  def setQos(self, qos: int) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setQos(quint8 qos)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#setQos

    Parameters
    ----------

    qos : int
      Passed on as it is.
    """
    #  void QMqttSubscription::setQos(quint8 qos)
    self.uglySide.call('ritual_ZN17QMqttSubscription6setQosEh', qos)

  @overload(bool)
  def setSharedSubscription(self, s: bool) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setSharedSubscription(bool s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#setSharedSubscription

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QMqttSubscription::setSharedSubscription(bool s)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription21setSharedSubscriptionEb', s,
    )

  @overload(str)
  def setSharedSubscriptionName(self, name: str) -> None:
    """
    Calls Qt's 'void QMqttSubscription::setSharedSubscriptionName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#setSharedSubscriptionName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttSubscription::setSharedSubscriptionName(const QString &name)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription25setSharedSubscriptionNameERK7QString',
        name,
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
    Notes what was given, for Qt's
    'QMqttSubscription::QMqttSubscription(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#QMqttSubscription

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMqttSubscription::QMqttSubscription(QObject *parent)
    self._noteCreation(QMqttSubscription, lambda: Rituals.call(
        'ritual_ZN17QMqttSubscriptionC1EP7QObject',
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

  @overload(SubscriptionState)
  def stateChanged(self, state: SubscriptionState) -> None:
    """
    Calls Qt's 'void QMqttSubscription::stateChanged(SubscriptionState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#stateChanged

    Parameters
    ----------

    state : SubscriptionState
      Passed on as its number.
    """
    #  void QMqttSubscription::stateChanged(SubscriptionState state)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription12stateChangedENS_17SubscriptionStateE',
        state.value,
    )

  @overload(int)
  def qosChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QMqttSubscription::qosChanged(quint8 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#qosChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QMqttSubscription::qosChanged(quint8 a0)
    self.uglySide.call('ritual_ZN17QMqttSubscription10qosChangedEh', a0)

  @overload(QMqttMessage)
  def messageReceived(self, msg: QMqttMessage) -> None:
    """
    Calls Qt's 'void QMqttSubscription::messageReceived(QMqttMessage msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttsubscription.html#messageReceived

    Parameters
    ----------

    msg : QMqttMessage
      Passed on as a value: Qt reads the C++ QMqttMessage, which stays
      Python's own.
    """
    #  void QMqttSubscription::messageReceived(QMqttMessage msg)
    self.uglySide.call(
        'ritual_ZN17QMqttSubscription15messageReceivedE12QMqttMessage',
        self._valueOf(msg),
    )

  def unsubscribe(self) -> None:
    """
    Calls Qt's 'void QMqttSubscription::unsubscribe()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#unsubscribe
    """
    #  void QMqttSubscription::unsubscribe()
    self.uglySide.call('ritual_ZN17QMqttSubscription11unsubscribeEv')

  def d_func(self) -> Optional[QMqttSubscriptionPrivate]:
    """
    Calls Qt's 'QMqttSubscriptionPrivate *QMqttSubscription::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttsubscription.html#d_func

    Returns
    -------

    Optional[QMqttSubscriptionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMqttSubscriptionPrivate *QMqttSubscription::d_func()
    address = self.uglySide.call('ritual_ZN17QMqttSubscription6d_funcEv')
    from . import QMqttSubscriptionPrivate
    return QMqttSubscriptionPrivate._cuteAt(address)
