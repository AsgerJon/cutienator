"""
QMouseEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import Qt
from ..QtCore import QEvent
from ..QtCore import QPoint
from ..QtCore import QPointF
from ._q_single_point_event import QSinglePointEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QMouseEvent(QSinglePointEvent):
  """
  The cute side of Qt's QMouseEvent: a plain Python object standing in front
  of one C++ QMouseEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QMouseEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMouseEvent that has a ritual and that Python can
  call so far, 12 names in all: 'clone', 'pos', 'globalPos', 'x', 'y',
  'globalX', 'globalY', 'localPos', 'windowPos', 'screenPos', 'source',
  'flags'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMouseEvent::~QMouseEvent()': the destructor: Python never removes
    a C++ QMouseEvent.
  - Qt's 'QMouseEvent::QMouseEvent(Type type, const QPointF &localPos,
    Qt::MouseButton button, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    modifiers, const QPointingDevice *device)': names 'QPointingDevice',
    which has no cute class yet.
  - Qt's 'QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    QPointF &globalPos, Qt::MouseButton button, Qt::MouseButtons buttons,
    Qt::KeyboardModifiers modifiers, const QPointingDevice *device)': names
    'QPointingDevice', which has no cute class yet.
  - Qt's 'QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, const
    QPointingDevice *device)': names 'QPointingDevice', which has no cute
    class yet.
  - Qt's 'QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    Qt::MouseEventSource source, const QPointingDevice *device)': names
    'QPointingDevice', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QMouseEvent is created at the first use, not by
    'QMouseEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMouseEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMouseEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QMouseEvent]:
    """
    Calls Qt's 'QMouseEvent *QMouseEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#clone

    Returns
    -------

    Optional[QMouseEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseEvent *QMouseEvent::clone() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent5cloneEv')
    return QMouseEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QMouseEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMouseEvent::pos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent3posEv')
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QMouseEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMouseEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9globalPosEv')
    return QPoint._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#x
    """
    #  int QMouseEvent::x() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#y
    """
    #  int QMouseEvent::y() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalX
    """
    #  int QMouseEvent::globalX() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalY
    """
    #  int QMouseEvent::globalY() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent7globalYEv')

  def localPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::localPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#localPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::localPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent8localPosEv')
    return QPointF._cuteOwning(address)

  def windowPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::windowPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#windowPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::windowPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9windowPosEv')
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::screenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#screenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::screenPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9screenPosEv')
    return QPointF._cuteOwning(address)

  def source(self) -> Qt.MouseEventSource:
    """
    Calls Qt's 'Qt::MouseEventSource QMouseEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#source

    Returns
    -------

    Qt.MouseEventSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MouseEventSource(number)' gives.
    """
    #  Qt::MouseEventSource QMouseEvent::source() const
    return Qt.MouseEventSource(self.uglySide.call(
        'ritual_ZNK11QMouseEvent6sourceEv',
    ))

  def flags(self) -> Qt.MouseEventFlags:
    """
    Calls Qt's 'Qt::MouseEventFlags QMouseEvent::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#flags

    Returns
    -------

    Qt.MouseEventFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseEventFlags QMouseEvent::flags() const
    return Qt.MouseEventFlags(self.uglySide.call(
        'ritual_ZNK11QMouseEvent5flagsEv',
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
