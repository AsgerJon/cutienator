//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stackframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::CppStackFrame::init(Function *v4Function, int argc, Kind kind)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413CppStackFrame4initEPNS_8FunctionEiNS_17CppStackFrameBase4KindE(
    QV4::CppStackFrame *self,
    QV4::Function *v4Function,
    int argc,
    QV4::CppStackFrameBase::Kind kind) {
  self->init(v4Function, argc, kind);
}

//  bool QV4::CppStackFrame::isJSTypesFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV413CppStackFrame14isJSTypesFrameEv(
    const QV4::CppStackFrame *self) {
  return self->isJSTypesFrame();
}

//  bool QV4::CppStackFrame::isMetaTypesFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV413CppStackFrame16isMetaTypesFrameEv(
    const QV4::CppStackFrame *self) {
  return self->isMetaTypesFrame();
}

//  QString QV4::CppStackFrame::source() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV413CppStackFrame6sourceEv(
    const QV4::CppStackFrame *self) {
  return new QString(self->source());
}

//  QString QV4::CppStackFrame::function() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV413CppStackFrame8functionEv(
    const QV4::CppStackFrame *self) {
  return new QString(self->function());
}

//  int QV4::CppStackFrame::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV413CppStackFrame10lineNumberEv(
    const QV4::CppStackFrame *self) {
  return self->lineNumber();
}

//  int QV4::CppStackFrame::statementNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV413CppStackFrame15statementNumberEv(
    const QV4::CppStackFrame *self) {
  return self->statementNumber();
}

//  int QV4::CppStackFrame::missingLineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV413CppStackFrame17missingLineNumberEv(
    const QV4::CppStackFrame *self) {
  return self->missingLineNumber();
}

//  CppStackFrame *QV4::CppStackFrame::parentFrame() const
extern "C" Q_DECL_EXPORT
QV4::CppStackFrame *ritual_ZNK3QV413CppStackFrame11parentFrameEv(
    const QV4::CppStackFrame *self) {
  return self->parentFrame();
}

//  void QV4::CppStackFrame::setParentFrame(CppStackFrame *parentFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413CppStackFrame14setParentFrameEPS0_(
    QV4::CppStackFrame *self,
    QV4::CppStackFrame *parentFrame) {
  self->setParentFrame(parentFrame);
}

//  int QV4::CppStackFrame::argc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV413CppStackFrame4argcEv(const QV4::CppStackFrame *self) {
  return self->argc();
}

//  ExecutionContext *QV4::CppStackFrame::context() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV413CppStackFrame7contextEv(
    const QV4::CppStackFrame *self) {
  return self->context();
}

//  Heap::CallContext *QV4::CppStackFrame::callContext() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV413CppStackFrame11callContextEv(
    const QV4::CppStackFrame *self) {
  return self->callContext();
}

//  ReturnedValue QV4::CppStackFrame::thisObject() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV413CppStackFrame10thisObjectEv(
    const QV4::CppStackFrame *self) {
  return self->thisObject();
}

//  QV4::CppStackFrame::CppStackFrame()
extern "C" Q_DECL_EXPORT
QV4::CppStackFrame *ritual_ZN3QV413CppStackFrameC1Ev() {
  return new QV4::CppStackFrame();
}

//  void QV4::CppStackFrame::push(EngineBase *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413CppStackFrame4pushEPNS_10EngineBaseE(
    QV4::CppStackFrame *self,
    QV4::EngineBase *engine) {
  self->push(engine);
}

//  void QV4::CppStackFrame::pop(EngineBase *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413CppStackFrame3popEPNS_10EngineBaseE(
    QV4::CppStackFrame *self,
    QV4::EngineBase *engine) {
  self->pop(engine);
}

//  Heap::CallContext *QV4::CppStackFrame::callContext(Heap::ExecutionContext
//      *ctx) const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV413CppStackFrame11callContextEPNS_4Heap16ExecutionContextE(
    const QV4::CppStackFrame *self,
    QV4::Heap::ExecutionContext *ctx) {
  return self->callContext(ctx);
}

//  QV4::CppStackFrame::~CppStackFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413CppStackFrameD1Ev(QV4::CppStackFrame *self) {
  delete self;
}
