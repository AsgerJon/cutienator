//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4typedarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::IntrinsicTypedArrayPrototype::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV428IntrinsicTypedArrayPrototype10__dataTestEv(
    QV4::IntrinsicTypedArrayPrototype *self) {
  self->__dataTest();
}

//  QV4::Heap::IntrinsicTypedArrayPrototype
//      *QV4::IntrinsicTypedArrayPrototype::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IntrinsicTypedArrayPrototype *ritual_ZNK3QV428IntrinsicTypedArrayPrototype11d_uncheckedEv(
    const QV4::IntrinsicTypedArrayPrototype *self) {
  return self->d_unchecked();
}

//  QV4::Heap::IntrinsicTypedArrayPrototype
//      *QV4::IntrinsicTypedArrayPrototype::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IntrinsicTypedArrayPrototype *ritual_ZNK3QV428IntrinsicTypedArrayPrototype1dEv(
    const QV4::IntrinsicTypedArrayPrototype *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::IntrinsicTypedArrayPrototype::defaultPrototype(QV4::ExecutionEn
//      gine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV428IntrinsicTypedArrayPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::IntrinsicTypedArrayPrototype::defaultPrototype(e);
}
