//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4proxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4proxy_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4persistent_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 753, as _ZN3QV45Proxy11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Proxy::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 781, as _ZN3QV45Proxy13method_revokeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Proxy::method_revoke(const FunctionObject *f, const Value *, const Value *, int)
{
    Scope scope(f);
    ScopedObject o(scope, f->get(scope.engine->symbol_revokableProxy()));
    Q_ASSERT(o);
    ProxyObject *proxy = o->cast<ProxyObject>();

    proxy->d()->target.set(scope.engine, nullptr);
    proxy->d()->handler.set(scope.engine, nullptr);
    return Encode::undefined();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Proxy::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45Proxy10__dataTestEv(QV4::Proxy *self) {
  self->__dataTest();
}

//  QV4::Heap::Proxy *QV4::Proxy::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Proxy *ritual_ZNK3QV45Proxy11d_uncheckedEv(
    const QV4::Proxy *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Proxy *QV4::Proxy::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Proxy *ritual_ZNK3QV45Proxy1dEv(const QV4::Proxy *self) {
  return self->d();
}

//  ReturnedValue QV4::Proxy::virtualCall(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV45Proxy11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::Proxy::virtualCall(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::Proxy::method_revoke(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV45Proxy13method_revokeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::Proxy::method_revoke(a0, thisObject, argv, argc);
}
