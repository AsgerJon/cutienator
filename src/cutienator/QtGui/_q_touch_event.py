"""
QTouchEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QEventPoint, QPointerEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject


class QTouchEvent(QPointerEvent):
  """
  The cute side of Qt's QTouchEvent: a plain Python object standing in front
  of one C++ QTouchEvent.

  It is built on the cute 'QPointerEvent', as Qt's QTouchEvent is built on
  Qt's QPointerEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTouchEvent that has a ritual and that Python can
  call so far, 6 names in all: 'clone', 'target', 'touchPointStates',
  'isBeginEvent', 'isUpdateEvent', 'isEndEvent'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTouchEvent::~QTouchEvent()': the destructor: Python never removes
    a C++ QTouchEvent.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QTouchEvent is created at the first use, not by
    'QTouchEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTouchEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTouchEvent'

  #  A C++ QTouchEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTouchEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QTouchEvent]:
    """
    Calls Qt's 'QTouchEvent *QTouchEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#clone

    Returns
    -------

    Optional[QTouchEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTouchEvent *QTouchEvent::clone() const
    ritual = 'ritual_ZNK11QTouchEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTouchEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QTouchEvent._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QTouchEvent::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QTouchEvent::target() const
    address = self.uglySide.call('ritual_ZNK11QTouchEvent6targetEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def touchPointStates(self) -> QEventPoint.States:
    """
    Calls Qt's 'QEventPoint::States QTouchEvent::touchPointStates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#touchPointStates

    Returns
    -------

    QEventPoint.States
      The value standing for the combination Qt gave back.
    """
    #  QEventPoint::States QTouchEvent::touchPointStates() const
    return QEventPoint.States(self.uglySide.call(
        'ritual_ZNK11QTouchEvent16touchPointStatesEv',
    ))

  def isBeginEvent(self) -> bool:
    """
    Calls Qt's 'bool QTouchEvent::isBeginEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#isBeginEvent
    """
    #  bool QTouchEvent::isBeginEvent() const
    ritual = 'ritual_ZNK11QTouchEvent12isBeginEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTouchEvent12isBeginEventEv'
    return self.uglySide.call(ritual)

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QTouchEvent::isUpdateEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#isUpdateEvent
    """
    #  bool QTouchEvent::isUpdateEvent() const
    ritual = 'ritual_ZNK11QTouchEvent13isUpdateEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTouchEvent13isUpdateEventEv'
    return self.uglySide.call(ritual)

  def isEndEvent(self) -> bool:
    """
    Calls Qt's 'bool QTouchEvent::isEndEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#isEndEvent
    """
    #  bool QTouchEvent::isEndEvent() const
    ritual = 'ritual_ZNK11QTouchEvent10isEndEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTouchEvent10isEndEventEv'
    return self.uglySide.call(ritual)

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
