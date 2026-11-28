"""
QGraphicsSceneHelpEvent binding of the Qt C++
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
from ..QtCore import QEvent
from . import QGraphicsSceneEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']


class QGraphicsSceneHelpEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneHelpEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneHelpEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneHelpEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneHelpEvent that has a ritual and that
  Python can call so far, 4 names in all: 'scenePos', 'setScenePos',
  'screenPos', 'setScreenPos'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneHelpEvent::~QGraphicsSceneHelpEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneHelpEvent.
  - Qt's 'QGraphicsSceneHelpEventPrivate *QGraphicsSceneHelpEvent::d_func()':
    gives 'QGraphicsSceneHelpEventPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsSceneHelpEventPrivate
    *QGraphicsSceneHelpEvent::d_func() const': gives
    'QGraphicsSceneHelpEventPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneHelpEvent is created at the first use, not by
    'QGraphicsSceneHelpEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneHelpEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneHelpEvent'

  #  A C++ QGraphicsSceneHelpEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneHelpEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneHelpEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneHelpEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsSceneHelpEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneHelpEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneHelpEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK23QGraphicsSceneHelpEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHelpEvent::setScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneHelpEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSceneHelpEvent11setScenePosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHelpEvent::setScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneHelpEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN23QGraphicsSceneHelpEvent12setScreenPosERK6QPoint',
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
  @overload(QEvent.Type)
  def __init__(self, type: QEvent.Type = QEvent.Type.NULL) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsSceneHelpEvent::QGraphicsSceneHelpEvent(Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehelpevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneHelpEvent::QGraphicsSceneHelpEvent(Type type)
    self._noteCreation(QGraphicsSceneHelpEvent, lambda: Rituals.call(
        'ritual_ZN23QGraphicsSceneHelpEventC1EN6QEvent4TypeE', type.value,
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
