"""
QGraphicsSceneContextMenuEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QGraphicsSceneEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']


class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneContextMenuEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneContextMenuEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneContextMenuEvent is built on Qt's QGraphicsSceneEvent, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneContextMenuEvent that has a ritual and
  that Python can call so far, 10 names in all: 'pos', 'setPos', 'scenePos',
  'setScenePos', 'screenPos', 'setScreenPos', 'modifiers', 'setModifiers',
  'reason', 'setReason'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneContextMenuEvent::~QGraphicsSceneContextMenuEvent()':
    the destructor: Python never removes a C++
    QGraphicsSceneContextMenuEvent.
  - Qt's 'QGraphicsSceneContextMenuEventPrivate
    *QGraphicsSceneContextMenuEvent::d_func()': gives
    'QGraphicsSceneContextMenuEventPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsSceneContextMenuEventPrivate
    *QGraphicsSceneContextMenuEvent::d_func() const': gives
    'QGraphicsSceneContextMenuEventPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneContextMenuEvent is created at the first use, not
    by 'QGraphicsSceneContextMenuEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneContextMenuEvent.
  """

  #  The enums Qt writes inside QGraphicsSceneContextMenuEvent, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Reason(CuteNum):
    """
    The enum 'QGraphicsSceneContextMenuEvent::Reason' of Qt, with the 3 names
    Qt gives in it.
    """

    Mouse = Kee[int](0)
    Keyboard = Kee[int](1)
    Other = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneContextMenuEvent'

  #  A C++ QGraphicsSceneContextMenuEvent Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneContextMenuEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneContextMenuEvent::pos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneContextMenuEvent::pos() const
    address = self.uglySide.call(
        'ritual_ZNK30QGraphicsSceneContextMenuEvent3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneContextMenuEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneContextMenuEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK30QGraphicsSceneContextMenuEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneContextMenuEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneContextMenuEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK30QGraphicsSceneContextMenuEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers
    QGraphicsSceneContextMenuEvent::modifiers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGraphicsSceneContextMenuEvent::modifiers()
    #      const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK30QGraphicsSceneContextMenuEvent9modifiersEv',
    ))

  def reason(self) -> Reason:
    """
    Calls Qt's 'Reason QGraphicsSceneContextMenuEvent::reason() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#reason

    Returns
    -------

    Reason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Reason(number)' gives.
    """
    #  Reason QGraphicsSceneContextMenuEvent::reason() const
    return QGraphicsSceneContextMenuEvent.Reason(self.uglySide.call(
        'ritual_ZNK30QGraphicsSceneContextMenuEvent6reasonEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneContextMenuEvent::setPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneContextMenuEvent::setPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN30QGraphicsSceneContextMenuEvent6setPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneContextMenuEvent::setScenePos(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneContextMenuEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN30QGraphicsSceneContextMenuEvent11setScenePosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneContextMenuEvent::setScreenPos(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneContextMenuEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN30QGraphicsSceneContextMenuEvent12setScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneContextMenuEvent::setModifiers(Qt::KeyboardModifiers
    modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void
    #      QGraphicsSceneContextMenuEvent::setModifiers(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN30QGraphicsSceneContextMenuEvent12setModifiersE6QFlagsIN2'
        'Qt16KeyboardModifierEE',
        modifiers.value,
    )

  @overload(Reason)
  def setReason(self, reason: Reason) -> None:
    """
    Calls Qt's 'void QGraphicsSceneContextMenuEvent::setReason(Reason
    reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html#setReason

    Parameters
    ----------

    reason : Reason
      Passed on as its number.
    """
    #  void QGraphicsSceneContextMenuEvent::setReason(Reason reason)
    self.uglySide.call(
        'ritual_ZN30QGraphicsSceneContextMenuEvent9setReasonENS_6ReasonE',
        reason.value,
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
    'QGraphicsSceneContextMenuEvent::QGraphicsSceneContextMenuEvent(Type
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenecontextmenuevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneContextMenuEvent::QGraphicsSceneContextMenuEvent(Type
    #      type)
    self._noteCreation(QGraphicsSceneContextMenuEvent, lambda: Rituals.call(
        'ritual_ZN30QGraphicsSceneContextMenuEventC1EN6QEvent4TypeE',
        type.value,
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
