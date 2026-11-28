"""
QMqttPublishProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttpublishproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QMqtt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from . import QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMqttUserProperties = WAIT['QMqttUserProperties']


class QMqttPublishProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttPublishProperties: a plain Python object
  standing in front of one C++ QMqttPublishProperties.

  C++ hands a QMqttPublishProperties around as a copy, so every C++
  QMqttPublishProperties behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttPublishProperties that has a ritual and that
  Python can call so far, 15 names in all: 'availableProperties',
  'payloadFormatIndicator', 'setPayloadFormatIndicator',
  'messageExpiryInterval', 'setMessageExpiryInterval', 'topicAlias',
  'setTopicAlias', 'responseTopic', 'setResponseTopic', 'correlationData',
  'setCorrelationData', 'userProperties', 'setUserProperties', 'contentType',
  'setContentType'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttPublishProperties &QMqttPublishProperties::operator=(const
    QMqttPublishProperties &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QMqttPublishProperties::~QMqttPublishProperties()': the destructor:
    Python removes its C++ QMqttPublishProperties by it, and has no other use
    for it.
  - Qt's 'QList<quint32> QMqttPublishProperties::subscriptionIdentifiers()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QMqttPublishProperties::setSubscriptionIdentifiers(const
    QList<quint32> &ids)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QMqttPublishProperties is created at the first use, not by
    'QMqttPublishProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttPublishProperties back gives a copy the ritual
    made for Python, in a new cute QMqttPublishProperties.
  - Each name of Qt's QMqttPublishProperties that has no cute function yet,
    'setSubscriptionIdentifiers', 'subscriptionIdentifiers', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMqttPublishProperties, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class PublishPropertyDetail(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QMqttPublishProperties::PublishPropertyDetail' of Qt,
    with the 9 names Qt gives in it. Qt names the type of its combinations
    'QMqttPublishProperties::PublishPropertyDetails'.
    """

    NULL = 0x0
    PayloadFormatIndicator = 0x1
    MessageExpiryInterval = 0x2
    TopicAlias = 0x4
    ResponseTopic = 0x8
    CorrelationData = 0x10
    UserProperty = 0x20
    SubscriptionIdentifier = 0x40
    ContentType = 0x80

  PublishPropertyDetails = PublishPropertyDetail

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttPublishProperties'

  #  Qt's '~QMqttPublishProperties()'. Naming it makes this a value class:
  #  Python owns every C++ QMqttPublishProperties behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QMqttPublishPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def availableProperties(self) -> PublishPropertyDetails:
    """
    Calls Qt's 'PublishPropertyDetails
    QMqttPublishProperties::availableProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#availableProperties

    Returns
    -------

    PublishPropertyDetails
      The value standing for the combination Qt gave back.
    """
    #  PublishPropertyDetails QMqttPublishProperties::availableProperties()
    #      const
    return QMqttPublishProperties.PublishPropertyDetails(self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties19availablePropertiesEv',
    ))

  def payloadFormatIndicator(self) -> QMqtt.PayloadFormatIndicator:
    """
    Calls Qt's 'QMqtt::PayloadFormatIndicator
    QMqttPublishProperties::payloadFormatIndicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#payloadFormatIndicator

    Returns
    -------

    QMqtt.PayloadFormatIndicator
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMqtt.PayloadFormatIndicator(number)' gives.
    """
    #  QMqtt::PayloadFormatIndicator
    #      QMqttPublishProperties::payloadFormatIndicator() const
    return QMqtt.PayloadFormatIndicator(self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties22payloadFormatIndicatorEv',
    ))

  def messageExpiryInterval(self) -> int:
    """
    Calls Qt's 'quint32 QMqttPublishProperties::messageExpiryInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#messageExpiryInterval
    """
    #  quint32 QMqttPublishProperties::messageExpiryInterval() const
    return self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties21messageExpiryIntervalEv',
    )

  def topicAlias(self) -> int:
    """
    Calls Qt's 'quint16 QMqttPublishProperties::topicAlias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#topicAlias
    """
    #  quint16 QMqttPublishProperties::topicAlias() const
    return self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties10topicAliasEv',
    )

  def responseTopic(self) -> str:
    """
    Calls Qt's 'QString QMqttPublishProperties::responseTopic() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#responseTopic

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttPublishProperties::responseTopic() const
    return self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties13responseTopicEv',
    )

  def correlationData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttPublishProperties::correlationData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#correlationData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttPublishProperties::correlationData() const
    address = self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties15correlationDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties QMqttPublishProperties::userProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttPublishProperties::userProperties() const
    address = self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  def contentType(self) -> str:
    """
    Calls Qt's 'QString QMqttPublishProperties::contentType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#contentType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttPublishProperties::contentType() const
    return self.uglySide.call(
        'ritual_ZNK22QMqttPublishProperties11contentTypeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMqtt.PayloadFormatIndicator)
  def setPayloadFormatIndicator(
      self,
      indicator: QMqtt.PayloadFormatIndicator,
  ) -> None:
    """
    Calls Qt's 'void
    QMqttPublishProperties::setPayloadFormatIndicator(QMqtt::
    PayloadFormatIndicator indicator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html

    Parameters
    ----------

    indicator : QMqtt.PayloadFormatIndicator
      Passed on as its number.
    """
    #  void QMqttPublishProperties::setPayloadFormatIndicator(QMqtt::
    #      PayloadFormatIndicator indicator)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties25setPayloadFormatIndicatorEN5QMq'
        'tt22PayloadFormatIndicatorE',
        indicator.value,
    )

  @overload(int)
  def setMessageExpiryInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setMessageExpiryInterval(quint32
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QMqttPublishProperties::setMessageExpiryInterval(quint32
    #      interval)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties24setMessageExpiryIntervalEj',
        interval,
    )

  @overload(int)
  def setTopicAlias(self, alias: int) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setTopicAlias(quint16 alias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#setTopicAlias

    Parameters
    ----------

    alias : int
      Passed on as it is.
    """
    #  void QMqttPublishProperties::setTopicAlias(quint16 alias)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties13setTopicAliasEt', alias,
    )

  @overload(str)
  def setResponseTopic(self, topic: str) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setResponseTopic(const QString
    &topic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#setResponseTopic

    Parameters
    ----------

    topic : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttPublishProperties::setResponseTopic(const QString &topic)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties16setResponseTopicERK7QString',
        topic,
    )

  @overload(QByteArray)
  def setCorrelationData(self, correlation: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setCorrelationData(const
    QByteArray &correlation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#setCorrelationData

    Parameters
    ----------

    correlation : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttPublishProperties::setCorrelationData(const QByteArray
    #      &correlation)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties18setCorrelationDataERK10QByteArr'
        'ay',
        self._valueOf(correlation),
    )

  @overload(QMqttUserProperties)
  def setUserProperties(self, properties: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setUserProperties(const
    QMqttUserProperties &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#setUserProperties

    Parameters
    ----------

    properties : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttPublishProperties::setUserProperties(const
    #      QMqttUserProperties &properties)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties17setUserPropertiesERK19QMqttUser'
        'Properties',
        self._valueOf(properties),
    )

  @overload(str)
  def setContentType(self, type: str) -> None:
    """
    Calls Qt's 'void QMqttPublishProperties::setContentType(const QString
    &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#setContentType

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttPublishProperties::setContentType(const QString &type)
    self.uglySide.call(
        'ritual_ZN22QMqttPublishProperties14setContentTypeERK7QString', type,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QMqttPublishProperties::QMqttPublishProperties()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#QMqttPublishProperties
    """
    #  QMqttPublishProperties::QMqttPublishProperties()
    self._noteCreation(QMqttPublishProperties, lambda: Rituals.call(
        'ritual_ZN22QMqttPublishPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttPublishProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttPublishProperties::QMqttPublishProperties(const
    QMqttPublishProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttpublishproperties.html#QMqttPublishProperties

    Parameters
    ----------

    a0 : QMqttPublishProperties
      Passed on as a value: Qt reads the C++ QMqttPublishProperties, which
      stays Python's own.
    """
    #  QMqttPublishProperties::QMqttPublishProperties(const
    #      QMqttPublishProperties &a0)
    self._noteCreation(QMqttPublishProperties, lambda: Rituals.call(
        'ritual_ZN22QMqttPublishPropertiesC1ERKS_', self._valueOf(a0),
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

  @staticmethod
  def setSubscriptionIdentifiers(*__, **_) -> Never:
    """
    Qt's 'void QMqttPublishProperties::setSubscriptionIdentifiers(const
    QList<quint32> &ids)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMqttPublishProperties.setSubscriptionIdentifiers' has no cute "
        "function yet. Qt's 'void "
        "QMqttPublishProperties::setSubscriptionIdentifiers(const "
        "QList<quint32> &ids)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def subscriptionIdentifiers(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QMqttPublishProperties::subscriptionIdentifiers()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMqttPublishProperties.subscriptionIdentifiers' has no cute "
        "function yet. Qt's 'QList<quint32> "
        "QMqttPublishProperties::subscriptionIdentifiers() const': gives a "
        "type Python has no way to take yet.")
