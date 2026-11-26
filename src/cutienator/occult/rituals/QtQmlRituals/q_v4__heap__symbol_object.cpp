//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 28, as _ZN3QV44Heap12SymbolObject4initEPKNS_6SymbolE
namespace QV4 {
inline void Heap::SymbolObject::init(const QV4::Symbol *s)
{
    Object::init();
    symbol.set(internalClass->engine, s->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::SymbolObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12SymbolObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::SymbolObject::markObjects(b, stack);
}

//  void QV4::Heap::SymbolObject::init(const QV4::Symbol *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12SymbolObject4initEPKNS_6SymbolE(
    QV4::Heap::SymbolObject *self,
    const QV4::Symbol *s) {
  self->init(s);
}

//  QV4::Heap::SymbolObject as the QV4::Heap::SymbolObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolObjectData *ritual_cast_QV4_Heap_SymbolObject_QV4_Heap_SymbolObjectData(
    QV4::Heap::SymbolObject *self) {
  return static_cast<QV4::Heap::SymbolObjectData *>(self);
}
