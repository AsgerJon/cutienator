//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Bool QV4::Runtime::DeleteName_NoThrow::call(ExecutionEngine *a0, int a1)
extern "C" Q_DECL_EXPORT
QV4::Bool ritual_ZN3QV47Runtime18DeleteName_NoThrow4callEPNS_15ExecutionEngineEi(
    QV4::ExecutionEngine *a0,
    int a1) {
  return QV4::Runtime::DeleteName_NoThrow::call(a0, a1);
}

//  QV4::Runtime::DeleteName_NoThrow::~DeleteName_NoThrow()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime18DeleteName_NoThrowD1Ev(
    QV4::Runtime::DeleteName_NoThrow *self) {
  delete self;
}
