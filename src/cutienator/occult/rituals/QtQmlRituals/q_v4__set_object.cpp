//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::SetObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49SetObject10__dataTestEv(QV4::SetObject *self) {
  self->__dataTest();
}

//  QV4::Heap::SetObject *QV4::SetObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetObject *ritual_ZNK3QV49SetObject11d_uncheckedEv(
    const QV4::SetObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SetObject *QV4::SetObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SetObject *ritual_ZNK3QV49SetObject1dEv(
    const QV4::SetObject *self) {
  return self->d();
}

//  QV4::Object *QV4::SetObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49SetObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SetObject::defaultPrototype(e);
}
