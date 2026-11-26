//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::QObjectWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV414QObjectWrapper12staticVTableEv() {
  return QV4::QObjectWrapper::staticVTable();
}

//  void QV4::QObjectWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper10__dataTestEv(QV4::QObjectWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectWrapper *ritual_ZNK3QV414QObjectWrapper11d_uncheckedEv(
    const QV4::QObjectWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QObjectWrapper *QV4::QObjectWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectWrapper *ritual_ZNK3QV414QObjectWrapper1dEv(
    const QV4::QObjectWrapper *self) {
  return self->d();
}

//  void QV4::QObjectWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QObjectWrapper::virtualDestroy(b);
}

//  void QV4::QObjectWrapper::initializeBindings(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper18initializeBindingsEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  QV4::QObjectWrapper::initializeBindings(engine);
}

//  const QMetaObject *QV4::QObjectWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV414QObjectWrapper10metaObjectEv(
    const QV4::QObjectWrapper *self) {
  return self->metaObject();
}

//  QObject *QV4::QObjectWrapper::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV414QObjectWrapper6objectEv(
    const QV4::QObjectWrapper *self) {
  return self->object();
}

//  ReturnedValue QV4::QObjectWrapper::getQmlProperty(const
//      QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags
//      flags, bool *hasProperty) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV414QObjectWrapper14getQmlPropertyERK14QQmlRefPointerI15QQmlContextDataEPNS_6StringE6QFlagsINS0_4FlagEEPb(
    const QV4::QObjectWrapper *self,
    const QQmlRefPointer<QQmlContextData> *qmlContext,
    QV4::String *name,
    int flags,
    bool *hasProperty) {
  return self->getQmlProperty(
      *qmlContext,
      name,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags),
      hasProperty);
}

//  ReturnedValue QV4::QObjectWrapper::getQmlProperty(ExecutionEngine
//      *engine, const QQmlRefPointer<QQmlContextData> &qmlContext,
//      Heap::Object *wrapper, QObject *object, String *name, Flags flags,
//      bool *hasProperty, const QQmlPropertyData **property)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper14getQmlPropertyEPNS_15ExecutionEngineERK14QQmlRefPointerI15QQmlContextDataEPNS_4Heap6ObjectEP7QObjectPNS_6StringE6QFlagsINS0_4FlagEEPbPPK16QQmlPropertyData(
    QV4::ExecutionEngine *engine,
    const QQmlRefPointer<QQmlContextData> *qmlContext,
    QV4::Heap::Object *wrapper,
    QObject *object,
    QV4::String *name,
    int flags,
    bool *hasProperty,
    const QQmlPropertyData **property) {
  return QV4::QObjectWrapper::getQmlProperty(
      engine,
      *qmlContext,
      wrapper,
      object,
      name,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags),
      hasProperty,
      property);
}

//  bool QV4::QObjectWrapper::setQmlProperty(ExecutionEngine *engine, const
//      QQmlRefPointer<QQmlContextData> &qmlContext, QObject *object, String
//      *name, Flags flags, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414QObjectWrapper14setQmlPropertyEPNS_15ExecutionEngineERK14QQmlRefPointerI15QQmlContextDataEP7QObjectPNS_6StringE6QFlagsINS0_4FlagEERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QQmlRefPointer<QQmlContextData> *qmlContext,
    QObject *object,
    QV4::String *name,
    int flags,
    const QV4::Value *value) {
  return QV4::QObjectWrapper::setQmlProperty(
      engine,
      *qmlContext,
      object,
      name,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags),
      *value);
}

//  ReturnedValue QV4::QObjectWrapper::wrap(ExecutionEngine *engine, QObject
//      *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper4wrapEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  return QV4::QObjectWrapper::wrap(engine, object);
}

//  ReturnedValue QV4::QObjectWrapper::wrapConst(ExecutionEngine *engine,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper9wrapConstEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  return QV4::QObjectWrapper::wrapConst(engine, object);
}

//  void QV4::QObjectWrapper::ensureWrapper(ExecutionEngine *engine, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper13ensureWrapperEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  QV4::QObjectWrapper::ensureWrapper(engine, object);
}

//  void QV4::QObjectWrapper::markWrapper(QObject *object, MarkStack
//      *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper11markWrapperEP7QObjectPNS_9MarkStackE(
    QObject *object,
    QV4::MarkStack *markStack) {
  QV4::QObjectWrapper::markWrapper(object, markStack);
}

//  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, QObject
//      *object, int propertyIndex, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEP7QObjectiRKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    QObject *object,
    int propertyIndex,
    const QV4::Value *value) {
  QV4::QObjectWrapper::setProperty(engine, object, propertyIndex, *value);
}

//  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, int
//      propertyIndex, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEiRKNS_5ValueE(
    QV4::QObjectWrapper *self,
    QV4::ExecutionEngine *engine,
    int propertyIndex,
    const QV4::Value *value) {
  self->setProperty(engine, propertyIndex, *value);
}

//  void QV4::QObjectWrapper::setProperty(ExecutionEngine *engine, QObject
//      *object, const QQmlPropertyData *property, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper11setPropertyEPNS_15ExecutionEngineEP7QObjectPK16QQmlPropertyDataRKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    QObject *object,
    const QQmlPropertyData *property,
    const QV4::Value *value) {
  QV4::QObjectWrapper::setProperty(engine, object, property, *value);
}

//  void QV4::QObjectWrapper::destroyObject(bool lastCall)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QObjectWrapper13destroyObjectEb(
    QV4::QObjectWrapper *self,
    bool lastCall) {
  self->destroyObject(lastCall);
}

