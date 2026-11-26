//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  5. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlvaluetypewrapper.cpp, line 44, as _ZN3QV44Heap20QQmlValueTypeWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlValueTypeWrapper::destroy()
{
    metaType().destroy(m_gadgetPtr);
    ReferenceObject::destroy();
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
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QQmlValueTypeWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV420QQmlValueTypeWrapper12staticVTableEv() {
  return QV4::QQmlValueTypeWrapper::staticVTable();
}

//  void QV4::QQmlValueTypeWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420QQmlValueTypeWrapper10__dataTestEv(
    QV4::QQmlValueTypeWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlValueTypeWrapper *QV4::QQmlValueTypeWrapper::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlValueTypeWrapper *ritual_ZNK3QV420QQmlValueTypeWrapper11d_uncheckedEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlValueTypeWrapper *QV4::QQmlValueTypeWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlValueTypeWrapper *ritual_ZNK3QV420QQmlValueTypeWrapper1dEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::QQmlValueTypeWrapper::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV420QQmlValueTypeWrapper16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::QQmlValueTypeWrapper::defaultPrototype(e);
}

//  void QV4::QQmlValueTypeWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420QQmlValueTypeWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QQmlValueTypeWrapper::virtualDestroy(b);
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine *engine,
//      const void *data, const QMetaObject *metaObject, QMetaType type,
//      Heap::Object *object, int property, Heap::ReferenceObject::Flags
//      flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper6createEPNS_15ExecutionEngineEPKvPK11QMetaObject9QMetaTypePNS_4Heap6ObjectEi6QFlagsINS9_15ReferenceObject4FlagEE(
    QV4::ExecutionEngine *engine,
    const void *data,
    const QMetaObject *metaObject,
    const QMetaType *type,
    QV4::Heap::Object *object,
    int property,
    int flags) {
  return QV4::QQmlValueTypeWrapper::create(
      engine,
      data,
      metaObject,
      *type,
      object,
      property,
      QFlags<QV4::Heap::ReferenceObject::Flag>::fromInt(flags));
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine *engine,
//      Heap::QQmlValueTypeWrapper *cloneFrom, Heap::Object *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper6createEPNS_15ExecutionEngineEPNS_4Heap20QQmlValueTypeWrapperEPNS3_6ObjectE(
    QV4::ExecutionEngine *engine,
    QV4::Heap::QQmlValueTypeWrapper *cloneFrom,
    QV4::Heap::Object *object) {
  return QV4::QQmlValueTypeWrapper::create(engine, cloneFrom, object);
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine *engine,
//      const void *a1, const QMetaObject *metaObject, QMetaType type)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper6createEPNS_15ExecutionEngineEPKvPK11QMetaObject9QMetaType(
    QV4::ExecutionEngine *engine,
    const void *a1,
    const QMetaObject *metaObject,
    const QMetaType *type) {
  return QV4::QQmlValueTypeWrapper::create(engine, a1, metaObject, *type);
}

//  QVariant QV4::QQmlValueTypeWrapper::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV420QQmlValueTypeWrapper9toVariantEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return new QVariant(self->toVariant());
}

//  bool QV4::QQmlValueTypeWrapper::toGadget(void *data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV420QQmlValueTypeWrapper8toGadgetEPv(
    const QV4::QQmlValueTypeWrapper *self,
    void *data) {
  return self->toGadget(data);
}

//  bool QV4::QQmlValueTypeWrapper::isEqual(const QVariant &value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV420QQmlValueTypeWrapper7isEqualERK8QVariant(
    const QV4::QQmlValueTypeWrapper *self,
    const QVariant *value) {
  return self->isEqual(*value);
}

//  int QV4::QQmlValueTypeWrapper::typeId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV420QQmlValueTypeWrapper6typeIdEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->typeId();
}

//  QMetaType QV4::QQmlValueTypeWrapper::type() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV420QQmlValueTypeWrapper4typeEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return new QMetaType(self->type());
}

//  bool QV4::QQmlValueTypeWrapper::write(QObject *target, int propertyIndex)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV420QQmlValueTypeWrapper5writeEP7QObjecti(
    const QV4::QQmlValueTypeWrapper *self,
    QObject *target,
    int propertyIndex) {
  return self->write(target, propertyIndex);
}

//  bool QV4::QQmlValueTypeWrapper::readReferenceValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV420QQmlValueTypeWrapper18readReferenceValueEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->readReferenceValue();
}

//  const QMetaObject *QV4::QQmlValueTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV420QQmlValueTypeWrapper10metaObjectEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->metaObject();
}

//  QQmlPropertyData
//      QV4::QQmlValueTypeWrapper::dataForPropertyKey(PropertyKey id) const
extern "C" Q_DECL_EXPORT
QQmlPropertyData *ritual_ZNK3QV420QQmlValueTypeWrapper18dataForPropertyKeyENS_11PropertyKeyE(
    const QV4::QQmlValueTypeWrapper *self,
    const QV4::PropertyKey *id) {
  return new QQmlPropertyData(self->dataForPropertyKey(*id));
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QQmlValueTypeWrapper::virtualGet(
      m,
      *id,
      receiver,
      hasProperty);
}

