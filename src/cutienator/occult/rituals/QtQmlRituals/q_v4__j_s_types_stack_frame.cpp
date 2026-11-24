//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stackframe_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::JSTypesStackFrame::init(Function *v4Function, const Value
//      *argv, int argc, bool callerCanHandleTailCall)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame4initEPNS_8FunctionEPKNS_5ValueEib(
    QV4::JSTypesStackFrame *self,
    QV4::Function *v4Function,
    const QV4::Value *argv,
    int argc,
    bool callerCanHandleTailCall) {
  self->init(v4Function, argv, argc, callerCanHandleTailCall);
}

//  const Value *QV4::JSTypesStackFrame::argv() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV417JSTypesStackFrame4argvEv(
    const QV4::JSTypesStackFrame *self) {
  return self->argv();
}

//  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize(uint nRegisters)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV417JSTypesStackFrame24requiredJSStackFrameSizeEj(
    uint nRegisters) {
  return QV4::JSTypesStackFrame::requiredJSStackFrameSize(nRegisters);
}

//  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize(Function
//      *v4Function)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV417JSTypesStackFrame24requiredJSStackFrameSizeEPNS_8FunctionE(
    QV4::Function *v4Function) {
  return QV4::JSTypesStackFrame::requiredJSStackFrameSize(v4Function);
}

//  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV417JSTypesStackFrame24requiredJSStackFrameSizeEv(
    const QV4::JSTypesStackFrame *self) {
  return self->requiredJSStackFrameSize();
}

//  void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace, const Value
//      &function, const Heap::ExecutionContext *scope, const Value
//      &thisObject, const Value &newTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame12setupJSFrameEPNS_5ValueERKS1_PKNS_4Heap16ExecutionContextES4_S4_(
    QV4::JSTypesStackFrame *self,
    QV4::Value *stackSpace,
    const QV4::Value *function,
    const QV4::Heap::ExecutionContext *scope,
    const QV4::Value *thisObject,
    const QV4::Value *newTarget) {
  self->setupJSFrame(stackSpace, *function, scope, *thisObject, *newTarget);
}

//  void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace, const Value
//      &function, const Heap::ExecutionContext *scope, const Value
//      &thisObject, const Value &newTarget, uint nFormals, uint nRegisters)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame12setupJSFrameEPNS_5ValueERKS1_PKNS_4Heap16ExecutionContextES4_S4_jj(
    QV4::JSTypesStackFrame *self,
    QV4::Value *stackSpace,
    const QV4::Value *function,
    const QV4::Heap::ExecutionContext *scope,
    const QV4::Value *thisObject,
    const QV4::Value *newTarget,
    uint nFormals,
    uint nRegisters) {
  self->setupJSFrame(
      stackSpace,
      *function,
      scope,
      *thisObject,
      *newTarget,
      nFormals,
      nRegisters);
}

//  ExecutionContext *QV4::JSTypesStackFrame::context() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV417JSTypesStackFrame7contextEv(
    const QV4::JSTypesStackFrame *self) {
  return self->context();
}

//  void QV4::JSTypesStackFrame::setContext(ExecutionContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame10setContextEPNS_16ExecutionContextE(
    QV4::JSTypesStackFrame *self,
    QV4::ExecutionContext *context) {
  self->setContext(context);
}

//  Heap::CallContext *QV4::JSTypesStackFrame::callContext() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV417JSTypesStackFrame11callContextEv(
    const QV4::JSTypesStackFrame *self) {
  return self->callContext();
}

//  bool QV4::JSTypesStackFrame::isTailCalling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417JSTypesStackFrame13isTailCallingEv(
    const QV4::JSTypesStackFrame *self) {
  return self->isTailCalling();
}

//  void QV4::JSTypesStackFrame::setTailCalling(bool tailCalling)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame14setTailCallingEb(
    QV4::JSTypesStackFrame *self,
    bool tailCalling) {
  self->setTailCalling(tailCalling);
}

//  bool QV4::JSTypesStackFrame::pendingTailCall() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417JSTypesStackFrame15pendingTailCallEv(
    const QV4::JSTypesStackFrame *self) {
  return self->pendingTailCall();
}

//  void QV4::JSTypesStackFrame::setPendingTailCall(bool pending)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame18setPendingTailCallEb(
    QV4::JSTypesStackFrame *self,
    bool pending) {
  self->setPendingTailCall(pending);
}

//  const char *QV4::JSTypesStackFrame::yield() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV417JSTypesStackFrame5yieldEv(
    const QV4::JSTypesStackFrame *self) {
  return self->yield();
}

//  void QV4::JSTypesStackFrame::setYield(const char *yield)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame8setYieldEPKc(
    QV4::JSTypesStackFrame *self,
    const char *yield) {
  self->setYield(yield);
}

//  bool QV4::JSTypesStackFrame::yieldIsIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417JSTypesStackFrame15yieldIsIteratorEv(
    const QV4::JSTypesStackFrame *self) {
  return self->yieldIsIterator();
}

//  void QV4::JSTypesStackFrame::setYieldIsIterator(bool isIter)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame18setYieldIsIteratorEb(
    QV4::JSTypesStackFrame *self,
    bool isIter) {
  self->setYieldIsIterator(isIter);
}

//  bool QV4::JSTypesStackFrame::callerCanHandleTailCall() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417JSTypesStackFrame23callerCanHandleTailCallEv(
    const QV4::JSTypesStackFrame *self) {
  return self->callerCanHandleTailCall();
}

//  ReturnedValue QV4::JSTypesStackFrame::thisObject() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV417JSTypesStackFrame10thisObjectEv(
    const QV4::JSTypesStackFrame *self) {
  return self->thisObject();
}

//  Value *QV4::JSTypesStackFrame::framePointer() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV417JSTypesStackFrame12framePointerEv(
    const QV4::JSTypesStackFrame *self) {
  return self->framePointer();
}

//  void QV4::JSTypesStackFrame::push(EngineBase *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame4pushEPNS_10EngineBaseE(
    QV4::JSTypesStackFrame *self,
    QV4::EngineBase *engine) {
  self->push(engine);
}

//  void QV4::JSTypesStackFrame::pop(EngineBase *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrame3popEPNS_10EngineBaseE(
    QV4::JSTypesStackFrame *self,
    QV4::EngineBase *engine) {
  self->pop(engine);
}

//  QV4::JSTypesStackFrame::~JSTypesStackFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417JSTypesStackFrameD1Ev(QV4::JSTypesStackFrame *self) {
  delete self;
}
