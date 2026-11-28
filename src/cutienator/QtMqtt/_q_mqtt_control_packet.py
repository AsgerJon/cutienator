"""
QMqttControlPacket binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/6.12.0/QtMqtt/private/qmqttcontrolpacket_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMqttControlPacket to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QMqttControlPacket(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttControlPacket: a plain Python object standing in
  front of one C++ QMqttControlPacket.

  C++ hands a QMqttControlPacket around as a copy, so every C++
  QMqttControlPacket behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttControlPacket that has a ritual and that Python
  can call so far, 9 names in all: 'clear', 'setHeader', 'header', 'append',
  'appendRaw', 'appendRawVariableInteger', 'serialize', 'serializePayload',
  'payload'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMqttControlPacket::append(char value)': takes a single letter
    as C has it.
  - Qt's 'void QMqttControlPacket::append(quint32 value)': takes in Python
    what 'void QMqttControlPacket::append(quint16 value)' takes.
  - Qt's 'QMqttControlPacket::~QMqttControlPacket()': the destructor: Python
    removes its C++ QMqttControlPacket by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMqttControlPacket is created at the first use, not by
    'QMqttControlPacket(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttControlPacket back gives a copy the ritual made
    for Python, in a new cute QMqttControlPacket.
  """

  #  The enums Qt writes inside QMqttControlPacket, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PacketType(CuteNum):
    """
    The enum 'QMqttControlPacket::PacketType' of Qt, with the 16 names Qt
    gives in it.
    """

    UNKNOWN = Kee[int](0)
    CONNECT = Kee[int](16)
    CONNACK = Kee[int](32)
    PUBLISH = Kee[int](48)
    PUBACK = Kee[int](64)
    PUBREC = Kee[int](80)
    PUBREL = Kee[int](96)
    PUBCOMP = Kee[int](112)
    SUBSCRIBE = Kee[int](128)
    SUBACK = Kee[int](144)
    UNSUBSCRIBE = Kee[int](160)
    UNSUBACK = Kee[int](176)
    PINGREQ = Kee[int](192)
    PINGRESP = Kee[int](208)
    DISCONNECT = Kee[int](224)
    AUTH = Kee[int](240)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttControlPacket'

  #  Qt's '~QMqttControlPacket()'. Naming it makes this a value class: Python
  #  owns every C++ QMqttControlPacket behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMqttControlPacketD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def header(self) -> int:
    """
    Calls Qt's 'quint8 QMqttControlPacket::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#header
    """
    #  quint8 QMqttControlPacket::header() const
    return self.uglySide.call('ritual_ZNK18QMqttControlPacket6headerEv')

  def serialize(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttControlPacket::serialize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#serialize

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttControlPacket::serialize() const
    address = self.uglySide.call(
        'ritual_ZNK18QMqttControlPacket9serializeEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def serializePayload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttControlPacket::serializePayload() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttcontrolpacket.html#serializePayload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttControlPacket::serializePayload() const
    address = self.uglySide.call(
        'ritual_ZNK18QMqttControlPacket16serializePayloadEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QMqttControlPacket::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QMqttControlPacket::payload() const
    address = self.uglySide.call('ritual_ZNK18QMqttControlPacket7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setHeader(self, h: int) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::setHeader(quint8 h)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#setHeader

    Parameters
    ----------

    h : int
      Passed on as it is.
    """
    #  void QMqttControlPacket::setHeader(quint8 h)
    self.uglySide.call('ritual_ZN18QMqttControlPacket9setHeaderEh', h)

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
    'QMqttControlPacket::QMqttControlPacket()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttcontrolpacket.html#QMqttControlPacket
    """
    #  QMqttControlPacket::QMqttControlPacket()
    self._noteCreation(QMqttControlPacket, lambda: Rituals.call(
        'ritual_ZN18QMqttControlPacketC1Ev',
    ))

  @overload(int)
  def __init__(self, header: int) -> None:
    """
    Notes what was given, for Qt's
    'QMqttControlPacket::QMqttControlPacket(quint8 header)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttcontrolpacket.html#QMqttControlPacket

    Parameters
    ----------

    header : int
      Passed on as it is.
    """
    #  QMqttControlPacket::QMqttControlPacket(quint8 header)
    self._noteCreation(QMqttControlPacket, lambda: Rituals.call(
        'ritual_ZN18QMqttControlPacketC1Eh', header,
    ))

  @overload(int, QByteArray)
  def __init__(self, header: int, pay: QByteArray) -> None:
    """
    Notes what was given, for Qt's
    'QMqttControlPacket::QMqttControlPacket(quint8 header, const QByteArray
    &pay)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttcontrolpacket.html#QMqttControlPacket

    Parameters
    ----------

    header : int
      Passed on as it is.

    pay : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QMqttControlPacket::QMqttControlPacket(quint8 header, const QByteArray
    #      &pay)
    self._noteCreation(QMqttControlPacket, lambda: Rituals.call(
        'ritual_ZN18QMqttControlPacketC1EhRK10QByteArray',
        header, self._valueOf(pay),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#clear
    """
    #  void QMqttControlPacket::clear()
    self.uglySide.call('ritual_ZN18QMqttControlPacket5clearEv')

  @overload(int)
  def append(self, value: int) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::append(quint16 value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#append

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QMqttControlPacket::append(quint16 value)
    self.uglySide.call('ritual_ZN18QMqttControlPacket6appendEt', value)

  @overload(QByteArray)
  def append(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::append(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#append

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttControlPacket::append(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QMqttControlPacket6appendERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QByteArray)
  def appendRaw(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::appendRaw(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttcontrolpacket.html#appendRaw

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QMqttControlPacket::appendRaw(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN18QMqttControlPacket9appendRawERK10QByteArray',
        self._valueOf(data),
    )

  @overload(int)
  def appendRawVariableInteger(self, value: int) -> None:
    """
    Calls Qt's 'void QMqttControlPacket::appendRawVariableInteger(quint32
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttcontrolpacket.html#appendRawVariableInteger

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QMqttControlPacket::appendRawVariableInteger(quint32 value)
    self.uglySide.call(
        'ritual_ZN18QMqttControlPacket24appendRawVariableIntegerEj', value,
    )
