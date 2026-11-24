//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqldatabase.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qsqldatabase.h>
#include <QtCore/qstring.h>

//  QString QSqlDatabaseDefaultConnectionName::defaultConnectionName()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QSqlDatabaseDefaultConnectionName21defaultConnectionNameEv() {
  return new QString(
      QSqlDatabaseDefaultConnectionName::defaultConnectionName());
}

//  QSqlDatabaseDefaultConnectionName::~QSqlDatabaseDefaultConnectionName()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QSqlDatabaseDefaultConnectionNameD1Ev(
    QSqlDatabaseDefaultConnectionName *self) {
  delete self;
}
