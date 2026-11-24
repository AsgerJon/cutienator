//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqldriver_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/qsqldriver.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqldriver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSqlDriver *QSqlDriverPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSqlDriver *ritual_ZN17QSqlDriverPrivate6q_funcEv(QSqlDriverPrivate *self) {
  return self->q_func();
}

//  const QSqlDriver *QSqlDriverPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSqlDriver *ritual_ZNK17QSqlDriverPrivate6q_funcEv(
    const QSqlDriverPrivate *self) {
  return self->q_func();
}

//  QSqlDriverPrivate::QSqlDriverPrivate(QSqlDriver::DbmsType type)
extern "C" Q_DECL_EXPORT
QSqlDriverPrivate *ritual_ZN17QSqlDriverPrivateC1EN10QSqlDriver8DbmsTypeE(
    QSqlDriver::DbmsType type) {
  return new QSqlDriverPrivate(type);
}
