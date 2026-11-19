"""
QWheelEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import Qt
from ..QtCore import QPoint
from ._q_single_point_event import QSinglePointEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QWheelEvent(QSinglePointEvent):
  """
  The cute side of Qt's QWheelEvent: a plain Python object standing in front
  of one C++ QWheelEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QWheelEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWheelEvent that has a ritual and that Python can
  call so far, 11 names in all: 'clone', 'pixelDelta', 'angleDelta', 'phase',
  'inverted', 'isInverted', 'hasPixelDelta', 'isBeginEvent', 'isUpdateEvent',
  'isEndEvent', 'source'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWheelEvent::~QWheelEvent()': the destructor: Python never removes
    a C++ QWheelEvent.
  - Qt's 'QWheelEvent::QWheelEvent(const QPointF &pos, const QPointF
    &globalPos, QPoint pixelDelta, QPoint angleDelta, Qt::MouseButtons
    buttons, Qt::KeyboardModifiers modifiers, Qt::ScrollPhase phase, bool
    inverted, Qt::MouseEventSource source, const QPointingDevice *device)':
    names 'QPointingDevice', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 20 functions Qt declares: 2 protected; 2 forbidden; 1 declared and
  nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QWheelEvent is created at the first use, not by
    'QWheelEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWheelEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWheelEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QWheelEvent]:
    """
    Calls Qt's 'QWheelEvent *QWheelEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#clone

    Returns
    -------

    Optional[QWheelEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWheelEvent *QWheelEvent::clone() const
    address = self.uglySide.call('ritual_ZNK11QWheelEvent5cloneEv')
    return QWheelEvent._cuteAt(address)

  def pixelDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWheelEvent::pixelDelta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#pixelDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWheelEvent::pixelDelta() const
    address = self.uglySide.call('ritual_ZNK11QWheelEvent10pixelDeltaEv')
    return QPoint._cuteOwning(address)

  def angleDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWheelEvent::angleDelta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#angleDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWheelEvent::angleDelta() const
    address = self.uglySide.call('ritual_ZNK11QWheelEvent10angleDeltaEv')
    return QPoint._cuteOwning(address)

  def phase(self) -> Qt.ScrollPhase:
    """
    Calls Qt's 'Qt::ScrollPhase QWheelEvent::phase() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#phase

    Returns
    -------

    Qt.ScrollPhase
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ScrollPhase(number)'
      gives.
    """
    #  Qt::ScrollPhase QWheelEvent::phase() const
    return Qt.ScrollPhase(self.uglySide.call(
        'ritual_ZNK11QWheelEvent5phaseEv',
    ))

  def inverted(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::inverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#inverted
    """
    #  bool QWheelEvent::inverted() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent8invertedEv')

  def isInverted(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::isInverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#isInverted
    """
    #  bool QWheelEvent::isInverted() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent10isInvertedEv')

  def hasPixelDelta(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::hasPixelDelta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#hasPixelDelta
    """
    #  bool QWheelEvent::hasPixelDelta() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent13hasPixelDeltaEv')

  def isBeginEvent(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::isBeginEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#isBeginEvent
    """
    #  bool QWheelEvent::isBeginEvent() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent12isBeginEventEv')

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::isUpdateEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#isUpdateEvent
    """
    #  bool QWheelEvent::isUpdateEvent() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent13isUpdateEventEv')

  def isEndEvent(self) -> bool:
    """
    Calls Qt's 'bool QWheelEvent::isEndEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#isEndEvent
    """
    #  bool QWheelEvent::isEndEvent() const
    return self.uglySide.call('ritual_ZNK11QWheelEvent10isEndEventEv')

  def source(self) -> Qt.MouseEventSource:
    """
    Calls Qt's 'Qt::MouseEventSource QWheelEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwheelevent.html#source

    Returns
    -------

    Qt.MouseEventSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MouseEventSource(number)' gives.
    """
    #  Qt::MouseEventSource QWheelEvent::source() const
    return Qt.MouseEventSource(self.uglySide.call(
        'ritual_ZNK11QWheelEvent6sourceEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
