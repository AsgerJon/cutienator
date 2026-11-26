//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4function_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4function_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::FunctionData::FunctionData(EngineBase *engine,
//      ExecutableCompilationUnit *compilationUnit_)
extern "C" Q_DECL_EXPORT
QV4::FunctionData *ritual_ZN3QV412FunctionDataC1EPNS_10EngineBaseEPNS_25ExecutableCompilationUnitE(
    QV4::EngineBase *engine,
    QV4::ExecutableCompilationUnit *compilationUnit_) {
  return new QV4::FunctionData(engine, compilationUnit_);
}

//  QV4::FunctionData::~FunctionData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412FunctionDataD1Ev(QV4::FunctionData *self) {
  delete self;
}
