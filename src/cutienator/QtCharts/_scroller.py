"""
Scroller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/scroller_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Scroller to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtWidgets import QGraphicsSceneMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Scroller(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Scroller: a plain Python object standing in front of
  one C++ Scroller.

  What exists
  -----------

  Every function of Qt's Scroller that has a ritual and that Python can call
  so far, 10 names in all: 'setOffset', 'offset', 'move', 'scrollTo',
  'handleMousePressEvent', 'handleMouseMoveEvent', 'handleMouseReleaseEvent',
  'scrollTick', 'startTicker', 'stopTicker'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Scroller::~Scroller()': the destructor: Python never removes a C++
    Scroller.
  - Qt's 'void Scroller::lowerSpeed(QPointF &speed, qreal maxSpeed)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ Scroller is created at the first use, not by 'Scroller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Scroller.
  - Each name of Qt's Scroller that has no cute function yet, 'lowerSpeed',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside Scroller, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """The enum 'Scroller::State' of Qt, with the 4 names Qt gives in it."""

    Idle = Kee[int](0)
    Pressed = Kee[int](1)
    Move = Kee[int](2)
    Scroll = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Scroller'

  #  A C++ Scroller Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Scroller'

  #  The functions Qt calls itself that Scroller is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setOffset': (
          ('_ZN8Scroller9setOffsetERK7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'offset': (
          ('_ZNK8Scroller6offsetEv',
           ('address', 'value', 'QtCore:QPointF'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF Scroller::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF Scroller::offset() const
    address = self._callAs('Scroller', 'ritual_ZNK8Scroller6offsetEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setOffset(self, point: QPointF) -> None:
    """
    Calls Qt's 'void Scroller::setOffset(const QPointF &point)'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#setOffset

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void Scroller::setOffset(const QPointF &point)
    self._callAs(
        'Scroller', 'ritual_ZN8Scroller9setOffsetERK7QPointF',
        self._valueOf(point, 'QPointF'),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Scroller::Scroller()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#Scroller
    """
    #  Scroller::Scroller()
    self._noteCreation(Scroller, lambda: Rituals.call(
        'ritual_ZN8ScrollerC1Ev',
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

  @overload(QPointF)
  def move(self, delta: QPointF) -> None:
    """
    Calls Qt's 'void Scroller::move(const QPointF &delta)'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#move

    Parameters
    ----------

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void Scroller::move(const QPointF &delta)
    self._callAs(
        'Scroller', 'ritual_ZN8Scroller4moveERK7QPointF',
        self._valueOf(delta, 'QPointF'),
    )

  @overload(QPointF)
  def scrollTo(self, delta: QPointF) -> None:
    """
    Calls Qt's 'void Scroller::scrollTo(const QPointF &delta)'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#scrollTo

    Parameters
    ----------

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void Scroller::scrollTo(const QPointF &delta)
    self._callAs(
        'Scroller', 'ritual_ZN8Scroller8scrollToERK7QPointF',
        self._valueOf(delta, 'QPointF'),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Scroller::handleMousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scroller.html#handleMousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scroller::handleMousePressEvent(QGraphicsSceneMouseEvent *event)
    self._callAs(
        'Scroller',
        'ritual_ZN8Scroller21handleMousePressEventEP24QGraphicsSceneMouseEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def handleMouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Scroller::handleMouseMoveEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#handleMouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scroller::handleMouseMoveEvent(QGraphicsSceneMouseEvent *event)
    self._callAs(
        'Scroller',
        'ritual_ZN8Scroller20handleMouseMoveEventEP24QGraphicsSceneMouseEve'
        'nt',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def handleMouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    Scroller::handleMouseReleaseEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/scroller.html#handleMouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Scroller::handleMouseReleaseEvent(QGraphicsSceneMouseEvent
    #      *event)
    self._callAs(
        'Scroller',
        'ritual_ZN8Scroller23handleMouseReleaseEventEP24QGraphicsSceneMouse'
        'Event',
        self._addressOf(event),
    )

  def scrollTick(self) -> None:
    """
    Calls Qt's 'void Scroller::scrollTick()'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#scrollTick
    """
    #  void Scroller::scrollTick()
    self._callAs('Scroller', 'ritual_ZN8Scroller10scrollTickEv')

  @overload(int)
  def startTicker(self, interval: int) -> None:
    """
    Calls Qt's 'void Scroller::startTicker(int interval)'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#startTicker

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void Scroller::startTicker(int interval)
    self._callAs('Scroller', 'ritual_ZN8Scroller11startTickerEi', interval)

  def stopTicker(self) -> None:
    """
    Calls Qt's 'void Scroller::stopTicker()'.

    Qt's own words: https://doc.qt.io/qt-6/scroller.html#stopTicker
    """
    #  void Scroller::stopTicker()
    self._callAs('Scroller', 'ritual_ZN8Scroller10stopTickerEv')

  @staticmethod
  def lowerSpeed(*__, **_) -> Never:
    """
    Qt's 'void Scroller::lowerSpeed(QPointF &speed, qreal maxSpeed)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Scroller.lowerSpeed' has no cute function yet. Qt's 'void "
        "Scroller::lowerSpeed(QPointF &speed, qreal maxSpeed)': takes a "
        "type Python has no way to hand over yet.")
