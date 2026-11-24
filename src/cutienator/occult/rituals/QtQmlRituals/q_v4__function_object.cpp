//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::FunctionObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV414FunctionObject12staticVTableEv() {
  return QV4::FunctionObject::staticVTable();
}

//  void QV4::FunctionObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414FunctionObject10__dataTestEv(QV4::FunctionObject *self) {
  self->__dataTest();
}

//  QV4::Heap::FunctionObject *QV4::FunctionObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV414FunctionObject11d_uncheckedEv(
    const QV4::FunctionObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::FunctionObject *QV4::FunctionObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV414FunctionObject1dEv(
    const QV4::FunctionObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::FunctionObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV414FunctionObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::FunctionObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::FunctionObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV414FunctionObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::FunctionObject::defaultPrototype(e);
}

//  bool QV4::FunctionObject::canBeTailCalled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414FunctionObject15canBeTailCalledEv(
    const QV4::FunctionObject *self) {
  return self->canBeTailCalled();
}

//  void QV4::FunctionObject::setName(String *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414FunctionObject7setNameEPNS_6StringE(
    QV4::FunctionObject *self,
    QV4::String *name) {
  self->setName(name);
}

//  ReturnedValue QV4::FunctionObject::callAsConstructor(const Value *argv,
//      int argc, const Value *newTarget) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject17callAsConstructorEPKNS_5ValueEiS3_(
    const QV4::FunctionObject *self,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *newTarget) {
  return self->callAsConstructor(argv, argc, newTarget);
}

//  ReturnedValue QV4::FunctionObject::call(const Value *thisObject, const
//      Value *argv, int argc) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject4callEPKNS_5ValueES3_i(
    const QV4::FunctionObject *self,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return self->call(thisObject, argv, argc);
}

//  ReturnedValue QV4::FunctionObject::callAsConstructor(const JSCallData
//      &data) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject17callAsConstructorERKNS_10JSCallDataE(
    const QV4::FunctionObject *self,
    const QV4::JSCallData *data) {
  return self->callAsConstructor(*data);
}

//  ReturnedValue QV4::FunctionObject::call(const JSCallData &data) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject4callERKNS_10JSCallDataE(
    const QV4::FunctionObject *self,
    const QV4::JSCallData *data) {
  return self->call(*data);
}

//  Heap::FunctionObject
//      *QV4::FunctionObject::createScriptFunction(ExecutionContext *scope,
//      Function *function)
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV414FunctionObject20createScriptFunctionEPNS_16ExecutionContextEPNS_8FunctionE(
    QV4::ExecutionContext *scope,
    QV4::Function *function) {
  return QV4::FunctionObject::createScriptFunction(scope, function);
}

//  bool QV4::FunctionObject::isConstructor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414FunctionObject13isConstructorEv(
    const QV4::FunctionObject *self) {
  return self->isConstructor();
}

//  ReturnedValue QV4::FunctionObject::protoProperty() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject13protoPropertyEv(
    const QV4::FunctionObject *self) {
  return self->protoProperty();
}

//  bool QV4::FunctionObject::hasHasInstanceProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414FunctionObject22hasHasInstancePropertyEv(
    const QV4::FunctionObject *self) {
  return self->hasHasInstanceProperty();
}
