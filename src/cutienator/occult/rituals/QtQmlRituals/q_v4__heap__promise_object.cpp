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

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 323, as _ZN3QV44Heap13PromiseObject4initEPNS_15ExecutionEngineE
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseObject::init(ExecutionEngine *e)
{
    Heap::Object::init();

    {
        Heap::ArrayObject* a = e->newArrayObject();
        fulfillReactions.set(e, a);
    }

    {
        Heap::ArrayObject* a = e->newArrayObject();
        rejectReactions.set(e, a);
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 211, as _ZN3QV44Heap13PromiseObject8setStateENS1_5StateE
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseObject::setState(PromiseObject::State state)
{
    this->state = state;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 216, as _ZNK3QV44Heap13PromiseObject9isSettledEv
namespace QV4 {
using namespace QV4::Promise;
inline bool Heap::PromiseObject::isSettled() const
{
    return (state != Pending);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 221, as _ZNK3QV44Heap13PromiseObject9isPendingEv
namespace QV4 {
using namespace QV4::Promise;
inline bool Heap::PromiseObject::isPending() const
{
    return (state == Pending);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 226, as _ZNK3QV44Heap13PromiseObject11isFulfilledEv
namespace QV4 {
using namespace QV4::Promise;
inline bool Heap::PromiseObject::isFulfilled() const
{
    return (state == Fulfilled);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 231, as _ZNK3QV44Heap13PromiseObject10isRejectedEv
namespace QV4 {
using namespace QV4::Promise;
inline bool Heap::PromiseObject::isRejected() const
{
    return (state == Rejected);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::PromiseObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13PromiseObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::PromiseObject::markObjects(b, stack);
}

//  void QV4::Heap::PromiseObject::init(ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13PromiseObject4initEPNS_15ExecutionEngineE(
    QV4::Heap::PromiseObject *self,
    QV4::ExecutionEngine *e) {
  self->init(e);
}

//  void QV4::Heap::PromiseObject::setState(State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13PromiseObject8setStateENS1_5StateE(
    QV4::Heap::PromiseObject *self,
    QV4::Heap::PromiseObject::State a0) {
  self->setState(a0);
}

//  bool QV4::Heap::PromiseObject::isSettled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13PromiseObject9isSettledEv(
    const QV4::Heap::PromiseObject *self) {
  return self->isSettled();
}

//  bool QV4::Heap::PromiseObject::isPending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13PromiseObject9isPendingEv(
    const QV4::Heap::PromiseObject *self) {
  return self->isPending();
}

//  bool QV4::Heap::PromiseObject::isFulfilled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13PromiseObject11isFulfilledEv(
    const QV4::Heap::PromiseObject *self) {
  return self->isFulfilled();
}

//  bool QV4::Heap::PromiseObject::isRejected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13PromiseObject10isRejectedEv(
    const QV4::Heap::PromiseObject *self) {
  return self->isRejected();
}

//  QV4::Heap::PromiseObject as the QV4::Heap::PromiseObjectData it is built
//      on
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseObjectData *ritual_cast_QV4_Heap_PromiseObject_QV4_Heap_PromiseObjectData(
    QV4::Heap::PromiseObject *self) {
  return static_cast<QV4::Heap::PromiseObjectData *>(self);
}
