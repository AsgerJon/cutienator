"""
QSqlDatabase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqldatabase.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QSql, QSqlDatabaseDefaultConnectionName

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QThread
  from . import QSqlDriver, QSqlDriverCreatorBase, QSqlError, QSqlIndex
  from . import QSqlQuery, QSqlRecord
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlDriver = WAIT['QSqlDriver']
  QSqlDriverCreatorBase = WAIT['QSqlDriverCreatorBase']
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlDatabase(QSqlDatabaseDefaultConnectionName):
  """
  The cute side of Qt's QSqlDatabase: a plain Python object standing in front
  of one C++ QSqlDatabase.

  It is built on the cute 'QSqlDatabaseDefaultConnectionName', as Qt's
  QSqlDatabase is built on Qt's QSqlDatabaseDefaultConnectionName, and has
  everything that class has.

  C++ hands a QSqlDatabase around as a copy, so every C++ QSqlDatabase behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlDatabase that has a ritual and that Python can
  call so far, 41 names in all: 'open', 'close', 'isOpen', 'isOpenError',
  'tables', 'primaryIndex', 'record', 'exec', 'lastError', 'isValid',
  'transaction', 'commit', 'rollback', 'setDatabaseName', 'setUserName',
  'setPassword', 'setHostName', 'setPort', 'setConnectOptions',
  'databaseName', 'userName', 'password', 'hostName', 'driverName', 'port',
  'connectOptions', 'connectionName', 'setNumericalPrecisionPolicy',
  'numericalPrecisionPolicy', 'moveToThread', 'thread', 'driver',
  'addDatabase', 'cloneDatabase', 'database', 'removeDatabase', 'contains',
  'drivers', 'connectionNames', 'registerSqlDriver', 'isDriverAvailable'. It
  can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlDatabase::~QSqlDatabase()': the destructor: Python removes its
    C++ QSqlDatabase by it, and has no other use for it.
  - Qt's 'QSqlDatabase &QSqlDatabase::operator=(const QSqlDatabase &other)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  3 of the 53 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QSqlDatabase is created at the first use, not by
    'QSqlDatabase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlDatabase back gives a copy the ritual made for
    Python, in a new cute QSqlDatabase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str)
  def addDatabase(type: str, connectionName: str) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlDatabase::addDatabase(const QString &type,
    const QString &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#addDatabase

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.

    connectionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlDatabase::addDatabase(const QString &type, const
    #      QString &connectionName)
    address = Rituals.call(
        'ritual_ZN12QSqlDatabase11addDatabaseERK7QStringS2_',
        type, connectionName,
    )
    return QSqlDatabase._cuteOwning(address)

  @staticmethod
  @overload(QSqlDriver, str)
  @overload(NoneType, str)
  def addDatabase(
      driver: Optional[QSqlDriver],
      connectionName: str,
  ) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlDatabase::addDatabase(QSqlDriver *driver,
    const QString &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#addDatabase

    Parameters
    ----------

    driver : Optional[QSqlDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    connectionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlDatabase::addDatabase(QSqlDriver *driver, const
    #      QString &connectionName)
    address = Rituals.call(
        'ritual_ZN12QSqlDatabase11addDatabaseEP10QSqlDriverRK7QString',
        CuteMixin._addressOf(driver), connectionName,
    )
    return QSqlDatabase._cuteOwning(address)

  @staticmethod
  @overload(THIS, str)
  def cloneDatabase(
      other: QSqlDatabase,
      connectionName: str,
  ) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlDatabase::cloneDatabase(const QSqlDatabase
    &other, const QString &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#cloneDatabase

    Parameters
    ----------

    other : QSqlDatabase
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own.

    connectionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlDatabase::cloneDatabase(const QSqlDatabase &other,
    #      const QString &connectionName)
    address = Rituals.call(
        'ritual_ZN12QSqlDatabase13cloneDatabaseERKS_RK7QString',
        CuteMixin._valueOf(other), connectionName,
    )
    return QSqlDatabase._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  def cloneDatabase(other: str, connectionName: str) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlDatabase::cloneDatabase(const QString
    &other, const QString &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#cloneDatabase

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.

    connectionName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlDatabase::cloneDatabase(const QString &other, const
    #      QString &connectionName)
    address = Rituals.call(
        'ritual_ZN12QSqlDatabase13cloneDatabaseERK7QStringS2_',
        other, connectionName,
    )
    return QSqlDatabase._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, bool)
  def database(connectionName: str, open: bool = True) -> QSqlDatabase:
    """
    Calls Qt's 'QSqlDatabase QSqlDatabase::database(const QString
    &connectionName, bool open)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#database

    Parameters
    ----------

    connectionName : str
      Passed on as it is: a QString is made of it for the call.

    open : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QSqlDatabase
      A new cute QSqlDatabase around the copy Qt gave back. Python owns it.
    """
    #  QSqlDatabase QSqlDatabase::database(const QString &connectionName,
    #      bool open)
    address = Rituals.call(
        'ritual_ZN12QSqlDatabase8databaseERK7QStringb', connectionName, open,
    )
    return QSqlDatabase._cuteOwning(address)

  @staticmethod
  @overload(str)
  def removeDatabase(connectionName: str) -> None:
    """
    Calls Qt's 'void QSqlDatabase::removeDatabase(const QString
    &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#removeDatabase

    Parameters
    ----------

    connectionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlDatabase::removeDatabase(const QString &connectionName)
    Rituals.call(
        'ritual_ZN12QSqlDatabase14removeDatabaseERK7QString', connectionName,
    )

  @staticmethod
  @overload(str)
  def contains(connectionName: str) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::contains(const QString &connectionName)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#contains

    Parameters
    ----------

    connectionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlDatabase::contains(const QString &connectionName)
    return Rituals.call(
        'ritual_ZN12QSqlDatabase8containsERK7QString', connectionName,
    )

  @staticmethod
  def drivers() -> QStringList:
    """
    Calls Qt's 'QStringList QSqlDatabase::drivers()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#drivers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlDatabase::drivers()
    address = Rituals.call('ritual_ZN12QSqlDatabase7driversEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def connectionNames() -> QStringList:
    """
    Calls Qt's 'QStringList QSqlDatabase::connectionNames()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#connectionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlDatabase::connectionNames()
    address = Rituals.call('ritual_ZN12QSqlDatabase15connectionNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QSqlDriverCreatorBase)
  @overload(str, NoneType)
  def registerSqlDriver(
      name: str,
      creator: Optional[QSqlDriverCreatorBase],
  ) -> None:
    """
    Calls Qt's 'void QSqlDatabase::registerSqlDriver(const QString &name,
    QSqlDriverCreatorBase *creator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldatabase.html#registerSqlDriver

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    creator : Optional[QSqlDriverCreatorBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSqlDatabase::registerSqlDriver(const QString &name,
    #      QSqlDriverCreatorBase *creator)
    Rituals.call(
        'ritual_ZN12QSqlDatabase17registerSqlDriverERK7QStringP21QSqlDriver'
        'CreatorBase',
        name, CuteMixin._addressOf(creator),
    )

  @staticmethod
  @overload(str)
  def isDriverAvailable(name: str) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::isDriverAvailable(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldatabase.html#isDriverAvailable

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlDatabase::isDriverAvailable(const QString &name)
    return Rituals.call(
        'ritual_ZN12QSqlDatabase17isDriverAvailableERK7QString', name,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlDatabase'

  #  Qt's '~QSqlDatabase()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlDatabase behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QSqlDatabaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#isOpen
    """
    #  bool QSqlDatabase::isOpen() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase6isOpenEv')

  def isOpenError(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::isOpenError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#isOpenError
    """
    #  bool QSqlDatabase::isOpenError() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase11isOpenErrorEv')

  @overload()
  @overload(QSql.TableType)
  def tables(
      self,
      type: QSql.TableType = QSql.TableType.Tables,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QSqlDatabase::tables(QSql::TableType type)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#tables

    Parameters
    ----------

    type : QSql.TableType
      Passed on as its number. May be left out, as in Qt: it is then
      QSql.TableType.Tables.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlDatabase::tables(QSql::TableType type) const
    address = self.uglySide.call(
        'ritual_ZNK12QSqlDatabase6tablesEN4QSql9TableTypeE', type.value,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def primaryIndex(self, tablename: str) -> QSqlIndex:
    """
    Calls Qt's 'QSqlIndex QSqlDatabase::primaryIndex(const QString
    &tablename) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#primaryIndex

    Parameters
    ----------

    tablename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlIndex
      A new cute QSqlIndex around the copy Qt gave back. Python owns it.
    """
    #  QSqlIndex QSqlDatabase::primaryIndex(const QString &tablename) const
    address = self.uglySide.call(
        'ritual_ZNK12QSqlDatabase12primaryIndexERK7QString', tablename,
    )
    from . import QSqlIndex
    return QSqlIndex._cuteOwning(address)

  @overload(str)
  def record(self, tablename: str) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlDatabase::record(const QString &tablename)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#record

    Parameters
    ----------

    tablename : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlDatabase::record(const QString &tablename) const
    address = self.uglySide.call(
        'ritual_ZNK12QSqlDatabase6recordERK7QString', tablename,
    )
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload()
  @overload(str)
  def exec(self, query: str = '') -> QSqlQuery:
    """
    Calls Qt's 'QSqlQuery QSqlDatabase::exec(const QString &query) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#exec

    Parameters
    ----------

    query : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QSqlQuery
      A new cute QSqlQuery around the copy Qt gave back. Python owns it.
    """
    #  QSqlQuery QSqlDatabase::exec(const QString &query) const
    address = self.uglySide.call(
        'ritual_ZNK12QSqlDatabase4execERK7QString', query,
    )
    from . import QSqlQuery
    return QSqlQuery._cuteOwning(address)

  def lastError(self) -> QSqlError:
    """
    Calls Qt's 'QSqlError QSqlDatabase::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#lastError

    Returns
    -------

    QSqlError
      A new cute QSqlError around the copy Qt gave back. Python owns it.
    """
    #  QSqlError QSqlDatabase::lastError() const
    address = self.uglySide.call('ritual_ZNK12QSqlDatabase9lastErrorEv')
    from . import QSqlError
    return QSqlError._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#isValid
    """
    #  bool QSqlDatabase::isValid() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase7isValidEv')

  def databaseName(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::databaseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#databaseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::databaseName() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase12databaseNameEv')

  def userName(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::userName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#userName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::userName() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase8userNameEv')

  def password(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::password() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#password

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::password() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase8passwordEv')

  def hostName(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::hostName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#hostName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::hostName() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase8hostNameEv')

  def driverName(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::driverName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#driverName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::driverName() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase10driverNameEv')

  def port(self) -> int:
    """
    Calls Qt's 'int QSqlDatabase::port() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#port
    """
    #  int QSqlDatabase::port() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase4portEv')

  def connectOptions(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::connectOptions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#connectOptions

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::connectOptions() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase14connectOptionsEv')

  def connectionName(self) -> str:
    """
    Calls Qt's 'QString QSqlDatabase::connectionName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#connectionName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDatabase::connectionName() const
    return self.uglySide.call('ritual_ZNK12QSqlDatabase14connectionNameEv')

  def numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy:
    """
    Calls Qt's 'QSql::NumericalPrecisionPolicy
    QSqlDatabase::numericalPrecisionPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldatabase.html#numericalPrecisionPolicy

    Returns
    -------

    QSql.NumericalPrecisionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSql.NumericalPrecisionPolicy(number)' gives.
    """
    #  QSql::NumericalPrecisionPolicy
    #      QSqlDatabase::numericalPrecisionPolicy() const
    return QSql.NumericalPrecisionPolicy(self.uglySide.call(
        'ritual_ZNK12QSqlDatabase24numericalPrecisionPolicyEv',
    ))

  def thread(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QSqlDatabase::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#thread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QSqlDatabase::thread() const
    address = self.uglySide.call('ritual_ZNK12QSqlDatabase6threadEv')
    from ..QtCore import QThread
    return QThread._cuteAt(address)

  def driver(self) -> Optional[QSqlDriver]:
    """
    Calls Qt's 'QSqlDriver *QSqlDatabase::driver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#driver

    Returns
    -------

    Optional[QSqlDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlDriver *QSqlDatabase::driver() const
    address = self.uglySide.call('ritual_ZNK12QSqlDatabase6driverEv')
    from . import QSqlDriver
    return QSqlDriver._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setDatabaseName(self, name: str) -> None:
    """
    Calls Qt's 'void QSqlDatabase::setDatabaseName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#setDatabaseName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlDatabase::setDatabaseName(const QString &name)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase15setDatabaseNameERK7QString', name,
    )

  @overload(str)
  def setUserName(self, name: str) -> None:
    """
    Calls Qt's 'void QSqlDatabase::setUserName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#setUserName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlDatabase::setUserName(const QString &name)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase11setUserNameERK7QString', name,
    )

  @overload(str)
  def setPassword(self, password: str) -> None:
    """
    Calls Qt's 'void QSqlDatabase::setPassword(const QString &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#setPassword

    Parameters
    ----------

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlDatabase::setPassword(const QString &password)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase11setPasswordERK7QString', password,
    )

  @overload(str)
  def setHostName(self, host: str) -> None:
    """
    Calls Qt's 'void QSqlDatabase::setHostName(const QString &host)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#setHostName

    Parameters
    ----------

    host : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSqlDatabase::setHostName(const QString &host)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase11setHostNameERK7QString', host,
    )

  @overload(int)
  def setPort(self, p: int) -> None:
    """
    Calls Qt's 'void QSqlDatabase::setPort(int p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#setPort

    Parameters
    ----------

    p : int
      Passed on as it is.
    """
    #  void QSqlDatabase::setPort(int p)
    self.uglySide.call('ritual_ZN12QSqlDatabase7setPortEi', p)

  @overload()
  @overload(str)
  def setConnectOptions(self, options: str = '') -> None:
    """
    Calls Qt's 'void QSqlDatabase::setConnectOptions(const QString
    &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldatabase.html#setConnectOptions

    Parameters
    ----------

    options : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QSqlDatabase::setConnectOptions(const QString &options)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase17setConnectOptionsERK7QString', options,
    )

  @overload(QSql.NumericalPrecisionPolicy)
  def setNumericalPrecisionPolicy(
      self,
      precisionPolicy: QSql.NumericalPrecisionPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QSqlDatabase::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy
    precisionPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldatabase.html#setNumericalPrecisionPolicy

    Parameters
    ----------

    precisionPolicy : QSql.NumericalPrecisionPolicy
      Passed on as its number.
    """
    #  void QSqlDatabase::setNumericalPrecisionPolicy(QSql::
    #      NumericalPrecisionPolicy precisionPolicy)
    self.uglySide.call(
        'ritual_ZN12QSqlDatabase27setNumericalPrecisionPolicyEN4QSql24Numer'
        'icalPrecisionPolicyE',
        precisionPolicy.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSqlDatabase::QSqlDatabase()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#QSqlDatabase
    """
    #  QSqlDatabase::QSqlDatabase()
    self._noteCreation(QSqlDatabase, lambda: Rituals.call(
        'ritual_ZN12QSqlDatabaseC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QSqlDatabase) -> None:
    """
    Notes what was given, for Qt's 'QSqlDatabase::QSqlDatabase(const
    QSqlDatabase &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#QSqlDatabase

    Parameters
    ----------

    other : QSqlDatabase
      Passed on as a value: Qt reads the C++ QSqlDatabase, which stays
      Python's own.
    """
    #  QSqlDatabase::QSqlDatabase(const QSqlDatabase &other)
    self._noteCreation(QSqlDatabase, lambda: Rituals.call(
        'ritual_ZN12QSqlDatabaseC1ERKS_', self._valueOf(other),
    ))

  @overload(str)
  def __init__(self, type: str) -> None:
    """
    Notes what was given, for Qt's 'QSqlDatabase::QSqlDatabase(const QString
    &type)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#QSqlDatabase

    Parameters
    ----------

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSqlDatabase::QSqlDatabase(const QString &type)
    self._noteCreation(QSqlDatabase, lambda: Rituals.call(
        'ritual_ZN12QSqlDatabaseC1ERK7QString', type,
    ))

  @overload(QSqlDriver)
  @overload(NoneType)
  def __init__(self, driver: Optional[QSqlDriver]) -> None:
    """
    Notes what was given, for Qt's 'QSqlDatabase::QSqlDatabase(QSqlDriver
    *driver)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#QSqlDatabase

    Parameters
    ----------

    driver : Optional[QSqlDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSqlDatabase::QSqlDatabase(QSqlDriver *driver)
    self._noteCreation(QSqlDatabase, lambda: Rituals.call(
        'ritual_ZN12QSqlDatabaseC1EP10QSqlDriver', self._addressOf(driver),
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

  @overload()
  def open(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#open
    """
    #  bool QSqlDatabase::open()
    return self.uglySide.call('ritual_ZN12QSqlDatabase4openEv')

  @overload(str, str)
  def open(self, user: str, password: str) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::open(const QString &user, const QString
    &password)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#open

    Parameters
    ----------

    user : str
      Passed on as it is: a QString is made of it for the call.

    password : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlDatabase::open(const QString &user, const QString &password)
    return self.uglySide.call(
        'ritual_ZN12QSqlDatabase4openERK7QStringS2_', user, password,
    )

  def close(self) -> None:
    """
    Calls Qt's 'void QSqlDatabase::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#close
    """
    #  void QSqlDatabase::close()
    self.uglySide.call('ritual_ZN12QSqlDatabase5closeEv')

  def transaction(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::transaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#transaction
    """
    #  bool QSqlDatabase::transaction()
    return self.uglySide.call('ritual_ZN12QSqlDatabase11transactionEv')

  def commit(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#commit
    """
    #  bool QSqlDatabase::commit()
    return self.uglySide.call('ritual_ZN12QSqlDatabase6commitEv')

  def rollback(self) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::rollback()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#rollback
    """
    #  bool QSqlDatabase::rollback()
    return self.uglySide.call('ritual_ZN12QSqlDatabase8rollbackEv')

  @overload(QThread)
  @overload(NoneType)
  def moveToThread(self, targetThread: Optional[QThread]) -> bool:
    """
    Calls Qt's 'bool QSqlDatabase::moveToThread(QThread *targetThread)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldatabase.html#moveToThread

    Parameters
    ----------

    targetThread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSqlDatabase::moveToThread(QThread *targetThread)
    return self.uglySide.call(
        'ritual_ZN12QSqlDatabase12moveToThreadEP7QThread',
        self._addressOf(targetThread),
    )
