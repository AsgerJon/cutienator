//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arrayiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arrayiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ArrayIteratorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ArrayIteratorObject10__dataTestEv(
    QV4::ArrayIteratorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayIteratorObject *QV4::ArrayIteratorObject::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayIteratorObject *ritual_ZNK3QV419ArrayIteratorObject11d_uncheckedEv(
    const QV4::ArrayIteratorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayIteratorObject *QV4::ArrayIteratorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayIteratorObject *ritual_ZNK3QV419ArrayIteratorObject1dEv(
    const QV4::ArrayIteratorObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::ArrayIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV419ArrayIteratorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ArrayIteratorObject::defaultPrototype(e);
}
