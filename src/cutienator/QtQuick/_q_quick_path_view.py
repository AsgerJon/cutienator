"""
QQuickPathView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from ..QtGui import QMouseEvent
  from ..QtQml import QQmlComponent
  from . import QQuickPath, QQuickPathViewAttached, QQuickPathViewPrivate
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickPath = WAIT['QQuickPath']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathView(QQuickItem):
  """
  The cute side of Qt's QQuickPathView: a plain Python object standing in
  front of one C++ QQuickPathView.

  It is built on the cute 'QQuickItem', as Qt's QQuickPathView is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathView that has a ritual and that Python can
  call so far, 99 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'path', 'setPath', 'currentIndex', 'setCurrentIndex', 'currentItem',
  'offset', 'setOffset', 'highlight', 'setHighlight', 'highlightItem',
  'highlightRangeMode', 'setHighlightRangeMode', 'preferredHighlightBegin',
  'setPreferredHighlightBegin', 'preferredHighlightEnd',
  'setPreferredHighlightEnd', 'highlightMoveDuration',
  'setHighlightMoveDuration', 'dragMargin', 'setDragMargin',
  'flickDeceleration', 'setFlickDeceleration', 'maximumFlickVelocity',
  'setMaximumFlickVelocity', 'isInteractive', 'setInteractive', 'isMoving',
  'isFlicking', 'isDragging', 'count', 'delegate', 'setDelegate',
  'pathItemCount', 'setPathItemCount', 'resetPathItemCount',
  'cacheItemCount', 'setCacheItemCount', 'snapMode', 'setSnapMode',
  'movementDirection', 'setMovementDirection', 'positionViewAtIndex',
  'indexAt', 'itemAt', 'itemAtIndex', 'qmlAttachedProperties',
  'incrementCurrentIndex', 'decrementCurrentIndex', 'currentIndexChanged',
  'currentItemChanged', 'offsetChanged', 'modelChanged', 'countChanged',
  'pathChanged', 'preferredHighlightBeginChanged',
  'preferredHighlightEndChanged', 'highlightRangeModeChanged',
  'dragMarginChanged', 'snapPositionChanged', 'delegateChanged',
  'pathItemCountChanged', 'maximumFlickVelocityChanged',
  'flickDecelerationChanged', 'interactiveChanged', 'movingChanged',
  'flickingChanged', 'draggingChanged', 'highlightChanged',
  'highlightItemChanged', 'highlightMoveDurationChanged', 'movementStarted',
  'movementEnded', 'movementDirectionChanged', 'flickStarted', 'flickEnded',
  'dragStarted', 'dragEnded', 'snapModeChanged', 'cacheItemCountChanged',
  'updatePolish', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'childMouseEventFilter', 'mouseUngrabEvent', 'componentComplete', 'refill',
  'ticked', 'movementEnding', 'modelUpdated', 'createdItem', 'initItem',
  'destroyingItem', 'pathUpdated', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPathView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickPathView::~QQuickPathView()': the destructor: Python never
    removes a C++ QQuickPathView.
  - Qt's 'const QQuickPathViewPrivate *QQuickPathView::d_func() const': takes
    in Python what 'QQuickPathViewPrivate *QQuickPathView::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 109 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPathView is created at the first use, not by
    'QQuickPathView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathView.
  - Qt tells when it has removed the C++ QQuickPathView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickPathView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HighlightRangeMode(CuteNum):
    """
    The enum 'QQuickPathView::HighlightRangeMode' of Qt, with the 3 names Qt
    gives in it.
    """

    NoHighlightRange = Kee[int](0)
    ApplyRange = Kee[int](1)
    StrictlyEnforceRange = Kee[int](2)

  class MovementDirection(CuteNum):
    """
    The enum 'QQuickPathView::MovementDirection' of Qt, with the 3 names Qt
    gives in it.
    """

    Shortest = Kee[int](0)
    Negative = Kee[int](1)
    Positive = Kee[int](2)

  class PositionMode(CuteNum):
    """
    The enum 'QQuickPathView::PositionMode' of Qt, with the 5 names Qt gives
    in it.
    """

    Beginning = Kee[int](0)
    Center = Kee[int](1)
    End = Kee[int](2)
    Contain = Kee[int](4)
    SnapPosition = Kee[int](5)

  class SnapMode(CuteNum):
    """
    The enum 'QQuickPathView::SnapMode' of Qt, with the 3 names Qt gives in
    it.
    """

    NoSnap = Kee[int](0)
    SnapToItem = Kee[int](1)
    SnapOneItem = Kee[int](2)

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
    Calls Qt's 'QString QQuickPathView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#tr

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
    #  QString QQuickPathView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickPathView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickPathViewAttached]:
    """
    Calls Qt's 'QQuickPathViewAttached
    *QQuickPathView::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPathViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathViewAttached *QQuickPathView::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN14QQuickPathView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQuickPathViewAttached
    return QQuickPathViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathView'

  #  A C++ QQuickPathView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPathView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPathView::model() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def path(self) -> Optional[QQuickPath]:
    """
    Calls Qt's 'QQuickPath *QQuickPathView::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#path

    Returns
    -------

    Optional[QQuickPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPath *QQuickPathView::path() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView4pathEv')
    from . import QQuickPath
    return QQuickPath._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickPathView::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#currentIndex
    """
    #  int QQuickPathView::currentIndex() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView12currentIndexEv')

  def currentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathView::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#currentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathView::currentItem() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView11currentItemEv')
    return QQuickItem._cuteAt(address)

  def offset(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#offset
    """
    #  qreal QQuickPathView::offset() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView6offsetEv')

  def highlight(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickPathView::highlight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#highlight

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickPathView::highlight() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView9highlightEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def highlightItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathView::highlightItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#highlightItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathView::highlightItem() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickPathView13highlightItemEv',
    )
    return QQuickItem._cuteAt(address)

  def highlightRangeMode(self) -> HighlightRangeMode:
    """
    Calls Qt's 'HighlightRangeMode QQuickPathView::highlightRangeMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightRangeMode

    Returns
    -------

    HighlightRangeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HighlightRangeMode(number)' gives.
    """
    #  HighlightRangeMode QQuickPathView::highlightRangeMode() const
    return QQuickPathView.HighlightRangeMode(self.uglySide.call(
        'ritual_ZNK14QQuickPathView18highlightRangeModeEv',
    ))

  def preferredHighlightBegin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::preferredHighlightBegin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#preferredHighlightBegin
    """
    #  qreal QQuickPathView::preferredHighlightBegin() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathView23preferredHighlightBeginEv',
    )

  def preferredHighlightEnd(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::preferredHighlightEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#preferredHighlightEnd
    """
    #  qreal QQuickPathView::preferredHighlightEnd() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathView21preferredHighlightEndEv',
    )

  def highlightMoveDuration(self) -> int:
    """
    Calls Qt's 'int QQuickPathView::highlightMoveDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightMoveDuration
    """
    #  int QQuickPathView::highlightMoveDuration() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathView21highlightMoveDurationEv',
    )

  def dragMargin(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::dragMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#dragMargin
    """
    #  qreal QQuickPathView::dragMargin() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView10dragMarginEv')

  def flickDeceleration(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::flickDeceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#flickDeceleration
    """
    #  qreal QQuickPathView::flickDeceleration() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathView17flickDecelerationEv',
    )

  def maximumFlickVelocity(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathView::maximumFlickVelocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#maximumFlickVelocity
    """
    #  qreal QQuickPathView::maximumFlickVelocity() const
    return self.uglySide.call(
        'ritual_ZNK14QQuickPathView20maximumFlickVelocityEv',
    )

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathView::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#isInteractive
    """
    #  bool QQuickPathView::isInteractive() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView13isInteractiveEv')

  def isMoving(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathView::isMoving() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#isMoving
    """
    #  bool QQuickPathView::isMoving() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView8isMovingEv')

  def isFlicking(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathView::isFlicking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#isFlicking
    """
    #  bool QQuickPathView::isFlicking() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView10isFlickingEv')

  def isDragging(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathView::isDragging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#isDragging
    """
    #  bool QQuickPathView::isDragging() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView10isDraggingEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickPathView::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#count
    """
    #  int QQuickPathView::count() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView5countEv')

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickPathView::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickPathView::delegate() const
    address = self.uglySide.call('ritual_ZNK14QQuickPathView8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def pathItemCount(self) -> int:
    """
    Calls Qt's 'int QQuickPathView::pathItemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#pathItemCount
    """
    #  int QQuickPathView::pathItemCount() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView13pathItemCountEv')

  def cacheItemCount(self) -> int:
    """
    Calls Qt's 'int QQuickPathView::cacheItemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#cacheItemCount
    """
    #  int QQuickPathView::cacheItemCount() const
    return self.uglySide.call('ritual_ZNK14QQuickPathView14cacheItemCountEv')

  def snapMode(self) -> SnapMode:
    """
    Calls Qt's 'SnapMode QQuickPathView::snapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#snapMode

    Returns
    -------

    SnapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SnapMode(number)' gives.
    """
    #  SnapMode QQuickPathView::snapMode() const
    return QQuickPathView.SnapMode(self.uglySide.call(
        'ritual_ZNK14QQuickPathView8snapModeEv',
    ))

  def movementDirection(self) -> MovementDirection:
    """
    Calls Qt's 'MovementDirection QQuickPathView::movementDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#movementDirection

    Returns
    -------

    MovementDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'MovementDirection(number)' gives.
    """
    #  MovementDirection QQuickPathView::movementDirection() const
    return QQuickPathView.MovementDirection(self.uglySide.call(
        'ritual_ZNK14QQuickPathView17movementDirectionEv',
    ))

  @overload(float, float)
  def indexAt(self, x: float, y: float) -> int:
    """
    Calls Qt's 'int QQuickPathView::indexAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#indexAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  int QQuickPathView::indexAt(qreal x, qreal y) const
    return self.uglySide.call('ritual_ZNK14QQuickPathView7indexAtEdd', x, y)

  @overload(float, float)
  def itemAt(self, x: float, y: float) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathView::itemAt(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#itemAt

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathView::itemAt(qreal x, qreal y) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickPathView6itemAtEdd', x, y,
    )
    return QQuickItem._cuteAt(address)

  @overload(int)
  def itemAtIndex(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathView::itemAtIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#itemAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathView::itemAtIndex(int index) const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickPathView11itemAtIndexEi', index,
    )
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, a0: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPathView::setModel(const QVariant &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setModel

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPathView::setModel(const QVariant &a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView8setModelERK8QVariant', self._valueOf(a0),
    )

  @overload(QQuickPath)
  @overload(NoneType)
  def setPath(self, a0: Optional[QQuickPath]) -> None:
    """
    Calls Qt's 'void QQuickPathView::setPath(QQuickPath *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setPath

    Parameters
    ----------

    a0 : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::setPath(QQuickPath *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView7setPathEP10QQuickPath',
        self._addressOf(a0),
    )

  @overload(int)
  def setCurrentIndex(self, idx: int) -> None:
    """
    Calls Qt's 'void QQuickPathView::setCurrentIndex(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setCurrentIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQuickPathView::setCurrentIndex(int idx)
    self.uglySide.call('ritual_ZN14QQuickPathView15setCurrentIndexEi', idx)

  @overload(float)
  def setOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setOffset(qreal offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickPathView::setOffset(qreal offset)
    self.uglySide.call('ritual_ZN14QQuickPathView9setOffsetEd', offset)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setHighlight(self, highlight: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickPathView::setHighlight(QQmlComponent *highlight)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setHighlight

    Parameters
    ----------

    highlight : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::setHighlight(QQmlComponent *highlight)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView12setHighlightEP13QQmlComponent',
        self._addressOf(highlight),
    )

  @overload(HighlightRangeMode)
  def setHighlightRangeMode(self, mode: HighlightRangeMode) -> None:
    """
    Calls Qt's 'void QQuickPathView::setHighlightRangeMode(HighlightRangeMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setHighlightRangeMode

    Parameters
    ----------

    mode : HighlightRangeMode
      Passed on as its number.
    """
    #  void QQuickPathView::setHighlightRangeMode(HighlightRangeMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView21setHighlightRangeModeENS_18HighlightRan'
        'geModeE',
        mode.value,
    )

  @overload(float)
  def setPreferredHighlightBegin(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setPreferredHighlightBegin(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setPreferredHighlightBegin

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathView::setPreferredHighlightBegin(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView26setPreferredHighlightBeginEd', a0,
    )

  @overload(float)
  def setPreferredHighlightEnd(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setPreferredHighlightEnd(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setPreferredHighlightEnd

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathView::setPreferredHighlightEnd(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView24setPreferredHighlightEndEd', a0,
    )

  @overload(int)
  def setHighlightMoveDuration(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathView::setHighlightMoveDuration(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setHighlightMoveDuration

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathView::setHighlightMoveDuration(int a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView24setHighlightMoveDurationEi', a0,
    )

  @overload(float)
  def setDragMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setDragMargin(qreal margin)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setDragMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QQuickPathView::setDragMargin(qreal margin)
    self.uglySide.call('ritual_ZN14QQuickPathView13setDragMarginEd', margin)

  @overload(float)
  def setFlickDeceleration(self, dec: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setFlickDeceleration(qreal dec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setFlickDeceleration

    Parameters
    ----------

    dec : float
      Passed on as it is.
    """
    #  void QQuickPathView::setFlickDeceleration(qreal dec)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView20setFlickDecelerationEd', dec,
    )

  @overload(float)
  def setMaximumFlickVelocity(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickPathView::setMaximumFlickVelocity(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setMaximumFlickVelocity

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickPathView::setMaximumFlickVelocity(qreal a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView23setMaximumFlickVelocityEd', a0,
    )

  @overload(bool)
  def setInteractive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPathView::setInteractive(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setInteractive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPathView::setInteractive(bool a0)
    self.uglySide.call('ritual_ZN14QQuickPathView14setInteractiveEb', a0)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickPathView::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(int)
  def setPathItemCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathView::setPathItemCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setPathItemCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathView::setPathItemCount(int a0)
    self.uglySide.call('ritual_ZN14QQuickPathView16setPathItemCountEi', a0)

  @overload(int)
  def setCacheItemCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickPathView::setCacheItemCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setCacheItemCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickPathView::setCacheItemCount(int a0)
    self.uglySide.call('ritual_ZN14QQuickPathView17setCacheItemCountEi', a0)

  @overload(SnapMode)
  def setSnapMode(self, mode: SnapMode) -> None:
    """
    Calls Qt's 'void QQuickPathView::setSnapMode(SnapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#setSnapMode

    Parameters
    ----------

    mode : SnapMode
      Passed on as its number.
    """
    #  void QQuickPathView::setSnapMode(SnapMode mode)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView11setSnapModeENS_8SnapModeE', mode.value,
    )

  @overload(MovementDirection)
  def setMovementDirection(self, dir: MovementDirection) -> None:
    """
    Calls Qt's 'void QQuickPathView::setMovementDirection(MovementDirection
    dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#setMovementDirection

    Parameters
    ----------

    dir : MovementDirection
      Passed on as its number.
    """
    #  void QQuickPathView::setMovementDirection(MovementDirection dir)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView20setMovementDirectionENS_17MovementDirec'
        'tionE',
        dir.value,
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
    Notes what was given, for Qt's 'QQuickPathView::QQuickPathView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#QQuickPathView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathView::QQuickPathView(QQuickItem *parent)
    self._noteCreation(QQuickPathView, lambda: Rituals.call(
        'ritual_ZN14QQuickPathViewC1EP10QQuickItem', self._addressOf(parent),
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

  def resetPathItemCount(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::resetPathItemCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#resetPathItemCount
    """
    #  void QQuickPathView::resetPathItemCount()
    self.uglySide.call('ritual_ZN14QQuickPathView18resetPathItemCountEv')

  @overload(int, int)
  def positionViewAtIndex(self, index: int, mode: int) -> None:
    """
    Calls Qt's 'void QQuickPathView::positionViewAtIndex(int index, int
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#positionViewAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    mode : int
      Passed on as it is.
    """
    #  void QQuickPathView::positionViewAtIndex(int index, int mode)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView19positionViewAtIndexEii', index, mode,
    )

  def incrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::incrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#incrementCurrentIndex
    """
    #  void QQuickPathView::incrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickPathView21incrementCurrentIndexEv')

  def decrementCurrentIndex(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::decrementCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#decrementCurrentIndex
    """
    #  void QQuickPathView::decrementCurrentIndex()
    self.uglySide.call('ritual_ZN14QQuickPathView21decrementCurrentIndexEv')

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#currentIndexChanged
    """
    #  void QQuickPathView::currentIndexChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView19currentIndexChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#currentItemChanged
    """
    #  void QQuickPathView::currentItemChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView18currentItemChangedEv')

  def offsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::offsetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#offsetChanged
    """
    #  void QQuickPathView::offsetChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView13offsetChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#modelChanged
    """
    #  void QQuickPathView::modelChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView12modelChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#countChanged
    """
    #  void QQuickPathView::countChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView12countChangedEv')

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::pathChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#pathChanged
    """
    #  void QQuickPathView::pathChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView11pathChangedEv')

  def preferredHighlightBeginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::preferredHighlightBeginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#preferredHighlightBeginChanged
    """
    #  void QQuickPathView::preferredHighlightBeginChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView30preferredHighlightBeginChangedEv',
    )

  def preferredHighlightEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::preferredHighlightEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#preferredHighlightEndChanged
    """
    #  void QQuickPathView::preferredHighlightEndChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView28preferredHighlightEndChangedEv',
    )

  def highlightRangeModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::highlightRangeModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightRangeModeChanged
    """
    #  void QQuickPathView::highlightRangeModeChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView25highlightRangeModeChangedEv',
    )

  def dragMarginChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::dragMarginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#dragMarginChanged
    """
    #  void QQuickPathView::dragMarginChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView17dragMarginChangedEv')

  def snapPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::snapPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#snapPositionChanged
    """
    #  void QQuickPathView::snapPositionChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView19snapPositionChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#delegateChanged
    """
    #  void QQuickPathView::delegateChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView15delegateChangedEv')

  def pathItemCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::pathItemCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#pathItemCountChanged
    """
    #  void QQuickPathView::pathItemCountChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView20pathItemCountChangedEv')

  def maximumFlickVelocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::maximumFlickVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#maximumFlickVelocityChanged
    """
    #  void QQuickPathView::maximumFlickVelocityChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView27maximumFlickVelocityChangedEv',
    )

  def flickDecelerationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::flickDecelerationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#flickDecelerationChanged
    """
    #  void QQuickPathView::flickDecelerationChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView24flickDecelerationChangedEv',
    )

  def interactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::interactiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#interactiveChanged
    """
    #  void QQuickPathView::interactiveChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView18interactiveChangedEv')

  def movingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::movingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#movingChanged
    """
    #  void QQuickPathView::movingChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView13movingChangedEv')

  def flickingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::flickingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#flickingChanged
    """
    #  void QQuickPathView::flickingChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView15flickingChangedEv')

  def draggingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::draggingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#draggingChanged
    """
    #  void QQuickPathView::draggingChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView15draggingChangedEv')

  def highlightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::highlightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightChanged
    """
    #  void QQuickPathView::highlightChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView16highlightChangedEv')

  def highlightItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::highlightItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightItemChanged
    """
    #  void QQuickPathView::highlightItemChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView20highlightItemChangedEv')

  def highlightMoveDurationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::highlightMoveDurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#highlightMoveDurationChanged
    """
    #  void QQuickPathView::highlightMoveDurationChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView28highlightMoveDurationChangedEv',
    )

  def movementStarted(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::movementStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#movementStarted
    """
    #  void QQuickPathView::movementStarted()
    self.uglySide.call('ritual_ZN14QQuickPathView15movementStartedEv')

  def movementEnded(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::movementEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#movementEnded
    """
    #  void QQuickPathView::movementEnded()
    self.uglySide.call('ritual_ZN14QQuickPathView13movementEndedEv')

  def movementDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::movementDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#movementDirectionChanged
    """
    #  void QQuickPathView::movementDirectionChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickPathView24movementDirectionChangedEv',
    )

  def flickStarted(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::flickStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#flickStarted
    """
    #  void QQuickPathView::flickStarted()
    self.uglySide.call('ritual_ZN14QQuickPathView12flickStartedEv')

  def flickEnded(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::flickEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#flickEnded
    """
    #  void QQuickPathView::flickEnded()
    self.uglySide.call('ritual_ZN14QQuickPathView10flickEndedEv')

  def dragStarted(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::dragStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#dragStarted
    """
    #  void QQuickPathView::dragStarted()
    self.uglySide.call('ritual_ZN14QQuickPathView11dragStartedEv')

  def dragEnded(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::dragEnded()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#dragEnded
    """
    #  void QQuickPathView::dragEnded()
    self.uglySide.call('ritual_ZN14QQuickPathView9dragEndedEv')

  def snapModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::snapModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#snapModeChanged
    """
    #  void QQuickPathView::snapModeChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView15snapModeChangedEv')

  def cacheItemCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::cacheItemCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#cacheItemCountChanged
    """
    #  void QQuickPathView::cacheItemCountChanged()
    self.uglySide.call('ritual_ZN14QQuickPathView21cacheItemCountChangedEv')

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#updatePolish
    """
    #  void QQuickPathView::updatePolish()
    ritual = 'ritual_ZN14QQuickPathView12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickPathView12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPathView::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickPathView15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickPathView15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPathView::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN14QQuickPathView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickPathView14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPathView::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN14QQuickPathView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickPathView17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

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
    Calls Qt's 'bool QQuickPathView::childMouseEventFilter(QQuickItem *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#childMouseEventFilter

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPathView::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
    ritual = (
        'ritual_ZN14QQuickPathView21childMouseEventFilterEP10QQuickItemP6QE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickPathView21childMouseEventFilterEP10QQuickIt'
          'emP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#mouseUngrabEvent
    """
    #  void QQuickPathView::mouseUngrabEvent()
    ritual = 'ritual_ZN14QQuickPathView16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickPathView16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathview.html#componentComplete
    """
    #  void QQuickPathView::componentComplete()
    ritual = 'ritual_ZN14QQuickPathView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickPathView17componentCompleteEv'
    self.uglySide.call(ritual)

  def refill(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::refill()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#refill
    """
    #  void QQuickPathView::refill()
    self.uglySide.call('ritual_ZN14QQuickPathView6refillEv')

  def ticked(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::ticked()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#ticked
    """
    #  void QQuickPathView::ticked()
    self.uglySide.call('ritual_ZN14QQuickPathView6tickedEv')

  def movementEnding(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::movementEnding()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#movementEnding
    """
    #  void QQuickPathView::movementEnding()
    self.uglySide.call('ritual_ZN14QQuickPathView14movementEndingEv')

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQuickPathView::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQuickPathView::modelUpdated(const QQmlChangeSet &changeSet, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView12modelUpdatedERK13QQmlChangeSetb',
        self._valueOf(changeSet), reset,
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def createdItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPathView::createdItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#createdItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::createdItem(int index, QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView11createdItemEiP7QObject',
        index, self._addressOf(item, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItem(self, index: int, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPathView::initItem(int index, QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#initItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::initItem(int index, QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView8initItemEiP7QObject',
        index, self._addressOf(item, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def destroyingItem(self, item: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPathView::destroyingItem(QObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#destroyingItem

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathView::destroyingItem(QObject *item)
    self.uglySide.call(
        'ritual_ZN14QQuickPathView14destroyingItemEP7QObject',
        self._addressOf(item, 'QObject'),
    )

  def pathUpdated(self) -> None:
    """
    Calls Qt's 'void QQuickPathView::pathUpdated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#pathUpdated
    """
    #  void QQuickPathView::pathUpdated()
    self.uglySide.call('ritual_ZN14QQuickPathView11pathUpdatedEv')

  def d_func(self) -> Optional[QQuickPathViewPrivate]:
    """
    Calls Qt's 'QQuickPathViewPrivate *QQuickPathView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathview.html#d_func

    Returns
    -------

    Optional[QQuickPathViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathViewPrivate *QQuickPathView::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickPathView6d_funcEv')
    from . import QQuickPathViewPrivate
    return QQuickPathViewPrivate._cuteAt(address)
