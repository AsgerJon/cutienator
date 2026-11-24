//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4managed_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4managed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::InternalClass::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413InternalClass10__dataTestEv(QV4::InternalClass *self) {
  self->__dataTest();
}

//  QV4::Heap::InternalClass *QV4::InternalClass::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZNK3QV413InternalClass11d_uncheckedEv(
    const QV4::InternalClass *self) {
  return self->d_unchecked();
}

//  QV4::Heap::InternalClass *QV4::InternalClass::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZNK3QV413InternalClass1dEv(
    const QV4::InternalClass *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::InternalClass::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV413InternalClass20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::InternalClass::defaultInternalClass(e);
}

//  Heap::InternalClass *QV4::InternalClass::changeVTable(const VTable *vt)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV413InternalClass12changeVTableEPKNS_6VTableE(
    QV4::InternalClass *self,
    const QV4::VTable *vt) {
  return self->changeVTable(vt);
}

//  Heap::InternalClass *QV4::InternalClass::changePrototype(Heap::Object
//      *proto)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV413InternalClass15changePrototypeEPNS_4Heap6ObjectE(
    QV4::InternalClass *self,
    QV4::Heap::Object *proto) {
  return self->changePrototype(proto);
}

//  void QV4::InternalClass::operator=(Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413InternalClassaSEPNS_4Heap13InternalClassE(
    QV4::InternalClass *self,
    QV4::Heap::InternalClass *ic) {
  self->operator=(ic);
}
