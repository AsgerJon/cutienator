//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4profiling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Profiling::FunctionCall::FunctionCall()
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1Ev() {
  return new QV4::Profiling::FunctionCall();
}

//  QV4::Profiling::FunctionCall::FunctionCall(Function *function, qint64
//      start, qint64 end)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1EPNS_8FunctionExx(
    QV4::Function *function,
    qint64 start,
    qint64 end) {
  return new QV4::Profiling::FunctionCall(function, start, end);
}

//  QV4::Profiling::FunctionCall::FunctionCall(const FunctionCall &other)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCall *ritual_ZN3QV49Profiling12FunctionCallC1ERKS1_(
    const QV4::Profiling::FunctionCall *other) {
  return new QV4::Profiling::FunctionCall(*other);
}

//  QV4::Profiling::FunctionCall::~FunctionCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling12FunctionCallD1Ev(
    QV4::Profiling::FunctionCall *self) {
  delete self;
}

//  Function *QV4::Profiling::FunctionCall::function() const
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZNK3QV49Profiling12FunctionCall8functionEv(
    const QV4::Profiling::FunctionCall *self) {
  return self->function();
}

#endif  // !(!QT_CONFIG(qml_debug))
