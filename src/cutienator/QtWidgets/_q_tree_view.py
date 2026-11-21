"""
QTreeView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtreeview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractItemView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QItemSelectionModel, QMetaObject
  from ..QtCore import QModelIndex, QPoint, QRect
  from . import QHeaderView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QHeaderView = WAIT['QHeaderView']
  QItemSelectionModel = WAIT['QItemSelectionModel']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeView(QAbstractItemView):
  """
  The cute side of Qt's QTreeView: a plain Python object standing in front of
  one C++ QTreeView.

  It is built on the cute 'QAbstractItemView', as Qt's QTreeView is built on
  Qt's QAbstractItemView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeView that has a ritual and that Python can call
  so far, 64 names in all: 'metaObject', 'tr', 'setModel', 'setRootIndex',
  'setSelectionModel', 'header', 'setHeader', 'autoExpandDelay',
  'setAutoExpandDelay', 'indentation', 'setIndentation', 'resetIndentation',
  'rootIsDecorated', 'setRootIsDecorated', 'uniformRowHeights',
  'setUniformRowHeights', 'itemsExpandable', 'setItemsExpandable',
  'expandsOnDoubleClick', 'setExpandsOnDoubleClick',
  'columnViewportPosition', 'columnWidth', 'setColumnWidth', 'columnAt',
  'isColumnHidden', 'setColumnHidden', 'isHeaderHidden', 'setHeaderHidden',
  'isRowHidden', 'setRowHidden', 'isFirstColumnSpanned',
  'setFirstColumnSpanned', 'isExpanded', 'setExpanded', 'setSortingEnabled',
  'isSortingEnabled', 'setAnimated', 'isAnimated', 'setAllColumnsShowFocus',
  'allColumnsShowFocus', 'setWordWrap', 'wordWrap', 'setTreePosition',
  'treePosition', 'keyboardSearch', 'visualRect', 'itemDecorationRect',
  'scrollTo', 'indexAt', 'indexAbove', 'indexBelow', 'doItemsLayout',
  'reset', 'selectAll', 'hideColumn', 'showColumn', 'expand', 'collapse',
  'resizeColumnToContents', 'sortByColumn', 'expandAll', 'expandRecursively',
  'collapseAll', 'expandToDepth'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeView::~QTreeView()': the destructor: Python never removes a
    C++ QTreeView.

  What has no ritual
  ------------------

  50 of the 116 functions Qt declares: 38 protected; 4 private; 3 takes or
  gives a type that cannot be passed yet; 2 a signal; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QTreeView is created at the first use, not by 'QTreeView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeView.
  - Qt tells when it has removed the C++ QTreeView. Every call on the cute
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
    Calls Qt's 'QString QTreeView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#tr

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
    #  QString QTreeView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QTreeView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTreeView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTreeView::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QTreeView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def header(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QTreeView::header() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#header

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QTreeView::header() const
    address = self.uglySide.call('ritual_ZNK9QTreeView6headerEv')
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  def autoExpandDelay(self) -> int:
    """
    Calls Qt's 'int QTreeView::autoExpandDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#autoExpandDelay
    """
    #  int QTreeView::autoExpandDelay() const
    return self.uglySide.call('ritual_ZNK9QTreeView15autoExpandDelayEv')

  def indentation(self) -> int:
    """
    Calls Qt's 'int QTreeView::indentation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#indentation
    """
    #  int QTreeView::indentation() const
    return self.uglySide.call('ritual_ZNK9QTreeView11indentationEv')

  def rootIsDecorated(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::rootIsDecorated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#rootIsDecorated
    """
    #  bool QTreeView::rootIsDecorated() const
    return self.uglySide.call('ritual_ZNK9QTreeView15rootIsDecoratedEv')

  def uniformRowHeights(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::uniformRowHeights() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#uniformRowHeights
    """
    #  bool QTreeView::uniformRowHeights() const
    return self.uglySide.call('ritual_ZNK9QTreeView17uniformRowHeightsEv')

  def itemsExpandable(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::itemsExpandable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#itemsExpandable
    """
    #  bool QTreeView::itemsExpandable() const
    return self.uglySide.call('ritual_ZNK9QTreeView15itemsExpandableEv')

  def expandsOnDoubleClick(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::expandsOnDoubleClick() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#expandsOnDoubleClick
    """
    #  bool QTreeView::expandsOnDoubleClick() const
    return self.uglySide.call('ritual_ZNK9QTreeView20expandsOnDoubleClickEv')

  @overload(int)
  def columnViewportPosition(self, column: int) -> int:
    """
    Calls Qt's 'int QTreeView::columnViewportPosition(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#columnViewportPosition

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QTreeView::columnViewportPosition(int column) const
    return self.uglySide.call(
        'ritual_ZNK9QTreeView22columnViewportPositionEi', column,
    )

  @overload(int)
  def columnWidth(self, column: int) -> int:
    """
    Calls Qt's 'int QTreeView::columnWidth(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#columnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QTreeView::columnWidth(int column) const
    return self.uglySide.call('ritual_ZNK9QTreeView11columnWidthEi', column)

  @overload(int)
  def columnAt(self, x: int) -> int:
    """
    Calls Qt's 'int QTreeView::columnAt(int x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#columnAt

    Parameters
    ----------

    x : int
      Passed on as it is.
    """
    #  int QTreeView::columnAt(int x) const
    return self.uglySide.call('ritual_ZNK9QTreeView8columnAtEi', x)

  @overload(int)
  def isColumnHidden(self, column: int) -> bool:
    """
    Calls Qt's 'bool QTreeView::isColumnHidden(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QTreeView::isColumnHidden(int column) const
    return self.uglySide.call(
        'ritual_ZNK9QTreeView14isColumnHiddenEi', column,
    )

  def isHeaderHidden(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::isHeaderHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isHeaderHidden
    """
    #  bool QTreeView::isHeaderHidden() const
    return self.uglySide.call('ritual_ZNK9QTreeView14isHeaderHiddenEv')

  @overload(int, QModelIndex)
  def isRowHidden(self, row: int, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeView::isRowHidden(int row, const QModelIndex
    &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeView::isRowHidden(int row, const QModelIndex &parent) const
    return self.uglySide.call(
        'ritual_ZNK9QTreeView11isRowHiddenEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(int, QModelIndex)
  def isFirstColumnSpanned(self, row: int, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeView::isFirstColumnSpanned(int row, const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#isFirstColumnSpanned

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeView::isFirstColumnSpanned(int row, const QModelIndex
    #      &parent) const
    return self.uglySide.call(
        'ritual_ZNK9QTreeView20isFirstColumnSpannedEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(QModelIndex)
  def isExpanded(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeView::isExpanded(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isExpanded

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeView::isExpanded(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK9QTreeView10isExpandedERK11QModelIndex',
        self._valueOf(index),
    )

  def isSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::isSortingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isSortingEnabled
    """
    #  bool QTreeView::isSortingEnabled() const
    return self.uglySide.call('ritual_ZNK9QTreeView16isSortingEnabledEv')

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#isAnimated
    """
    #  bool QTreeView::isAnimated() const
    return self.uglySide.call('ritual_ZNK9QTreeView10isAnimatedEv')

  def allColumnsShowFocus(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::allColumnsShowFocus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#allColumnsShowFocus
    """
    #  bool QTreeView::allColumnsShowFocus() const
    return self.uglySide.call('ritual_ZNK9QTreeView19allColumnsShowFocusEv')

  def wordWrap(self) -> bool:
    """
    Calls Qt's 'bool QTreeView::wordWrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#wordWrap
    """
    #  bool QTreeView::wordWrap() const
    return self.uglySide.call('ritual_ZNK9QTreeView8wordWrapEv')

  def treePosition(self) -> int:
    """
    Calls Qt's 'int QTreeView::treePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#treePosition
    """
    #  int QTreeView::treePosition() const
    return self.uglySide.call('ritual_ZNK9QTreeView12treePositionEv')

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QTreeView::visualRect(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#visualRect

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
    #  QRect QTreeView::visualRect(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK9QTreeView10visualRectERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex)
  def itemDecorationRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QTreeView::itemDecorationRect(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#itemDecorationRect

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
    #  QRect QTreeView::itemDecorationRect(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK9QTreeView18itemDecorationRectERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def indexAt(self, p: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeView::indexAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#indexAt

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
    #  QModelIndex QTreeView::indexAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK9QTreeView7indexAtERK6QPoint', self._valueOf(p),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def indexAbove(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeView::indexAbove(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#indexAbove

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeView::indexAbove(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK9QTreeView10indexAboveERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def indexBelow(self, index: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeView::indexBelow(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#indexBelow

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeView::indexBelow(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK9QTreeView10indexBelowERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QTreeView::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeView::setModel(QAbstractItemModel *model)
    self.uglySide.call(
        'ritual_ZN9QTreeView8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QTreeView::setRootIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTreeView::setRootIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN9QTreeView12setRootIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QTreeView::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeView::setSelectionModel(QItemSelectionModel *selectionModel)
    self.uglySide.call(
        'ritual_ZN9QTreeView17setSelectionModelEP19QItemSelectionModel',
        self._addressOf(selectionModel),
    )

  @overload(QHeaderView)
  @overload(NoneType)
  def setHeader(self, header: Optional[QHeaderView]) -> None:
    """
    Calls Qt's 'void QTreeView::setHeader(QHeaderView *header)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setHeader

    Parameters
    ----------

    header : Optional[QHeaderView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeView::setHeader(QHeaderView *header)
    self.uglySide.call(
        'ritual_ZN9QTreeView9setHeaderEP11QHeaderView',
        self._addressOf(header),
    )

  @overload(int)
  def setAutoExpandDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QTreeView::setAutoExpandDelay(int delay)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setAutoExpandDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QTreeView::setAutoExpandDelay(int delay)
    self.uglySide.call('ritual_ZN9QTreeView18setAutoExpandDelayEi', delay)

  @overload(int)
  def setIndentation(self, i: int) -> None:
    """
    Calls Qt's 'void QTreeView::setIndentation(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setIndentation

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QTreeView::setIndentation(int i)
    self.uglySide.call('ritual_ZN9QTreeView14setIndentationEi', i)

  @overload(bool)
  def setRootIsDecorated(self, show: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setRootIsDecorated(bool show)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setRootIsDecorated

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QTreeView::setRootIsDecorated(bool show)
    self.uglySide.call('ritual_ZN9QTreeView18setRootIsDecoratedEb', show)

  @overload(bool)
  def setUniformRowHeights(self, uniform: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setUniformRowHeights(bool uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#setUniformRowHeights

    Parameters
    ----------

    uniform : bool
      Passed on as it is.
    """
    #  void QTreeView::setUniformRowHeights(bool uniform)
    self.uglySide.call(
        'ritual_ZN9QTreeView20setUniformRowHeightsEb', uniform,
    )

  @overload(bool)
  def setItemsExpandable(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setItemsExpandable(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setItemsExpandable

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTreeView::setItemsExpandable(bool enable)
    self.uglySide.call('ritual_ZN9QTreeView18setItemsExpandableEb', enable)

  @overload(bool)
  def setExpandsOnDoubleClick(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setExpandsOnDoubleClick(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#setExpandsOnDoubleClick

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTreeView::setExpandsOnDoubleClick(bool enable)
    self.uglySide.call(
        'ritual_ZN9QTreeView23setExpandsOnDoubleClickEb', enable,
    )

  @overload(int, int)
  def setColumnWidth(self, column: int, width: int) -> None:
    """
    Calls Qt's 'void QTreeView::setColumnWidth(int column, int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QTreeView::setColumnWidth(int column, int width)
    self.uglySide.call(
        'ritual_ZN9QTreeView14setColumnWidthEii', column, width,
    )

  @overload(int, bool)
  def setColumnHidden(self, column: int, hide: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setColumnHidden(int column, bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setColumnHidden

    Parameters
    ----------

    column : int
      Passed on as it is.

    hide : bool
      Passed on as it is.
    """
    #  void QTreeView::setColumnHidden(int column, bool hide)
    self.uglySide.call(
        'ritual_ZN9QTreeView15setColumnHiddenEib', column, hide,
    )

  @overload(bool)
  def setHeaderHidden(self, hide: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setHeaderHidden(bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setHeaderHidden

    Parameters
    ----------

    hide : bool
      Passed on as it is.
    """
    #  void QTreeView::setHeaderHidden(bool hide)
    self.uglySide.call('ritual_ZN9QTreeView15setHeaderHiddenEb', hide)

  @overload(int, QModelIndex, bool)
  def setRowHidden(self, row: int, parent: QModelIndex, hide: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setRowHidden(int row, const QModelIndex
    &parent, bool hide)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setRowHidden

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hide : bool
      Passed on as it is.
    """
    #  void QTreeView::setRowHidden(int row, const QModelIndex &parent, bool
    #      hide)
    self.uglySide.call(
        'ritual_ZN9QTreeView12setRowHiddenEiRK11QModelIndexb',
        row, self._valueOf(parent), hide,
    )

  @overload(int, QModelIndex, bool)
  def setFirstColumnSpanned(
      self,
      row: int,
      parent: QModelIndex,
      span: bool,
  ) -> None:
    """
    Calls Qt's 'void QTreeView::setFirstColumnSpanned(int row, const
    QModelIndex &parent, bool span)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#setFirstColumnSpanned

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    span : bool
      Passed on as it is.
    """
    #  void QTreeView::setFirstColumnSpanned(int row, const QModelIndex
    #      &parent, bool span)
    self.uglySide.call(
        'ritual_ZN9QTreeView21setFirstColumnSpannedEiRK11QModelIndexb',
        row, self._valueOf(parent), span,
    )

  @overload(QModelIndex, bool)
  def setExpanded(self, index: QModelIndex, expand: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setExpanded(const QModelIndex &index, bool
    expand)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setExpanded

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    expand : bool
      Passed on as it is.
    """
    #  void QTreeView::setExpanded(const QModelIndex &index, bool expand)
    self.uglySide.call(
        'ritual_ZN9QTreeView11setExpandedERK11QModelIndexb',
        self._valueOf(index), expand,
    )

  @overload(bool)
  def setSortingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setSortingEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setSortingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTreeView::setSortingEnabled(bool enable)
    self.uglySide.call('ritual_ZN9QTreeView17setSortingEnabledEb', enable)

  @overload(bool)
  def setAnimated(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setAnimated(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setAnimated

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTreeView::setAnimated(bool enable)
    self.uglySide.call('ritual_ZN9QTreeView11setAnimatedEb', enable)

  @overload(bool)
  def setAllColumnsShowFocus(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setAllColumnsShowFocus(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#setAllColumnsShowFocus

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTreeView::setAllColumnsShowFocus(bool enable)
    self.uglySide.call(
        'ritual_ZN9QTreeView22setAllColumnsShowFocusEb', enable,
    )

  @overload(bool)
  def setWordWrap(self, on: bool) -> None:
    """
    Calls Qt's 'void QTreeView::setWordWrap(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setWordWrap

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QTreeView::setWordWrap(bool on)
    self.uglySide.call('ritual_ZN9QTreeView11setWordWrapEb', on)

  @overload(int)
  def setTreePosition(self, logicalIndex: int) -> None:
    """
    Calls Qt's 'void QTreeView::setTreePosition(int logicalIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#setTreePosition

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.
    """
    #  void QTreeView::setTreePosition(int logicalIndex)
    self.uglySide.call(
        'ritual_ZN9QTreeView15setTreePositionEi', logicalIndex,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QTreeView::QTreeView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#QTreeView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTreeView::QTreeView(QWidget *parent)
    self._noteCreation(QTreeView, lambda: Rituals.call(
        'ritual_ZN9QTreeViewC1EP7QWidget', self._addressOf(parent),
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

  def resetIndentation(self) -> None:
    """
    Calls Qt's 'void QTreeView::resetIndentation()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#resetIndentation
    """
    #  void QTreeView::resetIndentation()
    self.uglySide.call('ritual_ZN9QTreeView16resetIndentationEv')

  @overload(str)
  def keyboardSearch(self, search: str) -> None:
    """
    Calls Qt's 'void QTreeView::keyboardSearch(const QString &search)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#keyboardSearch

    Parameters
    ----------

    search : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeView::keyboardSearch(const QString &search)
    self.uglySide.call(
        'ritual_ZN9QTreeView14keyboardSearchERK7QString', search,
    )

  @overload(QModelIndex)
  @overload(QModelIndex, QAbstractItemView.ScrollHint)
  def scrollTo(
      self,
      index: QModelIndex,
      hint: QAbstractItemView.ScrollHint = (
          QAbstractItemView.ScrollHint.EnsureVisible),
  ) -> None:
    """
    Calls Qt's 'void QTreeView::scrollTo(const QModelIndex &index, ScrollHint
    hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#scrollTo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      QAbstractItemView.ScrollHint.EnsureVisible.
    """
    #  void QTreeView::scrollTo(const QModelIndex &index, ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN9QTreeView8scrollToERK11QModelIndexN17QAbstractItemView10'
        'ScrollHintE',
        self._valueOf(index), hint.value,
    )

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QTreeView::doItemsLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#doItemsLayout
    """
    #  void QTreeView::doItemsLayout()
    self.uglySide.call('ritual_ZN9QTreeView13doItemsLayoutEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QTreeView::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#reset
    """
    #  void QTreeView::reset()
    self.uglySide.call('ritual_ZN9QTreeView5resetEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QTreeView::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#selectAll
    """
    #  void QTreeView::selectAll()
    self.uglySide.call('ritual_ZN9QTreeView9selectAllEv')

  @overload(int)
  def hideColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTreeView::hideColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#hideColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTreeView::hideColumn(int column)
    self.uglySide.call('ritual_ZN9QTreeView10hideColumnEi', column)

  @overload(int)
  def showColumn(self, column: int) -> None:
    """
    Calls Qt's 'void QTreeView::showColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#showColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTreeView::showColumn(int column)
    self.uglySide.call('ritual_ZN9QTreeView10showColumnEi', column)

  @overload(QModelIndex)
  def expand(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QTreeView::expand(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#expand

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTreeView::expand(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN9QTreeView6expandERK11QModelIndex', self._valueOf(index),
    )

  @overload(QModelIndex)
  def collapse(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QTreeView::collapse(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#collapse

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTreeView::collapse(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN9QTreeView8collapseERK11QModelIndex', self._valueOf(index),
    )

  @overload(int)
  def resizeColumnToContents(self, column: int) -> None:
    """
    Calls Qt's 'void QTreeView::resizeColumnToContents(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreeview.html#resizeColumnToContents

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  void QTreeView::resizeColumnToContents(int column)
    self.uglySide.call(
        'ritual_ZN9QTreeView22resizeColumnToContentsEi', column,
    )

  @overload(int, Qt.SortOrder)
  def sortByColumn(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeView::sortByColumn(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#sortByColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeView::sortByColumn(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN9QTreeView12sortByColumnEiN2Qt9SortOrderE',
        column, order.value,
    )

  def expandAll(self) -> None:
    """
    Calls Qt's 'void QTreeView::expandAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#expandAll
    """
    #  void QTreeView::expandAll()
    self.uglySide.call('ritual_ZN9QTreeView9expandAllEv')

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def expandRecursively(self, index: QModelIndex, depth: int = -1) -> None:
    """
    Calls Qt's 'void QTreeView::expandRecursively(const QModelIndex &index,
    int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#expandRecursively

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    depth : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QTreeView::expandRecursively(const QModelIndex &index, int depth)
    self.uglySide.call(
        'ritual_ZN9QTreeView17expandRecursivelyERK11QModelIndexi',
        self._valueOf(index), depth,
    )

  def collapseAll(self) -> None:
    """
    Calls Qt's 'void QTreeView::collapseAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#collapseAll
    """
    #  void QTreeView::collapseAll()
    self.uglySide.call('ritual_ZN9QTreeView11collapseAllEv')

  @overload(int)
  def expandToDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QTreeView::expandToDepth(int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreeview.html#expandToDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QTreeView::expandToDepth(int depth)
    self.uglySide.call('ritual_ZN9QTreeView13expandToDepthEi', depth)
