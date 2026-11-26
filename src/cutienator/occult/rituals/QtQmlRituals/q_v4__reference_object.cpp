//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 539, as _ZN3QV44Heap15ReferenceObject17connectToBindableEP7QObjectiP10QQmlEngine
namespace QV4 {
inline void Heap::ReferenceObject::connectToBindable(QObject *obj, int property, QQmlEngine *engine)
{
    Q_ASSERT(obj);
    Q_ASSERT(engine);

    Q_ASSERT(!referenceEndpoint);
    Q_ASSERT(!bindableNotifier);

    bindableNotifier = new QPropertyNotifier(obj->metaObject()->property(property).bindable(obj)
                                                     .addNotifier([this](){ setDirty(true); }));
    new (onDelete) QMetaObject::Connection(
            QObject::connect(obj, &QObject::destroyed, obj, [this]() { setDirty(true); }));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 493, as _ZN3QV44Heap15ReferenceObject21connectToNotifySignalEP7QObjectiP10QQmlEngine
namespace QV4 {
inline void Heap::ReferenceObject::connectToNotifySignal(QObject *obj, int property, QQmlEngine *engine)
{
    Q_ASSERT(obj);
    Q_ASSERT(engine);

    Q_ASSERT(!referenceEndpoint);
    Q_ASSERT(!bindableNotifier);

    referenceEndpoint = new ReferenceObjectEndpoint(this);

    // Connect and signal emission work on "signal indexes". Those are different from "method
    // indexes".
    // The public MetaObject interface can, generally, give us the "method index" of the notify
    // signal.
    // Quite unintuitively, this is true for "notifySignalIndex". As the "method index" and the
    // "signal index" can be different, connecting the "method index" of the notify signal can
    // incur in issues when the signal is being emitted and checking for connected endpoints.
    // For example, we might be connected to the "method index" of the notify signal for the
    // property and end up checking for the subscribers of a different signal when the notify
    // signal is emitted, due to the different meaning of the same index.
    // Thus we pass by the private interface to ensure that we are connecting based on the "signal
    // index" instead.
    const int index = QMetaObjectPrivate::signalIndex(obj->metaObject()->property(property)
                                                                    .notifySignal());
    QQmlData::connectEndpoint(referenceEndpoint, obj, index, engine);

    // When the object that is being referenced is destroyed, we
    // need to ensure that one additional read is performed to
    // invalidate the data we hold.
    // As the object might be destroyed in a way that doesn't
    // trigger the notify signal for the relevant property, we react
    // directly to the destruction itself.
    // We use a plain connection instead of a QQmlNotifierEndpoint
    // based connection as, currently, declarative-side signals are
    // always discarded during destruction (see
    // QQmlData::signalEmitted).
    // In theory it should be possible to relax that condition for
    // the destroy signal specifically, which should allow a more
    // optimized way of connecting.
    // Nonetheless this seems to be the only place where we have
    // this kind of need, and thus go for the simpler solution,
    // which can be changed later if the need arises.
    new (onDelete) QMetaObject::Connection(
            QObject::connect(obj, &QObject::destroyed, obj, [this](){ setDirty(true); }));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 553, as _ZN3QV415ReferenceObject13shouldConnectEPNS_4Heap15ReferenceObjectE
namespace QV4 {
inline bool ReferenceObject::shouldConnect(Heap::ReferenceObject *ref)
{
    if (ref->isAlwaysDirty())
        return false;

    // We want to connect when we are reading the reference object from a statement that is not
    // its creation statement. In other words, when first storing it in a variable and then
    // reusing it, potentially multiple times. This ensures that the cost of the connection itself
    // is only paid when the user separated the declaration from the usage in their code, in the
    // hope that this catches more complex and frequent uses, like accesses in a loop, where
    // unnecessary copies would impact performance more significantly, and not one time accesses.
    if (CppStackFrame *frame = ref->internalClass->engine->currentStackFrame) {
        const auto *refObject = static_cast<Heap::ReferenceObject *>(ref);
        if (frame->v4Function && frame->v4Function == refObject->function()
            && frame->statementNumber() == refObject->statementIndex()) {
            return false;
        }
    }
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4referenceobject.cpp, line 574, as _ZN3QV415ReferenceObject7connectEPNS_4Heap15ReferenceObjectE
namespace QV4 {
inline void ReferenceObject::connect(Heap::ReferenceObject *ref)
{
    int property = ref->property();
    Heap::Object *object = ref->object();

    while (object
           && object->internalClass->vtable->type != Managed::Type_V4QObjectWrapper
           && object->internalClass->vtable->type != Managed::Type_QMLTypeWrapper)
    {
        const auto type = object->internalClass->vtable->type;
        if (type != Managed::Type_V4ReferenceObject
            && type != Managed::Type_V4Sequence
            && type != Managed::Type_DateObject
            && type != Managed::Type_QMLValueTypeWrapper) {
            break;
        }

        property = static_cast<QV4::Heap::ReferenceObject *>(object)->property();
        object = static_cast<QV4::Heap::ReferenceObject *>(object)->object();
    }

    const auto doConnect = [&](auto wrapper) {
        // The object may be valid on the first read but not on the second, check for that.
        if (QObject *obj = wrapper->object()) {
            auto *refObject = static_cast<Heap::ReferenceObject *>(ref);

            auto *qmlEngine = object->internalClass->engine->qmlEngine();
            if (qmlEngine && obj->metaObject()->property(property).isBindable())
                refObject->connectToBindable(obj, property, qmlEngine);
            else if (qmlEngine && obj->metaObject()->property(property).hasNotifySignal())
                refObject->connectToNotifySignal(obj, property, qmlEngine);
        }
    };

    if (object && object->internalClass->vtable->type == Managed::Type_V4QObjectWrapper) {
        doConnect(static_cast<QV4::Heap::QObjectWrapper *>(object));
    } else if (object && object->internalClass->vtable->type == Managed::Type_QMLTypeWrapper) {
        auto wrapper = static_cast<QV4::Heap::QQmlTypeWrapper *>(object);
        Scope scope(object->internalClass->engine);
        Scoped<QV4::QQmlTypeWrapper> scopedWrapper(scope, wrapper);
        doConnect(scopedWrapper);
    }

    if (!ref->isConnected()) {
        // Mark AlwaysDirty to prevent further connection failures on every read
        ref->setAlwaysDirty(true);
    }
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ReferenceObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ReferenceObject10__dataTestEv(
    QV4::ReferenceObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObject *ritual_ZNK3QV415ReferenceObject11d_uncheckedEv(
    const QV4::ReferenceObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObject *ritual_ZNK3QV415ReferenceObject1dEv(
    const QV4::ReferenceObject *self) {
  return self->d();
}

//  void QV4::ReferenceObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ReferenceObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ReferenceObject::virtualDestroy(b);
}

//  bool QV4::ReferenceObject::shouldConnect(Heap::ReferenceObject *ref)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415ReferenceObject13shouldConnectEPNS_4Heap15ReferenceObjectE(
    QV4::Heap::ReferenceObject *ref) {
  return QV4::ReferenceObject::shouldConnect(ref);
}

//  void QV4::ReferenceObject::connect(Heap::ReferenceObject *ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ReferenceObject7connectEPNS_4Heap15ReferenceObjectE(
    QV4::Heap::ReferenceObject *ref) {
  QV4::ReferenceObject::connect(ref);
}
