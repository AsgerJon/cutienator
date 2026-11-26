//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue
//      QV4::Runtime::CallQmlContextPropertyLookup::call(ExecutionEngine *a0,
//      uint a1, Value *a2, int a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime28CallQmlContextPropertyLookup4callEPNS_15ExecutionEngineEjPNS_5ValueEi(
    QV4::ExecutionEngine *a0,
    uint a1,
    QV4::Value *a2,
    int a3) {
  return QV4::Runtime::CallQmlContextPropertyLookup::call(a0, a1, a2, a3);
}

//  QV4::Runtime::CallQmlContextPropertyLookup::~CallQmlContextPropertyLookup
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime28CallQmlContextPropertyLookupD1Ev(
    QV4::Runtime::CallQmlContextPropertyLookup *self) {
  delete self;
}
