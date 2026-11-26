//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetasequence.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 95, as local:qv4sequenceobject.cpp:createVariantData
namespace QV4 {
static void *createVariantData(QMetaType type, QVariant *variant)
{
    if (type == QMetaType::fromType<QVariant>())
        return variant;
    *variant = QVariant(type);
    return variant->data();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 111, as local:qv4sequenceobject.cpp:generateWarning
namespace QV4 {
static void generateWarning(QV4::ExecutionEngine *v4, const QString& description)
{
    QQmlEngine *engine = v4->qmlEngine();
    if (!engine)
        return;
    QQmlError retn;
    retn.setDescription(description);

    QV4::CppStackFrame *stackFrame = v4->currentStackFrame;

    retn.setLine(stackFrame->lineNumber());
    retn.setUrl(QUrl(stackFrame->source()));
    QQmlEnginePrivate::warning(engine, retn);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 218, as _ZN3QV44Heap8Sequence21createElementWrappersEPKv
namespace QV4 {
inline void Heap::Sequence::createElementWrappers(const void *container)
{
    Q_ASSERT(!isStoredInline());

    if (!container)
        return;

    const QMetaSequence metaSequence(m_metaSequence);
    const QMetaType valueMetaType = metaSequence.valueMetaType();
    const qsizetype size = metaSequence.size(container);

    QV4::Scope scope(internalClass->engine);
    if (!qIsAtMostUintLimit(size)) {
        generateWarning(scope.engine, QLatin1String("Sequence length out of range"));
        return;
    }

    QV4::Scoped<QV4::Sequence> self(scope, this);
    self->arrayReserve(size);
    QV4::ScopedValue v(scope);
    if (valueMetaType == QMetaType::fromType<QVariant>()) {
        QVariant var;
        for (qsizetype i = 0; i < size; ++i) {
            metaSequence.valueAtIndex(container, i, &var);
            v = scope.engine->metaTypeToJS(var.metaType(), var.constData());
            self->arraySet(i, v);
        }
    } else {
        QVariant var(valueMetaType);
        for (qsizetype i = 0; i < size; ++i) {
            metaSequence.valueAtIndex(container, i, var.data());
            v = scope.engine->metaTypeToJS(valueMetaType, var.constData());
            self->arraySet(i, v);
        }
    }

    m_size = size;
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 179, as _ZN3QV44Heap8Sequence4initE9QMetaType13QMetaSequencePKv
namespace QV4 {
inline void Heap::Sequence::init(QMetaType listType, QMetaSequence metaSequence, const void *container)
{
    ReferenceObject::init(nullptr, -1, NoFlag);
    initTypes(listType,  metaSequence);
    if (isStoredInline())
        createInlineStorage(container);
    else
        createElementWrappers(container);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 189, as _ZN3QV44Heap8Sequence4initE9QMetaType13QMetaSequencePKvPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE
namespace QV4 {
inline void Heap::Sequence::init(
        QMetaType listType, QMetaSequence metaSequence, const void *container,
        Heap::Object *object, int propertyIndex, Heap::ReferenceObject::Flags flags)
{
    ReferenceObject::init(object, propertyIndex, flags | IsDirty);
    initTypes(listType, metaSequence);

    if (isStoredInline()) {
        if (CppStackFrame *frame = internalClass->engine->currentStackFrame)
            setLocation(frame->v4Function, frame->statementNumber());
        createInlineStorage(container);
        if (!container && (flags & EnforcesLocation))
            QV4::ReferenceObject::readReference(this);
    } else {
        createElementWrappers(container);
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 257, as _ZN3QV44Heap8Sequence8detachedEv
namespace QV4 {
inline Heap::Sequence *Heap::Sequence::detached()
{
    const QMetaType listType(m_listType);
    const QMetaSequence metaSequence(m_metaSequence);
    if (isStoredInline()) {
        return internalClass->engine->memoryManager->allocate<QV4::Sequence>(
                listType, metaSequence, m_container);
    }

    QVariant list(listType);

    const QMetaType valueMetaType(m_metaSequence->valueMetaType);
    QVariant element;
    void *elementData = createVariantData(valueMetaType, &element);

    QV4::Scope scope(internalClass->engine);
    if (qIsAtMostSizetypeLimit(m_size)) {
        QV4::Scoped<QV4::Sequence> self(scope, this);
        QV4::ScopedValue v(scope);
        for (uint i = 0; i < m_size; ++i) {
            v = self->get(PropertyKey::fromArrayIndex(i));
            ExecutionEngine::metaTypeFromJS(v, valueMetaType, elementData);
            metaSequence.addValue(list.data(), elementData);
        }
    } else {
        generateWarning(scope.engine, QLatin1String("Index out of range during toVariant()"));
    }

    return scope.engine->memoryManager->allocate<QV4::Sequence>(
            listType, metaSequence, list.constData());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 289, as _ZN3QV44Heap8Sequence7destroyEv
namespace QV4 {
inline void Heap::Sequence::destroy()
{
    if (isStoredInline() && m_container)
        listType().destroy(m_container);
    ReferenceObject::destroy();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 296, as _ZN3QV44Heap8Sequence14storagePointerEv
namespace QV4 {
inline void *Heap::Sequence::storagePointer()
{
    if (!isStoredInline())
        return nullptr;
    if (!m_container)
        m_container = listType().create();
    return m_container;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 305, as _ZN3QV44Heap8Sequence10setVariantERK8QVariant
namespace QV4 {
inline bool Heap::Sequence::setVariant(const QVariant &variant)
{
    // Should only happen from readReference(). Therefore we are attached.
    Q_ASSERT(isStoredInline());

    const QMetaType variantReferenceType = variant.metaType();
    if (variantReferenceType != listType()) {
        // This is a stale reference. That is, the property has been
        // overwritten with a different type in the meantime.
        // We need to modify this reference to the updated type, if
        // possible, or return false if it is not a sequence.
        const QQmlType newType = QQmlMetaType::qmlListType(variantReferenceType);
        if (newType.isSequentialContainer()) {
            if (m_container)
                listType().destroy(m_container);
            m_listType = newType.qListTypeId().iface();
            m_metaSequence = newType.listMetaSequence().iface();
            m_container = listType().create(variant.constData());
            return true;
        } else {
            return false;
        }
    }
    if (m_container) {
        variantReferenceType.destruct(m_container);
        variantReferenceType.construct(m_container, variant.constData());
    } else {
        m_container = variantReferenceType.create(variant.constData());
    }
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 336, as _ZNK3QV44Heap8Sequence9toVariantEv
namespace QV4 {
inline QVariant Heap::Sequence::toVariant() const
{
    // Should only happen from readReference(). Therefore we are attached.
    Q_ASSERT(isStoredInline());

    return QVariant(listType(), m_container);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 171, as _ZN3QV44Heap8Sequence9initTypesE9QMetaType13QMetaSequence
namespace QV4 {
inline void Heap::Sequence::initTypes(QMetaType listType, QMetaSequence metaSequence)
{
    m_listType = listType.iface();
    Q_ASSERT(m_listType);
    m_metaSequence = metaSequence.iface();
    Q_ASSERT(m_metaSequence);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 207, as _ZN3QV44Heap8Sequence19createInlineStorageEPKv
namespace QV4 {
inline void Heap::Sequence::createInlineStorage(const void *container)
{
    Q_ASSERT(isStoredInline());

    QV4::Scope scope(internalClass->engine);
    QV4::Scoped<QV4::Sequence> o(scope, this);
    o->setArrayType(Heap::ArrayData::Custom);
    if (container)
        m_container = listType().create(container);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 401, as _ZN3QV44Heap8Sequence13loadReferenceEv
namespace QV4 {
inline bool Heap::Sequence::loadReference()
{
    Q_ASSERT(isReference());
    // If locations are enforced we only read once
    return enforcesLocation() || QV4::ReferenceObject::readReference(this);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4sequenceobject.cpp, line 408, as _ZN3QV44Heap8Sequence14storeReferenceEv
namespace QV4 {
inline bool Heap::Sequence::storeReference()
{
    Q_ASSERT(isReference());
    return isAttachedToProperty() && QV4::ReferenceObject::writeBack(this);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::Sequence::init(QMetaType listType, QMetaSequence
//      metaSequence, const void *container)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap8Sequence4initE9QMetaType13QMetaSequencePKv(
    QV4::Heap::Sequence *self,
    const QMetaType *listType,
    const QMetaSequence *metaSequence,
    const void *container) {
  self->init(*listType, *metaSequence, container);
}

//  void QV4::Heap::Sequence::init(QMetaType listType, QMetaSequence
//      metaSequence, const void *container, Object *object, int
//      propertyIndex, Heap::ReferenceObject::Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap8Sequence4initE9QMetaType13QMetaSequencePKvPNS0_6ObjectEi6QFlagsINS0_15ReferenceObject4FlagEE(
    QV4::Heap::Sequence *self,
    const QMetaType *listType,
    const QMetaSequence *metaSequence,
    const void *container,
    QV4::Heap::Object *object,
    int propertyIndex,
    int flags) {
  self->init(
      *listType,
      *metaSequence,
      container,
      object,
      propertyIndex,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  Sequence *QV4::Heap::Sequence::detached()
extern "C" Q_DECL_EXPORT
QV4::Heap::Sequence *ritual_ZN3QV44Heap8Sequence8detachedEv(
    QV4::Heap::Sequence *self) {
  return self->detached();
}

//  void QV4::Heap::Sequence::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap8Sequence7destroyEv(QV4::Heap::Sequence *self) {
  self->destroy();
}

//  void *QV4::Heap::Sequence::storagePointer()
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV44Heap8Sequence14storagePointerEv(
    QV4::Heap::Sequence *self) {
  return self->storagePointer();
}

//  const void *QV4::Heap::Sequence::storagePointer() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK3QV44Heap8Sequence14storagePointerEv(
    const QV4::Heap::Sequence *self) {
  return self->storagePointer();
}

//  bool QV4::Heap::Sequence::isStoredInline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap8Sequence14isStoredInlineEv(
    const QV4::Heap::Sequence *self) {
  return self->isStoredInline();
}

//  bool QV4::Heap::Sequence::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap8Sequence10isReadOnlyEv(
    const QV4::Heap::Sequence *self) {
  return self->isReadOnly();
}

//  bool QV4::Heap::Sequence::setVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap8Sequence10setVariantERK8QVariant(
    QV4::Heap::Sequence *self,
    const QVariant *variant) {
  return self->setVariant(*variant);
}

//  QVariant QV4::Heap::Sequence::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Heap8Sequence9toVariantEv(
    const QV4::Heap::Sequence *self) {
  return new QVariant(self->toVariant());
}

//  QMetaType QV4::Heap::Sequence::listType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap8Sequence8listTypeEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaType(self->listType());
}

//  QMetaType QV4::Heap::Sequence::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap8Sequence13valueMetaTypeEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaType(self->valueMetaType());
}

//  QMetaSequence QV4::Heap::Sequence::metaSequence() const
extern "C" Q_DECL_EXPORT
QMetaSequence *ritual_ZNK3QV44Heap8Sequence12metaSequenceEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaSequence(self->metaSequence());
}

//  void QV4::Heap::Sequence::initTypes(QMetaType listType, QMetaSequence
//      metaSequence)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap8Sequence9initTypesE9QMetaType13QMetaSequence(
    QV4::Heap::Sequence *self,
    const QMetaType *listType,
    const QMetaSequence *metaSequence) {
  self->initTypes(*listType, *metaSequence);
}

//  void QV4::Heap::Sequence::createInlineStorage(const void *container)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap8Sequence19createInlineStorageEPKv(
    QV4::Heap::Sequence *self,
    const void *container) {
  self->createInlineStorage(container);
}

//  bool QV4::Heap::Sequence::loadReference()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap8Sequence13loadReferenceEv(
    QV4::Heap::Sequence *self) {
  return self->loadReference();
}

//  bool QV4::Heap::Sequence::storeReference()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap8Sequence14storeReferenceEv(
    QV4::Heap::Sequence *self) {
  return self->storeReference();
}
