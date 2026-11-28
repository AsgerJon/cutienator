"""
LegendMoveResizeHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/legendmoveresizehandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means LegendMoveResizeHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from . import QLegend
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QLegend = WAIT['QLegend']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LegendMoveResizeHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's LegendMoveResizeHandler: a plain Python object
  standing in front of one C++ LegendMoveResizeHandler.

  C++ hands a LegendMoveResizeHandler around as a copy, so every C++
  LegendMoveResizeHandler behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's LegendMoveResizeHandler that has a ritual and that
  Python can call so far, 10 names in all: 'shouldShowMoveHint', 'reset',
  'handleMousePressEvent', 'handleMouseMoveEvent', 'handleMouseReleaseEvent',
  'handleHoverEnterEvent', 'handleHoverMoveEvent', 'handleHoverLeaveEvent',
  'setMouseCursor', 'determineMousePosition'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'LegendMoveResizeHandler::~LegendMoveResizeHandler()': the
    destructor: Python removes its C++ LegendMoveResizeHandler by it, and has
    no other use for it.
  - Qt's 'void LegendMoveResizeHandler::setMouseCursor(MousePosition mpos)':
    names the enum 'LegendMoveResizeHandler::MousePosition', whose class
    cannot be named here.

  What to expect
  --------------

  - The C++ LegendMoveResizeHandler is created at the first use, not by
    'LegendMoveResizeHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a LegendMoveResizeHandler back gives a copy the ritual
    made for Python, in a new cute LegendMoveResizeHandler.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'LegendMoveResizeHandler'

  #  Qt's '~LegendMoveResizeHandler()'. Naming it makes this a value class:
  #  Python owns every C++ LegendMoveResizeHandler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23LegendMoveResizeHandlerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shouldShowMoveHint(self) -> bool:
    """
    Calls Qt's 'bool LegendMoveResizeHandler::shouldShowMoveHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#shouldShowMoveHint
    """
    #  bool LegendMoveResizeHandler::shouldShowMoveHint() const
    return self.uglySide.call(
        'ritual_ZNK23LegendMoveResizeHandler18shouldShowMoveHintEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setMouseCursor(self) -> None:
    """
    Calls Qt's 'void LegendMoveResizeHandler::setMouseCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#setMouseCursor
    """
    #  void LegendMoveResizeHandler::setMouseCursor()
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler14setMouseCursorEv',
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

  @overload(QLegend)
  @overload(NoneType)
  def __init__(self, legend: Optional[QLegend]) -> None:
    """
    Notes what was given, for Qt's
    'LegendMoveResizeHandler::LegendMoveResizeHandler(QLegend *legend)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html

    Parameters
    ----------

    legend : Optional[QLegend]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  LegendMoveResizeHandler::LegendMoveResizeHandler(QLegend *legend)
    self._noteCreation(LegendMoveResizeHandler, lambda: Rituals.call(
        'ritual_ZN23LegendMoveResizeHandlerC1EP7QLegend',
        self._addressOf(legend),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void LegendMoveResizeHandler::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/legendmoveresizehandler.html#reset
    """
    #  void LegendMoveResizeHandler::reset()
    self.uglySide.call('ritual_ZN23LegendMoveResizeHandler5resetEv')

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMoveResizeHandler::handleMousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#handleMousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleMousePressEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler21handleMousePressEventEP24QGrap'
        'hicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def handleMouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMoveResizeHandler::handleMouseMoveEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#handleMouseMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleMouseMoveEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler20handleMouseMoveEventEP24QGraph'
        'icsSceneMouseEvent',
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
    LegendMoveResizeHandler::handleMouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleMouseReleaseEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler23handleMouseReleaseEventEP24QGr'
        'aphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def handleHoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMoveResizeHandler::handleHoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#handleHoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleHoverEnterEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler21handleHoverEnterEventEP24QGrap'
        'hicsSceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def handleHoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMoveResizeHandler::handleHoverMoveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#handleHoverMoveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleHoverMoveEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler20handleHoverMoveEventEP24QGraph'
        'icsSceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def handleHoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void
    LegendMoveResizeHandler::handleHoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html#handleHoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void LegendMoveResizeHandler::handleHoverLeaveEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler21handleHoverLeaveEventEP24QGrap'
        'hicsSceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QPointF)
  def determineMousePosition(self, fromPoint: QPointF) -> None:
    """
    Calls Qt's 'void LegendMoveResizeHandler::determineMousePosition(QPointF
    fromPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/legendmoveresizehandler.html

    Parameters
    ----------

    fromPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void LegendMoveResizeHandler::determineMousePosition(QPointF
    #      fromPoint)
    self.uglySide.call(
        'ritual_ZN23LegendMoveResizeHandler22determineMousePositionE7QPoint'
        'F',
        self._valueOf(fromPoint, 'QPointF'),
    )
