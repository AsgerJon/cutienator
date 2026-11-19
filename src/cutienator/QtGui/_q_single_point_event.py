"""
QSinglePointEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import Qt
from ..QtCore import QObject
from ..QtCore import QPointF
from ._q_pointer_event import QPointerEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSinglePointEvent(QPointerEvent):
  """
  The cute side of Qt's QSinglePointEvent: a plain Python object standing in
  front of one C++ QSinglePointEvent.

  It is built on the cute 'QPointerEvent', as Qt's QSinglePointEvent is built
  on Qt's QPointerEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSinglePointEvent that has a ritual and that Python
  can call so far, 11 names in all: 'clone', 'button', 'buttons', 'position',
  'scenePosition', 'globalPosition', 'isBeginEvent', 'isUpdateEvent',
  'isEndEvent', 'exclusivePointGrabber', 'setExclusivePointGrabber'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSinglePointEvent::~QSinglePointEvent()': the destructor: Python
    never removes a C++ QSinglePointEvent.

  What has no ritual
  ------------------

  9 of the 21 functions Qt declares: 4 protected; 2 forbidden; 1 declared and
  nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QSinglePointEvent is created at the first use, not by
    'QSinglePointEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSinglePointEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSinglePointEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QSinglePointEvent]:
    """
    Calls Qt's 'QSinglePointEvent *QSinglePointEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#clone

    Returns
    -------

    Optional[QSinglePointEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSinglePointEvent *QSinglePointEvent::clone() const
    address = self.uglySide.call('ritual_ZNK17QSinglePointEvent5cloneEv')
    return QSinglePointEvent._cuteAt(address)

  def button(self) -> Qt.MouseButton:
    """
    Calls Qt's 'Qt::MouseButton QSinglePointEvent::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#button

    Returns
    -------

    Qt.MouseButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.MouseButton(number)'
      gives.
    """
    #  Qt::MouseButton QSinglePointEvent::button() const
    return Qt.MouseButton(self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent6buttonEv',
    ))

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QSinglePointEvent::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QSinglePointEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent7buttonsEv',
    ))

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::position() const
    address = self.uglySide.call('ritual_ZNK17QSinglePointEvent8positionEv')
    return QPointF._cuteOwning(address)

  def scenePosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::scenePosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#scenePosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::scenePosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent13scenePositionEv',
    )
    return QPointF._cuteOwning(address)

  def globalPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QSinglePointEvent::globalPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#globalPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QSinglePointEvent::globalPosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent14globalPositionEv',
    )
    return QPointF._cuteOwning(address)

  def isBeginEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isBeginEvent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#isBeginEvent
    """
    #  bool QSinglePointEvent::isBeginEvent() const
    return self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent12isBeginEventEv',
    )

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isUpdateEvent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#isUpdateEvent
    """
    #  bool QSinglePointEvent::isUpdateEvent() const
    return self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent13isUpdateEventEv',
    )

  def isEndEvent(self) -> bool:
    """
    Calls Qt's 'bool QSinglePointEvent::isEndEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsinglepointevent.html#isEndEvent
    """
    #  bool QSinglePointEvent::isEndEvent() const
    return self.uglySide.call('ritual_ZNK17QSinglePointEvent10isEndEventEv')

  def exclusivePointGrabber(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QSinglePointEvent::exclusivePointGrabber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#exclusivePointGrabber

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QSinglePointEvent::exclusivePointGrabber() const
    address = self.uglySide.call(
        'ritual_ZNK17QSinglePointEvent21exclusivePointGrabberEv',
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setExclusivePointGrabber(
      self,
      exclusiveGrabber: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QSinglePointEvent::setExclusivePointGrabber(QObject
    *exclusiveGrabber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsinglepointevent.html#setExclusivePointGrabber

    Parameters
    ----------

    exclusiveGrabber : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSinglePointEvent::setExclusivePointGrabber(QObject
    #      *exclusiveGrabber)
    self.uglySide.call(
        'ritual_ZN17QSinglePointEvent24setExclusivePointGrabberEP7QObject',
        self._addressOf(exclusiveGrabber),
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
