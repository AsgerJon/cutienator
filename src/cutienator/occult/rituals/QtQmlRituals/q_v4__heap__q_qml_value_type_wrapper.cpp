//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4referenceobject_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlvaluetype_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4jsonobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtCore/qline.h>
#include <QtCore/qsize.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(regularexpression)
#include <QtQml/private/qv4regexpobject_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 38, as _ZNK3QV44Heap20QQmlValueTypeWrapper8detachedEv
namespace QV4 {
inline Heap::QQmlValueTypeWrapper *Heap::QQmlValueTypeWrapper::detached() const
{
    return internalClass->engine->memoryManager->allocate<QV4::QQmlValueTypeWrapper>(
        m_gadgetPtr, QMetaType(m_metaType), m_metaObject, nullptr, -1, NoFlag);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 44, as _ZN3QV44Heap20QQmlValueTypeWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlValueTypeWrapper::destroy()
{
    metaType().destroy(m_gadgetPtr);
    ReferenceObject::destroy();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 50, as _ZNK3QV44Heap20QQmlValueTypeWrapper9toVariantEv
namespace QV4 {
inline QVariant Heap::QQmlValueTypeWrapper::toVariant() const
{
    Q_ASSERT(gadgetPtr());
    return QVariant(metaType(), gadgetPtr());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 83, as _ZN3QV44Heap20QQmlValueTypeWrapper14storagePointerEv
namespace QV4 {
inline void *Heap::QQmlValueTypeWrapper::storagePointer()
{
    if (!gadgetPtr()) {
        setGadgetPtr(metaType().create(nullptr));
    }
    return gadgetPtr();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 56, as _ZN3QV44Heap20QQmlValueTypeWrapper10setVariantERK8QVariant
namespace QV4 {
inline bool Heap::QQmlValueTypeWrapper::setVariant(const QVariant &variant)
{
    Q_ASSERT(isVariant());

    const QMetaType variantReferenceType = variant.metaType();
    if (variantReferenceType != metaType()) {
        // This is a stale VariantReference.  That is, the variant has been
        // overwritten with a different type in the meantime.
        // We need to modify this reference to the updated value type, if
        // possible, or return false if it is not a value type.
        if (QQmlMetaType::isValueType(variantReferenceType)) {
            const QMetaObject *mo = QQmlMetaType::metaObjectForValueType(variantReferenceType);
            metaType().destroy(gadgetPtr());
            setGadgetPtr(nullptr);
            setMetaObject(mo);
            setMetaType(variantReferenceType);
            if (!mo)
                return false;
        } else {
            return false;
        }
    }

    setData(variant.constData());
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 91, as _ZN3QV44Heap20QQmlValueTypeWrapper13readReferenceEv
namespace QV4 {
inline bool Heap::QQmlValueTypeWrapper::readReference()
{
    // If locations are enforced we only read once
    return enforcesLocation() || QV4::ReferenceObject::readReference(this);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 97, as _ZN3QV44Heap20QQmlValueTypeWrapper9writeBackEi
namespace QV4 {
inline bool Heap::QQmlValueTypeWrapper::writeBack(int propertyIndex)
{
    return isAttachedToProperty() && QV4::ReferenceObject::writeBack(this, propertyIndex);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QQmlValueTypeWrapper::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlValueTypeWrapper::markObjects(b, stack);
}

//  void QV4::Heap::QQmlValueTypeWrapper::init(const void *data, QMetaType
//      metaType, const QMetaObject *metaObject, Object *object, int
//      property, Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper4initEPKv9QMetaTypePK11QMetaObjectPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const void *data,
    const QMetaType *metaType,
    const QMetaObject *metaObject,
    QV4::Heap::Object *object,
    int property,
    int flags) {
  self->init(
      data,
      *metaType,
      metaObject,
      object,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  QQmlValueTypeWrapper *QV4::Heap::QQmlValueTypeWrapper::detached() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlValueTypeWrapper *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper8detachedEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->detached();
}

//  void QV4::Heap::QQmlValueTypeWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper7destroyEv(
    QV4::Heap::QQmlValueTypeWrapper *self) {
  self->destroy();
}

//  QMetaType QV4::Heap::QQmlValueTypeWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper8metaTypeEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return new QMetaType(self->metaType());
}

//  void QV4::Heap::QQmlValueTypeWrapper::setGadgetPtr(void *gadgetPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper12setGadgetPtrEPv(
    QV4::Heap::QQmlValueTypeWrapper *self,
    void *gadgetPtr) {
  self->setGadgetPtr(gadgetPtr);
}

//  void *QV4::Heap::QQmlValueTypeWrapper::gadgetPtr() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper9gadgetPtrEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->gadgetPtr();
}

//  const QMetaObject *QV4::Heap::QQmlValueTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper10metaObjectEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->metaObject();
}

//  void QV4::Heap::QQmlValueTypeWrapper::setData(const void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper7setDataEPKv(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const void *data) {
  self->setData(data);
}

//  QVariant QV4::Heap::QQmlValueTypeWrapper::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper9toVariantEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return new QVariant(self->toVariant());
}

//  void *QV4::Heap::QQmlValueTypeWrapper::storagePointer()
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV44Heap20QQmlValueTypeWrapper14storagePointerEv(
    QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->storagePointer();
}

//  bool QV4::Heap::QQmlValueTypeWrapper::setVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap20QQmlValueTypeWrapper10setVariantERK8QVariant(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const QVariant *variant) {
  return self->setVariant(*variant);
}

//  bool QV4::Heap::QQmlValueTypeWrapper::readReference()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap20QQmlValueTypeWrapper13readReferenceEv(
    QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->readReference();
}

//  bool QV4::Heap::QQmlValueTypeWrapper::writeBack(int propertyIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap20QQmlValueTypeWrapper9writeBackEi(
    QV4::Heap::QQmlValueTypeWrapper *self,
    int propertyIndex) {
  return self->writeBack(propertyIndex);
}

//  void QV4::Heap::QQmlValueTypeWrapper::setMetaObject(const QMetaObject
//      *metaObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper13setMetaObjectEPK11QMetaObject(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const QMetaObject *metaObject) {
  self->setMetaObject(metaObject);
}

//  void QV4::Heap::QQmlValueTypeWrapper::setMetaType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper11setMetaTypeE9QMetaType(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const QMetaType *metaType) {
  self->setMetaType(*metaType);
}

//  QV4::Heap::QQmlValueTypeWrapper as the
//      QV4::Heap::QQmlValueTypeWrapperData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlValueTypeWrapperData *ritual_cast_QV4_Heap_QQmlValueTypeWrapper_QV4_Heap_QQmlValueTypeWrapperData(
    QV4::Heap::QQmlValueTypeWrapper *self) {
  return static_cast<QV4::Heap::QQmlValueTypeWrapperData *>(self);
}
