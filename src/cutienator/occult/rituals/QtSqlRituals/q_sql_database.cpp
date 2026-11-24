//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqldatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqldatabase.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqlindex.h>
#include <QtSql/qsqlrecord.h>
#include <QtSql/qsqlquery.h>
#include <QtSql/qsqlerror.h>
#include <QtCore/qlist.h>

//  QSqlDatabase::QSqlDatabase()
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabaseC1Ev() {
  return new QSqlDatabase();
}

//  QSqlDatabase::QSqlDatabase(const QSqlDatabase &other)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabaseC1ERKS_(const QSqlDatabase *other) {
  return new QSqlDatabase(*other);
}

//  QSqlDatabase::~QSqlDatabase()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabaseD1Ev(QSqlDatabase *self) {
  delete self;
}

//  bool QSqlDatabase::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase4openEv(QSqlDatabase *self) {
  return self->open();
}

//  bool QSqlDatabase::open(const QString &user, const QString &password)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase4openERK7QStringS2_(
    QSqlDatabase *self,
    const QString *user,
    const QString *password) {
  return self->open(*user, *password);
}

//  void QSqlDatabase::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase5closeEv(QSqlDatabase *self) {
  self->close();
}

//  bool QSqlDatabase::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSqlDatabase6isOpenEv(const QSqlDatabase *self) {
  return self->isOpen();
}

//  bool QSqlDatabase::isOpenError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSqlDatabase11isOpenErrorEv(const QSqlDatabase *self) {
  return self->isOpenError();
}

//  QStringList QSqlDatabase::tables(QSql::TableType type) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QSqlDatabase6tablesEN4QSql9TableTypeE(
    const QSqlDatabase *self,
    QSql::TableType type) {
  return new QList<QString>(self->tables(type));
}

//  QSqlIndex QSqlDatabase::primaryIndex(const QString &tablename) const
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZNK12QSqlDatabase12primaryIndexERK7QString(
    const QSqlDatabase *self,
    const QString *tablename) {
  return new QSqlIndex(self->primaryIndex(*tablename));
}

//  QSqlRecord QSqlDatabase::record(const QString &tablename) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK12QSqlDatabase6recordERK7QString(
    const QSqlDatabase *self,
    const QString *tablename) {
  return new QSqlRecord(self->record(*tablename));
}

#if QT_DEPRECATED_SINCE(6, 6)
//  QSqlQuery QSqlDatabase::exec(const QString &query) const
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZNK12QSqlDatabase4execERK7QString(
    const QSqlDatabase *self,
    const QString *query) {
  return new QSqlQuery(self->exec(*query));
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  QSqlError QSqlDatabase::lastError() const
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZNK12QSqlDatabase9lastErrorEv(const QSqlDatabase *self) {
  return new QSqlError(self->lastError());
}

//  bool QSqlDatabase::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSqlDatabase7isValidEv(const QSqlDatabase *self) {
  return self->isValid();
}

//  bool QSqlDatabase::transaction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase11transactionEv(QSqlDatabase *self) {
  return self->transaction();
}

//  bool QSqlDatabase::commit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase6commitEv(QSqlDatabase *self) {
  return self->commit();
}

//  bool QSqlDatabase::rollback()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase8rollbackEv(QSqlDatabase *self) {
  return self->rollback();
}

//  void QSqlDatabase::setDatabaseName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase15setDatabaseNameERK7QString(
    QSqlDatabase *self,
    const QString *name) {
  self->setDatabaseName(*name);
}

//  void QSqlDatabase::setUserName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase11setUserNameERK7QString(
    QSqlDatabase *self,
    const QString *name) {
  self->setUserName(*name);
}

//  void QSqlDatabase::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase11setPasswordERK7QString(
    QSqlDatabase *self,
    const QString *password) {
  self->setPassword(*password);
}

//  void QSqlDatabase::setHostName(const QString &host)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase11setHostNameERK7QString(
    QSqlDatabase *self,
    const QString *host) {
  self->setHostName(*host);
}

//  void QSqlDatabase::setPort(int p)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase7setPortEi(QSqlDatabase *self, int p) {
  self->setPort(p);
}

//  void QSqlDatabase::setConnectOptions(const QString &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase17setConnectOptionsERK7QString(
    QSqlDatabase *self,
    const QString *options) {
  self->setConnectOptions(*options);
}

//  QString QSqlDatabase::databaseName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase12databaseNameEv(const QSqlDatabase *self) {
  return new QString(self->databaseName());
}

//  QString QSqlDatabase::userName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase8userNameEv(const QSqlDatabase *self) {
  return new QString(self->userName());
}

//  QString QSqlDatabase::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase8passwordEv(const QSqlDatabase *self) {
  return new QString(self->password());
}

//  QString QSqlDatabase::hostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase8hostNameEv(const QSqlDatabase *self) {
  return new QString(self->hostName());
}

//  QString QSqlDatabase::driverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase10driverNameEv(const QSqlDatabase *self) {
  return new QString(self->driverName());
}

