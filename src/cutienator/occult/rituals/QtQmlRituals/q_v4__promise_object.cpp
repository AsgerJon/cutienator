//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::PromiseObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV413PromiseObject12staticVTableEv() {
  return QV4::PromiseObject::staticVTable();
}

//  void QV4::PromiseObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413PromiseObject10__dataTestEv(QV4::PromiseObject *self) {
  self->__dataTest();
}

//  QV4::Heap::PromiseObject *QV4::PromiseObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseObject *ritual_ZNK3QV413PromiseObject11d_uncheckedEv(
    const QV4::PromiseObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::PromiseObject *QV4::PromiseObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseObject *ritual_ZNK3QV413PromiseObject1dEv(
    const QV4::PromiseObject *self) {
  return self->d();
}

//  void QV4::PromiseObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413PromiseObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::PromiseObject::virtualDestroy(b);
}

//  QV4::Object *QV4::PromiseObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV413PromiseObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::PromiseObject::defaultPrototype(e);
}
