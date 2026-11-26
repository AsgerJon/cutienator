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

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 348, as _ZN3QV44Heap21PromiseExecutionState4initEv
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseExecutionState::init()
{
    index = 0;
    remainingElementCount = 0;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::PromiseExecutionState::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap21PromiseExecutionState11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::PromiseExecutionState::markObjects(b, stack);
}

//  void QV4::Heap::PromiseExecutionState::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap21PromiseExecutionState4initEv(
    QV4::Heap::PromiseExecutionState *self) {
  self->init();
}

//  QV4::Heap::PromiseExecutionState as the
//      QV4::Heap::PromiseExecutionStateData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseExecutionStateData *ritual_cast_QV4_Heap_PromiseExecutionState_QV4_Heap_PromiseExecutionStateData(
    QV4::Heap::PromiseExecutionState *self) {
  return static_cast<QV4::Heap::PromiseExecutionStateData *>(self);
}