//  int QSqlDatabase::port() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSqlDatabase4portEv(const QSqlDatabase *self) {
  return self->port();
}

//  QString QSqlDatabase::connectOptions() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase14connectOptionsEv(
    const QSqlDatabase *self) {
  return new QString(self->connectOptions());
}

//  QString QSqlDatabase::connectionName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlDatabase14connectionNameEv(
    const QSqlDatabase *self) {
  return new QString(self->connectionName());
}

//  void
//      QSqlDatabase::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPol
//      icy precisionPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlDatabase *self,
    QSql::NumericalPrecisionPolicy precisionPolicy) {
  self->setNumericalPrecisionPolicy(precisionPolicy);
}

//  QSql::NumericalPrecisionPolicy QSqlDatabase::numericalPrecisionPolicy()
//      const
extern "C" Q_DECL_EXPORT
QSql::NumericalPrecisionPolicy ritual_ZNK12QSqlDatabase24numericalPrecisionPolicyEv(
    const QSqlDatabase *self) {
  return self->numericalPrecisionPolicy();
}

//  bool QSqlDatabase::moveToThread(QThread *targetThread)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase12moveToThreadEP7QThread(
    QSqlDatabase *self,
    QThread *targetThread) {
  return self->moveToThread(targetThread);
}

//  QThread *QSqlDatabase::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK12QSqlDatabase6threadEv(const QSqlDatabase *self) {
  return self->thread();
}

//  QSqlDriver *QSqlDatabase::driver() const
extern "C" Q_DECL_EXPORT
QSqlDriver *ritual_ZNK12QSqlDatabase6driverEv(const QSqlDatabase *self) {
  return self->driver();
}

//  QSqlDatabase QSqlDatabase::addDatabase(const QString &type, const QString
//      &connectionName)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabase11addDatabaseERK7QStringS2_(
    const QString *type,
    const QString *connectionName) {
  return new QSqlDatabase(QSqlDatabase::addDatabase(*type, *connectionName));
}

//  QSqlDatabase QSqlDatabase::addDatabase(QSqlDriver *driver, const QString
//      &connectionName)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabase11addDatabaseEP10QSqlDriverRK7QString(
    QSqlDriver *driver,
    const QString *connectionName) {
  return new QSqlDatabase(
      QSqlDatabase::addDatabase(
          driver,
          *connectionName));
}

//  QSqlDatabase QSqlDatabase::cloneDatabase(const QSqlDatabase &other, const
//      QString &connectionName)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabase13cloneDatabaseERKS_RK7QString(
    const QSqlDatabase *other,
    const QString *connectionName) {
  return new QSqlDatabase(
      QSqlDatabase::cloneDatabase(
          *other,
          *connectionName));
}

//  QSqlDatabase QSqlDatabase::cloneDatabase(const QString &other, const
//      QString &connectionName)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabase13cloneDatabaseERK7QStringS2_(
    const QString *other,
    const QString *connectionName) {
  return new QSqlDatabase(
      QSqlDatabase::cloneDatabase(
          *other,
          *connectionName));
}

//  QSqlDatabase QSqlDatabase::database(const QString &connectionName, bool
//      open)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabase8databaseERK7QStringb(
    const QString *connectionName,
    bool open) {
  return new QSqlDatabase(QSqlDatabase::database(*connectionName, open));
}

//  void QSqlDatabase::removeDatabase(const QString &connectionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase14removeDatabaseERK7QString(
    const QString *connectionName) {
  QSqlDatabase::removeDatabase(*connectionName);
}

//  bool QSqlDatabase::contains(const QString &connectionName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase8containsERK7QString(
    const QString *connectionName) {
  return QSqlDatabase::contains(*connectionName);
}

//  QStringList QSqlDatabase::drivers()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN12QSqlDatabase7driversEv() {
  return new QList<QString>(QSqlDatabase::drivers());
}

//  QStringList QSqlDatabase::connectionNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN12QSqlDatabase15connectionNamesEv() {
  return new QList<QString>(QSqlDatabase::connectionNames());
}

//  void QSqlDatabase::registerSqlDriver(const QString &name,
//      QSqlDriverCreatorBase *creator)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlDatabase17registerSqlDriverERK7QStringP21QSqlDriverCreatorBase(
    const QString *name,
    QSqlDriverCreatorBase *creator) {
  QSqlDatabase::registerSqlDriver(*name, creator);
}

//  bool QSqlDatabase::isDriverAvailable(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSqlDatabase17isDriverAvailableERK7QString(
    const QString *name) {
  return QSqlDatabase::isDriverAvailable(*name);
}

//  QSqlDatabase::QSqlDatabase(const QString &type)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabaseC1ERK7QString(const QString *type) {
  return new QSqlDatabase(*type);
}

//  QSqlDatabase::QSqlDatabase(QSqlDriver *driver)
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZN12QSqlDatabaseC1EP10QSqlDriver(QSqlDriver *driver) {
  return new QSqlDatabase(driver);
}
