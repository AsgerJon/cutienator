//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue
//      QV4::Runtime::CreateUnmappedArgumentsObject::call(ExecutionEngine
//      *a0)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime29CreateUnmappedArgumentsObject4callEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *a0) {
  return QV4::Runtime::CreateUnmappedArgumentsObject::call(a0);
}

//  QV4::Runtime::CreateUnmappedArgumentsObject::~CreateUnmappedArgumentsObje
//      ct()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime29CreateUnmappedArgumentsObjectD1Ev(
    QV4::Runtime::CreateUnmappedArgumentsObject *self) {
  delete self;
}
