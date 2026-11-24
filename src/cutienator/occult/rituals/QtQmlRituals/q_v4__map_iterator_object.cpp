//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::MapIteratorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417MapIteratorObject10__dataTestEv(
    QV4::MapIteratorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::MapIteratorObject *QV4::MapIteratorObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapIteratorObject *ritual_ZNK3QV417MapIteratorObject11d_uncheckedEv(
    const QV4::MapIteratorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MapIteratorObject *QV4::MapIteratorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapIteratorObject *ritual_ZNK3QV417MapIteratorObject1dEv(
    const QV4::MapIteratorObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::MapIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV417MapIteratorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::MapIteratorObject::defaultPrototype(e);
}
