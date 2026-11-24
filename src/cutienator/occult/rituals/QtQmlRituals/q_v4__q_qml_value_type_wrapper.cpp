//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  ReturnedValue QV4::QQmlValueTypeWrapper::create(ExecutionEngine *engine,
//      Heap::QQmlValueTypeWrapper *cloneFrom, Heap::Object *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420QQmlValueTypeWrapper6createEPNS_15ExecutionEngineEPNS_4Heap20QQmlValueTypeWrapperEPNS3_6ObjectE(
    QV4::ExecutionEngine *engine,
    QV4::Heap::QQmlValueTypeWrapper *cloneFrom,
    QV4::Heap::Object *object) {
  return QV4::QQmlValueTypeWrapper::create(engine, cloneFrom, object);
}

//  const QMetaObject *QV4::QQmlValueTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV420QQmlValueTypeWrapper10metaObjectEv(
    const QV4::QQmlValueTypeWrapper *self) {
  return self->metaObject();
}
