//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::LoadGlobalLookup::call(ExecutionEngine *a0,
//      Function *a1, int a2)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime16LoadGlobalLookup4callEPNS_15ExecutionEngineEPNS_8FunctionEi(
    QV4::ExecutionEngine *a0,
    QV4::Function *a1,
    int a2) {
  return QV4::Runtime::LoadGlobalLookup::call(a0, a1, a2);
}

//  QV4::Runtime::LoadGlobalLookup::~LoadGlobalLookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime16LoadGlobalLookupD1Ev(
    QV4::Runtime::LoadGlobalLookup *self) {
  delete self;
}
