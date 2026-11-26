//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlquery.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqlquery.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqldatabase.h>
#include <QtCore/qanystringview.h>
#include <QtSql/qsqlerror.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QSqlQuery::QSqlQuery(QSqlResult *r)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryC1EP10QSqlResult(QSqlResult *r) {
  return new QSqlQuery(r);
}

//  QSqlQuery::QSqlQuery(const QString &query, const QSqlDatabase &db)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryC1ERK7QStringRK12QSqlDatabase(
    const QString *query,
    const QSqlDatabase *db) {
  return new QSqlQuery(*query, *db);
}

//  QSqlQuery::QSqlQuery(const QSqlDatabase &db)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryC1ERK12QSqlDatabase(const QSqlDatabase *db) {
  return new QSqlQuery(*db);
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)
//  QSqlQuery::QSqlQuery(const QSqlQuery &other)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryC1ERKS_(const QSqlQuery *other) {
  return new QSqlQuery(*other);
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)
//  QSqlQuery &QSqlQuery::operator=(const QSqlQuery &other)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryaSERKS_(
    QSqlQuery *self,
    const QSqlQuery *other) {
  return &(self->operator=(*other));
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)

//  QSqlQuery::QSqlQuery(QSqlQuery &&other)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryC1EOS_(QSqlQuery *other) {
  return new QSqlQuery(std::move(*other));
}

//  QSqlQuery &QSqlQuery::operator=(QSqlQuery &&other)
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZN9QSqlQueryaSEOS_(QSqlQuery *self, QSqlQuery *other) {
  return &(self->operator=(std::move(*other)));
}

//  QSqlQuery::~QSqlQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQueryD1Ev(QSqlQuery *self) {
  delete self;
}

//  void QSqlQuery::swap(QSqlQuery &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery4swapERS_(QSqlQuery *self, QSqlQuery *other) {
  self->swap(*other);
}

//  bool QSqlQuery::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery7isValidEv(const QSqlQuery *self) {
  return self->isValid();
}

//  bool QSqlQuery::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery8isActiveEv(const QSqlQuery *self) {
  return self->isActive();
}

//  bool QSqlQuery::isNull(int field) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery6isNullEi(const QSqlQuery *self, int field) {
  return self->isNull(field);
}

//  bool QSqlQuery::isNull(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery6isNullE14QAnyStringView(
    const QSqlQuery *self,
    const QString *name) {
  return self->isNull(QAnyStringView(*name));
}

//  int QSqlQuery::at() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlQuery2atEv(const QSqlQuery *self) {
  return self->at();
}

//  QString QSqlQuery::lastQuery() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlQuery9lastQueryEv(const QSqlQuery *self) {
  return new QString(self->lastQuery());
}

//  int QSqlQuery::numRowsAffected() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlQuery15numRowsAffectedEv(const QSqlQuery *self) {
  return self->numRowsAffected();
}

//  QSqlError QSqlQuery::lastError() const
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZNK9QSqlQuery9lastErrorEv(const QSqlQuery *self) {
  return new QSqlError(self->lastError());
}

//  bool QSqlQuery::isSelect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery8isSelectEv(const QSqlQuery *self) {
  return self->isSelect();
}

//  int QSqlQuery::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QSqlQuery4sizeEv(const QSqlQuery *self) {
  return self->size();
}

//  const QSqlDriver *QSqlQuery::driver() const
extern "C" Q_DECL_EXPORT
const QSqlDriver *ritual_ZNK9QSqlQuery6driverEv(const QSqlQuery *self) {
  return self->driver();
}

//  const QSqlResult *QSqlQuery::result() const
extern "C" Q_DECL_EXPORT
const QSqlResult *ritual_ZNK9QSqlQuery6resultEv(const QSqlQuery *self) {
  return self->result();
}

//  bool QSqlQuery::isForwardOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery13isForwardOnlyEv(const QSqlQuery *self) {
  return self->isForwardOnly();
}

//  QSqlRecord QSqlQuery::record() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK9QSqlQuery6recordEv(const QSqlQuery *self) {
  return new QSqlRecord(self->record());
}

//  void QSqlQuery::setForwardOnly(bool forward)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery14setForwardOnlyEb(QSqlQuery *self, bool forward) {
  self->setForwardOnly(forward);
}

//  bool QSqlQuery::exec(const QString &query)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery4execERK7QString(
    QSqlQuery *self,
    const QString *query) {
  return self->exec(*query);
}

//  QVariant QSqlQuery::value(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlQuery5valueEi(const QSqlQuery *self, int i) {
  return new QVariant(self->value(i));
}

//  QVariant QSqlQuery::value(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlQuery5valueE14QAnyStringView(
    const QSqlQuery *self,
    const QString *name) {
  return new QVariant(self->value(QAnyStringView(*name)));
}

