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

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 55, as local:qv4promiseobject.cpp:PROMISE_RESOLVE_THENABLE_EVENT
namespace QV4::Promise {
using namespace QV4;
const int PROMISE_RESOLVE_THENABLE_EVENT = QEvent::registerEventType();
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 69, as local:qv4promiseobject.cpp:ResolveThenableEvent
namespace QV4::Promise {
using namespace QV4;
struct ResolveThenableEvent : public QEvent
{
    ResolveThenableEvent(ExecutionEngine *e, const PromiseObject *promise_, const Object *thenable_, const FunctionObject *then_)
        : QEvent(QEvent::Type(PROMISE_RESOLVE_THENABLE_EVENT)), promise(e, *promise_), thenable(e, *thenable_), then(e, *then_)
    {}

    QV4::PersistentValue promise;
    QV4::PersistentValue thenable;
    QV4::PersistentValue then;
};
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 251, as _ZN3QV44Heap13PromiseObject22triggerRejectReactionsEPNS_15ExecutionEngineE
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseObject::triggerRejectReactions(ExecutionEngine *e)
{
    Scope scope(e);
    ScopedArrayObject a(scope, rejectReactions);
    if (a->arrayData()) {
        Scoped<QV4::ArrayData> ad(scope, a->arrayData());
        const uint sz = ad->d()->length();
        ScopedValue value(scope, resolution);
        for (uint i = 0; i < sz; i++) {
            Scoped<QV4::PromiseReaction> r(scope, ad->d()->get(i));
            r->d()->triggerWithValue(scope.engine, value);
        }
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 236, as _ZN3QV44Heap13PromiseObject24triggerFullfillReactionsEPNS_15ExecutionEngineE
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::PromiseObject::triggerFullfillReactions(ExecutionEngine *e)
{
    Scope scope(e);
    ScopedArrayObject a(scope, fulfillReactions);
    if (a->arrayData()) {
        Scoped<QV4::ArrayData> ad(scope, a->arrayData());
        const uint sz = ad->length();
        ScopedValue value(scope, resolution);
        for (uint i = 0; i < sz; i++) {
            Scoped<QV4::PromiseReaction> r(scope, ad->get(i));
            r->d()->triggerWithValue(scope.engine, value);
        }
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 96, as _ZN3QV47Promise15ReactionHandler18addResolveThenableEPNS_15ExecutionEngineEPKNS_13PromiseObjectEPKNS_6ObjectEPKNS_14FunctionObjectE
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::addResolveThenable(ExecutionEngine *e, const PromiseObject *promise, const Object *thenable, const FunctionObject *then)
{
    QCoreApplication::postEvent(this, new ResolveThenableEvent(e, promise, thenable, then));
}
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 221, as _ZNK3QV44Heap13PromiseObject9isPendingEv
namespace QV4 {
using namespace QV4::Promise;
inline bool Heap::PromiseObject::isPending() const
{
    return (state == Pending);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ResolveWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414ResolveWrapper10__dataTestEv(QV4::ResolveWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::ResolveWrapper *QV4::ResolveWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ResolveWrapper *ritual_ZNK3QV414ResolveWrapper11d_uncheckedEv(
    const QV4::ResolveWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ResolveWrapper *QV4::ResolveWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ResolveWrapper *ritual_ZNK3QV414ResolveWrapper1dEv(
    const QV4::ResolveWrapper *self) {
  return self->d();
}
