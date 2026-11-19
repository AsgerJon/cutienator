"""
QTreeWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ._q_abstract_item_view import QAbstractItemView
from ..QtCore import QItemSelectionModel
from ..QtCore import QMetaObject
from ..QtCore import QModelIndex
from ..QtCore import QPoint
from ..QtCore import QRect
from ._q_tree_view import QTreeView
from ._q_widget import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeWidget(QTreeView):
  """
  The cute side of Qt's QTreeWidget: a plain Python object standing in front
  of one C++ QTreeWidget.

  It is built on the cute 'QTreeView', as Qt's QTreeWidget is built on Qt's
  QTreeView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeWidget that has a ritual and that Python can
  call so far, 39 names in all: 'metaObject', 'tr', 'columnCount',
  'setColumnCount', 'invisibleRootItem', 'topLevelItem', 'topLevelItemCount',
  'insertTopLevelItem', 'addTopLevelItem', 'takeTopLevelItem',
  'indexOfTopLevelItem', 'headerItem', 'setHeaderItem', 'setHeaderLabel',
  'currentItem', 'currentColumn', 'setCurrentItem', 'itemAt',
  'visualItemRect', 'sortColumn', 'sortItems', 'editItem',
  'openPersistentEditor', 'closePersistentEditor', 'isPersistentEditorOpen',
  'itemWidget', 'setItemWidget', 'removeItemWidget', 'itemAbove',
  'itemBelow', 'indexFromItem', 'itemFromIndex', 'setSelectionModel',
  'supportedDragActions', 'setSupportedDragActions', 'scrollToItem',
  'expandItem', 'collapseItem', 'clear'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTreeWidget::~QTreeWidget()': the destructor: Python never removes
    a C++ QTreeWidget.

  What has no ritual
  ------------------

  30 of the 74 functions Qt declares: 10 a signal; 7 takes or gives a type
  that cannot be passed yet; 6 protected; 4 private; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QTreeWidget is created at the first use, not by
    'QTreeWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeWidget.
  - Qt tells when it has removed the C++ QTreeWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

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
    Calls Qt's 'QString QTreeWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#tr

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
    #  QString QTreeWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTreeWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTreeWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTreeWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#columnCount
    """
    #  int QTreeWidget::columnCount() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget11columnCountEv')

  def invisibleRootItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::invisibleRootItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#invisibleRootItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::invisibleRootItem() const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget17invisibleRootItemEv',
    )
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(int)
  def topLevelItem(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#topLevelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget12topLevelItemEi', index,
    )
    return self.QTreeWidgetItem._cuteAt(address)

  def topLevelItemCount(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::topLevelItemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#topLevelItemCount
    """
    #  int QTreeWidget::topLevelItemCount() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget17topLevelItemCountEv')

  @overload(QTreeWidgetItem)
  def indexOfTopLevelItem(self, item: QTreeWidgetItem) -> int:
    """
    Calls Qt's 'int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#indexOfTopLevelItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK11QTreeWidget19indexOfTopLevelItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  def headerItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::headerItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#headerItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::headerItem() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget10headerItemEv')
    return self.QTreeWidgetItem._cuteAt(address)

  def currentItem(self) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#currentItem

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::currentItem() const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget11currentItemEv')
    return self.QTreeWidgetItem._cuteAt(address)

  def currentColumn(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::currentColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#currentColumn
    """
    #  int QTreeWidget::currentColumn() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget13currentColumnEv')

  @overload(QPoint)
  def itemAt(self, p: QPoint) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget6itemAtERK6QPoint', self._valueOf(p),
    )
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(int, int)
  def itemAt(self, x: int, y: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK11QTreeWidget6itemAtEii', x, y)
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  def visualItemRect(self, item: QTreeWidgetItem) -> QRect:
    """
    Calls Qt's 'QRect QTreeWidget::visualItemRect(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#visualItemRect

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QTreeWidget::visualItemRect(const QTreeWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget14visualItemRectEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    return QRect._cuteOwning(address)

  def sortColumn(self) -> int:
    """
    Calls Qt's 'int QTreeWidget::sortColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#sortColumn
    """
    #  int QTreeWidget::sortColumn() const
    return self.uglySide.call('ritual_ZNK11QTreeWidget10sortColumnEv')

  @overload(QTreeWidgetItem, int)
  def isPersistentEditorOpen(
      self,
      item: QTreeWidgetItem,
      column: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem
    *item, int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#isPersistentEditorOpen

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem *item, int
    #      column) const
    return self.uglySide.call(
        'ritual_ZNK11QTreeWidget22isPersistentEditorOpenEP15QTreeWidgetItem'
        'i',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  def itemWidget(
      self,
      item: QTreeWidgetItem,
      column: int,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget10itemWidgetEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )
    return QWidget._cuteAt(address)

  @overload(QTreeWidgetItem)
  def itemAbove(self, item: QTreeWidgetItem) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemAbove

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget9itemAboveEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem)
  def itemBelow(self, item: QTreeWidgetItem) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemBelow

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget9itemBelowEPK15QTreeWidgetItem',
        self._addressOf(item),
    )
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem, int)
  def indexFromItem(self, item: QTreeWidgetItem, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem
    *item, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#indexFromItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item,
    #      int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget13indexFromItemEPK15QTreeWidgetItemi',
        self._addressOf(item), column,
    )
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTreeWidget13itemFromIndexERK11QModelIndex',
        self._valueOf(index),
    )
    return self.QTreeWidgetItem._cuteAt(address)

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTreeWidget::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTreeWidget::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK11QTreeWidget20supportedDragActionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTreeWidget::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN11QTreeWidget14setColumnCountEi', columns)

  @overload(QTreeWidgetItem)
  def setHeaderItem(self, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setHeaderItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget13setHeaderItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(str)
  def setHeaderLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QTreeWidget::setHeaderLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setHeaderLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTreeWidget::setHeaderLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setHeaderLabelERK7QString', label,
    )

  @overload(QTreeWidgetItem)
  def setCurrentItem(self, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem, int)
  def setCurrentItem(self, item: QTreeWidgetItem, column: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int, QItemSelectionModel.SelectionFlags)
  def setCurrentItem(
      self,
      item: QTreeWidgetItem,
      column: int,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int
    column, QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setCurrentItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi6QFlagsI'
        'N19QItemSelectionModel13SelectionFlagEE',
        self._addressOf(item), column, command.value,
    )

  @overload(QTreeWidgetItem, int, QWidget)
  def setItemWidget(
      self,
      item: QTreeWidgetItem,
      column: int,
      widget: QWidget,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int
    column, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setItemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.

    widget : QWidget
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int column,
    #      QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget13setItemWidgetEP15QTreeWidgetItemiP7QWidget',
        self._addressOf(item), column, self._addressOf(widget),
    )

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeWidget::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionModel',
        self._addressOf(selectionModel),
    )

  @overload(Qt.DropActions)
  def setSupportedDragActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QTreeWidget::setSupportedDragActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#setSupportedDragActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QTreeWidget::setSupportedDragActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget23setSupportedDragActionsE6QFlagsIN2Qt10Drop'
        'ActionEE',
        actions.value,
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
    Notes what was given, for Qt's 'QTreeWidget::QTreeWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#QTreeWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTreeWidget::QTreeWidget(QWidget *parent)
    self._noteCreation(QTreeWidget, lambda: Rituals.call(
        'ritual_ZN11QTreeWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(int, QTreeWidgetItem)
  def insertTopLevelItem(self, index: int, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::insertTopLevelItem(int index,
    QTreeWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#insertTopLevelItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::insertTopLevelItem(int index, QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget18insertTopLevelItemEiP15QTreeWidgetItem',
        index, self._addressOf(item),
    )

  @overload(QTreeWidgetItem)
  def addTopLevelItem(self, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#addTopLevelItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget15addTopLevelItemEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeTopLevelItem(self, index: int) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#takeTopLevelItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)
    address = self.uglySide.call(
        'ritual_ZN11QTreeWidget16takeTopLevelItemEi', index,
    )
    return self.QTreeWidgetItem._cuteAt(address)

  @overload(int, Qt.SortOrder)
  def sortItems(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeWidget::sortItems(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#sortItems

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeWidget::sortItems(int column, Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget9sortItemsEiN2Qt9SortOrderE',
        column, order.value,
    )

  @overload(QTreeWidgetItem, int)
  def editItem(self, item: QTreeWidgetItem, column: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::editItem(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#editItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::editItem(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget8editItemEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  def openPersistentEditor(self, item: QTreeWidgetItem, column: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item,
    int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#openPersistentEditor

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item, int
    #      column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget20openPersistentEditorEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  def closePersistentEditor(
      self,
      item: QTreeWidgetItem,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::closePersistentEditor(QTreeWidgetItem
    *item, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreewidget.html#closePersistentEditor

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::closePersistentEditor(QTreeWidgetItem *item, int
    #      column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget21closePersistentEditorEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, int)
  def removeItemWidget(self, item: QTreeWidgetItem, column: int) -> None:
    """
    Calls Qt's 'void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#removeItemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    column : int
      Passed on as it is.
    """
    #  void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int column)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget16removeItemWidgetEP15QTreeWidgetItemi',
        self._addressOf(item), column,
    )

  @overload(QTreeWidgetItem, QAbstractItemView.ScrollHint)
  def scrollToItem(
      self,
      item: QTreeWidgetItem,
      hint: QAbstractItemView.ScrollHint,
  ) -> None:
    """
    Calls Qt's 'void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
    QAbstractItemView::ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#scrollToItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number.
    """
    #  void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
    #      QAbstractItemView::ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget12scrollToItemEPK15QTreeWidgetItemN17QAbstra'
        'ctItemView10ScrollHintE',
        self._addressOf(item), hint.value,
    )

  @overload(QTreeWidgetItem)
  def expandItem(self, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::expandItem(const QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#expandItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::expandItem(const QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget10expandItemEPK15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QTreeWidgetItem)
  def collapseItem(self, item: QTreeWidgetItem) -> None:
    """
    Calls Qt's 'void QTreeWidget::collapseItem(const QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#collapseItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QTreeWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QTreeWidget::collapseItem(const QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTreeWidget12collapseItemEPK15QTreeWidgetItem',
        self._addressOf(item),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QTreeWidget::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreewidget.html#clear
    """
    #  void QTreeWidget::clear()
    self.uglySide.call('ritual_ZN11QTreeWidget5clearEv')
