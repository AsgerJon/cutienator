"""
QGraphicsSceneMouseEvent binding of the Qt C++
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


class QGraphicsSceneMouseEvent(QGraphicsSceneEvent):
  """
  The cute side of Qt's QGraphicsSceneMouseEvent: a plain Python object
  standing in front of one C++ QGraphicsSceneMouseEvent.

  It is built on the cute 'QGraphicsSceneEvent', as Qt's
  QGraphicsSceneMouseEvent is built on Qt's QGraphicsSceneEvent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsSceneMouseEvent that has a ritual and that
  Python can call so far, 28 names in all: 'pos', 'setPos', 'scenePos',
  'setScenePos', 'screenPos', 'setScreenPos', 'buttonDownPos',
  'setButtonDownPos', 'buttonDownScenePos', 'setButtonDownScenePos',
  'buttonDownScreenPos', 'setButtonDownScreenPos', 'lastPos', 'setLastPos',
  'lastScenePos', 'setLastScenePos', 'lastScreenPos', 'setLastScreenPos',
  'buttons', 'setButtons', 'button', 'setButton', 'modifiers',
  'setModifiers', 'source', 'setSource', 'flags', 'setFlags'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsSceneMouseEvent::~QGraphicsSceneMouseEvent()': the
    destructor: Python never removes a C++ QGraphicsSceneMouseEvent.
  - Qt's 'QGraphicsSceneMouseEventPrivate
    *QGraphicsSceneMouseEvent::d_func()': gives
    'QGraphicsSceneMouseEventPrivate', which has no cute class yet.
  - Qt's 'const QGraphicsSceneMouseEventPrivate
    *QGraphicsSceneMouseEvent::d_func() const': gives
    'QGraphicsSceneMouseEventPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QGraphicsSceneMouseEvent is created at the first use, not by
    'QGraphicsSceneMouseEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsSceneMouseEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsSceneMouseEvent'

  #  A C++ QGraphicsSceneMouseEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsSceneMouseEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMouseEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#pos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::pos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent3posEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def scenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMouseEvent::scenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#scenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::scenePos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent8scenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneMouseEvent::screenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#screenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneMouseEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent9screenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(Qt.MouseButton)
  def buttonDownPos(self, button: Qt.MouseButton) -> QPointF:
    """
    Calls Qt's 'QPointF
    QGraphicsSceneMouseEvent::buttonDownPos(Qt::MouseButton button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#buttonDownPos

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::buttonDownPos(Qt::MouseButton
    #      button) const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent13buttonDownPosEN2Qt11MouseBut'
        'tonE',
        button.value,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.MouseButton)
  def buttonDownScenePos(self, button: Qt.MouseButton) -> QPointF:
    """
    Calls Qt's 'QPointF
    QGraphicsSceneMouseEvent::buttonDownScenePos(Qt::MouseButton button)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#buttonDownScenePos

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::buttonDownScenePos(Qt::MouseButton
    #      button) const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent18buttonDownScenePosEN2Qt11Mou'
        'seButtonE',
        button.value,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(Qt.MouseButton)
  def buttonDownScreenPos(self, button: Qt.MouseButton) -> QPoint:
    """
    Calls Qt's 'QPoint
    QGraphicsSceneMouseEvent::buttonDownScreenPos(Qt::MouseButton button)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#buttonDownScreenPos

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneMouseEvent::buttonDownScreenPos(Qt::MouseButton
    #      button) const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent19buttonDownScreenPosEN2Qt11Mo'
        'useButtonE',
        button.value,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def lastPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMouseEvent::lastPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#lastPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::lastPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent7lastPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScenePos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsSceneMouseEvent::lastScenePos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#lastScenePos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsSceneMouseEvent::lastScenePos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent12lastScenePosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def lastScreenPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QGraphicsSceneMouseEvent::lastScreenPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#lastScreenPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QGraphicsSceneMouseEvent::lastScreenPos() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent13lastScreenPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def buttons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QGraphicsSceneMouseEvent::buttons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#buttons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QGraphicsSceneMouseEvent::buttons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent7buttonsEv',
    ))

  def button(self) -> Qt.MouseButton:
    """
    Calls Qt's 'Qt::MouseButton QGraphicsSceneMouseEvent::button() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#button

    Returns
    -------

    Qt.MouseButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.MouseButton(number)'
      gives.
    """
    #  Qt::MouseButton QGraphicsSceneMouseEvent::button() const
    return Qt.MouseButton(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent6buttonEv',
    ))

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QGraphicsSceneMouseEvent::modifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QGraphicsSceneMouseEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent9modifiersEv',
    ))

  def source(self) -> Qt.MouseEventSource:
    """
    Calls Qt's 'Qt::MouseEventSource QGraphicsSceneMouseEvent::source()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#source

    Returns
    -------

    Qt.MouseEventSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MouseEventSource(number)' gives.
    """
    #  Qt::MouseEventSource QGraphicsSceneMouseEvent::source() const
    return Qt.MouseEventSource(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent6sourceEv',
    ))

  def flags(self) -> Qt.MouseEventFlags:
    """
    Calls Qt's 'Qt::MouseEventFlags QGraphicsSceneMouseEvent::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#flags

    Returns
    -------

    Qt.MouseEventFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseEventFlags QGraphicsSceneMouseEvent::flags() const
    return Qt.MouseEventFlags(self.uglySide.call(
        'ritual_ZNK24QGraphicsSceneMouseEvent5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent6setPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def setScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent11setScenePosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPoint)
  def setScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent12setScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.MouseButton, QPointF)
  def setButtonDownPos(self, button: Qt.MouseButton, pos: QPointF) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneMouseEvent::setButtonDownPos(Qt::MouseButton button, const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setButtonDownPos

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setButtonDownPos(Qt::MouseButton
    #      button, const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent16setButtonDownPosEN2Qt11MouseB'
        'uttonERK7QPointF',
        button.value, self._valueOf(pos, 'QPointF'),
    )

  @overload(Qt.MouseButton, QPointF)
  def setButtonDownScenePos(
      self,
      button: Qt.MouseButton,
      pos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneMouseEvent::setButtonDownScenePos(Qt::MouseButton button,
    const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setButtonDownScenePos(Qt::MouseButton
    #      button, const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent21setButtonDownScenePosEN2Qt11M'
        'ouseButtonERK7QPointF',
        button.value, self._valueOf(pos, 'QPointF'),
    )

  @overload(Qt.MouseButton, QPoint)
  def setButtonDownScreenPos(
      self,
      button: Qt.MouseButton,
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneMouseEvent::setButtonDownScreenPos(Qt::MouseButton button,
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setButtonDownScreenPos(Qt::MouseButton
    #      button, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent22setButtonDownScreenPosEN2Qt11'
        'MouseButtonERK6QPoint',
        button.value, self._valueOf(pos),
    )

  @overload(QPointF)
  def setLastPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setLastPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setLastPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setLastPos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent10setLastPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def setLastScenePos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setLastScenePos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setLastScenePos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setLastScenePos(const QPointF &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent15setLastScenePosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPoint)
  def setLastScreenPos(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setLastScreenPos(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setLastScreenPos

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsSceneMouseEvent::setLastScreenPos(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent16setLastScreenPosERK6QPoint',
        self._valueOf(pos),
    )

  @overload(Qt.MouseButtons)
  def setButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QGraphicsSceneMouseEvent::setButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent10setButtonsE6QFlagsIN2Qt11Mous'
        'eButtonEE',
        buttons.value,
    )

  @overload(Qt.MouseButton)
  def setButton(self, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setButton(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setButton

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QGraphicsSceneMouseEvent::setButton(Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent9setButtonEN2Qt11MouseButtonE',
        button.value,
    )

  @overload(Qt.KeyboardModifiers)
  def setModifiers(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QGraphicsSceneMouseEvent::setModifiers(Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setModifiers

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QGraphicsSceneMouseEvent::setModifiers(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent12setModifiersE6QFlagsIN2Qt16Ke'
        'yboardModifierEE',
        modifiers.value,
    )

  @overload(Qt.MouseEventSource)
  def setSource(self, source: Qt.MouseEventSource) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setSource(Qt::MouseEventSource
    source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setSource

    Parameters
    ----------

    source : Qt.MouseEventSource
      Passed on as its number.
    """
    #  void QGraphicsSceneMouseEvent::setSource(Qt::MouseEventSource source)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent9setSourceEN2Qt16MouseEventSour'
        'ceE',
        source.value,
    )

  @overload(Qt.MouseEventFlags)
  def setFlags(self, a0: Qt.MouseEventFlags) -> None:
    """
    Calls Qt's 'void QGraphicsSceneMouseEvent::setFlags(Qt::MouseEventFlags
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html#setFlags

    Parameters
    ----------

    a0 : Qt.MouseEventFlags
      Passed on as its number.
    """
    #  void QGraphicsSceneMouseEvent::setFlags(Qt::MouseEventFlags a0)
    self.uglySide.call(
        'ritual_ZN24QGraphicsSceneMouseEvent8setFlagsE6QFlagsIN2Qt14MouseEv'
        'entFlagEE',
        a0.value,
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
    'QGraphicsSceneMouseEvent::QGraphicsSceneMouseEvent(Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsscenemouseevent.html

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number. May be left out, as in Qt: it is then
      QEvent.Type.NULL.
    """
    #  QGraphicsSceneMouseEvent::QGraphicsSceneMouseEvent(Type type)
    self._noteCreation(QGraphicsSceneMouseEvent, lambda: Rituals.call(
        'ritual_ZN24QGraphicsSceneMouseEventC1EN6QEvent4TypeE', type.value,
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
