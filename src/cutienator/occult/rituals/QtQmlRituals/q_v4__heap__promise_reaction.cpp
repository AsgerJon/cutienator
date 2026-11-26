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

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 54, as local:qv4promiseobject.cpp:PROMISE_REACTION_EVENT
namespace QV4::Promise {
using namespace QV4;
const int PROMISE_REACTION_EVENT = QEvent::registerEventType();
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 57, as local:qv4promiseobject.cpp:ReactionEvent
namespace QV4::Promise {
using namespace QV4;
struct ReactionEvent : public QEvent
{
    ReactionEvent(ExecutionEngine *e, const Value *reaction_, const Value *resolution_)
            : QEvent(QEvent::Type(PROMISE_REACTION_EVENT)),
              reaction{e, *reaction_},
              resolution{e, *resolution_}
    {}

    QV4::PersistentValue reaction;
    QV4::PersistentValue resolution;
};
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 91, as _ZN3QV47Promise15ReactionHandler11addReactionEPNS_15ExecutionEngineEPKNS_5ValueES6_
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::addReaction(ExecutionEngine *e, const Value *reaction, const Value *value)
{
    QCoreApplication::postEvent(this, new ReactionEvent(e, reaction, value));
}
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 310, as _ZN3QV44Heap15PromiseReaction16triggerWithValueEPNS_15ExecutionEngineEPKNS_5ValueE
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseReaction::triggerWithValue(ExecutionEngine *e, const Value *value)
{
    Scope scope(e);
    auto handler =  e->getPromiseReactionHandler();
    ScopedValue reaction(scope, Value::fromHeapObject(this));
    handler->addReaction(e, reaction, value);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::PromiseReaction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15PromiseReaction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::PromiseReaction::markObjects(b, stack);
}

//  void QV4::Heap::PromiseReaction::triggerWithValue(ExecutionEngine *e,
//      const Value *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15PromiseReaction16triggerWithValueEPNS_15ExecutionEngineEPKNS_5ValueE(
    QV4::Heap::PromiseReaction *self,
    QV4::ExecutionEngine *e,
    const QV4::Value *value) {
  self->triggerWithValue(e, value);
}

//  QV4::Heap::PromiseReaction as the QV4::Heap::PromiseReactionData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseReactionData *ritual_cast_QV4_Heap_PromiseReaction_QV4_Heap_PromiseReactionData(
    QV4::Heap::PromiseReaction *self) {
  return static_cast<QV4::Heap::PromiseReactionData *>(self);
}
