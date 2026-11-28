"""
QQuickMouseArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmousearea_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickMouseArea to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QTimerEvent
  from ..QtGui import QHoverEvent, QMouseEvent, QWheelEvent
  from . import QQuickDrag, QQuickMouseAreaPrivate, QQuickMouseEvent
  from . import QQuickWheelEvent, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickMouseEvent = WAIT['QQuickMouseEvent']
  QQuickWheelEvent = WAIT['QQuickWheelEvent']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMouseArea(QQuickItem):
  """
  The cute side of Qt's QQuickMouseArea: a plain Python object standing in
  front of one C++ QQuickMouseArea.

  It is built on the cute 'QQuickItem', as Qt's QQuickMouseArea is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMouseArea that has a ritual and that Python
  can call so far, 70 names in all: 'metaObject', 'tr', 'mouseX', 'mouseY',
  'isEnabled', 'setEnabled', 'isScrollGestureEnabled',
  'setScrollGestureEnabled', 'hovered', 'isPressed', 'containsPress',
  'pressedButtons', 'acceptedButtons', 'setAcceptedButtons', 'hoverEnabled',
  'setHoverEnabled', 'drag', 'preventStealing', 'setPreventStealing',
  'propagateComposedEvents', 'setPropagateComposedEvents', 'cursorShape',
  'setCursorShape', 'pressAndHoldInterval', 'setPressAndHoldInterval',
  'resetPressAndHoldInterval', 'hoveredChanged', 'pressedChanged',
  'enabledChanged', 'scrollGestureEnabledChanged', 'pressedButtonsChanged',
  'acceptedButtonsChanged', 'hoverEnabledChanged', 'cursorShapeChanged',
  'positionChanged', 'mouseXChanged', 'mouseYChanged',
  'preventStealingChanged', 'propagateComposedEventsChanged', 'pressed',
  'pressAndHold', 'released', 'clicked', 'doubleClicked', 'wheel', 'entered',
  'exited', 'canceled', 'containsPressChanged',
  'pressAndHoldIntervalChanged', 'setHovered', 'setPressed',
  'sendMouseEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'mouseMoveEvent', 'mouseUngrabEvent',
  'touchUngrabEvent', 'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent',
  'wheelEvent', 'childMouseEventFilter', 'timerEvent', 'geometryChange',
  'itemChange', 'updatePaintNode', 'ungrabMouse', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMouseArea::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMouseArea::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMouseArea::~QQuickMouseArea()': the destructor: Python never
    removes a C++ QQuickMouseArea.
  - Qt's 'const QQuickMouseAreaPrivate *QQuickMouseArea::d_func() const':
    takes in Python what 'QQuickMouseAreaPrivate *QQuickMouseArea::d_func()'
    takes.

  What has no ritual
  ------------------

  6 of the 81 functions Qt declares: 4 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMouseArea is created at the first use, not by
    'QQuickMouseArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMouseArea.
  - Qt tells when it has removed the C++ QQuickMouseArea. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickMouseArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMouseArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickMouseArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMouseArea'

  #  A C++ QQuickMouseArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMouseArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMouseArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMouseArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickMouseArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mouseX(self) -> float:
    """
    Calls Qt's 'qreal QQuickMouseArea::mouseX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#mouseX
    """
    #  qreal QQuickMouseArea::mouseX() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea6mouseXEv')

  def mouseY(self) -> float:
    """
    Calls Qt's 'qreal QQuickMouseArea::mouseY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#mouseY
    """
    #  qreal QQuickMouseArea::mouseY() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea6mouseYEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#isEnabled
    """
    #  bool QQuickMouseArea::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea9isEnabledEv')

  def isScrollGestureEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::isScrollGestureEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#isScrollGestureEnabled
    """
    #  bool QQuickMouseArea::isScrollGestureEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea22isScrollGestureEnabledEv',
    )

  def hovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::hovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#hovered
    """
    #  bool QQuickMouseArea::hovered() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea7hoveredEv')

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#isPressed
    """
    #  bool QQuickMouseArea::isPressed() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea9isPressedEv')

  def containsPress(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::containsPress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#containsPress
    """
    #  bool QQuickMouseArea::containsPress() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea13containsPressEv')

  def pressedButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickMouseArea::pressedButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#pressedButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickMouseArea::pressedButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea14pressedButtonsEv',
    ))

  def acceptedButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickMouseArea::acceptedButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#acceptedButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickMouseArea::acceptedButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea15acceptedButtonsEv',
    ))

  def hoverEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::hoverEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#hoverEnabled
    """
    #  bool QQuickMouseArea::hoverEnabled() const
    return self.uglySide.call('ritual_ZNK15QQuickMouseArea12hoverEnabledEv')

  def preventStealing(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::preventStealing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#preventStealing
    """
    #  bool QQuickMouseArea::preventStealing() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea15preventStealingEv',
    )

  def propagateComposedEvents(self) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::propagateComposedEvents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#propagateComposedEvents
    """
    #  bool QQuickMouseArea::propagateComposedEvents() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea23propagateComposedEventsEv',
    )

  def cursorShape(self) -> Qt.CursorShape:
    """
    Calls Qt's 'Qt::CursorShape QQuickMouseArea::cursorShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#cursorShape

    Returns
    -------

    Qt.CursorShape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CursorShape(number)'
      gives.
    """
    #  Qt::CursorShape QQuickMouseArea::cursorShape() const
    return Qt.CursorShape(self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea11cursorShapeEv',
    ))

  def pressAndHoldInterval(self) -> int:
    """
    Calls Qt's 'int QQuickMouseArea::pressAndHoldInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#pressAndHoldInterval
    """
    #  int QQuickMouseArea::pressAndHoldInterval() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickMouseArea20pressAndHoldIntervalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN15QQuickMouseArea10setEnabledEb', a0)

  @overload(bool)
  def setScrollGestureEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setScrollGestureEnabled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setScrollGestureEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setScrollGestureEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea23setScrollGestureEnabledEb', a0,
    )

  @overload(Qt.MouseButtons)
  def setAcceptedButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setAcceptedButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setAcceptedButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickMouseArea::setAcceptedButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea18setAcceptedButtonsE6QFlagsIN2Qt11Mouse'
        'ButtonEE',
        buttons.value,
    )

  @overload(bool)
  def setHoverEnabled(self, h: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setHoverEnabled(bool h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setHoverEnabled

    Parameters
    ----------

    h : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setHoverEnabled(bool h)
    self.uglySide.call('ritual_ZN15QQuickMouseArea15setHoverEnabledEb', h)

  @overload(bool)
  def setPreventStealing(self, prevent: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setPreventStealing(bool prevent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setPreventStealing

    Parameters
    ----------

    prevent : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setPreventStealing(bool prevent)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea18setPreventStealingEb', prevent,
    )

  @overload(bool)
  def setPropagateComposedEvents(self, propagate: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setPropagateComposedEvents(bool
    propagate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setPropagateComposedEvents

    Parameters
    ----------

    propagate : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setPropagateComposedEvents(bool propagate)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea26setPropagateComposedEventsEb',
        propagate,
    )

  @overload(Qt.CursorShape)
  def setCursorShape(self, shape: Qt.CursorShape) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setCursorShape(Qt::CursorShape shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setCursorShape

    Parameters
    ----------

    shape : Qt.CursorShape
      Passed on as its number.
    """
    #  void QQuickMouseArea::setCursorShape(Qt::CursorShape shape)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea14setCursorShapeEN2Qt11CursorShapeE',
        shape.value,
    )

  @overload(int)
  def setPressAndHoldInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setPressAndHoldInterval(int interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#setPressAndHoldInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QQuickMouseArea::setPressAndHoldInterval(int interval)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea23setPressAndHoldIntervalEi', interval,
    )

  @overload(bool)
  def setHovered(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::setHovered(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#setHovered

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickMouseArea::setHovered(bool a0)
    self.uglySide.call('ritual_ZN15QQuickMouseArea10setHoveredEb', a0)

  @overload(Qt.MouseButton, bool, Qt.MouseEventSource)
  def setPressed(
      self,
      button: Qt.MouseButton,
      p: bool,
      source: Qt.MouseEventSource,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::setPressed(Qt::MouseButton button, bool
    p, Qt::MouseEventSource source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#setPressed

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.

    p : bool
      Passed on as it is.

    source : Qt.MouseEventSource
      Passed on as its number.
    """
    #  bool QQuickMouseArea::setPressed(Qt::MouseButton button, bool p,
    #      Qt::MouseEventSource source)
    return self.uglySide.call(
        'ritual_ZN15QQuickMouseArea10setPressedEN2Qt11MouseButtonEbNS0_16Mo'
        'useEventSourceE',
        button.value, p, source.value,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMouseArea::QQuickMouseArea(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#QQuickMouseArea

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMouseArea::QQuickMouseArea(QQuickItem *parent)
    self._noteCreation(QQuickMouseArea, lambda: Rituals.call(
        'ritual_ZN15QQuickMouseAreaC1EP10QQuickItem',
        self._addressOf(parent),
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

  def drag(self) -> Optional[QQuickDrag]:
    """
    Calls Qt's 'QQuickDrag *QQuickMouseArea::drag()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#drag

    Returns
    -------

    Optional[QQuickDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDrag *QQuickMouseArea::drag()
    address = self.uglySide.call('ritual_ZN15QQuickMouseArea4dragEv')
    from . import QQuickDrag
    return QQuickDrag._cuteAt(address)

  def resetPressAndHoldInterval(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::resetPressAndHoldInterval()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#resetPressAndHoldInterval
    """
    #  void QQuickMouseArea::resetPressAndHoldInterval()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea25resetPressAndHoldIntervalEv',
    )

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#hoveredChanged
    """
    #  void QQuickMouseArea::hoveredChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea14hoveredChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#pressedChanged
    """
    #  void QQuickMouseArea::pressedChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea14pressedChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#enabledChanged
    """
    #  void QQuickMouseArea::enabledChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea14enabledChangedEv')

  def scrollGestureEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::scrollGestureEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#scrollGestureEnabledChanged
    """
    #  void QQuickMouseArea::scrollGestureEnabledChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea27scrollGestureEnabledChangedEv',
    )

  def pressedButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::pressedButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#pressedButtonsChanged
    """
    #  void QQuickMouseArea::pressedButtonsChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea21pressedButtonsChangedEv')

  def acceptedButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::acceptedButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#acceptedButtonsChanged
    """
    #  void QQuickMouseArea::acceptedButtonsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea22acceptedButtonsChangedEv',
    )

  def hoverEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::hoverEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#hoverEnabledChanged
    """
    #  void QQuickMouseArea::hoverEnabledChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea19hoverEnabledChangedEv')

  def cursorShapeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::cursorShapeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#cursorShapeChanged
    """
    #  void QQuickMouseArea::cursorShapeChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea18cursorShapeChangedEv')

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def positionChanged(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::positionChanged(QQuickMouseEvent
    *mouse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#positionChanged

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::positionChanged(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea15positionChangedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def mouseXChanged(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseXChanged(QQuickMouseEvent
    *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#mouseXChanged

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mouseXChanged(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea13mouseXChangedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def mouseYChanged(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseYChanged(QQuickMouseEvent
    *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#mouseYChanged

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mouseYChanged(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea13mouseYChangedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  def preventStealingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::preventStealingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#preventStealingChanged
    """
    #  void QQuickMouseArea::preventStealingChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea22preventStealingChangedEv',
    )

  def propagateComposedEventsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::propagateComposedEventsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html
    """
    #  void QQuickMouseArea::propagateComposedEventsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea30propagateComposedEventsChangedEv',
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressed(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::pressed(QQuickMouseEvent *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#pressed

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::pressed(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea7pressedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def pressAndHold(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::pressAndHold(QQuickMouseEvent *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#pressAndHold

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::pressAndHold(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea12pressAndHoldEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def released(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::released(QQuickMouseEvent *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#released

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::released(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea8releasedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def clicked(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::clicked(QQuickMouseEvent *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#clicked

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::clicked(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea7clickedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickMouseEvent)
  @overload(NoneType)
  def doubleClicked(self, mouse: Optional[QQuickMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::doubleClicked(QQuickMouseEvent
    *mouse)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#doubleClicked

    Parameters
    ----------

    mouse : Optional[QQuickMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::doubleClicked(QQuickMouseEvent *mouse)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea13doubleClickedEP16QQuickMouseEvent',
        self._addressOf(mouse),
    )

  @overload(QQuickWheelEvent)
  @overload(NoneType)
  def wheel(self, wheel: Optional[QQuickWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::wheel(QQuickWheelEvent *wheel)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#wheel

    Parameters
    ----------

    wheel : Optional[QQuickWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::wheel(QQuickWheelEvent *wheel)
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea5wheelEP16QQuickWheelEvent',
        self._addressOf(wheel),
    )

  def entered(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::entered()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#entered
    """
    #  void QQuickMouseArea::entered()
    self.uglySide.call('ritual_ZN15QQuickMouseArea7enteredEv')

  def exited(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::exited()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#exited
    """
    #  void QQuickMouseArea::exited()
    self.uglySide.call('ritual_ZN15QQuickMouseArea6exitedEv')

  def canceled(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::canceled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#canceled
    """
    #  void QQuickMouseArea::canceled()
    self.uglySide.call('ritual_ZN15QQuickMouseArea8canceledEv')

  def containsPressChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::containsPressChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#containsPressChanged
    """
    #  void QQuickMouseArea::containsPressChanged()
    self.uglySide.call('ritual_ZN15QQuickMouseArea20containsPressChangedEv')

  def pressAndHoldIntervalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::pressAndHoldIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#pressAndHoldIntervalChanged
    """
    #  void QQuickMouseArea::pressAndHoldIntervalChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickMouseArea27pressAndHoldIntervalChangedEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def sendMouseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::sendMouseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#sendMouseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMouseArea::sendMouseEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN15QQuickMouseArea14sendMouseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN15QQuickMouseArea21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea21mouseDoubleClickEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#mouseUngrabEvent
    """
    #  void QQuickMouseArea::mouseUngrabEvent()
    ritual = 'ritual_ZN15QQuickMouseArea16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMouseArea16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::touchUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#touchUngrabEvent
    """
    #  void QQuickMouseArea::touchUngrabEvent()
    ritual = 'ritual_ZN15QQuickMouseArea16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMouseArea16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMouseArea10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      i: Optional[QQuickItem],
      e: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickMouseArea::childMouseEventFilter(QQuickItem *i,
    QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#childMouseEventFilter

    Parameters
    ----------

    i : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMouseArea::childMouseEventFilter(QQuickItem *i, QEvent *e)
    ritual = (
        'ritual_ZN15QQuickMouseArea21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(ritual, self._addressOf(i), self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMouseArea::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QQuickMouseArea10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMouseArea10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMouseArea::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickMouseArea14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMouseArea14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMouseArea::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickMouseArea10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickMouseArea::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmousearea.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickMouseArea::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN15QQuickMouseArea15updatePaintNodeEP7QSGNodePN10QQuickIte'
        'm19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMouseArea15updatePaintNodeEP7QSGNodePN10QQu'
          'ickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def ungrabMouse(self) -> None:
    """
    Calls Qt's 'void QQuickMouseArea::ungrabMouse()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#ungrabMouse
    """
    #  void QQuickMouseArea::ungrabMouse()
    self.uglySide.call('ritual_ZN15QQuickMouseArea11ungrabMouseEv')

  def d_func(self) -> Optional[QQuickMouseAreaPrivate]:
    """
    Calls Qt's 'QQuickMouseAreaPrivate *QQuickMouseArea::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmousearea.html#d_func

    Returns
    -------

    Optional[QQuickMouseAreaPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMouseAreaPrivate *QQuickMouseArea::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickMouseArea6d_funcEv')
    from . import QQuickMouseAreaPrivate
    return QQuickMouseAreaPrivate._cuteAt(address)
