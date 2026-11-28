"""
QSqlTableModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqltablemodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QSqlQueryModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QSqlDatabase, QSqlIndex, QSqlRecord, QSqlTableModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QSqlDatabase = WAIT['QSqlDatabase']
  QSqlIndex = WAIT['QSqlIndex']
  QSqlRecord = WAIT['QSqlRecord']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlTableModel(QSqlQueryModel):
  """
  The cute side of Qt's QSqlTableModel: a plain Python object standing in
  front of one C++ QSqlTableModel.

  It is built on the cute 'QSqlQueryModel', as Qt's QSqlTableModel is built
  on Qt's QSqlQueryModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlTableModel that has a ritual and that Python can
  call so far, 44 names in all: 'metaObject', 'tr', 'd_func', 'setTable',
  'tableName', 'flags', 'record', 'data', 'setData', 'clearItemData',
  'headerData', 'isDirty', 'clear', 'setEditStrategy', 'editStrategy',
  'primaryKey', 'database', 'fieldIndex', 'sort', 'setSort', 'filter',
  'setFilter', 'rowCount', 'removeColumns', 'removeRows', 'insertRows',
  'insertRecord', 'setRecord', 'revertRow', 'select', 'selectRow', 'submit',
  'revert', 'submitAll', 'revertAll', 'beforeDelete', 'updateRowInTable',
  'insertRowIntoTable', 'deleteRowFromTable', 'orderByClause',
  'selectStatement', 'setPrimaryKey', 'indexInQuery', 'primaryValues'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSqlTableModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSqlTableModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSqlTableModelPrivate *QSqlTableModel::d_func() const': takes
    in Python what 'QSqlTableModelPrivate *QSqlTableModel::d_func()' takes.
  - Qt's 'QSqlTableModel::~QSqlTableModel()': the destructor: Python never
    removes a C++ QSqlTableModel.
  - Qt's 'void QSqlTableModel::primeInsert(int row, QSqlRecord &record)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSqlTableModel::beforeInsert(QSqlRecord &record)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QSqlTableModel::beforeUpdate(int row, QSqlRecord &record)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSqlTableModel::QSqlTableModel(QSqlTableModelPrivate &dd, QObject
    *parent, const QSqlDatabase &db)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 57 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSqlTableModel is created at the first use, not by
    'QSqlTableModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlTableModel.
  - Qt tells when it has removed the C++ QSqlTableModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSqlTableModel that has no cute function yet,
    'beforeInsert', 'beforeUpdate', 'primeInsert', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSqlTableModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class EditStrategy(CuteNum):
    """
    The enum 'QSqlTableModel::EditStrategy' of Qt, with the 3 names Qt gives
    in it.
    """

    OnFieldChange = Kee[int](0)
    OnRowChange = Kee[int](1)
    OnManualSubmit = Kee[int](2)

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
    Calls Qt's 'QString QSqlTableModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#tr

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
    #  QString QSqlTableModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QSqlTableModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlTableModel'

  #  A C++ QSqlTableModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlTableModel'

  #  The functions Qt calls itself that QSqlTableModel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTable': (
          ('_ZN14QSqlTableModel8setTableERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setEditStrategy': (
          ('_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtSql:QSqlTableModel.EditStrategy'),
           )),
      ),
      'setSort': (
          ('_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.SortOrder'),
           )),
      ),
      'setFilter': (
          ('_ZN14QSqlTableModel9setFilterERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'revertRow': (
          ('_ZN14QSqlTableModel9revertRowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'select': (
          ('_ZN14QSqlTableModel6selectEv',
           ('bool', 'number', ''),
           ()),
      ),
      'selectRow': (
          ('_ZN14QSqlTableModel9selectRowEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'updateRowInTable': (
          ('_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtSql:QSqlRecord'),
           )),
      ),
      'insertRowIntoTable': (
          ('_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtSql:QSqlRecord'),
           )),
      ),
      'deleteRowFromTable': (
          ('_ZN14QSqlTableModel18deleteRowFromTableEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'orderByClause': (
          ('_ZNK14QSqlTableModel13orderByClauseEv',
           ('address', 'text', ''),
           ()),
      ),
      'selectStatement': (
          ('_ZNK14QSqlTableModel15selectStatementEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSqlTableModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSqlTableModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QSqlTableModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tableName(self) -> str:
    """
    Calls Qt's 'QString QSqlTableModel::tableName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#tableName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlTableModel::tableName() const
    return self.uglySide.call('ritual_ZNK14QSqlTableModel9tableNameEv')

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#flags

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
    #  Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index) const
    ritual = 'ritual_ZNK14QSqlTableModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel5flagsERK11QModelIndex'
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  @overload()
  def record(self) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlTableModel::record() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#record

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlTableModel::record() const
    address = self.uglySide.call('ritual_ZNK14QSqlTableModel6recordEv')
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(int)
  def record(self, row: int) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlTableModel::record(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#record

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlTableModel::record(int row) const
    address = self.uglySide.call('ritual_ZNK14QSqlTableModel6recordEi', row)
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, idx: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlTableModel::data(const QModelIndex &idx, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#data

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlTableModel::data(const QModelIndex &idx, int role) const
    ritual = 'ritual_ZNK14QSqlTableModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(idx), role)
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
    Calls Qt's 'QVariant QSqlTableModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#headerData

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
    #  QVariant QSqlTableModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = 'ritual_ZNK14QSqlTableModel10headerDataEiN2Qt11OrientationEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QSqlTableModel10headerDataEiN2Qt11OrientationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload()
  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#isDirty
    """
    #  bool QSqlTableModel::isDirty() const
    return self.uglySide.call('ritual_ZNK14QSqlTableModel7isDirtyEv')

  @overload(QModelIndex)
  def isDirty(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::isDirty(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#isDirty

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSqlTableModel::isDirty(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK14QSqlTableModel7isDirtyERK11QModelIndex',
        self._valueOf(index),
    )

  def editStrategy(self) -> EditStrategy:
    """
    Calls Qt's 'EditStrategy QSqlTableModel::editStrategy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#editStrategy

    Returns
    -------

    EditStrategy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EditStrategy(number)'
      gives.
    """
    #  EditStrategy QSqlTableModel::editStrategy() const
    return QSqlTableModel.EditStrategy(self.uglySide.call(
        'ritual_ZNK14QSqlTableModel12editStrategyEv',
    ))

  def primaryKey(self) -> QSqlIndex:
    """
    Calls Qt's 'QSqlIndex QSqlTableModel::primaryKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#primaryKey

    Returns
    -------

    QSqlIndex
      A new cute QSqlIndex around the copy Qt gave back. Python owns it.
    """
    #  QSqlIndex QSqlTableModel::primaryKey() const
    address = self.uglySide.call('ritual_ZNK14QSqlTableModel10primaryKeyEv')
    from . import QSqlIndex
    return QSqlIndex._cuteOwning(address)

  def database(self) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlTableModel::database() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#database

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlTableModel::database() const
    address = self.uglySide.call('ritual_ZNK14QSqlTableModel8databaseEv')
    from . import QSqlDatabase
    return QSqlDatabase._cuteOwning(address)

  @overload(str)
  def fieldIndex(self, fieldName: str) -> int:
    """
    Calls Qt's 'int QSqlTableModel::fieldIndex(const QString &fieldName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#fieldIndex

    Parameters
    ----------

    fieldName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QSqlTableModel::fieldIndex(const QString &fieldName) const
    return self.uglySide.call(
        'ritual_ZNK14QSqlTableModel10fieldIndexERK7QString', fieldName,
    )

  def filter(self) -> str:
    """
    Calls Qt's 'QString QSqlTableModel::filter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#filter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlTableModel::filter() const
    return self.uglySide.call('ritual_ZNK14QSqlTableModel6filterEv')

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QSqlTableModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QSqlTableModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QSqlTableModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  def orderByClause(self) -> str:
    """
    Calls Qt's 'QString QSqlTableModel::orderByClause() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#orderByClause

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlTableModel::orderByClause() const
    ritual = 'ritual_ZNK14QSqlTableModel13orderByClauseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel13orderByClauseEv'
    return self.uglySide.call(ritual)

  def selectStatement(self) -> str:
    """
    Calls Qt's 'QString QSqlTableModel::selectStatement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodel.html#selectStatement

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlTableModel::selectStatement() const
    ritual = 'ritual_ZNK14QSqlTableModel15selectStatementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel15selectStatementEv'
    return self.uglySide.call(ritual)

  @overload(QModelIndex)
  def indexInQuery(self, item: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSqlTableModel::indexInQuery(const QModelIndex
    &item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#indexInQuery

    Parameters
    ----------

    item : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QSqlTableModel::indexInQuery(const QModelIndex &item)
    #      const
    ritual = 'ritual_ZNK14QSqlTableModel12indexInQueryERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlTableModel12indexInQueryERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(item))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def primaryValues(self, row: int) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlTableModel::primaryValues(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#primaryValues

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlTableModel::primaryValues(int row) const
    address = self.uglySide.call(
        'ritual_ZNK14QSqlTableModel13primaryValuesEi', row,
    )
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTable(self, tableName: str) -> None:
    """
    Calls Qt's 'void QSqlTableModel::setTable(const QString &tableName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setTable

    Parameters
    ----------

    tableName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlTableModel::setTable(const QString &tableName)
    ritual = 'ritual_ZN14QSqlTableModel8setTableERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel8setTableERK7QString'
    self.uglySide.call(ritual, tableName)

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::setData(const QModelIndex &index, const
    QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setData

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
    #  bool QSqlTableModel::setData(const QModelIndex &index, const QVariant
    #      &value, int role)
    ritual = 'ritual_ZN14QSqlTableModel7setDataERK11QModelIndexRK8QVarianti'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlTableModel7setDataERK11QModelIndexRK8QVariant'
          'i')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  @overload(EditStrategy)
  def setEditStrategy(self, strategy: EditStrategy) -> None:
    """
    Calls Qt's 'void QSqlTableModel::setEditStrategy(EditStrategy strategy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodel.html#setEditStrategy

    Parameters
    ----------

    strategy : EditStrategy
      Passed on as its number.
    """
    #  void QSqlTableModel::setEditStrategy(EditStrategy strategy)
    ritual = 'ritual_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategy'
          'E')
    self.uglySide.call(ritual, strategy.value)

  @overload(int, Qt.SortOrder)
  def setSort(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QSqlTableModel::setSort(int column, Qt::SortOrder
    order)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setSort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QSqlTableModel::setSort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(str)
  def setFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void QSqlTableModel::setFilter(const QString &filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlTableModel::setFilter(const QString &filter)
    ritual = 'ritual_ZN14QSqlTableModel9setFilterERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel9setFilterERK7QString'
    self.uglySide.call(ritual, filter)

  @overload(int, QSqlRecord)
  def setRecord(self, row: int, record: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::setRecord(int row, const QSqlRecord
    &record)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setRecord

    Parameters
    ----------

    row : int
      Passed on as it is.

    record : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlTableModel::setRecord(int row, const QSqlRecord &record)
    return self.uglySide.call(
        'ritual_ZN14QSqlTableModel9setRecordEiRK10QSqlRecord',
        row, self._valueOf(record),
    )

  @overload(QSqlIndex)
  def setPrimaryKey(self, key: QSqlIndex) -> None:
    """
    Calls Qt's 'void QSqlTableModel::setPrimaryKey(const QSqlIndex &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#setPrimaryKey

    Parameters
    ----------

    key : QSqlIndex
      Passed on as a value: Qt reads the C++ QSqlIndex, which stays Python's
      own.
    """
    #  void QSqlTableModel::setPrimaryKey(const QSqlIndex &key)
    self.uglySide.call(
        'ritual_ZN14QSqlTableModel13setPrimaryKeyERK9QSqlIndex',
        self._valueOf(key),
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
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QSqlDatabase)
  @overload(NoneType, QSqlDatabase)
  def __init__(
      self,
      parent: Optional[QObject] = None,
      db: Optional[QSqlDatabase] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlTableModel::QSqlTableModel(QObject
    *parent, const QSqlDatabase &db)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#QSqlTableModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    db : Optional[QSqlDatabase]
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own. May be left out, as in Qt: a new 'QSqlDatabase()' is then
      passed on.
    """
    #  QSqlTableModel::QSqlTableModel(QObject *parent, const QSqlDatabase
    #      &db)
    if db is None:
      from . import QSqlDatabase
      db = QSqlDatabase()
    self._noteCreation(QSqlTableModel, lambda: Rituals.call(
        'ritual_ZN14QSqlTableModelC1EP7QObjectRK12QSqlDatabase',
        self._addressOf(parent, 'QObject'), self._valueOf(db),
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

  def d_func(self) -> Optional[QSqlTableModelPrivate]:
    """
    Calls Qt's 'QSqlTableModelPrivate *QSqlTableModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#d_func

    Returns
    -------

    Optional[QSqlTableModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlTableModelPrivate *QSqlTableModel::d_func()
    address = self.uglySide.call('ritual_ZN14QSqlTableModel6d_funcEv')
    from . import QSqlTableModelPrivate
    return QSqlTableModelPrivate._cuteAt(address)

  @overload(QModelIndex)
  def clearItemData(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::clearItemData(const QModelIndex
    &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#clearItemData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QSqlTableModel::clearItemData(const QModelIndex &index)
    ritual = 'ritual_ZN14QSqlTableModel13clearItemDataERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel13clearItemDataERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(index))

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlTableModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#clear
    """
    #  void QSqlTableModel::clear()
    ritual = 'ritual_ZN14QSqlTableModel5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel5clearEv'
    self.uglySide.call(ritual)

  @overload(int, Qt.SortOrder)
  def sort(self, column: int, order: Qt.SortOrder) -> None:
    """
    Calls Qt's 'void QSqlTableModel::sort(int column, Qt::SortOrder order)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#sort

    Parameters
    ----------

    column : int
      Passed on as it is.

    order : Qt.SortOrder
      Passed on as its number.
    """
    #  void QSqlTableModel::sort(int column, Qt::SortOrder order)
    ritual = 'ritual_ZN14QSqlTableModel4sortEiN2Qt9SortOrderE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel4sortEiN2Qt9SortOrderE'
    self.uglySide.call(ritual, column, order.value)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::removeColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#removeColumns

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
    #  bool QSqlTableModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlTableModel13removeColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlTableModel13removeColumnsEiiRK11QModelIndex')
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
    Calls Qt's 'bool QSqlTableModel::removeRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#removeRows

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
    #  bool QSqlTableModel::removeRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlTableModel10removeRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel10removeRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertRows(
      self,
      row: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::insertRows(int row, int count, const
    QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#insertRows

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
    #  bool QSqlTableModel::insertRows(int row, int count, const QModelIndex
    #      &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlTableModel10insertRowsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel10insertRowsEiiRK11QModelIndex'
    return self.uglySide.call(ritual, row, count, self._valueOf(parent))

  @overload(int, QSqlRecord)
  def insertRecord(self, row: int, record: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::insertRecord(int row, const QSqlRecord
    &record)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#insertRecord

    Parameters
    ----------

    row : int
      Passed on as it is.

    record : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlTableModel::insertRecord(int row, const QSqlRecord &record)
    return self.uglySide.call(
        'ritual_ZN14QSqlTableModel12insertRecordEiRK10QSqlRecord',
        row, self._valueOf(record),
    )

  @overload(int)
  def revertRow(self, row: int) -> None:
    """
    Calls Qt's 'void QSqlTableModel::revertRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#revertRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QSqlTableModel::revertRow(int row)
    ritual = 'ritual_ZN14QSqlTableModel9revertRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel9revertRowEi'
    self.uglySide.call(ritual, row)

  def select(self) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::select()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#select
    """
    #  bool QSqlTableModel::select()
    ritual = 'ritual_ZN14QSqlTableModel6selectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel6selectEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def selectRow(self, row: int) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::selectRow(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#selectRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QSqlTableModel::selectRow(int row)
    ritual = 'ritual_ZN14QSqlTableModel9selectRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel9selectRowEi'
    return self.uglySide.call(ritual, row)

  def submit(self) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::submit()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#submit
    """
    #  bool QSqlTableModel::submit()
    ritual = 'ritual_ZN14QSqlTableModel6submitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel6submitEv'
    return self.uglySide.call(ritual)

  def revert(self) -> None:
    """
    Calls Qt's 'void QSqlTableModel::revert()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#revert
    """
    #  void QSqlTableModel::revert()
    ritual = 'ritual_ZN14QSqlTableModel6revertEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel6revertEv'
    self.uglySide.call(ritual)

  def submitAll(self) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::submitAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#submitAll
    """
    #  bool QSqlTableModel::submitAll()
    return self.uglySide.call('ritual_ZN14QSqlTableModel9submitAllEv')

  def revertAll(self) -> None:
    """
    Calls Qt's 'void QSqlTableModel::revertAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#revertAll
    """
    #  void QSqlTableModel::revertAll()
    self.uglySide.call('ritual_ZN14QSqlTableModel9revertAllEv')

  @overload(int)
  def beforeDelete(self, row: int) -> None:
    """
    Calls Qt's 'void QSqlTableModel::beforeDelete(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqltablemodel.html#beforeDelete

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QSqlTableModel::beforeDelete(int row)
    self.uglySide.call('ritual_ZN14QSqlTableModel12beforeDeleteEi', row)

  @overload(int, QSqlRecord)
  def updateRowInTable(self, row: int, values: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::updateRowInTable(int row, const
    QSqlRecord &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodel.html#updateRowInTable

    Parameters
    ----------

    row : int
      Passed on as it is.

    values : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlTableModel::updateRowInTable(int row, const QSqlRecord
    #      &values)
    ritual = 'ritual_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord')
    return self.uglySide.call(ritual, row, self._valueOf(values))

  @overload(QSqlRecord)
  def insertRowIntoTable(self, values: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::insertRowIntoTable(const QSqlRecord
    &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodel.html#insertRowIntoTable

    Parameters
    ----------

    values : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlTableModel::insertRowIntoTable(const QSqlRecord &values)
    ritual = 'ritual_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord')
    return self.uglySide.call(ritual, self._valueOf(values))

  @overload(int)
  def deleteRowFromTable(self, row: int) -> bool:
    """
    Calls Qt's 'bool QSqlTableModel::deleteRowFromTable(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqltablemodel.html#deleteRowFromTable

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QSqlTableModel::deleteRowFromTable(int row)
    ritual = 'ritual_ZN14QSqlTableModel18deleteRowFromTableEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlTableModel18deleteRowFromTableEi'
    return self.uglySide.call(ritual, row)

  @staticmethod
  def beforeInsert(*__, **_) -> Never:
    """
    Qt's 'void QSqlTableModel::beforeInsert(QSqlRecord &record)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlTableModel.beforeInsert' has no cute function yet. Qt's 'void "
        "QSqlTableModel::beforeInsert(QSqlRecord &record)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def beforeUpdate(*__, **_) -> Never:
    """
    Qt's 'void QSqlTableModel::beforeUpdate(int row, QSqlRecord &record)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlTableModel.beforeUpdate' has no cute function yet. Qt's 'void "
        "QSqlTableModel::beforeUpdate(int row, QSqlRecord &record)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def primeInsert(*__, **_) -> Never:
    """
    Qt's 'void QSqlTableModel::primeInsert(int row, QSqlRecord &record)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlTableModel.primeInsert' has no cute function yet. Qt's 'void "
        "QSqlTableModel::primeInsert(int row, QSqlRecord &record)': takes a "
        "type Python has no way to hand over yet.")