//  ReturnedValue QV4::QObjectWrapper::getProperty(ExecutionEngine *engine,
//      Heap::Object *wrapper, QObject *object, const QQmlPropertyData
//      *property, Flags flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper11getPropertyEPNS_15ExecutionEngineEPNS_4Heap6ObjectEP7QObjectPK16QQmlPropertyData6QFlagsINS0_4FlagEE(
    QV4::ExecutionEngine *engine,
    QV4::Heap::Object *wrapper,
    QObject *object,
    const QQmlPropertyData *property,
    int flags) {
  return QV4::QObjectWrapper::getProperty(
      engine,
      wrapper,
      object,
      property,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags));
}

//  ReturnedValue QV4::QObjectWrapper::virtualResolveLookupGetter(const
//      Object *object, ExecutionEngine *engine, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper26virtualResolveLookupGetterEPKNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return QV4::QObjectWrapper::virtualResolveLookupGetter(
      object,
      engine,
      lookup);
}

//  bool QV4::QObjectWrapper::virtualResolveLookupSetter(Object *object,
//      ExecutionEngine *engine, Lookup *lookup, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414QObjectWrapper26virtualResolveLookupSetterEPNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE(
    QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup,
    const QV4::Value *value) {
  return QV4::QObjectWrapper::virtualResolveLookupSetter(
      object,
      engine,
      lookup,
      *value);
}

//  OwnPropertyKeyIterator *QV4::QObjectWrapper::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV414QObjectWrapper22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::QObjectWrapper::virtualOwnPropertyKeys(m, target);
}

//  int QV4::QObjectWrapper::virtualMetacall(Object *object,
//      QMetaObject::Call call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV414QObjectWrapper15virtualMetacallEPNS_6ObjectEN11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::QObjectWrapper::virtualMetacall(object, call, index, a);
}

//  QString QV4::QObjectWrapper::objectToString(ExecutionEngine *engine,
//      const QMetaObject *metaObject, QObject *object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV414QObjectWrapper14objectToStringEPNS_15ExecutionEngineEPK11QMetaObjectP7QObject(
    QV4::ExecutionEngine *engine,
    const QMetaObject *metaObject,
    QObject *object) {
  return new QString(
      QV4::QObjectWrapper::objectToString(
          engine,
          metaObject,
          object));
}

//  bool QV4::QObjectWrapper::virtualIsEqualTo(Managed *that, Managed *o)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414QObjectWrapper16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *that,
    QV4::Managed *o) {
  return QV4::QObjectWrapper::virtualIsEqualTo(that, o);
}

//  ReturnedValue QV4::QObjectWrapper::create(ExecutionEngine *engine,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper6createEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  return QV4::QObjectWrapper::create(engine, object);
}

//  const QQmlPropertyData *QV4::QObjectWrapper::findProperty(QObject *o,
//      const QQmlRefPointer<QQmlContextData> &qmlContext, String *name,
//      Flags flags, QQmlPropertyData *local)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN3QV414QObjectWrapper12findPropertyEP7QObjectRK14QQmlRefPointerI15QQmlContextDataEPNS_6StringE6QFlagsINS0_4FlagEEP16QQmlPropertyData(
    QObject *o,
    const QQmlRefPointer<QQmlContextData> *qmlContext,
    QV4::String *name,
    int flags,
    QQmlPropertyData *local) {
  return QV4::QObjectWrapper::findProperty(
      o,
      *qmlContext,
      name,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags),
      local);
}

//  const QQmlPropertyData *QV4::QObjectWrapper::findProperty(const
//      QQmlRefPointer<QQmlContextData> &qmlContext, String *name, Flags
//      flags, QQmlPropertyData *local) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK3QV414QObjectWrapper12findPropertyERK14QQmlRefPointerI15QQmlContextDataEPNS_6StringE6QFlagsINS0_4FlagEEP16QQmlPropertyData(
    const QV4::QObjectWrapper *self,
    const QQmlRefPointer<QQmlContextData> *qmlContext,
    QV4::String *name,
    int flags,
    QQmlPropertyData *local) {
  return self->findProperty(
      *qmlContext,
      name,
      QFlags<QV4::QObjectWrapper::Flag>::fromInt(flags),
      local);
}

//  ReturnedValue QV4::QObjectWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QObjectWrapper::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::QObjectWrapper::virtualPut(Managed *m, PropertyKey id, const
//      Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414QObjectWrapper10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::QObjectWrapper::virtualPut(m, *id, *value, receiver);
}

//  PropertyAttributes QV4::QObjectWrapper::virtualGetOwnProperty(const
//      Managed *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV414QObjectWrapper21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::QObjectWrapper::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  ReturnedValue QV4::QObjectWrapper::method_connect(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper14method_connectEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QObjectWrapper::method_connect(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::QObjectWrapper::method_disconnect(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper17method_disconnectEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QObjectWrapper::method_disconnect(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::QObjectWrapper::wrap_slowPath(ExecutionEngine *engine,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper13wrap_slowPathEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  return QV4::QObjectWrapper::wrap_slowPath(engine, object);
}

//  ReturnedValue QV4::QObjectWrapper::wrapConst_slowPath(ExecutionEngine
//      *engine, QObject *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QObjectWrapper18wrapConst_slowPathEPNS_15ExecutionEngineEP7QObject(
    QV4::ExecutionEngine *engine,
    QObject *object) {
  return QV4::QObjectWrapper::wrapConst_slowPath(engine, object);
}
