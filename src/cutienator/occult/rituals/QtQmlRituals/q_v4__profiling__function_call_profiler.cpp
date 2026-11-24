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

//  QV4::Profiling::FunctionCallProfiler::FunctionCallProfiler(ExecutionEngin
//      e *engine, Function *f)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionCallProfiler *ritual_ZN3QV49Profiling20FunctionCallProfilerC1EPNS_15ExecutionEngineEPNS_8FunctionE(
    QV4::ExecutionEngine *engine,
    QV4::Function *f) {
  return new QV4::Profiling::FunctionCallProfiler(engine, f);
}

//  QV4::Profiling::FunctionCallProfiler::~FunctionCallProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling20FunctionCallProfilerD1Ev(
    QV4::Profiling::FunctionCallProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
