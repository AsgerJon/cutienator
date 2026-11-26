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

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 19, as _ZN3QV44Heap11ProxyObject4initEPKNS_6ObjectES4_
namespace QV4 {
inline void Heap::ProxyObject::init(const QV4::Object *target, const QV4::Object *handler)
{
    Object::init();
    ExecutionEngine *e = internalClass->engine;
    this->target.set(e, target->d());
    this->handler.set(e, handler->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ProxyObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ProxyObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ProxyObject::markObjects(b, stack);
}

//  void QV4::Heap::ProxyObject::init(const QV4::Object *target, const
//      QV4::Object *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ProxyObject4initEPKNS_6ObjectES4_(
    QV4::Heap::ProxyObject *self,
    const QV4::Object *target,
    const QV4::Object *handler) {
  self->init(target, handler);
}

//  QV4::Heap::ProxyObject as the QV4::Heap::ProxyObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObjectData *ritual_cast_QV4_Heap_ProxyObject_QV4_Heap_ProxyObjectData(
    QV4::Heap::ProxyObject *self) {
  return static_cast<QV4::Heap::ProxyObjectData *>(self);
}
