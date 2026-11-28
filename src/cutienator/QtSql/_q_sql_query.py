"""
QSqlQuery binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlquery.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QSql

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QSqlDatabase, QSqlDriver, QSqlError, QSqlRecord, QSqlResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlDatabase = WAIT['QSqlDatabase']
  QSqlResult = WAIT['QSqlResult']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlQuery(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlQuery: a plain Python object standing in front of
  one C++ QSqlQuery.

  C++ hands a QSqlQuery around as a copy, so every C++ QSqlQuery behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlQuery that has a ritual and that Python can call
  so far, 38 names in all: 'isValid', 'isActive', 'isNull', 'at',
  'lastQuery', 'numRowsAffected', 'lastError', 'isSelect', 'size', 'driver',
  'result', 'isForwardOnly', 'record', 'setForwardOnly', 'exec', 'value',
  'setNumericalPrecisionPolicy', 'numericalPrecisionPolicy',
  'setPositionalBindingEnabled', 'isPositionalBindingEnabled', 'seek',
  'next', 'previous', 'first', 'last', 'clear', 'execBatch', 'prepare',
  'bindValue', 'addBindValue', 'boundValue', 'boundValues',
  'boundValueNames', 'boundValueName', 'executedQuery', 'lastInsertId',
  'finish', 'nextResult'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlQuery &QSqlQuery::operator=(const QSqlQuery &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSqlQuery::QSqlQuery(QSqlQuery &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSqlQuery &QSqlQuery::operator=(QSqlQuery &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSqlQuery::~QSqlQuery()': the destructor: Python removes its C++
    QSqlQuery by it, and has no other use for it.
  - Qt's 'void QSqlQuery::swap(QSqlQuery &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 55 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSqlQuery is created at the first use, not by 'QSqlQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlQuery back gives a copy the ritual made for
    Python, in a new cute QSqlQuery.
  - Each name of Qt's QSqlQuery that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSqlQuery, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class BatchExecutionMode(CuteNum):
    """
    The enum 'QSqlQuery::BatchExecutionMode' of Qt, with the 2 names Qt gives
    in it.
    """

    ValuesAsRows = Kee[int](0)
    ValuesAsColumns = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlQuery'

  #  Qt's '~QSqlQuery()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlQuery behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSqlQueryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isValid
    """
    #  bool QSqlQuery::isValid() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery7isValidEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isActive
    """
    #  bool QSqlQuery::isActive() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery8isActiveEv')

  @overload(int)
  def isNull(self, field: int) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isNull(int field) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isNull

    Parameters
    ----------

    field : int
      Passed on as it is.
    """
    #  bool QSqlQuery::isNull(int field) const
    return self.uglySide.call('ritual_ZNK9QSqlQuery6isNullEi', field)

  @overload(str)
  def isNull(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isNull(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isNull

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlQuery::isNull(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK9QSqlQuery6isNullE14QAnyStringView', name,
    )

  def at(self) -> int:
    """
    Calls Qt's 'int QSqlQuery::at() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#at
    """
    #  int QSqlQuery::at() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery2atEv')

  def lastQuery(self) -> str:
    """
    Calls Qt's 'QString QSqlQuery::lastQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#lastQuery

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlQuery::lastQuery() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery9lastQueryEv')

  def numRowsAffected(self) -> int:
    """
    Calls Qt's 'int QSqlQuery::numRowsAffected() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#numRowsAffected
    """
    #  int QSqlQuery::numRowsAffected() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery15numRowsAffectedEv')

  def lastError(self) -> QSqlError:
    """
    Calls Qt's 'QSqlError QSqlQuery::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#lastError

    Returns
    -------

    QSqlError
      A new cute QSqlError around the copy Qt gave back. Python owns it.
    """
    #  QSqlError QSqlQuery::lastError() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery9lastErrorEv')
    from . import QSqlError
    return QSqlError._cuteOwning(address)

  def isSelect(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isSelect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isSelect
    """
    #  bool QSqlQuery::isSelect() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery8isSelectEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QSqlQuery::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#size
    """
    #  int QSqlQuery::size() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery4sizeEv')

  def driver(self) -> Optional[QSqlDriver]:
    """
    Calls Qt's 'const QSqlDriver *QSqlQuery::driver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#driver

    Returns
    -------

    Optional[QSqlDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSqlDriver *QSqlQuery::driver() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery6driverEv')
    from . import QSqlDriver
    return QSqlDriver._cuteAt(address)

  def result(self) -> Optional[QSqlResult]:
    """
    Calls Qt's 'const QSqlResult *QSqlQuery::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#result

    Returns
    -------

    Optional[QSqlResult]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSqlResult *QSqlQuery::result() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery6resultEv')
    from . import QSqlResult
    return QSqlResult._cuteAt(address)

  def isForwardOnly(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isForwardOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#isForwardOnly
    """
    #  bool QSqlQuery::isForwardOnly() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery13isForwardOnlyEv')

  def record(self) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlQuery::record() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#record

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlQuery::record() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery6recordEv')
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(int)
  def value(self, i: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQuery::value(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#value

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlQuery::value(int i) const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery5valueEi', i)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def value(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQuery::value(QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlQuery::value(QAnyStringView name) const
    address = self.uglySide.call(
        'ritual_ZNK9QSqlQuery5valueE14QAnyStringView', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy:
    """
    Calls Qt's 'QSql::NumericalPrecisionPolicy
    QSqlQuery::numericalPrecisionPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquery.html#numericalPrecisionPolicy

    Returns
    -------

    QSql.NumericalPrecisionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSql.NumericalPrecisionPolicy(number)' gives.
    """
    #  QSql::NumericalPrecisionPolicy QSqlQuery::numericalPrecisionPolicy()
    #      const
    return QSql.NumericalPrecisionPolicy(self.uglySide.call(
        'ritual_ZNK9QSqlQuery24numericalPrecisionPolicyEv',
    ))

  def isPositionalBindingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::isPositionalBindingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquery.html#isPositionalBindingEnabled
    """
    #  bool QSqlQuery::isPositionalBindingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK9QSqlQuery26isPositionalBindingEnabledEv',
    )

  @overload(str)
  def boundValue(self, placeholder: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQuery::boundValue(const QString &placeholder)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#boundValue

    Parameters
    ----------

    placeholder : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlQuery::boundValue(const QString &placeholder) const
    address = self.uglySide.call(
        'ritual_ZNK9QSqlQuery10boundValueERK7QString', placeholder,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def boundValue(self, pos: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQuery::boundValue(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#boundValue

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlQuery::boundValue(int pos) const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery10boundValueEi', pos)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def boundValues(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QSqlQuery::boundValues() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#boundValues

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QSqlQuery::boundValues() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery11boundValuesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def boundValueNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSqlQuery::boundValueNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#boundValueNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlQuery::boundValueNames() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery15boundValueNamesEv')
    return QStringList._cuteOwning(address)

  @overload(int)
  def boundValueName(self, pos: int) -> str:
    """
    Calls Qt's 'QString QSqlQuery::boundValueName(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#boundValueName

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlQuery::boundValueName(int pos) const
    return self.uglySide.call('ritual_ZNK9QSqlQuery14boundValueNameEi', pos)

  def executedQuery(self) -> str:
    """
    Calls Qt's 'QString QSqlQuery::executedQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#executedQuery

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlQuery::executedQuery() const
    return self.uglySide.call('ritual_ZNK9QSqlQuery13executedQueryEv')

  def lastInsertId(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlQuery::lastInsertId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#lastInsertId

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlQuery::lastInsertId() const
    address = self.uglySide.call('ritual_ZNK9QSqlQuery12lastInsertIdEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setForwardOnly(self, forward: bool) -> None:
    """
    Calls Qt's 'void QSqlQuery::setForwardOnly(bool forward)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#setForwardOnly

    Parameters
    ----------

    forward : bool
      Passed on as it is.
    """
    #  void QSqlQuery::setForwardOnly(bool forward)
    self.uglySide.call('ritual_ZN9QSqlQuery14setForwardOnlyEb', forward)

  @overload(QSql.NumericalPrecisionPolicy)
  def setNumericalPrecisionPolicy(
      self,
      precisionPolicy: QSql.NumericalPrecisionPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QSqlQuery::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy
    precisionPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquery.html#setNumericalPrecisionPolicy

    Parameters
    ----------

    precisionPolicy : QSql.NumericalPrecisionPolicy
      Passed on as its number.
    """
    #  void QSqlQuery::setNumericalPrecisionPolicy(QSql::
    #      NumericalPrecisionPolicy precisionPolicy)
    self.uglySide.call(
        'ritual_ZN9QSqlQuery27setNumericalPrecisionPolicyEN4QSql24Numerical'
        'PrecisionPolicyE',
        precisionPolicy.value,
    )

  @overload(bool)
  def setPositionalBindingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSqlQuery::setPositionalBindingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlquery.html#setPositionalBindingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSqlQuery::setPositionalBindingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN9QSqlQuery27setPositionalBindingEnabledEb', enable,
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

  @overload(QSqlResult)
  @overload(NoneType)
  def __init__(self, r: Optional[QSqlResult]) -> None:
    """
    Notes what was given, for Qt's 'QSqlQuery::QSqlQuery(QSqlResult *r)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#QSqlQuery

    Parameters
    ----------

    r : Optional[QSqlResult]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSqlQuery::QSqlQuery(QSqlResult *r)
    self._noteCreation(QSqlQuery, lambda: Rituals.call(
        'ritual_ZN9QSqlQueryC1EP10QSqlResult', self._addressOf(r),
    ))

  @overload()
  @overload(str)
  @overload(str, QSqlDatabase)
  def __init__(
      self,
      query: str = '',
      db: Optional[QSqlDatabase] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlQuery::QSqlQuery(const QString
    &query, const QSqlDatabase &db)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#QSqlQuery

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    db : Optional[QSqlDatabase]
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own. May be left out, as in Qt: a new 'QSqlDatabase()' is then
      passed on.
    """
    #  QSqlQuery::QSqlQuery(const QString &query, const QSqlDatabase &db)
    if db is None:
      from . import QSqlDatabase
      db = QSqlDatabase()
    self._noteCreation(QSqlQuery, lambda: Rituals.call(
        'ritual_ZN9QSqlQueryC1ERK7QStringRK12QSqlDatabase',
        query, self._valueOf(db),
    ))

  @overload(QSqlDatabase)
  def __init__(self, db: QSqlDatabase) -> None:
    """
    Notes what was given, for Qt's 'QSqlQuery::QSqlQuery(const QSqlDatabase
    &db)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#QSqlQuery

    Parameters
    ----------

    db : QSqlDatabase
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own.
    """
    #  QSqlQuery::QSqlQuery(const QSqlDatabase &db)
    self._noteCreation(QSqlQuery, lambda: Rituals.call(
        'ritual_ZN9QSqlQueryC1ERK12QSqlDatabase', self._valueOf(db),
    ))

  @overload(THIS)
  def __init__(self, other: QSqlQuery) -> None:
    """
    Notes what was given, for Qt's 'QSqlQuery::QSqlQuery(const QSqlQuery
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#QSqlQuery

    Parameters
    ----------

    other : QSqlQuery
      Passed on as a value: Qt reads the C++ QSqlQuery, which stays Python's
      own.
    """
    #  QSqlQuery::QSqlQuery(const QSqlQuery &other)
    self._noteCreation(QSqlQuery, lambda: Rituals.call(
        'ritual_ZN9QSqlQueryC1ERKS_', self._valueOf(other),
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

  @overload(str)
  def exec(self, query: str) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::exec(const QString &query)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#exec

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlQuery::exec(const QString &query)
    return self.uglySide.call('ritual_ZN9QSqlQuery4execERK7QString', query)

  @overload()
  def exec(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#exec
    """
    #  bool QSqlQuery::exec()
    return self.uglySide.call('ritual_ZN9QSqlQuery4execEv')

  @overload(int)
  @overload(int, bool)
  def seek(self, i: int, relative: bool = False) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::seek(int i, bool relative)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#seek

    Parameters
    ----------

    i : int
      Passed on as it is.

    relative : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QSqlQuery::seek(int i, bool relative)
    return self.uglySide.call('ritual_ZN9QSqlQuery4seekEib', i, relative)

  def next(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#next
    """
    #  bool QSqlQuery::next()
    return self.uglySide.call('ritual_ZN9QSqlQuery4nextEv')

  def previous(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::previous()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#previous
    """
    #  bool QSqlQuery::previous()
    return self.uglySide.call('ritual_ZN9QSqlQuery8previousEv')

  def first(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::first()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#first
    """
    #  bool QSqlQuery::first()
    return self.uglySide.call('ritual_ZN9QSqlQuery5firstEv')

  def last(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::last()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#last
    """
    #  bool QSqlQuery::last()
    return self.uglySide.call('ritual_ZN9QSqlQuery4lastEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlQuery::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#clear
    """
    #  void QSqlQuery::clear()
    self.uglySide.call('ritual_ZN9QSqlQuery5clearEv')

  @overload()
  @overload(BatchExecutionMode)
  def execBatch(
      self,
      mode: BatchExecutionMode = BatchExecutionMode.ValuesAsRows,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::execBatch(BatchExecutionMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#execBatch

    Parameters
    ----------

    mode : BatchExecutionMode
      Passed on as its number. May be left out, as in Qt: it is then
      BatchExecutionMode.ValuesAsRows.
    """
    #  bool QSqlQuery::execBatch(BatchExecutionMode mode)
    return self.uglySide.call(
        'ritual_ZN9QSqlQuery9execBatchENS_18BatchExecutionModeE', mode.value,
    )

  @overload(str)
  def prepare(self, query: str) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::prepare(const QString &query)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#prepare

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlQuery::prepare(const QString &query)
    return self.uglySide.call(
        'ritual_ZN9QSqlQuery7prepareERK7QString', query,
    )

  @overload(str, QVariant)
  @overload(str, QVariant, QSql.ParamType)
  def bindValue(
      self,
      placeholder: str,
      val: QVariant,
      type: QSql.ParamType = QSql.ParamType.In,
  ) -> None:
    """
    Calls Qt's 'void QSqlQuery::bindValue(const QString &placeholder, const
    QVariant &val, QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#bindValue

    Parameters
    ----------

    placeholder : str
      Passed on as it is: a QString is made of it for the call.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number. May be left out, as in Qt: it is then
      QSql.ParamType.In.
    """
    #  void QSqlQuery::bindValue(const QString &placeholder, const QVariant
    #      &val, QSql::ParamType type)
    self.uglySide.call(
        'ritual_ZN9QSqlQuery9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql1'
        '3ParamTypeFlagEE',
        placeholder, self._valueOf(val), type.value,
    )

  @overload(int, QVariant)
  @overload(int, QVariant, QSql.ParamType)
  def bindValue(
      self,
      pos: int,
      val: QVariant,
      type: QSql.ParamType = QSql.ParamType.In,
  ) -> None:
    """
    Calls Qt's 'void QSqlQuery::bindValue(int pos, const QVariant &val,
    QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#bindValue

    Parameters
    ----------

    pos : int
      Passed on as it is.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number. May be left out, as in Qt: it is then
      QSql.ParamType.In.
    """
    #  void QSqlQuery::bindValue(int pos, const QVariant &val,
    #      QSql::ParamType type)
    self.uglySide.call(
        'ritual_ZN9QSqlQuery9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTyp'
        'eFlagEE',
        pos, self._valueOf(val), type.value,
    )

  @overload(QVariant)
  @overload(QVariant, QSql.ParamType)
  def addBindValue(
      self,
      val: QVariant,
      type: QSql.ParamType = QSql.ParamType.In,
  ) -> None:
    """
    Calls Qt's 'void QSqlQuery::addBindValue(const QVariant &val,
    QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#addBindValue

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number. May be left out, as in Qt: it is then
      QSql.ParamType.In.
    """
    #  void QSqlQuery::addBindValue(const QVariant &val, QSql::ParamType
    #      type)
    self.uglySide.call(
        'ritual_ZN9QSqlQuery12addBindValueERK8QVariant6QFlagsIN4QSql13Param'
        'TypeFlagEE',
        self._valueOf(val), type.value,
    )

  def finish(self) -> None:
    """
    Calls Qt's 'void QSqlQuery::finish()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#finish
    """
    #  void QSqlQuery::finish()
    self.uglySide.call('ritual_ZN9QSqlQuery6finishEv')

  def nextResult(self) -> bool:
    """
    Calls Qt's 'bool QSqlQuery::nextResult()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlquery.html#nextResult
    """
    #  bool QSqlQuery::nextResult()
    return self.uglySide.call('ritual_ZN9QSqlQuery10nextResultEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QSqlQuery::swap(QSqlQuery &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlQuery.swap' has no cute function yet. Qt's 'void "
        "QSqlQuery::swap(QSqlQuery &other)': takes a type Python has no way "
        "to hand over yet.")
