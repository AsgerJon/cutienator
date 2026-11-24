//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::QQmlContextWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV418QQmlContextWrapper12staticVTableEv() {
  return QV4::QQmlContextWrapper::staticVTable();
}

//  void QV4::QQmlContextWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418QQmlContextWrapper10__dataTestEv(
    QV4::QQmlContextWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZNK3QV418QQmlContextWrapper11d_uncheckedEv(
    const QV4::QQmlContextWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlContextWrapper *QV4::QQmlContextWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZNK3QV418QQmlContextWrapper1dEv(
    const QV4::QQmlContextWrapper *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::QQmlContextWrapper::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV418QQmlContextWrapper20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::QQmlContextWrapper::defaultInternalClass(e);
}

//  QObject *QV4::QQmlContextWrapper::getScopeObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV418QQmlContextWrapper14getScopeObjectEv(
    const QV4::QQmlContextWrapper *self) {
  return self->getScopeObject();
}
