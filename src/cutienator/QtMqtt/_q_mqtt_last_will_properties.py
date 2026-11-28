"""
QMqttLastWillProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QMqtt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QMqttUserProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMqttUserProperties = WAIT['QMqttUserProperties']


class QMqttLastWillProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttLastWillProperties: a plain Python object
  standing in front of one C++ QMqttLastWillProperties.

  C++ hands a QMqttLastWillProperties around as a copy, so every C++
  QMqttLastWillProperties behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttLastWillProperties that has a ritual and that
  Python can call so far, 14 names in all: 'willDelayInterval',
  'payloadFormatIndicator', 'messageExpiryInterval', 'contentType',
  'responseTopic', 'correlationData', 'userProperties',
  'setWillDelayInterval', 'setPayloadFormatIndicator',
  'setMessageExpiryInterval', 'setContentType', 'setResponseTopic',
  'setCorrelationData', 'setUserProperties'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttLastWillProperties &QMqttLastWillProperties::operator=(const
    QMqttLastWillProperties &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QMqttLastWillProperties::~QMqttLastWillProperties()': the
    destructor: Python removes its C++ QMqttLastWillProperties by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QMqttLastWillProperties is created at the first use, not by
    'QMqttLastWillProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttLastWillProperties back gives a copy the ritual
    made for Python, in a new cute QMqttLastWillProperties.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttLastWillProperties'

  #  Qt's '~QMqttLastWillProperties()'. Naming it makes this a value class:
  #  Python owns every C++ QMqttLastWillProperties behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QMqttLastWillPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def willDelayInterval(self) -> int:
    """
    Calls Qt's 'quint32 QMqttLastWillProperties::willDelayInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#willDelayInterval
    """
    #  quint32 QMqttLastWillProperties::willDelayInterval() const
    return self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties17willDelayIntervalEv',
    )

  def payloadFormatIndicator(self) -> QMqtt.PayloadFormatIndicator:
    """
    Calls Qt's 'QMqtt::PayloadFormatIndicator
    QMqttLastWillProperties::payloadFormatIndicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html

    Returns
    -------

    QMqtt.PayloadFormatIndicator
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMqtt.PayloadFormatIndicator(number)' gives.
    """
    #  QMqtt::PayloadFormatIndicator
    #      QMqttLastWillProperties::payloadFormatIndicator() const
    return QMqtt.PayloadFormatIndicator(self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties22payloadFormatIndicatorEv',
    ))

  def messageExpiryInterval(self) -> int:
    """
    Calls Qt's 'quint32 QMqttLastWillProperties::messageExpiryInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#messageExpiryInterval
    """
    #  quint32 QMqttLastWillProperties::messageExpiryInterval() const
    return self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties21messageExpiryIntervalEv',
    )

  def contentType(self) -> str:
    """
    Calls Qt's 'QString QMqttLastWillProperties::contentType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#contentType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttLastWillProperties::contentType() const
    return self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties11contentTypeEv',
    )

  def responseTopic(self) -> str:
    """
    Calls Qt's 'QString QMqttLastWillProperties::responseTopic() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#responseTopic

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttLastWillProperties::responseTopic() const
    return self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties13responseTopicEv',
    )

  def correlationData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttLastWillProperties::correlationData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#correlationData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttLastWillProperties::correlationData() const
    address = self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties15correlationDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def userProperties(self) -> QMqttUserProperties:
    """
    Calls Qt's 'QMqttUserProperties QMqttLastWillProperties::userProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#userProperties

    Returns
    -------

    QMqttUserProperties
      A new cute QMqttUserProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttUserProperties QMqttLastWillProperties::userProperties() const
    address = self.uglySide.call(
        'ritual_ZNK23QMqttLastWillProperties14userPropertiesEv',
    )
    from . import QMqttUserProperties
    return QMqttUserProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWillDelayInterval(self, delay: int) -> None:
    """
    Calls Qt's 'void QMqttLastWillProperties::setWillDelayInterval(quint32
    delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#setWillDelayInterval

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QMqttLastWillProperties::setWillDelayInterval(quint32 delay)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties20setWillDelayIntervalEj', delay,
    )

  @overload(QMqtt.PayloadFormatIndicator)
  def setPayloadFormatIndicator(
      self,
      p: QMqtt.PayloadFormatIndicator,
  ) -> None:
    """
    Calls Qt's 'void
    QMqttLastWillProperties::setPayloadFormatIndicator(QMqtt::
    PayloadFormatIndicator p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html

    Parameters
    ----------

    p : QMqtt.PayloadFormatIndicator
      Passed on as its number.
    """
    #  void QMqttLastWillProperties::setPayloadFormatIndicator(QMqtt::
    #      PayloadFormatIndicator p)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties25setPayloadFormatIndicatorEN5QM'
        'qtt22PayloadFormatIndicatorE',
        p.value,
    )

  @overload(int)
  def setMessageExpiryInterval(self, expiry: int) -> None:
    """
    Calls Qt's 'void
    QMqttLastWillProperties::setMessageExpiryInterval(quint32 expiry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html

    Parameters
    ----------

    expiry : int
      Passed on as it is.
    """
    #  void QMqttLastWillProperties::setMessageExpiryInterval(quint32 expiry)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties24setMessageExpiryIntervalEj',
        expiry,
    )

  @overload(str)
  def setContentType(self, content: str) -> None:
    """
    Calls Qt's 'void QMqttLastWillProperties::setContentType(const QString
    &content)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#setContentType

    Parameters
    ----------

    content : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttLastWillProperties::setContentType(const QString &content)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties14setContentTypeERK7QString',
        content,
    )

  @overload(str)
  def setResponseTopic(self, response: str) -> None:
    """
    Calls Qt's 'void QMqttLastWillProperties::setResponseTopic(const QString
    &response)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#setResponseTopic

    Parameters
    ----------

    response : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttLastWillProperties::setResponseTopic(const QString
    #      &response)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties16setResponseTopicERK7QString',
        response,
    )

  @overload(QByteArray)
  def setCorrelationData(self, correlation: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttLastWillProperties::setCorrelationData(const
    QByteArray &correlation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#setCorrelationData

    Parameters
    ----------

    correlation : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttLastWillProperties::setCorrelationData(const QByteArray
    #      &correlation)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties18setCorrelationDataERK10QByteAr'
        'ray',
        self._valueOf(correlation),
    )

  @overload(QMqttUserProperties)
  def setUserProperties(self, properties: QMqttUserProperties) -> None:
    """
    Calls Qt's 'void QMqttLastWillProperties::setUserProperties(const
    QMqttUserProperties &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html#setUserProperties

    Parameters
    ----------

    properties : QMqttUserProperties
      Passed on as a value: Qt reads the C++ QMqttUserProperties, which stays
      Python's own.
    """
    #  void QMqttLastWillProperties::setUserProperties(const
    #      QMqttUserProperties &properties)
    self.uglySide.call(
        'ritual_ZN23QMqttLastWillProperties17setUserPropertiesERK19QMqttUse'
        'rProperties',
        self._valueOf(properties),
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
    'QMqttLastWillProperties::QMqttLastWillProperties()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html
    """
    #  QMqttLastWillProperties::QMqttLastWillProperties()
    self._noteCreation(QMqttLastWillProperties, lambda: Rituals.call(
        'ritual_ZN23QMqttLastWillPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttLastWillProperties) -> None:
    """
    Notes what was given, for Qt's
    'QMqttLastWillProperties::QMqttLastWillProperties(const
    QMqttLastWillProperties &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttlastwillproperties.html

    Parameters
    ----------

    a0 : QMqttLastWillProperties
      Passed on as a value: Qt reads the C++ QMqttLastWillProperties, which
      stays Python's own.
    """
    #  QMqttLastWillProperties::QMqttLastWillProperties(const
    #      QMqttLastWillProperties &a0)
    self._noteCreation(QMqttLastWillProperties, lambda: Rituals.call(
        'ritual_ZN23QMqttLastWillPropertiesC1ERKS_', self._valueOf(a0),
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
