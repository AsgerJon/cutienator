"""
QQuickItemViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickItemViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQml import QAnimationJobChangeListener, QQmlIncubator
from . import QQuickFlickablePrivate, QQuickItemViewTransitionChangeListener
from ..QtQmlModels import QQmlChangeSet, QQmlInstanceModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRectF
  from ..QtQml import QAbstractAnimationJob, QQmlComponent
  from . import FxViewItem, QQuickGeometryChange, QQuickItem, QQuickItemView
  from . import QQuickItemViewAttached, QQuickItemViewTransitionableItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  FxViewItem = WAIT['FxViewItem']
  QAbstractAnimationJob = WAIT['QAbstractAnimationJob']
  QObject = WAIT['QObject']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickItemView = WAIT['QQuickItemView']
  QQuickItemViewTransitionableItem = WAIT['QQuickItemViewTransitionableItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewPrivate(QQuickFlickablePrivate, QQuickItemViewTransitionChangeListener, QAnimationJobChangeListener):
  """
  The cute side of Qt's QQuickItemViewPrivate: a plain Python object standing
  in front of one C++ QQuickItemViewPrivate.

  It is built on the cute 'QQuickFlickablePrivate', as Qt's
  QQuickItemViewPrivate is built on Qt's QQuickFlickablePrivate, and has
  everything that class has. It is built on the cute
  'QQuickItemViewTransitionChangeListener' as well, as Qt's
  QQuickItemViewPrivate is built on Qt's
  QQuickItemViewTransitionChangeListener too, and has everything that class
  has. It is built on the cute 'QAnimationJobChangeListener' as well, as Qt's
  QQuickItemViewPrivate is built on Qt's QAnimationJobChangeListener too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemViewPrivate that has a ritual and that
  Python can call so far, 84 names in all: 'q_func', 'get', 'isValid',
  'position', 'size', 'startPosition', 'endPosition', 'contentStartOffset',
  'findLastVisibleIndex', 'visibleItem', 'firstItemInView',
  'findLastIndexInView', 'mapFromModel', 'init', 'clear', 'updateViewport',
  'animationFinished', 'mirrorChange', 'createItem', 'releaseCurrentItem',
  'releaseItem', 'itemDestroyed', 'createHighlightItem',
  'createComponentItem', 'initializeComponentItem', 'updateTrackedItem',
  'updateUnrequestedIndexes', 'updateUnrequestedPositions',
  'updateVisibleIndex', 'calculatedMinExtent', 'calculatedMaxExtent',
  'applyDelegateModelAccessChange', 'removeItem',
  'updateSizeChangesBeforeVisiblePos', 'repositionFirstItem',
  'createTransitioner', 'prepareVisibleItemTransitions',
  'prepareNonVisibleItemTransition', 'viewItemTransitionFinished',
  'checkVisible', 'showVisibleItems', 'markExtentsDirty',
  'hasPendingChanges', 'forceLayoutPolish', 'releaseVisibleItems',
  'getAttachedObject', 'storeFirstVisibleItemPosition', 'layoutOrientation',
  'isContentFlowReversed', 'positionAt', 'endPositionAt', 'originPosition',
  'lastPosition', 'headerSize', 'footerSize', 'showHeaderForIndex',
  'showFooterForIndex', 'updateHeader', 'updateFooter', 'hasStickyHeader',
  'hasStickyFooter', 'createHighlight', 'updateHighlight',
  'resetHighlightPosition', 'movingFromHighlight', 'setPosition',
  'fixupPosition', 'addVisibleItems', 'removeNonVisibleItems',
  'visibleItemsChanged', 'newViewItem', 'repositionItemAt',
  'repositionPackageItemAt', 'resetFirstItemPosition', 'adjustFirstItem',
  'layoutVisibleItems', 'changedVisibleIndex',
  'needsRefillForAddedOrRemovedIndex', 'translateAndTransitionItemsAfter',
  'initializeViewItem', 'initializeCurrentItem', 'updateSectionCriteria',
  'updateSections', 'itemGeometryChanged'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickItemView *QQuickItemViewPrivate::q_func() const': takes
    in Python what 'QQuickItemView *QQuickItemViewPrivate::q_func()' takes.
  - Qt's 'QQuickItemViewPrivate::~QQuickItemViewPrivate()': the destructor:
    Python never removes a C++ QQuickItemViewPrivate.
  - Qt's 'qreal QQuickItemViewPrivate::minExtentForAxis(const AxisData
    &axisData, bool forXAxis) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'qreal QQuickItemViewPrivate::maxExtentForAxis(const AxisData
    &axisData, bool forXAxis) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QQuickItemViewPrivate::applyRemovalChange(const
    QQmlChangeSet::Change &removal, ChangeResult *changeResult, int
    *removedCount)': takes a number to change where it is.
  - Qt's 'void QQuickItemViewPrivate::prepareRemoveTransitions(
    QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *> *removedItems)': names
    'QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *>', which has no cute
    class yet.
  - Qt's 'int QQuickItemViewPrivate::findMoveKeyIndex(QQmlChangeSet::MoveKey
    key, const QList<QQmlChangeSet::Change> &changes) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QQuickItemViewPrivate::applyInsertionChange(const
    QQmlChangeSet::Change &insert, ChangeResult *changeResult,
    QList<FxViewItem *> *newItems, QList<MovedItem> *movingIntoView)': names
    'QList<FxViewItem *>', which has no cute class yet.

  What has no ritual
  ------------------

  14 of the 106 functions Qt declares: 12 leans on 'QQuickItemViewPrivate; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 leans on 'non-virtual thunk to
  QQuickItemViewPrivate.

  What to expect
  --------------

  - The C++ QQuickItemViewPrivate is created at the first use, not by
    'QQuickItemViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemViewPrivate.
  - Each name of Qt's QQuickItemViewPrivate that has no cute function yet,
    '__init__', 'applyDelegateChange', 'applyInsertionChange',
    'applyModelChanges', 'applyPendingChanges', 'applyRemovalChange',
    'connectModel', 'disconnectModel', 'emitCountChanged',
    'findMoveKeyIndex', 'layout', 'maxExtentForAxis', 'minExtentForAxis',
    'positionViewAtIndex', 'prepareRemoveTransitions', 'refill',
    'refillOrLayout', 'regenerate', 'updateCurrent', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickItemViewPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BufferMode(CuteNum):
    """
    The enum 'QQuickItemViewPrivate::BufferMode' of Qt, with the 3 names Qt
    gives in it.
    """

    NoBuffer = Kee[int](0)
    BufferBefore = Kee[int](1)
    BufferAfter = Kee[int](2)

  #  The classes Qt writes inside QQuickItemViewPrivate, each a class in here
  #  as in C++.

  class ChangeResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItemViewPrivate::ChangeResult: a plain Python
    object standing in front of one C++ QQuickItemViewPrivate::ChangeResult.

    C++ hands a QQuickItemViewPrivate::ChangeResult around as a copy, so
    every C++ QQuickItemViewPrivate::ChangeResult behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickItemViewPrivate::ChangeResult that has a
    ritual and that Python can call so far, 2 names in all: '__iadd__',
    'reset'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItemViewPrivate::ChangeResult::ChangeResult(const
      QQmlNullableValue<qreal> &p)': takes a type Python has no way to hand
      over yet.
    - Qt's 'QQuickItemViewPrivate::ChangeResult::~ChangeResult()': the
      destructor: Python removes its C++ QQuickItemViewPrivate::ChangeResult
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickItemViewPrivate::ChangeResult is created at the first
      use, not by 'QQuickItemViewPrivate::ChangeResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItemViewPrivate::ChangeResult back gives a
      copy the ritual made for Python, in a new cute
      QQuickItemViewPrivate::ChangeResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItemViewPrivate::ChangeResult'

    #  Qt's '~QQuickItemViewPrivate::ChangeResult()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickItemViewPrivate::ChangeResult
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuickItemViewPrivate12ChangeResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __iadd__(
        self,
        other: QQuickItemViewPrivate.ChangeResult,
    ) -> QQuickItemViewPrivate.ChangeResult:
      """
      Calls Qt's 'ChangeResult
      &QQuickItemViewPrivate::ChangeResult::operator+=(const ChangeResult
      &other)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemviewprivate-changeresult.html

      Parameters
      ----------

      other : QQuickItemViewPrivate.ChangeResult
        Passed on as a value: Qt reads the C++
        QQuickItemViewPrivate::ChangeResult, which stays Python's own.
      """
      #  ChangeResult &QQuickItemViewPrivate::ChangeResult::operator+=(const
      #      ChangeResult &other)
      self.uglySide.call(
          'ritual_ZN21QQuickItemViewPrivate12ChangeResultpLERKS0_',
          self._valueOf(other),
      )
      return self

    @overload.fallback
    def __iadd__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItemViewPrivate::ChangeResult::ChangeResult()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemviewprivate-changeresult.html
      """
      #  QQuickItemViewPrivate::ChangeResult::ChangeResult()
      self._noteCreation(
          QQuickItemViewPrivate.ChangeResult, lambda: Rituals.call(
              'ritual_ZN21QQuickItemViewPrivate12ChangeResultC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def reset(self) -> None:
      """
      Calls Qt's 'void QQuickItemViewPrivate::ChangeResult::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemviewprivate-changeresult.html#reset
      """
      #  void QQuickItemViewPrivate::ChangeResult::reset()
      self.uglySide.call(
          'ritual_ZN21QQuickItemViewPrivate12ChangeResult5resetEv',
      )

  class MovedItem(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickItemViewPrivate::MovedItem: a plain Python
    object standing in front of one C++ QQuickItemViewPrivate::MovedItem.

    C++ hands a QQuickItemViewPrivate::MovedItem around as a copy, so every
    C++ QQuickItemViewPrivate::MovedItem behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuickItemViewPrivate::MovedItem yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickItemViewPrivate::MovedItem::~MovedItem()': the destructor:
      Python removes its C++ QQuickItemViewPrivate::MovedItem by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickItemViewPrivate::MovedItem is created at the first use,
      not by 'QQuickItemViewPrivate::MovedItem(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickItemViewPrivate::MovedItem back gives a copy
      the ritual made for Python, in a new cute
      QQuickItemViewPrivate::MovedItem.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      FxViewItem = WAIT['FxViewItem']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickItemViewPrivate::MovedItem'

    #  Qt's '~QQuickItemViewPrivate::MovedItem()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickItemViewPrivate::MovedItem
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuickItemViewPrivate9MovedItemD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(FxViewItem, QQmlChangeSet.MoveKey)
    @overload(NoneType, QQmlChangeSet.MoveKey)
    def __init__(
        self,
        i: Optional[FxViewItem],
        k: QQmlChangeSet.MoveKey,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQuickItemViewPrivate::MovedItem::MovedItem(FxViewItem *i,
      QQmlChangeSet::MoveKey k)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickitemviewprivate-moveditem.html#MovedItem

      Parameters
      ----------

      i : Optional[FxViewItem]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      k : QQmlChangeSet.MoveKey
        Passed on as a value: Qt reads the C++ QQmlChangeSet::MoveKey, which
        stays Python's own.
      """
      #  QQuickItemViewPrivate::MovedItem::MovedItem(FxViewItem *i,
      #      QQmlChangeSet::MoveKey k)
      self._noteCreation(
          QQuickItemViewPrivate.MovedItem, lambda: Rituals.call(
              'ritual_ZN21QQuickItemViewPrivate9MovedItemC1EP10FxViewItemN1'
              '3QQmlChangeSet7MoveKeyE',
              self._addressOf(i), self._valueOf(k),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickItemView)
  @overload(NoneType)
  def get(o: Optional[QQuickItemView]) -> Optional[QQuickItemViewPrivate]:
    """
    Calls Qt's 'QQuickItemViewPrivate
    *QQuickItemViewPrivate::get(QQuickItemView *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#get

    Parameters
    ----------

    o : Optional[QQuickItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItemViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemViewPrivate *QQuickItemViewPrivate::get(QQuickItemView *o)
    address = Rituals.call(
        'ritual_ZN21QQuickItemViewPrivate3getEP14QQuickItemView',
        CuteMixin._addressOf(o),
    )
    return QQuickItemViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewPrivate'

  #  Qt's QQuickItemViewPrivate is built on more than one class. The part of
  #  a C++ QQuickItemViewPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemViewTransitionChangeListener':
          'ritual_cast_QQuickItemViewPrivate_QQuickItemViewTransitionChangeListener',
      'QAnimationJobChangeListener':
          'ritual_cast_QQuickItemViewPrivate_QAnimationJobChangeListener',
  }

  #  A C++ QQuickItemViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemViewPrivate'

  #  The functions Qt calls itself that QQuickItemViewPrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'applyInsertionChange': (
          'bool QQuickItemViewPrivate::applyInsertionChange(const '
          'QQmlChangeSet::Change &, ChangeResult *, QList<FxViewItem *> *, '
          'QList<MovedItem> *)',
      ),
  }

  #  The functions Qt calls itself that QQuickItemViewPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clear': (
          ('_ZN21QQuickItemViewPrivate5clearEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'updateViewport': (
          ('_ZN21QQuickItemViewPrivate14updateViewportEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'releaseItem': (
          ('_ZN21QQuickItemViewPrivate11releaseItemEP10FxViewItemN17QQmlIns'
           'tanceModel12ReusableFlagE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQuick:FxViewItem'),
               ('int', 'enum', 'QtQmlModels:QQmlInstanceModel.ReusableFlag'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'initializeComponentItem': (
          ('_ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQuickI'
           'tem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'updateSizeChangesBeforeVisiblePos': (
          ('_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePosEP'
           '10FxViewItemPNS_12ChangeResultE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:FxViewItem'),
               ('address', 'address',
                'QtQuick:QQuickItemViewPrivate.ChangeResult'),
           )),
      ),
      'getAttachedObject': (
          ('_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObject',
           ('address', 'address', 'QtQuick:QQuickItemViewAttached'),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'layoutOrientation': (
          ('_ZNK21QQuickItemViewPrivate17layoutOrientationEv',
           ('int', 'enum', 'QtCore:Qt.Orientation'),
           ()),
      ),
      'isContentFlowReversed': (
          ('_ZNK21QQuickItemViewPrivate21isContentFlowReversedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'positionAt': (
          ('_ZNK21QQuickItemViewPrivate10positionAtEi',
           ('double', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'endPositionAt': (
          ('_ZNK21QQuickItemViewPrivate13endPositionAtEi',
           ('double', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'originPosition': (
          ('_ZNK21QQuickItemViewPrivate14originPositionEv',
           ('double', 'number', ''),
           ()),
      ),
      'lastPosition': (
          ('_ZNK21QQuickItemViewPrivate12lastPositionEv',
           ('double', 'number', ''),
           ()),
      ),
      'headerSize': (
          ('_ZNK21QQuickItemViewPrivate10headerSizeEv',
           ('double', 'number', ''),
           ()),
      ),
      'footerSize': (
          ('_ZNK21QQuickItemViewPrivate10footerSizeEv',
           ('double', 'number', ''),
           ()),
      ),
      'showHeaderForIndex': (
          ('_ZNK21QQuickItemViewPrivate18showHeaderForIndexEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'showFooterForIndex': (
          ('_ZNK21QQuickItemViewPrivate18showFooterForIndexEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateHeader': (
          ('_ZN21QQuickItemViewPrivate12updateHeaderEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateFooter': (
          ('_ZN21QQuickItemViewPrivate12updateFooterEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hasStickyHeader': (
          ('_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasStickyFooter': (
          ('_ZNK21QQuickItemViewPrivate15hasStickyFooterEv',
           ('bool', 'number', ''),
           ()),
      ),
      'createHighlight': (
          ('_ZN21QQuickItemViewPrivate15createHighlightEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'updateHighlight': (
          ('_ZN21QQuickItemViewPrivate15updateHighlightEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resetHighlightPosition': (
          ('_ZN21QQuickItemViewPrivate22resetHighlightPositionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'movingFromHighlight': (
          ('_ZN21QQuickItemViewPrivate19movingFromHighlightEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setPosition': (
          ('_ZN21QQuickItemViewPrivate11setPositionEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'fixupPosition': (
          ('_ZN21QQuickItemViewPrivate13fixupPositionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addVisibleItems': (
          ('_ZN21QQuickItemViewPrivate15addVisibleItemsEddddb',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'removeNonVisibleItems': (
          ('_ZN21QQuickItemViewPrivate21removeNonVisibleItemsEdd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'visibleItemsChanged': (
          ('_ZN21QQuickItemViewPrivate19visibleItemsChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'newViewItem': (
          ('_ZN21QQuickItemViewPrivate11newViewItemEiP10QQuickItem',
           ('address', 'address', 'QtQuick:FxViewItem'),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'repositionItemAt': (
          ('_ZN21QQuickItemViewPrivate16repositionItemAtEP10FxViewItemid',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:FxViewItem'),
               ('int', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'repositionPackageItemAt': (
          ('_ZN21QQuickItemViewPrivate23repositionPackageItemAtEP10QQuickIt'
           'emi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('int', 'number', ''),
           )),
      ),
      'resetFirstItemPosition': (
          ('_ZN21QQuickItemViewPrivate22resetFirstItemPositionEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'adjustFirstItem': (
          ('_ZN21QQuickItemViewPrivate15adjustFirstItemEddi',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'layoutVisibleItems': (
          ('_ZN21QQuickItemViewPrivate18layoutVisibleItemsEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'changedVisibleIndex': (
          ('_ZN21QQuickItemViewPrivate19changedVisibleIndexEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'needsRefillForAddedOrRemovedIndex': (
          ('_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemovedIndexE'
           'i',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'translateAndTransitionItemsAfter': (
          ('_ZN21QQuickItemViewPrivate32translateAndTransitionItemsAfterEiR'
           'KNS_12ChangeResultES2_',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value',
                'QtQuick:QQuickItemViewPrivate.ChangeResult'),
               ('address', 'value',
                'QtQuick:QQuickItemViewPrivate.ChangeResult'),
           )),
      ),
      'initializeViewItem': (
          ('_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxViewItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:FxViewItem'),
           )),
      ),
      'initializeCurrentItem': (
          ('_ZN21QQuickItemViewPrivate21initializeCurrentItemEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateSectionCriteria': (
          ('_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateSections': (
          ('_ZN21QQuickItemViewPrivate14updateSectionsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#isValid
    """
    #  bool QQuickItemViewPrivate::isValid() const
    return self.uglySide.call('ritual_ZNK21QQuickItemViewPrivate7isValidEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#position
    """
    #  qreal QQuickItemViewPrivate::position() const
    return self.uglySide.call('ritual_ZNK21QQuickItemViewPrivate8positionEv')

  def size(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#size
    """
    #  qreal QQuickItemViewPrivate::size() const
    return self.uglySide.call('ritual_ZNK21QQuickItemViewPrivate4sizeEv')

  def startPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::startPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#startPosition
    """
    #  qreal QQuickItemViewPrivate::startPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate13startPositionEv',
    )

  def endPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::endPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#endPosition
    """
    #  qreal QQuickItemViewPrivate::endPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate11endPositionEv',
    )

  def contentStartOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::contentStartOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#contentStartOffset
    """
    #  qreal QQuickItemViewPrivate::contentStartOffset() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate18contentStartOffsetEv',
    )

  @overload()
  @overload(int)
  def findLastVisibleIndex(self, defaultValue: int = -1) -> int:
    """
    Calls Qt's 'int QQuickItemViewPrivate::findLastVisibleIndex(int
    defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#findLastVisibleIndex

    Parameters
    ----------

    defaultValue : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QQuickItemViewPrivate::findLastVisibleIndex(int defaultValue)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate20findLastVisibleIndexEi',
        defaultValue,
    )

  @overload(int)
  def visibleItem(self, modelIndex: int) -> Optional[FxViewItem]:
    """
    Calls Qt's 'FxViewItem *QQuickItemViewPrivate::visibleItem(int
    modelIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#visibleItem

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[FxViewItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxViewItem *QQuickItemViewPrivate::visibleItem(int modelIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate11visibleItemEi', modelIndex,
    )
    from . import FxViewItem
    return FxViewItem._cuteAt(address)

  def firstItemInView(self) -> Optional[FxViewItem]:
    """
    Calls Qt's 'FxViewItem *QQuickItemViewPrivate::firstItemInView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#firstItemInView

    Returns
    -------

    Optional[FxViewItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxViewItem *QQuickItemViewPrivate::firstItemInView() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate15firstItemInViewEv',
    )
    from . import FxViewItem
    return FxViewItem._cuteAt(address)

  def findLastIndexInView(self) -> int:
    """
    Calls Qt's 'int QQuickItemViewPrivate::findLastIndexInView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#findLastIndexInView
    """
    #  int QQuickItemViewPrivate::findLastIndexInView() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate19findLastIndexInViewEv',
    )

  @overload(int)
  def mapFromModel(self, modelIndex: int) -> int:
    """
    Calls Qt's 'int QQuickItemViewPrivate::mapFromModel(int modelIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#mapFromModel

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.
    """
    #  int QQuickItemViewPrivate::mapFromModel(int modelIndex) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate12mapFromModelEi', modelIndex,
    )

  @overload(QQmlComponent, float)
  @overload(NoneType, float)
  @overload(QQmlComponent, float, bool)
  @overload(NoneType, float, bool)
  def createComponentItem(
      self,
      component: Optional[QQmlComponent],
      zValue: float,
      createDefault: bool = False,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickItemViewPrivate::createComponentItem(QQmlComponent *component,
    qreal zValue, bool createDefault) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#createComponentItem

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    zValue : float
      Passed on as it is.

    createDefault : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemViewPrivate::createComponentItem(QQmlComponent
    #      *component, qreal zValue, bool createDefault) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate19createComponentItemEP13QQmlComp'
        'onentdb',
        self._addressOf(component), zValue, createDefault,
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def calculatedMinExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::calculatedMinExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#calculatedMinExtent
    """
    #  qreal QQuickItemViewPrivate::calculatedMinExtent() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate19calculatedMinExtentEv',
    )

  def calculatedMaxExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::calculatedMaxExtent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#calculatedMaxExtent
    """
    #  qreal QQuickItemViewPrivate::calculatedMaxExtent() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate19calculatedMaxExtentEv',
    )

  def hasPendingChanges(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::hasPendingChanges() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#hasPendingChanges
    """
    #  bool QQuickItemViewPrivate::hasPendingChanges() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate17hasPendingChangesEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def getAttachedObject(
      self,
      a0: Optional[QObject],
  ) -> Optional[QQuickItemViewAttached]:
    """
    Calls Qt's 'QQuickItemViewAttached
    *QQuickItemViewPrivate::getAttachedObject(const QObject *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#getAttachedObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItemViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemViewAttached *QQuickItemViewPrivate::getAttachedObject(const
    #      QObject *a0) const
    ritual = (
        'ritual_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObj'
          'ect')
    address = self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))
    from . import QQuickItemViewAttached
    return QQuickItemViewAttached._cuteAt(address)

  def layoutOrientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickItemViewPrivate::layoutOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#layoutOrientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickItemViewPrivate::layoutOrientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate17layoutOrientationEv',
    ))

  def isContentFlowReversed(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::isContentFlowReversed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#isContentFlowReversed
    """
    #  bool QQuickItemViewPrivate::isContentFlowReversed() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate21isContentFlowReversedEv',
    )

  @overload(int)
  def positionAt(self, index: int) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::positionAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#positionAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QQuickItemViewPrivate::positionAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate10positionAtEi', index,
    )

  @overload(int)
  def endPositionAt(self, index: int) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::endPositionAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#endPositionAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QQuickItemViewPrivate::endPositionAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate13endPositionAtEi', index,
    )

  def originPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::originPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#originPosition
    """
    #  qreal QQuickItemViewPrivate::originPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate14originPositionEv',
    )

  def lastPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::lastPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#lastPosition
    """
    #  qreal QQuickItemViewPrivate::lastPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate12lastPositionEv',
    )

  def headerSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::headerSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#headerSize
    """
    #  qreal QQuickItemViewPrivate::headerSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate10headerSizeEv',
    )

  def footerSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewPrivate::footerSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#footerSize
    """
    #  qreal QQuickItemViewPrivate::footerSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate10footerSizeEv',
    )

  @overload(int)
  def showHeaderForIndex(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::showHeaderForIndex(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#showHeaderForIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQuickItemViewPrivate::showHeaderForIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate18showHeaderForIndexEi', index,
    )

  @overload(int)
  def showFooterForIndex(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::showFooterForIndex(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#showFooterForIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQuickItemViewPrivate::showFooterForIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate18showFooterForIndexEi', index,
    )

  def hasStickyHeader(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::hasStickyHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#hasStickyHeader
    """
    #  bool QQuickItemViewPrivate::hasStickyHeader() const
    ritual = 'ritual_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv'
    return self.uglySide.call(ritual)

  def hasStickyFooter(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::hasStickyFooter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#hasStickyFooter
    """
    #  bool QQuickItemViewPrivate::hasStickyFooter() const
    ritual = 'ritual_ZNK21QQuickItemViewPrivate15hasStickyFooterEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickItemViewPrivate15hasStickyFooterEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def needsRefillForAddedOrRemovedIndex(self, a0: int) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(int a0)
    #      const
    ritual = (
        'ritual_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemovedInd'
        'exEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemo'
          'vedIndexEi')
    return self.uglySide.call(ritual, a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPosition(self, pos: float) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::setPosition(qreal pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#setPosition

    Parameters
    ----------

    pos : float
      Passed on as it is.
    """
    #  void QQuickItemViewPrivate::setPosition(qreal pos)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate11setPositionEd', pos,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickItemViewPrivate::QQuickItemViewPrivate()': leans on
    'non-virtual thunk to QQuickItemViewPrivate::viewItemTransitionFinished(
    QQuickItemViewTransitionableItem*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickItemViewPrivate::QQuickItemViewPrivate()': leans on "
        "'non-virtual thunk to "
        "QQuickItemViewPrivate::viewItemTransitionFinished(QQuickItemViewTra"
        "nsitionableItem*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickItemView]:
    """
    Calls Qt's 'QQuickItemView *QQuickItemViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItemView *QQuickItemViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickItemViewPrivate6q_funcEv')
    from . import QQuickItemView
    return QQuickItemView._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#init
    """
    #  void QQuickItemViewPrivate::init()
    ritual = 'ritual_ZN21QQuickItemViewPrivate4initEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate4initEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(bool)
  def clear(self, onDestruction: bool = False) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::clear(bool onDestruction)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewprivate.html#clear

    Parameters
    ----------

    onDestruction : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickItemViewPrivate::clear(bool onDestruction)
    ritual = 'ritual_ZN21QQuickItemViewPrivate5clearEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate5clearEb'
    self.uglySide.call(ritual, onDestruction)

  def updateViewport(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateViewport
    """
    #  void QQuickItemViewPrivate::updateViewport()
    ritual = 'ritual_ZN21QQuickItemViewPrivate14updateViewportEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate14updateViewportEv'
    self.uglySide.call(ritual)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationFinished(self, a0: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#animationFinished

    Parameters
    ----------

    a0 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob
    #      *a0)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate17animationFinishedEP21QAbstractAn'
        'imationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate17animationFinishedEP21QAbst'
          'ractAnimationJob')
    self.uglySide.call(ritual, self._addressOf(a0, 'QAbstractAnimationJob'))

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#mirrorChange
    """
    #  void QQuickItemViewPrivate::mirrorChange()
    self.uglySide.call('ritual_ZN21QQuickItemViewPrivate12mirrorChangeEv')

  @overload(int)
  @overload(int, QQmlIncubator.IncubationMode)
  def createItem(
      self,
      modelIndex: int,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> Optional[FxViewItem]:
    """
    Calls Qt's 'FxViewItem *QQuickItemViewPrivate::createItem(int modelIndex,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#createItem

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlIncubator.IncubationMode.AsynchronousIfNested.

    Returns
    -------

    Optional[FxViewItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxViewItem *QQuickItemViewPrivate::createItem(int modelIndex,
    #      QQmlIncubator::IncubationMode incubationMode)
    address = self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate10createItemEiN13QQmlIncubator14In'
        'cubationModeE',
        modelIndex, incubationMode.value,
    )
    from . import FxViewItem
    return FxViewItem._cuteAt(address)

  @overload(QQmlInstanceModel.ReusableFlag)
  def releaseCurrentItem(
      self,
      reusableFlag: QQmlInstanceModel.ReusableFlag,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewPrivate::releaseCurrentItem(QQmlInstanceModel::ReusableFlag
    reusableFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#releaseCurrentItem

    Parameters
    ----------

    reusableFlag : QQmlInstanceModel.ReusableFlag
      Passed on as its number.
    """
    #  bool QQuickItemViewPrivate::releaseCurrentItem(QQmlInstanceModel::
    #      ReusableFlag reusableFlag)
    return self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate18releaseCurrentItemEN17QQmlInstan'
        'ceModel12ReusableFlagE',
        reusableFlag.value,
    )

  @overload(FxViewItem, QQmlInstanceModel.ReusableFlag)
  @overload(NoneType, QQmlInstanceModel.ReusableFlag)
  def releaseItem(
      self,
      item: Optional[FxViewItem],
      reusableFlag: QQmlInstanceModel.ReusableFlag,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::releaseItem(FxViewItem *item,
    QQmlInstanceModel::ReusableFlag reusableFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#releaseItem

    Parameters
    ----------

    item : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reusableFlag : QQmlInstanceModel.ReusableFlag
      Passed on as its number.
    """
    #  bool QQuickItemViewPrivate::releaseItem(FxViewItem *item,
    #      QQmlInstanceModel::ReusableFlag reusableFlag)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate11releaseItemEP10FxViewItemN17QQml'
        'InstanceModel12ReusableFlagE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate11releaseItemEP10FxViewItemN'
          '17QQmlInstanceModel12ReusableFlagE')
    return self.uglySide.call(
        ritual, self._addressOf(item), reusableFlag.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickIte'
          'm')
    self.uglySide.call(ritual, self._addressOf(item))

  def createHighlightItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickItemViewPrivate::createHighlightItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#createHighlightItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickItemViewPrivate::createHighlightItem()
    address = self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate19createHighlightItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def initializeComponentItem(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::initializeComponentItem(QQuickItem *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#initializeComponentItem

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::initializeComponentItem(QQuickItem *a0)
    #      const
    ritual = (
        'ritual_ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQui'
        'ckItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickItemViewPrivate23initializeComponentItemEP'
          '10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  def updateTrackedItem(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateTrackedItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateTrackedItem
    """
    #  void QQuickItemViewPrivate::updateTrackedItem()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate17updateTrackedItemEv',
    )

  def updateUnrequestedIndexes(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateUnrequestedIndexes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html
    """
    #  void QQuickItemViewPrivate::updateUnrequestedIndexes()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate24updateUnrequestedIndexesEv',
    )

  def updateUnrequestedPositions(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateUnrequestedPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html
    """
    #  void QQuickItemViewPrivate::updateUnrequestedPositions()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate26updateUnrequestedPositionsEv',
    )

  def updateVisibleIndex(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateVisibleIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateVisibleIndex
    """
    #  void QQuickItemViewPrivate::updateVisibleIndex()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate18updateVisibleIndexEv',
    )

  def applyDelegateModelAccessChange(self) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::applyDelegateModelAccessChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html
    """
    #  void QQuickItemViewPrivate::applyDelegateModelAccessChange()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate30applyDelegateModelAccessChangeEv',
    )

  @overload(FxViewItem, QQmlChangeSet.Change, ChangeResult)
  @overload(FxViewItem, QQmlChangeSet.Change, NoneType)
  @overload(NoneType, QQmlChangeSet.Change, ChangeResult)
  @overload(NoneType, QQmlChangeSet.Change, NoneType)
  def removeItem(
      self,
      item: Optional[FxViewItem],
      removal: QQmlChangeSet.Change,
      removeResult: Optional[ChangeResult],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::removeItem(FxViewItem *item,
    const QQmlChangeSet::Change &removal, ChangeResult *removeResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#removeItem

    Parameters
    ----------

    item : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    removal : QQmlChangeSet.Change
      Passed on as a value: Qt reads the C++ QQmlChangeSet::Change, which
      stays Python's own.

    removeResult : Optional[ChangeResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::removeItem(FxViewItem *item, const
    #      QQmlChangeSet::Change &removal, ChangeResult *removeResult)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate10removeItemEP10FxViewItemRKN13QQm'
        'lChangeSet6ChangeEPNS_12ChangeResultE',
        self._addressOf(item), self._valueOf(removal),
        self._addressOf(removeResult),
    )

  @overload(FxViewItem, ChangeResult)
  @overload(FxViewItem, NoneType)
  @overload(NoneType, ChangeResult)
  @overload(NoneType, NoneType)
  def updateSizeChangesBeforeVisiblePos(
      self,
      item: Optional[FxViewItem],
      removeResult: Optional[ChangeResult],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(FxViewItem
    *item, ChangeResult *removeResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html

    Parameters
    ----------

    item : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    removeResult : Optional[ChangeResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(
    #      FxViewItem *item, ChangeResult *removeResult)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePo'
        'sEP10FxViewItemPNS_12ChangeResultE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVis'
          'iblePosEP10FxViewItemPNS_12ChangeResultE')
    self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(removeResult),
    )

  @overload(FxViewItem, float, FxViewItem, ChangeResult, ChangeResult)
  @overload(FxViewItem, float, FxViewItem, ChangeResult, NoneType)
  @overload(FxViewItem, float, FxViewItem, NoneType, ChangeResult)
  @overload(FxViewItem, float, FxViewItem, NoneType, NoneType)
  @overload(FxViewItem, float, NoneType, ChangeResult, ChangeResult)
  @overload(FxViewItem, float, NoneType, ChangeResult, NoneType)
  @overload(FxViewItem, float, NoneType, NoneType, ChangeResult)
  @overload(FxViewItem, float, NoneType, NoneType, NoneType)
  @overload(NoneType, float, FxViewItem, ChangeResult, ChangeResult)
  @overload(NoneType, float, FxViewItem, ChangeResult, NoneType)
  @overload(NoneType, float, FxViewItem, NoneType, ChangeResult)
  @overload(NoneType, float, FxViewItem, NoneType, NoneType)
  @overload(NoneType, float, NoneType, ChangeResult, ChangeResult)
  @overload(NoneType, float, NoneType, ChangeResult, NoneType)
  @overload(NoneType, float, NoneType, NoneType, ChangeResult)
  @overload(NoneType, float, NoneType, NoneType, NoneType)
  def repositionFirstItem(
      self,
      prevVisibleItemsFirst: Optional[FxViewItem],
      prevVisibleItemsFirstPos: float,
      prevFirstVisible: Optional[FxViewItem],
      insertionResult: Optional[ChangeResult],
      removalResult: Optional[ChangeResult],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::repositionFirstItem(FxViewItem
    *prevVisibleItemsFirst, qreal prevVisibleItemsFirstPos, FxViewItem
    *prevFirstVisible, ChangeResult *insertionResult, ChangeResult
    *removalResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#repositionFirstItem

    Parameters
    ----------

    prevVisibleItemsFirst : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    prevVisibleItemsFirstPos : float
      Passed on as it is.

    prevFirstVisible : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    insertionResult : Optional[ChangeResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    removalResult : Optional[ChangeResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::repositionFirstItem(FxViewItem
    #      *prevVisibleItemsFirst, qreal prevVisibleItemsFirstPos, FxViewItem
    #      *prevFirstVisible, ChangeResult *insertionResult, ChangeResult
    #      *removalResult)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate19repositionFirstItemEP10FxViewIte'
        'mdS1_PNS_12ChangeResultES3_',
        self._addressOf(prevVisibleItemsFirst), prevVisibleItemsFirstPos,
        self._addressOf(prevFirstVisible), self._addressOf(insertionResult),
        self._addressOf(removalResult),
    )

  def createTransitioner(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::createTransitioner()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#createTransitioner
    """
    #  void QQuickItemViewPrivate::createTransitioner()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate18createTransitionerEv',
    )

  def prepareVisibleItemTransitions(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::prepareVisibleItemTransitions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html
    """
    #  void QQuickItemViewPrivate::prepareVisibleItemTransitions()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate29prepareVisibleItemTransitionsEv',
    )

  @overload(FxViewItem, QRectF)
  @overload(NoneType, QRectF)
  def prepareNonVisibleItemTransition(
      self,
      item: Optional[FxViewItem],
      viewBounds: QRectF,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewPrivate::prepareNonVisibleItemTransition(FxViewItem *item,
    const QRectF &viewBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html

    Parameters
    ----------

    item : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QQuickItemViewPrivate::prepareNonVisibleItemTransition(FxViewItem
    #      *item, const QRectF &viewBounds)
    return self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate31prepareNonVisibleItemTransitionE'
        'P10FxViewItemRK6QRectF',
        self._addressOf(item), self._valueOf(viewBounds),
    )

  @overload(QQuickItemViewTransitionableItem)
  @overload(NoneType)
  def viewItemTransitionFinished(
      self,
      item: Optional[QQuickItemViewTransitionableItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::viewItemTransitionFinished(
    QQuickItemViewTransitionableItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html

    Parameters
    ----------

    item : Optional[QQuickItemViewTransitionableItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::viewItemTransitionFinished(
    #      QQuickItemViewTransitionableItem *item)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate26viewItemTransitionFinishedEP32QQ'
        'uickItemViewTransitionableItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate26viewItemTransitionFinished'
          'EP32QQuickItemViewTransitionableItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def checkVisible(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::checkVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#checkVisible
    """
    #  void QQuickItemViewPrivate::checkVisible() const
    self.uglySide.call('ritual_ZNK21QQuickItemViewPrivate12checkVisibleEv')

  def showVisibleItems(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::showVisibleItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#showVisibleItems
    """
    #  void QQuickItemViewPrivate::showVisibleItems() const
    self.uglySide.call(
        'ritual_ZNK21QQuickItemViewPrivate16showVisibleItemsEv',
    )

  def markExtentsDirty(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::markExtentsDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#markExtentsDirty
    """
    #  void QQuickItemViewPrivate::markExtentsDirty()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate16markExtentsDirtyEv',
    )

  def forceLayoutPolish(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::forceLayoutPolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#forceLayoutPolish
    """
    #  void QQuickItemViewPrivate::forceLayoutPolish()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate17forceLayoutPolishEv',
    )

  @overload(QQmlInstanceModel.ReusableFlag)
  def releaseVisibleItems(
      self,
      reusableFlag: QQmlInstanceModel.ReusableFlag,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::releaseVisibleItems(QQmlInstanceModel::
    ReusableFlag reusableFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#releaseVisibleItems

    Parameters
    ----------

    reusableFlag : QQmlInstanceModel.ReusableFlag
      Passed on as its number.
    """
    #  void QQuickItemViewPrivate::releaseVisibleItems(QQmlInstanceModel::
    #      ReusableFlag reusableFlag)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate19releaseVisibleItemsEN17QQmlInsta'
        'nceModel12ReusableFlagE',
        reusableFlag.value,
    )

  def storeFirstVisibleItemPosition(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::storeFirstVisibleItemPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html
    """
    #  void QQuickItemViewPrivate::storeFirstVisibleItemPosition()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate29storeFirstVisibleItemPositionEv',
    )

  def updateHeader(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateHeader()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateHeader
    """
    #  void QQuickItemViewPrivate::updateHeader()
    self.uglySide.call('ritual_ZN21QQuickItemViewPrivate12updateHeaderEv')

  def updateFooter(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateFooter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateFooter
    """
    #  void QQuickItemViewPrivate::updateFooter()
    self.uglySide.call('ritual_ZN21QQuickItemViewPrivate12updateFooterEv')

  @overload()
  @overload(bool)
  def createHighlight(self, onDestruction: bool = False) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::createHighlight(bool
    onDestruction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#createHighlight

    Parameters
    ----------

    onDestruction : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickItemViewPrivate::createHighlight(bool onDestruction)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate15createHighlightEb', onDestruction,
    )

  def updateHighlight(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateHighlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateHighlight
    """
    #  void QQuickItemViewPrivate::updateHighlight()
    self.uglySide.call('ritual_ZN21QQuickItemViewPrivate15updateHighlightEv')

  def resetHighlightPosition(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::resetHighlightPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#resetHighlightPosition
    """
    #  void QQuickItemViewPrivate::resetHighlightPosition()
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate22resetHighlightPositionEv',
    )

  def movingFromHighlight(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::movingFromHighlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#movingFromHighlight
    """
    #  bool QQuickItemViewPrivate::movingFromHighlight()
    ritual = 'ritual_ZN21QQuickItemViewPrivate19movingFromHighlightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate19movingFromHighlightEv'
    return self.uglySide.call(ritual)

  def fixupPosition(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::fixupPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#fixupPosition
    """
    #  void QQuickItemViewPrivate::fixupPosition()
    self.uglySide.call('ritual_ZN21QQuickItemViewPrivate13fixupPositionEv')

  @overload(float, float, float, float, bool)
  def addVisibleItems(
      self,
      fillFrom: float,
      fillTo: float,
      bufferFrom: float,
      bufferTo: float,
      doBuffer: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::addVisibleItems(qreal fillFrom,
    qreal fillTo, qreal bufferFrom, qreal bufferTo, bool doBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#addVisibleItems

    Parameters
    ----------

    fillFrom : float
      Passed on as it is.

    fillTo : float
      Passed on as it is.

    bufferFrom : float
      Passed on as it is.

    bufferTo : float
      Passed on as it is.

    doBuffer : bool
      Passed on as it is.
    """
    #  bool QQuickItemViewPrivate::addVisibleItems(qreal fillFrom, qreal
    #      fillTo, qreal bufferFrom, qreal bufferTo, bool doBuffer)
    return self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate15addVisibleItemsEddddb',
        fillFrom, fillTo, bufferFrom, bufferTo, doBuffer,
    )

  @overload(float, float)
  def removeNonVisibleItems(
      self,
      bufferFrom: float,
      bufferTo: float,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewPrivate::removeNonVisibleItems(qreal
    bufferFrom, qreal bufferTo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#removeNonVisibleItems

    Parameters
    ----------

    bufferFrom : float
      Passed on as it is.

    bufferTo : float
      Passed on as it is.
    """
    #  bool QQuickItemViewPrivate::removeNonVisibleItems(qreal bufferFrom,
    #      qreal bufferTo)
    return self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate21removeNonVisibleItemsEdd',
        bufferFrom, bufferTo,
    )

  def visibleItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::visibleItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#visibleItemsChanged
    """
    #  void QQuickItemViewPrivate::visibleItemsChanged()
    ritual = 'ritual_ZN21QQuickItemViewPrivate19visibleItemsChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate19visibleItemsChangedEv'
    self.uglySide.call(ritual)

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def newViewItem(
      self,
      index: int,
      item: Optional[QQuickItem],
  ) -> Optional[FxViewItem]:
    """
    Calls Qt's 'FxViewItem *QQuickItemViewPrivate::newViewItem(int index,
    QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#newViewItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[FxViewItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxViewItem *QQuickItemViewPrivate::newViewItem(int index, QQuickItem
    #      *item)
    address = self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate11newViewItemEiP10QQuickItem',
        index, self._addressOf(item),
    )
    from . import FxViewItem
    return FxViewItem._cuteAt(address)

  @overload(FxViewItem, int, float)
  @overload(NoneType, int, float)
  def repositionItemAt(
      self,
      item: Optional[FxViewItem],
      index: int,
      sizeBuffer: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::repositionItemAt(FxViewItem
    *item, int index, qreal sizeBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#repositionItemAt

    Parameters
    ----------

    item : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    sizeBuffer : float
      Passed on as it is.
    """
    #  void QQuickItemViewPrivate::repositionItemAt(FxViewItem *item, int
    #      index, qreal sizeBuffer)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate16repositionItemAtEP10FxViewItemid',
        self._addressOf(item), index, sizeBuffer,
    )

  @overload(QQuickItem, int)
  @overload(NoneType, int)
  def repositionPackageItemAt(
      self,
      item: Optional[QQuickItem],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::repositionPackageItemAt(QQuickItem *item, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#repositionPackageItemAt

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QQuickItemViewPrivate::repositionPackageItemAt(QQuickItem *item,
    #      int index)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate23repositionPackageItemAtEP10QQuic'
        'kItemi',
        self._addressOf(item), index,
    )

  @overload()
  @overload(float)
  def resetFirstItemPosition(self, pos: float = 0.0) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::resetFirstItemPosition(qreal
    pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#resetFirstItemPosition

    Parameters
    ----------

    pos : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QQuickItemViewPrivate::resetFirstItemPosition(qreal pos)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate22resetFirstItemPositionEd', pos,
    )

  @overload(float, float, int)
  def adjustFirstItem(
      self,
      forwards: float,
      backwards: float,
      changeBeforeVisible: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::adjustFirstItem(qreal forwards,
    qreal backwards, int changeBeforeVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#adjustFirstItem

    Parameters
    ----------

    forwards : float
      Passed on as it is.

    backwards : float
      Passed on as it is.

    changeBeforeVisible : int
      Passed on as it is.
    """
    #  void QQuickItemViewPrivate::adjustFirstItem(qreal forwards, qreal
    #      backwards, int changeBeforeVisible)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate15adjustFirstItemEddi',
        forwards, backwards, changeBeforeVisible,
    )

  @overload()
  @overload(int)
  def layoutVisibleItems(self, fromModelIndex: int = 0) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::layoutVisibleItems(int
    fromModelIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#layoutVisibleItems

    Parameters
    ----------

    fromModelIndex : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQuickItemViewPrivate::layoutVisibleItems(int fromModelIndex)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate18layoutVisibleItemsEi',
        fromModelIndex,
    )

  @overload(int)
  def changedVisibleIndex(self, newIndex: int) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::changedVisibleIndex(int
    newIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#changedVisibleIndex

    Parameters
    ----------

    newIndex : int
      Passed on as it is.
    """
    #  void QQuickItemViewPrivate::changedVisibleIndex(int newIndex)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate19changedVisibleIndexEi', newIndex,
    )

  @overload(int, ChangeResult, ChangeResult)
  def translateAndTransitionItemsAfter(
      self,
      afterIndex: int,
      insertionResult: ChangeResult,
      removalResult: ChangeResult,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewPrivate::translateAndTransitionItemsAfter(int afterIndex,
    const ChangeResult &insertionResult, const ChangeResult &removalResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html

    Parameters
    ----------

    afterIndex : int
      Passed on as it is.

    insertionResult : ChangeResult
      Passed on as a value: Qt reads the C++
      QQuickItemViewPrivate::ChangeResult, which stays Python's own.

    removalResult : ChangeResult
      Passed on as a value: Qt reads the C++
      QQuickItemViewPrivate::ChangeResult, which stays Python's own.
    """
    #  void QQuickItemViewPrivate::translateAndTransitionItemsAfter(int
    #      afterIndex, const ChangeResult &insertionResult, const
    #      ChangeResult &removalResult)
    self.uglySide.call(
        'ritual_ZN21QQuickItemViewPrivate32translateAndTransitionItemsAfter'
        'EiRKNS_12ChangeResultES2_',
        afterIndex, self._valueOf(insertionResult),
        self._valueOf(removalResult),
    )

  @overload(FxViewItem)
  @overload(NoneType)
  def initializeViewItem(self, a0: Optional[FxViewItem]) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::initializeViewItem(FxViewItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#initializeViewItem

    Parameters
    ----------

    a0 : Optional[FxViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewPrivate::initializeViewItem(FxViewItem *a0)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxViewItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxVi'
          'ewItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  def initializeCurrentItem(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::initializeCurrentItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#initializeCurrentItem
    """
    #  void QQuickItemViewPrivate::initializeCurrentItem()
    ritual = 'ritual_ZN21QQuickItemViewPrivate21initializeCurrentItemEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate21initializeCurrentItemEv')
    self.uglySide.call(ritual)

  def updateSectionCriteria(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateSectionCriteria()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateSectionCriteria
    """
    #  void QQuickItemViewPrivate::updateSectionCriteria()
    ritual = 'ritual_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv')
    self.uglySide.call(ritual)

  def updateSections(self) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::updateSections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#updateSections
    """
    #  void QQuickItemViewPrivate::updateSections()
    ritual = 'ritual_ZN21QQuickItemViewPrivate14updateSectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickItemViewPrivate14updateSectionsEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemViewPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemViewPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN21QQuickItemViewPrivate19itemGeometryChangedEP10QQuickIte'
        'm20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickItemViewPrivate19itemGeometryChangedEP10QQu'
          'ickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(a2),
    )

  @staticmethod
  def applyDelegateChange(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::applyDelegateChange()': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.applyDelegateChange' has no cute function "
        "yet. Qt's 'void QQuickItemViewPrivate::applyDelegateChange()': "
        "leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def applyInsertionChange(*__, **_) -> Never:
    """
    Qt's 'bool QQuickItemViewPrivate::applyInsertionChange(const
    QQmlChangeSet::Change &insert, ChangeResult *changeResult,
    QList<FxViewItem *> *newItems, QList<MovedItem> *movingIntoView)': names
    'QList<FxViewItem *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.applyInsertionChange' has no cute function "
        "yet. Qt's 'bool QQuickItemViewPrivate::applyInsertionChange(const "
        "QQmlChangeSet::Change &insert, ChangeResult *changeResult, "
        "QList<FxViewItem *> *newItems, QList<MovedItem> *movingIntoView)': "
        "names 'QList<FxViewItem *>', which has no cute class yet.")

  @staticmethod
  def applyModelChanges(*__, **_) -> Never:
    """
    Qt's 'bool QQuickItemViewPrivate::applyModelChanges(ChangeResult
    *insertionResult, ChangeResult *removalResult)': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.applyModelChanges' has no cute function "
        "yet. Qt's 'bool "
        "QQuickItemViewPrivate::applyModelChanges(ChangeResult "
        "*insertionResult, ChangeResult *removalResult)': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def applyPendingChanges(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::applyPendingChanges()': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.applyPendingChanges' has no cute function "
        "yet. Qt's 'void QQuickItemViewPrivate::applyPendingChanges()': "
        "leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def applyRemovalChange(*__, **_) -> Never:
    """
    Qt's 'bool QQuickItemViewPrivate::applyRemovalChange(const
    QQmlChangeSet::Change &removal, ChangeResult *changeResult, int
    *removedCount)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.applyRemovalChange' has no cute function "
        "yet. Qt's 'bool QQuickItemViewPrivate::applyRemovalChange(const "
        "QQmlChangeSet::Change &removal, ChangeResult *changeResult, int "
        "*removedCount)': takes a number to change where it is.")

  @staticmethod
  def connectModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::connectModel(QQuickItemView *q,
    QQmlDelegateModelPointer *model)': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.connectModel' has no cute function yet. "
        "Qt's 'void QQuickItemViewPrivate::connectModel(QQuickItemView *q, "
        "QQmlDelegateModelPointer *model)': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def disconnectModel(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::disconnectModel(QQuickItemView *q,
    QQmlDelegateModelPointer *model)': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.disconnectModel' has no cute function yet. "
        "Qt's 'void QQuickItemViewPrivate::disconnectModel(QQuickItemView "
        "*q, QQmlDelegateModelPointer *model)': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def emitCountChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::emitCountChanged()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'lcCount'.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.emitCountChanged' has no cute function yet. "
        "Qt's 'void QQuickItemViewPrivate::emitCountChanged()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'lcCount'.")

  @staticmethod
  def findMoveKeyIndex(*__, **_) -> Never:
    """
    Qt's 'int QQuickItemViewPrivate::findMoveKeyIndex(QQmlChangeSet::MoveKey
    key, const QList<QQmlChangeSet::Change> &changes) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.findMoveKeyIndex' has no cute function yet. "
        "Qt's 'int "
        "QQuickItemViewPrivate::findMoveKeyIndex(QQmlChangeSet::MoveKey "
        "key, const QList<QQmlChangeSet::Change> &changes) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def layout(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::layout()': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.layout' has no cute function yet. Qt's "
        "'void QQuickItemViewPrivate::layout()': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def maxExtentForAxis(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickItemViewPrivate::maxExtentForAxis(const AxisData
    &axisData, bool forXAxis) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.maxExtentForAxis' has no cute function yet. "
        "Qt's 'qreal QQuickItemViewPrivate::maxExtentForAxis(const AxisData "
        "&axisData, bool forXAxis) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def minExtentForAxis(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickItemViewPrivate::minExtentForAxis(const AxisData
    &axisData, bool forXAxis) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.minExtentForAxis' has no cute function yet. "
        "Qt's 'qreal QQuickItemViewPrivate::minExtentForAxis(const AxisData "
        "&axisData, bool forXAxis) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def positionViewAtIndex(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::positionViewAtIndex(int index, int
    mode)': leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.positionViewAtIndex' has no cute function "
        "yet. Qt's 'void QQuickItemViewPrivate::positionViewAtIndex(int "
        "index, int mode)': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def prepareRemoveTransitions(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::prepareRemoveTransitions(
    QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *> *removedItems)': names
    'QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.prepareRemoveTransitions' has no cute "
        "function yet. Qt's 'void "
        "QQuickItemViewPrivate::prepareRemoveTransitions(QMultiHash<QQmlChan"
        "geSet::MoveKey, FxViewItem *> *removedItems)': names "
        "'QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *>', which has no "
        "cute class yet.")

  @staticmethod
  def refill(*__, **_) -> Never:
    """
    - Qt's 'void QQuickItemViewPrivate::refill()': leans on
      'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QQuickItemViewPrivate::refill(qreal from, qreal to)': leans
      on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.refill' has no cute function yet. Qt's "
        "'void QQuickItemViewPrivate::refill()': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'void QQuickItemViewPrivate::refill(qreal "
        "from, qreal to)': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def refillOrLayout(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::refillOrLayout()': leans on
    'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.refillOrLayout' has no cute function yet. "
        "Qt's 'void QQuickItemViewPrivate::refillOrLayout()': leans on "
        "'QQuickItemViewPrivate::emitCountChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def regenerate(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::regenerate(bool orientationChanged)':
    leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.regenerate' has no cute function yet. Qt's "
        "'void QQuickItemViewPrivate::regenerate(bool orientationChanged)': "
        "leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateCurrent(*__, **_) -> Never:
    """
    Qt's 'void QQuickItemViewPrivate::updateCurrent(int modelIndex)': leans
    on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickItemViewPrivate.updateCurrent' has no cute function yet. "
        "Qt's 'void QQuickItemViewPrivate::updateCurrent(int modelIndex)': "
        "leans on 'QQuickItemViewPrivate::emitCountChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
