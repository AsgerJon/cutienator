//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::SparseArrayData::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415SparseArrayData12staticVTableEv() {
  return QV4::SparseArrayData::staticVTable();
}

//  void QV4::SparseArrayData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData10__dataTestEv(
    QV4::SparseArrayData *self) {
  self->__dataTest();
}

//  Heap::InternalClass
//      *QV4::SparseArrayData::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415SparseArrayData20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::SparseArrayData::defaultInternalClass(e);
}

//  void QV4::SparseArrayData::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::SparseArrayData::virtualDestroy(b);
}

//  SparseArray *QV4::SparseArrayData::sparse() const
extern "C" Q_DECL_EXPORT
QV4::SparseArray *ritual_ZNK3QV415SparseArrayData6sparseEv(
    const QV4::SparseArrayData *self) {
  return self->sparse();
}

//  void QV4::SparseArrayData::setSparse(SparseArray *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData9setSparseEPNS_11SparseArrayE(
    QV4::SparseArrayData *self,
    QV4::SparseArray *s) {
  self->setSparse(s);
}

//  uint QV4::SparseArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SparseArrayData11mappedIndexEj(
    const QV4::SparseArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}
