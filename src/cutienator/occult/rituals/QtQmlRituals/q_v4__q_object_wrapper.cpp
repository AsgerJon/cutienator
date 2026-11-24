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

//  OwnPropertyKeyIterator *QV4::QObjectWrapper::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV414QObjectWrapper22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::QObjectWrapper::virtualOwnPropertyKeys(m, target);
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
