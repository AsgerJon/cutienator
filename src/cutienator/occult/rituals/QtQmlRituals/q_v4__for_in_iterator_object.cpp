//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ForInIteratorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ForInIteratorObject10__dataTestEv(
    QV4::ForInIteratorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObject *ritual_ZNK3QV419ForInIteratorObject11d_uncheckedEv(
    const QV4::ForInIteratorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ForInIteratorObject *QV4::ForInIteratorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObject *ritual_ZNK3QV419ForInIteratorObject1dEv(
    const QV4::ForInIteratorObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::ForInIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV419ForInIteratorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ForInIteratorObject::defaultPrototype(e);
}
