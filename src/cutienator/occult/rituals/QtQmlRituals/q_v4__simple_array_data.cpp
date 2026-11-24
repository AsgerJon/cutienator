//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::SimpleArrayData::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415SimpleArrayData12staticVTableEv() {
  return QV4::SimpleArrayData::staticVTable();
}

//  void QV4::SimpleArrayData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SimpleArrayData10__dataTestEv(
    QV4::SimpleArrayData *self) {
  self->__dataTest();
}

//  Heap::InternalClass
//      *QV4::SimpleArrayData::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415SimpleArrayData20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::SimpleArrayData::defaultInternalClass(e);
}

//  uint QV4::SimpleArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SimpleArrayData11mappedIndexEj(
    const QV4::SimpleArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  Value QV4::SimpleArrayData::data(uint index) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV415SimpleArrayData4dataEj(
    const QV4::SimpleArrayData *self,
    uint index) {
  return new QV4::Value(self->data(index));
}

//  uint QV4::SimpleArrayData::len() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SimpleArrayData3lenEv(
    const QV4::SimpleArrayData *self) {
  return self->len();
}
