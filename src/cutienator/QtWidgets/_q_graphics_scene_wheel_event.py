"""
QGraphicsSceneWheelEvent binding of the Qt C++
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


class QGraphicsSceneWheelEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneWheelEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneWheelEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneWheelEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneWheelEvent that has a ritual and that
  Python can call so far, 20 names in all: 'pos', 'setPos', 'scenePos',
  'setScenePos', 'screenPos', 'setScreenPos', 'buttons', 'setButtons',
  'modifiers', 'setModifiers', 'delta', 'setDelta', 'orientation',
  'setOrientation', 'phase', 'setPhase', 'pixelDelta', 'setPixelDelta',
  'isInverted', 'setInverted'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneWheelEvent::~QGraphicsSceneWheelEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneWheelEvent.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneWheelEvent is created at the first use, not by
    'QGraphicsSceneWheelEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneWheelEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneWheelEvent'

  #  A C++ QGraphicsSceneWheelEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneWheelEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneWheelEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneWheelEvent::pos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneWheelEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneWheelEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneWheelEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneWheelEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent7buttonsEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent9modifiersEv',
    ))

  def delta(self) -> int:
    """
    Calls Qt's 'int QGraphicsSceneWheelEvent::delta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#delta
    """
    #  int QGraphicsSceneWheelEvent::delta() const
    return self.uglySide.call('ritual_ZNK24QGraphicsSceneWheelEvent5deltaEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QGraphicsSceneWheelEvent::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QGraphicsSceneWheelEvent::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent11orientationEv',
    ))

  def phase(self) -> Qt.ScrollPhase:
    """
    Calls Qt's 'Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#phase

    Returns
    -------

    Qt.ScrollPhase
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ScrollPhase(number)'
      gives.
    """
    #  Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const
    return Qt.ScrollPhase(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent5phaseEv',
    ))

  def pixelDelta(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneWheelEvent::pixelDelta() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#pixelDelta

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneWheelEvent::pixelDelta() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent10pixelDeltaEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def isInverted(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsSceneWheelEvent::isInverted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#isInverted
    """
    #  bool QGraphicsSceneWheelEvent::isInverted() const
    return self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneWheelEvent10isInvertedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneWheelEvent::setPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent6setPosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneWheelEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent11setScenePosERK7QPointF',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneWheelEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent12setScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.MouseButtons)
  def setButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphicsSceneWheelEvent::setButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent10setButtonsE6QFlagsIN2Qt11Mous'
        'eButtonEE',
        buttons.value,
    )

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneWheelEvent::setModifiers(Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QGraphicsSceneWheelEvent::setModifiers(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent12setModifiersE6QFlagsIN2Qt16Ke'
        'yboardModifierEE',
        modifiers.value,
    )

  @overload(int)
  def setDelta(self, delta: int) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setDelta(int delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setDelta

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QGraphicsSceneWheelEvent::setDelta(int delta)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent8setDeltaEi', delta,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsSceneWheelEvent::setOrientation(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent14setOrientationEN2Qt11Orientat'
        'ionE',
        orientation.value,
    )

  @overload(Qt.ScrollPhase)
  def setPhase(self, scrollPhase: Qt.ScrollPhase) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setPhase(Qt::ScrollPhase
    scrollPhase)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setPhase

    Parameters
    ----------

    scrollPhase : Qt.ScrollPhase
      Passed on as its number.
    """
    #  void QGraphicsSceneWheelEvent::setPhase(Qt::ScrollPhase scrollPhase)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent8setPhaseEN2Qt11ScrollPhaseE',
        scrollPhase.value,
    )

  @overload(QPoint)
  def setPixelDelta(self, delta: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setPixelDelta(QPoint delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setPixelDelta

    Parameters
    ----------

    delta : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneWheelEvent::setPixelDelta(QPoint delta)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent13setPixelDeltaE6QPoint',
        self._valueOf(delta),
    )

  @overload(bool)
  def setInverted(self, inverted: bool) -> None:
    """
    Calls Qt's 'void QGraphicsSceneWheelEvent::setInverted(bool inverted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html#setInverted

    Parameters
    ----------

    inverted : bool
      Passed on as it is.
    """
    #  void QGraphicsSceneWheelEvent::setInverted(bool inverted)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneWheelEvent11setInvertedEb', inverted,
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
    'QGraphicsSceneWheelEvent::QGraphicsSceneWheelEvent(Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenewheelevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneWheelEvent::QGraphicsSceneWheelEvent(Type type)
    self._noteCreation(QGraphicsSceneWheelEvent, lambda: Rituals.call(
        'ritual_ZN24QGraphicsSceneWheelEventC1EN6QEvent4TypeE', type.value,
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
