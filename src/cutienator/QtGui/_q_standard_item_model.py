"""
QStandardItemModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qstandarditemmodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractItemModel, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData, QModelIndex
  from ..QtCore import QModelRoleDataSpan, QVariant
  from . import QStandardItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QModelIndex = WAIT['QModelIndex']
  QModelRoleDataSpan = WAIT['QModelRoleDataSpan']
  QStandardItem = WAIT['QStandardItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStandardItemModel(QAbstractItemModel):
  """
  The cute side of Qt's QStandardItemModel: a plain Python object standing in
  front of one C++ QStandardItemModel.

  It is built on the cute 'QAbstractItemModel', as Qt's QStandardItemModel is
  built on Qt's QAbstractItemModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStandardItemModel that has a ritual and that Python
  can call so far, 43 names in all: 'metaObject', 'tr', 'index', 'parent',
  'rowCount', 'columnCount', 'hasChildren', 'data', 'multiData', 'setData',
  'clearItemData', 'headerData', 'setHeaderData', 'insertRows',
  'insertColumns', 'removeRows', 'removeColumns', 'flags',
  'supportedDropActions', 'clear', 'sort', 'itemFromIndex', 'indexFromItem',
  'item', 'setItem', 'invisibleRootItem', 'horizontalHeaderItem',
  'setHorizontalHeaderItem', 'verticalHeaderItem', 'setVerticalHeaderItem',
  'setRowCount', 'setColumnCount', 'appendRow', 'insertRow', 'insertColumn',
  'takeItem', 'takeHorizontalHeaderItem', 'takeVerticalHeaderItem',
  'itemPrototype', 'setItemPrototype', 'sortRole', 'setSortRole',
  'dropMimeData'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStandardItemModel::~QStandardItemModel()': the destructor: Python
    never removes a C++ QStandardItemModel.

  What has no ritual
  ------------------

  26 of the 74 functions Qt declares: 18 takes or gives a type that cannot be
  passed yet; 3 private; 2 forbidden; 1 a template; 1 a signal; 1 protected.

  What to expect
  --------------

  - The C++ QStandardItemModel is created at the first use, not by
    'QStandardItemModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStandardItemModel.
  - Qt tells when it has removed the C++ QStandardItemModel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QStandardItemModel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#tr

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
    #  QString QStandardItemModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QStandardItemModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStandardItemModel'

  #  A C++ QStandardItemModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStandardItemModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStandardItemModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStandardItemModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def index(
      self,
      row: int,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QStandardItemModel::index(int row, int column,
    const QModelIndex &parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#index

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
    #  QModelIndex QStandardItemModel::index(int row, int column, const
    #      QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QStandardItemModel5indexEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel5indexEiiRK11QModelIndex'
    address = self.uglySide.call(ritual, row, column, self._valueOf(parent))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def parent(self, child: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QStandardItemModel::parent(const QModelIndex
    &child) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#parent

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
    #  QModelIndex QStandardItemModel::parent(const QModelIndex &child) const
    ritual = 'ritual_ZNK18QStandardItemModel6parentERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel6parentERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(child))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QStandardItemModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QStandardItemModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QStandardItemModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QStandardItemModel::columnCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QStandardItemModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QStandardItemModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QStandardItemModel11columnCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def hasChildren(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::hasChildren(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#hasChildren

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK18QStandardItemModel11hasChildrenERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QStandardItemModel11hasChildrenERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QStandardItemModel::data(const QModelIndex &index,
    int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#data

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
    #  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
    #      const
    ritual = 'ritual_ZNK18QStandardItemModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, Qt.Orientation)
  @overload(int, Qt.Orientation, int)
  def headerData(
      self,
      section: int,
      orientation: Qt.Orientation,
      role: int = 0,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QStandardItemModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#headerData

    Parameters
    ----------

    section : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = (
        'ritual_ZNK18QStandardItemModel10headerDataEiN2Qt11OrientationEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QStandardItemModel10headerDataEiN2Qt11Orientatio'
          'nEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QStandardItemModel::flags(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#flags

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
    #  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK18QStandardItemModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def supportedDropActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QStandardItemModel::supportedDropActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#supportedDropActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QStandardItemModel::supportedDropActions() const
    ritual = 'ritual_ZNK18QStandardItemModel20supportedDropActionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QStandardItemModel20supportedDropActionsEv'
    return Qt.DropActions(self.uglySide.call(ritual))

  @overload(QModelIndex)
  def itemFromIndex(self, index: QModelIndex) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::itemFromIndex(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#itemFromIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::itemFromIndex(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel13itemFromIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(QStandardItem)
  @overload(NoneType)
  def indexFromItem(self, item: Optional[QStandardItem]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QStandardItemModel::indexFromItem(const
    QStandardItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#indexFromItem

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QStandardItemModel::indexFromItem(const QStandardItem
    #      *item) const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel13indexFromItemEPK13QStandardItem',
        self._addressOf(item),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  @overload(int, int)
  def item(self, row: int, column: int = 0) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::item(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#item

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::item(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel4itemEii', row, column,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  def invisibleRootItem(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::invisibleRootItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#invisibleRootItem

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::invisibleRootItem() const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel17invisibleRootItemEv',
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(int)
  def horizontalHeaderItem(self, column: int) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::horizontalHeaderItem(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#horizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::horizontalHeaderItem(int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel20horizontalHeaderItemEi', column,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(int)
  def verticalHeaderItem(self, row: int) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::verticalHeaderItem(int
    row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#verticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::verticalHeaderItem(int row) const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel18verticalHeaderItemEi', row,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  def itemPrototype(self) -> Optional[QStandardItem]:
    """
    Calls Qt's 'const QStandardItem *QStandardItemModel::itemPrototype()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#itemPrototype

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStandardItem *QStandardItemModel::itemPrototype() const
    address = self.uglySide.call(
        'ritual_ZNK18QStandardItemModel13itemPrototypeEv',
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  def sortRole(self) -> int:
    """
    Calls Qt's 'int QStandardItemModel::sortRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#sortRole
    """
    #  int QStandardItemModel::sortRole() const
    return self.uglySide.call('ritual_ZNK18QStandardItemModel8sortRoleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::setData(const QModelIndex &index,
    const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QStandardItemModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN18QStandardItemModel7setDataERK11QModelIndexRK8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel7setDataERK11QModelIndexRK8QVar'
          'ianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(int, Qt.Orientation, QVariant)
  @overload(int, Qt.Orientation, QVariant, int)
  def setHeaderData(
      self,
      section: int,
      orientation: Qt.Orientation,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setHeaderData

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
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN18QStandardItemModel13setHeaderDataEiN2Qt11OrientationERK'
        '8QVarianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel13setHeaderDataEiN2Qt11Orientat'
          'ionERK8QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
    )

  @overload(int, int, QStandardItem)
  @overload(int, int, NoneType)
  def setItem(
      self,
      row: int,
      column: int,
      item: Optional[QStandardItem],
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setItem(int row, int column,
    QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#setItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::setItem(int row, int column, QStandardItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel7setItemEiiP13QStandardItem',
        row, column, self._addressOf(item),
    )

  @overload(int, QStandardItem)
  @overload(int, NoneType)
  def setItem(self, row: int, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setItem(int row, QStandardItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#setItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::setItem(int row, QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel7setItemEiP13QStandardItem',
        row, self._addressOf(item),
    )

  @overload(int, QStandardItem)
  @overload(int, NoneType)
  def setHorizontalHeaderItem(
      self,
      column: int,
      item: Optional[QStandardItem],
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setHorizontalHeaderItem(int column,
    QStandardItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setHorizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::setHorizontalHeaderItem(int column,
    #      QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel23setHorizontalHeaderItemEiP13QStanda'
        'rdItem',
        column, self._addressOf(item),
    )

  @overload(int, QStandardItem)
  @overload(int, NoneType)
  def setVerticalHeaderItem(
      self,
      row: int,
      item: Optional[QStandardItem],
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setVerticalHeaderItem(int row,
    QStandardItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setVerticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::setVerticalHeaderItem(int row, QStandardItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel21setVerticalHeaderItemEiP13QStandard'
        'Item',
        row, self._addressOf(item),
    )

  @overload(int)
  def setRowCount(self, rows: int) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setRowCount(int rows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setRowCount

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QStandardItemModel::setRowCount(int rows)
    self.uglySide.call('ritual_ZN18QStandardItemModel11setRowCountEi', rows)

  @overload(int)
  def setColumnCount(self, columns: int) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setColumnCount(int columns)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setColumnCount

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QStandardItemModel::setColumnCount(int columns)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel14setColumnCountEi', columns,
    )

  @overload(QStandardItem)
  @overload(NoneType)
  def setItemPrototype(self, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setItemPrototype(const QStandardItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setItemPrototype

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::setItemPrototype(const QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel16setItemPrototypeEPK13QStandardItem',
        self._addressOf(item),
    )

  @overload(int)
  def setSortRole(self, role: int) -> None:
    """
    Calls Qt's 'void QStandardItemModel::setSortRole(int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#setSortRole

    Parameters
    ----------

    role : int
      Passed on as it is.
    """
    #  void QStandardItemModel::setSortRole(int role)
    self.uglySide.call('ritual_ZN18QStandardItemModel11setSortRoleEi', role)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QStandardItemModel::QStandardItemModel(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#QStandardItemModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStandardItemModel::QStandardItemModel(QObject *parent)
    self._noteCreation(QStandardItemModel, lambda: Rituals.call(
        'ritual_ZN18QStandardItemModelC1EP7QObject', self._addressOf(parent),
    ))

  @overload(int, int)
  @overload(int, int, QObject)
  @overload(int, int, NoneType)
  def __init__(
      self,
      rows: int,
      columns: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QStandardItemModel::QStandardItemModel(int rows, int columns, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#QStandardItemModel

    Parameters
    ----------

    rows : int
      Passed on as it is.

    columns : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStandardItemModel::QStandardItemModel(int rows, int columns, QObject
    #      *parent)
    self._noteCreation(QStandardItemModel, lambda: Rituals.call(
        'ritual_ZN18QStandardItemModelC1EiiP7QObject',
        rows, columns, self._addressOf(parent),
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

  @overload(QModelIndex, QModelRoleDataSpan)
  def multiData(
      self,
      index: QModelIndex,
      roleDataSpan: QModelRoleDataSpan,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModel::multiData(const QModelIndex &index,
    QModelRoleDataSpan roleDataSpan) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#multiData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleDataSpan : QModelRoleDataSpan
      Passed on as a value: Qt reads the C++ QModelRoleDataSpan, which stays
      Python's own.
    """
    #  void QStandardItemModel::multiData(const QModelIndex &index,
    #      QModelRoleDataSpan roleDataSpan) const
    ritual = (
        'ritual_ZNK18QStandardItemModel9multiDataERK11QModelIndex18QModelRo'
        'leDataSpan')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QStandardItemModel9multiDataERK11QModelIndex18QM'
          'odelRoleDataSpan')
    self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(roleDataSpan),
    )

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::clearItemData(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QStandardItemModel::clearItemData(const QModelIndex &index)
    ritual = 'ritual_ZN18QStandardItemModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel13clearItemDataERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#insertRows

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
    #  bool QStandardItemModel::insertRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QStandardItemModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel10insertRowsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::insertColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#insertColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QStandardItemModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QStandardItemModel13insertColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel13insertColumnsEiiRK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#removeRows

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
    #  bool QStandardItemModel::removeRows(int row, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QStandardItemModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel10removeRowsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::removeColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#removeColumns

    Parameters
    ----------

    column : int
      Passed on as it is.

    count : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QStandardItemModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN18QStandardItemModel13removeColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel13removeColumnsEiiRK11QModelInd'
          'ex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  def clear(self) -> None:
    """
    Calls Qt's 'void QStandardItemModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#clear
    """
    #  void QStandardItemModel::clear()
    self.uglySide.call('ritual_ZN18QStandardItemModel5clearEv')

  @overload(int)
  @overload(int, Qt.SortOrder)
  def sort(
      self,
      column: int,
      order: Qt.SortOrder = Qt.SortOrder.AscendingOrder,
  ) -> None:
    """
    Calls Qt's 'void QStandardItemModel::sort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SortOrder.AscendingOrder.
    """
    #  void QStandardItemModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN18QStandardItemModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QStandardItemModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(QStandardItem)
  @overload(NoneType)
  def appendRow(self, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItemModel::appendRow(QStandardItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#appendRow

    Parameters
    ----------

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::appendRow(QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel9appendRowEP13QStandardItem',
        self._addressOf(item),
    )

  @overload(int, QStandardItem)
  @overload(int, NoneType)
  def insertRow(self, row: int, item: Optional[QStandardItem]) -> None:
    """
    Calls Qt's 'void QStandardItemModel::insertRow(int row, QStandardItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    item : Optional[QStandardItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStandardItemModel::insertRow(int row, QStandardItem *item)
    self.uglySide.call(
        'ritual_ZN18QStandardItemModel9insertRowEiP13QStandardItem',
        row, self._addressOf(item),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def insertRow(
      self,
      row: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::insertRow(int row, const QModelIndex
    &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QStandardItemModel::insertRow(int row, const QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QStandardItemModel9insertRowEiRK11QModelIndex',
        row, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, QModelIndex)
  def insertColumn(
      self,
      column: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QStandardItemModel::insertColumn(int column, const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#insertColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QStandardItemModel::insertColumn(int column, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    return self.uglySide.call(
        'ritual_ZN18QStandardItemModel12insertColumnEiRK11QModelIndex',
        column, self._valueOf(parent),
    )

  @overload(int)
  @overload(int, int)
  def takeItem(self, row: int, column: int = 0) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::takeItem(int row, int
    column)'.

    Qt's own words: https://doc.qt.io/qt-6/qstandarditemmodel.html#takeItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::takeItem(int row, int column)
    address = self.uglySide.call(
        'ritual_ZN18QStandardItemModel8takeItemEii', row, column,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(int)
  def takeHorizontalHeaderItem(self, column: int) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem
    *QStandardItemModel::takeHorizontalHeaderItem(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#takeHorizontalHeaderItem

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::takeHorizontalHeaderItem(int
    #      column)
    address = self.uglySide.call(
        'ritual_ZN18QStandardItemModel24takeHorizontalHeaderItemEi', column,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

  @overload(int)
  def takeVerticalHeaderItem(self, row: int) -> Optional[QStandardItem]:
    """
    Calls Qt's 'QStandardItem *QStandardItemModel::takeVerticalHeaderItem(int
    row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#takeVerticalHeaderItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QStandardItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStandardItem *QStandardItemModel::takeVerticalHeaderItem(int row)
    address = self.uglySide.call(
        'ritual_ZN18QStandardItemModel22takeVerticalHeaderItemEi', row,
    )
    from . import QStandardItem
    return QStandardItem._cuteAt(address)

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
    Calls Qt's 'bool QStandardItemModel::dropMimeData(const QMimeData *data,
    Qt::DropAction action, int row, int column, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstandarditemmodel.html#dropMimeData

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
    #  bool QStandardItemModel::dropMimeData(const QMimeData *data,
    #      Qt::DropAction action, int row, int column, const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN18QStandardItemModel12dropMimeDataEPK9QMimeDataN2Qt10Drop'
        'ActionEiiRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QStandardItemModel12dropMimeDataEPK9QMimeDataN2Qt'
          '10DropActionEiiRK11QModelIndex')
    return self.uglySide.call(
        ritual,
        self._addressOf(data), action.value, row, column,
        self._valueOf(parent),
    )
