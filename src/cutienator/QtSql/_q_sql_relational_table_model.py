"""
QSqlRelationalTableModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlrelationaltablemodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSqlTableModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QVariant
  from . import QSqlDatabase, QSqlRecord, QSqlRelation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QSqlDatabase = WAIT['QSqlDatabase']
  QSqlRecord = WAIT['QSqlRecord']
  QSqlRelation = WAIT['QSqlRelation']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlRelationalTableModel(QSqlTableModel):
  """
  The cute side of Qt's QSqlRelationalTableModel: a plain Python object
  standing in front of one C++ QSqlRelationalTableModel.

  It is built on the cute 'QSqlTableModel', as Qt's QSqlRelationalTableModel
  is built on Qt's QSqlTableModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlRelationalTableModel that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'data',
  'setData', 'removeColumns', 'clear', 'select', 'setTable', 'setRelation',
  'relation', 'relationModel', 'setJoinMode', 'revertRow', 'selectStatement',
  'updateRowInTable', 'insertRowIntoTable', 'orderByClause'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSqlRelationalTableModel::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QSqlRelationalTableModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSqlRelationalTableModel::~QSqlRelationalTableModel()': the
    destructor: Python never removes a C++ QSqlRelationalTableModel.
  - Qt's 'QSqlRelationalTableModelPrivate
    *QSqlRelationalTableModel::d_func()': gives
    'QSqlRelationalTableModelPrivate', which has no cute class yet.
  - Qt's 'const QSqlRelationalTableModelPrivate
    *QSqlRelationalTableModel::d_func() const': gives
    'QSqlRelationalTableModelPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSqlRelationalTableModel is created at the first use, not by
    'QSqlRelationalTableModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlRelationalTableModel.
  - Qt tells when it has removed the C++ QSqlRelationalTableModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSqlRelationalTableModel, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class JoinMode(CuteNum):
    """
    The enum 'QSqlRelationalTableModel::JoinMode' of Qt, with the 2 names Qt
    gives in it.
    """

    InnerJoin = Kee[int](0)
    LeftJoin = Kee[int](1)

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
    Calls Qt's 'QString QSqlRelationalTableModel::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#tr

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
    #  QString QSqlRelationalTableModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QSqlRelationalTableModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlRelationalTableModel'

  #  A C++ QSqlRelationalTableModel Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlRelationalTableModel'

  #  The functions Qt calls itself that QSqlRelationalTableModel is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRelation': (
          ('_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRelation',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtSql:QSqlRelation'),
           )),
      ),
      'relationModel': (
          ('_ZNK24QSqlRelationalTableModel13relationModelEi',
           ('address', 'address', 'QtSql:QSqlTableModel'),
           (
               ('int', 'number', ''),
           )),
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
    Calls Qt's 'const QMetaObject *QSqlRelationalTableModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSqlRelationalTableModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QSqlRelationalTableModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, item: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlRelationalTableModel::data(const QModelIndex
    &item, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#data

    Parameters
    ----------

    item : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlRelationalTableModel::data(const QModelIndex &item, int
    #      role) const
    ritual = 'ritual_ZNK24QSqlRelationalTableModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QSqlRelationalTableModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(item), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def relation(self, column: int) -> QSqlRelation:
    """
    Calls Qt's 'QSqlRelation QSqlRelationalTableModel::relation(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#relation

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    QSqlRelation
      A new cute QSqlRelation around the copy Qt gave back. Python owns it.
    """
    #  QSqlRelation QSqlRelationalTableModel::relation(int column) const
    address = self.uglySide.call(
        'ritual_ZNK24QSqlRelationalTableModel8relationEi', column,
    )
    from . import QSqlRelation
    return QSqlRelation._cuteOwning(address)

  @overload(int)
  def relationModel(self, column: int) -> Optional[QSqlTableModel]:
    """
    Calls Qt's 'QSqlTableModel *QSqlRelationalTableModel::relationModel(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#relationModel

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QSqlTableModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlTableModel *QSqlRelationalTableModel::relationModel(int column)
    #      const
    ritual = 'ritual_ZNK24QSqlRelationalTableModel13relationModelEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSqlRelationalTableModel13relationModelEi'
    address = self.uglySide.call(ritual, column)
    return QSqlTableModel._cuteAt(address)

  def selectStatement(self) -> str:
    """
    Calls Qt's 'QString QSqlRelationalTableModel::selectStatement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#selectStatement

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRelationalTableModel::selectStatement() const
    ritual = 'ritual_ZNK24QSqlRelationalTableModel15selectStatementEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSqlRelationalTableModel15selectStatementEv'
    return self.uglySide.call(ritual)

  def orderByClause(self) -> str:
    """
    Calls Qt's 'QString QSqlRelationalTableModel::orderByClause() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#orderByClause

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlRelationalTableModel::orderByClause() const
    ritual = 'ritual_ZNK24QSqlRelationalTableModel13orderByClauseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSqlRelationalTableModel13orderByClauseEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      item: QModelIndex,
      value: QVariant,
      role: int = 2,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlRelationalTableModel::setData(const QModelIndex
    &item, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#setData

    Parameters
    ----------

    item : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 2.
    """
    #  bool QSqlRelationalTableModel::setData(const QModelIndex &item, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN24QSqlRelationalTableModel7setDataERK11QModelIndexRK8QVar'
        'ianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSqlRelationalTableModel7setDataERK11QModelIndexR'
          'K8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(item), self._valueOf(value), role,
    )

  @overload(str)
  def setTable(self, tableName: str) -> None:
    """
    Calls Qt's 'void QSqlRelationalTableModel::setTable(const QString
    &tableName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#setTable

    Parameters
    ----------

    tableName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlRelationalTableModel::setTable(const QString &tableName)
    ritual = 'ritual_ZN24QSqlRelationalTableModel8setTableERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSqlRelationalTableModel8setTableERK7QString'
    self.uglySide.call(ritual, tableName)

  @overload(int, QSqlRelation)
  def setRelation(self, column: int, relation: QSqlRelation) -> None:
    """
    Calls Qt's 'void QSqlRelationalTableModel::setRelation(int column, const
    QSqlRelation &relation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#setRelation

    Parameters
    ----------

    column : int
      Passed on as it is.

    relation : QSqlRelation
      Passed on as a value: Qt reads the C++ QSqlRelation, which stays
      Python's own.
    """
    #  void QSqlRelationalTableModel::setRelation(int column, const
    #      QSqlRelation &relation)
    ritual = (
        'ritual_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRelation')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRe'
          'lation')
    self.uglySide.call(ritual, column, self._valueOf(relation))

  @overload(JoinMode)
  def setJoinMode(self, joinMode: JoinMode) -> None:
    """
    Calls Qt's 'void
    QSqlRelationalTableModel::setJoinMode(QSqlRelationalTableModel::JoinMode
    joinMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#setJoinMode

    Parameters
    ----------

    joinMode : JoinMode
      Passed on as its number.
    """
    #  void QSqlRelationalTableModel::setJoinMode(QSqlRelationalTableModel::
    #      JoinMode joinMode)
    self.uglySide.call(
        'ritual_ZN24QSqlRelationalTableModel11setJoinModeENS_8JoinModeE',
        joinMode.value,
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
    Notes what was given, for Qt's
    'QSqlRelationalTableModel::QSqlRelationalTableModel(QObject *parent,
    const QSqlDatabase &db)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html

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
    #  QSqlRelationalTableModel::QSqlRelationalTableModel(QObject *parent,
    #      const QSqlDatabase &db)
    if db is None:
      from . import QSqlDatabase
      db = QSqlDatabase()
    self._noteCreation(QSqlRelationalTableModel, lambda: Rituals.call(
        'ritual_ZN24QSqlRelationalTableModelC1EP7QObjectRK12QSqlDatabase',
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

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlRelationalTableModel::removeColumns(int column, int
    count, const QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#removeColumns

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
    #  bool QSqlRelationalTableModel::removeColumns(int column, int count,
    #      const QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = (
        'ritual_ZN24QSqlRelationalTableModel13removeColumnsEiiRK11QModelInd'
        'ex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSqlRelationalTableModel13removeColumnsEiiRK11QMo'
          'delIndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlRelationalTableModel::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#clear
    """
    #  void QSqlRelationalTableModel::clear()
    ritual = 'ritual_ZN24QSqlRelationalTableModel5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSqlRelationalTableModel5clearEv'
    self.uglySide.call(ritual)

  def select(self) -> bool:
    """
    Calls Qt's 'bool QSqlRelationalTableModel::select()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#select
    """
    #  bool QSqlRelationalTableModel::select()
    ritual = 'ritual_ZN24QSqlRelationalTableModel6selectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSqlRelationalTableModel6selectEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def revertRow(self, row: int) -> None:
    """
    Calls Qt's 'void QSqlRelationalTableModel::revertRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#revertRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QSqlRelationalTableModel::revertRow(int row)
    ritual = 'ritual_ZN24QSqlRelationalTableModel9revertRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSqlRelationalTableModel9revertRowEi'
    self.uglySide.call(ritual, row)

  @overload(int, QSqlRecord)
  def updateRowInTable(self, row: int, values: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlRelationalTableModel::updateRowInTable(int row,
    const QSqlRecord &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#updateRowInTable

    Parameters
    ----------

    row : int
      Passed on as it is.

    values : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlRelationalTableModel::updateRowInTable(int row, const
    #      QSqlRecord &values)
    ritual = (
        'ritual_ZN24QSqlRelationalTableModel16updateRowInTableEiRK10QSqlRec'
        'ord')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSqlRelationalTableModel16updateRowInTableEiRK10Q'
          'SqlRecord')
    return self.uglySide.call(ritual, row, self._valueOf(values))

  @overload(QSqlRecord)
  def insertRowIntoTable(self, values: QSqlRecord) -> bool:
    """
    Calls Qt's 'bool QSqlRelationalTableModel::insertRowIntoTable(const
    QSqlRecord &values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html#insertRowIntoTable

    Parameters
    ----------

    values : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.
    """
    #  bool QSqlRelationalTableModel::insertRowIntoTable(const QSqlRecord
    #      &values)
    ritual = (
        'ritual_ZN24QSqlRelationalTableModel18insertRowIntoTableERK10QSqlRe'
        'cord')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QSqlRelationalTableModel18insertRowIntoTableERK10'
          'QSqlRecord')
    return self.uglySide.call(ritual, self._valueOf(values))
