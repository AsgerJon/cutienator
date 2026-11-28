"""
QMutableTouchEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qevent_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMutableTouchEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QList
from . import QTouchEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QEventPoint, QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEventPoint = WAIT['QEventPoint']
  QObject = WAIT['QObject']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMutableTouchEvent(QTouchEvent):
  """
  The cute side of Qt's QMutableTouchEvent: a plain Python object standing in
  front of one C++ QMutableTouchEvent.

  It is built on the cute 'QTouchEvent', as Qt's QMutableTouchEvent is built
  on Qt's QTouchEvent, and has everything that class has.

  C++ hands a QMutableTouchEvent around as a copy, so every C++
  QMutableTouchEvent behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMutableTouchEvent that has a ritual and that Python
  can call so far, 2 names in all: 'setTarget', 'addPoint'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMutableTouchEvent::~QMutableTouchEvent()': the destructor: Python
    removes its C++ QMutableTouchEvent by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QMutableTouchEvent is created at the first use, not by
    'QMutableTouchEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMutableTouchEvent back gives a copy the ritual made
    for Python, in a new cute QMutableTouchEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMutableTouchEvent'

  #  A C++ QMutableTouchEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMutableTouchEvent'

  #  Qt's '~QMutableTouchEvent()'. Naming it makes this a value class: Python
  #  owns every C++ QMutableTouchEvent behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QMutableTouchEventD1Ev'

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

  @overload(QObject)
  @overload(NoneType)
  def setTarget(self, target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMutableTouchEvent::setTarget(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutabletouchevent.html#setTarget

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMutableTouchEvent::setTarget(QObject *target)
    self.uglySide.call(
        'ritual_ZN18QMutableTouchEvent9setTargetEP7QObject',
        self._addressOf(target, 'QObject'),
    )

  @staticmethod
  @overload(QTouchEvent, QObject)
  @overload(QTouchEvent, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def setTarget(e: Optional[QTouchEvent], target: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QMutableTouchEvent::setTarget(QTouchEvent *e, QObject
    *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutabletouchevent.html#setTarget

    Parameters
    ----------

    e : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMutableTouchEvent::setTarget(QTouchEvent *e, QObject *target)
    Rituals.call(
        'ritual_ZN18QMutableTouchEvent9setTargetEP11QTouchEventP7QObject',
        CuteMixin._addressOf(e), CuteMixin._addressOf(target, 'QObject'),
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
    Notes what was given, for Qt's
    'QMutableTouchEvent::QMutableTouchEvent(QEvent::Type eventType, const
    QPointingDevice *device, Qt::KeyboardModifiers modifiers, const
    QList<QEventPoint> &touchPoints)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmutabletouchevent.html#QMutableTouchEvent

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
    #  QMutableTouchEvent::QMutableTouchEvent(QEvent::Type eventType, const
    #      QPointingDevice *device, Qt::KeyboardModifiers modifiers, const
    #      QList<QEventPoint> &touchPoints)
    self._noteCreation(QMutableTouchEvent, lambda: Rituals.call(
        'ritual_ZN18QMutableTouchEventC1EN6QEvent4TypeEPK15QPointingDevice6'
        'QFlagsIN2Qt16KeyboardModifierEERK5QListI11QEventPointE',
        eventType.value, self._addressOf(device), modifiers.value,
        self._valueOf(touchPoints),
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

  @overload(QEventPoint)
  def addPoint(self, point: QEventPoint) -> None:
    """
    Calls Qt's 'void QMutableTouchEvent::addPoint(const QEventPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutabletouchevent.html#addPoint

    Parameters
    ----------

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QMutableTouchEvent::addPoint(const QEventPoint &point)
    self.uglySide.call(
        'ritual_ZN18QMutableTouchEvent8addPointERK11QEventPoint',
        self._valueOf(point),
    )

  @staticmethod
  @overload(QTouchEvent, QEventPoint)
  @overload(NoneType, QEventPoint)
  def addPoint(e: Optional[QTouchEvent], point: QEventPoint) -> None:
    """
    Calls Qt's 'void QMutableTouchEvent::addPoint(QTouchEvent *e, const
    QEventPoint &point)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutabletouchevent.html#addPoint

    Parameters
    ----------

    e : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    point : QEventPoint
      Passed on as a value: Qt reads the C++ QEventPoint, which stays
      Python's own.
    """
    #  void QMutableTouchEvent::addPoint(QTouchEvent *e, const QEventPoint
    #      &point)
    Rituals.call(
        'ritual_ZN18QMutableTouchEvent8addPointEP11QTouchEventRK11QEventPoi'
        'nt',
        CuteMixin._addressOf(e), CuteMixin._valueOf(point),
    )