//  void
//      QSqlQuery::setNumericalPrecisionPolicy(QSql::NumericalPrecisionPolicy
//      precisionPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlQuery *self,
    QSql::NumericalPrecisionPolicy precisionPolicy) {
  self->setNumericalPrecisionPolicy(precisionPolicy);
}

//  QSql::NumericalPrecisionPolicy QSqlQuery::numericalPrecisionPolicy()
//      const
extern "C" Q_DECL_EXPORT
QSql::NumericalPrecisionPolicy ritual_ZNK9QSqlQuery24numericalPrecisionPolicyEv(
    const QSqlQuery *self) {
  return self->numericalPrecisionPolicy();
}

//  void QSqlQuery::setPositionalBindingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery27setPositionalBindingEnabledEb(
    QSqlQuery *self,
    bool enable) {
  self->setPositionalBindingEnabled(enable);
}

//  bool QSqlQuery::isPositionalBindingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSqlQuery26isPositionalBindingEnabledEv(
    const QSqlQuery *self) {
  return self->isPositionalBindingEnabled();
}

//  bool QSqlQuery::seek(int i, bool relative)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery4seekEib(QSqlQuery *self, int i, bool relative) {
  return self->seek(i, relative);
}

//  bool QSqlQuery::next()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery4nextEv(QSqlQuery *self) {
  return self->next();
}

//  bool QSqlQuery::previous()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery8previousEv(QSqlQuery *self) {
  return self->previous();
}

//  bool QSqlQuery::first()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery5firstEv(QSqlQuery *self) {
  return self->first();
}

//  bool QSqlQuery::last()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery4lastEv(QSqlQuery *self) {
  return self->last();
}

//  void QSqlQuery::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery5clearEv(QSqlQuery *self) {
  self->clear();
}

//  bool QSqlQuery::exec()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery4execEv(QSqlQuery *self) {
  return self->exec();
}

//  bool QSqlQuery::execBatch(BatchExecutionMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery9execBatchENS_18BatchExecutionModeE(
    QSqlQuery *self,
    QSqlQuery::BatchExecutionMode mode) {
  return self->execBatch(mode);
}

//  bool QSqlQuery::prepare(const QString &query)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery7prepareERK7QString(
    QSqlQuery *self,
    const QString *query) {
  return self->prepare(*query);
}

//  void QSqlQuery::bindValue(const QString &placeholder, const QVariant
//      &val, QSql::ParamType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery9bindValueERK7QStringRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlQuery *self,
    const QString *placeholder,
    const QVariant *val,
    int type) {
  self->bindValue(
      *placeholder,
      *val,
      QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  void QSqlQuery::bindValue(int pos, const QVariant &val, QSql::ParamType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery9bindValueEiRK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlQuery *self,
    int pos,
    const QVariant *val,
    int type) {
  self->bindValue(pos, *val, QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  void QSqlQuery::addBindValue(const QVariant &val, QSql::ParamType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery12addBindValueERK8QVariant6QFlagsIN4QSql13ParamTypeFlagEE(
    QSqlQuery *self,
    const QVariant *val,
    int type) {
  self->addBindValue(*val, QFlags<QSql::ParamTypeFlag>::fromInt(type));
}

//  QVariant QSqlQuery::boundValue(const QString &placeholder) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlQuery10boundValueERK7QString(
    const QSqlQuery *self,
    const QString *placeholder) {
  return new QVariant(self->boundValue(*placeholder));
}

//  QVariant QSqlQuery::boundValue(int pos) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlQuery10boundValueEi(
    const QSqlQuery *self,
    int pos) {
  return new QVariant(self->boundValue(pos));
}

//  QVariantList QSqlQuery::boundValues() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK9QSqlQuery11boundValuesEv(const QSqlQuery *self) {
  return new QList<QVariant>(self->boundValues());
}

//  QStringList QSqlQuery::boundValueNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QSqlQuery15boundValueNamesEv(
    const QSqlQuery *self) {
  return new QList<QString>(self->boundValueNames());
}

//  QString QSqlQuery::boundValueName(int pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlQuery14boundValueNameEi(
    const QSqlQuery *self,
    int pos) {
  return new QString(self->boundValueName(pos));
}

//  QString QSqlQuery::executedQuery() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSqlQuery13executedQueryEv(const QSqlQuery *self) {
  return new QString(self->executedQuery());
}

//  QVariant QSqlQuery::lastInsertId() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QSqlQuery12lastInsertIdEv(const QSqlQuery *self) {
  return new QVariant(self->lastInsertId());
}

//  void QSqlQuery::finish()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSqlQuery6finishEv(QSqlQuery *self) {
  self->finish();
}

//  bool QSqlQuery::nextResult()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSqlQuery10nextResultEv(QSqlQuery *self) {
  return self->nextResult();
}
