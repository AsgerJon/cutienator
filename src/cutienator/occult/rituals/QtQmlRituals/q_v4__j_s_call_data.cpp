//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4jscall_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::JSCallData::JSCallData(const Value *thisObject, const Value *argv,
//      int argc)
extern "C" Q_DECL_EXPORT
QV4::JSCallData *ritual_ZN3QV410JSCallDataC1EPKNS_5ValueES3_i(
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return new QV4::JSCallData(thisObject, argv, argc);
}

//  QV4::JSCallData::JSCallData(const JSCallArguments &args)
extern "C" Q_DECL_EXPORT
QV4::JSCallData *ritual_ZN3QV410JSCallDataC1ERKNS_15JSCallArgumentsE(
    const QV4::JSCallArguments *args) {
  return new QV4::JSCallData(*args);
}

//  QV4::JSCallData::~JSCallData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410JSCallDataD1Ev(QV4::JSCallData *self) {
  delete self;
}
