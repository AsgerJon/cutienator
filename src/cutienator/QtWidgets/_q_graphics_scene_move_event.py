"""
QGraphicsSceneMoveEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGraphicsSceneEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QGraphicsSceneMoveEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneMoveEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneMoveEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneMoveEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneMoveEvent that has a ritual and that
  Python can call so far, 4 names in all: 'oldPos', 'setOldPos', 'newPos',
  'setNewPos'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneMoveEvent::~QGraphicsSceneMoveEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneMoveEvent.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 private; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneMoveEvent is created at the first use, not by
    'QGraphicsSceneMoveEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneMoveEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneMoveEvent'

  #  A C++ QGraphicsSceneMoveEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneMoveEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def oldPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMoveEvent::oldPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemoveevent.html#oldPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMoveEvent::oldPos() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsSceneMoveEvent6oldPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def newPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMoveEvent::newPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemoveevent.html#newPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMoveEvent::newPos() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsSceneMoveEvent6newPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setOldPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMoveEvent::setOldPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemoveevent.html#setOldPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMoveEvent::setOldPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSceneMoveEvent9setOldPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setNewPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMoveEvent::setNewPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemoveevent.html#setNewPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMoveEvent::setNewPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSceneMoveEvent9setNewPosERK7QPointF',
        self._valueOf(pos),
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
    Notes what was given, for Qt's
    'QGraphicsSceneMoveEvent::QGraphicsSceneMoveEvent()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemoveevent.html
    """
    #  QGraphicsSceneMoveEvent::QGraphicsSceneMoveEvent()
    self._noteCreation(QGraphicsSceneMoveEvent, lambda: Rituals.call(
        'ritual_ZN23QGraphicsSceneMoveEventC1Ev',
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
