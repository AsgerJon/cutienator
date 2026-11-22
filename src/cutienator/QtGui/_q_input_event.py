"""
QInputEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QInputDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QInputEvent(QEvent):
  """
  The cute side of Qt's QInputEvent: a plain Python object standing in front
  of one C++ QInputEvent.

  It is built on the cute 'QEvent', as Qt's QInputEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputEvent that has a ritual and that Python can
  call so far, 7 names in all: 'clone', 'device', 'deviceType', 'modifiers',
  'setModifiers', 'timestamp', 'setTimestamp'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputEvent::~QInputEvent()': the destructor: Python never removes
    a C++ QInputEvent.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 4 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QInputEvent is created at the first use, not by
    'QInputEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputEvent'

  #  A C++ QInputEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QInputEvent'

  #  The functions Qt calls itself that QInputEvent is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setTimestamp': (
          ('_ZN11QInputEvent12setTimestampEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QInputEvent]:
    """
    Calls Qt's 'QInputEvent *QInputEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#clone

    Returns
    -------

    Optional[QInputEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputEvent *QInputEvent::clone() const
    ritual = 'ritual_ZNK11QInputEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QInputEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QInputEvent._cuteAt(address)

  def device(self) -> Optional[QInputDevice]:
    """
    Calls Qt's 'const QInputDevice *QInputEvent::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#device

    Returns
    -------

    Optional[QInputDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QInputDevice *QInputEvent::device() const
    address = self.uglySide.call('ritual_ZNK11QInputEvent6deviceEv')
    return QInputDevice._cuteAt(address)

  def deviceType(self) -> QInputDevice.DeviceType:
    """
    Calls Qt's 'QInputDevice::DeviceType QInputEvent::deviceType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#deviceType

    Returns
    -------

    QInputDevice.DeviceType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QInputDevice.DeviceType(number)' gives.
    """
    #  QInputDevice::DeviceType QInputEvent::deviceType() const
    return QInputDevice.DeviceType(self.uglySide.call(
        'ritual_ZNK11QInputEvent10deviceTypeEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QInputEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QInputEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK11QInputEvent9modifiersEv',
    ))

  def timestamp(self) -> int:
    """
    Calls Qt's 'quint64 QInputEvent::timestamp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#timestamp
    """
    #  quint64 QInputEvent::timestamp() const
    return self.uglySide.call('ritual_ZNK11QInputEvent9timestampEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void QInputEvent::setModifiers(Qt::KeyboardModifiers
    modifiers)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QInputEvent::setModifiers(Qt::KeyboardModifiers modifiers)
    self.uglySide.call(
        'ritual_ZN11QInputEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifie'
        'rEE',
        modifiers.value,
    )

  @overload(int)
  def setTimestamp(self, timestamp: int) -> None:
    """
    Calls Qt's 'void QInputEvent::setTimestamp(quint64 timestamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#setTimestamp

    Parameters
    ----------

    timestamp : int
      Passed on as it is.
    """
    #  void QInputEvent::setTimestamp(quint64 timestamp)
    ritual = 'ritual_ZN11QInputEvent12setTimestampEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QInputEvent12setTimestampEy'
    self.uglySide.call(ritual, timestamp)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QEvent.Type, QInputDevice)
  @overload(QEvent.Type, NoneType)
  @overload(QEvent.Type, QInputDevice, Qt.KeyboardModifiers)
  @overload(QEvent.Type, NoneType, Qt.KeyboardModifiers)
  def __init__(
      self,
      type: QEvent.Type,
      m_dev: Optional[QInputDevice],
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
  ) -> None:
    """
    Notes what was given, for Qt's 'QInputEvent::QInputEvent(Type type, const
    QInputDevice *m_dev, Qt::KeyboardModifiers modifiers)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qinputevent.html#QInputEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    m_dev : Optional[QInputDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.
    """
    #  QInputEvent::QInputEvent(Type type, const QInputDevice *m_dev,
    #      Qt::KeyboardModifiers modifiers)
    self._noteCreation(QInputEvent, lambda: Rituals.call(
        'ritual_ZN11QInputEventC1EN6QEvent4TypeEPK12QInputDevice6QFlagsIN2Q'
        't16KeyboardModifierEE',
        type.value, self._addressOf(m_dev), modifiers.value,
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
