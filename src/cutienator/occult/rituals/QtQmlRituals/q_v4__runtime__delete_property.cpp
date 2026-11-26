//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::DeleteProperty::call(ExecutionEngine *a0,
//      Function *a1, const Value &a2, const Value &a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime14DeleteProperty4callEPNS_15ExecutionEngineEPNS_8FunctionERKNS_5ValueES8_(
    QV4::ExecutionEngine *a0,
    QV4::Function *a1,
    const QV4::Value *a2,
    const QV4::Value *a3) {
  return QV4::Runtime::DeleteProperty::call(a0, a1, *a2, *a3);
}

//  QV4::Runtime::DeleteProperty::~DeleteProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime14DeletePropertyD1Ev(
    QV4::Runtime::DeleteProperty *self) {
  delete self;
}
