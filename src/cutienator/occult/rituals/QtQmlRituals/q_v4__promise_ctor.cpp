//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QCoreApplication>
#include <QtQml/private/qv4promiseobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 374, as _ZN3QV411PromiseCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace QV4::Promise;
inline ReturnedValue PromiseCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    // 25.4.3.1 Promise ( executor )
    // 1. If NewTarget is undefined, throw a TypeError exception.
    Scope scope(f);
    THROW_TYPE_ERROR();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::PromiseCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411PromiseCtor10__dataTestEv(QV4::PromiseCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::PromiseCtor *QV4::PromiseCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseCtor *ritual_ZNK3QV411PromiseCtor11d_uncheckedEv(
    const QV4::PromiseCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::PromiseCtor *QV4::PromiseCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseCtor *ritual_ZNK3QV411PromiseCtor1dEv(
    const QV4::PromiseCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::PromiseCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411PromiseCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::PromiseCtor::virtualCall(f, thisObject, argv, argc);
}
