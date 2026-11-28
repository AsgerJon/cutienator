"""
QMqttMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqttmessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QMqttPublishProperties, QMqttTopicName
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMqttTopicName = WAIT['QMqttTopicName']


class QMqttMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttMessage: a plain Python object standing in front
  of one C++ QMqttMessage.

  C++ hands a QMqttMessage around as a copy, so every C++ QMqttMessage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttMessage that has a ritual and that Python can
  call so far, 9 names in all: '__eq__', '__ne__', 'payload', 'qos', 'id',
  'topic', 'duplicate', 'retain', 'publishProperties'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttMessage::~QMqttMessage()': the destructor: Python removes its
    C++ QMqttMessage by it, and has no other use for it.
  - Qt's 'QMqttMessage &QMqttMessage::operator=(const QMqttMessage &other)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  3 of the 17 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QMqttMessage is created at the first use, not by
    'QMqttMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttMessage back gives a copy the ritual made for
    Python, in a new cute QMqttMessage.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttMessage'

  #  Qt's '~QMqttMessage()'. Naming it makes this a value class: Python owns
  #  every C++ QMqttMessage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QMqttMessageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QMqttMessage::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QMqttMessage::payload() const
    address = self.uglySide.call('ritual_ZNK12QMqttMessage7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def qos(self) -> int:
    """
    Calls Qt's 'quint8 QMqttMessage::qos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#qos
    """
    #  quint8 QMqttMessage::qos() const
    return self.uglySide.call('ritual_ZNK12QMqttMessage3qosEv')

  def id(self) -> int:
    """
    Calls Qt's 'quint16 QMqttMessage::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#id
    """
    #  quint16 QMqttMessage::id() const
    return self.uglySide.call('ritual_ZNK12QMqttMessage2idEv')

  def topic(self) -> QMqttTopicName:
    """
    Calls Qt's 'QMqttTopicName QMqttMessage::topic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#topic

    Returns
    -------

    QMqttTopicName
      A new cute QMqttTopicName around the copy Qt gave back. Python owns it.
    """
    #  QMqttTopicName QMqttMessage::topic() const
    address = self.uglySide.call('ritual_ZNK12QMqttMessage5topicEv')
    from . import QMqttTopicName
    return QMqttTopicName._cuteOwning(address)

  def duplicate(self) -> bool:
    """
    Calls Qt's 'bool QMqttMessage::duplicate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#duplicate
    """
    #  bool QMqttMessage::duplicate() const
    return self.uglySide.call('ritual_ZNK12QMqttMessage9duplicateEv')

  def retain(self) -> bool:
    """
    Calls Qt's 'bool QMqttMessage::retain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#retain
    """
    #  bool QMqttMessage::retain() const
    return self.uglySide.call('ritual_ZNK12QMqttMessage6retainEv')

  def publishProperties(self) -> QMqttPublishProperties:
    """
    Calls Qt's 'QMqttPublishProperties QMqttMessage::publishProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttmessage.html#publishProperties

    Returns
    -------

    QMqttPublishProperties
      A new cute QMqttPublishProperties around the copy Qt gave back. Python
      owns it.
    """
    #  QMqttPublishProperties QMqttMessage::publishProperties() const
    address = self.uglySide.call(
        'ritual_ZNK12QMqttMessage17publishPropertiesEv',
    )
    from . import QMqttPublishProperties
    return QMqttPublishProperties._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QMqttMessage) -> bool:
    """
    Calls Qt's 'bool QMqttMessage::operator==(const QMqttMessage &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#operator==

    Parameters
    ----------

    other : QMqttMessage
      Passed on as a value: Qt reads the C++ QMqttMessage, which stays
      Python's own.
    """
    #  bool QMqttMessage::operator==(const QMqttMessage &other) const
    return self.uglySide.call(
        'ritual_ZNK12QMqttMessageeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QMqttMessage) -> bool:
    """
    Calls Qt's 'bool QMqttMessage::operator!=(const QMqttMessage &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#operator!=

    Parameters
    ----------

    other : QMqttMessage
      Passed on as a value: Qt reads the C++ QMqttMessage, which stays
      Python's own.
    """
    #  bool QMqttMessage::operator!=(const QMqttMessage &other) const
    return self.uglySide.call(
        'ritual_ZNK12QMqttMessageneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMqttMessage::QMqttMessage()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#QMqttMessage
    """
    #  QMqttMessage::QMqttMessage()
    self._noteCreation(QMqttMessage, lambda: Rituals.call(
        'ritual_ZN12QMqttMessageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QMqttMessage) -> None:
    """
    Notes what was given, for Qt's 'QMqttMessage::QMqttMessage(const
    QMqttMessage &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#QMqttMessage

    Parameters
    ----------

    other : QMqttMessage
      Passed on as a value: Qt reads the C++ QMqttMessage, which stays
      Python's own.
    """
    #  QMqttMessage::QMqttMessage(const QMqttMessage &other)
    self._noteCreation(QMqttMessage, lambda: Rituals.call(
        'ritual_ZN12QMqttMessageC1ERKS_', self._valueOf(other),
    ))

  @overload(QMqttTopicName, QByteArray, int, int, bool, bool)
  def __init__(
      self,
      topic: QMqttTopicName,
      payload: QByteArray,
      id: int,
      qos: int,
      dup: bool,
      retain: bool,
  ) -> None:
    """
    Notes what was given, for Qt's 'QMqttMessage::QMqttMessage(const
    QMqttTopicName &topic, const QByteArray &payload, quint16 id, quint8 qos,
    bool dup, bool retain)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmqttmessage.html#QMqttMessage

    Parameters
    ----------

    topic : QMqttTopicName
      Passed on as a value: Qt reads the C++ QMqttTopicName, which stays
      Python's own.

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    id : int
      Passed on as it is.

    qos : int
      Passed on as it is.

    dup : bool
      Passed on as it is.

    retain : bool
      Passed on as it is.
    """
    #  QMqttMessage::QMqttMessage(const QMqttTopicName &topic, const
    #      QByteArray &payload, quint16 id, quint8 qos, bool dup, bool
    #      retain)
    self._noteCreation(QMqttMessage, lambda: Rituals.call(
        'ritual_ZN12QMqttMessageC1ERK14QMqttTopicNameRK10QByteArraythbb',
        self._valueOf(topic), self._valueOf(payload), id, qos, dup, retain,
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
