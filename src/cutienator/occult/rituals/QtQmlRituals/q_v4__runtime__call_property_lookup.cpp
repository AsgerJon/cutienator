//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::CallPropertyLookup::call(ExecutionEngine *a0,
//      const Value &a1, uint a2, Value *a3, int a4)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime18CallPropertyLookup4callEPNS_15ExecutionEngineERKNS_5ValueEjPS4_i(
    QV4::ExecutionEngine *a0,
    const QV4::Value *a1,
    uint a2,
    QV4::Value *a3,
    int a4) {
  return QV4::Runtime::CallPropertyLookup::call(a0, *a1, a2, a3, a4);
}

//  QV4::Runtime::CallPropertyLookup::~CallPropertyLookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime18CallPropertyLookupD1Ev(
    QV4::Runtime::CallPropertyLookup *self) {
  delete self;
}
