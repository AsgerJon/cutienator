//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::StrictEqual::call(const Value &a0, const
//      Value &a1)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime11StrictEqual4callERKNS_5ValueES4_(
    const QV4::Value *a0,
    const QV4::Value *a1) {
  return QV4::Runtime::StrictEqual::call(*a0, *a1);
}

//  QV4::Runtime::StrictEqual::~StrictEqual()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime11StrictEqualD1Ev(
    QV4::Runtime::StrictEqual *self) {
  delete self;
}