//  bool QV4::QQmlValueTypeWrapper::virtualPut(Managed *m, PropertyKey id,
//      const Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV420QQmlValueTypeWrapper10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::QQmlValueTypeWrapper::virtualPut(m, *id, *value, receiver);
}

//  bool QV4::QQmlValueTypeWrapper::virtualIsEqualTo(Managed *m, Managed
//      *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV420QQmlValueTypeWrapper16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *m,
    QV4::Managed *other) {
  return QV4::QQmlValueTypeWrapper::virtualIsEqualTo(m, other);
}

//  bool QV4::QQmlValueTypeWrapper::virtualHasProperty(const Managed *m,
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV420QQmlValueTypeWrapper18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::QQmlValueTypeWrapper::virtualHasProperty(m, *id);
}

//  PropertyAttributes QV4::QQmlValueTypeWrapper::virtualGetOwnProperty(const
//      Managed *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV420QQmlValueTypeWrapper21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::QQmlValueTypeWrapper::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  OwnPropertyKeyIterator
//      *QV4::QQmlValueTypeWrapper::virtualOwnPropertyKeys(const Object *m,
//      Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV420QQmlValueTypeWrapper22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::QQmlValueTypeWrapper::virtualOwnPropertyKeys(m, target);
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::method_toString(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QQmlValueTypeWrapper::method_toString(
      b,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::QQmlValueTypeWrapper::virtualResolveLookupGetter(const
//      Object *object, ExecutionEngine *engine, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper26virtualResolveLookupGetterEPKNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return QV4::QQmlValueTypeWrapper::virtualResolveLookupGetter(
      object,
      engine,
      lookup);
}

//  bool QV4::QQmlValueTypeWrapper::virtualResolveLookupSetter(Object
//      *object, ExecutionEngine *engine, Lookup *lookup, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV420QQmlValueTypeWrapper26virtualResolveLookupSetterEPNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE(
    QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup,
    const QV4::Value *value) {
  return QV4::QQmlValueTypeWrapper::virtualResolveLookupSetter(
      object,
      engine,
      lookup,
      *value);
}

//  void QV4::QQmlValueTypeWrapper::initProto(ExecutionEngine *v4)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV420QQmlValueTypeWrapper9initProtoEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *v4) {
  QV4::QQmlValueTypeWrapper::initProto(v4);
}

//  int QV4::QQmlValueTypeWrapper::virtualMetacall(Object *object,
//      QMetaObject::Call call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV420QQmlValueTypeWrapper15virtualMetacallEPNS_6ObjectEN11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::QQmlValueTypeWrapper::virtualMetacall(object, call, index, a);
}

//  ReturnedValue
//      QV4::QQmlValueTypeWrapper::getGadgetProperty(ExecutionEngine *engine,
//      Heap::QQmlValueTypeWrapper *valueTypeWrapper, QMetaType metaType,
//      quint16 coreIndex, bool isFunction, bool isEnum)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper17getGadgetPropertyEPNS_15ExecutionEngineEPNS_4Heap20QQmlValueTypeWrapperE9QMetaTypetbb(
    QV4::ExecutionEngine *engine,
    QV4::Heap::QQmlValueTypeWrapper *valueTypeWrapper,
    const QMetaType *metaType,
    quint16 coreIndex,
    bool isFunction,
    bool isEnum) {
  return QV4::QQmlValueTypeWrapper::getGadgetProperty(
      engine,
      valueTypeWrapper,
      *metaType,
      coreIndex,
      isFunction,
      isEnum);
}

//  int *QV4::QQmlValueTypeWrapper::cast<int>() const
extern "C" Q_DECL_EXPORT
int * ritual_ZNK3QV420QQmlValueTypeWrapper4castIiEEPT_v(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->cast<int>();
}

//  double *QV4::QQmlValueTypeWrapper::cast<double>() const
extern "C" Q_DECL_EXPORT
double * ritual_ZNK3QV420QQmlValueTypeWrapper4castIdEEPT_v(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->cast<double>();
}

//  bool *QV4::QQmlValueTypeWrapper::cast<bool>() const
extern "C" Q_DECL_EXPORT
bool * ritual_ZNK3QV420QQmlValueTypeWrapper4castIbEEPT_v(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->cast<bool>();
}

//  QString *QV4::QQmlValueTypeWrapper::cast<QString>() const
extern "C" Q_DECL_EXPORT
QString * ritual_ZNK3QV420QQmlValueTypeWrapper4castI7QStringEEPT_v(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->cast<QString>();
}

//  QVariant *QV4::QQmlValueTypeWrapper::cast<QVariant>() const
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZNK3QV420QQmlValueTypeWrapper4castI8QVariantEEPT_v(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->cast<QVariant>();
}
