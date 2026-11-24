//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stackframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QMetaType QV4::MetaTypesStackFrame::returnType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV419MetaTypesStackFrame10returnTypeEv(
    const QV4::MetaTypesStackFrame *self) {
  return new QMetaType(self->returnType());
}

//  bool QV4::MetaTypesStackFrame::isReturnValueUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV419MetaTypesStackFrame22isReturnValueUndefinedEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->isReturnValueUndefined();
}

//  void QV4::MetaTypesStackFrame::setReturnValueUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419MetaTypesStackFrame23setReturnValueUndefinedEv(
    QV4::MetaTypesStackFrame *self) {
  self->setReturnValueUndefined();
}

//  const QMetaType *QV4::MetaTypesStackFrame::argTypes() const
extern "C" Q_DECL_EXPORT
const QMetaType *ritual_ZNK3QV419MetaTypesStackFrame8argTypesEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->argTypes();
}

//  const QMetaType *QV4::MetaTypesStackFrame::returnAndArgTypes() const
extern "C" Q_DECL_EXPORT
const QMetaType *ritual_ZNK3QV419MetaTypesStackFrame17returnAndArgTypesEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->returnAndArgTypes();
}

//  QObject *QV4::MetaTypesStackFrame::thisObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV419MetaTypesStackFrame10thisObjectEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->thisObject();
}

//  ExecutionContext *QV4::MetaTypesStackFrame::context() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV419MetaTypesStackFrame7contextEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->context();
}

//  void QV4::MetaTypesStackFrame::setContext(ExecutionContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419MetaTypesStackFrame10setContextEPNS_16ExecutionContextE(
    QV4::MetaTypesStackFrame *self,
    QV4::ExecutionContext *context) {
  self->setContext(context);
}

//  const QQmlPrivate::AOTTrackedLocalsStorage
//      *QV4::MetaTypesStackFrame::locals() const
extern "C" Q_DECL_EXPORT
const QQmlPrivate::AOTTrackedLocalsStorage *ritual_ZNK3QV419MetaTypesStackFrame6localsEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->locals();
}

//  void QV4::MetaTypesStackFrame::setLocals(const
//      QQmlPrivate::AOTTrackedLocalsStorage *locals)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419MetaTypesStackFrame9setLocalsEPKN11QQmlPrivate23AOTTrackedLocalsStorageE(
    QV4::MetaTypesStackFrame *self,
    const QQmlPrivate::AOTTrackedLocalsStorage *locals) {
  self->setLocals(locals);
}

//  Heap::CallContext *QV4::MetaTypesStackFrame::callContext() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV419MetaTypesStackFrame11callContextEv(
    const QV4::MetaTypesStackFrame *self) {
  return self->callContext();
}

//  QV4::MetaTypesStackFrame::~MetaTypesStackFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419MetaTypesStackFrameD1Ev(QV4::MetaTypesStackFrame *self) {
  delete self;
}
