//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::QMetaObjectWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV418QMetaObjectWrapper12staticVTableEv() {
  return QV4::QMetaObjectWrapper::staticVTable();
}

//  void QV4::QMetaObjectWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QMetaObjectWrapper10__dataTestEv(
    QV4::QMetaObjectWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QMetaObjectWrapper *ritual_ZNK3QV418QMetaObjectWrapper11d_uncheckedEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QMetaObjectWrapper *QV4::QMetaObjectWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QMetaObjectWrapper *ritual_ZNK3QV418QMetaObjectWrapper1dEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->d();
}

//  ReturnedValue QV4::QMetaObjectWrapper::create(ExecutionEngine *engine,
//      const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV418QMetaObjectWrapper6createEPNS_15ExecutionEngineEPK11QMetaObject(
    QV4::ExecutionEngine *engine,
    const QMetaObject *metaObject) {
  return QV4::QMetaObjectWrapper::create(engine, metaObject);
}

//  const QMetaObject *QV4::QMetaObjectWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV418QMetaObjectWrapper10metaObjectEv(
    const QV4::QMetaObjectWrapper *self) {
  return self->metaObject();
}
