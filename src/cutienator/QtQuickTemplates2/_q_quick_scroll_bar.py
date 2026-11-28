"""
QQuickScrollBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollBar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QHoverEvent, QMouseEvent
  from . import QQuickIndicatorButton, QQuickScrollBarAttached
  from . import QQuickScrollBarPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHoverEvent = WAIT['QHoverEvent']
  QMouseEvent = WAIT['QMouseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollBar(QQuickControl):
  """
  The cute side of Qt's QQuickScrollBar: a plain Python object standing in
  front of one C++ QQuickScrollBar.

  It is built on the cute 'QQuickControl', as Qt's QQuickScrollBar is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScrollBar that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'size', 'position', 'stepSize', 'setStepSize',
  'isActive', 'setActive', 'isPressed', 'setPressed', 'orientation',
  'setOrientation', 'snapMode', 'setSnapMode', 'isInteractive',
  'setInteractive', 'resetInteractive', 'policy', 'setPolicy',
  'isHorizontal', 'isVertical', 'minimumSize', 'setMinimumSize',
  'visualSize', 'visualPosition', 'decreaseVisual', 'increaseVisual',
  'increase', 'decrease', 'setSize', 'setPosition', 'sizeChanged',
  'positionChanged', 'stepSizeChanged', 'activeChanged', 'pressedChanged',
  'orientationChanged', 'snapModeChanged', 'interactiveChanged',
  'policyChanged', 'minimumSizeChanged', 'visualSizeChanged',
  'visualPositionChanged', 'mousePressEvent', 'hoverChange',
  'hoverEnterEvent', 'hoverMoveEvent', 'hoverLeaveEvent', 'classBegin',
  'componentComplete', 'accessibilityActiveChanged', 'accessibleRole',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScrollBar::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickScrollBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickScrollBar::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'const QQuickScrollBarPrivate *QQuickScrollBar::d_func() const':
    takes in Python what 'QQuickScrollBarPrivate *QQuickScrollBar::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 63 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickScrollBar is created at the first use, not by
    'QQuickScrollBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollBar.
  - Qt tells when it has removed the C++ QQuickScrollBar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickScrollBar, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Policy(CuteNum):
    """
    The enum 'QQuickScrollBar::Policy' of Qt, with the 3 names Qt gives in
    it.
    """

    AsNeeded = Kee[int](0)
    AlwaysOff = Kee[int](1)
    AlwaysOn = Kee[int](2)

  class SnapMode(CuteNum):
    """
    The enum 'QQuickScrollBar::SnapMode' of Qt, with the 3 names Qt gives in
    it.
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
    Calls Qt's 'QString QQuickScrollBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#tr

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
    #  QString QQuickScrollBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickScrollBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickScrollBarAttached]:
    """
    Calls Qt's 'QQuickScrollBarAttached
    *QQuickScrollBar::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickScrollBarAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBarAttached
    #      *QQuickScrollBar::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN15QQuickScrollBar21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickScrollBarAttached
    return QQuickScrollBarAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScrollBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScrollBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickScrollBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def size(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#size
    """
    #  qreal QQuickScrollBar::size() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar4sizeEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#position
    """
    #  qreal QQuickScrollBar::position() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar8positionEv')

  def stepSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::stepSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#stepSize
    """
    #  qreal QQuickScrollBar::stepSize() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar8stepSizeEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBar::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#isActive
    """
    #  bool QQuickScrollBar::isActive() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar8isActiveEv')

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBar::isPressed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#isPressed
    """
    #  bool QQuickScrollBar::isPressed() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar9isPressedEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickScrollBar::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickScrollBar::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QQuickScrollBar11orientationEv',
    ))

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickScrollBar::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickScrollBar::snapMode() const
    return QQuickScrollBar.SnapMode(self.uglySide.call(
        'ritual_ZNK15QQuickScrollBar8snapModeEv',
    ))

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBar::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#isInteractive
    """
    #  bool QQuickScrollBar::isInteractive() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar13isInteractiveEv')

  def policy(self) -> Policy:
    """
    Calls Qt's 'Policy QQuickScrollBar::policy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#policy

    Returns
    -------

    Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Policy(number)' gives.
    """
    #  Policy QQuickScrollBar::policy() const
    return QQuickScrollBar.Policy(self.uglySide.call(
        'ritual_ZNK15QQuickScrollBar6policyEv',
    ))

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBar::isHorizontal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#isHorizontal
    """
    #  bool QQuickScrollBar::isHorizontal() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar12isHorizontalEv')

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollBar::isVertical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#isVertical
    """
    #  bool QQuickScrollBar::isVertical() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar10isVerticalEv')

  def minimumSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#minimumSize
    """
    #  qreal QQuickScrollBar::minimumSize() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar11minimumSizeEv')

  def visualSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::visualSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#visualSize
    """
    #  qreal QQuickScrollBar::visualSize() const
    return self.uglySide.call('ritual_ZNK15QQuickScrollBar10visualSizeEv')

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollBar::visualPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#visualPosition
    """
    #  qreal QQuickScrollBar::visualPosition() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickScrollBar14visualPositionEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickScrollBar::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickScrollBar::accessibleRole() const
    ritual = 'ritual_ZNK15QQuickScrollBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickScrollBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setStepSize(self, step: float) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setStepSize(qreal step)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setStepSize

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QQuickScrollBar::setStepSize(qreal step)
    self.uglySide.call('ritual_ZN15QQuickScrollBar11setStepSizeEd', step)

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickScrollBar::setActive(bool active)
    self.uglySide.call('ritual_ZN15QQuickScrollBar9setActiveEb', active)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setPressed(bool pressed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickScrollBar::setPressed(bool pressed)
    self.uglySide.call('ritual_ZN15QQuickScrollBar10setPressedEb', pressed)

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickScrollBar::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QQuickScrollBar14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickScrollBar::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN15QQuickScrollBar11setSnapModeENS_8SnapModeE', mode.value,
    )

  @overload(bool)
  def setInteractive(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setInteractive(bool interactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#setInteractive

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QQuickScrollBar::setInteractive(bool interactive)
    self.uglySide.call(
        'ritual_ZN15QQuickScrollBar14setInteractiveEb', interactive,
    )

  @overload(Policy)
  def setPolicy(self, policy: Policy) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setPolicy(Policy policy)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setPolicy

    Parameters
    ----------

    policy : Policy
      Passed on as its number.
    """
    #  void QQuickScrollBar::setPolicy(Policy policy)
    self.uglySide.call(
        'ritual_ZN15QQuickScrollBar9setPolicyENS_6PolicyE', policy.value,
    )

  @overload(float)
  def setMinimumSize(self, minimumSize: float) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setMinimumSize(qreal minimumSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#setMinimumSize

    Parameters
    ----------

    minimumSize : float
      Passed on as it is.
    """
    #  void QQuickScrollBar::setMinimumSize(qreal minimumSize)
    self.uglySide.call(
        'ritual_ZN15QQuickScrollBar14setMinimumSizeEd', minimumSize,
    )

  @overload(float)
  def setSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setSize(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuickScrollBar::setSize(qreal size)
    self.uglySide.call('ritual_ZN15QQuickScrollBar7setSizeEd', size)

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::setPosition(qreal position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickScrollBar::setPosition(qreal position)
    self.uglySide.call('ritual_ZN15QQuickScrollBar11setPositionEd', position)

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
    'QQuickScrollBar::QQuickScrollBar(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#QQuickScrollBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScrollBar::QQuickScrollBar(QQuickItem *parent)
    self._noteCreation(QQuickScrollBar, lambda: Rituals.call(
        'ritual_ZN15QQuickScrollBarC1EP10QQuickItem',
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

  def resetInteractive(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::resetInteractive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#resetInteractive
    """
    #  void QQuickScrollBar::resetInteractive()
    self.uglySide.call('ritual_ZN15QQuickScrollBar16resetInteractiveEv')

  def decreaseVisual(self) -> Optional[QQuickIndicatorButton]:
    """
    Calls Qt's 'QQuickIndicatorButton *QQuickScrollBar::decreaseVisual()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#decreaseVisual

    Returns
    -------

    Optional[QQuickIndicatorButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIndicatorButton *QQuickScrollBar::decreaseVisual()
    address = self.uglySide.call(
        'ritual_ZN15QQuickScrollBar14decreaseVisualEv',
    )
    from . import QQuickIndicatorButton
    return QQuickIndicatorButton._cuteAt(address)

  def increaseVisual(self) -> Optional[QQuickIndicatorButton]:
    """
    Calls Qt's 'QQuickIndicatorButton *QQuickScrollBar::increaseVisual()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#increaseVisual

    Returns
    -------

    Optional[QQuickIndicatorButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickIndicatorButton *QQuickScrollBar::increaseVisual()
    address = self.uglySide.call(
        'ritual_ZN15QQuickScrollBar14increaseVisualEv',
    )
    from . import QQuickIndicatorButton
    return QQuickIndicatorButton._cuteAt(address)

  def increase(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::increase()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#increase
    """
    #  void QQuickScrollBar::increase()
    self.uglySide.call('ritual_ZN15QQuickScrollBar8increaseEv')

  def decrease(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::decrease()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#decrease
    """
    #  void QQuickScrollBar::decrease()
    self.uglySide.call('ritual_ZN15QQuickScrollBar8decreaseEv')

  def sizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::sizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#sizeChanged
    """
    #  void QQuickScrollBar::sizeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar11sizeChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#positionChanged
    """
    #  void QQuickScrollBar::positionChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar15positionChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::stepSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#stepSizeChanged
    """
    #  void QQuickScrollBar::stepSizeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar15stepSizeChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#activeChanged
    """
    #  void QQuickScrollBar::activeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar13activeChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#pressedChanged
    """
    #  void QQuickScrollBar::pressedChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar14pressedChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#orientationChanged
    """
    #  void QQuickScrollBar::orientationChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar18orientationChangedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#snapModeChanged
    """
    #  void QQuickScrollBar::snapModeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar15snapModeChangedEv')

  def interactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::interactiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#interactiveChanged
    """
    #  void QQuickScrollBar::interactiveChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar18interactiveChangedEv')

  def policyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::policyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#policyChanged
    """
    #  void QQuickScrollBar::policyChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar13policyChangedEv')

  def minimumSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::minimumSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#minimumSizeChanged
    """
    #  void QQuickScrollBar::minimumSizeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar18minimumSizeChangedEv')

  def visualSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::visualSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#visualSizeChanged
    """
    #  void QQuickScrollBar::visualSizeChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar17visualSizeChangedEv')

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#visualPositionChanged
    """
    #  void QQuickScrollBar::visualPositionChanged()
    self.uglySide.call('ritual_ZN15QQuickScrollBar21visualPositionChangedEv')

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBar::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickScrollBar15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickScrollBar15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def hoverChange(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::hoverChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#hoverChange
    """
    #  void QQuickScrollBar::hoverChange()
    ritual = 'ritual_ZN15QQuickScrollBar11hoverChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickScrollBar11hoverChangeEv'
    self.uglySide.call(ritual)

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBar::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickScrollBar15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickScrollBar15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBar::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickScrollBar14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickScrollBar14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBar::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickScrollBar15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickScrollBar15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#classBegin
    """
    #  void QQuickScrollBar::classBegin()
    ritual = 'ritual_ZN15QQuickScrollBar10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickScrollBar10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#componentComplete
    """
    #  void QQuickScrollBar::componentComplete()
    ritual = 'ritual_ZN15QQuickScrollBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickScrollBar17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollBar::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbar.html#accessibilityActiveChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickScrollBar::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN15QQuickScrollBar26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickScrollBar26accessibilityActiveChangedEb'
    self.uglySide.call(ritual, active)

  def d_func(self) -> Optional[QQuickScrollBarPrivate]:
    """
    Calls Qt's 'QQuickScrollBarPrivate *QQuickScrollBar::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollbar.html#d_func

    Returns
    -------

    Optional[QQuickScrollBarPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBarPrivate *QQuickScrollBar::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickScrollBar6d_funcEv')
    from . import QQuickScrollBarPrivate
    return QQuickScrollBarPrivate._cuteAt(address)
