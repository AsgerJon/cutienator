//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::StoreNameSloppy::call(ExecutionEngine *a0, int a1,
//      const Value &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15StoreNameSloppy4callEPNS_15ExecutionEngineEiRKNS_5ValueE(
    QV4::ExecutionEngine *a0,
    int a1,
    const QV4::Value *a2) {
  QV4::Runtime::StoreNameSloppy::call(a0, a1, *a2);
}

//  QV4::Runtime::StoreNameSloppy::~StoreNameSloppy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15StoreNameSloppyD1Ev(
    QV4::Runtime::StoreNameSloppy *self) {
  delete self;
}
