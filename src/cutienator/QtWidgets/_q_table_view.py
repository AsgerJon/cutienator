"""
QTableView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtableview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QAbstractItemModel
from ._q_abstract_item_view import QAbstractItemView
from ._q_header_view import QHeaderView
from ..QtCore import QItemSelectionModel
from ..QtCore import QMetaObject
from ..QtCore import QModelIndex
from ..QtCore import QPoint
from ..QtCore import QRect
from ._q_widget import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTableView(QAbstractItemView):
  """
  The cute side of Qt's QTableView: a plain Python object standing in front
  of one C++ QTableView.

  It is built on the cute 'QAbstractItemView', as Qt's QTableView is built on
  Qt's QAbstractItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTableView that has a ritual and that Python can
  call so far, 50 names in all: 'metaObject', 'tr', 'setModel',
  'setRootIndex', 'setSelectionModel', 'doItemsLayout', 'horizontalHeader',
  'verticalHeader', 'setHorizontalHeader', 'setVerticalHeader',
  'rowViewportPosition', 'rowAt', 'setRowHeight', 'rowHeight',
  'columnViewportPosition', 'columnAt', 'setColumnWidth', 'columnWidth',
  'isRowHidden', 'setRowHidden', 'isColumnHidden', 'setColumnHidden',
  'setSortingEnabled', 'isSortingEnabled', 'showGrid', 'gridStyle',
  'setGridStyle', 'setWordWrap', 'wordWrap', 'setCornerButtonEnabled',
  'isCornerButtonEnabled', 'visualRect', 'scrollTo', 'indexAt', 'setSpan',
  'rowSpan', 'columnSpan', 'clearSpans', 'selectRow', 'selectColumn',
  'hideRow', 'hideColumn', 'showRow', 'showColumn', 'resizeRowToContents',
  'resizeRowsToContents', 'resizeColumnToContents',
  'resizeColumnsToContents', 'sortByColumn', 'setShowGrid'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableView::~QTableView()': the destructor: Python never removes a
    C++ QTableView.

  What has no ritual
  ------------------

  36 of the 88 functions Qt declares: 27 protected; 4 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QTableView is created at the first use, not by 'QTableView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTableView.
  - Qt tells when it has removed the C++ QTableView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString QTableView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#tr

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
    #  QString QTableView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QTableView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTableView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTableView::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTableView10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def horizontalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QTableView::horizontalHeader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#horizontalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QTableView::horizontalHeader() const
    address = self.uglySide.call(
        'ritual_ZNK10QTableView16horizontalHeaderEv',
    )
    return QHeaderView._cuteAt(address)

  def verticalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QTableView::verticalHeader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#verticalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QTableView::verticalHeader() const
    address = self.uglySide.call('ritual_ZNK10QTableView14verticalHeaderEv')
    return QHeaderView._cuteAt(address)

  @overload(int)
  def rowViewportPosition(self, row: int) -> int:
    """
    Calls Qt's 'int QTableView::rowViewportPosition(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#rowViewportPosition

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QTableView::rowViewportPosition(int row) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView19rowViewportPositionEi', row,
    )

  @overload(int)
  def rowAt(self, y: int) -> int:
    """
    Calls Qt's 'int QTableView::rowAt(int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#rowAt

    Parameters
    ----------

    y : int
      Passed on as it is.
    """
    #  int QTableView::rowAt(int y) const
    return self.uglySide.call('ritual_ZNK10QTableView5rowAtEi', y)

  @overload(int)
  def rowHeight(self, row: int) -> int:
    """
    Calls Qt's 'int QTableView::rowHeight(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#rowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QTableView::rowHeight(int row) const
    return self.uglySide.call('ritual_ZNK10QTableView9rowHeightEi', row)

  @overload(int)
  def columnViewportPosition(self, column: int) -> int:
    """
    Calls Qt's 'int QTableView::columnViewportPosition(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#columnViewportPosition

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QTableView::columnViewportPosition(int column) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView22columnViewportPositionEi', column,
    )

  @overload(int)
  def columnAt(self, x: int) -> int:
    """
    Calls Qt's 'int QTableView::columnAt(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#columnAt

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QTableView::columnAt(int x) const
    return self.uglySide.call('ritual_ZNK10QTableView8columnAtEi', x)

  @overload(int)
  def columnWidth(self, column: int) -> int:
    """
    Calls Qt's 'int QTableView::columnWidth(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#columnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QTableView::columnWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView11columnWidthEi', column,
    )

  @overload(int)
  def isRowHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QTableView::isRowHidden(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#isRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QTableView::isRowHidden(int row) const
    return self.uglySide.call('ritual_ZNK10QTableView11isRowHiddenEi', row)

  @overload(int)
  def isColumnHidden(self, column: int) -> bool:
    """
    Calls Qt's 'bool QTableView::isColumnHidden(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#isColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QTableView::isColumnHidden(int column) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView14isColumnHiddenEi', column,
    )

  def isSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTableView::isSortingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#isSortingEnabled
    """
    #  bool QTableView::isSortingEnabled() const
    return self.uglySide.call('ritual_ZNK10QTableView16isSortingEnabledEv')

  def showGrid(self) -> bool:
    """
    Calls Qt's 'bool QTableView::showGrid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#showGrid
    """
    #  bool QTableView::showGrid() const
    return self.uglySide.call('ritual_ZNK10QTableView8showGridEv')

  def gridStyle(self) -> Qt.PenStyle:
    """
    Calls Qt's 'Qt::PenStyle QTableView::gridStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#gridStyle

    Returns
    -------

    Qt.PenStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenStyle(number)'
      gives.
    """
    #  Qt::PenStyle QTableView::gridStyle() const
    return Qt.PenStyle(self.uglySide.call(
        'ritual_ZNK10QTableView9gridStyleEv',
    ))

  def wordWrap(self) -> bool:
    """
    Calls Qt's 'bool QTableView::wordWrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#wordWrap
    """
    #  bool QTableView::wordWrap() const
    return self.uglySide.call('ritual_ZNK10QTableView8wordWrapEv')

  def isCornerButtonEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTableView::isCornerButtonEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#isCornerButtonEnabled
    """
    #  bool QTableView::isCornerButtonEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10QTableView21isCornerButtonEnabledEv',
    )

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QTableView::visualRect(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#visualRect

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
    #  QRect QTableView::visualRect(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK10QTableView10visualRectERK11QModelIndex',
        self._valueOf(index),
    )
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def indexAt(self, p: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTableView::indexAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#indexAt

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
    #  QModelIndex QTableView::indexAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK10QTableView7indexAtERK6QPoint', self._valueOf(p),
    )
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def rowSpan(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QTableView::rowSpan(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#rowSpan

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QTableView::rowSpan(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView7rowSpanEii', row, column,
    )

  @overload(int, int)
  def columnSpan(self, row: int, column: int) -> int:
    """
    Calls Qt's 'int QTableView::columnSpan(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#columnSpan

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  int QTableView::columnSpan(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK10QTableView10columnSpanEii', row, column,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QTableView::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableView::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN10QTableView8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QTableView::setRootIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTableView::setRootIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN10QTableView12setRootIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QTableView::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableView::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    self.uglySide.call(
        'ritual_ZN10QTableView17setSelectionModelEP19QItemSelectionModel',
        self._addressOf(selectionModel),
    )

  @overload(QHeaderView)
  @overload(NoneType)
  def setHorizontalHeader(self, header: Optional[QHeaderView]) -> None:
    """
    Calls Qt's 'void QTableView::setHorizontalHeader(QHeaderView *header)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#setHorizontalHeader

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableView::setHorizontalHeader(QHeaderView *header)
    self.uglySide.call(
        'ritual_ZN10QTableView19setHorizontalHeaderEP11QHeaderView',
        self._addressOf(header),
    )

  @overload(QHeaderView)
  @overload(NoneType)
  def setVerticalHeader(self, header: Optional[QHeaderView]) -> None:
    """
    Calls Qt's 'void QTableView::setVerticalHeader(QHeaderView *header)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setVerticalHeader

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableView::setVerticalHeader(QHeaderView *header)
    self.uglySide.call(
        'ritual_ZN10QTableView17setVerticalHeaderEP11QHeaderView',
        self._addressOf(header),
    )

  @overload(int, int)
  def setRowHeight(self, row: int, height: int) -> None:
    """
    Calls Qt's 'void QTableView::setRowHeight(int row, int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QTableView::setRowHeight(int row, int height)
    self.uglySide.call('ritual_ZN10QTableView12setRowHeightEii', row, height)

  @overload(int, int)
  def setColumnWidth(self, column: int, width: int) -> None:
    """
    Calls Qt's 'void QTableView::setColumnWidth(int column, int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QTableView::setColumnWidth(int column, int width)
    self.uglySide.call(
        'ritual_ZN10QTableView14setColumnWidthEii', column, width,
    )

  @overload(int, bool)
  def setRowHidden(self, row: int, hide: bool) -> None:
    """
    Calls Qt's 'void QTableView::setRowHidden(int row, bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.

    hide : bool
      Passed on as it is.
    """
    #  void QTableView::setRowHidden(int row, bool hide)
    self.uglySide.call('ritual_ZN10QTableView12setRowHiddenEib', row, hide)

  @overload(int, bool)
  def setColumnHidden(self, column: int, hide: bool) -> None:
    """
    Calls Qt's 'void QTableView::setColumnHidden(int column, bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.

    hide : bool
      Passed on as it is.
    """
    #  void QTableView::setColumnHidden(int column, bool hide)
    self.uglySide.call(
        'ritual_ZN10QTableView15setColumnHiddenEib', column, hide,
    )

  @overload(bool)
  def setSortingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTableView::setSortingEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setSortingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTableView::setSortingEnabled(bool enable)
    self.uglySide.call('ritual_ZN10QTableView17setSortingEnabledEb', enable)

  @overload(Qt.PenStyle)
  def setGridStyle(self, style: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void QTableView::setGridStyle(Qt::PenStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setGridStyle

    Parameters
    ----------

    style : Qt.PenStyle
      Passed on as its number.
    """
    #  void QTableView::setGridStyle(Qt::PenStyle style)
    self.uglySide.call(
        'ritual_ZN10QTableView12setGridStyleEN2Qt8PenStyleE', style.value,
    )

  @overload(bool)
  def setWordWrap(self, on: bool) -> None:
    """
    Calls Qt's 'void QTableView::setWordWrap(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setWordWrap

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QTableView::setWordWrap(bool on)
    self.uglySide.call('ritual_ZN10QTableView11setWordWrapEb', on)

  @overload(bool)
  def setCornerButtonEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTableView::setCornerButtonEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#setCornerButtonEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTableView::setCornerButtonEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN10QTableView22setCornerButtonEnabledEb', enable,
    )

  @overload(int, int, int, int)
  def setSpan(
      self,
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
  ) -> None:
    """
    Calls Qt's 'void QTableView::setSpan(int row, int column, int rowSpan,
    int columnSpan)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setSpan

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
    #  void QTableView::setSpan(int row, int column, int rowSpan, int
    #      columnSpan)
    self.uglySide.call(
        'ritual_ZN10QTableView7setSpanEiiii',
        row, column, rowSpan, columnSpan,
    )

  @overload(bool)
  def setShowGrid(self, show: bool) -> None:
    """
    Calls Qt's 'void QTableView::setShowGrid(bool show)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#setShowGrid

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QTableView::setShowGrid(bool show)
    self.uglySide.call('ritual_ZN10QTableView11setShowGridEb', show)

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
    Notes what was given, for Qt's 'QTableView::QTableView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#QTableView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTableView::QTableView(QWidget *parent)
    self._noteCreation(QTableView, lambda: Rituals.call(
        'ritual_ZN10QTableViewC1EP7QWidget', self._addressOf(parent),
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

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QTableView::doItemsLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#doItemsLayout
    """
    #  void QTableView::doItemsLayout()
    self.uglySide.call('ritual_ZN10QTableView13doItemsLayoutEv')

  @overload(QModelIndex)
  @overload(QModelIndex, QAbstractItemView.ScrollHint)
  def scrollTo(
      self,
      index: QModelIndex,
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QTableView::scrollTo(const QModelIndex &index,
    ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#scrollTo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QTableView::scrollTo(const QModelIndex &index, ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN10QTableView8scrollToERK11QModelIndexN17QAbstractItemView'
        '10ScrollHintE',
        self._valueOf(index), hint.value,
    )

  def clearSpans(self) -> None:
    """
    Calls Qt's 'void QTableView::clearSpans()'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#clearSpans
    """
    #  void QTableView::clearSpans()
    self.uglySide.call('ritual_ZN10QTableView10clearSpansEv')

  @overload(int)
  def selectRow(self, row: int) -> None:
    """
    Calls Qt's 'void QTableView::selectRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableView::selectRow(int row)
    self.uglySide.call('ritual_ZN10QTableView9selectRowEi', row)

  @overload(int)
  def selectColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTableView::selectColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#selectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableView::selectColumn(int column)
    self.uglySide.call('ritual_ZN10QTableView12selectColumnEi', column)

  @overload(int)
  def hideRow(self, row: int) -> None:
    """
    Calls Qt's 'void QTableView::hideRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#hideRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableView::hideRow(int row)
    self.uglySide.call('ritual_ZN10QTableView7hideRowEi', row)

  @overload(int)
  def hideColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTableView::hideColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#hideColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableView::hideColumn(int column)
    self.uglySide.call('ritual_ZN10QTableView10hideColumnEi', column)

  @overload(int)
  def showRow(self, row: int) -> None:
    """
    Calls Qt's 'void QTableView::showRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#showRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableView::showRow(int row)
    self.uglySide.call('ritual_ZN10QTableView7showRowEi', row)

  @overload(int)
  def showColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTableView::showColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#showColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableView::showColumn(int column)
    self.uglySide.call('ritual_ZN10QTableView10showColumnEi', column)

  @overload(int)
  def resizeRowToContents(self, row: int) -> None:
    """
    Calls Qt's 'void QTableView::resizeRowToContents(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#resizeRowToContents

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QTableView::resizeRowToContents(int row)
    self.uglySide.call('ritual_ZN10QTableView19resizeRowToContentsEi', row)

  def resizeRowsToContents(self) -> None:
    """
    Calls Qt's 'void QTableView::resizeRowsToContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#resizeRowsToContents
    """
    #  void QTableView::resizeRowsToContents()
    self.uglySide.call('ritual_ZN10QTableView20resizeRowsToContentsEv')

  @overload(int)
  def resizeColumnToContents(self, column: int) -> None:
    """
    Calls Qt's 'void QTableView::resizeColumnToContents(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#resizeColumnToContents

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTableView::resizeColumnToContents(int column)
    self.uglySide.call(
        'ritual_ZN10QTableView22resizeColumnToContentsEi', column,
    )

  def resizeColumnsToContents(self) -> None:
    """
    Calls Qt's 'void QTableView::resizeColumnsToContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtableview.html#resizeColumnsToContents
    """
    #  void QTableView::resizeColumnsToContents()
    self.uglySide.call('ritual_ZN10QTableView23resizeColumnsToContentsEv')

  @overload(int, Qt.SortOrder)
  def sortByColumn(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTableView::sortByColumn(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtableview.html#sortByColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTableView::sortByColumn(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN10QTableView12sortByColumnEiN2Qt9SortOrderE',
        column, order.value,
    )
