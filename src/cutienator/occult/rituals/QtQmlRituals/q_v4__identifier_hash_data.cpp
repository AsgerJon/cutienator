//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4identifierhashdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4identifierhashdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::IdentifierHashData::IdentifierHashData(IdentifierTable *table, int
//      numBits)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHashData *ritual_ZN3QV418IdentifierHashDataC1EPNS_15IdentifierTableEi(
    QV4::IdentifierTable *table,
    int numBits) {
  return new QV4::IdentifierHashData(table, numBits);
}

//  QV4::IdentifierHashData::IdentifierHashData(IdentifierHashData *other)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHashData *ritual_ZN3QV418IdentifierHashDataC1EPS0_(
    QV4::IdentifierHashData *other) {
  return new QV4::IdentifierHashData(other);
}

//  QV4::IdentifierHashData::~IdentifierHashData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418IdentifierHashDataD1Ev(QV4::IdentifierHashData *self) {
  delete self;
}

//  void QV4::IdentifierHashData::markObjects(MarkStack *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV418IdentifierHashData11markObjectsEPNS_9MarkStackE(
    const QV4::IdentifierHashData *self,
    QV4::MarkStack *markStack) {
  self->markObjects(markStack);
}
