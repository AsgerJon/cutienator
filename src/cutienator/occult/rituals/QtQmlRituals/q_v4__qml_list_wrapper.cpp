//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  const QV4::VTable *QV4::QmlListWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV414QmlListWrapper12staticVTableEv() {
  return QV4::QmlListWrapper::staticVTable();
}

//  void QV4::QmlListWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414QmlListWrapper10__dataTestEv(QV4::QmlListWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlListWrapper *ritual_ZNK3QV414QmlListWrapper11d_uncheckedEv(
    const QV4::QmlListWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QmlListWrapper *QV4::QmlListWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlListWrapper *ritual_ZNK3QV414QmlListWrapper1dEv(
    const QV4::QmlListWrapper *self) {
  return self->d();
}

//  QV4::Object *QV4::QmlListWrapper::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV414QmlListWrapper16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::QmlListWrapper::defaultPrototype(e);
}

//  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
//      QObject *object, int propId, QMetaType propType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineEP7QObjecti9QMetaType(
    QV4::ExecutionEngine *engine,
    QObject *object,
    int propId,
    const QMetaType *propType) {
  return QV4::QmlListWrapper::create(engine, object, propId, *propType);
}

//  ReturnedValue QV4::QmlListWrapper::create(ExecutionEngine *engine,
//      QMetaType propType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414QmlListWrapper6createEPNS_15ExecutionEngineE9QMetaType(
    QV4::ExecutionEngine *engine,
    const QMetaType *propType) {
  return QV4::QmlListWrapper::create(engine, *propType);
}
