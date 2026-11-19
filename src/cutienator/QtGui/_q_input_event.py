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

from ..QtCore import Qt
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QInputEvent(QEvent):
  """
  The cute side of Qt's QInputEvent: a plain Python object standing in front
  of one C++ QInputEvent.

  It is built on the cute 'QEvent', as Qt's QInputEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputEvent that has a ritual and that Python can
  call so far, 5 names in all: 'clone', 'modifiers', 'setModifiers',
  'timestamp', 'setTimestamp'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputEvent::~QInputEvent()': the destructor: Python never removes
    a C++ QInputEvent.
  - Qt's 'QInputEvent::QInputEvent(Type type, const QInputDevice *m_dev,
    Qt::KeyboardModifiers modifiers)': names 'QInputDevice', which has no
    cute class yet.
  - Qt's 'const QInputDevice *QInputEvent::device() const': gives
    'QInputDevice', which has no cute class yet.
  - Qt's 'QInputDevice::DeviceType QInputEvent::deviceType() const': gives
    the enum 'QInputDevice::DeviceType', whose class cannot be named here.

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
    address = self.uglySide.call('ritual_ZNK11QInputEvent5cloneEv')
    return QInputEvent._cuteAt(address)

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
    self.uglySide.call('ritual_ZN11QInputEvent12setTimestampEy', timestamp)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
