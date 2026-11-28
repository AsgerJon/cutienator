"""
QQuickDial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDial to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
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


class QQuickDial(QQuickControl):
  """
  The cute side of Qt's QQuickDial: a plain Python object standing in front
  of one C++ QQuickDial.

  It is built on the cute 'QQuickControl', as Qt's QQuickDial is built on
  Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDial that has a ritual and that Python can
  call so far, 55 names in all: 'metaObject', 'tr', 'from_', 'setFrom', 'to',
  'setTo', 'value', 'setValue', 'position', 'angle', 'stepSize',
  'setStepSize', 'startAngle', 'setStartAngle', 'endAngle', 'setEndAngle',
  'snapMode', 'setSnapMode', 'wrap', 'setWrap', 'isPressed', 'setPressed',
  'handle', 'setHandle', 'live', 'setLive', 'inputMode', 'setInputMode',
  'increase', 'decrease', 'fromChanged', 'toChanged', 'valueChanged',
  'positionChanged', 'angleChanged', 'stepSizeChanged', 'snapModeChanged',
  'wrapChanged', 'pressedChanged', 'handleChanged', 'moved', 'liveChanged',
  'inputModeChanged', 'startAngleChanged', 'endAngleChanged', 'wrapped',
  'keyPressEvent', 'keyReleaseEvent', 'mousePressEvent', 'touchEvent',
  'wheelEvent', 'mirrorChange', 'componentComplete',
  'accessibilityActiveChanged', 'accessibleRole'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDial::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDial::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickDialPrivate *QQuickDial::d_func()': gives
    'QQuickDialPrivate', which has no cute class yet.
  - Qt's 'const QQuickDialPrivate *QQuickDial::d_func() const': gives
    'QQuickDialPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 64 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDial is created at the first use, not by 'QQuickDial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDial.
  - Qt tells when it has removed the C++ QQuickDial. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickDial, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class InputMode(CuteNum):
    """
    The enum 'QQuickDial::InputMode' of Qt, with the 3 names Qt gives in it.
    """

    Circular = Kee[int](0)
    Horizontal = Kee[int](1)
    Vertical = Kee[int](2)

  class SnapMode(CuteNum):
    """
    The enum 'QQuickDial::SnapMode' of Qt, with the 3 names Qt gives in it.
    """

    NoSnap = Kee[int](0)
    SnapAlways = Kee[int](1)
    SnapOnRelease = Kee[int](2)

  class WrapDirection(CuteNum):
    """
    The enum 'QQuickDial::WrapDirection' of Qt, with the 2 names Qt gives in
    it.
    """

    Clockwise = Kee[int](0)
    CounterClockwise = Kee[int](1)

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
    Calls Qt's 'QString QQuickDial::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#tr

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
    #  QString QQuickDial::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickDial2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDial::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDial::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickDial10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#from
    """
    #  qreal QQuickDial::from() const
    return self.uglySide.call('ritual_ZNK10QQuickDial4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#to
    """
    #  qreal QQuickDial::to() const
    return self.uglySide.call('ritual_ZNK10QQuickDial2toEv')

  def value(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#value
    """
    #  qreal QQuickDial::value() const
    return self.uglySide.call('ritual_ZNK10QQuickDial5valueEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#position
    """
    #  qreal QQuickDial::position() const
    return self.uglySide.call('ritual_ZNK10QQuickDial8positionEv')

  def angle(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::angle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#angle
    """
    #  qreal QQuickDial::angle() const
    return self.uglySide.call('ritual_ZNK10QQuickDial5angleEv')

  def stepSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::stepSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#stepSize
    """
    #  qreal QQuickDial::stepSize() const
    return self.uglySide.call('ritual_ZNK10QQuickDial8stepSizeEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#startAngle
    """
    #  qreal QQuickDial::startAngle() const
    return self.uglySide.call('ritual_ZNK10QQuickDial10startAngleEv')

  def endAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickDial::endAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#endAngle
    """
    #  qreal QQuickDial::endAngle() const
    return self.uglySide.call('ritual_ZNK10QQuickDial8endAngleEv')

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickDial::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickDial::snapMode() const
    return QQuickDial.SnapMode(self.uglySide.call(
        'ritual_ZNK10QQuickDial8snapModeEv',
    ))

  def wrap(self) -> bool:
    """
    Calls Qt's 'bool QQuickDial::wrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#wrap
    """
    #  bool QQuickDial::wrap() const
    return self.uglySide.call('ritual_ZNK10QQuickDial4wrapEv')

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickDial::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#isPressed
    """
    #  bool QQuickDial::isPressed() const
    return self.uglySide.call('ritual_ZNK10QQuickDial9isPressedEv')

  def handle(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDial::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#handle

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDial::handle() const
    address = self.uglySide.call('ritual_ZNK10QQuickDial6handleEv')
    return QQuickItem._cuteAt(address)

  def live(self) -> bool:
    """
    Calls Qt's 'bool QQuickDial::live() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#live
    """
    #  bool QQuickDial::live() const
    return self.uglySide.call('ritual_ZNK10QQuickDial4liveEv')

  def inputMode(self) -> InputMode:
    """
    Calls Qt's 'InputMode QQuickDial::inputMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#inputMode

    Returns
    -------

    InputMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InputMode(number)' gives.
    """
    #  InputMode QQuickDial::inputMode() const
    return QQuickDial.InputMode(self.uglySide.call(
        'ritual_ZNK10QQuickDial9inputModeEv',
    ))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickDial::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickDial::accessibleRole() const
    ritual = 'ritual_ZNK10QQuickDial14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickDial14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickDial::setFrom(qreal from)
    self.uglySide.call('ritual_ZN10QQuickDial7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickDial::setTo(qreal to)
    self.uglySide.call('ritual_ZN10QQuickDial5setToEd', to)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setValue(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QQuickDial::setValue(qreal value)
    self.uglySide.call('ritual_ZN10QQuickDial8setValueEd', value)

  @overload(float)
  def setStepSize(self, step: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setStepSize(qreal step)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setStepSize

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QQuickDial::setStepSize(qreal step)
    self.uglySide.call('ritual_ZN10QQuickDial11setStepSizeEd', step)

  @overload(float)
  def setStartAngle(self, startAngle: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setStartAngle(qreal startAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setStartAngle

    Parameters
    ----------

    startAngle : float
      Passed on as it is.
    """
    #  void QQuickDial::setStartAngle(qreal startAngle)
    self.uglySide.call('ritual_ZN10QQuickDial13setStartAngleEd', startAngle)

  @overload(float)
  def setEndAngle(self, endAngle: float) -> None:
    """
    Calls Qt's 'void QQuickDial::setEndAngle(qreal endAngle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setEndAngle

    Parameters
    ----------

    endAngle : float
      Passed on as it is.
    """
    #  void QQuickDial::setEndAngle(qreal endAngle)
    self.uglySide.call('ritual_ZN10QQuickDial11setEndAngleEd', endAngle)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickDial::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickDial::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN10QQuickDial11setSnapModeENS_8SnapModeE', mode.value,
    )

  @overload(bool)
  def setWrap(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickDial::setWrap(bool wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setWrap

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickDial::setWrap(bool wrap)
    self.uglySide.call('ritual_ZN10QQuickDial7setWrapEb', wrap)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickDial::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickDial::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN10QQuickDial10setPressedEb', pressed)

  @overload(QQuickItem)
  @overload(NoneType)
  def setHandle(self, handle: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDial::setHandle(QQuickItem *handle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setHandle

    Parameters
    ----------

    handle : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::setHandle(QQuickItem *handle)
    self.uglySide.call(
        'ritual_ZN10QQuickDial9setHandleEP10QQuickItem',
        self._addressOf(handle),
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickDial::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickDial::setLive(bool live)
    self.uglySide.call('ritual_ZN10QQuickDial7setLiveEb', live)

  @overload(InputMode)
  def setInputMode(self, mode: InputMode) -> None:
    """
    Calls Qt's 'void QQuickDial::setInputMode(InputMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#setInputMode

    Parameters
    ----------

    mode : InputMode
      Passed on as its number.
    """
    #  void QQuickDial::setInputMode(InputMode mode)
    self.uglySide.call(
        'ritual_ZN10QQuickDial12setInputModeENS_9InputModeE', mode.value,
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
    Notes what was given, for Qt's 'QQuickDial::QQuickDial(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#QQuickDial

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDial::QQuickDial(QQuickItem *parent)
    self._noteCreation(QQuickDial, lambda: Rituals.call(
        'ritual_ZN10QQuickDialC1EP10QQuickItem', self._addressOf(parent),
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

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickDial::increase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#increase
    """
    #  void QQuickDial::increase()
    self.uglySide.call('ritual_ZN10QQuickDial8increaseEv')

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickDial::decrease()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#decrease
    """
    #  void QQuickDial::decrease()
    self.uglySide.call('ritual_ZN10QQuickDial8decreaseEv')

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#fromChanged
    """
    #  void QQuickDial::fromChanged()
    self.uglySide.call('ritual_ZN10QQuickDial11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#toChanged
    """
    #  void QQuickDial::toChanged()
    self.uglySide.call('ritual_ZN10QQuickDial9toChangedEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#valueChanged
    """
    #  void QQuickDial::valueChanged()
    self.uglySide.call('ritual_ZN10QQuickDial12valueChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#positionChanged
    """
    #  void QQuickDial::positionChanged()
    self.uglySide.call('ritual_ZN10QQuickDial15positionChangedEv')

  def angleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::angleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#angleChanged
    """
    #  void QQuickDial::angleChanged()
    self.uglySide.call('ritual_ZN10QQuickDial12angleChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::stepSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#stepSizeChanged
    """
    #  void QQuickDial::stepSizeChanged()
    self.uglySide.call('ritual_ZN10QQuickDial15stepSizeChangedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::snapModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#snapModeChanged
    """
    #  void QQuickDial::snapModeChanged()
    self.uglySide.call('ritual_ZN10QQuickDial15snapModeChangedEv')

  def wrapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::wrapChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#wrapChanged
    """
    #  void QQuickDial::wrapChanged()
    self.uglySide.call('ritual_ZN10QQuickDial11wrapChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::pressedChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#pressedChanged
    """
    #  void QQuickDial::pressedChanged()
    self.uglySide.call('ritual_ZN10QQuickDial14pressedChangedEv')

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::handleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#handleChanged
    """
    #  void QQuickDial::handleChanged()
    self.uglySide.call('ritual_ZN10QQuickDial13handleChangedEv')

  def moved(self) -> None:
    """
    Calls Qt's 'void QQuickDial::moved()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#moved
    """
    #  void QQuickDial::moved()
    self.uglySide.call('ritual_ZN10QQuickDial5movedEv')

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::liveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#liveChanged
    """
    #  void QQuickDial::liveChanged()
    self.uglySide.call('ritual_ZN10QQuickDial11liveChangedEv')

  def inputModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::inputModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#inputModeChanged
    """
    #  void QQuickDial::inputModeChanged()
    self.uglySide.call('ritual_ZN10QQuickDial16inputModeChangedEv')

  def startAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::startAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#startAngleChanged
    """
    #  void QQuickDial::startAngleChanged()
    self.uglySide.call('ritual_ZN10QQuickDial17startAngleChangedEv')

  def endAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDial::endAngleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#endAngleChanged
    """
    #  void QQuickDial::endAngleChanged()
    self.uglySide.call('ritual_ZN10QQuickDial15endAngleChangedEv')

  @overload(WrapDirection)
  def wrapped(self, a0: WrapDirection) -> None:
    """
    Calls Qt's 'void QQuickDial::wrapped(WrapDirection a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#wrapped

    Parameters
    ----------

    a0 : WrapDirection
      Passed on as its number.
    """
    #  void QQuickDial::wrapped(WrapDirection a0)
    self.uglySide.call(
        'ritual_ZN10QQuickDial7wrappedENS_13WrapDirectionE', a0.value,
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickDial::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN10QQuickDial13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickDial::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN10QQuickDial15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickDial::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN10QQuickDial15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickDial::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN10QQuickDial10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickDial::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDial::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN10QQuickDial10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickDial::mirrorChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#mirrorChange
    """
    #  void QQuickDial::mirrorChange()
    ritual = 'ritual_ZN10QQuickDial12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial12mirrorChangeEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickDial::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdial.html#componentComplete
    """
    #  void QQuickDial::componentComplete()
    ritual = 'ritual_ZN10QQuickDial17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickDial::accessibilityActiveChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdial.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickDial::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN10QQuickDial26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickDial26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)
