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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 914, as _ZN3QV427CapabilitiesExecutorWrapper11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace QV4::Promise;
inline ReturnedValue CapabilitiesExecutorWrapper::virtualCall(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    Q_UNUSED(thisObject);

    Scope scope(f);
    const CapabilitiesExecutorWrapper* self = static_cast<const CapabilitiesExecutorWrapper*>(f);
    Heap::PromiseCapability *capabilities = self->d()->capabilities;

    if (!capabilities->resolve.isUndefined() || !capabilities->reject.isUndefined())
        THROW_TYPE_ERROR();

    if (argc >= 1 && !argv[0].isUndefined())
        capabilities->resolve.set(scope.engine, argv[0]);

    if (argc >= 2 && !argv[1].isUndefined())
        capabilities->reject.set(scope.engine, argv[1]);

    return Encode::undefined();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::CapabilitiesExecutorWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV427CapabilitiesExecutorWrapper10__dataTestEv(
    QV4::CapabilitiesExecutorWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::CapabilitiesExecutorWrapper
//      *QV4::CapabilitiesExecutorWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CapabilitiesExecutorWrapper *ritual_ZNK3QV427CapabilitiesExecutorWrapper11d_uncheckedEv(
    const QV4::CapabilitiesExecutorWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::CapabilitiesExecutorWrapper
//      *QV4::CapabilitiesExecutorWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CapabilitiesExecutorWrapper *ritual_ZNK3QV427CapabilitiesExecutorWrapper1dEv(
    const QV4::CapabilitiesExecutorWrapper *self) {
  return self->d();
}

//  ReturnedValue QV4::CapabilitiesExecutorWrapper::virtualCall(const
//      FunctionObject *f, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV427CapabilitiesExecutorWrapper11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::CapabilitiesExecutorWrapper::virtualCall(
      f,
      thisObject,
      argv,
      argc);
}
