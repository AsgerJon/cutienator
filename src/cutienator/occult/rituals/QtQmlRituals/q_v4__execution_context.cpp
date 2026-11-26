//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::ExecutionContext::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV416ExecutionContext12staticVTableEv() {
  return QV4::ExecutionContext::staticVTable();
}

//  void QV4::ExecutionContext::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416ExecutionContext10__dataTestEv(
    QV4::ExecutionContext *self) {
  self->__dataTest();
}

//  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV416ExecutionContext11d_uncheckedEv(
    const QV4::ExecutionContext *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV416ExecutionContext1dEv(
    const QV4::ExecutionContext *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ExecutionContext::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV416ExecutionContext20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ExecutionContext::defaultInternalClass(e);
}

//  Heap::CallContext
//      *QV4::ExecutionContext::newBlockContext(QV4::CppStackFrame *frame,
//      int blockIndex)
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZN3QV416ExecutionContext15newBlockContextEPNS_13CppStackFrameEi(
    QV4::CppStackFrame *frame,
    int blockIndex) {
  return QV4::ExecutionContext::newBlockContext(frame, blockIndex);
}

//  Heap::CallContext
//      *QV4::ExecutionContext::cloneBlockContext(ExecutionEngine *engine,
//      Heap::CallContext *callContext)
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZN3QV416ExecutionContext17cloneBlockContextEPNS_15ExecutionEngineEPNS_4Heap11CallContextE(
    QV4::ExecutionEngine *engine,
    QV4::Heap::CallContext *callContext) {
  return QV4::ExecutionContext::cloneBlockContext(engine, callContext);
}

//  Heap::CallContext
//      *QV4::ExecutionContext::newCallContext(JSTypesStackFrame *frame)
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZN3QV416ExecutionContext14newCallContextEPNS_17JSTypesStackFrameE(
    QV4::JSTypesStackFrame *frame) {
  return QV4::ExecutionContext::newCallContext(frame);
}

//  Heap::ExecutionContext
//      *QV4::ExecutionContext::newWithContext(Heap::Object *with) const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV416ExecutionContext14newWithContextEPNS_4Heap6ObjectE(
    const QV4::ExecutionContext *self,
    QV4::Heap::Object *with) {
  return self->newWithContext(with);
}

//  Heap::ExecutionContext
//      *QV4::ExecutionContext::newCatchContext(CppStackFrame *frame, int
//      blockIndex, Heap::String *exceptionVarName)
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZN3QV416ExecutionContext15newCatchContextEPNS_13CppStackFrameEiPNS_4Heap6StringE(
    QV4::CppStackFrame *frame,
    int blockIndex,
    QV4::Heap::String *exceptionVarName) {
  return QV4::ExecutionContext::newCatchContext(
      frame,
      blockIndex,
      exceptionVarName);
}

//  void QV4::ExecutionContext::createMutableBinding(String *name, bool
//      deletable)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416ExecutionContext20createMutableBindingEPNS_6StringEb(
    QV4::ExecutionContext *self,
    QV4::String *name,
    bool deletable) {
  self->createMutableBinding(name, deletable);
}

//  Error QV4::ExecutionContext::setProperty(String *name, const Value
//      &value)
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext::Error ritual_ZN3QV416ExecutionContext11setPropertyEPNS_6StringERKNS_5ValueE(
    QV4::ExecutionContext *self,
    QV4::String *name,
    const QV4::Value *value) {
  return self->setProperty(name, *value);
}

//  ReturnedValue QV4::ExecutionContext::getProperty(String *name)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416ExecutionContext11getPropertyEPNS_6StringE(
    QV4::ExecutionContext *self,
    QV4::String *name) {
  return self->getProperty(name);
}

//  ReturnedValue QV4::ExecutionContext::getPropertyAndBase(String *name,
//      Value *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416ExecutionContext18getPropertyAndBaseEPNS_6StringEPNS_5ValueE(
    QV4::ExecutionContext *self,
    QV4::String *name,
    QV4::Value *base) {
  return self->getPropertyAndBase(name, base);
}

//  bool QV4::ExecutionContext::deleteProperty(String *name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV416ExecutionContext14deletePropertyEPNS_6StringE(
    QV4::ExecutionContext *self,
    QV4::String *name) {
  return self->deleteProperty(name);
}

//  CallContext *QV4::ExecutionContext::asCallContext()
extern "C" Q_DECL_EXPORT
QV4::CallContext *ritual_ZN3QV416ExecutionContext13asCallContextEv(
    QV4::ExecutionContext *self) {
  return self->asCallContext();
}

//  const CallContext *QV4::ExecutionContext::asCallContext() const
extern "C" Q_DECL_EXPORT
const QV4::CallContext *ritual_ZNK3QV416ExecutionContext13asCallContextEv(
    const QV4::ExecutionContext *self) {
  return self->asCallContext();
}

//  bool QV4::ExecutionContext::virtualDeleteProperty(Managed *a0,
//      PropertyKey a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV416ExecutionContext21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *a0,
    const QV4::PropertyKey *a1) {
  return QV4::ExecutionContext::virtualDeleteProperty(a0, *a1);
}
