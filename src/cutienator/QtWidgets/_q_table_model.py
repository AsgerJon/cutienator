"""
QTableModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTableModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QAbstractTableModel, QList, QMap, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex, QVariant
  from . import QTableWidget, QTableWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QTableWidgetItem = WAIT['QTableWidgetItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTableModel(QAbstractTableModel):
  """
  The cute side of Qt's QTableModel: a plain Python object standing in front
  of one C++ QTableModel.

  It is built on the cute 'QAbstractTableModel', as Qt's QTableModel is built
  on Qt's QAbstractTableModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTableModel that has a ritual and that Python can
  call so far, 46 names in all: 'metaObject', 'view', 'insertRows',
  'insertColumns', 'removeRows', 'removeColumns', 'moveRows', 'setItem',
  'takeItem', 'item', 'removeItem', 'setHorizontalHeaderItem',
  'setVerticalHeaderItem', 'takeHorizontalHeaderItem',
  'takeVerticalHeaderItem', 'horizontalHeaderItem', 'verticalHeaderItem',
  'index', 'setRowCount', 'setColumnCount', 'rowCount', 'columnCount',
  'data', 'setData', 'setItemData', 'clearItemData', 'itemData',
  'headerData', 'setHeaderData', 'flags', 'sort', 'ensureSorted',
  'columnItems', 'isValid', 'tableIndex', 'clear', 'clearContents',
  'createItem', 'itemPrototype', 'setItemPrototype', 'mimeTypes', 'mimeData',
  'dropMimeData', 'supportedDropActions', 'supportedDragActions',
  'internalMimeData'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTableModel::~QTableModel()': the destructor: Python never removes
    a C++ QTableModel.

  What has no ritual
  ------------------

  11 of the 60 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 2 declared and nowhere to be found; 1 a template; 1 leans on
  'QTableModel.

  What to expect
  --------------

  - The C++ QTableModel is created at the first use, not by
    'QTableModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTableModel.
  - Qt tells when it has removed the C++ QTableModel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTableModel'

  #  A C++ QTableModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTableModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTableModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTableModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTableModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QTableWidget]:
    """
    Calls Qt's 'QTableWidget *QTableModel::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#view

    Returns
    -------

    Optional[QTableWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidget *QTableModel::view() const
    address = self.uglySide.call('ritual_ZNK11QTableModel4viewEv')
    from . import QTableWidget
    return QTableWidget._cuteAt(address)

  @overload(int, int)
  def item(self, row: int, column: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::item(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#item

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::item(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel4itemEii', row, column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(QModelIndex)
  def item(self, index: QModelIndex) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::item(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#item

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::item(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel4itemERK11QModelIndex', self._valueOf(index),
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTableModel::index(int row, int column, const
    QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#index

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTableModel::index(int row, int column, const QModelIndex
    #      &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK11QTableModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def index(self, item: Optional[QTableWidgetItem]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QTableModel::index(const QTableWidgetItem *item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#index

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QTableModel::index(const QTableWidgetItem *item) const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel5indexEPK16QTableWidgetItem',
        self._addressOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QTableModel::rowCount(const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QTableModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK11QTableModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QTableModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QTableModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK11QTableModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel11columnCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QTableModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#data

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
    #  QVariant QTableModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK11QTableModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def itemData(self, index: QModelIndex) -> QMap[int, QVariant]:
    """
    Calls Qt's 'QMap<int, QVariant> QTableModel::itemData(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#itemData

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
    #  QMap<int, QVariant> QTableModel::itemData(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel8itemDataERK11QModelIndex',
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
    Calls Qt's 'QVariant QTableModel::headerData(int section, Qt::Orientation
    orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#headerData

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
    #  QVariant QTableModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = 'ritual_ZNK11QTableModel10headerDataEiN2Qt11OrientationEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel10headerDataEiN2Qt11OrientationEi'
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QTableModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#flags

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
    #  Qt::ItemFlags QTableModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK11QTableModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  @overload(int)
  def columnItems(self, column: int) -> QList[QTableWidgetItem]:
    """
    Calls Qt's 'QList<QTableWidgetItem *> QTableModel::columnItems(int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#columnItems

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QList[QTableWidgetItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QTableWidgetItem *> QTableModel::columnItems(int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel11columnItemsEi', column,
    )
    from . import QTableWidgetItem
    return QList[QTableWidgetItem]._cuteOwning(address)

  @overload(QModelIndex)
  def isValid(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTableModel::isValid(const QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#isValid

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTableModel::isValid(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK11QTableModel7isValidERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int, int)
  def tableIndex(self, row: int, column: int) -> int:
    """
    Calls Qt's 'long QTableModel::tableIndex(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#tableIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  long QTableModel::tableIndex(int row, int column) const
    return self.uglySide.call(
        'ritual_ZNK11QTableModel10tableIndexEii', row, column,
    )

  def createItem(self) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::createItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#createItem

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::createItem() const
    address = self.uglySide.call('ritual_ZNK11QTableModel10createItemEv')
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def itemPrototype(self) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'const QTableWidgetItem *QTableModel::itemPrototype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#itemPrototype

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTableWidgetItem *QTableModel::itemPrototype() const
    address = self.uglySide.call('ritual_ZNK11QTableModel13itemPrototypeEv')
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  def mimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList QTableModel::mimeTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#mimeTypes

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTableModel::mimeTypes() const
    address = self.uglySide.call('ritual_ZNK11QTableModel9mimeTypesEv')
    return QStringList._cuteOwning(address)

  @overload(QList[QModelIndex])
  def mimeData(self, indexes: QList[QModelIndex]) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QTableModel::mimeData(const QModelIndexList
    &indexes) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#mimeData

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
    #  QMimeData *QTableModel::mimeData(const QModelIndexList &indexes) const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel8mimeDataERK5QListI11QModelIndexE',
        self._valueOf(indexes),
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTableModel::supportedDropActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTableModel::supportedDropActions() const
    ritual = 'ritual_ZNK11QTableModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def supportedDragActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QTableModel::supportedDragActions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#supportedDragActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QTableModel::supportedDragActions() const
    ritual = 'ritual_ZNK11QTableModel20supportedDragActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QTableModel20supportedDragActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  def internalMimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QTableModel::internalMimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#internalMimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QTableModel::internalMimeData() const
    address = self.uglySide.call(
        'ritual_ZNK11QTableModel16internalMimeDataEv',
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, QTableWidgetItem)
  @overload(int, int, NoneType)
  def setItem(
      self,
      row: int,
      column: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableModel::setItem(int row, int column,
    QTableWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableModel::setItem(int row, int column, QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTableModel7setItemEiiP16QTableWidgetItem',
        row, column, self._addressOf(item),
    )

  @overload(int, QTableWidgetItem)
  @overload(int, NoneType)
  def setHorizontalHeaderItem(
      self,
      section: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableModel::setHorizontalHeaderItem(int section,
    QTableWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#setHorizontalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableModel::setHorizontalHeaderItem(int section,
    #      QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTableModel23setHorizontalHeaderItemEiP16QTableWidgetIt'
        'em',
        section, self._addressOf(item),
    )

  @overload(int, QTableWidgetItem)
  @overload(int, NoneType)
  def setVerticalHeaderItem(
      self,
      section: int,
      item: Optional[QTableWidgetItem],
  ) -> None:
    """
    Calls Qt's 'void QTableModel::setVerticalHeaderItem(int section,
    QTableWidgetItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#setVerticalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableModel::setVerticalHeaderItem(int section, QTableWidgetItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN11QTableModel21setVerticalHeaderItemEiP16QTableWidgetItem',
        section, self._addressOf(item),
    )

  @overload(int)
  def setRowCount(self, rows: int) -> None:
    """
    Calls Qt's 'void QTableModel::setRowCount(int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setRowCount

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QTableModel::setRowCount(int rows)
    self.uglySide.call('ritual_ZN11QTableModel11setRowCountEi', rows)

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QTableModel::setColumnCount(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QTableModel::setColumnCount(int columns)
    self.uglySide.call('ritual_ZN11QTableModel14setColumnCountEi', columns)

  @overload(QModelIndex, QVariant, int)
  def setData(self, index: QModelIndex, value: QVariant, role: int) -> bool:
    """
    Calls Qt's 'bool QTableModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setData

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
    #  bool QTableModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN11QTableModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QTableModel7setDataERK11QModelIndexRK8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(QModelIndex, QMap[int, QVariant])
  def setItemData(
      self,
      index: QModelIndex,
      roles: QMap[int, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QTableModel::setItemData(const QModelIndex &index, const
    QMap<int, QVariant> &roles)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roles : QMap[int, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QTableModel::setItemData(const QModelIndex &index, const
    #      QMap<int, QVariant> &roles)
    return self.uglySide.call(
        'ritual_ZN11QTableModel11setItemDataERK11QModelIndexRK4QMapIi8QVari'
        'antE',
        self._valueOf(index), self._valueOf(roles),
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
    Calls Qt's 'bool QTableModel::setHeaderData(int section, Qt::Orientation
    orientation, const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setHeaderData

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
    #  bool QTableModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN11QTableModel13setHeaderDataEiN2Qt11OrientationERK8QVaria'
        'nti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QTableModel13setHeaderDataEiN2Qt11OrientationERK8'
          'QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
    )

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def setItemPrototype(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableModel::setItemPrototype(const QTableWidgetItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#setItemPrototype

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableModel::setItemPrototype(const QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTableModel16setItemPrototypeEPK16QTableWidgetItem',
        self._addressOf(item),
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
    Calls Qt's 'bool QTableModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#insertRows

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
    #  bool QTableModel::insertRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN11QTableModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel10insertRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int = 1,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTableModel::insertColumns(int column, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTableModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN11QTableModel13insertColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel13insertColumnsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

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
    Calls Qt's 'bool QTableModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#removeRows

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
    #  bool QTableModel::removeRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN11QTableModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel10removeRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int)
  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int = 1,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QTableModel::removeColumns(int column, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QTableModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN11QTableModel13removeColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel13removeColumnsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

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
    Calls Qt's 'bool QTableModel::moveRows(const QModelIndex &sourceParent,
    int sourceRow, int count, const QModelIndex &destinationParent, int
    destinationChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#moveRows

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
    #  bool QTableModel::moveRows(const QModelIndex &sourceParent, int
    #      sourceRow, int count, const QModelIndex &destinationParent, int
    #      destinationChild)
    ritual = 'ritual_ZN11QTableModel8moveRowsERK11QModelIndexiiS2_i'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel8moveRowsERK11QModelIndexiiS2_i'
    return self.uglySide.call(
        ritual,
        self._valueOf(sourceParent), sourceRow, count,
        self._valueOf(destinationParent), destinationChild,
    )

  @overload(int, int)
  def takeItem(self, row: int, column: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::takeItem(int row, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#takeItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::takeItem(int row, int column)
    address = self.uglySide.call(
        'ritual_ZN11QTableModel8takeItemEii', row, column,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(QTableWidgetItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QTableWidgetItem]) -> None:
    """
    Calls Qt's 'void QTableModel::removeItem(QTableWidgetItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#removeItem

    Parameters
    ----------

    item : Optional[QTableWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTableModel::removeItem(QTableWidgetItem *item)
    self.uglySide.call(
        'ritual_ZN11QTableModel10removeItemEP16QTableWidgetItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeHorizontalHeaderItem(
      self,
      section: int,
  ) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::takeHorizontalHeaderItem(int
    section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#takeHorizontalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::takeHorizontalHeaderItem(int section)
    address = self.uglySide.call(
        'ritual_ZN11QTableModel24takeHorizontalHeaderItemEi', section,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def takeVerticalHeaderItem(
      self,
      section: int,
  ) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::takeVerticalHeaderItem(int
    section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#takeVerticalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::takeVerticalHeaderItem(int section)
    address = self.uglySide.call(
        'ritual_ZN11QTableModel22takeVerticalHeaderItemEi', section,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def horizontalHeaderItem(self, section: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::horizontalHeaderItem(int
    section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#horizontalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::horizontalHeaderItem(int section)
    address = self.uglySide.call(
        'ritual_ZN11QTableModel20horizontalHeaderItemEi', section,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(int)
  def verticalHeaderItem(self, section: int) -> Optional[QTableWidgetItem]:
    """
    Calls Qt's 'QTableWidgetItem *QTableModel::verticalHeaderItem(int
    section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtablemodel.html#verticalHeaderItem

    Parameters
    ----------

    section : int
      Passed on as it is.

    Returns
    -------

    Optional[QTableWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTableWidgetItem *QTableModel::verticalHeaderItem(int section)
    address = self.uglySide.call(
        'ritual_ZN11QTableModel18verticalHeaderItemEi', section,
    )
    from . import QTableWidgetItem
    return QTableWidgetItem._cuteAt(address)

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QTableModel::clearItemData(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QTableModel::clearItemData(const QModelIndex &index)
    ritual = 'ritual_ZN11QTableModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel13clearItemDataERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(int, Qt.SortOrder)
  def sort(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QTableModel::sort(int column, Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QTableModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN11QTableModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QTableModel4sortEiN2Qt9SortOrderE'
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
    Calls Qt's 'void QTableModel::ensureSorted(int column, Qt::SortOrder
    order, int start, int end)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#ensureSorted

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
    #  void QTableModel::ensureSorted(int column, Qt::SortOrder order, int
    #      start, int end)
    self.uglySide.call(
        'ritual_ZN11QTableModel12ensureSortedEiN2Qt9SortOrderEii',
        column, order.value, start, end,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QTableModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#clear
    """
    #  void QTableModel::clear()
    self.uglySide.call('ritual_ZN11QTableModel5clearEv')

  def clearContents(self) -> None:
    """
    Calls Qt's 'void QTableModel::clearContents()'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#clearContents
    """
    #  void QTableModel::clearContents()
    self.uglySide.call('ritual_ZN11QTableModel13clearContentsEv')

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
    Calls Qt's 'bool QTableModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtablemodel.html#dropMimeData

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
    #  bool QTableModel::dropMimeData(const QMimeData *data, Qt::DropAction
    #      action, int row, int column, const QModelIndex &parent)
    ritual = (
        'ritual_ZN11QTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionE'
        'iiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropA'
          'ctionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )
