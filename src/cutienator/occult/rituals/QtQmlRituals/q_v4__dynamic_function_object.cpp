//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::DynamicFunctionObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV421DynamicFunctionObject12staticVTableEv() {
  return QV4::DynamicFunctionObject::staticVTable();
}

//  void QV4::DynamicFunctionObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421DynamicFunctionObject10__dataTestEv(
    QV4::DynamicFunctionObject *self) {
  self->__dataTest();
}

//  QV4::Heap::DynamicFunctionObject
//      *QV4::DynamicFunctionObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DynamicFunctionObject *ritual_ZNK3QV421DynamicFunctionObject11d_uncheckedEv(
    const QV4::DynamicFunctionObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DynamicFunctionObject *QV4::DynamicFunctionObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DynamicFunctionObject *ritual_ZNK3QV421DynamicFunctionObject1dEv(
    const QV4::DynamicFunctionObject *self) {
  return self->d();
}

//  ReturnedValue QV4::DynamicFunctionObject::virtualCall(const
//      FunctionObject *f, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV421DynamicFunctionObject11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::DynamicFunctionObject::virtualCall(f, thisObject, argv, argc);
}
