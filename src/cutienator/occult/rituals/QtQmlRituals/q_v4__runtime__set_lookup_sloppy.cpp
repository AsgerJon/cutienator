//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::SetLookupSloppy::call(Function *a0, const Value &a1,
//      int a2, const Value &a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15SetLookupSloppy4callEPNS_8FunctionERKNS_5ValueEiS6_(
    QV4::Function *a0,
    const QV4::Value *a1,
    int a2,
    const QV4::Value *a3) {
  QV4::Runtime::SetLookupSloppy::call(a0, *a1, a2, *a3);
}

//  QV4::Runtime::SetLookupSloppy::~SetLookupSloppy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15SetLookupSloppyD1Ev(
    QV4::Runtime::SetLookupSloppy *self) {
  delete self;
}
