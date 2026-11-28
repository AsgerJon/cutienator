"""
QTreeModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTreeModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QList, QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex, QTimerEvent
  from ..QtCore import QVariant
  from . import QTreeModelPrivate, QTreeWidget, QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QTimerEvent = WAIT['QTimerEvent']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTreeModel(QAbstractItemModel):
  """
  The cute side of Qt's QTreeModel: a plain Python object standing in front
  of one C++ QTreeModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QTreeModel is built
  on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTreeModel that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'view', 'clear',
  'setColumnCount', 'item', 'itemChanged', 'index', 'parent', 'rowCount',
  'columnCount', 'hasChildren', 'data', 'setData', 'clearItemData',
  'itemData', 'headerData', 'setHeaderData', 'flags', 'sort', 'ensureSorted',
  'insertRows', 'insertColumns', 'removeRows', 'mimeTypes', 'mimeData',
  'dropMimeData', 'supportedDropActions', 'supportedDragActions',
  'internalMimeData', 'createIndexFromItem', 'beginInsertItems',
  'endInsertItems', 'beginRemoveItems', 'endRemoveItems', 'timerEvent',
  'executePendingSort', 'isChanging', 'd_func'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTreeModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTreeModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTreeModel::~QTreeModel()': the destructor: Python never removes a
    C++ QTreeModel.
  - Qt's 'bool QTreeModel::itemLessThan(const std::pair<QTreeWidgetItem *,
    int> &left, const std::pair<QTreeWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QTreeModel::itemGreaterThan(const std::pair<QTreeWidgetItem *,
    int> &left, const std::pair<QTreeWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<QTreeWidgetItem *>::iterator
    QTreeModel::sortedInsertionIterator(const QList<QTreeWidgetItem
    *>::iterator &begin, const QList<QTreeWidgetItem *>::iterator &end,
    Qt::SortOrder order, QTreeWidgetItem *item)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QTreeModel::emitDataChanged(QTreeWidgetItem *item, int column,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QTreeModel::sortItems(QList<QTreeWidgetItem *> *items, int
    column, Qt::SortOrder order)': names 'QList<QTreeWidgetItem *>', which
    has no cute class yet.
  - Qt's 'const QTreeModelPrivate *QTreeModel::d_func() const': takes in
    Python what 'QTreeModelPrivate *QTreeModel::d_func()' takes.

  What has no ritual
  ------------------

  5 of the 53 functions Qt declares: 3 leans on 'QTreeModel; 2 not a gap.

  What to expect
  --------------

  - The C++ QTreeModel is created at the first use, not by 'QTreeModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTreeModel.
  - Qt tells when it has removed the C++ QTreeModel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QTreeModel that has no cute function yet, '__init__',
    'emitDataChanged', 'itemGreaterThan', 'itemLessThan', 'sortItems',
    'sortedInsertionIterator', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QTreeModel, each a class in here as in C++.

  class SkipSorting(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTreeModel::SkipSorting: a plain Python object
    standing in front of one C++ QTreeModel::SkipSorting.

    C++ hands a QTreeModel::SkipSorting around as a copy, so every C++
    QTreeModel::SkipSorting behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QTreeModel::SkipSorting yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTreeModel::SkipSorting::~SkipSorting()': the destructor: Python
      removes its C++ QTreeModel::SkipSorting by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QTreeModel::SkipSorting is created at the first use, not by
      'QTreeModel::SkipSorting(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTreeModel::SkipSorting back gives a copy the
      ritual made for Python, in a new cute QTreeModel::SkipSorting.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTreeModel = WAIT['QTreeModel']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTreeModel::SkipSorting'

    #  Qt's '~QTreeModel::SkipSorting()'. Naming it makes this a value class:
    #  Python owns every C++ QTreeModel::SkipSorting behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QTreeModel11SkipSortingD1Ev'

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

    @overload(QTreeModel)
    @overload(NoneType)
    def __init__(self, m: Optional[QTreeModel]) -> None:
      """
      Notes what was given, for Qt's
      'QTreeModel::SkipSorting::SkipSorting(const QTreeModel *m)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qtreemodel-skipsorting.html#SkipSorting

      Parameters
      ----------

      m : Optional[QTreeModel]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QTreeModel::SkipSorting::SkipSorting(const QTreeModel *m)
      self._noteCreation(QTreeModel.SkipSorting, lambda: Rituals.call(
          'ritual_ZN10QTreeModel11SkipSortingC1EPKS_', self._addressOf(m),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTreeModel'

  #  A C++ QTreeModel Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTreeModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTreeModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTreeModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QTreeModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QTreeWidget]:
    """
    Calls Qt's 'QTreeWidget *QTreeModel::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#view

    Returns
    -------

    Optional[QTreeWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidget *QTreeModel::view() const
    address = self.uglySide.call('ritual_ZNK10QTreeModel4viewEv')
    from . import QTreeWidget
    return QTreeWidget._cuteAt(address)

  @overload(QModelIndex)
  def item(self, index: QModelIndex) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem *QTreeModel::item(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#item

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
    #  QTreeWidgetItem *QTreeModel::item(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel4itemERK11QModelIndex', self._valueOf(index),
    )
    from . import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

  @overload(QTreeWidgetItem, int)
  @overload(NoneType, int)
  def index(
      self,
      item: Optional[QTreeWidgetItem],
      column: int,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeModel::index(const QTreeWidgetItem *item,
    int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#index

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeModel::index(const QTreeWidgetItem *item, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel5indexEPK15QTreeWidgetItemi',
        self._addressOf(item), column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int, QModelIndex)
  def index(self, row: int, column: int, parent: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeModel::index(int row, int column, const QModelIndex
    #      &parent) const
    ritual = 'ritual_ZNK10QTreeModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeModel::parent(const QModelIndex &child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#parent

    Parameters
    ----------

    child : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeModel::parent(const QModelIndex &child) const
    ritual = 'ritual_ZNK10QTreeModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QTreeModel::rowCount(const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QTreeModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK10QTreeModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QTreeModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QTreeModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK10QTreeModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel11columnCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  def hasChildren(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeModel::hasChildren(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#hasChildren

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeModel::hasChildren(const QModelIndex &parent) const
    ritual = 'ritual_ZNK10QTreeModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel11hasChildrenERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QTreeModel::data(const QModelIndex &index, int role)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTreeModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK10QTreeModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def itemData(self, index: QModelIndex) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QTreeModel::itemData(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#itemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QMap[int, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QMap<int, QVariant> QTreeModel::itemData(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel8itemDataERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QTreeModel::headerData(int section, Qt::Orientation
    orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTreeModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = 'ritual_ZNK10QTreeModel10headerDataEiN2Qt11OrientationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel10headerDataEiN2Qt11OrientationEi'
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QTreeModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QTreeModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK10QTreeModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTreeModel::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTreeModel::mimeTypes() const
    address = self.uglySide.call('ritual_ZNK10QTreeModel9mimeTypesEv')
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QTreeModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#mimeData

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QTreeModel::mimeData(const QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTreeModel::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreemodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTreeModel::supportedDropActions() const
    ritual = 'ritual_ZNK10QTreeModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTreeModel::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreemodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTreeModel::supportedDragActions() const
    ritual = 'ritual_ZNK10QTreeModel20supportedDragActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QTreeModel20supportedDragActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def internalMimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QTreeModel::internalMimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#internalMimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QTreeModel::internalMimeData() const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel16internalMimeDataEv',
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  @overload(int, int, QTreeWidgetItem)
  @overload(int, int, NoneType)
  def createIndexFromItem(
      self,
      row: int,
      col: int,
      item: Optional[QTreeWidgetItem],
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTreeModel::createIndexFromItem(int row, int col,
    QTreeWidgetItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtreemodel.html#createIndexFromItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    col : int
      Passed on as it is.

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTreeModel::createIndexFromItem(int row, int col,
    #      QTreeWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK10QTreeModel19createIndexFromItemEiiP15QTreeWidgetItem',
        row, col, self._addressOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def executePendingSort(self) -> bool:
    """
    Calls Qt's 'bool QTreeModel::executePendingSort() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#executePendingSort
    """
    #  bool QTreeModel::executePendingSort() const
    return self.uglySide.call('ritual_ZNK10QTreeModel18executePendingSortEv')

  def isChanging(self) -> bool:
    """
    Calls Qt's 'bool QTreeModel::isChanging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#isChanging
    """
    #  bool QTreeModel::isChanging() const
    return self.uglySide.call('ritual_ZNK10QTreeModel10isChangingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QTreeModel::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTreeModel::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN10QTreeModel14setColumnCountEi', columns)

  @overload(QModelIndex, QVariant, int)
  def setData(self, index: QModelIndex, value: QVariant, role: int) -> bool:
    """
    Calls Qt's 'bool QTreeModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is.
    """
    #  bool QTreeModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN10QTreeModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QTreeModel7setDataERK11QModelIndexRK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      value: QVariant,
      role: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeModel::setHeaderData(int section, Qt::Orientation
    orientation, const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#setHeaderData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is.
    """
    #  bool QTreeModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN10QTreeModel13setHeaderDataEiN2Qt11OrientationERK8QVarian'
        'ti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QTreeModel13setHeaderDataEiN2Qt11OrientationERK8Q'
          'Varianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
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
    - Qt's 'QTreeModel::QTreeModel(int columns, QTreeWidget *parent)': leans
      on 'QTreeModel::qt_metacall(QMetaObject::Call, int, void**)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'QTreeModel::QTreeModel(QTreeModelPrivate &a0, QTreeWidget
      *parent)': leans on 'QTreeModel::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTreeModel.__init__' has no cute function yet. Qt's "
        "'QTreeModel::QTreeModel(int columns, QTreeWidget *parent)': leans "
        "on 'QTreeModel::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's "
        "'QTreeModel::QTreeModel(QTreeModelPrivate &a0, QTreeWidget "
        "*parent)': leans on 'QTreeModel::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QTreeModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#clear
    """
    #  void QTreeModel::clear()
    self.uglySide.call('ritual_ZN10QTreeModel5clearEv')

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def itemChanged(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Calls Qt's 'void QTreeModel::itemChanged(QTreeWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#itemChanged

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeModel::itemChanged(QTreeWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN10QTreeModel11itemChangedEP15QTreeWidgetItem',
        self._addressOf(item),
    )

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeModel::clearItemData(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeModel::clearItemData(const QModelIndex &index)
    ritual = 'ritual_ZN10QTreeModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel13clearItemDataERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(int, Qt.SortOrder)
  def sort(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTreeModel::sort(int column, Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTreeModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN10QTreeModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(int, Qt.SortOrder, int, int, QModelIndex)
  def ensureSorted(
      self,
      column: int,
      order: Qt.SortOrder,
      start: int,
      end: int,
      parent: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QTreeModel::ensureSorted(int column, Qt::SortOrder
    order, int start, int end, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#ensureSorted

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QTreeModel::ensureSorted(int column, Qt::SortOrder order, int
    #      start, int end, const QModelIndex &parent)
    self.uglySide.call(
        'ritual_ZN10QTreeModel12ensureSortedEiN2Qt9SortOrderEiiRK11QModelIn'
        'dex',
        column, order.value, start, end, self._valueOf(parent),
    )

  @overload(int, int, QModelIndex)
  def insertRows(self, row: int, count: int, a2: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeModel::insertRows(int row, int count, const
    QModelIndex &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    a2 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeModel::insertRows(int row, int count, const QModelIndex &a2)
    ritual = 'ritual_ZN10QTreeModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel10insertRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(a2))

  @overload(int, int, QModelIndex)
  def insertColumns(self, column: int, count: int, a2: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTreeModel::insertColumns(int column, int count, const
    QModelIndex &a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    a2 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeModel::insertColumns(int column, int count, const
    #      QModelIndex &a2)
    ritual = 'ritual_ZN10QTreeModel13insertColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel13insertColumnsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, column, count, self._valueOf(a2))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTreeModel::removeRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN10QTreeModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel10removeRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(QMimeData, Qt.DropAction, int, int, QModelIndex)
  @overload(NoneType, Qt.DropAction, int, int, QModelIndex)
  def dropMimeData(
      self,
      data: Optional[QMimeData],
      action: Qt.DropAction,
      row: int,
      column: int,
      parent: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QTreeModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#dropMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Qt.DropAction
      Passed on as its number.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTreeModel::dropMimeData(const QMimeData *data, Qt::DropAction
    #      action, int row, int column, const QModelIndex &parent)
    ritual = (
        'ritual_ZN10QTreeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEi'
        'iRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QTreeModel12dropMimeDataEPK9QMimeDataN2Qt10DropAc'
          'tionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @overload(QTreeWidgetItem, int, int)
  @overload(NoneType, int, int)
  def beginInsertItems(
      self,
      parent: Optional[QTreeWidgetItem],
      row: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeModel::beginInsertItems(QTreeWidgetItem *parent,
    int row, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#beginInsertItems

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QTreeModel::beginInsertItems(QTreeWidgetItem *parent, int row,
    #      int count)
    self.uglySide.call(
        'ritual_ZN10QTreeModel16beginInsertItemsEP15QTreeWidgetItemii',
        self._addressOf(parent), row, count,
    )

  def endInsertItems(self) -> None:
    """
    Calls Qt's 'void QTreeModel::endInsertItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#endInsertItems
    """
    #  void QTreeModel::endInsertItems()
    self.uglySide.call('ritual_ZN10QTreeModel14endInsertItemsEv')

  @overload(QTreeWidgetItem, int, int)
  @overload(NoneType, int, int)
  def beginRemoveItems(
      self,
      parent: Optional[QTreeWidgetItem],
      row: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void QTreeModel::beginRemoveItems(QTreeWidgetItem *parent,
    int row, int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#beginRemoveItems

    Parameters
    ----------

    parent : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QTreeModel::beginRemoveItems(QTreeWidgetItem *parent, int row,
    #      int count)
    self.uglySide.call(
        'ritual_ZN10QTreeModel16beginRemoveItemsEP15QTreeWidgetItemii',
        self._addressOf(parent), row, count,
    )

  def endRemoveItems(self) -> None:
    """
    Calls Qt's 'void QTreeModel::endRemoveItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#endRemoveItems
    """
    #  void QTreeModel::endRemoveItems()
    self.uglySide.call('ritual_ZN10QTreeModel14endRemoveItemsEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QTreeModel::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTreeModel::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN10QTreeModel10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QTreeModel10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def d_func(self) -> Optional[QTreeModelPrivate]:
    """
    Calls Qt's 'QTreeModelPrivate *QTreeModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtreemodel.html#d_func

    Returns
    -------

    Optional[QTreeModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeModelPrivate *QTreeModel::d_func()
    address = self.uglySide.call('ritual_ZN10QTreeModel6d_funcEv')
    from . import QTreeModelPrivate
    return QTreeModelPrivate._cuteAt(address)

  @staticmethod
  def emitDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QTreeModel::emitDataChanged(QTreeWidgetItem *item, int column,
    const QList<int> &roles)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QTreeModel.emitDataChanged' has no cute function yet. Qt's 'void "
        "QTreeModel::emitDataChanged(QTreeWidgetItem *item, int column, "
        "const QList<int> &roles)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def itemGreaterThan(*__, **_) -> Never:
    """
    Qt's 'bool QTreeModel::itemGreaterThan(const std::pair<QTreeWidgetItem *,
    int> &left, const std::pair<QTreeWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTreeModel.itemGreaterThan' has no cute function yet. Qt's 'bool "
        "QTreeModel::itemGreaterThan(const std::pair<QTreeWidgetItem *, "
        "int> &left, const std::pair<QTreeWidgetItem *, int> &right)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def itemLessThan(*__, **_) -> Never:
    """
    Qt's 'bool QTreeModel::itemLessThan(const std::pair<QTreeWidgetItem *,
    int> &left, const std::pair<QTreeWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTreeModel.itemLessThan' has no cute function yet. Qt's 'bool "
        "QTreeModel::itemLessThan(const std::pair<QTreeWidgetItem *, int> "
        "&left, const std::pair<QTreeWidgetItem *, int> &right)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def sortItems(*__, **_) -> Never:
    """
    Qt's 'void QTreeModel::sortItems(QList<QTreeWidgetItem *> *items, int
    column, Qt::SortOrder order)': names 'QList<QTreeWidgetItem *>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QTreeModel.sortItems' has no cute function yet. Qt's 'void "
        "QTreeModel::sortItems(QList<QTreeWidgetItem *> *items, int column, "
        "Qt::SortOrder order)': names 'QList<QTreeWidgetItem *>', which has "
        "no cute class yet.")

  @staticmethod
  def sortedInsertionIterator(*__, **_) -> Never:
    """
    Qt's 'QList<QTreeWidgetItem *>::iterator
    QTreeModel::sortedInsertionIterator(const QList<QTreeWidgetItem
    *>::iterator &begin, const QList<QTreeWidgetItem *>::iterator &end,
    Qt::SortOrder order, QTreeWidgetItem *item)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QTreeModel.sortedInsertionIterator' has no cute function yet. "
        "Qt's 'QList<QTreeWidgetItem *>::iterator "
        "QTreeModel::sortedInsertionIterator(const QList<QTreeWidgetItem "
        "*>::iterator &begin, const QList<QTreeWidgetItem *>::iterator "
        "&end, Qt::SortOrder order, QTreeWidgetItem *item)': takes a type "
        "Python has no way to hand over yet.")
