"""
QListWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlistwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ._q_abstract_item_view import QAbstractItemView
from ..QtCore import QItemSelectionModel
from ._q_list_view import QListView
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


class QListWidget(QListView):
  """
  The cute side of Qt's QListWidget: a plain Python object standing in front
  of one C++ QListWidget.

  It is built on the cute 'QListView', as Qt's QListWidget is built on Qt's
  QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QListWidget that has a ritual and that Python can
  call so far, 31 names in all: 'metaObject', 'tr', 'setSelectionModel',
  'item', 'row', 'insertItem', 'addItem', 'takeItem', 'count', 'currentItem',
  'setCurrentItem', 'currentRow', 'setCurrentRow', 'itemAt',
  'visualItemRect', 'sortItems', 'setSortingEnabled', 'isSortingEnabled',
  'editItem', 'openPersistentEditor', 'closePersistentEditor',
  'isPersistentEditorOpen', 'itemWidget', 'setItemWidget',
  'removeItemWidget', 'indexFromItem', 'itemFromIndex',
  'setSupportedDragActions', 'supportedDragActions', 'scrollToItem', 'clear'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QListWidget::~QListWidget()': the destructor: Python never removes
    a C++ QListWidget.

  What has no ritual
  ------------------

  31 of the 69 functions Qt declares: 10 a signal; 7 takes or gives a type
  that cannot be passed yet; 6 protected; 5 private; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QListWidget is created at the first use, not by
    'QListWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QListWidget.
  - Qt tells when it has removed the C++ QListWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QListWidgetItem = WAIT['QListWidgetItem']

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
    Calls Qt's 'QString QListWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#tr

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
    #  QString QListWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QListWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QListWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QListWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QListWidget10metaObjectEv')
    return QMetaObject._cuteAt(address)

  @overload(int)
  def item(self, row: int) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::item(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#item

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::item(int row) const
    address = self.uglySide.call('ritual_ZNK11QListWidget4itemEi', row)
    return self.QListWidgetItem._cuteAt(address)

  @overload(QListWidgetItem)
  def row(self, item: QListWidgetItem) -> int:
    """
    Calls Qt's 'int QListWidget::row(const QListWidgetItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#row

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  int QListWidget::row(const QListWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK11QListWidget3rowEPK15QListWidgetItem',
        self._addressOf(item),
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QListWidget::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#count
    """
    #  int QListWidget::count() const
    return self.uglySide.call('ritual_ZNK11QListWidget5countEv')

  def currentItem(self) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#currentItem

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::currentItem() const
    address = self.uglySide.call('ritual_ZNK11QListWidget11currentItemEv')
    return self.QListWidgetItem._cuteAt(address)

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QListWidget::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#currentRow
    """
    #  int QListWidget::currentRow() const
    return self.uglySide.call('ritual_ZNK11QListWidget10currentRowEv')

  @overload(QPoint)
  def itemAt(self, p: QPoint) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::itemAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#itemAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::itemAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK11QListWidget6itemAtERK6QPoint', self._valueOf(p),
    )
    return self.QListWidgetItem._cuteAt(address)

  @overload(int, int)
  def itemAt(self, x: int, y: int) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::itemAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#itemAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::itemAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK11QListWidget6itemAtEii', x, y)
    return self.QListWidgetItem._cuteAt(address)

  @overload(QListWidgetItem)
  def visualItemRect(self, item: QListWidgetItem) -> QRect:
    """
    Calls Qt's 'QRect QListWidget::visualItemRect(const QListWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#visualItemRect

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListWidget::visualItemRect(const QListWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK11QListWidget14visualItemRectEPK15QListWidgetItem',
        self._addressOf(item),
    )
    return QRect._cuteOwning(address)

  def isSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QListWidget::isSortingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#isSortingEnabled
    """
    #  bool QListWidget::isSortingEnabled() const
    return self.uglySide.call('ritual_ZNK11QListWidget16isSortingEnabledEv')

  @overload(QListWidgetItem)
  def isPersistentEditorOpen(self, item: QListWidgetItem) -> bool:
    """
    Calls Qt's 'bool QListWidget::isPersistentEditorOpen(QListWidgetItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidget.html#isPersistentEditorOpen

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  bool QListWidget::isPersistentEditorOpen(QListWidgetItem *item) const
    return self.uglySide.call(
        'ritual_ZNK11QListWidget22isPersistentEditorOpenEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem)
  def itemWidget(self, item: QListWidgetItem) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QListWidget::itemWidget(QListWidgetItem *item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#itemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QListWidget::itemWidget(QListWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK11QListWidget10itemWidgetEP15QListWidgetItem',
        self._addressOf(item),
    )
    return QWidget._cuteAt(address)

  @overload(QListWidgetItem)
  def indexFromItem(self, item: QListWidgetItem) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListWidget::indexFromItem(const QListWidgetItem
    *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#indexFromItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListWidget::indexFromItem(const QListWidgetItem *item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QListWidget13indexFromItemEPK15QListWidgetItem',
        self._addressOf(item),
    )
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::itemFromIndex(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::itemFromIndex(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QListWidget13itemFromIndexERK11QModelIndex',
        self._valueOf(index),
    )
    return self.QListWidgetItem._cuteAt(address)

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QListWidget::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidget.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QListWidget::supportedDragActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK11QListWidget20supportedDragActionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QListWidget::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListWidget::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    self.uglySide.call(
        'ritual_ZN11QListWidget17setSelectionModelEP19QItemSelectionModel',
        self._addressOf(selectionModel),
    )

  @overload(QListWidgetItem)
  def setCurrentItem(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::setCurrentItem(QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setCurrentItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::setCurrentItem(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem, QItemSelectionModel.SelectionFlags)
  def setCurrentItem(
      self,
      item: QListWidgetItem,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QListWidget::setCurrentItem(QListWidgetItem *item,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setCurrentItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QListWidget::setCurrentItem(QListWidgetItem *item,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem6QFlagsIN'
        '19QItemSelectionModel13SelectionFlagEE',
        self._addressOf(item), command.value,
    )

  @overload(int)
  def setCurrentRow(self, row: int) -> None:
    """
    Calls Qt's 'void QListWidget::setCurrentRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setCurrentRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QListWidget::setCurrentRow(int row)
    self.uglySide.call('ritual_ZN11QListWidget13setCurrentRowEi', row)

  @overload(int, QItemSelectionModel.SelectionFlags)
  def setCurrentRow(
      self,
      row: int,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QListWidget::setCurrentRow(int row,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setCurrentRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QListWidget::setCurrentRow(int row,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN11QListWidget13setCurrentRowEi6QFlagsIN19QItemSelectionMo'
        'del13SelectionFlagEE',
        row, command.value,
    )

  @overload(bool)
  def setSortingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QListWidget::setSortingEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setSortingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QListWidget::setSortingEnabled(bool enable)
    self.uglySide.call('ritual_ZN11QListWidget17setSortingEnabledEb', enable)

  @overload(QListWidgetItem, QWidget)
  def setItemWidget(self, item: QListWidgetItem, widget: QWidget) -> None:
    """
    Calls Qt's 'void QListWidget::setItemWidget(QListWidgetItem *item,
    QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#setItemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    widget : QWidget
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::setItemWidget(QListWidgetItem *item, QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN11QListWidget13setItemWidgetEP15QListWidgetItemP7QWidget',
        self._addressOf(item), self._addressOf(widget),
    )

  @overload(Qt.DropActions)
  def setSupportedDragActions(self, actions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QListWidget::setSupportedDragActions(Qt::DropActions
    actions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidget.html#setSupportedDragActions

    Parameters
    ----------

    actions : Qt.DropActions
      Passed on as its number.
    """
    #  void QListWidget::setSupportedDragActions(Qt::DropActions actions)
    self.uglySide.call(
        'ritual_ZN11QListWidget23setSupportedDragActionsE6QFlagsIN2Qt10Drop'
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
    Notes what was given, for Qt's 'QListWidget::QListWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#QListWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QListWidget::QListWidget(QWidget *parent)
    self._noteCreation(QListWidget, lambda: Rituals.call(
        'ritual_ZN11QListWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(int, QListWidgetItem)
  def insertItem(self, row: int, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::insertItem(int row, QListWidgetItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#insertItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::insertItem(int row, QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget10insertItemEiP15QListWidgetItem',
        row, self._addressOf(item),
    )

  @overload(int, str)
  def insertItem(self, row: int, label: str) -> None:
    """
    Calls Qt's 'void QListWidget::insertItem(int row, const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#insertItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidget::insertItem(int row, const QString &label)
    self.uglySide.call(
        'ritual_ZN11QListWidget10insertItemEiRK7QString', row, label,
    )

  @overload(str)
  def addItem(self, label: str) -> None:
    """
    Calls Qt's 'void QListWidget::addItem(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#addItem

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QListWidget::addItem(const QString &label)
    self.uglySide.call('ritual_ZN11QListWidget7addItemERK7QString', label)

  @overload(QListWidgetItem)
  def addItem(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::addItem(QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#addItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::addItem(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget7addItemEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeItem(self, row: int) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListWidget::takeItem(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#takeItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QListWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidgetItem *QListWidget::takeItem(int row)
    address = self.uglySide.call('ritual_ZN11QListWidget8takeItemEi', row)
    return self.QListWidgetItem._cuteAt(address)

  @overload()
  @overload(Qt.SortOrder)
  def sortItems(
      self,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QListWidget::sortItems(Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#sortItems

    Parameters
    ----------

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QListWidget::sortItems(Qt::SortOrder order)
    self.uglySide.call(
        'ritual_ZN11QListWidget9sortItemsEN2Qt9SortOrderE', order.value,
    )

  @overload(QListWidgetItem)
  def editItem(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::editItem(QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#editItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::editItem(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget8editItemEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem)
  def openPersistentEditor(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::openPersistentEditor(QListWidgetItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidget.html#openPersistentEditor

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::openPersistentEditor(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget20openPersistentEditorEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem)
  def closePersistentEditor(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::closePersistentEditor(QListWidgetItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistwidget.html#closePersistentEditor

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::closePersistentEditor(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget21closePersistentEditorEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem)
  def removeItemWidget(self, item: QListWidgetItem) -> None:
    """
    Calls Qt's 'void QListWidget::removeItemWidget(QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#removeItemWidget

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.
    """
    #  void QListWidget::removeItemWidget(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QListWidget16removeItemWidgetEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(QListWidgetItem, QAbstractItemView.ScrollHint)
  def scrollToItem(
      self,
      item: QListWidgetItem,
      hint: QAbstractItemView.ScrollHint,
  ) -> None:
    """
    Calls Qt's 'void QListWidget::scrollToItem(const QListWidgetItem *item,
    QAbstractItemView::ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#scrollToItem

    The signature names a class made later, so the function takes the full
    call only: no argument may be left out, and None is taken nowhere.

    Parameters
    ----------

    item : QListWidgetItem
      Passed on as the address of its C++ object.

    hint : QAbstractItemView.ScrollHint
      Passed on as its number.
    """
    #  void QListWidget::scrollToItem(const QListWidgetItem *item,
    #      QAbstractItemView::ScrollHint hint)
    self.uglySide.call(
        'ritual_ZN11QListWidget12scrollToItemEPK15QListWidgetItemN17QAbstra'
        'ctItemView10ScrollHintE',
        self._addressOf(item), hint.value,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QListWidget::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistwidget.html#clear
    """
    #  void QListWidget::clear()
    self.uglySide.call('ritual_ZN11QListWidget5clearEv')
