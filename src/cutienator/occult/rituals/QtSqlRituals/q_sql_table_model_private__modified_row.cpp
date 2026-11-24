//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqltablemodel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSql/qtsqlglobal.h>
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqltablemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/qsqlrecord.h>
#include <QtCore/qvariant.h>

//  QSqlTableModelPrivate::ModifiedRow::ModifiedRow(Op o, const QSqlRecord
//      &r)
extern "C" Q_DECL_EXPORT
QSqlTableModelPrivate::ModifiedRow *ritual_ZN21QSqlTableModelPrivate11ModifiedRowC1ENS_2OpERK10QSqlRecord(
    QSqlTableModelPrivate::Op o,
    const QSqlRecord *r) {
  return new QSqlTableModelPrivate::ModifiedRow(o, *r);
}

//  Op QSqlTableModelPrivate::ModifiedRow::op() const
extern "C" Q_DECL_EXPORT
QSqlTableModelPrivate::Op ritual_ZNK21QSqlTableModelPrivate11ModifiedRow2opEv(
    const QSqlTableModelPrivate::ModifiedRow *self) {
  return self->op();
}

//  void QSqlTableModelPrivate::ModifiedRow::setOp(Op o)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRow5setOpENS_2OpE(
    QSqlTableModelPrivate::ModifiedRow *self,
    QSqlTableModelPrivate::Op o) {
  self->setOp(o);
}

//  const QSqlRecord &QSqlTableModelPrivate::ModifiedRow::rec() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK21QSqlTableModelPrivate11ModifiedRow3recEv(
    const QSqlTableModelPrivate::ModifiedRow *self) {
  return new QSqlRecord(self->rec());
}

//  void QSqlTableModelPrivate::ModifiedRow::setValue(int c, const QVariant
//      &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRow8setValueEiRK8QVariant(
    QSqlTableModelPrivate::ModifiedRow *self,
    int c,
    const QVariant *v) {
  self->setValue(c, *v);
}

//  bool QSqlTableModelPrivate::ModifiedRow::submitted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSqlTableModelPrivate11ModifiedRow9submittedEv(
    const QSqlTableModelPrivate::ModifiedRow *self) {
  return self->submitted();
}

//  void QSqlTableModelPrivate::ModifiedRow::setSubmitted()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRow12setSubmittedEv(
    QSqlTableModelPrivate::ModifiedRow *self) {
  self->setSubmitted();
}

//  void QSqlTableModelPrivate::ModifiedRow::refresh(bool exists, const
//      QSqlRecord &newvals)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRow7refreshEbRK10QSqlRecord(
    QSqlTableModelPrivate::ModifiedRow *self,
    bool exists,
    const QSqlRecord *newvals) {
  self->refresh(exists, *newvals);
}

//  bool QSqlTableModelPrivate::ModifiedRow::insert() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSqlTableModelPrivate11ModifiedRow6insertEv(
    const QSqlTableModelPrivate::ModifiedRow *self) {
  return self->insert();
}

//  void QSqlTableModelPrivate::ModifiedRow::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRow6revertEv(
    QSqlTableModelPrivate::ModifiedRow *self) {
  self->revert();
}

//  QSqlRecord QSqlTableModelPrivate::ModifiedRow::primaryValues(const
//      QSqlRecord &pi) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK21QSqlTableModelPrivate11ModifiedRow13primaryValuesERK10QSqlRecord(
    const QSqlTableModelPrivate::ModifiedRow *self,
    const QSqlRecord *pi) {
  return new QSqlRecord(self->primaryValues(*pi));
}

//  QSqlTableModelPrivate::ModifiedRow::~ModifiedRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSqlTableModelPrivate11ModifiedRowD1Ev(
    QSqlTableModelPrivate::ModifiedRow *self) {
  delete self;
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
