"""
QListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QListModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QAbstractListModel, QList, QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex, QVariant
  from . import QListWidget, QListWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QListWidgetItem = WAIT['QListWidgetItem']
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QListModel(QAbstractListModel):
  """
  The cute side of Qt's QListModel: a plain Python object standing in front
  of one C++ QListModel.

  It is built on the cute 'QAbstractListModel', as Qt's QListModel is built
  on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QListModel that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'view', 'clear', 'at',
  'insert', 'remove', 'take', 'move', 'rowCount', 'index', 'data', 'setData',
  'clearItemData', 'itemData', 'insertRows', 'removeRows', 'moveRows',
  'flags', 'sort', 'ensureSorted', 'mimeTypes', 'mimeData', 'dropMimeData',
  'supportedDropActions', 'supportedDragActions', 'internalMimeData'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QListModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QListModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QListModel::~QListModel()': the destructor: Python never removes a
    C++ QListModel.
  - Qt's 'bool QListModel::itemLessThan(const std::pair<QListWidgetItem *,
    int> &left, const std::pair<QListWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QListModel::itemGreaterThan(const std::pair<QListWidgetItem *,
    int> &left, const std::pair<QListWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QList<QListWidgetItem *>::iterator
    QListModel::sortedInsertionIterator(const QList<QListWidgetItem
    *>::iterator &begin, const QList<QListWidgetItem *>::iterator &end,
    Qt::SortOrder order, QListWidgetItem *item)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QListModel::itemChanged(QListWidgetItem *item, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 39 functions Qt declares: 2 not a gap; 2 leans on 'QListModel.

  What to expect
  --------------

  - The C++ QListModel is created at the first use, not by 'QListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QListModel.
  - Qt tells when it has removed the C++ QListModel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QListModel that has no cute function yet, '__init__',
    'itemChanged', 'itemGreaterThan', 'itemLessThan',
    'sortedInsertionIterator', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListModel'

  #  A C++ QListModel Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QListModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QListModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QListModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QListModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QListWidget]:
    """
    Calls Qt's 'QListWidget *QListModel::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#view

    Returns
    -------

    Optional[QListWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QListWidget *QListModel::view() const
    address = self.uglySide.call('ritual_ZNK10QListModel4viewEv')
    from . import QListWidget
    return QListWidget._cuteAt(address)

  @overload(int)
  def at(self, row: int) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListModel::at(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#at

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
    #  QListWidgetItem *QListModel::at(int row) const
    address = self.uglySide.call('ritual_ZNK10QListModel2atEi', row)
    from . import QListWidgetItem
    return QListWidgetItem._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QListModel::rowCount(const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QListModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK10QListModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QListWidgetItem)
  @overload(NoneType)
  def index(self, item: Optional[QListWidgetItem]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListModel::index(const QListWidgetItem *item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#index

    Parameters
    ----------

    item : Optional[QListWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListModel::index(const QListWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK10QListModel5indexEPK15QListWidgetItem',
        self._addressOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int = 0,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QListModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QListModel::index(int row, int column, const QModelIndex
    #      &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK10QListModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QListModel::data(const QModelIndex &index, int role)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#data

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
    #  QVariant QListModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK10QListModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def itemData(self, index: QModelIndex) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QListModel::itemData(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#itemData

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
    #  QMap<int, QVariant> QListModel::itemData(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10QListModel8itemDataERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QVariant
    return QMap[int, QVariant]._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QListModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#flags

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
    #  Qt::ItemFlags QListModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK10QListModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QListModel::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QListModel::mimeTypes() const
    address = self.uglySide.call('ritual_ZNK10QListModel9mimeTypesEv')
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QListModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#mimeData

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
    #  QMimeData *QListModel::mimeData(const QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK10QListModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QListModel::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QListModel::supportedDropActions() const
    ritual = 'ritual_ZNK10QListModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QListModel::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlistmodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QListModel::supportedDragActions() const
    ritual = 'ritual_ZNK10QListModel20supportedDragActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QListModel20supportedDragActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def internalMimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QListModel::internalMimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#internalMimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QListModel::internalMimeData() const
    address = self.uglySide.call(
        'ritual_ZNK10QListModel16internalMimeDataEv',
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant, int)
  def setData(self, index: QModelIndex, value: QVariant, role: int) -> bool:
    """
    Calls Qt's 'bool QListModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#setData

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
    #  bool QListModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN10QListModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QListModel7setDataERK11QModelIndexRK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
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
    Qt's 'QListModel::QListModel(QListWidget *parent)': leans on
    'QListModel::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QListModel.__init__' has no cute function yet. Qt's "
        "'QListModel::QListModel(QListWidget *parent)': leans on "
        "'QListModel::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QListModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#clear
    """
    #  void QListModel::clear()
    self.uglySide.call('ritual_ZN10QListModel5clearEv')

  @overload(int, QListWidgetItem)
  @overload(int, NoneType)
  def insert(self, row: int, item: Optional[QListWidgetItem]) -> None:
    """
    Calls Qt's 'void QListModel::insert(int row, QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#insert

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QListWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListModel::insert(int row, QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN10QListModel6insertEiP15QListWidgetItem',
        row, self._addressOf(item),
    )

  @overload(int, QStringList)
  def insert(self, row: int, items: QStringList) -> None:
    """
    Calls Qt's 'void QListModel::insert(int row, const QStringList &items)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#insert

    Parameters
    ----------

    row : int
      Passed on as it is.

    items : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QListModel::insert(int row, const QStringList &items)
    self.uglySide.call(
        'ritual_ZN10QListModel6insertEiRK5QListI7QStringE',
        row, self._valueOf(items),
    )

  @overload(QListWidgetItem)
  @overload(NoneType)
  def remove(self, item: Optional[QListWidgetItem]) -> None:
    """
    Calls Qt's 'void QListModel::remove(QListWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#remove

    Parameters
    ----------

    item : Optional[QListWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QListModel::remove(QListWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN10QListModel6removeEP15QListWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def take(self, row: int) -> Optional[QListWidgetItem]:
    """
    Calls Qt's 'QListWidgetItem *QListModel::take(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#take

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
    #  QListWidgetItem *QListModel::take(int row)
    address = self.uglySide.call('ritual_ZN10QListModel4takeEi', row)
    from . import QListWidgetItem
    return QListWidgetItem._cuteAt(address)

  @overload(int, int)
  def move(self, srcRow: int, dstRow: int) -> None:
    """
    Calls Qt's 'void QListModel::move(int srcRow, int dstRow)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#move

    Parameters
    ----------

    srcRow : int
      Passed on as it is.

    dstRow : int
      Passed on as it is.
    """
    #  void QListModel::move(int srcRow, int dstRow)
    self.uglySide.call('ritual_ZN10QListModel4moveEii', srcRow, dstRow)

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QListModel::clearItemData(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QListModel::clearItemData(const QModelIndex &index)
    ritual = 'ritual_ZN10QListModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QListModel13clearItemDataERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int = 1,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QListModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#insertRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QListModel::insertRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN10QListModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QListModel10insertRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int = 1,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QListModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QListModel::removeRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN10QListModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QListModel10removeRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(QModelIndex, int, int, QModelIndex, int)
  def moveRows(
      self,
      sourceParent: QModelIndex,
      sourceRow: int,
      count: int,
      destinationParent: QModelIndex,
      destinationChild: int,
  ) -> bool:
    """
    Calls Qt's 'bool QListModel::moveRows(const QModelIndex &sourceParent,
    int sourceRow, int count, const QModelIndex &destinationParent, int
    destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#moveRows

    Parameters
    ----------

    sourceParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceRow : int
      Passed on as it is.

    count : int
      Passed on as it is.

    destinationParent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationChild : int
      Passed on as it is.
    """
    #  bool QListModel::moveRows(const QModelIndex &sourceParent, int
    #      sourceRow, int count, const QModelIndex &destinationParent, int
    #      destinationChild)
    ritual = 'ritual_ZN10QListModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QListModel8moveRowsERK11QModelIndexiiS2_i'
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int, Qt.SortOrder)
  def sort(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QListModel::sort(int column, Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QListModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN10QListModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QListModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(int, Qt.SortOrder, int, int)
  def ensureSorted(
      self,
      column: int,
      order: Qt.SortOrder,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QListModel::ensureSorted(int column, Qt::SortOrder
    order, int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#ensureSorted

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
    """
    #  void QListModel::ensureSorted(int column, Qt::SortOrder order, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN10QListModel12ensureSortedEiN2Qt9SortOrderEii',
        column, order.value, start, end,
    )

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
    Calls Qt's 'bool QListModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistmodel.html#dropMimeData

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
    #  bool QListModel::dropMimeData(const QMimeData *data, Qt::DropAction
    #      action, int row, int column, const QModelIndex &parent)
    ritual = (
        'ritual_ZN10QListModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEi'
        'iRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QListModel12dropMimeDataEPK9QMimeDataN2Qt10DropAc'
          'tionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )

  @staticmethod
  def itemChanged(*__, **_) -> Never:
    """
    Qt's 'void QListModel::itemChanged(QListWidgetItem *item, const
    QList<int> &roles)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QListModel.itemChanged' has no cute function yet. Qt's 'void "
        "QListModel::itemChanged(QListWidgetItem *item, const QList<int> "
        "&roles)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def itemGreaterThan(*__, **_) -> Never:
    """
    Qt's 'bool QListModel::itemGreaterThan(const std::pair<QListWidgetItem *,
    int> &left, const std::pair<QListWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QListModel.itemGreaterThan' has no cute function yet. Qt's 'bool "
        "QListModel::itemGreaterThan(const std::pair<QListWidgetItem *, "
        "int> &left, const std::pair<QListWidgetItem *, int> &right)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def itemLessThan(*__, **_) -> Never:
    """
    Qt's 'bool QListModel::itemLessThan(const std::pair<QListWidgetItem *,
    int> &left, const std::pair<QListWidgetItem *, int> &right)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QListModel.itemLessThan' has no cute function yet. Qt's 'bool "
        "QListModel::itemLessThan(const std::pair<QListWidgetItem *, int> "
        "&left, const std::pair<QListWidgetItem *, int> &right)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def sortedInsertionIterator(*__, **_) -> Never:
    """
    Qt's 'QList<QListWidgetItem *>::iterator
    QListModel::sortedInsertionIterator(const QList<QListWidgetItem
    *>::iterator &begin, const QList<QListWidgetItem *>::iterator &end,
    Qt::SortOrder order, QListWidgetItem *item)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QListModel.sortedInsertionIterator' has no cute function yet. "
        "Qt's 'QList<QListWidgetItem *>::iterator "
        "QListModel::sortedInsertionIterator(const QList<QListWidgetItem "
        "*>::iterator &begin, const QList<QListWidgetItem *>::iterator "
        "&end, Qt::SortOrder order, QListWidgetItem *item)': takes a type "
        "Python has no way to hand over yet.")
