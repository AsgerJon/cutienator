//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::StringIteratorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420StringIteratorObject10__dataTestEv(
    QV4::StringIteratorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::StringIteratorObject *QV4::StringIteratorObject::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringIteratorObject *ritual_ZNK3QV420StringIteratorObject11d_uncheckedEv(
    const QV4::StringIteratorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::StringIteratorObject *QV4::StringIteratorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringIteratorObject *ritual_ZNK3QV420StringIteratorObject1dEv(
    const QV4::StringIteratorObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::StringIteratorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV420StringIteratorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::StringIteratorObject::defaultPrototype(e);
}
