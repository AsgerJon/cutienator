//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stackframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ScopedStackFrame::ScopedStackFrame(const Scope &scope,
//      ExecutionContext *context)
extern "C" Q_DECL_EXPORT
QV4::ScopedStackFrame *ritual_ZN3QV416ScopedStackFrameC1ERKNS_5ScopeEPNS_16ExecutionContextE(
    const QV4::Scope *scope,
    QV4::ExecutionContext *context) {
  return new QV4::ScopedStackFrame(*scope, context);
}

//  QV4::ScopedStackFrame::~ScopedStackFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416ScopedStackFrameD1Ev(QV4::ScopedStackFrame *self) {
  delete self;
}
