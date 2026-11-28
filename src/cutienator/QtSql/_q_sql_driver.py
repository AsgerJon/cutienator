"""
QSqlDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqldriver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from . import QSql

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QSqlDriverPrivate, QSqlError, QSqlField, QSqlIndex
  from . import QSqlRecord, QSqlResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlError = WAIT['QSqlError']
  QSqlField = WAIT['QSqlField']
  QSqlRecord = WAIT['QSqlRecord']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSqlDriver(QObject):
  """
  The cute side of Qt's QSqlDriver: a plain Python object standing in front
  of one C++ QSqlDriver.

  It is built on the cute 'QObject', as Qt's QSqlDriver is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlDriver that has a ritual and that Python can
  call so far, 35 names in all: 'metaObject', 'tr', 'd_func', 'isOpen',
  'isOpenError', 'beginTransaction', 'commitTransaction',
  'rollbackTransaction', 'tables', 'primaryIndex', 'record', 'formatValue',
  'escapeIdentifier', 'sqlStatement', 'lastError', 'handle', 'hasFeature',
  'close', 'createResult', 'open', 'subscribeToNotification',
  'unsubscribeFromNotification', 'subscribedToNotifications',
  'isIdentifierEscaped', 'stripDelimiters', 'setNumericalPrecisionPolicy',
  'numericalPrecisionPolicy', 'dbmsType', 'maximumIdentifierLength',
  'connectionName', 'cancelQuery', 'notification', 'setOpen', 'setOpenError',
  'setLastError'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSqlDriver::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSqlDriver::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QSqlDriverPrivate *QSqlDriver::d_func() const': takes in
    Python what 'QSqlDriverPrivate *QSqlDriver::d_func()' takes.
  - Qt's 'QSqlDriver::~QSqlDriver()': the destructor: Python never removes a
    C++ QSqlDriver.
  - Qt's 'QSqlDriver::QSqlDriver(QSqlDriverPrivate &dd, QObject *parent)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSqlDriver is created at the first use, not by 'QSqlDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlDriver.
  - Qt tells when it has removed the C++ QSqlDriver. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QSqlDriver, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DbmsType(CuteNum):
    """
    The enum 'QSqlDriver::DbmsType' of Qt, with the 10 names Qt gives in it.
    """

    UnknownDbms = Kee[int](0)
    MSSqlServer = Kee[int](1)
    MySqlServer = Kee[int](2)
    PostgreSQL = Kee[int](3)
    Oracle = Kee[int](4)
    Sybase = Kee[int](5)
    SQLite = Kee[int](6)
    Interbase = Kee[int](7)
    DB2 = Kee[int](8)
    MimerSQL = Kee[int](9)

  class DriverFeature(CuteNum):
    """
    The enum 'QSqlDriver::DriverFeature' of Qt, with the 15 names Qt gives in
    it.
    """

    Transactions = Kee[int](0)
    QuerySize = Kee[int](1)
    BLOB = Kee[int](2)
    Unicode = Kee[int](3)
    PreparedQueries = Kee[int](4)
    NamedPlaceholders = Kee[int](5)
    PositionalPlaceholders = Kee[int](6)
    LastInsertId = Kee[int](7)
    BatchOperations = Kee[int](8)
    SimpleLocking = Kee[int](9)
    LowPrecisionNumbers = Kee[int](10)
    EventNotifications = Kee[int](11)
    FinishQuery = Kee[int](12)
    MultipleResultSets = Kee[int](13)
    CancelQuery = Kee[int](14)

  class IdentifierType(CuteNum):
    """
    The enum 'QSqlDriver::IdentifierType' of Qt, with the 2 names Qt gives in
    it.
    """

    FieldName = Kee[int](0)
    TableName = Kee[int](1)

  class NotificationSource(CuteNum):
    """
    The enum 'QSqlDriver::NotificationSource' of Qt, with the 3 names Qt
    gives in it.
    """

    UnknownSource = Kee[int](0)
    SelfSource = Kee[int](1)
    OtherSource = Kee[int](2)

  class StatementType(CuteNum):
    """
    The enum 'QSqlDriver::StatementType' of Qt, with the 5 names Qt gives in
    it.
    """

    WhereStatement = Kee[int](0)
    SelectStatement = Kee[int](1)
    UpdateStatement = Kee[int](2)
    InsertStatement = Kee[int](3)
    DeleteStatement = Kee[int](4)

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
    Calls Qt's 'QString QSqlDriver::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#tr

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
    #  QString QSqlDriver::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QSqlDriver2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlDriver'

  #  A C++ QSqlDriver Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlDriver'

  #  The functions Qt calls itself that QSqlDriver is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'tables': (
          'QStringList QSqlDriver::tables(QSql::TableType) const',
      ),
      'subscribedToNotifications': (
          'QStringList QSqlDriver::subscribedToNotifications() const',
      ),
  }

  #  The functions Qt calls itself that QSqlDriver is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isOpen': (
          ('_ZNK10QSqlDriver6isOpenEv',
           ('bool', 'number', ''),
           ()),
      ),
      'beginTransaction': (
          ('_ZN10QSqlDriver16beginTransactionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'commitTransaction': (
          ('_ZN10QSqlDriver17commitTransactionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'rollbackTransaction': (
          ('_ZN10QSqlDriver19rollbackTransactionEv',
           ('bool', 'number', ''),
           ()),
      ),
      'primaryIndex': (
          ('_ZNK10QSqlDriver12primaryIndexERK7QString',
           ('address', 'value', 'QtSql:QSqlIndex'),
           (
               ('address', 'text', ''),
           )),
      ),
      'record': (
          ('_ZNK10QSqlDriver6recordERK7QString',
           ('address', 'value', 'QtSql:QSqlRecord'),
           (
               ('address', 'text', ''),
           )),
      ),
      'formatValue': (
          ('_ZNK10QSqlDriver11formatValueERK9QSqlFieldb',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtSql:QSqlField'),
               ('bool', 'number', ''),
           )),
      ),
      'escapeIdentifier': (
          ('_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14IdentifierTyp'
           'eE',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
               ('int', 'enum', 'QtSql:QSqlDriver.IdentifierType'),
           )),
      ),
      'sqlStatement': (
          ('_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QStringRK1'
           '0QSqlRecordb',
           ('address', 'text', ''),
           (
               ('int', 'enum', 'QtSql:QSqlDriver.StatementType'),
               ('address', 'text', ''),
               ('address', 'value', 'QtSql:QSqlRecord'),
               ('bool', 'number', ''),
           )),
      ),
      'handle': (
          ('_ZNK10QSqlDriver6handleEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'hasFeature': (
          ('_ZNK10QSqlDriver10hasFeatureENS_13DriverFeatureE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtSql:QSqlDriver.DriverFeature'),
           )),
      ),
      'close': (
          ('_ZN10QSqlDriver5closeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'createResult': (
          ('_ZNK10QSqlDriver12createResultEv',
           ('address', 'address', 'QtSql:QSqlResult'),
           ()),
      ),
      'open': (
          ('_ZN10QSqlDriver4openERK7QStringS2_S2_S2_iS2_',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('address', 'text', ''),
           )),
      ),
      'subscribeToNotification': (
          ('_ZN10QSqlDriver23subscribeToNotificationERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'unsubscribeFromNotification': (
          ('_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'isIdentifierEscaped': (
          ('_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14Identifier'
           'TypeE',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
               ('int', 'enum', 'QtSql:QSqlDriver.IdentifierType'),
           )),
      ),
      'stripDelimiters': (
          ('_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierType'
           'E',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
               ('int', 'enum', 'QtSql:QSqlDriver.IdentifierType'),
           )),
      ),
      'maximumIdentifierLength': (
          ('_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTypeE',
           ('int', 'number', ''),
           (
               ('int', 'enum', 'QtSql:QSqlDriver.IdentifierType'),
           )),
      ),
      'cancelQuery': (
          ('_ZN10QSqlDriver11cancelQueryEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setOpen': (
          ('_ZN10QSqlDriver7setOpenEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setOpenError': (
          ('_ZN10QSqlDriver12setOpenErrorEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setLastError': (
          ('_ZN10QSqlDriver12setLastErrorERK9QSqlError',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtSql:QSqlError'),
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
    Calls Qt's 'const QMetaObject *QSqlDriver::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSqlDriver::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QSqlDriver10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#isOpen
    """
    #  bool QSqlDriver::isOpen() const
    ritual = 'ritual_ZNK10QSqlDriver6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlDriver6isOpenEv'
    return self.uglySide.call(ritual)

  def isOpenError(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::isOpenError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#isOpenError
    """
    #  bool QSqlDriver::isOpenError() const
    return self.uglySide.call('ritual_ZNK10QSqlDriver11isOpenErrorEv')

  @overload(QSql.TableType)
  def tables(self, tableType: QSql.TableType) -> QStringList:
    """
    Calls Qt's 'QStringList QSqlDriver::tables(QSql::TableType tableType)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#tables

    Parameters
    ----------

    tableType : QSql.TableType
      Passed on as its number.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlDriver::tables(QSql::TableType tableType) const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlDriver6tablesEN4QSql9TableTypeE', tableType.value,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def primaryIndex(self, tableName: str) -> QSqlIndex:
    """
    Calls Qt's 'QSqlIndex QSqlDriver::primaryIndex(const QString &tableName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#primaryIndex

    Parameters
    ----------

    tableName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlIndex
      A new cute QSqlIndex around the copy Qt gave back. Python owns it.
    """
    #  QSqlIndex QSqlDriver::primaryIndex(const QString &tableName) const
    ritual = 'ritual_ZNK10QSqlDriver12primaryIndexERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlDriver12primaryIndexERK7QString'
    address = self.uglySide.call(ritual, tableName)
    from . import QSqlIndex
    return QSqlIndex._cuteOwning(address)

  @overload(str)
  def record(self, tableName: str) -> QSqlRecord:
    """
    Calls Qt's 'QSqlRecord QSqlDriver::record(const QString &tableName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#record

    Parameters
    ----------

    tableName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QSqlRecord
      A new cute QSqlRecord around the copy Qt gave back. Python owns it.
    """
    #  QSqlRecord QSqlDriver::record(const QString &tableName) const
    ritual = 'ritual_ZNK10QSqlDriver6recordERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlDriver6recordERK7QString'
    address = self.uglySide.call(ritual, tableName)
    from . import QSqlRecord
    return QSqlRecord._cuteOwning(address)

  @overload(QSqlField)
  @overload(QSqlField, bool)
  def formatValue(self, field: QSqlField, trimStrings: bool = False) -> str:
    """
    Calls Qt's 'QString QSqlDriver::formatValue(const QSqlField &field, bool
    trimStrings) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#formatValue

    Parameters
    ----------

    field : QSqlField
      Passed on as a value: Qt reads the C++ QSqlField, which stays Python's
      own.

    trimStrings : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDriver::formatValue(const QSqlField &field, bool
    #      trimStrings) const
    ritual = 'ritual_ZNK10QSqlDriver11formatValueERK9QSqlFieldb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlDriver11formatValueERK9QSqlFieldb'
    return self.uglySide.call(ritual, self._valueOf(field), trimStrings)

  @overload(str, IdentifierType)
  def escapeIdentifier(self, identifier: str, type: IdentifierType) -> str:
    """
    Calls Qt's 'QString QSqlDriver::escapeIdentifier(const QString
    &identifier, IdentifierType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#escapeIdentifier

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.

    type : IdentifierType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDriver::escapeIdentifier(const QString &identifier,
    #      IdentifierType type) const
    ritual = (
        'ritual_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14Identifier'
        'TypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSqlDriver16escapeIdentifierERK7QStringNS_14Iden'
          'tifierTypeE')
    return self.uglySide.call(ritual, identifier, type.value)

  @overload(StatementType, str, QSqlRecord, bool)
  def sqlStatement(
      self,
      type: StatementType,
      tableName: str,
      rec: QSqlRecord,
      preparedStatement: bool,
  ) -> str:
    """
    Calls Qt's 'QString QSqlDriver::sqlStatement(StatementType type, const
    QString &tableName, const QSqlRecord &rec, bool preparedStatement)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#sqlStatement

    Parameters
    ----------

    type : StatementType
      Passed on as its number.

    tableName : str
      Passed on as it is: a QString is made of it for the call.

    rec : QSqlRecord
      Passed on as a value: Qt reads the C++ QSqlRecord, which stays Python's
      own.

    preparedStatement : bool
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDriver::sqlStatement(StatementType type, const QString
    #      &tableName, const QSqlRecord &rec, bool preparedStatement) const
    ritual = (
        'ritual_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7QString'
        'RK10QSqlRecordb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSqlDriver12sqlStatementENS_13StatementTypeERK7Q'
          'StringRK10QSqlRecordb')
    return self.uglySide.call(
        ritual, type.value, tableName, self._valueOf(rec), preparedStatement,
    )

  def lastError(self) -> QSqlError:
    """
    Calls Qt's 'QSqlError QSqlDriver::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#lastError

    Returns
    -------

    QSqlError
      A new cute QSqlError around the copy Qt gave back. Python owns it.
    """
    #  QSqlError QSqlDriver::lastError() const
    address = self.uglySide.call('ritual_ZNK10QSqlDriver9lastErrorEv')
    from . import QSqlError
    return QSqlError._cuteOwning(address)

  def handle(self) -> QVariant:
    """
    Calls Qt's 'QVariant QSqlDriver::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#handle

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QSqlDriver::handle() const
    ritual = 'ritual_ZNK10QSqlDriver6handleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QSqlDriver6handleEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(DriverFeature)
  def hasFeature(self, f: DriverFeature) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::hasFeature(DriverFeature f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#hasFeature

    Parameters
    ----------

    f : DriverFeature
      Passed on as its number.
    """
    #  bool QSqlDriver::hasFeature(DriverFeature f) const
    return self.uglySide.call(
        'ritual_ZNK10QSqlDriver10hasFeatureENS_13DriverFeatureE', f.value,
    )

  def createResult(self) -> Optional[QSqlResult]:
    """
    Calls Qt's 'QSqlResult *QSqlDriver::createResult() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#createResult

    Returns
    -------

    Optional[QSqlResult]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlResult *QSqlDriver::createResult() const
    address = self.uglySide.call('ritual_ZNK10QSqlDriver12createResultEv')
    from . import QSqlResult
    return QSqlResult._cuteAt(address)

  def subscribedToNotifications(self) -> QStringList:
    """
    Calls Qt's 'QStringList QSqlDriver::subscribedToNotifications() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#subscribedToNotifications

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QSqlDriver::subscribedToNotifications() const
    address = self.uglySide.call(
        'ritual_ZNK10QSqlDriver25subscribedToNotificationsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str, IdentifierType)
  def isIdentifierEscaped(
      self,
      identifier: str,
      type: IdentifierType,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::isIdentifierEscaped(const QString
    &identifier, IdentifierType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#isIdentifierEscaped

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.

    type : IdentifierType
      Passed on as its number.
    """
    #  bool QSqlDriver::isIdentifierEscaped(const QString &identifier,
    #      IdentifierType type) const
    ritual = (
        'ritual_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14Identif'
        'ierTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSqlDriver19isIdentifierEscapedERK7QStringNS_14I'
          'dentifierTypeE')
    return self.uglySide.call(ritual, identifier, type.value)

  @overload(str, IdentifierType)
  def stripDelimiters(self, identifier: str, type: IdentifierType) -> str:
    """
    Calls Qt's 'QString QSqlDriver::stripDelimiters(const QString
    &identifier, IdentifierType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#stripDelimiters

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.

    type : IdentifierType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDriver::stripDelimiters(const QString &identifier,
    #      IdentifierType type) const
    ritual = (
        'ritual_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14IdentifierT'
        'ypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSqlDriver15stripDelimitersERK7QStringNS_14Ident'
          'ifierTypeE')
    return self.uglySide.call(ritual, identifier, type.value)

  def numericalPrecisionPolicy(self) -> QSql.NumericalPrecisionPolicy:
    """
    Calls Qt's 'QSql::NumericalPrecisionPolicy
    QSqlDriver::numericalPrecisionPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#numericalPrecisionPolicy

    Returns
    -------

    QSql.NumericalPrecisionPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSql.NumericalPrecisionPolicy(number)' gives.
    """
    #  QSql::NumericalPrecisionPolicy QSqlDriver::numericalPrecisionPolicy()
    #      const
    return QSql.NumericalPrecisionPolicy(self.uglySide.call(
        'ritual_ZNK10QSqlDriver24numericalPrecisionPolicyEv',
    ))

  def dbmsType(self) -> DbmsType:
    """
    Calls Qt's 'DbmsType QSqlDriver::dbmsType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#dbmsType

    Returns
    -------

    DbmsType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DbmsType(number)' gives.
    """
    #  DbmsType QSqlDriver::dbmsType() const
    return QSqlDriver.DbmsType(self.uglySide.call(
        'ritual_ZNK10QSqlDriver8dbmsTypeEv',
    ))

  @overload(IdentifierType)
  def maximumIdentifierLength(self, type: IdentifierType) -> int:
    """
    Calls Qt's 'int QSqlDriver::maximumIdentifierLength(IdentifierType type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#maximumIdentifierLength

    Parameters
    ----------

    type : IdentifierType
      Passed on as its number.
    """
    #  int QSqlDriver::maximumIdentifierLength(IdentifierType type) const
    ritual = (
        'ritual_ZNK10QSqlDriver23maximumIdentifierLengthENS_14IdentifierTyp'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK10QSqlDriver23maximumIdentifierLengthENS_14Identif'
          'ierTypeE')
    return self.uglySide.call(ritual, type.value)

  def connectionName(self) -> str:
    """
    Calls Qt's 'QString QSqlDriver::connectionName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#connectionName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlDriver::connectionName() const
    return self.uglySide.call('ritual_ZNK10QSqlDriver14connectionNameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSql.NumericalPrecisionPolicy)
  def setNumericalPrecisionPolicy(
      self,
      precisionPolicy: QSql.NumericalPrecisionPolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QSqlDriver::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy
    precisionPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#setNumericalPrecisionPolicy

    Parameters
    ----------

    precisionPolicy : QSql.NumericalPrecisionPolicy
      Passed on as its number.
    """
    #  void QSqlDriver::setNumericalPrecisionPolicy(QSql::
    #      NumericalPrecisionPolicy precisionPolicy)
    self.uglySide.call(
        'ritual_ZN10QSqlDriver27setNumericalPrecisionPolicyEN4QSql24Numeric'
        'alPrecisionPolicyE',
        precisionPolicy.value,
    )

  @overload(bool)
  def setOpen(self, o: bool) -> None:
    """
    Calls Qt's 'void QSqlDriver::setOpen(bool o)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#setOpen

    Parameters
    ----------

    o : bool
      Passed on as it is.
    """
    #  void QSqlDriver::setOpen(bool o)
    ritual = 'ritual_ZN10QSqlDriver7setOpenEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver7setOpenEb'
    self.uglySide.call(ritual, o)

  @overload(bool)
  def setOpenError(self, e: bool) -> None:
    """
    Calls Qt's 'void QSqlDriver::setOpenError(bool e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#setOpenError

    Parameters
    ----------

    e : bool
      Passed on as it is.
    """
    #  void QSqlDriver::setOpenError(bool e)
    ritual = 'ritual_ZN10QSqlDriver12setOpenErrorEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver12setOpenErrorEb'
    self.uglySide.call(ritual, e)

  @overload(QSqlError)
  def setLastError(self, e: QSqlError) -> None:
    """
    Calls Qt's 'void QSqlDriver::setLastError(const QSqlError &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#setLastError

    Parameters
    ----------

    e : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  void QSqlDriver::setLastError(const QSqlError &e)
    ritual = 'ritual_ZN10QSqlDriver12setLastErrorERK9QSqlError'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver12setLastErrorERK9QSqlError'
    self.uglySide.call(ritual, self._valueOf(e))

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
    Notes what was given, for Qt's 'QSqlDriver::QSqlDriver(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#QSqlDriver

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSqlDriver::QSqlDriver(QObject *parent)
    self._noteCreation(QSqlDriver, lambda: Rituals.call(
        'ritual_ZN10QSqlDriverC1EP7QObject',
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

  def d_func(self) -> Optional[QSqlDriverPrivate]:
    """
    Calls Qt's 'QSqlDriverPrivate *QSqlDriver::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#d_func

    Returns
    -------

    Optional[QSqlDriverPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlDriverPrivate *QSqlDriver::d_func()
    address = self.uglySide.call('ritual_ZN10QSqlDriver6d_funcEv')
    from . import QSqlDriverPrivate
    return QSqlDriverPrivate._cuteAt(address)

  def beginTransaction(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::beginTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#beginTransaction
    """
    #  bool QSqlDriver::beginTransaction()
    ritual = 'ritual_ZN10QSqlDriver16beginTransactionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver16beginTransactionEv'
    return self.uglySide.call(ritual)

  def commitTransaction(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::commitTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#commitTransaction
    """
    #  bool QSqlDriver::commitTransaction()
    ritual = 'ritual_ZN10QSqlDriver17commitTransactionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver17commitTransactionEv'
    return self.uglySide.call(ritual)

  def rollbackTransaction(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::rollbackTransaction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#rollbackTransaction
    """
    #  bool QSqlDriver::rollbackTransaction()
    ritual = 'ritual_ZN10QSqlDriver19rollbackTransactionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver19rollbackTransactionEv'
    return self.uglySide.call(ritual)

  def close(self) -> None:
    """
    Calls Qt's 'void QSqlDriver::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#close
    """
    #  void QSqlDriver::close()
    self.uglySide.call('ritual_ZN10QSqlDriver5closeEv')

  @overload(str)
  @overload(str, str)
  @overload(str, str, str)
  @overload(str, str, str, str)
  @overload(str, str, str, str, int)
  @overload(str, str, str, str, int, str)
  def open(
      self,
      db: str,
      user: str = '',
      password: str = '',
      host: str = '',
      port: int = -1,
      connOpts: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::open(const QString &db, const QString &user,
    const QString &password, const QString &host, int port, const QString
    &connOpts)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#open

    Parameters
    ----------

    db : str
      Passed on as it is: a QString is made of it for the call.

    user : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    password : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    host : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    connOpts : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QSqlDriver::open(const QString &db, const QString &user, const
    #      QString &password, const QString &host, int port, const QString
    #      &connOpts)
    return self.uglySide.call(
        'ritual_ZN10QSqlDriver4openERK7QStringS2_S2_S2_iS2_',
        db, user, password, host, port, connOpts,
    )

  @overload(str)
  def subscribeToNotification(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::subscribeToNotification(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#subscribeToNotification

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlDriver::subscribeToNotification(const QString &name)
    ritual = 'ritual_ZN10QSqlDriver23subscribeToNotificationERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSqlDriver23subscribeToNotificationERK7QString')
    return self.uglySide.call(ritual, name)

  @overload(str)
  def unsubscribeFromNotification(self, name: str) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::unsubscribeFromNotification(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsqldriver.html#unsubscribeFromNotification

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlDriver::unsubscribeFromNotification(const QString &name)
    ritual = 'ritual_ZN10QSqlDriver27unsubscribeFromNotificationERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QSqlDriver27unsubscribeFromNotificationERK7QStrin'
          'g')
    return self.uglySide.call(ritual, name)

  def cancelQuery(self) -> bool:
    """
    Calls Qt's 'bool QSqlDriver::cancelQuery()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#cancelQuery
    """
    #  bool QSqlDriver::cancelQuery()
    ritual = 'ritual_ZN10QSqlDriver11cancelQueryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QSqlDriver11cancelQueryEv'
    return self.uglySide.call(ritual)

  @overload(str, NotificationSource, QVariant)
  def notification(
      self,
      name: str,
      source: NotificationSource,
      payload: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QSqlDriver::notification(const QString &name,
    QSqlDriver::NotificationSource source, const QVariant &payload)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqldriver.html#notification

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    source : NotificationSource
      Passed on as its number.

    payload : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QSqlDriver::notification(const QString &name,
    #      QSqlDriver::NotificationSource source, const QVariant &payload)
    self.uglySide.call(
        'ritual_ZN10QSqlDriver12notificationERK7QStringNS_18NotificationSou'
        'rceERK8QVariant',
        name, source.value, self._valueOf(payload),
    )
