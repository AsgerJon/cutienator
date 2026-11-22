"""
QTouchEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QList
from . import QEventPoint, QPointerEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTouchEvent(QPointerEvent):
  """
  The cute side of Qt's QTouchEvent: a plain Python object standing in front
  of one C++ QTouchEvent.

  It is built on the cute 'QPointerEvent', as Qt's QTouchEvent is built on
  Qt's QPointerEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTouchEvent that has a ritual and that Python can
  call so far, 7 names in all: 'clone', 'target', 'touchPointStates',
  'touchPoints', 'isBeginEvent', 'isUpdateEvent', 'isEndEvent'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTouchEvent::~QTouchEvent()': the destructor: Python never removes
    a C++ QTouchEvent.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 protected; 2 forbidden.

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

  def touchPoints(self) -> QList[QEventPoint]:
    """
    Calls Qt's 'const QList<QEventPoint> &QTouchEvent::touchPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#touchPoints

    Returns
    -------

    QList[QEventPoint]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QEventPoint> &QTouchEvent::touchPoints() const
    address = self.uglySide.call('ritual_ZNK11QTouchEvent11touchPointsEv')
    return QList[QEventPoint]._cuteOwning(address)

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

  @overload(
      QEvent.Type, QPointingDevice, Qt.KeyboardModifiers, QList[QEventPoint],
  )
  @overload(QEvent.Type, NoneType, Qt.KeyboardModifiers, QList[QEventPoint])
  def __init__(
      self,
      eventType: QEvent.Type,
      device: Optional[QPointingDevice],
      modifiers: Qt.KeyboardModifiers,
      touchPoints: QList[QEventPoint],
  ) -> None:
    """
    Notes what was given, for Qt's 'QTouchEvent::QTouchEvent(QEvent::Type
    eventType, const QPointingDevice *device, Qt::KeyboardModifiers
    modifiers, const QList<QEventPoint> &touchPoints)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#QTouchEvent

    Parameters
    ----------

    eventType : QEvent.Type
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    touchPoints : QList[QEventPoint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QTouchEvent::QTouchEvent(QEvent::Type eventType, const QPointingDevice
    #      *device, Qt::KeyboardModifiers modifiers, const QList<QEventPoint>
    #      &touchPoints)
    self._noteCreation(QTouchEvent, lambda: Rituals.call(
        'ritual_ZN11QTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6QFlagsI'
        'N2Qt16KeyboardModifierEERK5QListI11QEventPointE',
        eventType.value, self._addressOf(device), modifiers.value,
        self._valueOf(touchPoints),
    ))

  @overload(
      QEvent.Type, QPointingDevice, Qt.KeyboardModifiers, QEventPoint.States,
      QList[QEventPoint],
  )
  @overload(
      QEvent.Type, NoneType, Qt.KeyboardModifiers, QEventPoint.States,
      QList[QEventPoint],
  )
  def __init__(
      self,
      eventType: QEvent.Type,
      device: Optional[QPointingDevice],
      modifiers: Qt.KeyboardModifiers,
      touchPointStates: QEventPoint.States,
      touchPoints: QList[QEventPoint],
  ) -> None:
    """
    Notes what was given, for Qt's 'QTouchEvent::QTouchEvent(QEvent::Type
    eventType, const QPointingDevice *device, Qt::KeyboardModifiers
    modifiers, QEventPoint::States touchPointStates, const QList<QEventPoint>
    &touchPoints)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtouchevent.html#QTouchEvent

    Parameters
    ----------

    eventType : QEvent.Type
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    touchPointStates : QEventPoint.States
      Passed on as its number.

    touchPoints : QList[QEventPoint]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QTouchEvent::QTouchEvent(QEvent::Type eventType, const QPointingDevice
    #      *device, Qt::KeyboardModifiers modifiers, QEventPoint::States
    #      touchPointStates, const QList<QEventPoint> &touchPoints)
    self._noteCreation(QTouchEvent, lambda: Rituals.call(
        'ritual_ZN11QTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6QFlagsI'
        'N2Qt16KeyboardModifierEES5_IN11QEventPoint5StateEERK5QListIS9_E',
        eventType.value, self._addressOf(device), modifiers.value,
        touchPointStates.value, self._valueOf(touchPoints),
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
