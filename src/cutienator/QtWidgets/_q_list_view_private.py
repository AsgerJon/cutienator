"""
QListViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QListViewPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import QItemSelectionModel, QList
from . import QAbstractItemViewPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QModelIndex, QPoint, QRect, QSize
  from . import QItemViewPaintPair, QListView, QListViewItem
  from . import QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QListViewItem = WAIT['QListViewItem']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QListViewPrivate(QAbstractItemViewPrivate):
  """
  The cute side of Qt's QListViewPrivate: a plain Python object standing in
  front of one C++ QListViewPrivate.

  It is built on the cute 'QAbstractItemViewPrivate', as Qt's
  QListViewPrivate is built on Qt's QAbstractItemViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QListViewPrivate that has a ritual and that Python
  can call so far, 38 names in all: 'q_func', 'clear', 'prepareItemsLayout',
  'doItemsLayout', 'intersectingSet', 'resetBatchStartRow', 'batchStartRow',
  'contentsSize', 'setContentsSize', 'flipX', 'viewItemRect',
  'indexToListViewItem', 'listViewItemToIndex', 'hasRectForIndex',
  'rectForIndex', 'cellRectForIndex', 'viewUpdateGeometries',
  'mapToViewport', 'closestIndex', 'itemSize', 'selectionAllowed',
  'selection', 'selectAll', 'accessibleChildIndex', 'setGridSize',
  'gridSize', 'setWrapping', 'isWrapping', 'setSpacing', 'spacing',
  'setSelectionRectVisible', 'isSelectionRectVisible', 'modelIndex',
  'isHidden', 'isHiddenOrDisabled', 'scrollElasticBandBy',
  'draggablePaintPairs', 'emitIndexesMoved'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QListView *QListViewPrivate::q_func() const': takes in Python
    what 'QListView *QListViewPrivate::q_func()' takes.
  - Qt's 'QListViewPrivate::~QListViewPrivate()': the destructor: Python
    never removes a C++ QListViewPrivate.
  - Qt's 'int QListViewPrivate::horizontalScrollToValue(const QModelIndex
    &index, const QRect &rect, QListView::ScrollHint hint) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'int QListViewPrivate::verticalScrollToValue(const QModelIndex
    &index, const QRect &rect, QListView::ScrollHint hint) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'QAbstractItemView::DropIndicatorPosition
    QListViewPrivate::position(const QPoint &pos, const QRect &rect, const
    QModelIndex &idx) const': gives the enum
    'QAbstractItemView::DropIndicatorPosition', whose class cannot be named
    here.
  - Qt's 'bool QListViewPrivate::dropOn(QDropEvent *event, int *row, int
    *col, QModelIndex *index)': takes a number to change where it is.
  - Qt's 'QList<int> QListViewPrivate::hiddenRowIds() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QListViewPrivate::removeCurrentAndDisabled(QList<QModelIndex>
    *indexes, const QModelIndex &current) const': names 'QList<QModelIndex>',
    which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 49 functions Qt declares: 1 leans on 'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QListViewPrivate is created at the first use, not by
    'QListViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QListViewPrivate.
  - Each name of Qt's QListViewPrivate that has no cute function yet,
    '__init__', 'hiddenRowIds', 'horizontalScrollToValue',
    'removeCurrentAndDisabled', 'verticalScrollToValue', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QListViewPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ModeProperties(CuteNum):
    """
    The enum 'QListViewPrivate::ModeProperties' of Qt, with the 7 names Qt
    gives in it.
    """

    Wrap = Kee[int](1)
    Spacing = Kee[int](2)
    GridSize = Kee[int](4)
    Flow = Kee[int](8)
    Movement = Kee[int](16)
    ResizeMode = Kee[int](32)
    SelectionRectVisible = Kee[int](64)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListViewPrivate'

  #  A C++ QListViewPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QListViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  @overload(QRect, bool)
  def intersectingSet(
      self,
      area: QRect,
      doLayout: bool = True,
  ) -> QList[QModelIndex]:
    """
    Calls Qt's 'QList<QModelIndex> QListViewPrivate::intersectingSet(const
    QRect &area, bool doLayout) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#intersectingSet

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    doLayout : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QModelIndex> QListViewPrivate::intersectingSet(const QRect
    #      &area, bool doLayout) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate15intersectingSetERK5QRectb',
        self._valueOf(area), doLayout,
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  def batchStartRow(self) -> int:
    """
    Calls Qt's 'int QListViewPrivate::batchStartRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#batchStartRow
    """
    #  int QListViewPrivate::batchStartRow() const
    return self.uglySide.call(
        'ritual_ZNK16QListViewPrivate13batchStartRowEv',
    )

  def contentsSize(self) -> QSize:
    """
    Calls Qt's 'QSize QListViewPrivate::contentsSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#contentsSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListViewPrivate::contentsSize() const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate12contentsSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def flipX(self, x: int) -> int:
    """
    Calls Qt's 'int QListViewPrivate::flipX(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#flipX

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QListViewPrivate::flipX(int x) const
    return self.uglySide.call('ritual_ZNK16QListViewPrivate5flipXEi', x)

  @overload(QPoint)
  def flipX(self, p: QPoint) -> QPoint:
    """
    Calls Qt's 'QPoint QListViewPrivate::flipX(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#flipX

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QListViewPrivate::flipX(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate5flipXERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QRect)
  def flipX(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QListViewPrivate::flipX(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#flipX

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListViewPrivate::flipX(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate5flipXERK5QRect', self._valueOf(r),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QListViewItem)
  def viewItemRect(self, item: QListViewItem) -> QRect:
    """
    Calls Qt's 'QRect QListViewPrivate::viewItemRect(const QListViewItem
    &item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#viewItemRect

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListViewPrivate::viewItemRect(const QListViewItem &item) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate12viewItemRectERK13QListViewItem',
        self._valueOf(item),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex)
  def indexToListViewItem(self, index: QModelIndex) -> QListViewItem:
    """
    Calls Qt's 'QListViewItem QListViewPrivate::indexToListViewItem(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#indexToListViewItem

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QListViewItem
      A new cute QListViewItem around the copy Qt gave back. Python owns it.
    """
    #  QListViewItem QListViewPrivate::indexToListViewItem(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate19indexToListViewItemERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QListViewItem
    return QListViewItem._cuteOwning(address)

  @overload(QListViewItem)
  def listViewItemToIndex(self, item: QListViewItem) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListViewPrivate::listViewItemToIndex(const
    QListViewItem &item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#listViewItemToIndex

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListViewPrivate::listViewItemToIndex(const QListViewItem
    #      &item) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate19listViewItemToIndexERK13QListViewIte'
        'm',
        self._valueOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def hasRectForIndex(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::hasRectForIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#hasRectForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QListViewPrivate::hasRectForIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QListViewPrivate15hasRectForIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def rectForIndex(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QListViewPrivate::rectForIndex(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#rectForIndex

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
    #  QRect QListViewPrivate::rectForIndex(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate12rectForIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect)
  @overload(QRect, bool)
  def mapToViewport(self, rect: QRect, extend: bool = True) -> QRect:
    """
    Calls Qt's 'QRect QListViewPrivate::mapToViewport(const QRect &rect, bool
    extend) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#mapToViewport

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    extend : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListViewPrivate::mapToViewport(const QRect &rect, bool extend)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate13mapToViewportERK5QRectb',
        self._valueOf(rect), extend,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QRect, QList[QModelIndex])
  def closestIndex(
      self,
      target: QRect,
      candidates: QList[QModelIndex],
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListViewPrivate::closestIndex(const QRect
    &target, const QList<QModelIndex> &candidates) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#closestIndex

    Parameters
    ----------

    target : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    candidates : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListViewPrivate::closestIndex(const QRect &target, const
    #      QList<QModelIndex> &candidates) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate12closestIndexERK5QRectRK5QListI11QMod'
        'elIndexE',
        self._valueOf(target), self._valueOf(candidates),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QStyleOptionViewItem, QModelIndex)
  def itemSize(
      self,
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> QSize:
    """
    Calls Qt's 'QSize QListViewPrivate::itemSize(const QStyleOptionViewItem
    &option, const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#itemSize

    Parameters
    ----------

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListViewPrivate::itemSize(const QStyleOptionViewItem &option,
    #      const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate8itemSizeERK20QStyleOptionViewItemRK11'
        'QModelIndex',
        self._valueOf(option), self._valueOf(index),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  def selectionAllowed(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::selectionAllowed(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#selectionAllowed

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QListViewPrivate::selectionAllowed(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK16QListViewPrivate16selectionAllowedERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QListViewPrivate16selectionAllowedERK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(QRect)
  def selection(self, rect: QRect) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection QListViewPrivate::selection(const QRect &rect)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#selection

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection QListViewPrivate::selection(const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate9selectionERK5QRect',
        self._valueOf(rect),
    )
    from ..QtCore import QItemSelection
    return QItemSelection._cuteOwning(address)

  @overload(QModelIndex)
  def accessibleChildIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QListViewPrivate::accessibleChildIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#accessibleChildIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QListViewPrivate::accessibleChildIndex(const QModelIndex &index)
    #      const
    ritual = (
        'ritual_ZNK16QListViewPrivate20accessibleChildIndexERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QListViewPrivate20accessibleChildIndexERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  def gridSize(self) -> QSize:
    """
    Calls Qt's 'QSize QListViewPrivate::gridSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#gridSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QListViewPrivate::gridSize() const
    address = self.uglySide.call('ritual_ZNK16QListViewPrivate8gridSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isWrapping(self) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::isWrapping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#isWrapping
    """
    #  bool QListViewPrivate::isWrapping() const
    return self.uglySide.call('ritual_ZNK16QListViewPrivate10isWrappingEv')

  def spacing(self) -> int:
    """
    Calls Qt's 'int QListViewPrivate::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#spacing
    """
    #  int QListViewPrivate::spacing() const
    return self.uglySide.call('ritual_ZNK16QListViewPrivate7spacingEv')

  def isSelectionRectVisible(self) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::isSelectionRectVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#isSelectionRectVisible
    """
    #  bool QListViewPrivate::isSelectionRectVisible() const
    return self.uglySide.call(
        'ritual_ZNK16QListViewPrivate22isSelectionRectVisibleEv',
    )

  @overload(int)
  def modelIndex(self, row: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListViewPrivate::modelIndex(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#modelIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListViewPrivate::modelIndex(int row) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate10modelIndexEi', row,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def isHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::isHidden(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#isHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QListViewPrivate::isHidden(int row) const
    return self.uglySide.call('ritual_ZNK16QListViewPrivate8isHiddenEi', row)

  @overload(int)
  def isHiddenOrDisabled(self, row: int) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::isHiddenOrDisabled(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#isHiddenOrDisabled

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QListViewPrivate::isHiddenOrDisabled(int row) const
    return self.uglySide.call(
        'ritual_ZNK16QListViewPrivate18isHiddenOrDisabledEi', row,
    )

  @overload(QList[QModelIndex], QRect)
  @overload(QList[QModelIndex], NoneType)
  def draggablePaintPairs(
      self,
      indexes: QList[QModelIndex],
      r: Optional[QRect],
  ) -> QList[QItemViewPaintPair]:
    """
    Calls Qt's 'QItemViewPaintPairs
    QListViewPrivate::draggablePaintPairs(const QModelIndexList &indexes,
    QRect *r) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#draggablePaintPairs

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    r : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QItemViewPaintPair]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QItemViewPaintPairs QListViewPrivate::draggablePaintPairs(const
    #      QModelIndexList &indexes, QRect *r) const
    address = self.uglySide.call(
        'ritual_ZNK16QListViewPrivate19draggablePaintPairsERK5QListI11QMode'
        'lIndexEP5QRect',
        self._valueOf(indexes), self._addressOf(r),
    )
    from . import QItemViewPaintPair
    return QList[QItemViewPaintPair]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setContentsSize(self, w: int, h: int) -> None:
    """
    Calls Qt's 'void QListViewPrivate::setContentsSize(int w, int h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#setContentsSize

    Parameters
    ----------

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.
    """
    #  void QListViewPrivate::setContentsSize(int w, int h)
    self.uglySide.call(
        'ritual_ZN16QListViewPrivate15setContentsSizeEii', w, h,
    )

  @overload(QSize)
  def setGridSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QListViewPrivate::setGridSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#setGridSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListViewPrivate::setGridSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN16QListViewPrivate11setGridSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def setWrapping(self, b: bool) -> None:
    """
    Calls Qt's 'void QListViewPrivate::setWrapping(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#setWrapping

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QListViewPrivate::setWrapping(bool b)
    self.uglySide.call('ritual_ZN16QListViewPrivate11setWrappingEb', b)

  @overload(int)
  def setSpacing(self, s: int) -> None:
    """
    Calls Qt's 'void QListViewPrivate::setSpacing(int s)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#setSpacing

    Parameters
    ----------

    s : int
      Passed on as it is.
    """
    #  void QListViewPrivate::setSpacing(int s)
    self.uglySide.call('ritual_ZN16QListViewPrivate10setSpacingEi', s)

  @overload(bool)
  def setSelectionRectVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QListViewPrivate::setSelectionRectVisible(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#setSelectionRectVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QListViewPrivate::setSelectionRectVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN16QListViewPrivate23setSelectionRectVisibleEb', visible,
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
    Qt's 'QListViewPrivate::QListViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QListViewPrivate.__init__' has no cute function yet. Qt's "
        "'QListViewPrivate::QListViewPrivate()': leans on "
        "'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex "
        "const&, int, int)', which Qt's source does not mark for use from "
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

  def q_func(self) -> Optional[QListView]:
    """
    Calls Qt's 'QListView *QListViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#q_func

    Returns
    -------

    Optional[QListView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListView *QListViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN16QListViewPrivate6q_funcEv')
    from . import QListView
    return QListView._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QListViewPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#clear
    """
    #  void QListViewPrivate::clear()
    self.uglySide.call('ritual_ZN16QListViewPrivate5clearEv')

  def prepareItemsLayout(self) -> None:
    """
    Calls Qt's 'void QListViewPrivate::prepareItemsLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#prepareItemsLayout
    """
    #  void QListViewPrivate::prepareItemsLayout()
    self.uglySide.call('ritual_ZN16QListViewPrivate18prepareItemsLayoutEv')

  @overload(int)
  def doItemsLayout(self, num: int) -> bool:
    """
    Calls Qt's 'bool QListViewPrivate::doItemsLayout(int num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#doItemsLayout

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  bool QListViewPrivate::doItemsLayout(int num)
    return self.uglySide.call(
        'ritual_ZN16QListViewPrivate13doItemsLayoutEi', num,
    )

  def resetBatchStartRow(self) -> None:
    """
    Calls Qt's 'void QListViewPrivate::resetBatchStartRow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#resetBatchStartRow
    """
    #  void QListViewPrivate::resetBatchStartRow()
    self.uglySide.call('ritual_ZN16QListViewPrivate18resetBatchStartRowEv')

  @overload(QModelIndex)
  def cellRectForIndex(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QListViewPrivate::cellRectForIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#cellRectForIndex

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
    #  QRect QListViewPrivate::cellRectForIndex(const QModelIndex &index)
    address = self.uglySide.call(
        'ritual_ZN16QListViewPrivate16cellRectForIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def viewUpdateGeometries(self) -> None:
    """
    Calls Qt's 'void QListViewPrivate::viewUpdateGeometries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#viewUpdateGeometries
    """
    #  void QListViewPrivate::viewUpdateGeometries()
    self.uglySide.call('ritual_ZN16QListViewPrivate20viewUpdateGeometriesEv')

  @overload(QItemSelectionModel.SelectionFlags)
  def selectAll(self, command: QItemSelectionModel.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
    command)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewprivate.html#selectAll

    Parameters
    ----------

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
    #      command)
    ritual = (
        'ritual_ZN16QListViewPrivate9selectAllE6QFlagsIN19QItemSelectionMod'
        'el13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QListViewPrivate9selectAllE6QFlagsIN19QItemSelect'
          'ionModel13SelectionFlagEE')
    self.uglySide.call(ritual, command.value)

  @overload(int, int)
  def scrollElasticBandBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QListViewPrivate::scrollElasticBandBy(int dx, int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#scrollElasticBandBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QListViewPrivate::scrollElasticBandBy(int dx, int dy)
    self.uglySide.call(
        'ritual_ZN16QListViewPrivate19scrollElasticBandByEii', dx, dy,
    )

  @overload(QList[QModelIndex])
  def emitIndexesMoved(self, indexes: QList[QModelIndex]) -> None:
    """
    Calls Qt's 'void QListViewPrivate::emitIndexesMoved(const QModelIndexList
    &indexes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistviewprivate.html#emitIndexesMoved

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QListViewPrivate::emitIndexesMoved(const QModelIndexList
    #      &indexes)
    self.uglySide.call(
        'ritual_ZN16QListViewPrivate16emitIndexesMovedERK5QListI11QModelInd'
        'exE',
        self._valueOf(indexes),
    )

  @staticmethod
  def hiddenRowIds(*__, **_) -> Never:
    """
    Qt's 'QList<int> QListViewPrivate::hiddenRowIds() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QListViewPrivate.hiddenRowIds' has no cute function yet. Qt's "
        "'QList<int> QListViewPrivate::hiddenRowIds() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def horizontalScrollToValue(*__, **_) -> Never:
    """
    Qt's 'int QListViewPrivate::horizontalScrollToValue(const QModelIndex
    &index, const QRect &rect, QListView::ScrollHint hint) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QListViewPrivate.horizontalScrollToValue' has no cute function "
        "yet. Qt's 'int QListViewPrivate::horizontalScrollToValue(const "
        "QModelIndex &index, const QRect &rect, QListView::ScrollHint hint) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def removeCurrentAndDisabled(*__, **_) -> Never:
    """
    Qt's 'void QListViewPrivate::removeCurrentAndDisabled(QList<QModelIndex>
    *indexes, const QModelIndex &current) const': names 'QList<QModelIndex>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QListViewPrivate.removeCurrentAndDisabled' has no cute function "
        "yet. Qt's 'void "
        "QListViewPrivate::removeCurrentAndDisabled(QList<QModelIndex> "
        "*indexes, const QModelIndex &current) const': names "
        "'QList<QModelIndex>', which has no cute class yet.")

  @staticmethod
  def verticalScrollToValue(*__, **_) -> Never:
    """
    Qt's 'int QListViewPrivate::verticalScrollToValue(const QModelIndex
    &index, const QRect &rect, QListView::ScrollHint hint) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QListViewPrivate.verticalScrollToValue' has no cute function yet. "
        "Qt's 'int QListViewPrivate::verticalScrollToValue(const "
        "QModelIndex &index, const QRect &rect, QListView::ScrollHint hint) "
        "const': takes a type Python has no way to hand over yet.")
