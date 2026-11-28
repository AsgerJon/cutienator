"""
QQuickFlickable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickflickable_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFlickable to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPointF, QRectF, QTimerEvent
  from ..QtGui import QMouseEvent, QPointerEvent, QTouchEvent, QWheelEvent
  from . import QQuickFlickablePrivate, QQuickFlickableVisibleArea
  from . import QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickTransition = WAIT['QQuickTransition']
  QRectF = WAIT['QRectF']
  QTimerEvent = WAIT['QTimerEvent']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFlickable(QQuickItem):
  """
  The cute side of Qt's QQuickFlickable: a plain Python object standing in
  front of one C++ QQuickFlickable.

  It is built on the cute 'QQuickItem', as Qt's QQuickFlickable is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFlickable that has a ritual and that Python
  can call so far, 139 names in all: 'metaObject', 'tr', 'boundsBehavior',
  'setBoundsBehavior', 'boundsMovement', 'setBoundsMovement', 'rebound',
  'setRebound', 'contentWidth', 'setContentWidth', 'contentHeight',
  'setContentHeight', 'contentX', 'setContentX', 'contentY', 'setContentY',
  'topMargin', 'setTopMargin', 'bottomMargin', 'setBottomMargin',
  'leftMargin', 'setLeftMargin', 'rightMargin', 'setRightMargin', 'originY',
  'originX', 'isMoving', 'isMovingHorizontally', 'isMovingVertically',
  'isFlicking', 'isFlickingHorizontally', 'isFlickingVertically',
  'isDragging', 'isDraggingHorizontally', 'isDraggingVertically',
  'pressDelay', 'setPressDelay', 'maximumFlickVelocity',
  'setMaximumFlickVelocity', 'flickDeceleration', 'setFlickDeceleration',
  'isInteractive', 'setInteractive', 'horizontalVelocity',
  'verticalVelocity', 'isAtXEnd', 'isAtXBeginning', 'isAtYEnd',
  'isAtYBeginning', 'contentItem', 'flickableDirection',
  'setFlickableDirection', 'pixelAligned', 'setPixelAligned',
  'synchronousDrag', 'setSynchronousDrag', 'acceptedButtons',
  'setAcceptedButtons', 'horizontalOvershoot', 'verticalOvershoot',
  'resizeContent', 'returnToBounds', 'flick', 'cancelFlick',
  'positionViewAtChild', 'flickToChild', 'flickTo', 'contentWidthChanged',
  'contentHeightChanged', 'contentXChanged', 'contentYChanged',
  'topMarginChanged', 'bottomMarginChanged', 'leftMarginChanged',
  'rightMarginChanged', 'originYChanged', 'originXChanged', 'movingChanged',
  'movingHorizontallyChanged', 'movingVerticallyChanged', 'flickingChanged',
  'flickingHorizontallyChanged', 'flickingVerticallyChanged',
  'draggingChanged', 'draggingHorizontallyChanged',
  'draggingVerticallyChanged', 'horizontalVelocityChanged',
  'verticalVelocityChanged', 'isAtBoundaryChanged',
  'flickableDirectionChanged', 'interactiveChanged', 'boundsBehaviorChanged',
  'boundsMovementChanged', 'reboundChanged', 'maximumFlickVelocityChanged',
  'flickDecelerationChanged', 'pressDelayChanged', 'movementStarted',
  'movementEnded', 'flickStarted', 'flickEnded', 'dragStarted', 'dragEnded',
  'pixelAlignedChanged', 'synchronousDragChanged',
  'horizontalOvershootChanged', 'verticalOvershootChanged', 'atXEndChanged',
  'atYEndChanged', 'atXBeginningChanged', 'atYBeginningChanged',
  'acceptedButtonsChanged', 'childMouseEventFilter', 'mousePressEvent',
  'mouseMoveEvent', 'mouseReleaseEvent', 'touchEvent', 'wheelEvent',
  'timerEvent', 'visibleArea', 'movementStarting', 'movementEnding',
  'velocityTimelineCompleted', 'timelineCompleted', 'minXExtent',
  'minYExtent', 'maxXExtent', 'maxYExtent', 'vWidth', 'vHeight',
  'componentComplete', 'viewportMoved', 'geometryChange', 'mouseUngrabEvent',
  'filterPointerEvent', 'xflick', 'yflick', 'computePosition', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFlickable::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFlickable::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFlickable::~QQuickFlickable()': the destructor: Python never
    removes a C++ QQuickFlickable.
  - Qt's 'QQmlListProperty<QObject> QQuickFlickable::flickableData()': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickFlickable::flickableChildren()':
    gives a type Python has no way to take yet.
  - Qt's 'QQuickFlickable::QQuickFlickable(QQuickFlickablePrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickFlickablePrivate *QQuickFlickable::d_func() const':
    takes in Python what 'QQuickFlickablePrivate *QQuickFlickable::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 152 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFlickable is created at the first use, not by
    'QQuickFlickable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFlickable.
  - Qt tells when it has removed the C++ QQuickFlickable. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFlickable that has no cute function yet,
    'flickableChildren', 'flickableData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickFlickable, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BoundsBehaviorFlag(CuteFlags):
    """
    The flags enum 'QQuickFlickable::BoundsBehaviorFlag' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QQuickFlickable::BoundsBehavior'.
    """

    StopAtBounds = 0x0
    DragOverBounds = 0x1
    OvershootBounds = 0x2
    DragAndOvershootBounds = 0x3

  BoundsBehavior = BoundsBehaviorFlag

  class BoundsMovement(CuteNum):
    """
    The enum 'QQuickFlickable::BoundsMovement' of Qt, with the 1 names Qt
    gives in it.
    """

    FollowBoundsBehavior = Kee[int](1)

  class FlickableDirection(CuteNum):
    """
    The enum 'QQuickFlickable::FlickableDirection' of Qt, with the 5 names Qt
    gives in it.
    """

    AutoFlickDirection = Kee[int](0)
    HorizontalFlick = Kee[int](1)
    VerticalFlick = Kee[int](2)
    HorizontalAndVerticalFlick = Kee[int](3)
    AutoFlickIfNeeded = Kee[int](12)

  class PositionModeFlag(CuteFlags):
    """
    The flags enum 'QQuickFlickable::PositionModeFlag' of Qt, with the 9
    names Qt gives in it. Qt names the type of its combinations
    'QQuickFlickable::PositionMode'.
    """

    AlignLeft = 0x1
    AlignRight = 0x2
    AlignHCenter = 0x4
    AlignTop = 0x20
    AlignBottom = 0x40
    AlignVCenter = 0x80
    AlignCenter = 0x84
    Visible = 0x1000
    Contain = 0x2000

  PositionMode = PositionModeFlag

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
    Calls Qt's 'QString QQuickFlickable::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#tr

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
    #  QString QQuickFlickable::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickFlickable2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFlickable'

  #  A C++ QQuickFlickable Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFlickable'

  #  The functions Qt calls itself that QQuickFlickable is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setContentX': (
          ('_ZN15QQuickFlickable11setContentXEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setContentY': (
          ('_ZN15QQuickFlickable11setContentYEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'originY': (
          ('_ZNK15QQuickFlickable7originYEv',
           ('double', 'number', ''),
           ()),
      ),
      'originX': (
          ('_ZNK15QQuickFlickable7originXEv',
           ('double', 'number', ''),
           ()),
      ),
      'minXExtent': (
          ('_ZNK15QQuickFlickable10minXExtentEv',
           ('double', 'number', ''),
           ()),
      ),
      'minYExtent': (
          ('_ZNK15QQuickFlickable10minYExtentEv',
           ('double', 'number', ''),
           ()),
      ),
      'maxXExtent': (
          ('_ZNK15QQuickFlickable10maxXExtentEv',
           ('double', 'number', ''),
           ()),
      ),
      'maxYExtent': (
          ('_ZNK15QQuickFlickable10maxYExtentEv',
           ('double', 'number', ''),
           ()),
      ),
      'viewportMoved': (
          ('_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11OrientationEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.Orientation'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFlickable::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFlickable::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickFlickable10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundsBehavior(self) -> BoundsBehavior:
    """
    Calls Qt's 'BoundsBehavior QQuickFlickable::boundsBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#boundsBehavior

    Returns
    -------

    BoundsBehavior
      The value standing for the combination Qt gave back.
    """
    #  BoundsBehavior QQuickFlickable::boundsBehavior() const
    return QQuickFlickable.BoundsBehavior(self.uglySide.call(
        'ritual_ZNK15QQuickFlickable14boundsBehaviorEv',
    ))

  def boundsMovement(self) -> BoundsMovement:
    """
    Calls Qt's 'BoundsMovement QQuickFlickable::boundsMovement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#boundsMovement

    Returns
    -------

    BoundsMovement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BoundsMovement(number)'
      gives.
    """
    #  BoundsMovement QQuickFlickable::boundsMovement() const
    return QQuickFlickable.BoundsMovement(self.uglySide.call(
        'ritual_ZNK15QQuickFlickable14boundsMovementEv',
    ))

  def rebound(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickFlickable::rebound() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#rebound

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickFlickable::rebound() const
    address = self.uglySide.call('ritual_ZNK15QQuickFlickable7reboundEv')
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def contentWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::contentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#contentWidth
    """
    #  qreal QQuickFlickable::contentWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable12contentWidthEv')

  def contentHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::contentHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#contentHeight
    """
    #  qreal QQuickFlickable::contentHeight() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable13contentHeightEv')

  def contentX(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::contentX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#contentX
    """
    #  qreal QQuickFlickable::contentX() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable8contentXEv')

  def contentY(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::contentY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#contentY
    """
    #  qreal QQuickFlickable::contentY() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable8contentYEv')

  def topMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::topMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#topMargin
    """
    #  qreal QQuickFlickable::topMargin() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable9topMarginEv')

  def bottomMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::bottomMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#bottomMargin
    """
    #  qreal QQuickFlickable::bottomMargin() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable12bottomMarginEv')

  def leftMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::leftMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#leftMargin
    """
    #  qreal QQuickFlickable::leftMargin() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable10leftMarginEv')

  def rightMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::rightMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#rightMargin
    """
    #  qreal QQuickFlickable::rightMargin() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable11rightMarginEv')

  def originY(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::originY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#originY
    """
    #  qreal QQuickFlickable::originY() const
    ritual = 'ritual_ZNK15QQuickFlickable7originYEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable7originYEv'
    return self.uglySide.call(ritual)

  def originX(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::originX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#originX
    """
    #  qreal QQuickFlickable::originX() const
    ritual = 'ritual_ZNK15QQuickFlickable7originXEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable7originXEv'
    return self.uglySide.call(ritual)

  def isMoving(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isMoving() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isMoving
    """
    #  bool QQuickFlickable::isMoving() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable8isMovingEv')

  def isMovingHorizontally(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isMovingHorizontally() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isMovingHorizontally
    """
    #  bool QQuickFlickable::isMovingHorizontally() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable20isMovingHorizontallyEv',
    )

  def isMovingVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isMovingVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isMovingVertically
    """
    #  bool QQuickFlickable::isMovingVertically() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable18isMovingVerticallyEv',
    )

  def isFlicking(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isFlicking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isFlicking
    """
    #  bool QQuickFlickable::isFlicking() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable10isFlickingEv')

  def isFlickingHorizontally(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isFlickingHorizontally() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isFlickingHorizontally
    """
    #  bool QQuickFlickable::isFlickingHorizontally() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable22isFlickingHorizontallyEv',
    )

  def isFlickingVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isFlickingVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isFlickingVertically
    """
    #  bool QQuickFlickable::isFlickingVertically() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable20isFlickingVerticallyEv',
    )

  def isDragging(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isDragging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isDragging
    """
    #  bool QQuickFlickable::isDragging() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable10isDraggingEv')

  def isDraggingHorizontally(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isDraggingHorizontally() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isDraggingHorizontally
    """
    #  bool QQuickFlickable::isDraggingHorizontally() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable22isDraggingHorizontallyEv',
    )

  def isDraggingVertically(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isDraggingVertically() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isDraggingVertically
    """
    #  bool QQuickFlickable::isDraggingVertically() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable20isDraggingVerticallyEv',
    )

  def pressDelay(self) -> int:
    """
    Calls Qt's 'int QQuickFlickable::pressDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#pressDelay
    """
    #  int QQuickFlickable::pressDelay() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable10pressDelayEv')

  def maximumFlickVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::maximumFlickVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#maximumFlickVelocity
    """
    #  qreal QQuickFlickable::maximumFlickVelocity() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable20maximumFlickVelocityEv',
    )

  def flickDeceleration(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::flickDeceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickDeceleration
    """
    #  qreal QQuickFlickable::flickDeceleration() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable17flickDecelerationEv',
    )

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isInteractive
    """
    #  bool QQuickFlickable::isInteractive() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable13isInteractiveEv')

  def horizontalVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::horizontalVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#horizontalVelocity
    """
    #  qreal QQuickFlickable::horizontalVelocity() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable18horizontalVelocityEv',
    )

  def verticalVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::verticalVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#verticalVelocity
    """
    #  qreal QQuickFlickable::verticalVelocity() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable16verticalVelocityEv',
    )

  def isAtXEnd(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isAtXEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isAtXEnd
    """
    #  bool QQuickFlickable::isAtXEnd() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable8isAtXEndEv')

  def isAtXBeginning(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isAtXBeginning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isAtXBeginning
    """
    #  bool QQuickFlickable::isAtXBeginning() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable14isAtXBeginningEv',
    )

  def isAtYEnd(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isAtYEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#isAtYEnd
    """
    #  bool QQuickFlickable::isAtYEnd() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable8isAtYEndEv')

  def isAtYBeginning(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::isAtYBeginning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isAtYBeginning
    """
    #  bool QQuickFlickable::isAtYBeginning() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable14isAtYBeginningEv',
    )

  def contentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickFlickable::contentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#contentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickFlickable::contentItem() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickFlickable11contentItemEv',
    )
    return QQuickItem._cuteAt(address)

  def flickableDirection(self) -> FlickableDirection:
    """
    Calls Qt's 'FlickableDirection QQuickFlickable::flickableDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickableDirection

    Returns
    -------

    FlickableDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'FlickableDirection(number)' gives.
    """
    #  FlickableDirection QQuickFlickable::flickableDirection() const
    return QQuickFlickable.FlickableDirection(self.uglySide.call(
        'ritual_ZNK15QQuickFlickable18flickableDirectionEv',
    ))

  def pixelAligned(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::pixelAligned() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#pixelAligned
    """
    #  bool QQuickFlickable::pixelAligned() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable12pixelAlignedEv')

  def synchronousDrag(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::synchronousDrag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#synchronousDrag
    """
    #  bool QQuickFlickable::synchronousDrag() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable15synchronousDragEv',
    )

  def acceptedButtons(self) -> Qt.MouseButtons:
    """
    Calls Qt's 'Qt::MouseButtons QQuickFlickable::acceptedButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#acceptedButtons

    Returns
    -------

    Qt.MouseButtons
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseButtons QQuickFlickable::acceptedButtons() const
    return Qt.MouseButtons(self.uglySide.call(
        'ritual_ZNK15QQuickFlickable15acceptedButtonsEv',
    ))

  def horizontalOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::horizontalOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#horizontalOvershoot
    """
    #  qreal QQuickFlickable::horizontalOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable19horizontalOvershootEv',
    )

  def verticalOvershoot(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::verticalOvershoot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#verticalOvershoot
    """
    #  qreal QQuickFlickable::verticalOvershoot() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickFlickable17verticalOvershootEv',
    )

  def minXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::minXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#minXExtent
    """
    #  qreal QQuickFlickable::minXExtent() const
    ritual = 'ritual_ZNK15QQuickFlickable10minXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable10minXExtentEv'
    return self.uglySide.call(ritual)

  def minYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::minYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#minYExtent
    """
    #  qreal QQuickFlickable::minYExtent() const
    ritual = 'ritual_ZNK15QQuickFlickable10minYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable10minYExtentEv'
    return self.uglySide.call(ritual)

  def maxXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::maxXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#maxXExtent
    """
    #  qreal QQuickFlickable::maxXExtent() const
    ritual = 'ritual_ZNK15QQuickFlickable10maxXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable10maxXExtentEv'
    return self.uglySide.call(ritual)

  def maxYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::maxYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#maxYExtent
    """
    #  qreal QQuickFlickable::maxYExtent() const
    ritual = 'ritual_ZNK15QQuickFlickable10maxYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickFlickable10maxYExtentEv'
    return self.uglySide.call(ritual)

  def vWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::vWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#vWidth
    """
    #  qreal QQuickFlickable::vWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable6vWidthEv')

  def vHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickFlickable::vHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#vHeight
    """
    #  qreal QQuickFlickable::vHeight() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable7vHeightEv')

  def xflick(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::xflick() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#xflick
    """
    #  bool QQuickFlickable::xflick() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable6xflickEv')

  def yflick(self) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::yflick() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#yflick
    """
    #  bool QQuickFlickable::yflick() const
    return self.uglySide.call('ritual_ZNK15QQuickFlickable6yflickEv')

  @overload(QPointF, QRectF, PositionMode)
  @overload(QPointF, QRectF, PositionMode, QPointF)
  def computePosition(
      self,
      currentPosition: QPointF,
      itemRect: QRectF,
      mode: PositionMode,
      offset: Optional[QPointF] = None,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickFlickable::computePosition(QPointF
    currentPosition, QRectF itemRect, PositionMode mode, const QPointF
    &offset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#computePosition

    Parameters
    ----------

    currentPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    itemRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    mode : PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickFlickable::computePosition(QPointF currentPosition,
    #      QRectF itemRect, PositionMode mode, const QPointF &offset) const
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    address = self.uglySide.call(
        'ritual_ZNK15QQuickFlickable15computePositionE7QPointF6QRectF6QFlag'
        'sINS_16PositionModeFlagEERKS0_',
        self._valueOf(currentPosition, 'QPointF'), self._valueOf(itemRect),
        mode.value, self._valueOf(offset, 'QPointF'),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BoundsBehavior)
  def setBoundsBehavior(self, a0: BoundsBehavior) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setBoundsBehavior(BoundsBehavior a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setBoundsBehavior

    Parameters
    ----------

    a0 : BoundsBehavior
      Passed on as its number.
    """
    #  void QQuickFlickable::setBoundsBehavior(BoundsBehavior a0)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable17setBoundsBehaviorE6QFlagsINS_18BoundsB'
        'ehaviorFlagEE',
        a0.value,
    )

  @overload(BoundsMovement)
  def setBoundsMovement(self, movement: BoundsMovement) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setBoundsMovement(BoundsMovement
    movement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setBoundsMovement

    Parameters
    ----------

    movement : BoundsMovement
      Passed on as its number.
    """
    #  void QQuickFlickable::setBoundsMovement(BoundsMovement movement)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable17setBoundsMovementENS_14BoundsMovementE',
        movement.value,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setRebound(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setRebound(QQuickTransition
    *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setRebound

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::setRebound(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable10setReboundEP16QQuickTransition',
        self._addressOf(transition),
    )

  @overload(float)
  def setContentWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setContentWidth(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setContentWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setContentWidth(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickFlickable15setContentWidthEd', a0)

  @overload(float)
  def setContentHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setContentHeight(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setContentHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setContentHeight(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickFlickable16setContentHeightEd', a0)

  @overload(float)
  def setContentX(self, pos: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setContentX(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setContentX

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setContentX(qreal pos)
    ritual = 'ritual_ZN15QQuickFlickable11setContentXEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable11setContentXEd'
    self.uglySide.call(ritual, pos)

  @overload(float)
  def setContentY(self, pos: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setContentY(qreal pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setContentY

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setContentY(qreal pos)
    ritual = 'ritual_ZN15QQuickFlickable11setContentYEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable11setContentYEd'
    self.uglySide.call(ritual, pos)

  @overload(float)
  def setTopMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setTopMargin(qreal m)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setTopMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setTopMargin(qreal m)
    self.uglySide.call('ritual_ZN15QQuickFlickable12setTopMarginEd', m)

  @overload(float)
  def setBottomMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setBottomMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setBottomMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setBottomMargin(qreal m)
    self.uglySide.call('ritual_ZN15QQuickFlickable15setBottomMarginEd', m)

  @overload(float)
  def setLeftMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setLeftMargin(qreal m)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setLeftMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setLeftMargin(qreal m)
    self.uglySide.call('ritual_ZN15QQuickFlickable13setLeftMarginEd', m)

  @overload(float)
  def setRightMargin(self, m: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setRightMargin(qreal m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setRightMargin

    Parameters
    ----------

    m : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setRightMargin(qreal m)
    self.uglySide.call('ritual_ZN15QQuickFlickable14setRightMarginEd', m)

  @overload(int)
  def setPressDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setPressDelay(int delay)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#setPressDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickFlickable::setPressDelay(int delay)
    self.uglySide.call('ritual_ZN15QQuickFlickable13setPressDelayEi', delay)

  @overload(float)
  def setMaximumFlickVelocity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setMaximumFlickVelocity(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setMaximumFlickVelocity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setMaximumFlickVelocity(qreal a0)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable23setMaximumFlickVelocityEd', a0,
    )

  @overload(float)
  def setFlickDeceleration(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setFlickDeceleration(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setFlickDeceleration

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickFlickable::setFlickDeceleration(qreal a0)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable20setFlickDecelerationEd', a0,
    )

  @overload(bool)
  def setInteractive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setInteractive(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setInteractive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickFlickable::setInteractive(bool a0)
    self.uglySide.call('ritual_ZN15QQuickFlickable14setInteractiveEb', a0)

  @overload(FlickableDirection)
  def setFlickableDirection(self, a0: FlickableDirection) -> None:
    """
    Calls Qt's 'void
    QQuickFlickable::setFlickableDirection(FlickableDirection a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setFlickableDirection

    Parameters
    ----------

    a0 : FlickableDirection
      Passed on as its number.
    """
    #  void QQuickFlickable::setFlickableDirection(FlickableDirection a0)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable21setFlickableDirectionENS_18FlickableDi'
        'rectionE',
        a0.value,
    )

  @overload(bool)
  def setPixelAligned(self, align: bool) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setPixelAligned(bool align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setPixelAligned

    Parameters
    ----------

    align : bool
      Passed on as it is.
    """
    #  void QQuickFlickable::setPixelAligned(bool align)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable15setPixelAlignedEb', align,
    )

  @overload(bool)
  def setSynchronousDrag(self, v: bool) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setSynchronousDrag(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setSynchronousDrag

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQuickFlickable::setSynchronousDrag(bool v)
    self.uglySide.call('ritual_ZN15QQuickFlickable18setSynchronousDragEb', v)

  @overload(Qt.MouseButtons)
  def setAcceptedButtons(self, buttons: Qt.MouseButtons) -> None:
    """
    Calls Qt's 'void QQuickFlickable::setAcceptedButtons(Qt::MouseButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#setAcceptedButtons

    Parameters
    ----------

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  void QQuickFlickable::setAcceptedButtons(Qt::MouseButtons buttons)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable18setAcceptedButtonsE6QFlagsIN2Qt11Mouse'
        'ButtonEE',
        buttons.value,
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
    'QQuickFlickable::QQuickFlickable(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#QQuickFlickable

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFlickable::QQuickFlickable(QQuickItem *parent)
    self._noteCreation(QQuickFlickable, lambda: Rituals.call(
        'ritual_ZN15QQuickFlickableC1EP10QQuickItem',
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

  @overload(float, float, QPointF)
  def resizeContent(self, w: float, h: float, center: QPointF) -> None:
    """
    Calls Qt's 'void QQuickFlickable::resizeContent(qreal w, qreal h, QPointF
    center)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#resizeContent

    Parameters
    ----------

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickFlickable::resizeContent(qreal w, qreal h, QPointF center)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable13resizeContentEdd7QPointF',
        w, h, self._valueOf(center, 'QPointF'),
    )

  def returnToBounds(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::returnToBounds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#returnToBounds
    """
    #  void QQuickFlickable::returnToBounds()
    self.uglySide.call('ritual_ZN15QQuickFlickable14returnToBoundsEv')

  @overload(float, float)
  def flick(self, xVelocity: float, yVelocity: float) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flick(qreal xVelocity, qreal
    yVelocity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#flick

    Parameters
    ----------

    xVelocity : float
      Passed on as it is.

    yVelocity : float
      Passed on as it is.
    """
    #  void QQuickFlickable::flick(qreal xVelocity, qreal yVelocity)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable5flickEdd', xVelocity, yVelocity,
    )

  def cancelFlick(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::cancelFlick()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#cancelFlick
    """
    #  void QQuickFlickable::cancelFlick()
    self.uglySide.call('ritual_ZN15QQuickFlickable11cancelFlickEv')

  @overload(QQuickItem, PositionMode)
  @overload(NoneType, PositionMode)
  @overload(QQuickItem, PositionMode, QPointF)
  @overload(NoneType, PositionMode, QPointF)
  def positionViewAtChild(
      self,
      child: Optional[QQuickItem],
      mode: PositionMode,
      offset: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickable::positionViewAtChild(QQuickItem *child,
    PositionMode mode, const QPointF &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#positionViewAtChild

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QQuickFlickable::positionViewAtChild(QQuickItem *child,
    #      PositionMode mode, const QPointF &offset)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable19positionViewAtChildEP10QQuickItem6QFla'
        'gsINS_16PositionModeFlagEERK7QPointF',
        self._addressOf(child), mode.value, self._valueOf(offset, 'QPointF'),
    )

  @overload(QQuickItem, PositionMode)
  @overload(NoneType, PositionMode)
  @overload(QQuickItem, PositionMode, QPointF)
  @overload(NoneType, PositionMode, QPointF)
  def flickToChild(
      self,
      child: Optional[QQuickItem],
      mode: PositionMode,
      offset: Optional[QPointF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickToChild(QQuickItem *child,
    PositionMode mode, const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#flickToChild

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.
    """
    #  void QQuickFlickable::flickToChild(QQuickItem *child, PositionMode
    #      mode, const QPointF &offset)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable12flickToChildEP10QQuickItem6QFlagsINS_1'
        '6PositionModeFlagEERK7QPointF',
        self._addressOf(child), mode.value, self._valueOf(offset, 'QPointF'),
    )

  @overload(QPointF)
  def flickTo(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickTo(const QPointF &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#flickTo

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickFlickable::flickTo(const QPointF &position)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable7flickToERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  def contentWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::contentWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#contentWidthChanged
    """
    #  void QQuickFlickable::contentWidthChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19contentWidthChangedEv')

  def contentHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::contentHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#contentHeightChanged
    """
    #  void QQuickFlickable::contentHeightChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable20contentHeightChangedEv')

  def contentXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::contentXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#contentXChanged
    """
    #  void QQuickFlickable::contentXChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable15contentXChangedEv')

  def contentYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::contentYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#contentYChanged
    """
    #  void QQuickFlickable::contentYChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable15contentYChangedEv')

  def topMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::topMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#topMarginChanged
    """
    #  void QQuickFlickable::topMarginChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable16topMarginChangedEv')

  def bottomMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::bottomMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#bottomMarginChanged
    """
    #  void QQuickFlickable::bottomMarginChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19bottomMarginChangedEv')

  def leftMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::leftMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#leftMarginChanged
    """
    #  void QQuickFlickable::leftMarginChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable17leftMarginChangedEv')

  def rightMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::rightMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#rightMarginChanged
    """
    #  void QQuickFlickable::rightMarginChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable18rightMarginChangedEv')

  def originYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::originYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#originYChanged
    """
    #  void QQuickFlickable::originYChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable14originYChangedEv')

  def originXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::originXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#originXChanged
    """
    #  void QQuickFlickable::originXChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable14originXChangedEv')

  def movingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#movingChanged
    """
    #  void QQuickFlickable::movingChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable13movingChangedEv')

  def movingHorizontallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movingHorizontallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movingHorizontallyChanged
    """
    #  void QQuickFlickable::movingHorizontallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25movingHorizontallyChangedEv',
    )

  def movingVerticallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movingVerticallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movingVerticallyChanged
    """
    #  void QQuickFlickable::movingVerticallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable23movingVerticallyChangedEv',
    )

  def flickingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickingChanged
    """
    #  void QQuickFlickable::flickingChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable15flickingChangedEv')

  def flickingHorizontallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickingHorizontallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickingHorizontallyChanged
    """
    #  void QQuickFlickable::flickingHorizontallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable27flickingHorizontallyChangedEv',
    )

  def flickingVerticallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickingVerticallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickingVerticallyChanged
    """
    #  void QQuickFlickable::flickingVerticallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25flickingVerticallyChangedEv',
    )

  def draggingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::draggingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#draggingChanged
    """
    #  void QQuickFlickable::draggingChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable15draggingChangedEv')

  def draggingHorizontallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::draggingHorizontallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#draggingHorizontallyChanged
    """
    #  void QQuickFlickable::draggingHorizontallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable27draggingHorizontallyChangedEv',
    )

  def draggingVerticallyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::draggingVerticallyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#draggingVerticallyChanged
    """
    #  void QQuickFlickable::draggingVerticallyChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25draggingVerticallyChangedEv',
    )

  def horizontalVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::horizontalVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#horizontalVelocityChanged
    """
    #  void QQuickFlickable::horizontalVelocityChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25horizontalVelocityChangedEv',
    )

  def verticalVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::verticalVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#verticalVelocityChanged
    """
    #  void QQuickFlickable::verticalVelocityChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable23verticalVelocityChangedEv',
    )

  def isAtBoundaryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::isAtBoundaryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#isAtBoundaryChanged
    """
    #  void QQuickFlickable::isAtBoundaryChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19isAtBoundaryChangedEv')

  def flickableDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickableDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickableDirectionChanged
    """
    #  void QQuickFlickable::flickableDirectionChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25flickableDirectionChangedEv',
    )

  def interactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::interactiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#interactiveChanged
    """
    #  void QQuickFlickable::interactiveChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable18interactiveChangedEv')

  def boundsBehaviorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::boundsBehaviorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#boundsBehaviorChanged
    """
    #  void QQuickFlickable::boundsBehaviorChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable21boundsBehaviorChangedEv')

  def boundsMovementChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::boundsMovementChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#boundsMovementChanged
    """
    #  void QQuickFlickable::boundsMovementChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable21boundsMovementChangedEv')

  def reboundChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::reboundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#reboundChanged
    """
    #  void QQuickFlickable::reboundChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable14reboundChangedEv')

  def maximumFlickVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::maximumFlickVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#maximumFlickVelocityChanged
    """
    #  void QQuickFlickable::maximumFlickVelocityChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable27maximumFlickVelocityChangedEv',
    )

  def flickDecelerationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickDecelerationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#flickDecelerationChanged
    """
    #  void QQuickFlickable::flickDecelerationChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable24flickDecelerationChangedEv',
    )

  def pressDelayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::pressDelayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#pressDelayChanged
    """
    #  void QQuickFlickable::pressDelayChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable17pressDelayChangedEv')

  def movementStarted(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movementStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movementStarted
    """
    #  void QQuickFlickable::movementStarted()
    self.uglySide.call('ritual_ZN15QQuickFlickable15movementStartedEv')

  def movementEnded(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movementEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#movementEnded
    """
    #  void QQuickFlickable::movementEnded()
    self.uglySide.call('ritual_ZN15QQuickFlickable13movementEndedEv')

  def flickStarted(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#flickStarted
    """
    #  void QQuickFlickable::flickStarted()
    self.uglySide.call('ritual_ZN15QQuickFlickable12flickStartedEv')

  def flickEnded(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::flickEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#flickEnded
    """
    #  void QQuickFlickable::flickEnded()
    self.uglySide.call('ritual_ZN15QQuickFlickable10flickEndedEv')

  def dragStarted(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::dragStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#dragStarted
    """
    #  void QQuickFlickable::dragStarted()
    self.uglySide.call('ritual_ZN15QQuickFlickable11dragStartedEv')

  def dragEnded(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::dragEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#dragEnded
    """
    #  void QQuickFlickable::dragEnded()
    self.uglySide.call('ritual_ZN15QQuickFlickable9dragEndedEv')

  def pixelAlignedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::pixelAlignedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#pixelAlignedChanged
    """
    #  void QQuickFlickable::pixelAlignedChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19pixelAlignedChangedEv')

  def synchronousDragChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::synchronousDragChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#synchronousDragChanged
    """
    #  void QQuickFlickable::synchronousDragChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable22synchronousDragChangedEv',
    )

  def horizontalOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::horizontalOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#horizontalOvershootChanged
    """
    #  void QQuickFlickable::horizontalOvershootChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable26horizontalOvershootChangedEv',
    )

  def verticalOvershootChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::verticalOvershootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#verticalOvershootChanged
    """
    #  void QQuickFlickable::verticalOvershootChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable24verticalOvershootChangedEv',
    )

  def atXEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::atXEndChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#atXEndChanged
    """
    #  void QQuickFlickable::atXEndChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable13atXEndChangedEv')

  def atYEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::atYEndChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#atYEndChanged
    """
    #  void QQuickFlickable::atYEndChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable13atYEndChangedEv')

  def atXBeginningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::atXBeginningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#atXBeginningChanged
    """
    #  void QQuickFlickable::atXBeginningChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19atXBeginningChangedEv')

  def atYBeginningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::atYBeginningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#atYBeginningChanged
    """
    #  void QQuickFlickable::atYBeginningChanged()
    self.uglySide.call('ritual_ZN15QQuickFlickable19atYBeginningChangedEv')

  def acceptedButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::acceptedButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#acceptedButtonsChanged
    """
    #  void QQuickFlickable::acceptedButtonsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable22acceptedButtonsChangedEv',
    )

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#childMouseEventFilter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFlickable::childMouseEventFilter(QQuickItem *a0, QEvent
    #      *a1)
    ritual = (
        'ritual_ZN15QQuickFlickable21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickFlickable21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickFlickable15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickFlickable14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickFlickable17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::touchEvent(QTouchEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable10touchEventEP11QTouchEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickFlickable::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFlickable::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN15QQuickFlickable10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def visibleArea(self) -> Optional[QQuickFlickableVisibleArea]:
    """
    Calls Qt's 'QQuickFlickableVisibleArea *QQuickFlickable::visibleArea()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#visibleArea

    Returns
    -------

    Optional[QQuickFlickableVisibleArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlickableVisibleArea *QQuickFlickable::visibleArea()
    address = self.uglySide.call('ritual_ZN15QQuickFlickable11visibleAreaEv')
    from . import QQuickFlickableVisibleArea
    return QQuickFlickableVisibleArea._cuteAt(address)

  def movementStarting(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movementStarting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movementStarting
    """
    #  void QQuickFlickable::movementStarting()
    self.uglySide.call('ritual_ZN15QQuickFlickable16movementStartingEv')

  @overload()
  def movementEnding(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movementEnding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movementEnding
    """
    #  void QQuickFlickable::movementEnding()
    self.uglySide.call('ritual_ZN15QQuickFlickable14movementEndingEv')

  @overload(bool, bool)
  def movementEnding(
      self,
      hMovementEnding: bool,
      vMovementEnding: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickFlickable::movementEnding(bool hMovementEnding,
    bool vMovementEnding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#movementEnding

    Parameters
    ----------

    hMovementEnding : bool
      Passed on as it is.

    vMovementEnding : bool
      Passed on as it is.
    """
    #  void QQuickFlickable::movementEnding(bool hMovementEnding, bool
    #      vMovementEnding)
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable14movementEndingEbb',
        hMovementEnding, vMovementEnding,
    )

  def velocityTimelineCompleted(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::velocityTimelineCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#velocityTimelineCompleted
    """
    #  void QQuickFlickable::velocityTimelineCompleted()
    self.uglySide.call(
        'ritual_ZN15QQuickFlickable25velocityTimelineCompletedEv',
    )

  def timelineCompleted(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::timelineCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#timelineCompleted
    """
    #  void QQuickFlickable::timelineCompleted()
    self.uglySide.call('ritual_ZN15QQuickFlickable17timelineCompletedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#componentComplete
    """
    #  void QQuickFlickable::componentComplete()
    ritual = 'ritual_ZN15QQuickFlickable17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(Qt.Orientations)
  def viewportMoved(self, orient: Qt.Orientations) -> None:
    """
    Calls Qt's 'void QQuickFlickable::viewportMoved(Qt::Orientations
    orient)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#viewportMoved

    Parameters
    ----------

    orient : Qt.Orientations
      Passed on as its number.
    """
    #  void QQuickFlickable::viewportMoved(Qt::Orientations orient)
    ritual = (
        'ritual_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11Orientatio'
        'nEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickFlickable13viewportMovedE6QFlagsIN2Qt11Orie'
          'ntationEE')
    self.uglySide.call(ritual, orient.value)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickFlickable::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickFlickable::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickFlickable14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickFlickable::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#mouseUngrabEvent
    """
    #  void QQuickFlickable::mouseUngrabEvent()
    ritual = 'ritual_ZN15QQuickFlickable16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickFlickable16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QPointerEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QPointerEvent)
  @overload(NoneType, NoneType)
  def filterPointerEvent(
      self,
      receiver: Optional[QQuickItem],
      event: Optional[QPointerEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickFlickable::filterPointerEvent(QQuickItem
    *receiver, QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickflickable.html#filterPointerEvent

    Parameters
    ----------

    receiver : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickFlickable::filterPointerEvent(QQuickItem *receiver,
    #      QPointerEvent *event)
    return self.uglySide.call(
        'ritual_ZN15QQuickFlickable18filterPointerEventEP10QQuickItemP13QPo'
        'interEvent',
        self._addressOf(receiver), self._addressOf(event),
    )

  def d_func(self) -> Optional[QQuickFlickablePrivate]:
    """
    Calls Qt's 'QQuickFlickablePrivate *QQuickFlickable::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickflickable.html#d_func

    Returns
    -------

    Optional[QQuickFlickablePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlickablePrivate *QQuickFlickable::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickFlickable6d_funcEv')
    from . import QQuickFlickablePrivate
    return QQuickFlickablePrivate._cuteAt(address)

  @staticmethod
  def flickableChildren(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickFlickable::flickableChildren()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickFlickable.flickableChildren' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> "
        "QQuickFlickable::flickableChildren()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def flickableData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickFlickable::flickableData()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickFlickable.flickableData' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickFlickable::flickableData()': "
        "gives a type Python has no way to take yet.")
