"""
QQuickTableViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTableViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QList
from ..QtQml import QQmlIncubator
from . import QQuickFlickablePrivate, QQuickSelectable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QModelIndex, QObject
  from ..QtCore import QPersistentModelIndex, QPoint, QPointF, QRect, QRectF
  from ..QtCore import QSize, QSizeF, QTypeRevision, QVariant
  from ..QtGui import QKeyEvent
  from . import FxTableItem, QQuickHandlerPoint, QQuickItem, QQuickTableView
  from . import QQuickTableViewAttached, QQuickTableViewPointerHandler
  from ..QtQmlModels import QQmlChangeSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']
  QKeyEvent = WAIT['QKeyEvent']
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQmlChangeSet = WAIT['QQmlChangeSet']
  QQuickHandlerPoint = WAIT['QQuickHandlerPoint']
  QQuickTableView = WAIT['QQuickTableView']
  QQuickTableViewPointerHandler = WAIT['QQuickTableViewPointerHandler']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTableViewPrivate(QQuickFlickablePrivate, QQuickSelectable):
  """
  The cute side of Qt's QQuickTableViewPrivate: a plain Python object
  standing in front of one C++ QQuickTableViewPrivate.

  It is built on the cute 'QQuickFlickablePrivate', as Qt's
  QQuickTableViewPrivate is built on Qt's QQuickFlickablePrivate, and has
  everything that class has. It is built on the cute 'QQuickSelectable' as
  well, as Qt's QQuickTableViewPrivate is built on Qt's QQuickSelectable too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableViewPrivate that has a ritual and that
  Python can call so far, 161 names in all: 'q_func', 'get', 'updatePolish',
  'init', 'getAttachedObject', 'modelIndexAtCell', 'cellAtModelIndex',
  'modelIndexToCellIndex', 'cellIsValid', 'sizeHintForColumn',
  'sizeHintForRow', 'calculateTableSize', 'isColumnHidden', 'isRowHidden',
  'getColumnLayoutWidth', 'getRowLayoutHeight', 'getColumnWidth',
  'getRowHeight', 'getEffectiveRowY', 'getEffectiveRowHeight',
  'getEffectiveColumnX', 'getEffectiveColumnWidth', 'getAlignmentContentX',
  'getAlignmentContentY', 'topRow', 'bottomRow', 'leftColumn', 'rightColumn',
  'rootSyncView', 'updateTableRecursive', 'updateTable',
  'relayoutTableItems', 'layoutVerticalEdge', 'layoutHorizontalEdge',
  'layoutTopLeftItem', 'layoutTableEdgeFromLoadRequest',
  'updateContentWidth', 'updateContentHeight', 'updateAverageColumnWidth',
  'updateAverageRowHeight', 'checkForVisibilityChanges', 'forceLayout',
  'updateExtents', 'syncLoadedTableRectFromLoadedTable',
  'syncLoadedTableFromLoadRequest', 'nextVisibleEdgeIndex',
  'nextVisibleEdgeIndexAroundLoadedTable', 'atTableEnd', 'edgeToArrayIndex',
  'clearEdgeSizeCache', 'canLoadTableEdge', 'canUnloadTableEdge',
  'nextEdgeToLoad', 'nextEdgeToUnload', 'cellWidth', 'cellHeight',
  'loadedTableItem', 'createFxTableItem', 'loadFxTableItem', 'unloadItem',
  'loadEdge', 'unloadEdge', 'loadAndUnloadVisibleEdges',
  'drainReusePoolAfterLoadRequest', 'processLoadRequest',
  'processRebuildTable', 'moveToNextRebuildState', 'loadInitialTable',
  'layoutAfterLoadingInitialTable', 'adjustViewportXAccordingToAlignment',
  'adjustViewportYAccordingToAlignment', 'cancelOvershootAfterLayout',
  'scheduleRebuildTable', 'updateCursor', 'updateEditItem',
  'updateContentSize', 'resolveImportVersion', 'createWrapperModel', 'qaim',
  'initItemCallback', 'itemCreatedCallback', 'itemPooledCallback',
  'itemReusedCallback', 'modelUpdated', 'updateItemProperties',
  'syncWithPendingChanges', 'syncDelegate', 'syncDelegateModelAccess',
  'modelImpl', 'setModelImpl', 'syncModel', 'syncSyncView',
  'syncPositionView', 'selectionSourceModel', 'syncRebuildOptions',
  'connectToModel', 'disconnectFromModel', 'rowsMovedCallback',
  'columnsMovedCallback', 'rowsInsertedCallback', 'rowsRemovedCallback',
  'columnsInsertedCallback', 'columnsRemovedCallback',
  'layoutChangedCallback', 'modelResetCallback', 'positionViewAtRow',
  'positionViewAtColumn', 'scrollToRow', 'scrollToColumn',
  'scheduleRebuildIfFastFlick', 'setLocalViewportX', 'setLocalViewportY',
  'syncViewportRect', 'syncViewportPosRecursive', 'selectedInSelectionModel',
  'selectionChangedInSelectionModel', 'updateSelectedOnAllDelegateItems',
  'setSelectedOnDelegateItem', 'currentInSelectionModel',
  'currentChangedInSelectionModel', 'setCurrentOnDelegateItem',
  'updateCurrentRowAndColumn', 'fetchMoreData', 'tableLayoutToString',
  'dumpTable', 'setRequiredProperty', 'handleTap', 'setCurrentIndexFromTap',
  'setCurrentIndex', 'setCurrentIndexFromKeyEvent', 'canEdit',
  'editFromKeyEvent', 'closeEditorAndCommit',
  'installEventFilterOnFocusObjectInsideEditItem',
  'selectionPointerHandlerTarget', 'hasSelection', 'startSelection',
  'setSelectionStartPos', 'setSelectionEndPos', 'clearSelection',
  'normalizeSelection', 'selectionRectangle', 'scrollTowardsPoint',
  'cancelSelectionTracking', 'clampedCellAtPos', 'updateSelection',
  'selection', 'initSectionDragHandler', 'destroySectionDragHandler',
  'setActivePointerHandler', 'activePointerHandler', 'moveSection',
  'initializeIndexMapping', 'clearIndexMapping', 'clearSection',
  'logicalRowIndex', 'logicalColumnIndex', 'visualRowIndex',
  'visualColumnIndex', 'setContainsDragOnDelegateItem', 'getEditCellIndex'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTableView *QQuickTableViewPrivate::q_func() const':
    takes in Python what 'QQuickTableView *QQuickTableViewPrivate::q_func()'
    takes.
  - Qt's 'QQuickTableViewPrivate::~QQuickTableViewPrivate()': the destructor:
    Python never removes a C++ QQuickTableViewPrivate.
  - Qt's 'void QQuickTableViewPrivate::fixup(AxisData &data, qreal minExtent,
    qreal maxExtent)': takes a type Python has no way to hand over yet.
  - Qt's 'std::vector<SectionData>
    &QQuickTableViewPrivate::visualIndicesForOrientation(Qt::Orientation
    orientation)': gives a type Python has no way to take yet.
  - Qt's 'std::vector<SectionData>
    &QQuickTableViewPrivate::logicalIndicesForOrientation(Qt::Orientation
    orientation)': gives a type Python has no way to take yet.
  - Qt's 'void QQuickTableViewPrivate::releaseItem(FxTableItem *fxTableItem,
    QQmlTableInstanceModel::ReusableFlag reusableFlag)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void
    QQuickTableViewPrivate::releaseLoadedItems(QQmlTableInstanceModel::
    ReusableFlag reusableFlag)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickTableViewPrivate::calculateTopLeft(QPoint &topLeft,
    QPointF &topLeftPos)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTableViewPrivate::dataChangedCallback(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTableViewPrivate::setCallback(std::function<void
    (CallBackFlag)> func)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 177 functions Qt declares: 4 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickTableViewPrivate is created at the first use, not by
    'QQuickTableViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableViewPrivate.
  - Each name of Qt's QQuickTableViewPrivate that has no cute function yet,
    '_q_componentFinalized', 'calculateTopLeft', 'compareModel',
    'dataChangedCallback', 'logicalIndicesForOrientation',
    'registerCallbackWhenBindingsAreEvaluated', 'releaseItem',
    'releaseLoadedItems', 'updateTableSize', 'visualIndicesForOrientation',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQuickTableViewPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class RebuildOption(CuteFlags, scoped=True):
    """
    The flags enum 'QQuickTableViewPrivate::RebuildOption' of Qt, with the 10
    names Qt gives in it. Qt names the type of its combinations
    'QQuickTableViewPrivate::RebuildOptions'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    All = 0x1
    LayoutOnly = 0x2
    ViewportOnly = 0x4
    CalculateNewTopLeftRow = 0x8
    CalculateNewTopLeftColumn = 0x10
    CalculateNewContentWidth = 0x20
    CalculateNewContentHeight = 0x40
    PositionViewAtRow = 0x80
    PositionViewAtColumn = 0x100

  RebuildOptions = RebuildOption

  class RebuildState(CuteNum, scoped=True):
    """
    The enum 'QQuickTableViewPrivate::RebuildState' of Qt, with the 10 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Begin = Kee[int](0)
    LoadInitalTable = Kee[int](1)
    VerifyTable = Kee[int](2)
    LayoutTable = Kee[int](3)
    CancelOvershoot = Kee[int](4)
    UpdateContentSize = Kee[int](5)
    PreloadColumns = Kee[int](6)
    PreloadRows = Kee[int](7)
    MovePreloadedItemsToPool = Kee[int](8)
    Done = Kee[int](9)

  class SectionState(CuteNum, scoped=True):
    """
    The enum 'QQuickTableViewPrivate::SectionState' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Idle = Kee[int](0)
    Moving = Kee[int](1)

  #  The classes Qt writes inside QQuickTableViewPrivate, each a class in
  #  here as in C++.

  class EdgeRange(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTableViewPrivate::EdgeRange: a plain Python
    object standing in front of one C++ QQuickTableViewPrivate::EdgeRange.

    C++ hands a QQuickTableViewPrivate::EdgeRange around as a copy, so every
    C++ QQuickTableViewPrivate::EdgeRange behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQuickTableViewPrivate::EdgeRange that has a
    ritual and that Python can call so far, 1 name in all: 'containsIndex'.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTableViewPrivate::EdgeRange::~EdgeRange()': the destructor:
      Python removes its C++ QQuickTableViewPrivate::EdgeRange by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuickTableViewPrivate::EdgeRange is created at the first use,
      not by 'QQuickTableViewPrivate::EdgeRange(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTableViewPrivate::EdgeRange back gives a copy
      the ritual made for Python, in a new cute
      QQuickTableViewPrivate::EdgeRange.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTableViewPrivate::EdgeRange'

    #  Qt's '~QQuickTableViewPrivate::EdgeRange()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTableViewPrivate::EdgeRange
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickTableViewPrivate9EdgeRangeD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickTableViewPrivate::EdgeRange::EdgeRange()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-edgerange.html#EdgeRange
      """
      #  QQuickTableViewPrivate::EdgeRange::EdgeRange()
      self._noteCreation(
          QQuickTableViewPrivate.EdgeRange, lambda: Rituals.call(
              'ritual_ZN22QQuickTableViewPrivate9EdgeRangeC1Ev',
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

    @overload(Qt.Edge, int)
    def containsIndex(self, edge: Qt.Edge, index: int) -> bool:
      """
      Calls Qt's 'bool
      QQuickTableViewPrivate::EdgeRange::containsIndex(Qt::Edge edge, int
      index)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-edgerange.html

      Parameters
      ----------

      edge : Qt.Edge
        Passed on as its number.

      index : int
        Passed on as it is.
      """
      #  bool QQuickTableViewPrivate::EdgeRange::containsIndex(Qt::Edge edge,
      #      int index)
      return self.uglySide.call(
          'ritual_ZN22QQuickTableViewPrivate9EdgeRange13containsIndexEN2Qt4'
          'EdgeEi',
          edge.value, index,
      )

  class SectionData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTableViewPrivate::SectionData: a plain Python
    object standing in front of one C++ QQuickTableViewPrivate::SectionData.

    C++ hands a QQuickTableViewPrivate::SectionData around as a copy, so
    every C++ QQuickTableViewPrivate::SectionData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickTableViewPrivate::SectionData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTableViewPrivate::SectionData::~SectionData()': the
      destructor: Python removes its C++ QQuickTableViewPrivate::SectionData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickTableViewPrivate::SectionData is created at the first
      use, not by 'QQuickTableViewPrivate::SectionData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTableViewPrivate::SectionData back gives a
      copy the ritual made for Python, in a new cute
      QQuickTableViewPrivate::SectionData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTableViewPrivate::SectionData'

    #  Qt's '~QQuickTableViewPrivate::SectionData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTableViewPrivate::SectionData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuickTableViewPrivate11SectionDataD1Ev'

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

  class TableEdgeLoadRequest(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTableViewPrivate::TableEdgeLoadRequest: a
    plain Python object standing in front of one C++
    QQuickTableViewPrivate::TableEdgeLoadRequest.

    C++ hands a QQuickTableViewPrivate::TableEdgeLoadRequest around as a
    copy, so every C++ QQuickTableViewPrivate::TableEdgeLoadRequest behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuickTableViewPrivate::TableEdgeLoadRequest that
    has a ritual and that Python can call so far, 13 names in all: 'begin',
    'markAsDone', 'isActive', 'currentCell', 'hasCurrentCell',
    'moveToNextCell', 'edge', 'row', 'column', 'incubationMode',
    'startPosition', 'toString', 'cellAt'. None can be made from Python: one
    comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'void QQuickTableViewPrivate::TableEdgeLoadRequest::begin(Qt::Edge
      edgeToLoad, int edgeIndex, const QList<int> visibleCellsInEdge,
      QQmlIncubator::IncubationMode incubationMode)': takes a type Python has
      no way to hand over yet.
    - Qt's
      'QQuickTableViewPrivate::TableEdgeLoadRequest::~TableEdgeLoadRequest(
      )': the destructor: Python removes its C++
      QQuickTableViewPrivate::TableEdgeLoadRequest by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QQuickTableViewPrivate::TableEdgeLoadRequest is created at the
      first use, not by 'QQuickTableViewPrivate::TableEdgeLoadRequest(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTableViewPrivate::TableEdgeLoadRequest back
      gives a copy the ritual made for Python, in a new cute
      QQuickTableViewPrivate::TableEdgeLoadRequest.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPoint = WAIT['QPoint']
      QPointF = WAIT['QPointF']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTableViewPrivate::TableEdgeLoadRequest'

    #  Qt's '~QQuickTableViewPrivate::TableEdgeLoadRequest()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QQuickTableViewPrivate::TableEdgeLoadRequest behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequestD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isActive(self) -> bool:
      """
      Calls Qt's 'bool
      QQuickTableViewPrivate::TableEdgeLoadRequest::isActive() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  bool QQuickTableViewPrivate::TableEdgeLoadRequest::isActive() const
      return self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest8isActiv'
          'eEv',
      )

    def currentCell(self) -> QPoint:
      """
      Calls Qt's 'QPoint
      QQuickTableViewPrivate::TableEdgeLoadRequest::currentCell() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Returns
      -------

      QPoint
        A new cute QPoint around the copy Qt gave back. Python owns it.
      """
      #  QPoint QQuickTableViewPrivate::TableEdgeLoadRequest::currentCell()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest11curren'
          'tCellEv',
      )
      from ..QtCore import QPoint
      return QPoint._cuteOwning(address)

    def hasCurrentCell(self) -> bool:
      """
      Calls Qt's 'bool
      QQuickTableViewPrivate::TableEdgeLoadRequest::hasCurrentCell() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  bool QQuickTableViewPrivate::TableEdgeLoadRequest::hasCurrentCell()
      #      const
      return self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest14hasCur'
          'rentCellEv',
      )

    def edge(self) -> Qt.Edge:
      """
      Calls Qt's 'Qt::Edge
      QQuickTableViewPrivate::TableEdgeLoadRequest::edge() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Returns
      -------

      Qt.Edge
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that 'Qt.Edge(number)'
        gives.
      """
      #  Qt::Edge QQuickTableViewPrivate::TableEdgeLoadRequest::edge() const
      return Qt.Edge(self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest4edgeEv',
      ))

    def row(self) -> int:
      """
      Calls Qt's 'int QQuickTableViewPrivate::TableEdgeLoadRequest::row()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  int QQuickTableViewPrivate::TableEdgeLoadRequest::row() const
      return self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest3rowEv',
      )

    def column(self) -> int:
      """
      Calls Qt's 'int QQuickTableViewPrivate::TableEdgeLoadRequest::column()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  int QQuickTableViewPrivate::TableEdgeLoadRequest::column() const
      return self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest6columnE'
          'v',
      )

    def incubationMode(self) -> QQmlIncubator.IncubationMode:
      """
      Calls Qt's 'QQmlIncubator::IncubationMode
      QQuickTableViewPrivate::TableEdgeLoadRequest::incubationMode() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Returns
      -------

      QQmlIncubator.IncubationMode
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that
        'QQmlIncubator.IncubationMode(number)' gives.
      """
      #  QQmlIncubator::IncubationMode
      #      QQuickTableViewPrivate::TableEdgeLoadRequest::incubationMode()
      #      const
      return QQmlIncubator.IncubationMode(self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest14incuba'
          'tionModeEv',
      ))

    def startPosition(self) -> QPointF:
      """
      Calls Qt's 'QPointF
      QQuickTableViewPrivate::TableEdgeLoadRequest::startPosition() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Returns
      -------

      QPointF
        A new cute QPointF around the copy Qt gave back. Python owns it.
      """
      #  QPointF
      #      QQuickTableViewPrivate::TableEdgeLoadRequest::startPosition()
      #      const
      address = self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest13startP'
          'ositionEv',
      )
      from ..QtCore import QPointF
      return QPointF._cuteOwning(address)

    def toString(self) -> str:
      """
      Calls Qt's 'QString
      QQuickTableViewPrivate::TableEdgeLoadRequest::toString() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQuickTableViewPrivate::TableEdgeLoadRequest::toString()
      #      const
      return self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest8toStrin'
          'gEv',
      )

    @overload(int)
    def cellAt(self, index: int) -> QPoint:
      """
      Calls Qt's 'QPoint
      QQuickTableViewPrivate::TableEdgeLoadRequest::cellAt(int index) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Parameters
      ----------

      index : int
        Passed on as it is.

      Returns
      -------

      QPoint
        A new cute QPoint around the copy Qt gave back. Python owns it.
      """
      #  QPoint QQuickTableViewPrivate::TableEdgeLoadRequest::cellAt(int
      #      index) const
      address = self.uglySide.call(
          'ritual_ZNK22QQuickTableViewPrivate20TableEdgeLoadRequest6cellAtE'
          'i',
          index,
      )
      from ..QtCore import QPoint
      return QPoint._cuteOwning(address)

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

    @overload(QPoint, QPointF, QQmlIncubator.IncubationMode)
    def begin(
        self,
        cell: QPoint,
        pos: QPointF,
        incubationMode: QQmlIncubator.IncubationMode,
    ) -> None:
      """
      Calls Qt's 'void
      QQuickTableViewPrivate::TableEdgeLoadRequest::begin(const QPoint &cell,
      const QPointF &pos, QQmlIncubator::IncubationMode incubationMode)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html

      Parameters
      ----------

      cell : QPoint
        Passed on as a value: Qt reads the C++ QPoint, which stays Python's
        own.

      pos : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      incubationMode : QQmlIncubator.IncubationMode
        Passed on as its number.
      """
      #  void QQuickTableViewPrivate::TableEdgeLoadRequest::begin(const
      #      QPoint &cell, const QPointF &pos, QQmlIncubator::IncubationMode
      #      incubationMode)
      self.uglySide.call(
          'ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest5beginERK'
          '6QPointRK7QPointFN13QQmlIncubator14IncubationModeE',
          self._valueOf(cell), self._valueOf(pos, 'QPointF'),
          incubationMode.value,
      )

    def markAsDone(self) -> None:
      """
      Calls Qt's 'void
      QQuickTableViewPrivate::TableEdgeLoadRequest::markAsDone()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  void QQuickTableViewPrivate::TableEdgeLoadRequest::markAsDone()
      self.uglySide.call(
          'ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest10markAsD'
          'oneEv',
      )

    def moveToNextCell(self) -> None:
      """
      Calls Qt's 'void
      QQuickTableViewPrivate::TableEdgeLoadRequest::moveToNextCell()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktableviewprivate-tableedgeloadrequest.html
      """
      #  void QQuickTableViewPrivate::TableEdgeLoadRequest::moveToNextCell()
      self.uglySide.call(
          'ritual_ZN22QQuickTableViewPrivate20TableEdgeLoadRequest14moveToN'
          'extCellEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTableView)
  @overload(NoneType)
  def get(q: Optional[QQuickTableView]) -> Optional[QQuickTableViewPrivate]:
    """
    Calls Qt's 'QQuickTableViewPrivate
    *QQuickTableViewPrivate::get(QQuickTableView *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewprivate.html#get

    Parameters
    ----------

    q : Optional[QQuickTableView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTableViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewPrivate *QQuickTableViewPrivate::get(QQuickTableView
    #      *q)
    address = Rituals.call(
        'ritual_ZN22QQuickTableViewPrivate3getEP15QQuickTableView',
        CuteMixin._addressOf(q),
    )
    return QQuickTableViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableViewPrivate'

  #  Qt's QQuickTableViewPrivate is built on more than one class. The part of
  #  a C++ QQuickTableViewPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickSelectable':
          'ritual_cast_QQuickTableViewPrivate_QQuickSelectable',
  }

  #  A C++ QQuickTableViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTableViewPrivate'

  #  The functions Qt calls itself that QQuickTableViewPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initItemCallback': (
          ('_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'itemCreatedCallback': (
          ('_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'itemPooledCallback': (
          ('_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'itemReusedCallback': (
          ('_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'modelUpdated': (
          ('_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQmlModels:QQmlChangeSet'),
               ('bool', 'number', ''),
           )),
      ),
      'updateItemProperties': (
          ('_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObjectb',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtCore:QObject'),
               ('bool', 'number', ''),
           )),
      ),
      'syncWithPendingChanges': (
          ('_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'syncDelegate': (
          ('_ZN22QQuickTableViewPrivate12syncDelegateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'syncDelegateModelAccess': (
          ('_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'modelImpl': (
          ('_ZNK22QQuickTableViewPrivate9modelImplEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'setModelImpl': (
          ('_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'syncModel': (
          ('_ZN22QQuickTableViewPrivate9syncModelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'syncSyncView': (
          ('_ZN22QQuickTableViewPrivate12syncSyncViewEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'syncPositionView': (
          ('_ZN22QQuickTableViewPrivate16syncPositionViewEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'selectionSourceModel': (
          ('_ZN22QQuickTableViewPrivate20selectionSourceModelEv',
           ('address', 'address', 'QtCore:QAbstractItemModel'),
           ()),
      ),
      'updateSelection': (
          ('_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'logicalRowIndex': (
          ('_ZNK22QQuickTableViewPrivate15logicalRowIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'logicalColumnIndex': (
          ('_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'visualRowIndex': (
          ('_ZNK22QQuickTableViewPrivate14visualRowIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'visualColumnIndex': (
          ('_ZNK22QQuickTableViewPrivate17visualColumnIndexEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
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

  @overload(QObject)
  @overload(NoneType)
  def getAttachedObject(
      self,
      object: Optional[QObject],
  ) -> Optional[QQuickTableViewAttached]:
    """
    Calls Qt's 'QQuickTableViewAttached
    *QQuickTableViewPrivate::getAttachedObject(const QObject *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getAttachedObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTableViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewAttached
    #      *QQuickTableViewPrivate::getAttachedObject(const QObject *object)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate17getAttachedObjectEPK7QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QQuickTableViewAttached
    return QQuickTableViewAttached._cuteAt(address)

  @overload(QPoint)
  def modelIndexAtCell(self, cell: QPoint) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::modelIndexAtCell(const QPoint
    &cell) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#modelIndexAtCell

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QQuickTableViewPrivate::modelIndexAtCell(const QPoint &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16modelIndexAtCellERK6QPoint',
        self._valueOf(cell),
    )

  @overload(int)
  def cellAtModelIndex(self, modelIndex: int) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableViewPrivate::cellAtModelIndex(int
    modelIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#cellAtModelIndex

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableViewPrivate::cellAtModelIndex(int modelIndex) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16cellAtModelIndexEi', modelIndex,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, bool)
  def modelIndexToCellIndex(
      self,
      modelIndex: QModelIndex,
      visualIndex: bool = True,
  ) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::modelIndexToCellIndex(const
    QModelIndex &modelIndex, bool visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#modelIndexToCellIndex

    Parameters
    ----------

    modelIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    visualIndex : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  int QQuickTableViewPrivate::modelIndexToCellIndex(const QModelIndex
    #      &modelIndex, bool visualIndex) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate21modelIndexToCellIndexERK11QMod'
        'elIndexb',
        self._valueOf(modelIndex), visualIndex,
    )

  @overload(QPoint)
  def cellIsValid(self, cell: QPoint) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::cellIsValid(const QPoint &cell)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#cellIsValid

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QQuickTableViewPrivate::cellIsValid(const QPoint &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate11cellIsValidERK6QPoint',
        self._valueOf(cell),
    )

  @overload(int)
  def sizeHintForColumn(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::sizeHintForColumn(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#sizeHintForColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::sizeHintForColumn(int column) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate17sizeHintForColumnEi', column,
    )

  @overload(int)
  def sizeHintForRow(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::sizeHintForRow(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#sizeHintForRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::sizeHintForRow(int row) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate14sizeHintForRowEi', row,
    )

  @overload(int)
  def isColumnHidden(self, column: int) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::isColumnHidden(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#isColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QQuickTableViewPrivate::isColumnHidden(int column) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate14isColumnHiddenEi', column,
    )

  @overload(int)
  def isRowHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::isRowHidden(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#isRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQuickTableViewPrivate::isRowHidden(int row) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate11isRowHiddenEi', row,
    )

  @overload(int)
  def getColumnWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getColumnWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getColumnWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate14getColumnWidthEi', column,
    )

  @overload(int)
  def getRowHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getRowHeight(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getRowHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate12getRowHeightEi', row,
    )

  @overload(int)
  def getEffectiveRowY(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getEffectiveRowY(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getEffectiveRowY

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getEffectiveRowY(int row) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16getEffectiveRowYEi', row,
    )

  @overload(int)
  def getEffectiveRowHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getEffectiveRowHeight(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getEffectiveRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getEffectiveRowHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate21getEffectiveRowHeightEi', row,
    )

  @overload(int)
  def getEffectiveColumnX(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getEffectiveColumnX(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getEffectiveColumnX

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getEffectiveColumnX(int column) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate19getEffectiveColumnXEi', column,
    )

  @overload(int)
  def getEffectiveColumnWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getEffectiveColumnWidth(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getEffectiveColumnWidth(int column)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate23getEffectiveColumnWidthEi',
        column,
    )

  def topRow(self) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::topRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewprivate.html#topRow
    """
    #  int QQuickTableViewPrivate::topRow() const
    return self.uglySide.call('ritual_ZNK22QQuickTableViewPrivate6topRowEv')

  def bottomRow(self) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::bottomRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#bottomRow
    """
    #  int QQuickTableViewPrivate::bottomRow() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate9bottomRowEv',
    )

  def leftColumn(self) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::leftColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#leftColumn
    """
    #  int QQuickTableViewPrivate::leftColumn() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate10leftColumnEv',
    )

  def rightColumn(self) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::rightColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#rightColumn
    """
    #  int QQuickTableViewPrivate::rightColumn() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate11rightColumnEv',
    )

  def rootSyncView(self) -> Optional[QQuickTableView]:
    """
    Calls Qt's 'QQuickTableView *QQuickTableViewPrivate::rootSyncView()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#rootSyncView

    Returns
    -------

    Optional[QQuickTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableView *QQuickTableViewPrivate::rootSyncView() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate12rootSyncViewEv',
    )
    from . import QQuickTableView
    return QQuickTableView._cuteAt(address)

  @overload(Qt.Edge, int)
  def nextVisibleEdgeIndex(self, edge: Qt.Edge, startIndex: int) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::nextVisibleEdgeIndex(Qt::Edge
    edge, int startIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#nextVisibleEdgeIndex

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.

    startIndex : int
      Passed on as it is.
    """
    #  int QQuickTableViewPrivate::nextVisibleEdgeIndex(Qt::Edge edge, int
    #      startIndex) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate20nextVisibleEdgeIndexEN2Qt4Edge'
        'Ei',
        edge.value, startIndex,
    )

  @overload(Qt.Edge)
  def nextVisibleEdgeIndexAroundLoadedTable(self, edge: Qt.Edge) -> int:
    """
    Calls Qt's 'int
    QQuickTableViewPrivate::nextVisibleEdgeIndexAroundLoadedTable(Qt::Edge
    edge) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  int QQuickTableViewPrivate::nextVisibleEdgeIndexAroundLoadedTable(
    #      Qt::Edge edge) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate37nextVisibleEdgeIndexAroundLoad'
        'edTableEN2Qt4EdgeE',
        edge.value,
    )

  @overload(Qt.Edge)
  def atTableEnd(self, edge: Qt.Edge) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#atTableEnd

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate10atTableEndEN2Qt4EdgeE',
        edge.value,
    )

  @overload(Qt.Edge, int)
  def atTableEnd(self, edge: Qt.Edge, startIndex: int) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge, int
    startIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#atTableEnd

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.

    startIndex : int
      Passed on as it is.
    """
    #  bool QQuickTableViewPrivate::atTableEnd(Qt::Edge edge, int startIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate10atTableEndEN2Qt4EdgeEi',
        edge.value, startIndex,
    )

  @overload(Qt.Edge)
  def edgeToArrayIndex(self, edge: Qt.Edge) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::edgeToArrayIndex(Qt::Edge edge)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#edgeToArrayIndex

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  int QQuickTableViewPrivate::edgeToArrayIndex(Qt::Edge edge) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16edgeToArrayIndexEN2Qt4EdgeE',
        edge.value,
    )

  @overload(Qt.Edge, QRectF)
  def canLoadTableEdge(self, tableEdge: Qt.Edge, fillRect: QRectF) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::canLoadTableEdge(Qt::Edge
    tableEdge, const QRectF fillRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#canLoadTableEdge

    Parameters
    ----------

    tableEdge : Qt.Edge
      Passed on as its number.

    fillRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QQuickTableViewPrivate::canLoadTableEdge(Qt::Edge tableEdge,
    #      const QRectF fillRect) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16canLoadTableEdgeEN2Qt4EdgeE6QR'
        'ectF',
        tableEdge.value, self._valueOf(fillRect),
    )

  @overload(Qt.Edge, QRectF)
  def canUnloadTableEdge(self, tableEdge: Qt.Edge, fillRect: QRectF) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::canUnloadTableEdge(Qt::Edge
    tableEdge, const QRectF fillRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#canUnloadTableEdge

    Parameters
    ----------

    tableEdge : Qt.Edge
      Passed on as its number.

    fillRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QQuickTableViewPrivate::canUnloadTableEdge(Qt::Edge tableEdge,
    #      const QRectF fillRect) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate18canUnloadTableEdgeEN2Qt4EdgeE6'
        'QRectF',
        tableEdge.value, self._valueOf(fillRect),
    )

  @overload(QPoint)
  def cellWidth(self, cell: QPoint) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::cellWidth(const QPoint &cell)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#cellWidth

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  qreal QQuickTableViewPrivate::cellWidth(const QPoint &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate9cellWidthERK6QPoint',
        self._valueOf(cell),
    )

  @overload(QPoint)
  def cellHeight(self, cell: QPoint) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::cellHeight(const QPoint &cell)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#cellHeight

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  qreal QQuickTableViewPrivate::cellHeight(const QPoint &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate10cellHeightERK6QPoint',
        self._valueOf(cell),
    )

  @overload(QPoint)
  def loadedTableItem(self, cell: QPoint) -> Optional[FxTableItem]:
    """
    Calls Qt's 'FxTableItem *QQuickTableViewPrivate::loadedTableItem(const
    QPoint &cell) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#loadedTableItem

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[FxTableItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxTableItem *QQuickTableViewPrivate::loadedTableItem(const QPoint
    #      &cell) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate15loadedTableItemERK6QPoint',
        self._valueOf(cell),
    )
    from . import FxTableItem
    return FxTableItem._cuteAt(address)

  @overload(QVariant)
  def qaim(self, modelAsVariant: QVariant) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QQuickTableViewPrivate::qaim(QVariant
    modelAsVariant) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewprivate.html#qaim

    Parameters
    ----------

    modelAsVariant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQuickTableViewPrivate::qaim(QVariant
    #      modelAsVariant) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate4qaimE8QVariant',
        self._valueOf(modelAsVariant),
    )
    return QAbstractItemModel._cuteAt(address)

  def modelImpl(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTableViewPrivate::modelImpl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#modelImpl

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTableViewPrivate::modelImpl() const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate9modelImplEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate9modelImplEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QPoint)
  def selectedInSelectionModel(self, cell: QPoint) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::selectedInSelectionModel(const
    QPoint &cell) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QQuickTableViewPrivate::selectedInSelectionModel(const QPoint
    #      &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate24selectedInSelectionModelERK6QP'
        'oint',
        self._valueOf(cell),
    )

  @overload(QPoint)
  def currentInSelectionModel(self, cell: QPoint) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::currentInSelectionModel(const
    QPoint &cell) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QQuickTableViewPrivate::currentInSelectionModel(const QPoint
    #      &cell) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate23currentInSelectionModelERK6QPo'
        'int',
        self._valueOf(cell),
    )

  def tableLayoutToString(self) -> str:
    """
    Calls Qt's 'QString QQuickTableViewPrivate::tableLayoutToString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#tableLayoutToString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTableViewPrivate::tableLayoutToString() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate19tableLayoutToStringEv',
    )

  def selectionPointerHandlerTarget(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickTableViewPrivate::selectionPointerHandlerTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTableViewPrivate::selectionPointerHandlerTarget()
    #      const
    ritual = (
        'ritual_ZNK22QQuickTableViewPrivate29selectionPointerHandlerTargetE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QQuickTableViewPrivate29selectionPointerHandlerT'
          'argetEv')
    address = self.uglySide.call(ritual)
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def hasSelection(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::hasSelection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#hasSelection
    """
    #  bool QQuickTableViewPrivate::hasSelection() const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate12hasSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate12hasSelectionEv'
    return self.uglySide.call(ritual)

  def selectionRectangle(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickTableViewPrivate::selectionRectangle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#selectionRectangle

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickTableViewPrivate::selectionRectangle() const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate18selectionRectangleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate18selectionRectangleEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QPointF)
  def clampedCellAtPos(self, pos: QPointF) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableViewPrivate::clampedCellAtPos(const QPointF
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#clampedCellAtPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableViewPrivate::clampedCellAtPos(const QPointF &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16clampedCellAtPosERK7QPointF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def selection(self) -> QRect:
    """
    Calls Qt's 'QRect QQuickTableViewPrivate::selection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#selection

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickTableViewPrivate::selection() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate9selectionEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def activePointerHandler(self) -> Optional[QQuickTableViewPointerHandler]:
    """
    Calls Qt's 'QQuickTableViewPointerHandler
    *QQuickTableViewPrivate::activePointerHandler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#activePointerHandler

    Returns
    -------

    Optional[QQuickTableViewPointerHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewPointerHandler
    #      *QQuickTableViewPrivate::activePointerHandler() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate20activePointerHandlerEv',
    )
    from . import QQuickTableViewPointerHandler
    return QQuickTableViewPointerHandler._cuteAt(address)

  @overload(int)
  def logicalRowIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::logicalRowIndex(const int
    visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#logicalRowIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QQuickTableViewPrivate::logicalRowIndex(const int visualIndex)
    #      const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate15logicalRowIndexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate15logicalRowIndexEi'
    return self.uglySide.call(ritual, visualIndex)

  @overload(int)
  def logicalColumnIndex(self, visualIndex: int) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::logicalColumnIndex(const int
    visualIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#logicalColumnIndex

    Parameters
    ----------

    visualIndex : int
      Passed on as it is.
    """
    #  int QQuickTableViewPrivate::logicalColumnIndex(const int visualIndex)
    #      const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate18logicalColumnIndexEi'
    return self.uglySide.call(ritual, visualIndex)

  @overload(int)
  def visualRowIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::visualRowIndex(const int
    logicalIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#visualRowIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QQuickTableViewPrivate::visualRowIndex(const int logicalIndex)
    #      const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate14visualRowIndexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate14visualRowIndexEi'
    return self.uglySide.call(ritual, logicalIndex)

  @overload(int)
  def visualColumnIndex(self, logicalIndex: int) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::visualColumnIndex(const int
    logicalIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#visualColumnIndex

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  int QQuickTableViewPrivate::visualColumnIndex(const int logicalIndex)
    #      const
    ritual = 'ritual_ZNK22QQuickTableViewPrivate17visualColumnIndexEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickTableViewPrivate17visualColumnIndexEi'
    return self.uglySide.call(ritual, logicalIndex)

  @overload(QModelIndex)
  def getEditCellIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QQuickTableViewPrivate::getEditCellIndex(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getEditCellIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQuickTableViewPrivate::getEditCellIndex(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QQuickTableViewPrivate16getEditCellIndexERK11QModelInd'
        'ex',
        self._valueOf(index),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModelImpl(self, newModel: QVariant) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setModelImpl(const QVariant
    &newModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setModelImpl

    Parameters
    ----------

    newModel : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::setModelImpl(const QVariant &newModel)
    ritual = 'ritual_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate12setModelImplERK8QVariant')
    self.uglySide.call(ritual, self._valueOf(newModel))

  @overload(float)
  def setLocalViewportX(self, contentX: float) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setLocalViewportX(qreal
    contentX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setLocalViewportX

    Parameters
    ----------

    contentX : float
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setLocalViewportX(qreal contentX)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17setLocalViewportXEd', contentX,
    )

  @overload(float)
  def setLocalViewportY(self, contentY: float) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setLocalViewportY(qreal
    contentY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setLocalViewportY

    Parameters
    ----------

    contentY : float
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setLocalViewportY(qreal contentY)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17setLocalViewportYEd', contentY,
    )

  @overload(QModelIndex, bool)
  def setSelectedOnDelegateItem(
      self,
      modelIndex: QModelIndex,
      select: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setSelectedOnDelegateItem(const
    QModelIndex &modelIndex, bool select)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    modelIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    select : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setSelectedOnDelegateItem(const
    #      QModelIndex &modelIndex, bool select)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate25setSelectedOnDelegateItemERK11Q'
        'ModelIndexb',
        self._valueOf(modelIndex), select,
    )

  @overload(QModelIndex, bool)
  def setCurrentOnDelegateItem(
      self,
      index: QModelIndex,
      isCurrent: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setCurrentOnDelegateItem(const
    QModelIndex &index, bool isCurrent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    isCurrent : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setCurrentOnDelegateItem(const
    #      QModelIndex &index, bool isCurrent)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate24setCurrentOnDelegateItemERK11QM'
        'odelIndexb',
        self._valueOf(index), isCurrent,
    )

  @overload(str, QVariant, int, QObject, bool)
  @overload(str, QVariant, int, NoneType, bool)
  @overload(NoneType, QVariant, int, QObject, bool)
  @overload(NoneType, QVariant, int, NoneType, bool)
  def setRequiredProperty(
      self,
      property: Optional[str],
      value: QVariant,
      serializedModelIndex: int,
      object: Optional[QObject],
      init: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setRequiredProperty(const char
    *property, const QVariant &value, int serializedModelIndex, QObject
    *object, bool init)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setRequiredProperty

    Parameters
    ----------

    property : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    serializedModelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    init : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setRequiredProperty(const char *property,
    #      const QVariant &value, int serializedModelIndex, QObject *object,
    #      bool init)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate19setRequiredPropertyEPKcRK8QVari'
        'antiP7QObjectb',
        self._bytesOf(property), self._valueOf(value), serializedModelIndex,
        self._addressOf(object, 'QObject'), init,
    )

  @overload(QPointF)
  def setCurrentIndexFromTap(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setCurrentIndexFromTap(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setCurrentIndexFromTap

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::setCurrentIndexFromTap(const QPointF
    #      &pos)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22setCurrentIndexFromTapERK7QPoin'
        'tF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPoint)
  def setCurrentIndex(self, cell: QPoint) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setCurrentIndex(const QPoint
    &cell)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setCurrentIndex

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::setCurrentIndex(const QPoint &cell)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate15setCurrentIndexERK6QPoint',
        self._valueOf(cell),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def setCurrentIndexFromKeyEvent(self, e: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickTableViewPrivate::setCurrentIndexFromKeyEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTableViewPrivate::setCurrentIndexFromKeyEvent(QKeyEvent *e)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate27setCurrentIndexFromKeyEventEP9Q'
        'KeyEvent',
        self._addressOf(e),
    )

  @overload(QPointF)
  def setSelectionStartPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setSelectionStartPos(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setSelectionStartPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::setSelectionStartPos(const QPointF &pos)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate20setSelectionStartPosERK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate20setSelectionStartPosERK7Q'
          'PointF')
    self.uglySide.call(ritual, self._valueOf(pos, 'QPointF'))

  @overload(QPointF)
  def setSelectionEndPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setSelectionEndPos(const QPointF
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#setSelectionEndPos

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::setSelectionEndPos(const QPointF &pos)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate18setSelectionEndPosERK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate18setSelectionEndPosERK7QPo'
          'intF')
    self.uglySide.call(ritual, self._valueOf(pos, 'QPointF'))

  @overload(QQuickTableViewPointerHandler)
  @overload(NoneType)
  def setActivePointerHandler(
      self,
      handler: Optional[QQuickTableViewPointerHandler],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::setActivePointerHandler(
    QQuickTableViewPointerHandler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    handler : Optional[QQuickTableViewPointerHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewPrivate::setActivePointerHandler(
    #      QQuickTableViewPointerHandler *handler)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate23setActivePointerHandlerEP29QQui'
        'ckTableViewPointerHandler',
        self._addressOf(handler),
    )

  @overload(QModelIndex, bool)
  def setContainsDragOnDelegateItem(
      self,
      modelIndex: QModelIndex,
      overlay: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::setContainsDragOnDelegateItem(const QModelIndex
    &modelIndex, bool overlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    modelIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    overlay : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::setContainsDragOnDelegateItem(const
    #      QModelIndex &modelIndex, bool overlay)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate29setContainsDragOnDelegateItemER'
        'K11QModelIndexb',
        self._valueOf(modelIndex), overlay,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTableViewPrivate::QQuickTableViewPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#QQuickTableViewPrivate
    """
    #  QQuickTableViewPrivate::QQuickTableViewPrivate()
    self._noteCreation(QQuickTableViewPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickTableViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickTableView]:
    """
    Calls Qt's 'QQuickTableView *QQuickTableViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableView *QQuickTableViewPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate6q_funcEv',
    )
    from . import QQuickTableView
    return QQuickTableView._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updatePolish
    """
    #  void QQuickTableViewPrivate::updatePolish()
    ritual = 'ritual_ZN22QQuickTableViewPrivate12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate12updatePolishEv'
    self.uglySide.call(ritual)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableviewprivate.html#init
    """
    #  void QQuickTableViewPrivate::init()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate4initEv')

  def calculateTableSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickTableViewPrivate::calculateTableSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#calculateTableSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickTableViewPrivate::calculateTableSize()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18calculateTableSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def getColumnLayoutWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getColumnLayoutWidth(int
    column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getColumnLayoutWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getColumnLayoutWidth(int column)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20getColumnLayoutWidthEi', column,
    )

  @overload(int)
  def getRowLayoutHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getRowLayoutHeight(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getRowLayoutHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableViewPrivate::getRowLayoutHeight(int row)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18getRowLayoutHeightEi', row,
    )

  @overload(int, Qt.Alignment, float, QRectF)
  def getAlignmentContentX(
      self,
      column: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: QRectF,
  ) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getAlignmentContentX(int
    column, Qt::Alignment alignment, const qreal offset, const QRectF
    &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getAlignmentContentX

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  qreal QQuickTableViewPrivate::getAlignmentContentX(int column,
    #      Qt::Alignment alignment, const qreal offset, const QRectF
    #      &subRect)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20getAlignmentContentXEi6QFlagsIN'
        '2Qt13AlignmentFlagEEdRK6QRectF',
        column, alignment.value, offset, self._valueOf(subRect),
    )

  @overload(int, Qt.Alignment, float, QRectF)
  def getAlignmentContentY(
      self,
      row: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: QRectF,
  ) -> float:
    """
    Calls Qt's 'qreal QQuickTableViewPrivate::getAlignmentContentY(int row,
    Qt::Alignment alignment, const qreal offset, const QRectF &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#getAlignmentContentY

    Parameters
    ----------

    row : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  qreal QQuickTableViewPrivate::getAlignmentContentY(int row,
    #      Qt::Alignment alignment, const qreal offset, const QRectF
    #      &subRect)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20getAlignmentContentYEi6QFlagsIN'
        '2Qt13AlignmentFlagEEdRK6QRectF',
        row, alignment.value, offset, self._valueOf(subRect),
    )

  def updateTableRecursive(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::updateTableRecursive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateTableRecursive
    """
    #  bool QQuickTableViewPrivate::updateTableRecursive()
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20updateTableRecursiveEv',
    )

  def updateTable(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::updateTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateTable
    """
    #  bool QQuickTableViewPrivate::updateTable()
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate11updateTableEv',
    )

  def relayoutTableItems(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::relayoutTableItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#relayoutTableItems
    """
    #  void QQuickTableViewPrivate::relayoutTableItems()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18relayoutTableItemsEv',
    )

  @overload(Qt.Edge)
  def layoutVerticalEdge(self, tableEdge: Qt.Edge) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::layoutVerticalEdge(Qt::Edge
    tableEdge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#layoutVerticalEdge

    Parameters
    ----------

    tableEdge : Qt.Edge
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::layoutVerticalEdge(Qt::Edge tableEdge)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18layoutVerticalEdgeEN2Qt4EdgeE',
        tableEdge.value,
    )

  @overload(Qt.Edge)
  def layoutHorizontalEdge(self, tableEdge: Qt.Edge) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::layoutHorizontalEdge(Qt::Edge
    tableEdge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#layoutHorizontalEdge

    Parameters
    ----------

    tableEdge : Qt.Edge
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::layoutHorizontalEdge(Qt::Edge tableEdge)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20layoutHorizontalEdgeEN2Qt4EdgeE',
        tableEdge.value,
    )

  def layoutTopLeftItem(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::layoutTopLeftItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#layoutTopLeftItem
    """
    #  void QQuickTableViewPrivate::layoutTopLeftItem()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17layoutTopLeftItemEv',
    )

  def layoutTableEdgeFromLoadRequest(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::layoutTableEdgeFromLoadRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::layoutTableEdgeFromLoadRequest()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate30layoutTableEdgeFromLoadRequestE'
        'v',
    )

  def updateContentWidth(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateContentWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateContentWidth
    """
    #  void QQuickTableViewPrivate::updateContentWidth()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18updateContentWidthEv',
    )

  def updateContentHeight(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateContentHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateContentHeight
    """
    #  void QQuickTableViewPrivate::updateContentHeight()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate19updateContentHeightEv',
    )

  def updateAverageColumnWidth(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateAverageColumnWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::updateAverageColumnWidth()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate24updateAverageColumnWidthEv',
    )

  def updateAverageRowHeight(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateAverageRowHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateAverageRowHeight
    """
    #  void QQuickTableViewPrivate::updateAverageRowHeight()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22updateAverageRowHeightEv',
    )

  def checkForVisibilityChanges(self) -> RebuildOptions:
    """
    Calls Qt's 'RebuildOptions
    QQuickTableViewPrivate::checkForVisibilityChanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Returns
    -------

    RebuildOptions
      The value standing for the combination Qt gave back.
    """
    #  RebuildOptions QQuickTableViewPrivate::checkForVisibilityChanges()
    return QQuickTableViewPrivate.RebuildOptions(self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate25checkForVisibilityChangesEv',
    ))

  @overload(bool)
  def forceLayout(self, immediate: bool) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::forceLayout(bool immediate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#forceLayout

    Parameters
    ----------

    immediate : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::forceLayout(bool immediate)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate11forceLayoutEb', immediate,
    )

  def updateExtents(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateExtents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateExtents
    """
    #  void QQuickTableViewPrivate::updateExtents()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate13updateExtentsEv')

  def syncLoadedTableRectFromLoadedTable(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::syncLoadedTableRectFromLoadedTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::syncLoadedTableRectFromLoadedTable()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate34syncLoadedTableRectFromLoadedTa'
        'bleEv',
    )

  def syncLoadedTableFromLoadRequest(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::syncLoadedTableFromLoadRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::syncLoadedTableFromLoadRequest()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate30syncLoadedTableFromLoadRequestE'
        'v',
    )

  def clearEdgeSizeCache(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::clearEdgeSizeCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#clearEdgeSizeCache
    """
    #  void QQuickTableViewPrivate::clearEdgeSizeCache()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18clearEdgeSizeCacheEv',
    )

  @overload(QRectF)
  def nextEdgeToLoad(self, rect: QRectF) -> Qt.Edge:
    """
    Calls Qt's 'Qt::Edge QQuickTableViewPrivate::nextEdgeToLoad(const QRectF
    rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#nextEdgeToLoad

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    Qt.Edge
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Edge(number)' gives.
    """
    #  Qt::Edge QQuickTableViewPrivate::nextEdgeToLoad(const QRectF rect)
    return Qt.Edge(self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate14nextEdgeToLoadE6QRectF',
        self._valueOf(rect),
    ))

  @overload(QRectF)
  def nextEdgeToUnload(self, rect: QRectF) -> Qt.Edge:
    """
    Calls Qt's 'Qt::Edge QQuickTableViewPrivate::nextEdgeToUnload(const
    QRectF rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#nextEdgeToUnload

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    Qt.Edge
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Edge(number)' gives.
    """
    #  Qt::Edge QQuickTableViewPrivate::nextEdgeToUnload(const QRectF rect)
    return Qt.Edge(self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate16nextEdgeToUnloadE6QRectF',
        self._valueOf(rect),
    ))

  @overload(QPoint, QQmlIncubator.IncubationMode)
  def createFxTableItem(
      self,
      cell: QPoint,
      incubationMode: QQmlIncubator.IncubationMode,
  ) -> Optional[FxTableItem]:
    """
    Calls Qt's 'FxTableItem *QQuickTableViewPrivate::createFxTableItem(const
    QPoint &cell, QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#createFxTableItem

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number.

    Returns
    -------

    Optional[FxTableItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxTableItem *QQuickTableViewPrivate::createFxTableItem(const QPoint
    #      &cell, QQmlIncubator::IncubationMode incubationMode)
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17createFxTableItemERK6QPointN13Q'
        'QmlIncubator14IncubationModeE',
        self._valueOf(cell), incubationMode.value,
    )
    from . import FxTableItem
    return FxTableItem._cuteAt(address)

  @overload(QPoint, QQmlIncubator.IncubationMode)
  def loadFxTableItem(
      self,
      cell: QPoint,
      incubationMode: QQmlIncubator.IncubationMode,
  ) -> Optional[FxTableItem]:
    """
    Calls Qt's 'FxTableItem *QQuickTableViewPrivate::loadFxTableItem(const
    QPoint &cell, QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#loadFxTableItem

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number.

    Returns
    -------

    Optional[FxTableItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FxTableItem *QQuickTableViewPrivate::loadFxTableItem(const QPoint
    #      &cell, QQmlIncubator::IncubationMode incubationMode)
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate15loadFxTableItemERK6QPointN13QQm'
        'lIncubator14IncubationModeE',
        self._valueOf(cell), incubationMode.value,
    )
    from . import FxTableItem
    return FxTableItem._cuteAt(address)

  @overload(QPoint)
  def unloadItem(self, cell: QPoint) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::unloadItem(const QPoint &cell)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#unloadItem

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QQuickTableViewPrivate::unloadItem(const QPoint &cell)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate10unloadItemERK6QPoint',
        self._valueOf(cell),
    )

  @overload(Qt.Edge, QQmlIncubator.IncubationMode)
  def loadEdge(
      self,
      edge: Qt.Edge,
      incubationMode: QQmlIncubator.IncubationMode,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::loadEdge(Qt::Edge edge,
    QQmlIncubator::IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#loadEdge

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::loadEdge(Qt::Edge edge,
    #      QQmlIncubator::IncubationMode incubationMode)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate8loadEdgeEN2Qt4EdgeEN13QQmlIncuba'
        'tor14IncubationModeE',
        edge.value, incubationMode.value,
    )

  @overload(Qt.Edge)
  def unloadEdge(self, edge: Qt.Edge) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::unloadEdge(Qt::Edge edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#unloadEdge

    Parameters
    ----------

    edge : Qt.Edge
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::unloadEdge(Qt::Edge edge)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate10unloadEdgeEN2Qt4EdgeE',
        edge.value,
    )

  @overload()
  @overload(QQmlIncubator.IncubationMode)
  def loadAndUnloadVisibleEdges(
      self,
      incubationMode: QQmlIncubator.IncubationMode = (
          QQmlIncubator.IncubationMode.AsynchronousIfNested),
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::loadAndUnloadVisibleEdges(QQmlIncubator::
    IncubationMode incubationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    incubationMode : QQmlIncubator.IncubationMode
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlIncubator.IncubationMode.AsynchronousIfNested.
    """
    #  void QQuickTableViewPrivate::loadAndUnloadVisibleEdges(QQmlIncubator::
    #      IncubationMode incubationMode)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate25loadAndUnloadVisibleEdgesEN13QQ'
        'mlIncubator14IncubationModeE',
        incubationMode.value,
    )

  def drainReusePoolAfterLoadRequest(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::drainReusePoolAfterLoadRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::drainReusePoolAfterLoadRequest()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate30drainReusePoolAfterLoadRequestE'
        'v',
    )

  def processLoadRequest(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::processLoadRequest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#processLoadRequest
    """
    #  void QQuickTableViewPrivate::processLoadRequest()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18processLoadRequestEv',
    )

  def processRebuildTable(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::processRebuildTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#processRebuildTable
    """
    #  void QQuickTableViewPrivate::processRebuildTable()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate19processRebuildTableEv',
    )

  def moveToNextRebuildState(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::moveToNextRebuildState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#moveToNextRebuildState
    """
    #  bool QQuickTableViewPrivate::moveToNextRebuildState()
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22moveToNextRebuildStateEv',
    )

  def loadInitialTable(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::loadInitialTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#loadInitialTable
    """
    #  void QQuickTableViewPrivate::loadInitialTable()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate16loadInitialTableEv',
    )

  def layoutAfterLoadingInitialTable(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::layoutAfterLoadingInitialTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::layoutAfterLoadingInitialTable()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate30layoutAfterLoadingInitialTableE'
        'v',
    )

  def adjustViewportXAccordingToAlignment(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::adjustViewportXAccordingToAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::adjustViewportXAccordingToAlignment()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate35adjustViewportXAccordingToAlign'
        'mentEv',
    )

  def adjustViewportYAccordingToAlignment(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::adjustViewportYAccordingToAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::adjustViewportYAccordingToAlignment()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate35adjustViewportYAccordingToAlign'
        'mentEv',
    )

  def cancelOvershootAfterLayout(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::cancelOvershootAfterLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::cancelOvershootAfterLayout()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate26cancelOvershootAfterLayoutEv',
    )

  @overload(RebuildOptions)
  def scheduleRebuildTable(self, options: RebuildOptions) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::scheduleRebuildTable(QQuickTableViewPrivate::
    RebuildOptions options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#scheduleRebuildTable

    Parameters
    ----------

    options : RebuildOptions
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::scheduleRebuildTable(
    #      QQuickTableViewPrivate::RebuildOptions options)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20scheduleRebuildTableE6QFlagsINS'
        '_13RebuildOptionEE',
        options.value,
    )

  def updateCursor(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateCursor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateCursor
    """
    #  void QQuickTableViewPrivate::updateCursor()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate12updateCursorEv')

  def updateEditItem(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateEditItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateEditItem
    """
    #  void QQuickTableViewPrivate::updateEditItem()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate14updateEditItemEv')

  def updateContentSize(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateContentSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateContentSize
    """
    #  void QQuickTableViewPrivate::updateContentSize()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17updateContentSizeEv',
    )

  def resolveImportVersion(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision
    QQuickTableViewPrivate::resolveImportVersion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#resolveImportVersion

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQuickTableViewPrivate::resolveImportVersion()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20resolveImportVersionEv',
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def createWrapperModel(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::createWrapperModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#createWrapperModel
    """
    #  void QQuickTableViewPrivate::createWrapperModel()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18createWrapperModelEv',
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def initItemCallback(
      self,
      modelIndex: int,
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::initItemCallback(int modelIndex,
    QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#initItemCallback

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewPrivate::initItemCallback(int modelIndex, QObject
    #      *item)
    ritual = 'ritual_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate16initItemCallbackEiP7QObje'
          'ct')
    self.uglySide.call(ritual, modelIndex, self._addressOf(item, 'QObject'))

  @overload(int, QObject)
  @overload(int, NoneType)
  def itemCreatedCallback(
      self,
      modelIndex: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::itemCreatedCallback(int
    modelIndex, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#itemCreatedCallback

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewPrivate::itemCreatedCallback(int modelIndex,
    #      QObject *object)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate19itemCreatedCallbackEiP7QO'
          'bject')
    self.uglySide.call(
        ritual, modelIndex, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def itemPooledCallback(
      self,
      modelIndex: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::itemPooledCallback(int
    modelIndex, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#itemPooledCallback

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewPrivate::itemPooledCallback(int modelIndex,
    #      QObject *object)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate18itemPooledCallbackEiP7QOb'
          'ject')
    self.uglySide.call(
        ritual, modelIndex, self._addressOf(object, 'QObject'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def itemReusedCallback(
      self,
      modelIndex: int,
      object: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::itemReusedCallback(int
    modelIndex, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#itemReusedCallback

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableViewPrivate::itemReusedCallback(int modelIndex,
    #      QObject *object)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate18itemReusedCallbackEiP7QOb'
          'ject')
    self.uglySide.call(
        ritual, modelIndex, self._addressOf(object, 'QObject'),
    )

  @overload(QQmlChangeSet, bool)
  def modelUpdated(self, changeSet: QQmlChangeSet, reset: bool) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet
    &changeSet, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#modelUpdated

    Parameters
    ----------

    changeSet : QQmlChangeSet
      Passed on as a value: Qt reads the C++ QQmlChangeSet, which stays
      Python's own.

    reset : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::modelUpdated(const QQmlChangeSet
    #      &changeSet, bool reset)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChangeSetb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate12modelUpdatedERK13QQmlChan'
          'geSetb')
    self.uglySide.call(ritual, self._valueOf(changeSet), reset)

  @overload(int, QObject, bool)
  @overload(int, NoneType, bool)
  def updateItemProperties(
      self,
      flatIndex: int,
      object: Optional[QObject],
      init: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateItemProperties(int
    flatIndex, QObject *object, bool init)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateItemProperties

    Parameters
    ----------

    flatIndex : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    init : bool
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::updateItemProperties(int flatIndex,
    #      QObject *object, bool init)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7QObject'
        'b')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate20updateItemPropertiesEiP7Q'
          'Objectb')
    self.uglySide.call(
        ritual, flatIndex, self._addressOf(object, 'QObject'), init,
    )

  def syncWithPendingChanges(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncWithPendingChanges()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncWithPendingChanges
    """
    #  void QQuickTableViewPrivate::syncWithPendingChanges()
    ritual = 'ritual_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate22syncWithPendingChangesEv')
    self.uglySide.call(ritual)

  def syncDelegate(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncDelegate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncDelegate
    """
    #  void QQuickTableViewPrivate::syncDelegate()
    ritual = 'ritual_ZN22QQuickTableViewPrivate12syncDelegateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate12syncDelegateEv'
    self.uglySide.call(ritual)

  def syncDelegateModelAccess(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncDelegateModelAccess()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::syncDelegateModelAccess()
    ritual = 'ritual_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate23syncDelegateModelAccessEv')
    self.uglySide.call(ritual)

  def syncModel(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncModel
    """
    #  void QQuickTableViewPrivate::syncModel()
    ritual = 'ritual_ZN22QQuickTableViewPrivate9syncModelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate9syncModelEv'
    self.uglySide.call(ritual)

  def syncSyncView(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncSyncView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncSyncView
    """
    #  void QQuickTableViewPrivate::syncSyncView()
    ritual = 'ritual_ZN22QQuickTableViewPrivate12syncSyncViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate12syncSyncViewEv'
    self.uglySide.call(ritual)

  def syncPositionView(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncPositionView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncPositionView
    """
    #  void QQuickTableViewPrivate::syncPositionView()
    ritual = 'ritual_ZN22QQuickTableViewPrivate16syncPositionViewEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate16syncPositionViewEv'
    self.uglySide.call(ritual)

  def selectionSourceModel(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel
    *QQuickTableViewPrivate::selectionSourceModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#selectionSourceModel

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QQuickTableViewPrivate::selectionSourceModel()
    ritual = 'ritual_ZN22QQuickTableViewPrivate20selectionSourceModelEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate20selectionSourceModelEv')
    address = self.uglySide.call(ritual)
    return QAbstractItemModel._cuteAt(address)

  def syncRebuildOptions(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncRebuildOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncRebuildOptions
    """
    #  void QQuickTableViewPrivate::syncRebuildOptions()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18syncRebuildOptionsEv',
    )

  def connectToModel(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::connectToModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#connectToModel
    """
    #  void QQuickTableViewPrivate::connectToModel()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate14connectToModelEv')

  def disconnectFromModel(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::disconnectFromModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#disconnectFromModel
    """
    #  void QQuickTableViewPrivate::disconnectFromModel()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate19disconnectFromModelEv',
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def rowsMovedCallback(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
      destination: QModelIndex,
      row: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::rowsMovedCallback(const
    QModelIndex &parent, int start, int end, const QModelIndex &destination,
    int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#rowsMovedCallback

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    destination : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    row : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::rowsMovedCallback(const QModelIndex
    #      &parent, int start, int end, const QModelIndex &destination, int
    #      row)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17rowsMovedCallbackERK11QModelInd'
        'exiiS2_i',
        self._valueOf(parent), start, end, self._valueOf(destination), row,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def columnsMovedCallback(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
      destination: QModelIndex,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::columnsMovedCallback(const
    QModelIndex &parent, int start, int end, const QModelIndex &destination,
    int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#columnsMovedCallback

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    destination : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    column : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::columnsMovedCallback(const QModelIndex
    #      &parent, int start, int end, const QModelIndex &destination, int
    #      column)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20columnsMovedCallbackERK11QModel'
        'IndexiiS2_i',
        self._valueOf(parent), start, end, self._valueOf(destination),
        column,
    )

  @overload(QModelIndex, int, int)
  def rowsInsertedCallback(
      self,
      parent: QModelIndex,
      begin: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::rowsInsertedCallback(const
    QModelIndex &parent, int begin, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#rowsInsertedCallback

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    begin : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::rowsInsertedCallback(const QModelIndex
    #      &parent, int begin, int end)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20rowsInsertedCallbackERK11QModel'
        'Indexii',
        self._valueOf(parent), begin, end,
    )

  @overload(QModelIndex, int, int)
  def rowsRemovedCallback(
      self,
      parent: QModelIndex,
      begin: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::rowsRemovedCallback(const
    QModelIndex &parent, int begin, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#rowsRemovedCallback

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    begin : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::rowsRemovedCallback(const QModelIndex
    #      &parent, int begin, int end)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate19rowsRemovedCallbackERK11QModelI'
        'ndexii',
        self._valueOf(parent), begin, end,
    )

  @overload(QModelIndex, int, int)
  def columnsInsertedCallback(
      self,
      parent: QModelIndex,
      begin: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::columnsInsertedCallback(const
    QModelIndex &parent, int begin, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    begin : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::columnsInsertedCallback(const QModelIndex
    #      &parent, int begin, int end)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate23columnsInsertedCallbackERK11QMo'
        'delIndexii',
        self._valueOf(parent), begin, end,
    )

  @overload(QModelIndex, int, int)
  def columnsRemovedCallback(
      self,
      parent: QModelIndex,
      begin: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::columnsRemovedCallback(const
    QModelIndex &parent, int begin, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#columnsRemovedCallback

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    begin : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QQuickTableViewPrivate::columnsRemovedCallback(const QModelIndex
    #      &parent, int begin, int end)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22columnsRemovedCallbackERK11QMod'
        'elIndexii',
        self._valueOf(parent), begin, end,
    )

  @overload(
      QList[QPersistentModelIndex], QAbstractItemModel.LayoutChangeHint,
  )
  def layoutChangedCallback(
      self,
      parents: QList[QPersistentModelIndex],
      hint: QAbstractItemModel.LayoutChangeHint,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::layoutChangedCallback(const
    QList<QPersistentModelIndex> &parents,
    QAbstractItemModel::LayoutChangeHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#layoutChangedCallback

    Parameters
    ----------

    parents : QList[QPersistentModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    hint : QAbstractItemModel.LayoutChangeHint
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::layoutChangedCallback(const
    #      QList<QPersistentModelIndex> &parents,
    #      QAbstractItemModel::LayoutChangeHint hint)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate21layoutChangedCallbackERK5QListI'
        '21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE',
        self._valueOf(parents), hint.value,
    )

  def modelResetCallback(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::modelResetCallback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#modelResetCallback
    """
    #  void QQuickTableViewPrivate::modelResetCallback()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate18modelResetCallbackEv',
    )

  @overload(int, Qt.Alignment, float)
  @overload(int, Qt.Alignment, float, QRectF)
  def positionViewAtRow(
      self,
      row: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::positionViewAtRow(int row,
    Qt::Alignment alignment, qreal offset, const QRectF subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#positionViewAtRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableViewPrivate::positionViewAtRow(int row, Qt::Alignment
    #      alignment, qreal offset, const QRectF subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17positionViewAtRowEi6QFlagsIN2Qt'
        '13AlignmentFlagEEd6QRectF',
        row, alignment.value, offset, self._valueOf(subRect),
    )

  @overload(int, Qt.Alignment, float)
  @overload(int, Qt.Alignment, float, QRectF)
  def positionViewAtColumn(
      self,
      column: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::positionViewAtColumn(int column,
    Qt::Alignment alignment, qreal offset, const QRectF subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#positionViewAtColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableViewPrivate::positionViewAtColumn(int column,
    #      Qt::Alignment alignment, qreal offset, const QRectF subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20positionViewAtColumnEi6QFlagsIN'
        '2Qt13AlignmentFlagEEd6QRectF',
        column, alignment.value, offset, self._valueOf(subRect),
    )

  @overload(int, Qt.Alignment, float)
  @overload(int, Qt.Alignment, float, QRectF)
  def scrollToRow(
      self,
      row: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: Optional[QRectF] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::scrollToRow(int row,
    Qt::Alignment alignment, qreal offset, const QRectF subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#scrollToRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  bool QQuickTableViewPrivate::scrollToRow(int row, Qt::Alignment
    #      alignment, qreal offset, const QRectF subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate11scrollToRowEi6QFlagsIN2Qt13Alig'
        'nmentFlagEEd6QRectF',
        row, alignment.value, offset, self._valueOf(subRect),
    )

  @overload(int, Qt.Alignment, float)
  @overload(int, Qt.Alignment, float, QRectF)
  def scrollToColumn(
      self,
      column: int,
      alignment: Qt.Alignment,
      offset: float,
      subRect: Optional[QRectF] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::scrollToColumn(int column,
    Qt::Alignment alignment, qreal offset, const QRectF subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#scrollToColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    offset : float
      Passed on as it is.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  bool QQuickTableViewPrivate::scrollToColumn(int column, Qt::Alignment
    #      alignment, qreal offset, const QRectF subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate14scrollToColumnEi6QFlagsIN2Qt13A'
        'lignmentFlagEEd6QRectF',
        column, alignment.value, offset, self._valueOf(subRect),
    )

  def scheduleRebuildIfFastFlick(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::scheduleRebuildIfFastFlick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::scheduleRebuildIfFastFlick()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate26scheduleRebuildIfFastFlickEv',
    )

  def syncViewportRect(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncViewportRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#syncViewportRect
    """
    #  void QQuickTableViewPrivate::syncViewportRect()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate16syncViewportRectEv',
    )

  def syncViewportPosRecursive(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::syncViewportPosRecursive()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::syncViewportPosRecursive()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate24syncViewportPosRecursiveEv',
    )

  @overload(QItemSelection, QItemSelection)
  def selectionChangedInSelectionModel(
      self,
      selected: QItemSelection,
      deselected: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::selectionChangedInSelectionModel(const
    QItemSelection &selected, const QItemSelection &deselected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    selected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    deselected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void QQuickTableViewPrivate::selectionChangedInSelectionModel(const
    #      QItemSelection &selected, const QItemSelection &deselected)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate32selectionChangedInSelectionMode'
        'lERK14QItemSelectionS2_',
        self._valueOf(selected), self._valueOf(deselected),
    )

  def updateSelectedOnAllDelegateItems(self) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::updateSelectedOnAllDelegateItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::updateSelectedOnAllDelegateItems()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate32updateSelectedOnAllDelegateItem'
        'sEv',
    )

  @overload(QModelIndex, QModelIndex)
  def currentChangedInSelectionModel(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::currentChangedInSelectionModel(const QModelIndex
    &current, const QModelIndex &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQuickTableViewPrivate::currentChangedInSelectionModel(const
    #      QModelIndex &current, const QModelIndex &previous)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate30currentChangedInSelectionModelE'
        'RK11QModelIndexS2_',
        self._valueOf(current), self._valueOf(previous),
    )

  def updateCurrentRowAndColumn(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateCurrentRowAndColumn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::updateCurrentRowAndColumn()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate25updateCurrentRowAndColumnEv',
    )

  def fetchMoreData(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::fetchMoreData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#fetchMoreData
    """
    #  void QQuickTableViewPrivate::fetchMoreData()
    self.uglySide.call('ritual_ZN22QQuickTableViewPrivate13fetchMoreDataEv')

  def dumpTable(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::dumpTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#dumpTable
    """
    #  void QQuickTableViewPrivate::dumpTable() const
    self.uglySide.call('ritual_ZNK22QQuickTableViewPrivate9dumpTableEv')

  @overload(QQuickHandlerPoint)
  def handleTap(self, point: QQuickHandlerPoint) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::handleTap(const
    QQuickHandlerPoint &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#handleTap

    Parameters
    ----------

    point : QQuickHandlerPoint
      Passed on as a value: Qt reads the C++ QQuickHandlerPoint, which stays
      Python's own.
    """
    #  void QQuickTableViewPrivate::handleTap(const QQuickHandlerPoint
    #      &point)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate9handleTapERK18QQuickHandlerPoint',
        self._valueOf(point),
    )

  @overload(QModelIndex, bool)
  def canEdit(self, tappedIndex: QModelIndex, warn: bool) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::canEdit(const QModelIndex
    tappedIndex, bool warn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#canEdit

    Parameters
    ----------

    tappedIndex : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    warn : bool
      Passed on as it is.
    """
    #  bool QQuickTableViewPrivate::canEdit(const QModelIndex tappedIndex,
    #      bool warn)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate7canEditE11QModelIndexb',
        self._valueOf(tappedIndex), warn,
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def editFromKeyEvent(self, e: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::editFromKeyEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#editFromKeyEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTableViewPrivate::editFromKeyEvent(QKeyEvent *e)
    return self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate16editFromKeyEventEP9QKeyEvent',
        self._addressOf(e),
    )

  def closeEditorAndCommit(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::closeEditorAndCommit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#closeEditorAndCommit
    """
    #  void QQuickTableViewPrivate::closeEditorAndCommit()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate20closeEditorAndCommitEv',
    )

  def installEventFilterOnFocusObjectInsideEditItem(
      self,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQuickTableViewPrivate::installEventFilterOnFocusObjectInsideEditItem(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickTableViewPrivate::
    #      installEventFilterOnFocusObjectInsideEditItem()
    address = self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate45installEventFilterOnFocusObject'
        'InsideEditItemEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QPointF, Qt.KeyboardModifiers)
  def startSelection(
      self,
      pos: QPointF,
      modifiers: Qt.KeyboardModifiers,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTableViewPrivate::startSelection(const QPointF
    &pos, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#startSelection

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool QQuickTableViewPrivate::startSelection(const QPointF &pos,
    #      Qt::KeyboardModifiers modifiers)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate14startSelectionERK7QPointF6QFlag'
        'sIN2Qt16KeyboardModifierEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate14startSelectionERK7QPointF'
          '6QFlagsIN2Qt16KeyboardModifierEE')
    return self.uglySide.call(
        ritual, self._valueOf(pos, 'QPointF'), modifiers.value,
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#clearSelection
    """
    #  void QQuickTableViewPrivate::clearSelection()
    ritual = 'ritual_ZN22QQuickTableViewPrivate14clearSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate14clearSelectionEv'
    self.uglySide.call(ritual)

  def normalizeSelection(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::normalizeSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#normalizeSelection
    """
    #  void QQuickTableViewPrivate::normalizeSelection()
    ritual = 'ritual_ZN22QQuickTableViewPrivate18normalizeSelectionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickTableViewPrivate18normalizeSelectionEv'
    self.uglySide.call(ritual)

  @overload(QPointF, QSizeF)
  def scrollTowardsPoint(self, pos: QPointF, step: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickTableViewPrivate::scrollTowardsPoint(const
    QPointF &pos, const QSizeF &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#scrollTowardsPoint

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    step : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickTableViewPrivate::scrollTowardsPoint(const QPointF &pos,
    #      const QSizeF &step)
    ritual = (
        'ritual_ZN22QQuickTableViewPrivate18scrollTowardsPointERK7QPointFRK'
        '6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate18scrollTowardsPointERK7QPo'
          'intFRK6QSizeF')
    address = self.uglySide.call(
        ritual, self._valueOf(pos, 'QPointF'), self._valueOf(step),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def cancelSelectionTracking(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::cancelSelectionTracking()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::cancelSelectionTracking()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate23cancelSelectionTrackingEv',
    )

  @overload(QRect, QRect)
  def updateSelection(
      self,
      oldSelection: QRect,
      newSelection: QRect,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::updateSelection(const QRect
    &oldSelection, const QRect &newSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#updateSelection

    Parameters
    ----------

    oldSelection : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    newSelection : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QQuickTableViewPrivate::updateSelection(const QRect
    #      &oldSelection, const QRect &newSelection)
    ritual = 'ritual_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTableViewPrivate15updateSelectionERK5QRectS'
          '2_')
    self.uglySide.call(
        ritual, self._valueOf(oldSelection), self._valueOf(newSelection),
    )

  @overload(Qt.Orientation)
  def initSectionDragHandler(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void
    QQuickTableViewPrivate::initSectionDragHandler(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#initSectionDragHandler

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::initSectionDragHandler(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22initSectionDragHandlerEN2Qt11Or'
        'ientationE',
        orientation.value,
    )

  def destroySectionDragHandler(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::destroySectionDragHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html
    """
    #  void QQuickTableViewPrivate::destroySectionDragHandler()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate25destroySectionDragHandlerEv',
    )

  @overload(int, int, Qt.Orientation)
  def moveSection(
      self,
      source: int,
      destination: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::moveSection(int source, int
    destination, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#moveSection

    Parameters
    ----------

    source : int
      Passed on as it is.

    destination : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::moveSection(int source, int destination,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate11moveSectionEiiN2Qt11Orientation'
        'E',
        source, destination, orientation.value,
    )

  def initializeIndexMapping(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::initializeIndexMapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#initializeIndexMapping
    """
    #  void QQuickTableViewPrivate::initializeIndexMapping()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate22initializeIndexMappingEv',
    )

  def clearIndexMapping(self) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::clearIndexMapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#clearIndexMapping
    """
    #  void QQuickTableViewPrivate::clearIndexMapping()
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate17clearIndexMappingEv',
    )

  @overload(Qt.Orientation)
  def clearSection(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickTableViewPrivate::clearSection(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewprivate.html#clearSection

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickTableViewPrivate::clearSection(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN22QQuickTableViewPrivate12clearSectionEN2Qt11OrientationE',
        orientation.value,
    )

  @staticmethod
  def _q_componentFinalized(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewPrivate::_q_componentFinalized()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate._q_componentFinalized' has no cute "
        "function yet. Qt's 'void "
        "QQuickTableViewPrivate::_q_componentFinalized()': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def calculateTopLeft(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewPrivate::calculateTopLeft(QPoint &topLeft,
    QPointF &topLeftPos)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.calculateTopLeft' has no cute function "
        "yet. Qt's 'void QQuickTableViewPrivate::calculateTopLeft(QPoint "
        "&topLeft, QPointF &topLeftPos)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def compareModel(*__, **_) -> Never:
    """
    Qt's 'bool QQuickTableViewPrivate::compareModel(const QVariant &model1,
    const QVariant &model2) const': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.compareModel' has no cute function yet. "
        "Qt's 'bool QQuickTableViewPrivate::compareModel(const QVariant "
        "&model1, const QVariant &model2) const': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def dataChangedCallback(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewPrivate::dataChangedCallback(const QModelIndex
    &topLeft, const QModelIndex &bottomRight, const QList<int> &roles)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.dataChangedCallback' has no cute function "
        "yet. Qt's 'void QQuickTableViewPrivate::dataChangedCallback(const "
        "QModelIndex &topLeft, const QModelIndex &bottomRight, const "
        "QList<int> &roles)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def logicalIndicesForOrientation(*__, **_) -> Never:
    """
    Qt's 'std::vector<SectionData>
    &QQuickTableViewPrivate::logicalIndicesForOrientation(Qt::Orientation
    orientation)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.logicalIndicesForOrientation' has no cute "
        "function yet. Qt's 'std::vector<SectionData> "
        "&QQuickTableViewPrivate::logicalIndicesForOrientation(Qt::Orientati"
        "on orientation)': gives a type Python has no way to take yet.")

  @staticmethod
  def registerCallbackWhenBindingsAreEvaluated(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTableViewPrivate::registerCallbackWhenBindingsAreEvaluated()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.registerCallbackWhenBindingsAreEvaluated' "
        "has no cute function yet. Qt's 'void "
        "QQuickTableViewPrivate::registerCallbackWhenBindingsAreEvaluated()'"
        ": cannot be called and cannot be called through the meta-object "
        "and cannot be copied: no header file has its code, Qt's source "
        "does not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def releaseItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewPrivate::releaseItem(FxTableItem *fxTableItem,
    QQmlTableInstanceModel::ReusableFlag reusableFlag)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.releaseItem' has no cute function yet. "
        "Qt's 'void QQuickTableViewPrivate::releaseItem(FxTableItem "
        "*fxTableItem, QQmlTableInstanceModel::ReusableFlag reusableFlag)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def releaseLoadedItems(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickTableViewPrivate::releaseLoadedItems(QQmlTableInstanceModel::
    ReusableFlag reusableFlag)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.releaseLoadedItems' has no cute function "
        "yet. Qt's 'void "
        "QQuickTableViewPrivate::releaseLoadedItems(QQmlTableInstanceModel::"
        "ReusableFlag reusableFlag)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateTableSize(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewPrivate::updateTableSize()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.updateTableSize' has no cute function yet. "
        "Qt's 'void QQuickTableViewPrivate::updateTableSize()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def visualIndicesForOrientation(*__, **_) -> Never:
    """
    Qt's 'std::vector<SectionData>
    &QQuickTableViewPrivate::visualIndicesForOrientation(Qt::Orientation
    orientation)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewPrivate.visualIndicesForOrientation' has no cute "
        "function yet. Qt's 'std::vector<SectionData> "
        "&QQuickTableViewPrivate::visualIndicesForOrientation(Qt::Orientatio"
        "n orientation)': gives a type Python has no way to take yet.")
