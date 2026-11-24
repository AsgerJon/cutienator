//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ArrayObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ArrayObject10__dataTestEv(QV4::ArrayObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayObject *QV4::ArrayObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZNK3QV411ArrayObject11d_uncheckedEv(
    const QV4::ArrayObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayObject *QV4::ArrayObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZNK3QV411ArrayObject1dEv(
    const QV4::ArrayObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ArrayObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ArrayObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ArrayObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::ArrayObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV411ArrayObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ArrayObject::defaultPrototype(e);
}
