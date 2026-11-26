//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::StoreSuperProperty::call(ExecutionEngine *a0, const
//      Value &a1, const Value &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime18StoreSuperProperty4callEPNS_15ExecutionEngineERKNS_5ValueES6_(
    QV4::ExecutionEngine *a0,
    const QV4::Value *a1,
    const QV4::Value *a2) {
  QV4::Runtime::StoreSuperProperty::call(a0, *a1, *a2);
}

//  QV4::Runtime::StoreSuperProperty::~StoreSuperProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime18StoreSuperPropertyD1Ev(
    QV4::Runtime::StoreSuperProperty *self) {
  delete self;
}
