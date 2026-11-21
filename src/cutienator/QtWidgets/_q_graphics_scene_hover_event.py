"""
QGraphicsSceneHoverEvent binding of the Qt C++
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


class QGraphicsSceneHoverEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneHoverEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneHoverEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneHoverEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneHoverEvent that has a ritual and that
  Python can call so far, 14 names in all: 'pos', 'setPos', 'scenePos',
  'setScenePos', 'screenPos', 'setScreenPos', 'lastPos', 'setLastPos',
  'lastScenePos', 'setLastScenePos', 'lastScreenPos', 'setLastScreenPos',
  'modifiers', 'setModifiers'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneHoverEvent::~QGraphicsSceneHoverEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneHoverEvent.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 private; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneHoverEvent is created at the first use, not by
    'QGraphicsSceneHoverEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneHoverEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneHoverEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneHoverEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneHoverEvent::pos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneHoverEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneHoverEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneHoverEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneHoverEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def lastPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneHoverEvent::lastPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneHoverEvent::lastPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent7lastPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneHoverEvent::lastScenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneHoverEvent::lastScenePos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent12lastScenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScreenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneHoverEvent::lastScreenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#lastScreenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneHoverEvent::lastScreenPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent13lastScreenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QGraphicsSceneHoverEvent::modifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGraphicsSceneHoverEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneHoverEvent9modifiersEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent6setPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent11setScenePosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent12setScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setLastPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setLastPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setLastPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setLastPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent10setLastPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setLastScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setLastScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setLastScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setLastScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent15setLastScenePosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def setLastScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneHoverEvent::setLastScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setLastScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneHoverEvent::setLastScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent16setLastScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneHoverEvent::setModifiers(Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QGraphicsSceneHoverEvent::setModifiers(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneHoverEvent12setModifiersE6QFlagsIN2Qt16Ke'
        'yboardModifierEE',
        modifiers.value,
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
    'QGraphicsSceneHoverEvent::QGraphicsSceneHoverEvent(Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenehoverevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneHoverEvent::QGraphicsSceneHoverEvent(Type type)
    self._noteCreation(QGraphicsSceneHoverEvent, lambda: Rituals.call(
        'ritual_ZN24QGraphicsSceneHoverEventC1EN6QEvent4TypeE', type.value,
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
