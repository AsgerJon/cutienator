//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Bool QV4::Runtime::ToBoolean::call(const Value &a0)
extern "C" Q_DECL_EXPORT
QV4::Bool ritual_ZN3QV47Runtime9ToBoolean4callERKNS_5ValueE(
    const QV4::Value *a0) {
  return QV4::Runtime::ToBoolean::call(*a0);
}

//  QV4::Runtime::ToBoolean::~ToBoolean()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime9ToBooleanD1Ev(QV4::Runtime::ToBoolean *self) {
  delete self;
}
