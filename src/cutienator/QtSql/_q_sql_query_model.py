"""
QSqlQueryModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlquerymodel.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QAbstractTableModel, QHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QSqlDatabase, QSqlError, QSqlQuery, QSqlQueryModelPrivate
  from . import QSqlRecord
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QSqlDatabase = WAIT['QSqlDatabase']
  QSqlError = WAIT['QSqlError']
  QSqlQuery = WAIT['QSqlQuery']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlQueryModel(QAbstractTableModel):
  """
  The cute side of Qt's QSqlQueryModel: a plain Python object standing in
  front of one C++ QSqlQueryModel.

  It is built on the cute 'QAbstractTableModel', as Qt's QSqlQueryModel is
  built on Qt's QAbstractTableModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlQueryModel that has a ritual and that Python can
  call so far, 32 names in all: 'metaObject', 'tr', 'd_func', 'rowCount',
  'columnCount', 'record', 'data', 'headerData', 'setHeaderData',
  'insertColumns', 'removeColumns', 'setQuery', 'refresh', 'query', 'clear',
  'lastError', 'fetchMore', 'canFetchMore', 'roleNames', 'beginInsertRows',
  'endInsertRows', 'beginRemoveRows', 'endRemoveRows', 'beginInsertColumns',
  'endInsertColumns', 'beginRemoveColumns', 'endRemoveColumns',
  'beginResetModel', 'endResetModel', 'queryChange', 'indexInQuery',
  'setLastError'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSqlQueryModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSqlQueryModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSqlQueryModelPrivate *QSqlQueryModel::d_func() const': takes
    in Python what 'QSqlQueryModelPrivate *QSqlQueryModel::d_func()' takes.
  - Qt's 'QSqlQueryModel::~QSqlQueryModel()': the destructor: Python never
    removes a C++ QSqlQueryModel.
  - Qt's 'void QSqlQueryModel::setQuery(QSqlQuery &&query)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QSqlQueryModel::QSqlQueryModel(QSqlQueryModelPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 43 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSqlQueryModel is created at the first use, not by
    'QSqlQueryModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlQueryModel.
  - Qt tells when it has removed the C++ QSqlQueryModel. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QSqlQueryModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#tr

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
    #  QString QSqlQueryModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QSqlQueryModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlQueryModel'

  #  A C++ QSqlQueryModel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlQueryModel'

  #  The functions Qt calls itself that QSqlQueryModel is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clear': (
          ('_ZN14QSqlQueryModel5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'queryChange': (
          ('_ZN14QSqlQueryModel11queryChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'indexInQuery': (
          ('_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
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
    Calls Qt's 'const QMetaObject *QSqlQueryModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSqlQueryModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QSqlQueryModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QSqlQueryModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QSqlQueryModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QSqlQueryModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlQueryModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload()
  @overload(QModelIndex)
  def columnCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QSqlQueryModel::columnCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#columnCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QSqlQueryModel::columnCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QSqlQueryModel11columnCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlQueryModel11columnCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(int)
  def record(self, row: int) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlQueryModel::record(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#record

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlQueryModel::record(int row) const
    address = self.uglySide.call('ritual_ZNK14QSqlQueryModel6recordEi', row)
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload()
  def record(self) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlQueryModel::record() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#record

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlQueryModel::record() const
    address = self.uglySide.call('ritual_ZNK14QSqlQueryModel6recordEv')
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, item: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQueryModel::data(const QModelIndex &item, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#data

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
    #  QVariant QSqlQueryModel::data(const QModelIndex &item, int role) const
    ritual = 'ritual_ZNK14QSqlQueryModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlQueryModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(item), role)
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
    Calls Qt's 'QVariant QSqlQueryModel::headerData(int section,
    Qt::Orientation orientation, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#headerData

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
    #  QVariant QSqlQueryModel::headerData(int section, Qt::Orientation
    #      orientation, int role) const
    ritual = 'ritual_ZNK14QSqlQueryModel10headerDataEiN2Qt11OrientationEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QSqlQueryModel10headerDataEiN2Qt11OrientationEi')
    address = self.uglySide.call(ritual, section, orientation.value, role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(WAIT['Qt.Disambiguated_t'])
  def query(self, a0: Qt.Disambiguated_t) -> QSqlQuery:
    """
    Calls Qt's 'const QSqlQuery &QSqlQueryModel::query(Qt::Disambiguated_t
    a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#query

    Parameters
    ----------

    a0 : Qt.Disambiguated_t
      Passed on as a value: Qt reads the C++ Qt::Disambiguated_t, which stays
      Python's own.

    Returns
    -------

    QSqlQuery
      A new cute QSqlQuery around the copy Qt gave back. Python owns it.
    """
    #  const QSqlQuery &QSqlQueryModel::query(Qt::Disambiguated_t a0) const
    address = self.uglySide.call(
        'ritual_ZNK14QSqlQueryModel5queryEN2Qt15Disambiguated_tE',
        self._valueOf(a0),
    )
    from . import QSqlQuery
    return QSqlQuery._cuteOwning(address)

  def lastError(self) -> QSqlError:
    """
    Calls Qt's 'QSqlError QSqlQueryModel::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#lastError

    Returns
    -------

    QSqlError
      A new cute QSqlError around the copy Qt gave back. Python owns it.
    """
    #  QSqlError QSqlQueryModel::lastError() const
    address = self.uglySide.call('ritual_ZNK14QSqlQueryModel9lastErrorEv')
    from . import QSqlError
    return QSqlError._cuteOwning(address)

  @overload()
  @overload(QModelIndex)
  def canFetchMore(self, parent: Optional[QModelIndex] = None) -> bool:
    """
    Calls Qt's 'bool QSqlQueryModel::canFetchMore(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#canFetchMore

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  bool QSqlQueryModel::canFetchMore(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK14QSqlQueryModel12canFetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlQueryModel12canFetchMoreERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QSqlQueryModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QSqlQueryModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK14QSqlQueryModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex)
  def indexInQuery(self, item: QModelIndex) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QSqlQueryModel::indexInQuery(const QModelIndex
    &item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#indexInQuery

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
    #  QModelIndex QSqlQueryModel::indexInQuery(const QModelIndex &item)
    #      const
    ritual = 'ritual_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(item))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'bool QSqlQueryModel::setHeaderData(int section,
    Qt::Orientation orientation, const QVariant &value, int role)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#setHeaderData

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
    #  bool QSqlQueryModel::setHeaderData(int section, Qt::Orientation
    #      orientation, const QVariant &value, int role)
    ritual = (
        'ritual_ZN14QSqlQueryModel13setHeaderDataEiN2Qt11OrientationERK8QVa'
        'rianti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlQueryModel13setHeaderDataEiN2Qt11OrientationE'
          'RK8QVarianti')
    return self.uglySide.call(
        ritual, section, orientation.value, self._valueOf(value), role,
    )

  @overload(QSqlQuery)
  def setQuery(self, query: QSqlQuery) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::setQuery(const QSqlQuery &query)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#setQuery

    Parameters
    ----------

    query : QSqlQuery
      Passed on as a value: Qt reads the C++ QSqlQuery, which stays Python's
      own.
    """
    #  void QSqlQueryModel::setQuery(const QSqlQuery &query)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel8setQueryERK9QSqlQuery',
        self._valueOf(query),
    )

  @overload(str)
  @overload(str, QSqlDatabase)
  def setQuery(self, query: str, db: Optional[QSqlDatabase] = None) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::setQuery(const QString &query, const
    QSqlDatabase &db)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#setQuery

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.

    db : Optional[QSqlDatabase]
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own. May be left out, as in Qt: a new 'QSqlDatabase()' is then
      passed on.
    """
    #  void QSqlQueryModel::setQuery(const QString &query, const QSqlDatabase
    #      &db)
    if db is None:
      from . import QSqlDatabase
      db = QSqlDatabase()
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel8setQueryERK7QStringRK12QSqlDatabase',
        query, self._valueOf(db),
    )

  @overload(QSqlError)
  def setLastError(self, error: QSqlError) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::setLastError(const QSqlError &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#setLastError

    Parameters
    ----------

    error : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  void QSqlQueryModel::setLastError(const QSqlError &error)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel12setLastErrorERK9QSqlError',
        self._valueOf(error),
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
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSqlQueryModel::QSqlQueryModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#QSqlQueryModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSqlQueryModel::QSqlQueryModel(QObject *parent)
    self._noteCreation(QSqlQueryModel, lambda: Rituals.call(
        'ritual_ZN14QSqlQueryModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QSqlQueryModelPrivate]:
    """
    Calls Qt's 'QSqlQueryModelPrivate *QSqlQueryModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#d_func

    Returns
    -------

    Optional[QSqlQueryModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlQueryModelPrivate *QSqlQueryModel::d_func()
    address = self.uglySide.call('ritual_ZN14QSqlQueryModel6d_funcEv')
    from . import QSqlQueryModelPrivate
    return QSqlQueryModelPrivate._cuteAt(address)

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def insertColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlQueryModel::insertColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#insertColumns

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
    #  bool QSqlQueryModel::insertColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlQueryModel13insertColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlQueryModel13insertColumnsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  @overload(int, int)
  @overload(int, int, QModelIndex)
  def removeColumns(
      self,
      column: int,
      count: int,
      parent: Optional[QModelIndex] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlQueryModel::removeColumns(int column, int count,
    const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#removeColumns

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
    #  bool QSqlQueryModel::removeColumns(int column, int count, const
    #      QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlQueryModel13removeColumnsEiiRK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QSqlQueryModel13removeColumnsEiiRK11QModelIndex')
    return self.uglySide.call(ritual, column, count, self._valueOf(parent))

  def refresh(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#refresh
    """
    #  void QSqlQueryModel::refresh()
    self.uglySide.call('ritual_ZN14QSqlQueryModel7refreshEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#clear
    """
    #  void QSqlQueryModel::clear()
    ritual = 'ritual_ZN14QSqlQueryModel5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlQueryModel5clearEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(QModelIndex)
  def fetchMore(self, parent: Optional[QModelIndex] = None) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::fetchMore(const QModelIndex &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#fetchMore

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  void QSqlQueryModel::fetchMore(const QModelIndex &parent)
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZN14QSqlQueryModel9fetchMoreERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlQueryModel9fetchMoreERK11QModelIndex'
    self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int, int)
  def beginInsertRows(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::beginInsertRows(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#beginInsertRows

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QSqlQueryModel::beginInsertRows(const QModelIndex &parent, int
    #      first, int last)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel15beginInsertRowsERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  def endInsertRows(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::endInsertRows()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#endInsertRows
    """
    #  void QSqlQueryModel::endInsertRows()
    self.uglySide.call('ritual_ZN14QSqlQueryModel13endInsertRowsEv')

  @overload(QModelIndex, int, int)
  def beginRemoveRows(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::beginRemoveRows(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#beginRemoveRows

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QSqlQueryModel::beginRemoveRows(const QModelIndex &parent, int
    #      first, int last)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel15beginRemoveRowsERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  def endRemoveRows(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::endRemoveRows()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#endRemoveRows
    """
    #  void QSqlQueryModel::endRemoveRows()
    self.uglySide.call('ritual_ZN14QSqlQueryModel13endRemoveRowsEv')

  @overload(QModelIndex, int, int)
  def beginInsertColumns(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::beginInsertColumns(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#beginInsertColumns

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QSqlQueryModel::beginInsertColumns(const QModelIndex &parent, int
    #      first, int last)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel18beginInsertColumnsERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  def endInsertColumns(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::endInsertColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#endInsertColumns
    """
    #  void QSqlQueryModel::endInsertColumns()
    self.uglySide.call('ritual_ZN14QSqlQueryModel16endInsertColumnsEv')

  @overload(QModelIndex, int, int)
  def beginRemoveColumns(
      self,
      parent: QModelIndex,
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::beginRemoveColumns(const QModelIndex
    &parent, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#beginRemoveColumns

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QSqlQueryModel::beginRemoveColumns(const QModelIndex &parent, int
    #      first, int last)
    self.uglySide.call(
        'ritual_ZN14QSqlQueryModel18beginRemoveColumnsERK11QModelIndexii',
        self._valueOf(parent), first, last,
    )

  def endRemoveColumns(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::endRemoveColumns()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#endRemoveColumns
    """
    #  void QSqlQueryModel::endRemoveColumns()
    self.uglySide.call('ritual_ZN14QSqlQueryModel16endRemoveColumnsEv')

  def beginResetModel(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::beginResetModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquerymodel.html#beginResetModel
    """
    #  void QSqlQueryModel::beginResetModel()
    self.uglySide.call('ritual_ZN14QSqlQueryModel15beginResetModelEv')

  def endResetModel(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::endResetModel()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#endResetModel
    """
    #  void QSqlQueryModel::endResetModel()
    self.uglySide.call('ritual_ZN14QSqlQueryModel13endResetModelEv')

  def queryChange(self) -> None:
    """
    Calls Qt's 'void QSqlQueryModel::queryChange()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquerymodel.html#queryChange
    """
    #  void QSqlQueryModel::queryChange()
    ritual = 'ritual_ZN14QSqlQueryModel11queryChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlQueryModel11queryChangeEv'
    self.uglySide.call(ritual)
