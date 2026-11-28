"""
QQuickRangeSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickrangeslider_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRangeSlider to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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
  from ..QtGui import QFocusEvent, QHoverEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QTouchEvent
  from . import QQuickRangeSliderNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFocusEvent = WAIT['QFocusEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickRangeSliderNode = WAIT['QQuickRangeSliderNode']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRangeSlider(QQuickControl):
  """
  The cute side of Qt's QQuickRangeSlider: a plain Python object standing in
  front of one C++ QQuickRangeSlider.

  It is built on the cute 'QQuickControl', as Qt's QQuickRangeSlider is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRangeSlider that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr', 'from_', 'setFrom',
  'to', 'setTo', 'first', 'second', 'stepSize', 'setStepSize', 'snapMode',
  'setSnapMode', 'orientation', 'setOrientation', 'setValues', 'live',
  'setLive', 'isHorizontal', 'isVertical', 'touchDragThreshold',
  'setTouchDragThreshold', 'resetTouchDragThreshold', 'valueAt',
  'isCrossingEnabled', 'setCrossingEnabled', 'handlesCrossed',
  'effectiveFirstValue', 'effectiveSecondValue', 'fromChanged', 'toChanged',
  'stepSizeChanged', 'snapModeChanged', 'orientationChanged', 'liveChanged',
  'touchDragThresholdChanged', 'crossingEnabledChanged',
  'handlesCrossedChanged', 'effectiveFirstValueChanged',
  'effectiveSecondValueChanged', 'focusInEvent', 'hoverEnterEvent',
  'hoverMoveEvent', 'hoverLeaveEvent', 'keyPressEvent', 'keyReleaseEvent',
  'mousePressEvent', 'touchEvent', 'mirrorChange', 'classBegin',
  'componentComplete', 'accessibleRole', 'updateHandleCrossing',
  'effectiveValueChange', 'updateFocusOrder'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRangeSlider::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickRangeSlider::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRangeSlider::~QQuickRangeSlider()': the destructor: Python
    never removes a C++ QQuickRangeSlider.
  - Qt's 'QQuickRangeSliderPrivate *QQuickRangeSlider::d_func()': gives
    'QQuickRangeSliderPrivate', which has no cute class yet.
  - Qt's 'const QQuickRangeSliderPrivate *QQuickRangeSlider::d_func() const':
    gives 'QQuickRangeSliderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 64 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRangeSlider is created at the first use, not by
    'QQuickRangeSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRangeSlider.
  - Qt tells when it has removed the C++ QQuickRangeSlider. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickRangeSlider, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SnapMode(CuteNum):
    """
    The enum 'QQuickRangeSlider::SnapMode' of Qt, with the 3 names Qt gives
    in it.
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
    Calls Qt's 'QString QQuickRangeSlider::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#tr

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
    #  QString QQuickRangeSlider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickRangeSlider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRangeSlider'

  #  A C++ QQuickRangeSlider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRangeSlider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRangeSlider::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRangeSlider::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#from
    """
    #  qreal QQuickRangeSlider::from() const
    return self.uglySide.call('ritual_ZNK17QQuickRangeSlider4fromEv')

  def to(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#to
    """
    #  qreal QQuickRangeSlider::to() const
    return self.uglySide.call('ritual_ZNK17QQuickRangeSlider2toEv')

  def first(self) -> Optional[QQuickRangeSliderNode]:
    """
    Calls Qt's 'QQuickRangeSliderNode *QQuickRangeSlider::first() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#first

    Returns
    -------

    Optional[QQuickRangeSliderNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRangeSliderNode *QQuickRangeSlider::first() const
    address = self.uglySide.call('ritual_ZNK17QQuickRangeSlider5firstEv')
    from . import QQuickRangeSliderNode
    return QQuickRangeSliderNode._cuteAt(address)

  def second(self) -> Optional[QQuickRangeSliderNode]:
    """
    Calls Qt's 'QQuickRangeSliderNode *QQuickRangeSlider::second() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#second

    Returns
    -------

    Optional[QQuickRangeSliderNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRangeSliderNode *QQuickRangeSlider::second() const
    address = self.uglySide.call('ritual_ZNK17QQuickRangeSlider6secondEv')
    from . import QQuickRangeSliderNode
    return QQuickRangeSliderNode._cuteAt(address)

  def stepSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::stepSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#stepSize
    """
    #  qreal QQuickRangeSlider::stepSize() const
    return self.uglySide.call('ritual_ZNK17QQuickRangeSlider8stepSizeEv')

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickRangeSlider::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickRangeSlider::snapMode() const
    return QQuickRangeSlider.SnapMode(self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider8snapModeEv',
    ))

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickRangeSlider::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickRangeSlider::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider11orientationEv',
    ))

  def live(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSlider::live() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#live
    """
    #  bool QQuickRangeSlider::live() const
    return self.uglySide.call('ritual_ZNK17QQuickRangeSlider4liveEv')

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSlider::isHorizontal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#isHorizontal
    """
    #  bool QQuickRangeSlider::isHorizontal() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider12isHorizontalEv',
    )

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSlider::isVertical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#isVertical
    """
    #  bool QQuickRangeSlider::isVertical() const
    return self.uglySide.call('ritual_ZNK17QQuickRangeSlider10isVerticalEv')

  def touchDragThreshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::touchDragThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#touchDragThreshold
    """
    #  qreal QQuickRangeSlider::touchDragThreshold() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider18touchDragThresholdEv',
    )

  @overload(float)
  def valueAt(self, position: float) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::valueAt(qreal position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#valueAt

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  qreal QQuickRangeSlider::valueAt(qreal position) const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider7valueAtEd', position,
    )

  def isCrossingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSlider::isCrossingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#isCrossingEnabled
    """
    #  bool QQuickRangeSlider::isCrossingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider17isCrossingEnabledEv',
    )

  def handlesCrossed(self) -> bool:
    """
    Calls Qt's 'bool QQuickRangeSlider::handlesCrossed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#handlesCrossed
    """
    #  bool QQuickRangeSlider::handlesCrossed() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider14handlesCrossedEv',
    )

  def effectiveFirstValue(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::effectiveFirstValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#effectiveFirstValue
    """
    #  qreal QQuickRangeSlider::effectiveFirstValue() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider19effectiveFirstValueEv',
    )

  def effectiveSecondValue(self) -> float:
    """
    Calls Qt's 'qreal QQuickRangeSlider::effectiveSecondValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#effectiveSecondValue
    """
    #  qreal QQuickRangeSlider::effectiveSecondValue() const
    return self.uglySide.call(
        'ritual_ZNK17QQuickRangeSlider20effectiveSecondValueEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickRangeSlider::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickRangeSlider::accessibleRole() const
    ritual = 'ritual_ZNK17QQuickRangeSlider14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickRangeSlider14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setFrom(self, from_: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setFrom(qreal from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setFrom

    Parameters
    ----------

    from_ : float
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setFrom(qreal from)
    self.uglySide.call('ritual_ZN17QQuickRangeSlider7setFromEd', from_)

  @overload(float)
  def setTo(self, to: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setTo(qreal to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setTo

    Parameters
    ----------

    to : float
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setTo(qreal to)
    self.uglySide.call('ritual_ZN17QQuickRangeSlider5setToEd', to)

  @overload(float)
  def setStepSize(self, step: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setStepSize(qreal step)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setStepSize

    Parameters
    ----------

    step : float
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setStepSize(qreal step)
    self.uglySide.call('ritual_ZN17QQuickRangeSlider11setStepSizeEd', step)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickRangeSlider::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider11setSnapModeENS_8SnapModeE',
        mode.value,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickRangeSlider::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(float, float)
  def setValues(self, firstValue: float, secondValue: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setValues(qreal firstValue, qreal
    secondValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setValues

    Parameters
    ----------

    firstValue : float
      Passed on as it is.

    secondValue : float
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setValues(qreal firstValue, qreal secondValue)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider9setValuesEdd', firstValue, secondValue,
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setLive(bool live)
    self.uglySide.call('ritual_ZN17QQuickRangeSlider7setLiveEb', live)

  @overload(float)
  def setTouchDragThreshold(self, touchDragThreshold: float) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setTouchDragThreshold(qreal
    touchDragThreshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#setTouchDragThreshold

    Parameters
    ----------

    touchDragThreshold : float
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setTouchDragThreshold(qreal
    #      touchDragThreshold)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider21setTouchDragThresholdEd',
        touchDragThreshold,
    )

  @overload(bool)
  def setCrossingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::setCrossingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#setCrossingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickRangeSlider::setCrossingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider18setCrossingEnabledEb', enabled,
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
    'QQuickRangeSlider::QQuickRangeSlider(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#QQuickRangeSlider

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRangeSlider::QQuickRangeSlider(QQuickItem *parent)
    self._noteCreation(QQuickRangeSlider, lambda: Rituals.call(
        'ritual_ZN17QQuickRangeSliderC1EP10QQuickItem',
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

  def resetTouchDragThreshold(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::resetTouchDragThreshold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#resetTouchDragThreshold
    """
    #  void QQuickRangeSlider::resetTouchDragThreshold()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider23resetTouchDragThresholdEv',
    )

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#fromChanged
    """
    #  void QQuickRangeSlider::fromChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#toChanged
    """
    #  void QQuickRangeSlider::toChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider9toChangedEv')

  def stepSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::stepSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#stepSizeChanged
    """
    #  void QQuickRangeSlider::stepSizeChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider15stepSizeChangedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#snapModeChanged
    """
    #  void QQuickRangeSlider::snapModeChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider15snapModeChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#orientationChanged
    """
    #  void QQuickRangeSlider::orientationChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider18orientationChangedEv')

  def liveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::liveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#liveChanged
    """
    #  void QQuickRangeSlider::liveChanged()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider11liveChangedEv')

  def touchDragThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::touchDragThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#touchDragThresholdChanged
    """
    #  void QQuickRangeSlider::touchDragThresholdChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider25touchDragThresholdChangedEv',
    )

  def crossingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::crossingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#crossingEnabledChanged
    """
    #  void QQuickRangeSlider::crossingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider22crossingEnabledChangedEv',
    )

  def handlesCrossedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::handlesCrossedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#handlesCrossedChanged
    """
    #  void QQuickRangeSlider::handlesCrossedChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider21handlesCrossedChangedEv',
    )

  def effectiveFirstValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::effectiveFirstValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#effectiveFirstValueChanged
    """
    #  void QQuickRangeSlider::effectiveFirstValueChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider26effectiveFirstValueChangedEv',
    )

  def effectiveSecondValueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::effectiveSecondValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#effectiveSecondValueChanged
    """
    #  void QQuickRangeSlider::effectiveSecondValueChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider27effectiveSecondValueChangedEv',
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::hoverEnterEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::hoverEnterEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider15hoverEnterEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider15hoverEnterEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickRangeSlider13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickRangeSlider15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN17QQuickRangeSlider10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickRangeSlider10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#mirrorChange
    """
    #  void QQuickRangeSlider::mirrorChange()
    ritual = 'ritual_ZN17QQuickRangeSlider12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickRangeSlider12mirrorChangeEv'
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrangeslider.html#classBegin
    """
    #  void QQuickRangeSlider::classBegin()
    ritual = 'ritual_ZN17QQuickRangeSlider10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickRangeSlider10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#componentComplete
    """
    #  void QQuickRangeSlider::componentComplete()
    ritual = 'ritual_ZN17QQuickRangeSlider17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickRangeSlider17componentCompleteEv'
    self.uglySide.call(ritual)

  def updateHandleCrossing(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::updateHandleCrossing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#updateHandleCrossing
    """
    #  void QQuickRangeSlider::updateHandleCrossing()
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider20updateHandleCrossingEv',
    )

  @overload(QQuickRangeSliderNode)
  @overload(NoneType)
  def effectiveValueChange(
      self,
      node: Optional[QQuickRangeSliderNode],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRangeSlider::effectiveValueChange(QQuickRangeSliderNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#effectiveValueChange

    Parameters
    ----------

    node : Optional[QQuickRangeSliderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRangeSlider::effectiveValueChange(QQuickRangeSliderNode
    #      *node)
    self.uglySide.call(
        'ritual_ZN17QQuickRangeSlider20effectiveValueChangeEP21QQuickRangeS'
        'liderNode',
        self._addressOf(node),
    )

  def updateFocusOrder(self) -> None:
    """
    Calls Qt's 'void QQuickRangeSlider::updateFocusOrder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrangeslider.html#updateFocusOrder
    """
    #  void QQuickRangeSlider::updateFocusOrder()
    self.uglySide.call('ritual_ZN17QQuickRangeSlider16updateFocusOrderEv')
