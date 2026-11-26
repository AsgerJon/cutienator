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

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 27, as _ZN3QV44Heap19ProxyFunctionObject4initEPKNS_14FunctionObjectEPKNS_6ObjectE
namespace QV4 {
inline void Heap::ProxyFunctionObject::init(const QV4::FunctionObject *target, const QV4::Object *handler)
{
    ExecutionEngine *e = internalClass->engine;
    FunctionObject::init(e);
    this->target.set(e, target->d());
    this->handler.set(e, handler->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ProxyFunctionObject::init(const QV4::FunctionObject
//      *target, const QV4::Object *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ProxyFunctionObject4initEPKNS_14FunctionObjectEPKNS_6ObjectE(
    QV4::Heap::ProxyFunctionObject *self,
    const QV4::FunctionObject *target,
    const QV4::Object *handler) {
  self->init(target, handler);
}
