//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlcachedresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  Only a class built on QSqlCachedResult may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlCachedResult : QSqlCachedResult {
  using QSqlCachedResult::data;
  using QSqlCachedResult::isNull;
  using QSqlCachedResult::fetch;
  using QSqlCachedResult::fetchNext;
  using QSqlCachedResult::fetchPrevious;
  using QSqlCachedResult::fetchFirst;
  using QSqlCachedResult::fetchLast;
  using QSqlCachedResult::detachFromResultSet;
  using QSqlCachedResult::setNumericalPrecisionPolicy;
};

//  QSqlCachedResultPrivate *QSqlCachedResult::d_func()
extern "C" Q_DECL_EXPORT
QSqlCachedResultPrivate *ritual_ZN16QSqlCachedResult6d_funcEv(
    QSqlCachedResult *self) {
  return self->d_func();
}

//  const QSqlCachedResultPrivate *QSqlCachedResult::d_func() const
extern "C" Q_DECL_EXPORT
const QSqlCachedResultPrivate *ritual_ZNK16QSqlCachedResult6d_funcEv(
    const QSqlCachedResult *self) {
  return self->d_func();
}

//  void QSqlCachedResult::init(int colCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSqlCachedResult4initEi(
    QSqlCachedResult *self,
    int colCount) {
  self->init(colCount);
}

//  void QSqlCachedResult::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSqlCachedResult7cleanupEv(QSqlCachedResult *self) {
  self->cleanup();
}

//  void QSqlCachedResult::clearValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSqlCachedResult11clearValuesEv(QSqlCachedResult *self) {
  self->clearValues();
}

//  QVariant QSqlCachedResult::data(int i)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN16QSqlCachedResult4dataEi(QSqlCachedResult *self, int i) {
  return new QVariant(self->data(i));
}

//  bool QSqlCachedResult::isNull(int i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult6isNullEi(QSqlCachedResult *self, int i) {
  return self->isNull(i);
}

//  bool QSqlCachedResult::fetch(int i)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult5fetchEi(QSqlCachedResult *self, int i) {
  return self->fetch(i);
}

//  bool QSqlCachedResult::fetchNext()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult9fetchNextEv(QSqlCachedResult *self) {
  return self->fetchNext();
}

//  bool QSqlCachedResult::fetchPrevious()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult13fetchPreviousEv(QSqlCachedResult *self) {
  return self->fetchPrevious();
}

//  bool QSqlCachedResult::fetchFirst()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult10fetchFirstEv(QSqlCachedResult *self) {
  return self->fetchFirst();
}

//  bool QSqlCachedResult::fetchLast()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult9fetchLastEv(QSqlCachedResult *self) {
  return self->fetchLast();
}

//  int QSqlCachedResult::colCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSqlCachedResult8colCountEv(const QSqlCachedResult *self) {
  return self->colCount();
}

//  void QSqlCachedResult::detachFromResultSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSqlCachedResult19detachFromResultSetEv(
    QSqlCachedResult *self) {
  self->detachFromResultSet();
}

//  void QSqlCachedResult::setNumericalPrecisionPolicy(QSql::NumericalPrecisi
//      onPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSqlCachedResult27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlCachedResult *self,
    QSql::NumericalPrecisionPolicy policy) {
  self->setNumericalPrecisionPolicy(policy);
}

//  bool QSqlCachedResult::cacheNext()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSqlCachedResult9cacheNextEv(QSqlCachedResult *self) {
  return self->cacheNext();
}

//  QVariant QSqlCachedResult::data(int i)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN16QSqlCachedResult4dataEi(
    QSqlCachedResult *self,
    int i) {
  return new QVariant(
      static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::data(
          i));
}

//  bool QSqlCachedResult::isNull(int i)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult6isNullEi(
    QSqlCachedResult *self,
    int i) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::isNull(
      i);
}

//  bool QSqlCachedResult::fetch(int i)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult5fetchEi(QSqlCachedResult *self, int i) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::fetch(
      i);
}

//  bool QSqlCachedResult::fetchNext()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult9fetchNextEv(QSqlCachedResult *self) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::fetchNext();
}

//  bool QSqlCachedResult::fetchPrevious()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult13fetchPreviousEv(
    QSqlCachedResult *self) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::fetchPrevious();
}

//  bool QSqlCachedResult::fetchFirst()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult10fetchFirstEv(QSqlCachedResult *self) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::fetchFirst();
}

//  bool QSqlCachedResult::fetchLast()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QSqlCachedResult9fetchLastEv(QSqlCachedResult *self) {
  return static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::fetchLast();
}

//  void QSqlCachedResult::detachFromResultSet()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSqlCachedResult19detachFromResultSetEv(
    QSqlCachedResult *self) {
  static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::detachFromResultSet();
}

//  void QSqlCachedResult::setNumericalPrecisionPolicy(QSql::NumericalPrecisi
//      onPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSqlCachedResult27setNumericalPrecisionPolicyEN4QSql24NumericalPrecisionPolicyE(
    QSqlCachedResult *self,
    QSql::NumericalPrecisionPolicy policy) {
  static_cast<OwnQSqlCachedResult *>(self)->OwnQSqlCachedResult::setNumericalPrecisionPolicy(
      policy);
}
