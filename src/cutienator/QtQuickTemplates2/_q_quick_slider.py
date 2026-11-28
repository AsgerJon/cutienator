"""
QQuickSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickslider_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSlider to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QKeyEvent, QMouseEvent, QTouchEvent, QWheelEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSlider(QQuickControl):
  """
  The cute side of Qt's QQuickSlider: a plain Python object standing in front
  of one C++ QQuickSlider.

  It is built on the cute 'QQuickControl', as Qt's QQuickSlider is built on
  Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSlider that has a ritual and that Python can
  call so far, 56 names in all: 'metaObject', 'tr', 'from_', 'setFrom', 'to',
  'setTo', 'value', 'setValue', 'position', 'visualPosition', 'stepSize',
  'setStepSize', 'snapMode', 'setSnapMode', 'isPressed', 'setPressed',
  'orientation', 'setOrientation', 'handle', 'setHandle', 'valueAt', 'live',
  'setLive', 'isHorizontal', 'isVertical', 'touchDragThreshold',
  'setTouchDragThreshold', 'resetTouchDragThreshold', 'implicitHandleWidth',
  'implicitHandleHeight', 'increase', 'decrease', 'fromChanged', 'toChanged',
  'valueChanged', 'positionChanged', 'visualPositionChanged',
  'stepSizeChanged', 'snapModeChanged', 'pressedChanged',
  'orientationChanged', 'handleChanged', 'moved', 'liveChanged',
  'touchDragThresholdChanged', 'implicitHandleWidthChanged',
  'implicitHandleHeightChanged', 'keyPressEvent', 'keyReleaseEvent',
  'mousePressEvent', 'touchEvent', 'wheelEvent', 'mirrorChange',
  'componentComplete', 'accessibilityActiveChanged', 'accessibleRole'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSlider::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSlider::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSlider::~QQuickSlider()': the destructor: Python never
    removes a C++ QQuickSlider.
  - Qt's 'QQuickSliderPrivate *QQuickSlider::d_func()': gives
    'QQuickSliderPrivate', which has no cute class yet.
  - Qt's 'const QQuickSliderPrivate *QQuickSlider::d_func() const': gives
    'QQuickSliderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 66 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSlider is created at the first use, not by
    'QQuickSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSlider.
  - Qt tells when it has removed the C++ QQuickSlider. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSlider, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class SnapMode(CuteNum):
    """
    The enum 'QQuickSlider::SnapMode' of Qt, with the 3 names Qt gives in it.
    """

    NoSnap = Kee[int](0)
    SnapAlways = Kee[int](1)
    SnapOnRelease = Kee[int](2)

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
    Calls Qt's 'QString QQuickSlider::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#tr

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
    #  QString QQuickSlider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickSlider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSlider'

  #  A C++ QQuickSlider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSlider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSlider::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSlider::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickSlider10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#from
    """
    #  qreal QQuickSlider::from() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#to
    """
    #  qreal QQuickSlider::to() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider2toEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#value
    """
    #  qreal QQuickSlider::value() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider5valueEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#position
    """
    #  qreal QQuickSlider::position() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider8positionEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::visualPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#visualPosition
    """
    #  qreal QQuickSlider::visualPosition() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider14visualPositionEv')

  def stepSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::stepSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#stepSize
    """
    #  qreal QQuickSlider::stepSize() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider8stepSizeEv')

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickSlider::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickSlider::snapMode() const
    return QQuickSlider.SnapMode(self.uglySide.call(
        'ritual_ZNK12QQuickSlider8snapModeEv',
    ))

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickSlider::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#isPressed
    """
    #  bool QQuickSlider::isPressed() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider9isPressedEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickSlider::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickSlider::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK12QQuickSlider11orientationEv',
    ))

  def handle(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSlider::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#handle

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSlider::handle() const
    address = self.uglySide.call('ritual_ZNK12QQuickSlider6handleEv')
    return QQuickItem._cuteAt(address)

  @overload(float)
  def valueAt(self, position: float) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::valueAt(qreal position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#valueAt

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  qreal QQuickSlider::valueAt(qreal position) const
    return self.uglySide.call('ritual_ZNK12QQuickSlider7valueAtEd', position)

  def live(self) -> bool:
    """
    Calls Qt's 'bool QQuickSlider::live() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#live
    """
    #  bool QQuickSlider::live() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider4liveEv')

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickSlider::isHorizontal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#isHorizontal
    """
    #  bool QQuickSlider::isHorizontal() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider12isHorizontalEv')

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickSlider::isVertical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#isVertical
    """
    #  bool QQuickSlider::isVertical() const
    return self.uglySide.call('ritual_ZNK12QQuickSlider10isVerticalEv')

  def touchDragThreshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::touchDragThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#touchDragThreshold
    """
    #  qreal QQuickSlider::touchDragThreshold() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickSlider18touchDragThresholdEv',
    )

  def implicitHandleWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::implicitHandleWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#implicitHandleWidth
    """
    #  qreal QQuickSlider::implicitHandleWidth() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickSlider19implicitHandleWidthEv',
    )

  def implicitHandleHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickSlider::implicitHandleHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#implicitHandleHeight
    """
    #  qreal QQuickSlider::implicitHandleHeight() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickSlider20implicitHandleHeightEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickSlider::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickSlider::accessibleRole() const
    ritual = 'ritual_ZNK12QQuickSlider14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickSlider14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickSlider::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickSlider::setFrom(qreal from)
    self.uglySide.call('ritual_ZN12QQuickSlider7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickSlider::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickSlider::setTo(qreal to)
    self.uglySide.call('ritual_ZN12QQuickSlider5setToEd', to)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickSlider::setValue(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickSlider::setValue(qreal value)
    self.uglySide.call('ritual_ZN12QQuickSlider8setValueEd', value)

  @overload(float)
  def setStepSize(self, step: float) -> None:
    """
    Calls Qt's 'void QQuickSlider::setStepSize(qreal step)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setStepSize

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QQuickSlider::setStepSize(qreal step)
    self.uglySide.call('ritual_ZN12QQuickSlider11setStepSizeEd', step)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickSlider::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickSlider::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN12QQuickSlider11setSnapModeENS_8SnapModeE', mode.value,
    )

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickSlider::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickSlider::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN12QQuickSlider10setPressedEb', pressed)

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickSlider::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickSlider::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN12QQuickSlider14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setHandle(self, handle: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSlider::setHandle(QQuickItem *handle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setHandle

    Parameters
    ----------

    handle : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::setHandle(QQuickItem *handle)
    self.uglySide.call(
        'ritual_ZN12QQuickSlider9setHandleEP10QQuickItem',
        self._addressOf(handle),
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickSlider::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickSlider::setLive(bool live)
    self.uglySide.call('ritual_ZN12QQuickSlider7setLiveEb', live)

  @overload(float)
  def setTouchDragThreshold(self, touchDragThreshold: float) -> None:
    """
    Calls Qt's 'void QQuickSlider::setTouchDragThreshold(qreal
    touchDragThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#setTouchDragThreshold

    Parameters
    ----------

    touchDragThreshold : float
      Passed on as it is.
    """
    #  void QQuickSlider::setTouchDragThreshold(qreal touchDragThreshold)
    self.uglySide.call(
        'ritual_ZN12QQuickSlider21setTouchDragThresholdEd',
        touchDragThreshold,
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
    Notes what was given, for Qt's 'QQuickSlider::QQuickSlider(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#QQuickSlider

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSlider::QQuickSlider(QQuickItem *parent)
    self._noteCreation(QQuickSlider, lambda: Rituals.call(
        'ritual_ZN12QQuickSliderC1EP10QQuickItem', self._addressOf(parent),
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

  def resetTouchDragThreshold(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::resetTouchDragThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#resetTouchDragThreshold
    """
    #  void QQuickSlider::resetTouchDragThreshold()
    self.uglySide.call('ritual_ZN12QQuickSlider23resetTouchDragThresholdEv')

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::increase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#increase
    """
    #  void QQuickSlider::increase()
    self.uglySide.call('ritual_ZN12QQuickSlider8increaseEv')

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::decrease()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#decrease
    """
    #  void QQuickSlider::decrease()
    self.uglySide.call('ritual_ZN12QQuickSlider8decreaseEv')

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#fromChanged
    """
    #  void QQuickSlider::fromChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#toChanged
    """
    #  void QQuickSlider::toChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider9toChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#valueChanged
    """
    #  void QQuickSlider::valueChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider12valueChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#positionChanged
    """
    #  void QQuickSlider::positionChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider15positionChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#visualPositionChanged
    """
    #  void QQuickSlider::visualPositionChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider21visualPositionChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::stepSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#stepSizeChanged
    """
    #  void QQuickSlider::stepSizeChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider15stepSizeChangedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::snapModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#snapModeChanged
    """
    #  void QQuickSlider::snapModeChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider15snapModeChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::pressedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#pressedChanged
    """
    #  void QQuickSlider::pressedChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider14pressedChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#orientationChanged
    """
    #  void QQuickSlider::orientationChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider18orientationChangedEv')

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::handleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#handleChanged
    """
    #  void QQuickSlider::handleChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider13handleChangedEv')

  def moved(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::moved()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#moved
    """
    #  void QQuickSlider::moved()
    self.uglySide.call('ritual_ZN12QQuickSlider5movedEv')

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::liveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#liveChanged
    """
    #  void QQuickSlider::liveChanged()
    self.uglySide.call('ritual_ZN12QQuickSlider11liveChangedEv')

  def touchDragThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::touchDragThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#touchDragThresholdChanged
    """
    #  void QQuickSlider::touchDragThresholdChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickSlider25touchDragThresholdChangedEv',
    )

  def implicitHandleWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::implicitHandleWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#implicitHandleWidthChanged
    """
    #  void QQuickSlider::implicitHandleWidthChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickSlider26implicitHandleWidthChangedEv',
    )

  def implicitHandleHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::implicitHandleHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#implicitHandleHeightChanged
    """
    #  void QQuickSlider::implicitHandleHeightChanged()
    self.uglySide.call(
        'ritual_ZN12QQuickSlider27implicitHandleHeightChangedEv',
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickSlider::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN12QQuickSlider13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickSlider::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN12QQuickSlider15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickSlider::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN12QQuickSlider15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickSlider::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN12QQuickSlider10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickSlider::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSlider::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN12QQuickSlider10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::mirrorChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickslider.html#mirrorChange
    """
    #  void QQuickSlider::mirrorChange()
    ritual = 'ritual_ZN12QQuickSlider12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider12mirrorChangeEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSlider::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#componentComplete
    """
    #  void QQuickSlider::componentComplete()
    ritual = 'ritual_ZN12QQuickSlider17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickSlider::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickslider.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickSlider::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN12QQuickSlider26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickSlider26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)
