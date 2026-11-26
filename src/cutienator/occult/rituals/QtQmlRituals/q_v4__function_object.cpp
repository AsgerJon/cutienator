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

//  ReturnedValue QV4::FunctionObject::name() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject4nameEv(
    const QV4::FunctionObject *self) {
  return self->name();
}

//  void QV4::FunctionObject::setName(String *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414FunctionObject7setNameEPNS_6StringE(
    QV4::FunctionObject *self,
    QV4::String *name) {
  self->setName(name);
}

//  void QV4::FunctionObject::createDefaultPrototypeProperty(uint
//      protoConstructorSlot)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414FunctionObject30createDefaultPrototypePropertyEj(
    QV4::FunctionObject *self,
    uint protoConstructorSlot) {
  self->createDefaultPrototypeProperty(protoConstructorSlot);
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

//  void QV4::FunctionObject::call(QObject *thisObject, void **argv, const
//      QMetaType *types, int argc) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV414FunctionObject4callEP7QObjectPPvPK9QMetaTypei(
    const QV4::FunctionObject *self,
    QObject *thisObject,
    void **argv,
    const QMetaType *types,
    int argc) {
  self->call(thisObject, argv, types, argc);
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

//  ReturnedValue QV4::FunctionObject::failCall() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject8failCallEv(
    const QV4::FunctionObject *self) {
  return self->failCall();
}

//  ReturnedValue QV4::FunctionObject::failCallAsConstructor() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject21failCallAsConstructorEv(
    const QV4::FunctionObject *self) {
  return self->failCallAsConstructor();
}

//  void QV4::FunctionObject::virtualConvertAndCall(const FunctionObject *f,
//      QObject *thisObject, void **argv, const QMetaType *types, int argc)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414FunctionObject21virtualConvertAndCallEPKS0_P7QObjectPPvPK9QMetaTypei(
    const QV4::FunctionObject *f,
    QObject *thisObject,
    void **argv,
    const QMetaType *types,
    int argc) {
  QV4::FunctionObject::virtualConvertAndCall(
      f,
      thisObject,
      argv,
      types,
      argc);
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

//  Heap::FunctionObject
//      *QV4::FunctionObject::createConstructorFunction(ExecutionContext
//      *scope, Function *function, Object *homeObject, bool
//      isDerivedConstructor)
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV414FunctionObject25createConstructorFunctionEPNS_16ExecutionContextEPNS_8FunctionEPNS_6ObjectEb(
    QV4::ExecutionContext *scope,
    QV4::Function *function,
    QV4::Object *homeObject,
    bool isDerivedConstructor) {
  return QV4::FunctionObject::createConstructorFunction(
      scope,
      function,
      homeObject,
      isDerivedConstructor);
}

//  Heap::FunctionObject
//      *QV4::FunctionObject::createMemberFunction(ExecutionContext *scope,
//      Function *function, Object *homeObject, String *name)
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV414FunctionObject20createMemberFunctionEPNS_16ExecutionContextEPNS_8FunctionEPNS_6ObjectEPNS_6StringE(
    QV4::ExecutionContext *scope,
    QV4::Function *function,
    QV4::Object *homeObject,
    QV4::String *name) {
  return QV4::FunctionObject::createMemberFunction(
      scope,
      function,
      homeObject,
      name);
}

//  Heap::FunctionObject
//      *QV4::FunctionObject::createBuiltinFunction(ExecutionEngine *engine,
//      StringOrSymbol *nameOrSymbol, VTable::Call code, int argumentCount)
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV414FunctionObject21createBuiltinFunctionEPNS_15ExecutionEngineEPNS_14StringOrSymbolEPFyPKS0_PKNS_5ValueES9_iEi(
    QV4::ExecutionEngine *engine,
    QV4::StringOrSymbol *nameOrSymbol,
    void *code,
    int argumentCount) {
  return QV4::FunctionObject::createBuiltinFunction(
      engine,
      nameOrSymbol,
      reinterpret_cast<QV4::VTable::Call>(code),
      argumentCount);
}

//  bool QV4::FunctionObject::isConstructor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV414FunctionObject13isConstructorEv(
    const QV4::FunctionObject *self) {
  return self->isConstructor();
}

//  ReturnedValue QV4::FunctionObject::getHomeObject() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414FunctionObject13getHomeObjectEv(
    const QV4::FunctionObject *self) {
  return self->getHomeObject();
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
