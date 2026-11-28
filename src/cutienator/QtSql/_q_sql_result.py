"""
QSqlResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList, Qt
from . import QSql

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QSqlDriver, QSqlError, QSqlRecord, QSqlResultPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlDriver = WAIT['QSqlDriver']
  QSqlError = WAIT['QSqlError']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlResult: a plain Python object standing in front
  of one C++ QSqlResult.

  What exists
  -----------

  Every function of Qt's QSqlResult that has a ritual and that Python can
  call so far, 50 names in all: 'd_func', 'handle', 'at', 'lastQuery',
  'lastError', 'isValid', 'isActive', 'isSelect', 'isForwardOnly', 'driver',
  'setAt', 'setActive', 'setLastError', 'setQuery', 'setSelect',
  'setForwardOnly', 'exec', 'prepare', 'savePrepare', 'bindValue',
  'addBindValue', 'boundValue', 'bindValueType', 'boundValueCount',
  'boundValues', 'executedQuery', 'boundValueNames', 'boundValueName',
  'clear', 'hasOutValues', 'data', 'isNull', 'reset', 'fetch', 'fetchNext',
  'fetchPrevious', 'fetchFirst', 'fetchLast', 'size', 'numRowsAffected',
  'record', 'lastInsertId', 'execBatch', 'detachFromResultSet',
  'setNumericalPrecisionPolicy', 'numericalPrecisionPolicy',
  'setPositionalBindingEnabled', 'isPositionalBindingEnabled', 'nextResult',
  'resetBindCount'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSqlResultPrivate *QSqlResult::d_func() const': takes in
    Python what 'QSqlResultPrivate *QSqlResult::d_func()' takes.
  - Qt's 'QSqlResult::~QSqlResult()': the destructor: Python never removes a
    C++ QSqlResult.
  - Qt's 'QSqlResult::QSqlResult(QSqlResultPrivate &dd)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVariantList &QSqlResult::boundValues(Qt::Disambiguated_t a0)':
    gives a type Python has no way to take yet.
  - Qt's 'BindingSyntax QSqlResult::bindingSyntax() const': gives the enum
    'QSqlResult::BindingSyntax', whose class cannot be named here.
  - Qt's 'void QSqlResult::virtual_hook(int id, void *data)': names 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 62 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSqlResult is created at the first use, not by 'QSqlResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlResult.
  - Each name of Qt's QSqlResult that has no cute function yet,
    'bindingSyntax', 'virtual_hook', holds a function that raises
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
  __qt_class__ = 'QSqlResult'

  #  A C++ QSqlResult Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlResult'

  #  The functions Qt calls itself that QSqlResult is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'virtual_hook': (
          'void QSqlResult::virtual_hook(int, void *)',
      ),
  }

  #  The functions Qt calls itself that QSqlResult is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'handle': (
          ('_ZNK10QSqlResult6handleEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'setAt': (
          ('_ZN10QSqlResult5setAtEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setActive': (
          ('_ZN10QSqlResult9setActiveEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setLastError': (
          ('_ZN10QSqlResult12setLastErrorERK9QSqlError',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtSql:QSqlError'),
           )),
      ),
      'setQuery': (
          ('_ZN10QSqlResult8setQueryERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setSelect': (
          ('_ZN10QSqlResult9setSelectEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setForwardOnly': (
          ('_ZN10QSqlResult14setForwardOnlyEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'exec': (
          ('_ZN10QSqlResult4execEv',
           ('bool', 'number', ''),
           ()),
      ),
      'prepare': (
          ('_ZN10QSqlResult7prepareERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'savePrepare': (
          ('_ZN10QSqlResult11savePrepareERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'bindValue': (
          ('_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamType'
           'FlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'flags', 'QtSql:QSql.ParamTypeFlag'),
           )),
          ('_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13'
           'ParamTypeFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('int', 'flags', 'QtSql:QSql.ParamTypeFlag'),
           )),
      ),
      'data': (
          ('_ZN10QSqlResult4dataEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'isNull': (
          ('_ZN10QSqlResult6isNullEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'reset': (
          ('_ZN10QSqlResult5resetERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'fetch': (
          ('_ZN10QSqlResult5fetchEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'fetchNext': (
          ('_ZN10QSqlResult9fetchNextEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fetchPrevious': (
          ('_ZN10QSqlResult13fetchPreviousEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fetchFirst': (
          ('_ZN10QSqlResult10fetchFirstEv',
           ('bool', 'number', ''),
           ()),
      ),
      'fetchLast': (
          ('_ZN10QSqlResult9fetchLastEv',
           ('bool', 'number', ''),
           ()),
      ),
      'size': (
          ('_ZN10QSqlResult4sizeEv',
           ('int', 'number', ''),
           ()),
      ),
      'numRowsAffected': (
          ('_ZN10QSqlResult15numRowsAffectedEv',
           ('int', 'number', ''),
           ()),
      ),
      'record': (
          ('_ZNK10QSqlResult6recordEv',
           ('address', 'value', 'QtSql:QSqlRecord'),
           ()),
      ),
      'lastInsertId': (
          ('_ZNK10QSqlResult12lastInsertIdEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'execBatch': (
          ('_ZN10QSqlResult9execBatchEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'detachFromResultSet': (
          ('_ZN10QSqlResult19detachFromResultSetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setNumericalPrecisionPolicy': (
          ('_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24NumericalP'
           'recisionPolicyE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtSql:QSql.NumericalPrecisionPolicy'),
           )),
      ),
      'nextResult': (
          ('_ZN10QSqlResult10nextResultEv',
           ('bool', 'number', ''),
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

  def handle(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlResult::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#handle

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlResult::handle() const
    ritual = 'ritual_ZNK10QSqlResult6handleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlResult6handleEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def at(self) -> int:
    """
    Calls Qt's 'int QSqlResult::at() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#at
    """
    #  int QSqlResult::at() const
    return self.uglySide.call('ritual_ZNK10QSqlResult2atEv')

  def lastQuery(self) -> str:
    """
    Calls Qt's 'QString QSqlResult::lastQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#lastQuery

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResult::lastQuery() const
    return self.uglySide.call('ritual_ZNK10QSqlResult9lastQueryEv')

  def lastError(self) -> QSqlError:
    """
    Calls Qt's 'QSqlError QSqlResult::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#lastError

    Returns
    -------

    QSqlError
      A new cute QSqlError around the copy Qt gave back. Python owns it.
    """
    #  QSqlError QSqlResult::lastError() const
    address = self.uglySide.call('ritual_ZNK10QSqlResult9lastErrorEv')
    from . import QSqlError
    return QSqlError._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#isValid
    """
    #  bool QSqlResult::isValid() const
    return self.uglySide.call('ritual_ZNK10QSqlResult7isValidEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#isActive
    """
    #  bool QSqlResult::isActive() const
    return self.uglySide.call('ritual_ZNK10QSqlResult8isActiveEv')

  def isSelect(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isSelect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#isSelect
    """
    #  bool QSqlResult::isSelect() const
    return self.uglySide.call('ritual_ZNK10QSqlResult8isSelectEv')

  def isForwardOnly(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isForwardOnly() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#isForwardOnly
    """
    #  bool QSqlResult::isForwardOnly() const
    return self.uglySide.call('ritual_ZNK10QSqlResult13isForwardOnlyEv')

  def driver(self) -> Optional[QSqlDriver]:
    """
    Calls Qt's 'const QSqlDriver *QSqlResult::driver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#driver

    Returns
    -------

    Optional[QSqlDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSqlDriver *QSqlResult::driver() const
    address = self.uglySide.call('ritual_ZNK10QSqlResult6driverEv')
    from . import QSqlDriver
    return QSqlDriver._cuteAt(address)

  @overload(str)
  def boundValue(self, placeholder: str) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlResult::boundValue(const QString &placeholder)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValue

    Parameters
    ----------

    placeholder : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlResult::boundValue(const QString &placeholder) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlResult10boundValueERK7QString', placeholder,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def boundValue(self, pos: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlResult::boundValue(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValue

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlResult::boundValue(int pos) const
    address = self.uglySide.call('ritual_ZNK10QSqlResult10boundValueEi', pos)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def bindValueType(self, placeholder: str) -> QSql.ParamType:
    """
    Calls Qt's 'QSql::ParamType QSqlResult::bindValueType(const QString
    &placeholder) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#bindValueType

    Parameters
    ----------

    placeholder : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSql.ParamType
      The value standing for the combination Qt gave back.
    """
    #  QSql::ParamType QSqlResult::bindValueType(const QString &placeholder)
    #      const
    return QSql.ParamType(self.uglySide.call(
        'ritual_ZNK10QSqlResult13bindValueTypeERK7QString', placeholder,
    ))

  @overload(int)
  def bindValueType(self, pos: int) -> QSql.ParamType:
    """
    Calls Qt's 'QSql::ParamType QSqlResult::bindValueType(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#bindValueType

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QSql.ParamType
      The value standing for the combination Qt gave back.
    """
    #  QSql::ParamType QSqlResult::bindValueType(int pos) const
    return QSql.ParamType(self.uglySide.call(
        'ritual_ZNK10QSqlResult13bindValueTypeEi', pos,
    ))

  def boundValueCount(self) -> int:
    """
    Calls Qt's 'int QSqlResult::boundValueCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValueCount
    """
    #  int QSqlResult::boundValueCount() const
    return self.uglySide.call('ritual_ZNK10QSqlResult15boundValueCountEv')

  @overload(WAIT['Qt.Disambiguated_t'])
  def boundValues(self, a0: Qt.Disambiguated_t) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QSqlResult::boundValues(Qt::Disambiguated_t a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValues

    Parameters
    ----------

    a0 : Qt.Disambiguated_t
      Passed on as a value: Qt reads the C++ Qt::Disambiguated_t, which stays
      Python's own.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QSqlResult::boundValues(Qt::Disambiguated_t a0) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlResult11boundValuesEN2Qt15Disambiguated_tE',
        self._valueOf(a0),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def executedQuery(self) -> str:
    """
    Calls Qt's 'QString QSqlResult::executedQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#executedQuery

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResult::executedQuery() const
    return self.uglySide.call('ritual_ZNK10QSqlResult13executedQueryEv')

  def boundValueNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSqlResult::boundValueNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValueNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlResult::boundValueNames() const
    address = self.uglySide.call('ritual_ZNK10QSqlResult15boundValueNamesEv')
    return QStringList._cuteOwning(address)

  @overload(int)
  def boundValueName(self, pos: int) -> str:
    """
    Calls Qt's 'QString QSqlResult::boundValueName(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#boundValueName

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlResult::boundValueName(int pos) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlResult14boundValueNameEi', pos,
    )

  def hasOutValues(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::hasOutValues() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#hasOutValues
    """
    #  bool QSqlResult::hasOutValues() const
    return self.uglySide.call('ritual_ZNK10QSqlResult12hasOutValuesEv')

  def record(self) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlResult::record() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#record

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlResult::record() const
    ritual = 'ritual_ZNK10QSqlResult6recordEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlResult6recordEv'
    address = self.uglySide.call(ritual)
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  def lastInsertId(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlResult::lastInsertId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#lastInsertId

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlResult::lastInsertId() const
    ritual = 'ritual_ZNK10QSqlResult12lastInsertIdEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlResult12lastInsertIdEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy:
    """
    Calls Qt's 'QSql::NumericalPrecisionPolicy
    QSqlResult::numericalPrecisionPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresult.html#numericalPrecisionPolicy

    Returns
    -------

    QSql.NumericalPrecisionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSql.NumericalPrecisionPolicy(number)' gives.
    """
    #  QSql::NumericalPrecisionPolicy QSqlResult::numericalPrecisionPolicy()
    #      const
    return QSql.NumericalPrecisionPolicy(self.uglySide.call(
        'ritual_ZNK10QSqlResult24numericalPrecisionPolicyEv',
    ))

  def isPositionalBindingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isPositionalBindingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresult.html#isPositionalBindingEnabled
    """
    #  bool QSqlResult::isPositionalBindingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10QSqlResult26isPositionalBindingEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAt(self, at: int) -> None:
    """
    Calls Qt's 'void QSqlResult::setAt(int at)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setAt

    Parameters
    ----------

    at : int
      Passed on as it is.
    """
    #  void QSqlResult::setAt(int at)
    ritual = 'ritual_ZN10QSqlResult5setAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult5setAtEi'
    self.uglySide.call(ritual, at)

  @overload(bool)
  def setActive(self, a: bool) -> None:
    """
    Calls Qt's 'void QSqlResult::setActive(bool a)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setActive

    Parameters
    ----------

    a : bool
      Passed on as it is.
    """
    #  void QSqlResult::setActive(bool a)
    ritual = 'ritual_ZN10QSqlResult9setActiveEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult9setActiveEb'
    self.uglySide.call(ritual, a)

  @overload(QSqlError)
  def setLastError(self, e: QSqlError) -> None:
    """
    Calls Qt's 'void QSqlResult::setLastError(const QSqlError &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setLastError

    Parameters
    ----------

    e : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  void QSqlResult::setLastError(const QSqlError &e)
    ritual = 'ritual_ZN10QSqlResult12setLastErrorERK9QSqlError'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult12setLastErrorERK9QSqlError'
    self.uglySide.call(ritual, self._valueOf(e))

  @overload(str)
  def setQuery(self, query: str) -> None:
    """
    Calls Qt's 'void QSqlResult::setQuery(const QString &query)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setQuery

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlResult::setQuery(const QString &query)
    ritual = 'ritual_ZN10QSqlResult8setQueryERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult8setQueryERK7QString'
    self.uglySide.call(ritual, query)

  @overload(bool)
  def setSelect(self, s: bool) -> None:
    """
    Calls Qt's 'void QSqlResult::setSelect(bool s)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setSelect

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QSqlResult::setSelect(bool s)
    ritual = 'ritual_ZN10QSqlResult9setSelectEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult9setSelectEb'
    self.uglySide.call(ritual, s)

  @overload(bool)
  def setForwardOnly(self, forward: bool) -> None:
    """
    Calls Qt's 'void QSqlResult::setForwardOnly(bool forward)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#setForwardOnly

    Parameters
    ----------

    forward : bool
      Passed on as it is.
    """
    #  void QSqlResult::setForwardOnly(bool forward)
    ritual = 'ritual_ZN10QSqlResult14setForwardOnlyEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult14setForwardOnlyEb'
    self.uglySide.call(ritual, forward)

  @overload(QSql.NumericalPrecisionPolicy)
  def setNumericalPrecisionPolicy(
      self,
      policy: QSql.NumericalPrecisionPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QSqlResult::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresult.html#setNumericalPrecisionPolicy

    Parameters
    ----------

    policy : QSql.NumericalPrecisionPolicy
      Passed on as its number.
    """
    #  void QSqlResult::setNumericalPrecisionPolicy(QSql::
    #      NumericalPrecisionPolicy policy)
    ritual = (
        'ritual_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24Numeric'
        'alPrecisionPolicyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSqlResult27setNumericalPrecisionPolicyEN4QSql24N'
          'umericalPrecisionPolicyE')
    self.uglySide.call(ritual, policy.value)

  @overload(bool)
  def setPositionalBindingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSqlResult::setPositionalBindingEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresult.html#setPositionalBindingEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSqlResult::setPositionalBindingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN10QSqlResult27setPositionalBindingEnabledEb', enable,
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

  @overload(QSqlDriver)
  @overload(NoneType)
  def __init__(self, db: Optional[QSqlDriver]) -> None:
    """
    Notes what was given, for Qt's 'QSqlResult::QSqlResult(const QSqlDriver
    *db)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#QSqlResult

    Parameters
    ----------

    db : Optional[QSqlDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSqlResult::QSqlResult(const QSqlDriver *db)
    self._noteCreation(QSqlResult, lambda: Rituals.call(
        'ritual_ZN10QSqlResultC1EPK10QSqlDriver', self._addressOf(db),
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

  def d_func(self) -> Optional[QSqlResultPrivate]:
    """
    Calls Qt's 'QSqlResultPrivate *QSqlResult::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#d_func

    Returns
    -------

    Optional[QSqlResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlResultPrivate *QSqlResult::d_func()
    address = self.uglySide.call('ritual_ZN10QSqlResult6d_funcEv')
    from . import QSqlResultPrivate
    return QSqlResultPrivate._cuteAt(address)

  def exec(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#exec
    """
    #  bool QSqlResult::exec()
    ritual = 'ritual_ZN10QSqlResult4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult4execEv'
    return self.uglySide.call(ritual)

  @overload(str)
  def prepare(self, query: str) -> bool:
    """
    Calls Qt's 'bool QSqlResult::prepare(const QString &query)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#prepare

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlResult::prepare(const QString &query)
    ritual = 'ritual_ZN10QSqlResult7prepareERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult7prepareERK7QString'
    return self.uglySide.call(ritual, query)

  @overload(str)
  def savePrepare(self, sqlquery: str) -> bool:
    """
    Calls Qt's 'bool QSqlResult::savePrepare(const QString &sqlquery)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#savePrepare

    Parameters
    ----------

    sqlquery : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlResult::savePrepare(const QString &sqlquery)
    ritual = 'ritual_ZN10QSqlResult11savePrepareERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult11savePrepareERK7QString'
    return self.uglySide.call(ritual, sqlquery)

  @overload(int, QVariant, QSql.ParamType)
  def bindValue(self, pos: int, val: QVariant, type: QSql.ParamType) -> None:
    """
    Calls Qt's 'void QSqlResult::bindValue(int pos, const QVariant &val,
    QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#bindValue

    Parameters
    ----------

    pos : int
      Passed on as it is.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number.
    """
    #  void QSqlResult::bindValue(int pos, const QVariant &val,
    #      QSql::ParamType type)
    ritual = (
        'ritual_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamT'
        'ypeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSqlResult9bindValueEiRK8QVariant6QFlagsIN4QSql13'
          'ParamTypeFlagEE')
    self.uglySide.call(ritual, pos, self._valueOf(val), type.value)

  @overload(str, QVariant, QSql.ParamType)
  def bindValue(
      self,
      placeholder: str,
      val: QVariant,
      type: QSql.ParamType,
  ) -> None:
    """
    Calls Qt's 'void QSqlResult::bindValue(const QString &placeholder, const
    QVariant &val, QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#bindValue

    Parameters
    ----------

    placeholder : str
      Passed on as it is: a QString is made of it for the call.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number.
    """
    #  void QSqlResult::bindValue(const QString &placeholder, const QVariant
    #      &val, QSql::ParamType type)
    ritual = (
        'ritual_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlagsIN4QSq'
        'l13ParamTypeFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSqlResult9bindValueERK7QStringRK8QVariant6QFlags'
          'IN4QSql13ParamTypeFlagEE')
    self.uglySide.call(ritual, placeholder, self._valueOf(val), type.value)

  @overload(QVariant, QSql.ParamType)
  def addBindValue(self, val: QVariant, type: QSql.ParamType) -> None:
    """
    Calls Qt's 'void QSqlResult::addBindValue(const QVariant &val,
    QSql::ParamType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#addBindValue

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    type : QSql.ParamType
      Passed on as its number.
    """
    #  void QSqlResult::addBindValue(const QVariant &val, QSql::ParamType
    #      type)
    self.uglySide.call(
        'ritual_ZN10QSqlResult12addBindValueERK8QVariant6QFlagsIN4QSql13Par'
        'amTypeFlagEE',
        self._valueOf(val), type.value,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QSqlResult::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#clear
    """
    #  void QSqlResult::clear()
    self.uglySide.call('ritual_ZN10QSqlResult5clearEv')

  @overload(int)
  def data(self, i: int) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlResult::data(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#data

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlResult::data(int i)
    address = self.uglySide.call('ritual_ZN10QSqlResult4dataEi', i)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def isNull(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlResult::isNull(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#isNull

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlResult::isNull(int i)
    return self.uglySide.call('ritual_ZN10QSqlResult6isNullEi', i)

  @overload(str)
  def reset(self, sqlquery: str) -> bool:
    """
    Calls Qt's 'bool QSqlResult::reset(const QString &sqlquery)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#reset

    Parameters
    ----------

    sqlquery : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlResult::reset(const QString &sqlquery)
    return self.uglySide.call(
        'ritual_ZN10QSqlResult5resetERK7QString', sqlquery,
    )

  @overload(int)
  def fetch(self, i: int) -> bool:
    """
    Calls Qt's 'bool QSqlResult::fetch(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#fetch

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QSqlResult::fetch(int i)
    return self.uglySide.call('ritual_ZN10QSqlResult5fetchEi', i)

  def fetchNext(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::fetchNext()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#fetchNext
    """
    #  bool QSqlResult::fetchNext()
    ritual = 'ritual_ZN10QSqlResult9fetchNextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult9fetchNextEv'
    return self.uglySide.call(ritual)

  def fetchPrevious(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::fetchPrevious()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#fetchPrevious
    """
    #  bool QSqlResult::fetchPrevious()
    ritual = 'ritual_ZN10QSqlResult13fetchPreviousEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult13fetchPreviousEv'
    return self.uglySide.call(ritual)

  def fetchFirst(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::fetchFirst()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#fetchFirst
    """
    #  bool QSqlResult::fetchFirst()
    return self.uglySide.call('ritual_ZN10QSqlResult10fetchFirstEv')

  def fetchLast(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::fetchLast()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#fetchLast
    """
    #  bool QSqlResult::fetchLast()
    return self.uglySide.call('ritual_ZN10QSqlResult9fetchLastEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QSqlResult::size()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#size
    """
    #  int QSqlResult::size()
    return self.uglySide.call('ritual_ZN10QSqlResult4sizeEv')

  def numRowsAffected(self) -> int:
    """
    Calls Qt's 'int QSqlResult::numRowsAffected()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#numRowsAffected
    """
    #  int QSqlResult::numRowsAffected()
    return self.uglySide.call('ritual_ZN10QSqlResult15numRowsAffectedEv')

  @overload()
  @overload(bool)
  def execBatch(self, arrayBind: bool = False) -> bool:
    """
    Calls Qt's 'bool QSqlResult::execBatch(bool arrayBind)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#execBatch

    Parameters
    ----------

    arrayBind : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QSqlResult::execBatch(bool arrayBind)
    ritual = 'ritual_ZN10QSqlResult9execBatchEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult9execBatchEb'
    return self.uglySide.call(ritual, arrayBind)

  def detachFromResultSet(self) -> None:
    """
    Calls Qt's 'void QSqlResult::detachFromResultSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqlresult.html#detachFromResultSet
    """
    #  void QSqlResult::detachFromResultSet()
    ritual = 'ritual_ZN10QSqlResult19detachFromResultSetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult19detachFromResultSetEv'
    self.uglySide.call(ritual)

  def nextResult(self) -> bool:
    """
    Calls Qt's 'bool QSqlResult::nextResult()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#nextResult
    """
    #  bool QSqlResult::nextResult()
    ritual = 'ritual_ZN10QSqlResult10nextResultEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlResult10nextResultEv'
    return self.uglySide.call(ritual)

  def resetBindCount(self) -> None:
    """
    Calls Qt's 'void QSqlResult::resetBindCount()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlresult.html#resetBindCount
    """
    #  void QSqlResult::resetBindCount()
    self.uglySide.call('ritual_ZN10QSqlResult14resetBindCountEv')

  @staticmethod
  def bindingSyntax(*__, **_) -> Never:
    """
    Qt's 'BindingSyntax QSqlResult::bindingSyntax() const': gives the enum
    'QSqlResult::BindingSyntax', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSqlResult.bindingSyntax' has no cute function yet. Qt's "
        "'BindingSyntax QSqlResult::bindingSyntax() const': gives the enum "
        "'QSqlResult::BindingSyntax', whose class cannot be named here.")

  @staticmethod
  def virtual_hook(*__, **_) -> Never:
    """
    Qt's 'void QSqlResult::virtual_hook(int id, void *data)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSqlResult.virtual_hook' has no cute function yet. Qt's 'void "
        "QSqlResult::virtual_hook(int id, void *data)': names 'void', which "
        "has no cute class yet.")
