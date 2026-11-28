"""
QModbusCommEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbuscommevent_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QModbusCommEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QModbusCommEvent(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QModbusCommEvent: a plain Python object standing in
  front of one C++ QModbusCommEvent.

  C++ hands a QModbusCommEvent around as a copy, so every C++
  QModbusCommEvent behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModbusCommEvent that has a ritual and that Python
  can call so far, 1 name in all: '__ior__'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'quint8 QModbusCommEvent::operator unsigned char() const': an
    operator Python has no name for.
  - Qt's 'QModbusCommEvent::EventByte QModbusCommEvent::operator
    QModbusCommEvent::EventByte() const': an operator Python has no name for.
  - Qt's 'QModbusCommEvent
    &QModbusCommEvent::operator=(QModbusCommEvent::EventByte byte)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QModbusCommEvent::~QModbusCommEvent()': the destructor: Python
    removes its C++ QModbusCommEvent by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QModbusCommEvent is created at the first use, not by
    'QModbusCommEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusCommEvent back gives a copy the ritual made
    for Python, in a new cute QModbusCommEvent.
  """

  #  The enums Qt writes inside QModbusCommEvent, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class EventByte(CuteNum):
    """
    The enum 'QModbusCommEvent::EventByte' of Qt, with the 4 names Qt gives
    in it.
    """

    SentEvent = Kee[int](64)
    ReceiveEvent = Kee[int](128)
    EnteredListenOnlyMode = Kee[int](4)
    InitiatedCommunicationRestart = Kee[int](0)

  class ReceiveFlag(CuteNum, scoped=True):
    """
    The enum 'QModbusCommEvent::ReceiveFlag' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    CommunicationError = Kee[int](2)
    CharacterOverrun = Kee[int](16)
    CurrentlyInListenOnlyMode = Kee[int](32)
    BroadcastReceived = Kee[int](64)

  class SendFlag(CuteNum, scoped=True):
    """
    The enum 'QModbusCommEvent::SendFlag' of Qt, with the 6 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    ReadExceptionSent = Kee[int](1)
    ServerAbortExceptionSent = Kee[int](2)
    ServerBusyExceptionSent = Kee[int](4)
    ServerProgramNAKExceptionSent = Kee[int](8)
    WriteTimeoutErrorOccurred = Kee[int](16)
    CurrentlyInListenOnlyMode = Kee[int](32)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusCommEvent'

  #  Qt's '~QModbusCommEvent()'. Naming it makes this a value class: Python
  #  owns every C++ QModbusCommEvent behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QModbusCommEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SendFlag)
  def __ior__(self, sf: SendFlag) -> QModbusCommEvent:
    """
    Calls Qt's 'QModbusCommEvent
    &QModbusCommEvent::operator|=(QModbusCommEvent::SendFlag sf)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuscommevent.html#operator|=

    Parameters
    ----------

    sf : SendFlag
      Passed on as its number.
    """
    #  QModbusCommEvent
    #      &QModbusCommEvent::operator|=(QModbusCommEvent::SendFlag sf)
    self.uglySide.call(
        'ritual_ZN16QModbusCommEventoRENS_8SendFlagE', sf.value,
    )
    return self

  @overload(ReceiveFlag)
  def __ior__(self, rf: ReceiveFlag) -> QModbusCommEvent:
    """
    Calls Qt's 'QModbusCommEvent
    &QModbusCommEvent::operator|=(QModbusCommEvent::ReceiveFlag rf)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbuscommevent.html#operator|=

    Parameters
    ----------

    rf : ReceiveFlag
      Passed on as its number.
    """
    #  QModbusCommEvent
    #      &QModbusCommEvent::operator|=(QModbusCommEvent::ReceiveFlag rf)
    self.uglySide.call(
        'ritual_ZN16QModbusCommEventoRENS_11ReceiveFlagE', rf.value,
    )
    return self

  @overload.fallback
  def __ior__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(EventByte)
  def __init__(self, byte: EventByte) -> None:
    """
    Notes what was given, for Qt's
    'QModbusCommEvent::QModbusCommEvent(QModbusCommEvent::EventByte byte)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbuscommevent.html#QModbusCommEvent

    Parameters
    ----------

    byte : EventByte
      Passed on as its number.
    """
    #  QModbusCommEvent::QModbusCommEvent(QModbusCommEvent::EventByte byte)
    self._noteCreation(QModbusCommEvent, lambda: Rituals.call(
        'ritual_ZN16QModbusCommEventC1ENS_9EventByteE', byte.value,
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
