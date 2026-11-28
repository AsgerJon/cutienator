"""
QTableViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTableViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import Qt
from . import QAbstractItemViewPrivate, QSpanCollection, QStyleOptionViewItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QBitArray, QItemSelectionRange, QModelIndex, QRect
  from ..QtGui import QPainter, QRegion
  from . import QHeaderView, QTableView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBitArray = WAIT['QBitArray']
  QHeaderView = WAIT['QHeaderView']
  QItemSelectionRange = WAIT['QItemSelectionRange']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTableViewPrivate(QAbstractItemViewPrivate):
  """
  The cute side of Qt's QTableViewPrivate: a plain Python object standing in
  front of one C++ QTableViewPrivate.

  It is built on the cute 'QAbstractItemViewPrivate', as Qt's
  QTableViewPrivate is built on Qt's QAbstractItemViewPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QTableViewPrivate that has a ritual and that Python
  can call so far, 39 names in all: 'q_func', 'clearConnections',
  'trimHiddenSelections', 'intersectedRect', 'isHidden', 'visualRow',
  'visualColumn', 'logicalRow', 'logicalColumn', 'viewItemPosition',
  'accessibleChildIndex', 'sectionSpanEndLogical', 'sectionSpanSize',
  'spanContainsSection', 'drawAndClipSpans', 'drawCell', 'widthHintForIndex',
  'setSpan', 'span', 'rowSpan', 'columnSpan', 'hasSpans', 'rowSpanHeight',
  'columnSpanWidth', 'rowSpanEndLogical', 'columnSpanEndLogical',
  'isRowHidden', 'isColumnHidden', 'isCellEnabled', 'nextActiveVisualRow',
  'nextActiveVisualColumn', 'visualSpanRect', 'selectRow', 'selectColumn',
  'updateSpanInsertedRows', 'updateSpanInsertedColumns',
  'updateSpanRemovedRows', 'updateSpanRemovedColumns',
  'sortIndicatorChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTableView *QTableViewPrivate::q_func() const': takes in
    Python what 'QTableView *QTableViewPrivate::q_func()' takes.
  - Qt's 'int QTableViewPrivate::heightHintForIndex(const QModelIndex &index,
    int hint, QStyleOptionViewItem &option) const': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QAbstractItemViewPrivate.

  What to expect
  --------------

  - The C++ QTableViewPrivate is created at the first use, not by
    'QTableViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTableViewPrivate.
  - Each name of Qt's QTableViewPrivate that has no cute function yet,
    '__init__', 'heightHintForIndex', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTableViewPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SearchDirection(CuteNum, scoped=True):
    """
    The enum 'QTableViewPrivate::SearchDirection' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Increasing = Kee[int](0)
    Decreasing = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableViewPrivate'

  #  A C++ QTableViewPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTableViewPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect, QModelIndex, QModelIndex)
  def intersectedRect(
      self,
      rect: QRect,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> QRect:
    """
    Calls Qt's 'QRect QTableViewPrivate::intersectedRect(const QRect rect,
    const QModelIndex &topLeft, const QModelIndex &bottomRight) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#intersectedRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTableViewPrivate::intersectedRect(const QRect rect, const
    #      QModelIndex &topLeft, const QModelIndex &bottomRight) const
    ritual = (
        'ritual_ZNK17QTableViewPrivate15intersectedRectE5QRectRK11QModelInd'
        'exS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QTableViewPrivate15intersectedRectE5QRectRK11QMo'
          'delIndexS3_')
    address = self.uglySide.call(
        ritual,
        self._valueOf(rect), self._valueOf(topLeft),
        self._valueOf(bottomRight),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int, int)
  def isHidden(self, row: int, col: int) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::isHidden(int row, int col) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#isHidden

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.
    """
    #  bool QTableViewPrivate::isHidden(int row, int col) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate8isHiddenEii', row, col,
    )

  @overload(int)
  def visualRow(self, logicalRow: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::visualRow(int logicalRow) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#visualRow

    Parameters
    ----------

    logicalRow : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::visualRow(int logicalRow) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate9visualRowEi', logicalRow,
    )

  @overload(int)
  def visualColumn(self, logicalCol: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::visualColumn(int logicalCol) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#visualColumn

    Parameters
    ----------

    logicalCol : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::visualColumn(int logicalCol) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate12visualColumnEi', logicalCol,
    )

  @overload(int)
  def logicalRow(self, visualRow: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::logicalRow(int visualRow) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#logicalRow

    Parameters
    ----------

    visualRow : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::logicalRow(int visualRow) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate10logicalRowEi', visualRow,
    )

  @overload(int)
  def logicalColumn(self, visualCol: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::logicalColumn(int visualCol) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#logicalColumn

    Parameters
    ----------

    visualCol : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::logicalColumn(int visualCol) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate13logicalColumnEi', visualCol,
    )

  @overload(QModelIndex)
  def viewItemPosition(
      self,
      index: QModelIndex,
  ) -> QStyleOptionViewItem.ViewItemPosition:
    """
    Calls Qt's 'QStyleOptionViewItem::ViewItemPosition
    QTableViewPrivate::viewItemPosition(const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#viewItemPosition

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QStyleOptionViewItem.ViewItemPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyleOptionViewItem.ViewItemPosition(number)' gives.
    """
    #  QStyleOptionViewItem::ViewItemPosition
    #      QTableViewPrivate::viewItemPosition(const QModelIndex &index)
    #      const
    return QStyleOptionViewItem.ViewItemPosition(self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate16viewItemPositionERK11QModelIndex',
        self._valueOf(index),
    ))

  @overload(QModelIndex)
  def accessibleChildIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::accessibleChildIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#accessibleChildIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QTableViewPrivate::accessibleChildIndex(const QModelIndex &index)
    #      const
    ritual = (
        'ritual_ZNK17QTableViewPrivate20accessibleChildIndexERK11QModelInde'
        'x')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QTableViewPrivate20accessibleChildIndexERK11QMod'
          'elIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(QHeaderView, int, int)
  @overload(NoneType, int, int)
  def sectionSpanEndLogical(
      self,
      header: Optional[QHeaderView],
      logical: int,
      span: int,
  ) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::sectionSpanEndLogical(const
    QHeaderView *header, int logical, int span) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#sectionSpanEndLogical

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logical : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::sectionSpanEndLogical(const QHeaderView
    #      *header, int logical, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate21sectionSpanEndLogicalEPK11QHeaderVi'
        'ewii',
        self._addressOf(header), logical, span,
    )

  @overload(QHeaderView, int, int)
  @overload(NoneType, int, int)
  def sectionSpanSize(
      self,
      header: Optional[QHeaderView],
      logical: int,
      span: int,
  ) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::sectionSpanSize(const QHeaderView
    *header, int logical, int span) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#sectionSpanSize

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logical : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::sectionSpanSize(const QHeaderView *header, int
    #      logical, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate15sectionSpanSizeEPK11QHeaderViewii',
        self._addressOf(header), logical, span,
    )

  @overload(QHeaderView, int, int, int)
  @overload(NoneType, int, int, int)
  def spanContainsSection(
      self,
      header: Optional[QHeaderView],
      logical: int,
      spanLogical: int,
      span: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::spanContainsSection(const QHeaderView
    *header, int logical, int spanLogical, int span) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#spanContainsSection

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logical : int
      Passed on as it is.

    spanLogical : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  bool QTableViewPrivate::spanContainsSection(const QHeaderView *header,
    #      int logical, int spanLogical, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate19spanContainsSectionEPK11QHeaderView'
        'iii',
        self._addressOf(header), logical, spanLogical, span,
    )

  @overload(QModelIndex, int, QStyleOptionViewItem)
  def widthHintForIndex(
      self,
      index: QModelIndex,
      hint: int,
      option: QStyleOptionViewItem,
  ) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::widthHintForIndex(const QModelIndex
    &index, int hint, const QStyleOptionViewItem &option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#widthHintForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : int
      Passed on as it is.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.
    """
    #  int QTableViewPrivate::widthHintForIndex(const QModelIndex &index, int
    #      hint, const QStyleOptionViewItem &option) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate17widthHintForIndexERK11QModelIndexiR'
        'K20QStyleOptionViewItem',
        self._valueOf(index), hint, self._valueOf(option),
    )

  @overload(int, int)
  def span(self, row: int, column: int) -> QSpanCollection.Span:
    """
    Calls Qt's 'QSpanCollection::Span QTableViewPrivate::span(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#span

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QSpanCollection.Span
      A new cute QSpanCollection::Span around the copy Qt gave back. Python
      owns it.
    """
    #  QSpanCollection::Span QTableViewPrivate::span(int row, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate4spanEii', row, column,
    )
    return QSpanCollection.Span._cuteOwning(address)

  @overload(int, int)
  def rowSpan(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::rowSpan(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#rowSpan

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::rowSpan(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate7rowSpanEii', row, column,
    )

  @overload(int, int)
  def columnSpan(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::columnSpan(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#columnSpan

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::columnSpan(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate10columnSpanEii', row, column,
    )

  def hasSpans(self) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::hasSpans() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#hasSpans
    """
    #  bool QTableViewPrivate::hasSpans() const
    return self.uglySide.call('ritual_ZNK17QTableViewPrivate8hasSpansEv')

  @overload(int, int)
  def rowSpanHeight(self, row: int, span: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::rowSpanHeight(int row, int span)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#rowSpanHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::rowSpanHeight(int row, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate13rowSpanHeightEii', row, span,
    )

  @overload(int, int)
  def columnSpanWidth(self, column: int, span: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::columnSpanWidth(int column, int span)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#columnSpanWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::columnSpanWidth(int column, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate15columnSpanWidthEii', column, span,
    )

  @overload(int, int)
  def rowSpanEndLogical(self, row: int, span: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::rowSpanEndLogical(int row, int span)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#rowSpanEndLogical

    Parameters
    ----------

    row : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::rowSpanEndLogical(int row, int span) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate17rowSpanEndLogicalEii', row, span,
    )

  @overload(int, int)
  def columnSpanEndLogical(self, column: int, span: int) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::columnSpanEndLogical(int column, int
    span) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#columnSpanEndLogical

    Parameters
    ----------

    column : int
      Passed on as it is.

    span : int
      Passed on as it is.
    """
    #  int QTableViewPrivate::columnSpanEndLogical(int column, int span)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate20columnSpanEndLogicalEii',
        column, span,
    )

  @overload(int)
  def isRowHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::isRowHidden(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#isRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QTableViewPrivate::isRowHidden(int row) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate11isRowHiddenEi', row,
    )

  @overload(int)
  def isColumnHidden(self, column: int) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::isColumnHidden(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#isColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QTableViewPrivate::isColumnHidden(int column) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate14isColumnHiddenEi', column,
    )

  @overload(int, int)
  def isCellEnabled(self, row: int, column: int) -> bool:
    """
    Calls Qt's 'bool QTableViewPrivate::isCellEnabled(int row, int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#isCellEnabled

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  bool QTableViewPrivate::isCellEnabled(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate13isCellEnabledEii', row, column,
    )

  @overload(int, int, int, SearchDirection)
  def nextActiveVisualRow(
      self,
      rowToStart: int,
      column: int,
      limit: int,
      searchDirection: SearchDirection,
  ) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::nextActiveVisualRow(int rowToStart,
    int column, int limit, SearchDirection searchDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#nextActiveVisualRow

    Parameters
    ----------

    rowToStart : int
      Passed on as it is.

    column : int
      Passed on as it is.

    limit : int
      Passed on as it is.

    searchDirection : SearchDirection
      Passed on as its number.
    """
    #  int QTableViewPrivate::nextActiveVisualRow(int rowToStart, int column,
    #      int limit, SearchDirection searchDirection) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate19nextActiveVisualRowEiiiNS_15SearchD'
        'irectionE',
        rowToStart, column, limit, searchDirection.value,
    )

  @overload(int, int, int, SearchDirection)
  def nextActiveVisualColumn(
      self,
      row: int,
      columnToStart: int,
      limit: int,
      searchDirection: SearchDirection,
  ) -> int:
    """
    Calls Qt's 'int QTableViewPrivate::nextActiveVisualColumn(int row, int
    columnToStart, int limit, SearchDirection searchDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#nextActiveVisualColumn

    Parameters
    ----------

    row : int
      Passed on as it is.

    columnToStart : int
      Passed on as it is.

    limit : int
      Passed on as it is.

    searchDirection : SearchDirection
      Passed on as its number.
    """
    #  int QTableViewPrivate::nextActiveVisualColumn(int row, int
    #      columnToStart, int limit, SearchDirection searchDirection) const
    return self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate22nextActiveVisualColumnEiiiNS_15Sear'
        'chDirectionE',
        row, columnToStart, limit, searchDirection.value,
    )

  @overload(QSpanCollection.Span)
  def visualSpanRect(self, span: QSpanCollection.Span) -> QRect:
    """
    Calls Qt's 'QRect QTableViewPrivate::visualSpanRect(const
    QSpanCollection::Span &span) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#visualSpanRect

    Parameters
    ----------

    span : QSpanCollection.Span
      Passed on as a value: Qt reads the C++ QSpanCollection::Span, which
      stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTableViewPrivate::visualSpanRect(const QSpanCollection::Span
    #      &span) const
    address = self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate14visualSpanRectERKN15QSpanCollection'
        '4SpanE',
        self._valueOf(span),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int, int)
  def setSpan(
      self,
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::setSpan(int row, int column, int
    rowSpan, int columnSpan)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#setSpan

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is.

    columnSpan : int
      Passed on as it is.
    """
    #  void QTableViewPrivate::setSpan(int row, int column, int rowSpan, int
    #      columnSpan)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate7setSpanEiiii',
        row, column, rowSpan, columnSpan,
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
    Qt's 'QTableViewPrivate::QTableViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTableViewPrivate.__init__' has no cute function yet. Qt's "
        "'QTableViewPrivate::QTableViewPrivate()': leans on "
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

  def q_func(self) -> Optional[QTableView]:
    """
    Calls Qt's 'QTableView *QTableViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#q_func

    Returns
    -------

    Optional[QTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableView *QTableViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QTableViewPrivate6q_funcEv')
    from . import QTableView
    return QTableView._cuteAt(address)

  def clearConnections(self) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::clearConnections()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#clearConnections
    """
    #  void QTableViewPrivate::clearConnections()
    self.uglySide.call('ritual_ZN17QTableViewPrivate16clearConnectionsEv')

  @overload(QItemSelectionRange)
  @overload(NoneType)
  def trimHiddenSelections(
      self,
      range: Optional[QItemSelectionRange],
  ) -> None:
    """
    Calls Qt's 'void
    QTableViewPrivate::trimHiddenSelections(QItemSelectionRange *range)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#trimHiddenSelections

    Parameters
    ----------

    range : Optional[QItemSelectionRange]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableViewPrivate::trimHiddenSelections(QItemSelectionRange
    #      *range) const
    self.uglySide.call(
        'ritual_ZNK17QTableViewPrivate20trimHiddenSelectionsEP19QItemSelect'
        'ionRange',
        self._addressOf(range),
    )

  @overload(
      QRegion, QPainter, QStyleOptionViewItem, QBitArray, int, int, int, int,
  )
  @overload(
      QRegion, QPainter, QStyleOptionViewItem, NoneType, int, int, int, int,
  )
  @overload(
      QRegion, NoneType, QStyleOptionViewItem, QBitArray, int, int, int, int,
  )
  @overload(
      QRegion, NoneType, QStyleOptionViewItem, NoneType, int, int, int, int,
  )
  def drawAndClipSpans(
      self,
      area: QRegion,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      drawn: Optional[QBitArray],
      firstVisualRow: int,
      lastVisualRow: int,
      firstVisualColumn: int,
      lastVisualColumn: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::drawAndClipSpans(const QRegion &area,
    QPainter *painter, const QStyleOptionViewItem &option, QBitArray *drawn,
    int firstVisualRow, int lastVisualRow, int firstVisualColumn, int
    lastVisualColumn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#drawAndClipSpans

    Parameters
    ----------

    area : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    drawn : Optional[QBitArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstVisualRow : int
      Passed on as it is.

    lastVisualRow : int
      Passed on as it is.

    firstVisualColumn : int
      Passed on as it is.

    lastVisualColumn : int
      Passed on as it is.
    """
    #  void QTableViewPrivate::drawAndClipSpans(const QRegion &area, QPainter
    #      *painter, const QStyleOptionViewItem &option, QBitArray *drawn,
    #      int firstVisualRow, int lastVisualRow, int firstVisualColumn, int
    #      lastVisualColumn)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate16drawAndClipSpansERK7QRegionP8QPainte'
        'rRK20QStyleOptionViewItemP9QBitArrayiiii',
        self._valueOf(area), self._addressOf(painter), self._valueOf(option),
        self._addressOf(drawn), firstVisualRow, lastVisualRow,
        firstVisualColumn, lastVisualColumn,
    )

  @overload(QPainter, QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QStyleOptionViewItem, QModelIndex)
  def drawCell(
      self,
      painter: Optional[QPainter],
      option: QStyleOptionViewItem,
      index: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::drawCell(QPainter *painter, const
    QStyleOptionViewItem &option, const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#drawCell

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTableViewPrivate::drawCell(QPainter *painter, const
    #      QStyleOptionViewItem &option, const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate8drawCellEP8QPainterRK20QStyleOptionVi'
        'ewItemRK11QModelIndex',
        self._addressOf(painter), self._valueOf(option),
        self._valueOf(index),
    )

  @overload(int, bool)
  def selectRow(self, row: int, anchor: bool) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::selectRow(int row, bool anchor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableviewprivate.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    anchor : bool
      Passed on as it is.
    """
    #  void QTableViewPrivate::selectRow(int row, bool anchor)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate9selectRowEib', row, anchor,
    )

  @overload(int, bool)
  def selectColumn(self, column: int, anchor: bool) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::selectColumn(int column, bool
    anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#selectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    anchor : bool
      Passed on as it is.
    """
    #  void QTableViewPrivate::selectColumn(int column, bool anchor)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate12selectColumnEib', column, anchor,
    )

  @overload(QModelIndex, int, int)
  def updateSpanInsertedRows(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::updateSpanInsertedRows(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#updateSpanInsertedRows

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
    #  void QTableViewPrivate::updateSpanInsertedRows(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate22updateSpanInsertedRowsERK11QModelInd'
        'exii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def updateSpanInsertedColumns(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::updateSpanInsertedColumns(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#updateSpanInsertedColumns

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
    #  void QTableViewPrivate::updateSpanInsertedColumns(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate25updateSpanInsertedColumnsERK11QModel'
        'Indexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def updateSpanRemovedRows(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::updateSpanRemovedRows(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#updateSpanRemovedRows

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
    #  void QTableViewPrivate::updateSpanRemovedRows(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate21updateSpanRemovedRowsERK11QModelInde'
        'xii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def updateSpanRemovedColumns(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::updateSpanRemovedColumns(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#updateSpanRemovedColumns

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
    #  void QTableViewPrivate::updateSpanRemovedColumns(const QModelIndex
    #      &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate24updateSpanRemovedColumnsERK11QModelI'
        'ndexii',
        self._valueOf(parent), start, end,
    )

  @overload(int, Qt.SortOrder)
  def sortIndicatorChanged(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTableViewPrivate::sortIndicatorChanged(int column,
    Qt::SortOrder order)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableviewprivate.html#sortIndicatorChanged

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTableViewPrivate::sortIndicatorChanged(int column, Qt::SortOrder
    #      order)
    self.uglySide.call(
        'ritual_ZN17QTableViewPrivate20sortIndicatorChangedEiN2Qt9SortOrder'
        'E',
        column, order.value,
    )

  @staticmethod
  def heightHintForIndex(*__, **_) -> Never:
    """
    Qt's 'int QTableViewPrivate::heightHintForIndex(const QModelIndex &index,
    int hint, QStyleOptionViewItem &option) const': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTableViewPrivate.heightHintForIndex' has no cute function yet. "
        "Qt's 'int QTableViewPrivate::heightHintForIndex(const QModelIndex "
        "&index, int hint, QStyleOptionViewItem &option) const': takes a "
        "type Python has no way to hand over yet.")
