"""
QAccessibleTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/itemviews_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAccessibleTable to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtGui import QAccessible, QAccessibleInterface
from ..QtGui import QAccessibleSelectionInterface, QAccessibleTableInterface
from . import QAccessibleWidgetV2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex
  from ..QtGui import QAccessibleTableModelChangeEvent
  from . import QAbstractItemView, QHeaderView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccessibleTableModelChangeEvent = WAIT['QAccessibleTableModelChangeEvent']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleTable(QAccessibleTableInterface, QAccessibleSelectionInterface, QAccessibleWidgetV2):
  """
  The cute side of Qt's QAccessibleTable: a plain Python object standing in
  front of one C++ QAccessibleTable.

  It is built on the cute 'QAccessibleTableInterface', as Qt's
  QAccessibleTable is built on Qt's QAccessibleTableInterface, and has
  everything that class has. It is built on the cute
  'QAccessibleSelectionInterface' as well, as Qt's QAccessibleTable is built
  on Qt's QAccessibleSelectionInterface too, and has everything that class
  has. It is built on the cute 'QAccessibleWidgetV2' as well, as Qt's
  QAccessibleTable is built on Qt's QAccessibleWidgetV2 too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleTable that has a ritual and that Python
  can call so far, 36 names in all: 'childAt', 'focusChild', 'childCount',
  'indexOfChild', 'parent', 'child', 'cellAt', 'caption', 'summary',
  'columnDescription', 'rowDescription', 'columnCount', 'rowCount',
  'selectedCellCount', 'selectedColumnCount', 'selectedRowCount',
  'selectedCells', 'isColumnSelected', 'isRowSelected', 'selectRow',
  'selectColumn', 'unselectRow', 'unselectColumn', 'selectedItemCount',
  'selectedItems', 'isSelected', 'select', 'unselect', 'selectAll', 'clear',
  'view', 'modelChange', 'cellRole', 'horizontalHeader', 'verticalHeader',
  'logicalIndex'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAccessibleTable::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.
  - Qt's 'QList<int> QAccessibleTable::selectedColumns() const': gives a type
    Python has no way to take yet.
  - Qt's 'QList<int> QAccessibleTable::selectedRows() const': gives a type
    Python has no way to take yet.
  - Qt's 'QAccessibleTable::~QAccessibleTable()': the destructor: Python
    never removes a C++ QAccessibleTable.

  What has no ritual
  ------------------

  1 of the 41 functions Qt declares: 1 leans on 'non-virtual thunk to
  QAccessibleTable.

  What to expect
  --------------

  - The C++ QAccessibleTable is created at the first use, not by
    'QAccessibleTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleTable.
  - Each name of Qt's QAccessibleTable that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleTable'

  #  Qt's QAccessibleTable is built on more than one class. The part of a C++
  #  QAccessibleTable that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleSelectionInterface':
          'ritual_cast_QAccessibleTable_QAccessibleSelectionInterface',
      'QAccessibleWidgetV2':
          'ritual_cast_QAccessibleTable_QAccessibleWidgetV2',
  }

  #  A C++ QAccessibleTable Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleTable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def childAt(self, x: int, y: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::childAt(int x, int y)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#childAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::childAt(int x, int y) const
    ritual = 'ritual_ZNK16QAccessibleTable7childAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable7childAtEii'
    address = self.uglySide.call(ritual, x, y)
    return QAccessibleInterface._cuteAt(address)

  def focusChild(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::focusChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#focusChild

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::focusChild() const
    ritual = 'ritual_ZNK16QAccessibleTable10focusChildEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable10focusChildEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#childCount
    """
    #  int QAccessibleTable::childCount() const
    ritual = 'ritual_ZNK16QAccessibleTable10childCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable10childCountEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def indexOfChild(self, a0: Optional[QAccessibleInterface]) -> int:
    """
    Calls Qt's 'int QAccessibleTable::indexOfChild(const QAccessibleInterface
    *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#indexOfChild

    Parameters
    ----------

    a0 : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAccessibleTable::indexOfChild(const QAccessibleInterface *a0)
    #      const
    ritual = (
        'ritual_ZNK16QAccessibleTable12indexOfChildEPK20QAccessibleInterfac'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QAccessibleTable12indexOfChildEPK20QAccessibleIn'
          'terface')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QAccessibleInterface'),
    )

  def parent(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#parent

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::parent() const
    ritual = 'ritual_ZNK16QAccessibleTable6parentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable6parentEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def child(self, index: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::child(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#child

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::child(int index) const
    ritual = 'ritual_ZNK16QAccessibleTable5childEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable5childEi'
    address = self.uglySide.call(ritual, index)
    return QAccessibleInterface._cuteAt(address)

  @overload(int, int)
  def cellAt(self, row: int, column: int) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::cellAt(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#cellAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::cellAt(int row, int column)
    #      const
    ritual = 'ritual_ZNK16QAccessibleTable6cellAtEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable6cellAtEii'
    address = self.uglySide.call(ritual, row, column)
    return QAccessibleInterface._cuteAt(address)

  def caption(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::caption() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#caption

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::caption() const
    ritual = 'ritual_ZNK16QAccessibleTable7captionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable7captionEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  def summary(self) -> Optional[QAccessibleInterface]:
    """
    Calls Qt's 'QAccessibleInterface *QAccessibleTable::summary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#summary

    Returns
    -------

    Optional[QAccessibleInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAccessibleInterface *QAccessibleTable::summary() const
    ritual = 'ritual_ZNK16QAccessibleTable7summaryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable7summaryEv'
    address = self.uglySide.call(ritual)
    return QAccessibleInterface._cuteAt(address)

  @overload(int)
  def columnDescription(self, column: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTable::columnDescription(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#columnDescription

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTable::columnDescription(int column) const
    ritual = 'ritual_ZNK16QAccessibleTable17columnDescriptionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable17columnDescriptionEi'
    return self.uglySide.call(ritual, column)

  @overload(int)
  def rowDescription(self, row: int) -> str:
    """
    Calls Qt's 'QString QAccessibleTable::rowDescription(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#rowDescription

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAccessibleTable::rowDescription(int row) const
    ritual = 'ritual_ZNK16QAccessibleTable14rowDescriptionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable14rowDescriptionEi'
    return self.uglySide.call(ritual, row)

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#columnCount
    """
    #  int QAccessibleTable::columnCount() const
    ritual = 'ritual_ZNK16QAccessibleTable11columnCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable11columnCountEv'
    return self.uglySide.call(ritual)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#rowCount
    """
    #  int QAccessibleTable::rowCount() const
    ritual = 'ritual_ZNK16QAccessibleTable8rowCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable8rowCountEv'
    return self.uglySide.call(ritual)

  def selectedCellCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::selectedCellCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedCellCount
    """
    #  int QAccessibleTable::selectedCellCount() const
    ritual = 'ritual_ZNK16QAccessibleTable17selectedCellCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable17selectedCellCountEv'
    return self.uglySide.call(ritual)

  def selectedColumnCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::selectedColumnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedColumnCount
    """
    #  int QAccessibleTable::selectedColumnCount() const
    ritual = 'ritual_ZNK16QAccessibleTable19selectedColumnCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable19selectedColumnCountEv'
    return self.uglySide.call(ritual)

  def selectedRowCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::selectedRowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedRowCount
    """
    #  int QAccessibleTable::selectedRowCount() const
    ritual = 'ritual_ZNK16QAccessibleTable16selectedRowCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable16selectedRowCountEv'
    return self.uglySide.call(ritual)

  def selectedCells(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTable::selectedCells() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedCells

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *> QAccessibleTable::selectedCells() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleTable13selectedCellsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

  @overload(int)
  def isColumnSelected(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::isColumnSelected(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#isColumnSelected

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::isColumnSelected(int column) const
    ritual = 'ritual_ZNK16QAccessibleTable16isColumnSelectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable16isColumnSelectedEi'
    return self.uglySide.call(ritual, column)

  @overload(int)
  def isRowSelected(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::isRowSelected(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#isRowSelected

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::isRowSelected(int row) const
    ritual = 'ritual_ZNK16QAccessibleTable13isRowSelectedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable13isRowSelectedEi'
    return self.uglySide.call(ritual, row)

  def selectedItemCount(self) -> int:
    """
    Calls Qt's 'int QAccessibleTable::selectedItemCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedItemCount
    """
    #  int QAccessibleTable::selectedItemCount() const
    ritual = 'ritual_ZNK16QAccessibleTable17selectedItemCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QAccessibleTable17selectedItemCountEv'
    return self.uglySide.call(ritual)

  def selectedItems(self) -> QList[QAccessibleInterface]:
    """
    Calls Qt's 'QList<QAccessibleInterface *>
    QAccessibleTable::selectedItems() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#selectedItems

    Returns
    -------

    QList[QAccessibleInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAccessibleInterface *> QAccessibleTable::selectedItems() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleTable13selectedItemsEv',
    )
    return QList[QAccessibleInterface]._cuteOwning(address)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def isSelected(self, childCell: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::isSelected(QAccessibleInterface
    *childCell) const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#isSelected

    Parameters
    ----------

    childCell : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTable::isSelected(QAccessibleInterface *childCell)
    #      const
    ritual = (
        'ritual_ZNK16QAccessibleTable10isSelectedEP20QAccessibleInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QAccessibleTable10isSelectedEP20QAccessibleInter'
          'face')
    return self.uglySide.call(
        ritual, self._addressOf(childCell, 'QAccessibleInterface'),
    )

  def view(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QAccessibleTable::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#view

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QAccessibleTable::view() const
    address = self.uglySide.call('ritual_ZNK16QAccessibleTable4viewEv')
    from . import QAbstractItemView
    return QAbstractItemView._cuteAt(address)

  def cellRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QAccessibleTable::cellRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#cellRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QAccessibleTable::cellRole() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK16QAccessibleTable8cellRoleEv',
    ))

  def horizontalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QAccessibleTable::horizontalHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#horizontalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QAccessibleTable::horizontalHeader() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleTable16horizontalHeaderEv',
    )
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  def verticalHeader(self) -> Optional[QHeaderView]:
    """
    Calls Qt's 'QHeaderView *QAccessibleTable::verticalHeader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#verticalHeader

    Returns
    -------

    Optional[QHeaderView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeaderView *QAccessibleTable::verticalHeader() const
    address = self.uglySide.call(
        'ritual_ZNK16QAccessibleTable14verticalHeaderEv',
    )
    from . import QHeaderView
    return QHeaderView._cuteAt(address)

  @overload(QModelIndex)
  def logicalIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QAccessibleTable::logicalIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#logicalIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QAccessibleTable::logicalIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK16QAccessibleTable12logicalIndexERK11QModelIndex',
        self._valueOf(index),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QAccessibleTable::QAccessibleTable(QWidget *w, QAccessible::Role
    role)': leans on 'non-virtual thunk to QAccessibleTable::selectedItems()
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAccessibleTable.__init__' has no cute function yet. Qt's "
        "'QAccessibleTable::QAccessibleTable(QWidget *w, QAccessible::Role "
        "role)': leans on 'non-virtual thunk to "
        "QAccessibleTable::selectedItems() const', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def selectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::selectRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::selectRow(int row)
    ritual = 'ritual_ZN16QAccessibleTable9selectRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable9selectRowEi'
    return self.uglySide.call(ritual, row)

  @overload(int)
  def selectColumn(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::selectColumn(int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#selectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::selectColumn(int column)
    ritual = 'ritual_ZN16QAccessibleTable12selectColumnEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable12selectColumnEi'
    return self.uglySide.call(ritual, column)

  @overload(int)
  def unselectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::unselectRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#unselectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::unselectRow(int row)
    ritual = 'ritual_ZN16QAccessibleTable11unselectRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable11unselectRowEi'
    return self.uglySide.call(ritual, row)

  @overload(int)
  def unselectColumn(self, column: int) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::unselectColumn(int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessibletable.html#unselectColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QAccessibleTable::unselectColumn(int column)
    ritual = 'ritual_ZN16QAccessibleTable14unselectColumnEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable14unselectColumnEi'
    return self.uglySide.call(ritual, column)

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def select(self, childCell: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::select(QAccessibleInterface
    *childCell)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#select

    Parameters
    ----------

    childCell : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTable::select(QAccessibleInterface *childCell)
    ritual = 'ritual_ZN16QAccessibleTable6selectEP20QAccessibleInterface'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAccessibleTable6selectEP20QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(childCell, 'QAccessibleInterface'),
    )

  @overload(QAccessibleInterface)
  @overload(NoneType)
  def unselect(self, childCell: Optional[QAccessibleInterface]) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::unselect(QAccessibleInterface
    *childCell)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#unselect

    Parameters
    ----------

    childCell : Optional[QAccessibleInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAccessibleTable::unselect(QAccessibleInterface *childCell)
    ritual = 'ritual_ZN16QAccessibleTable8unselectEP20QAccessibleInterface'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAccessibleTable8unselectEP20QAccessibleInterface')
    return self.uglySide.call(
        ritual, self._addressOf(childCell, 'QAccessibleInterface'),
    )

  def selectAll(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#selectAll
    """
    #  bool QAccessibleTable::selectAll()
    ritual = 'ritual_ZN16QAccessibleTable9selectAllEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable9selectAllEv'
    return self.uglySide.call(ritual)

  def clear(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleTable::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#clear
    """
    #  bool QAccessibleTable::clear()
    ritual = 'ritual_ZN16QAccessibleTable5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QAccessibleTable5clearEv'
    return self.uglySide.call(ritual)

  @overload(QAccessibleTableModelChangeEvent)
  @overload(NoneType)
  def modelChange(
      self,
      event: Optional[QAccessibleTableModelChangeEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qaccessibletable.html#modelChange

    Parameters
    ----------

    event : Optional[QAccessibleTableModelChangeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAccessibleTable::modelChange(QAccessibleTableModelChangeEvent
    #      *event)
    ritual = (
        'ritual_ZN16QAccessibleTable11modelChangeEP32QAccessibleTableModelC'
        'hangeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QAccessibleTable11modelChangeEP32QAccessibleTable'
          'ModelChangeEvent')
    self.uglySide.call(ritual, self._addressOf(event))
