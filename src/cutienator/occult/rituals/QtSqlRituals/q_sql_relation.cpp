//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlrelationaltablemodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtSql/qtsqlglobal.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/qsqlrelationaltablemodel.h>
#include <QtCore/qstring.h>

//  QSqlRelation::QSqlRelation()
extern "C" Q_DECL_EXPORT
QSqlRelation *ritual_ZN12QSqlRelationC1Ev() {
  return new QSqlRelation();
}

//  QSqlRelation::QSqlRelation(const QString &aTableName, const QString
//      &indexCol, const QString &displayCol)
extern "C" Q_DECL_EXPORT
QSqlRelation *ritual_ZN12QSqlRelationC1ERK7QStringS2_S2_(
    const QString *aTableName,
    const QString *indexCol,
    const QString *displayCol) {
  return new QSqlRelation(*aTableName, *indexCol, *displayCol);
}

//  QString QSqlRelation::tableName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlRelation9tableNameEv(const QSqlRelation *self) {
  return new QString(self->tableName());
}

//  QString QSqlRelation::indexColumn() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlRelation11indexColumnEv(const QSqlRelation *self) {
  return new QString(self->indexColumn());
}

//  QString QSqlRelation::displayColumn() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSqlRelation13displayColumnEv(
    const QSqlRelation *self) {
  return new QString(self->displayColumn());
}

//  bool QSqlRelation::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSqlRelation7isValidEv(const QSqlRelation *self) {
  return self->isValid();
}

//  QSqlRelation::~QSqlRelation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSqlRelationD1Ev(QSqlRelation *self) {
  delete self;
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
