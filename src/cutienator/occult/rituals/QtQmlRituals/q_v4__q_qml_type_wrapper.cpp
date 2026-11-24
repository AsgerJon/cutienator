//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::QQmlTypeWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415QQmlTypeWrapper12staticVTableEv() {
  return QV4::QQmlTypeWrapper::staticVTable();
}

//  void QV4::QQmlTypeWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlTypeWrapper10__dataTestEv(
    QV4::QQmlTypeWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper *ritual_ZNK3QV415QQmlTypeWrapper11d_uncheckedEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper *ritual_ZNK3QV415QQmlTypeWrapper1dEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->d();
}

//  QV4::Object *QV4::QQmlTypeWrapper::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV415QQmlTypeWrapper16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::QQmlTypeWrapper::defaultPrototype(e);
}

//  ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine *a0, QObject
//      *a1, const QQmlType &a2, Heap::QQmlTypeWrapper::TypeNameMode a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper6createEPNS_15ExecutionEngineEP7QObjectRK8QQmlTypeNS_4Heap15QQmlTypeWrapper12TypeNameModeE(
    QV4::ExecutionEngine *a0,
    QObject *a1,
    const QQmlType *a2,
    QV4::Heap::QQmlTypeWrapper::TypeNameMode a3) {
  return QV4::QQmlTypeWrapper::create(a0, a1, *a2, a3);
}
