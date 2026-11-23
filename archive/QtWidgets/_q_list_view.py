"""
QListView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlistview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QItemSelectionModel, QList
from . import QAbstractItemView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QItemSelection, QMetaObject, QModelIndex
  from ..QtCore import QPoint, QRect, QSize, QTimerEvent
  from ..QtGui import QDragLeaveEvent, QDragMoveEvent, QDropEvent
  from ..QtGui import QMouseEvent, QPaintEvent, QRegion, QResizeEvent
  from ..QtGui import QWheelEvent
  from . import QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QResizeEvent = WAIT['QResizeEvent']
  QSize = WAIT['QSize']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QListView(QAbstractItemView):
  """
  The cute side of Qt's QListView: a plain Python object standing in front of
  one C++ QListView.

  It is built on the cute 'QAbstractItemView', as Qt's QListView is built on
  Qt's QAbstractItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QListView that has a ritual and that Python can call
  so far, 69 names in all: 'metaObject', 'tr', 'setMovement', 'movement',
  'setFlow', 'flow', 'setWrapping', 'isWrapping', 'setResizeMode',
  'resizeMode', 'setLayoutMode', 'layoutMode', 'setSpacing', 'spacing',
  'setBatchSize', 'batchSize', 'setGridSize', 'gridSize', 'setViewMode',
  'viewMode', 'clearPropertyFlags', 'isRowHidden', 'setRowHidden',
  'setModelColumn', 'modelColumn', 'setUniformItemSizes', 'uniformItemSizes',
  'setWordWrap', 'wordWrap', 'setSelectionRectVisible',
  'isSelectionRectVisible', 'setItemAlignment', 'itemAlignment',
  'visualRect', 'scrollTo', 'indexAt', 'doItemsLayout', 'reset',
  'setRootIndex', 'event', 'scrollContentsBy', 'resizeContents',
  'contentsSize', 'rowsInserted', 'rowsAboutToBeRemoved', 'mouseMoveEvent',
  'mouseReleaseEvent', 'wheelEvent', 'timerEvent', 'resizeEvent',
  'dragMoveEvent', 'dragLeaveEvent', 'dropEvent', 'startDrag',
  'initViewItemOption', 'paintEvent', 'horizontalOffset', 'verticalOffset',
  'rectForIndex', 'setPositionForIndex', 'setSelection',
  'visualRegionForSelection', 'selectedIndexes', 'updateGeometries',
  'isIndexHidden', 'selectionChanged', 'currentChanged', 'viewportSizeHint',
  'visualIndex'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QListView::~QListView()': the destructor: Python never removes a
    C++ QListView.
  - Qt's 'QModelIndex QListView::moveCursor(CursorAction cursorAction,
    Qt::KeyboardModifiers modifiers)': names the enum
    'QAbstractItemView::CursorAction', whose class cannot be named here.

  What has no ritual
  ------------------

  11 of the 83 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QListView is created at the first use, not by 'QListView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QListView.
  - Qt tells when it has removed the C++ QListView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QListView, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flow(CuteNum):
    """The enum 'QListView::Flow' of Qt, with the 2 names Qt gives in it."""

    LeftToRight = Kee[int](0)
    TopToBottom = Kee[int](1)

  class LayoutMode(CuteNum):
    """
    The enum 'QListView::LayoutMode' of Qt, with the 2 names Qt gives in it.
    """

    SinglePass = Kee[int](0)
    Batched = Kee[int](1)

  class Movement(CuteNum):
    """
    The enum 'QListView::Movement' of Qt, with the 3 names Qt gives in it.
    """

    Static = Kee[int](0)
    Free = Kee[int](1)
    Snap = Kee[int](2)

  class ResizeMode(CuteNum):
    """
    The enum 'QListView::ResizeMode' of Qt, with the 2 names Qt gives in it.
    """

    Fixed = Kee[int](0)
    Adjust = Kee[int](1)

  class ViewMode(CuteNum):
    """
    The enum 'QListView::ViewMode' of Qt, with the 2 names Qt gives in it.
    """

    ListMode = Kee[int](0)
    IconMode = Kee[int](1)

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
    Calls Qt's 'QString QListView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#tr

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
    #  QString QListView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QListView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListView'

  #  A C++ QListView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QListView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QListView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QListView::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QListView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def movement(self) -> Movement:
    """
    Calls Qt's 'Movement QListView::movement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#movement

    Returns
    -------

    Movement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Movement(number)' gives.
    """
    #  Movement QListView::movement() const
    return QListView.Movement(self.uglySide.call(
        'ritual_ZNK9QListView8movementEv',
    ))

  def flow(self) -> Flow:
    """
    Calls Qt's 'Flow QListView::flow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#flow

    Returns
    -------

    Flow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Flow(number)' gives.
    """
    #  Flow QListView::flow() const
    return QListView.Flow(self.uglySide.call('ritual_ZNK9QListView4flowEv'))

  def isWrapping(self) -> bool:
    """
    Calls Qt's 'bool QListView::isWrapping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#isWrapping
    """
    #  bool QListView::isWrapping() const
    return self.uglySide.call('ritual_ZNK9QListView10isWrappingEv')

  def resizeMode(self) -> ResizeMode:
    """
    Calls Qt's 'ResizeMode QListView::resizeMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#resizeMode

    Returns
    -------

    ResizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ResizeMode(number)'
      gives.
    """
    #  ResizeMode QListView::resizeMode() const
    return QListView.ResizeMode(self.uglySide.call(
        'ritual_ZNK9QListView10resizeModeEv',
    ))

  def layoutMode(self) -> LayoutMode:
    """
    Calls Qt's 'LayoutMode QListView::layoutMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#layoutMode

    Returns
    -------

    LayoutMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LayoutMode(number)'
      gives.
    """
    #  LayoutMode QListView::layoutMode() const
    return QListView.LayoutMode(self.uglySide.call(
        'ritual_ZNK9QListView10layoutModeEv',
    ))

  def spacing(self) -> int:
    """
    Calls Qt's 'int QListView::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#spacing
    """
    #  int QListView::spacing() const
    return self.uglySide.call('ritual_ZNK9QListView7spacingEv')

  def batchSize(self) -> int:
    """
    Calls Qt's 'int QListView::batchSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#batchSize
    """
    #  int QListView::batchSize() const
    return self.uglySide.call('ritual_ZNK9QListView9batchSizeEv')

  def gridSize(self) -> QSize:
    """
    Calls Qt's 'QSize QListView::gridSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#gridSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListView::gridSize() const
    address = self.uglySide.call('ritual_ZNK9QListView8gridSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def viewMode(self) -> ViewMode:
    """
    Calls Qt's 'ViewMode QListView::viewMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#viewMode

    Returns
    -------

    ViewMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ViewMode(number)' gives.
    """
    #  ViewMode QListView::viewMode() const
    return QListView.ViewMode(self.uglySide.call(
        'ritual_ZNK9QListView8viewModeEv',
    ))

  @overload(int)
  def isRowHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QListView::isRowHidden(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#isRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QListView::isRowHidden(int row) const
    return self.uglySide.call('ritual_ZNK9QListView11isRowHiddenEi', row)

  def modelColumn(self) -> int:
    """
    Calls Qt's 'int QListView::modelColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#modelColumn
    """
    #  int QListView::modelColumn() const
    return self.uglySide.call('ritual_ZNK9QListView11modelColumnEv')

  def uniformItemSizes(self) -> bool:
    """
    Calls Qt's 'bool QListView::uniformItemSizes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#uniformItemSizes
    """
    #  bool QListView::uniformItemSizes() const
    return self.uglySide.call('ritual_ZNK9QListView16uniformItemSizesEv')

  def wordWrap(self) -> bool:
    """
    Calls Qt's 'bool QListView::wordWrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#wordWrap
    """
    #  bool QListView::wordWrap() const
    return self.uglySide.call('ritual_ZNK9QListView8wordWrapEv')

  def isSelectionRectVisible(self) -> bool:
    """
    Calls Qt's 'bool QListView::isSelectionRectVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistview.html#isSelectionRectVisible
    """
    #  bool QListView::isSelectionRectVisible() const
    return self.uglySide.call(
        'ritual_ZNK9QListView22isSelectionRectVisibleEv',
    )

  def itemAlignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QListView::itemAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#itemAlignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QListView::itemAlignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK9QListView13itemAlignmentEv',
    ))

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QListView::visualRect(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#visualRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListView::visualRect(const QModelIndex &index) const
    ritual = 'ritual_ZNK9QListView10visualRectERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView10visualRectERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def indexAt(self, p: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListView::indexAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#indexAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListView::indexAt(const QPoint &p) const
    ritual = 'ritual_ZNK9QListView7indexAtERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView7indexAtERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(p))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def contentsSize(self) -> QSize:
    """
    Calls Qt's 'QSize QListView::contentsSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#contentsSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListView::contentsSize() const
    address = self.uglySide.call('ritual_ZNK9QListView12contentsSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QListView::horizontalOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#horizontalOffset
    """
    #  int QListView::horizontalOffset() const
    ritual = 'ritual_ZNK9QListView16horizontalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView16horizontalOffsetEv'
    return self.uglySide.call(ritual)

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QListView::verticalOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#verticalOffset
    """
    #  int QListView::verticalOffset() const
    ritual = 'ritual_ZNK9QListView14verticalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView14verticalOffsetEv'
    return self.uglySide.call(ritual)

  @overload(QModelIndex)
  def rectForIndex(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QListView::rectForIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#rectForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListView::rectForIndex(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK9QListView12rectForIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QItemSelection)
  def visualRegionForSelection(self, selection: QItemSelection) -> QRegion:
    """
    Calls Qt's 'QRegion QListView::visualRegionForSelection(const
    QItemSelection &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistview.html#visualRegionForSelection

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QListView::visualRegionForSelection(const QItemSelection
    #      &selection) const
    ritual = (
        'ritual_ZNK9QListView24visualRegionForSelectionERK14QItemSelection')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QListView24visualRegionForSelectionERK14QItemSele'
          'ction')
    address = self.uglySide.call(ritual, self._valueOf(selection))
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def selectedIndexes(self) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList QListView::selectedIndexes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#selectedIndexes

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QListView::selectedIndexes() const
    address = self.uglySide.call('ritual_ZNK9QListView15selectedIndexesEv')
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QModelIndex)
  def isIndexHidden(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QListView::isIndexHidden(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#isIndexHidden

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QListView::isIndexHidden(const QModelIndex &index) const
    ritual = 'ritual_ZNK9QListView13isIndexHiddenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView13isIndexHiddenERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  def viewportSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QListView::viewportSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#viewportSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListView::viewportSizeHint() const
    ritual = 'ritual_ZNK9QListView16viewportSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QListView16viewportSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  def visualIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QListView::visualIndex(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#visualIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QListView::visualIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK9QListView11visualIndexERK11QModelIndex',
        self._valueOf(index),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Movement)
  def setMovement(self, movement: Movement) -> None:
    """
    Calls Qt's 'void QListView::setMovement(Movement movement)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setMovement

    Parameters
    ----------

    movement : Movement
      Passed on as its number.
    """
    #  void QListView::setMovement(Movement movement)
    self.uglySide.call(
        'ritual_ZN9QListView11setMovementENS_8MovementE', movement.value,
    )

  @overload(Flow)
  def setFlow(self, flow: Flow) -> None:
    """
    Calls Qt's 'void QListView::setFlow(Flow flow)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setFlow

    Parameters
    ----------

    flow : Flow
      Passed on as its number.
    """
    #  void QListView::setFlow(Flow flow)
    self.uglySide.call('ritual_ZN9QListView7setFlowENS_4FlowE', flow.value)

  @overload(bool)
  def setWrapping(self, enable: bool) -> None:
    """
    Calls Qt's 'void QListView::setWrapping(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setWrapping

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QListView::setWrapping(bool enable)
    self.uglySide.call('ritual_ZN9QListView11setWrappingEb', enable)

  @overload(ResizeMode)
  def setResizeMode(self, mode: ResizeMode) -> None:
    """
    Calls Qt's 'void QListView::setResizeMode(ResizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setResizeMode

    Parameters
    ----------

    mode : ResizeMode
      Passed on as its number.
    """
    #  void QListView::setResizeMode(ResizeMode mode)
    self.uglySide.call(
        'ritual_ZN9QListView13setResizeModeENS_10ResizeModeE', mode.value,
    )

  @overload(LayoutMode)
  def setLayoutMode(self, mode: LayoutMode) -> None:
    """
    Calls Qt's 'void QListView::setLayoutMode(LayoutMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setLayoutMode

    Parameters
    ----------

    mode : LayoutMode
      Passed on as its number.
    """
    #  void QListView::setLayoutMode(LayoutMode mode)
    self.uglySide.call(
        'ritual_ZN9QListView13setLayoutModeENS_10LayoutModeE', mode.value,
    )

  @overload(int)
  def setSpacing(self, space: int) -> None:
    """
    Calls Qt's 'void QListView::setSpacing(int space)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setSpacing

    Parameters
    ----------

    space : int
      Passed on as it is.
    """
    #  void QListView::setSpacing(int space)
    self.uglySide.call('ritual_ZN9QListView10setSpacingEi', space)

  @overload(int)
  def setBatchSize(self, batchSize: int) -> None:
    """
    Calls Qt's 'void QListView::setBatchSize(int batchSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setBatchSize

    Parameters
    ----------

    batchSize : int
      Passed on as it is.
    """
    #  void QListView::setBatchSize(int batchSize)
    self.uglySide.call('ritual_ZN9QListView12setBatchSizeEi', batchSize)

  @overload(QSize)
  def setGridSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QListView::setGridSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setGridSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListView::setGridSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN9QListView11setGridSizeERK5QSize', self._valueOf(size),
    )

  @overload(ViewMode)
  def setViewMode(self, mode: ViewMode) -> None:
    """
    Calls Qt's 'void QListView::setViewMode(ViewMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setViewMode

    Parameters
    ----------

    mode : ViewMode
      Passed on as its number.
    """
    #  void QListView::setViewMode(ViewMode mode)
    self.uglySide.call(
        'ritual_ZN9QListView11setViewModeENS_8ViewModeE', mode.value,
    )

  @overload(int, bool)
  def setRowHidden(self, row: int, hide: bool) -> None:
    """
    Calls Qt's 'void QListView::setRowHidden(int row, bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.

    hide : bool
      Passed on as it is.
    """
    #  void QListView::setRowHidden(int row, bool hide)
    self.uglySide.call('ritual_ZN9QListView12setRowHiddenEib', row, hide)

  @overload(int)
  def setModelColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QListView::setModelColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setModelColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QListView::setModelColumn(int column)
    self.uglySide.call('ritual_ZN9QListView14setModelColumnEi', column)

  @overload(bool)
  def setUniformItemSizes(self, enable: bool) -> None:
    """
    Calls Qt's 'void QListView::setUniformItemSizes(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setUniformItemSizes

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QListView::setUniformItemSizes(bool enable)
    self.uglySide.call('ritual_ZN9QListView19setUniformItemSizesEb', enable)

  @overload(bool)
  def setWordWrap(self, on: bool) -> None:
    """
    Calls Qt's 'void QListView::setWordWrap(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setWordWrap

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QListView::setWordWrap(bool on)
    self.uglySide.call('ritual_ZN9QListView11setWordWrapEb', on)

  @overload(bool)
  def setSelectionRectVisible(self, show: bool) -> None:
    """
    Calls Qt's 'void QListView::setSelectionRectVisible(bool show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistview.html#setSelectionRectVisible

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QListView::setSelectionRectVisible(bool show)
    self.uglySide.call(
        'ritual_ZN9QListView23setSelectionRectVisibleEb', show,
    )

  @overload(Qt.Alignment)
  def setItemAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QListView::setItemAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setItemAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QListView::setItemAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN9QListView16setItemAlignmentE6QFlagsIN2Qt13AlignmentFlagE'
        'E',
        alignment.value,
    )

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QListView::setRootIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QListView::setRootIndex(const QModelIndex &index)
    ritual = 'ritual_ZN9QListView12setRootIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView12setRootIndexERK11QModelIndex'
    self.uglySide.call(ritual, self._valueOf(index))

  @overload(QPoint, QModelIndex)
  def setPositionForIndex(
      self,
      position: QPoint,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QListView::setPositionForIndex(const QPoint &position,
    const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setPositionForIndex

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QListView::setPositionForIndex(const QPoint &position, const
    #      QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN9QListView19setPositionForIndexERK6QPointRK11QModelIndex',
        self._valueOf(position), self._valueOf(index),
    )

  @overload(QRect, QItemSelectionModel.SelectionFlags)
  def setSelection(
      self,
      rect: QRect,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QListView::setSelection(const QRect &rect,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#setSelection

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QListView::setSelection(const QRect &rect,
    #      QItemSelectionModel::SelectionFlags command)
    ritual = (
        'ritual_ZN9QListView12setSelectionERK5QRect6QFlagsIN19QItemSelectio'
        'nModel13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QListView12setSelectionERK5QRect6QFlagsIN19QItemSe'
          'lectionModel13SelectionFlagEE')
    self.uglySide.call(ritual, self._valueOf(rect), command.value)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QListView::QListView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#QListView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QListView::QListView(QWidget *parent)
    self._noteCreation(QListView, lambda: Rituals.call(
        'ritual_ZN9QListViewC1EP7QWidget', self._addressOf(parent),
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

  def clearPropertyFlags(self) -> None:
    """
    Calls Qt's 'void QListView::clearPropertyFlags()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#clearPropertyFlags
    """
    #  void QListView::clearPropertyFlags()
    self.uglySide.call('ritual_ZN9QListView18clearPropertyFlagsEv')

  @overload(QModelIndex)
  @overload(QModelIndex, QAbstractItemView.ScrollHint)
  def scrollTo(
      self,
      index: QModelIndex,
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QListView::scrollTo(const QModelIndex &index, ScrollHint
    hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#scrollTo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
    ritual = (
        'ritual_ZN9QListView8scrollToERK11QModelIndexN17QAbstractItemView10'
        'ScrollHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QListView8scrollToERK11QModelIndexN17QAbstractItem'
          'View10ScrollHintE')
    self.uglySide.call(ritual, self._valueOf(index), hint.value)

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QListView::doItemsLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#doItemsLayout
    """
    #  void QListView::doItemsLayout()
    ritual = 'ritual_ZN9QListView13doItemsLayoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView13doItemsLayoutEv'
    self.uglySide.call(ritual)

  def reset(self) -> None:
    """
    Calls Qt's 'void QListView::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#reset
    """
    #  void QListView::reset()
    ritual = 'ritual_ZN9QListView5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView5resetEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QListView::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QListView::event(QEvent *e)
    ritual = 'ritual_ZN9QListView5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QListView::scrollContentsBy(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QListView::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN9QListView16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

  @overload(int, int)
  def resizeContents(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void QListView::resizeContents(int width, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#resizeContents

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QListView::resizeContents(int width, int height)
    self.uglySide.call(
        'ritual_ZN9QListView14resizeContentsEii', width, height,
    )

  @overload(QModelIndex, int, int)
  def rowsInserted(self, parent: QModelIndex, start: int, end: int) -> None:
    """
    Calls Qt's 'void QListView::rowsInserted(const QModelIndex &parent, int
    start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#rowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QListView::rowsInserted(const QModelIndex &parent, int start, int
    #      end)
    ritual = 'ritual_ZN9QListView12rowsInsertedERK11QModelIndexii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView12rowsInsertedERK11QModelIndexii'
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def rowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QListView::rowsAboutToBeRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistview.html#rowsAboutToBeRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
    #      start, int end)
    ritual = 'ritual_ZN9QListView20rowsAboutToBeRemovedERK11QModelIndexii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QListView20rowsAboutToBeRemovedERK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QListView::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::mouseMoveEvent(QMouseEvent *e)
    ritual = 'ritual_ZN9QListView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QListView::mouseReleaseEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::mouseReleaseEvent(QMouseEvent *e)
    ritual = 'ritual_ZN9QListView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, e: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QListView::wheelEvent(QWheelEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#wheelEvent

    Parameters
    ----------

    e : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::wheelEvent(QWheelEvent *e)
    ritual = 'ritual_ZN9QListView10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QListView::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN9QListView10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QListView::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN9QListView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, e: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QListView::dragMoveEvent(QDragMoveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#dragMoveEvent

    Parameters
    ----------

    e : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::dragMoveEvent(QDragMoveEvent *e)
    ritual = 'ritual_ZN9QListView13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView13dragMoveEventEP14QDragMoveEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, e: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QListView::dragLeaveEvent(QDragLeaveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#dragLeaveEvent

    Parameters
    ----------

    e : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
    ritual = 'ritual_ZN9QListView14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView14dragLeaveEventEP15QDragLeaveEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QListView::dropEvent(QDropEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#dropEvent

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::dropEvent(QDropEvent *e)
    ritual = 'ritual_ZN9QListView9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(Qt.DropActions)
  def startDrag(self, supportedActions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QListView::startDrag(Qt::DropActions supportedActions)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#startDrag

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number.
    """
    #  void QListView::startDrag(Qt::DropActions supportedActions)
    ritual = 'ritual_ZN9QListView9startDragE6QFlagsIN2Qt10DropActionEE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView9startDragE6QFlagsIN2Qt10DropActionEE'
    self.uglySide.call(ritual, supportedActions.value)

  @overload(QStyleOptionViewItem)
  @overload(NoneType)
  def initViewItemOption(
      self,
      option: Optional[QStyleOptionViewItem],
  ) -> None:
    """
    Calls Qt's 'void QListView::initViewItemOption(QStyleOptionViewItem
    *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#initViewItemOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::initViewItemOption(QStyleOptionViewItem *option) const
    ritual = (
        'ritual_ZNK9QListView18initViewItemOptionEP20QStyleOptionViewItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK9QListView18initViewItemOptionEP20QStyleOptionView'
          'Item')
    self.uglySide.call(ritual, self._addressOf(option))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QListView::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListView::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN9QListView10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  def updateGeometries(self) -> None:
    """
    Calls Qt's 'void QListView::updateGeometries()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#updateGeometries
    """
    #  void QListView::updateGeometries()
    ritual = 'ritual_ZN9QListView16updateGeometriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView16updateGeometriesEv'
    self.uglySide.call(ritual)

  @overload(QItemSelection, QItemSelection)
  def selectionChanged(
      self,
      selected: QItemSelection,
      deselected: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void QListView::selectionChanged(const QItemSelection
    &selected, const QItemSelection &deselected)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#selectionChanged

    Parameters
    ----------

    selected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    deselected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void QListView::selectionChanged(const QItemSelection &selected, const
    #      QItemSelection &deselected)
    ritual = 'ritual_ZN9QListView16selectionChangedERK14QItemSelectionS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QListView16selectionChangedERK14QItemSelectionS2_')
    self.uglySide.call(
        ritual, self._valueOf(selected), self._valueOf(deselected),
    )

  @overload(QModelIndex, QModelIndex)
  def currentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QListView::currentChanged(const QModelIndex &current,
    const QModelIndex &previous)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistview.html#currentChanged

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QListView::currentChanged(const QModelIndex &current, const
    #      QModelIndex &previous)
    ritual = 'ritual_ZN9QListView14currentChangedERK11QModelIndexS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QListView14currentChangedERK11QModelIndexS2_'
    self.uglySide.call(
        ritual, self._valueOf(current), self._valueOf(previous),
    )
