//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/6.12.0/QtSql/private/qsqlresult_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSql/6.12.0/QtSql/private/qtsqlglobal_p.h>
#include <QtSql/QtSql>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSql/6.12.0/QtSql/private/qsqlresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QHolder::QHolder(const QString &hldr, qsizetype index)
extern "C" Q_DECL_EXPORT
QHolder *ritual_ZN7QHolderC1ERK7QStringx(
    const QString *hldr,
    qsizetype index) {
  return new QHolder(*hldr, index);
}

//  bool QHolder::operator==(const QHolder &h) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QHoldereqERKS_(const QHolder *self, const QHolder *h) {
  return self->operator==(*h);
}

//  bool QHolder::operator!=(const QHolder &h) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QHolderneERKS_(const QHolder *self, const QHolder *h) {
  return self->operator!=(*h);
}

//  QHolder::~QHolder()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QHolderD1Ev(QHolder *self) {
  delete self;
}
