//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::QmlContext::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV410QmlContext12staticVTableEv() {
  return QV4::QmlContext::staticVTable();
}

//  void QV4::QmlContext::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410QmlContext10__dataTestEv(QV4::QmlContext *self) {
  self->__dataTest();
}

//  QV4::Heap::QmlContext *QV4::QmlContext::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContext *ritual_ZNK3QV410QmlContext11d_uncheckedEv(
    const QV4::QmlContext *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QmlContext *QV4::QmlContext::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContext *ritual_ZNK3QV410QmlContext1dEv(
    const QV4::QmlContext *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::QmlContext::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV410QmlContext20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::QmlContext::defaultInternalClass(e);
}

//  Heap::QmlContext *QV4::QmlContext::create(QV4::ExecutionContext *parent,
//      QQmlRefPointer<QQmlContextData> context, QObject *scopeObject)
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContext *ritual_ZN3QV410QmlContext6createEPNS_16ExecutionContextE14QQmlRefPointerI15QQmlContextDataEP7QObject(
    QV4::ExecutionContext *parent,
    const QQmlRefPointer<QQmlContextData> *context,
    QObject *scopeObject) {
  return QV4::QmlContext::create(parent, *context, scopeObject);
}

//  QObject *QV4::QmlContext::qmlScope() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV410QmlContext8qmlScopeEv(const QV4::QmlContext *self) {
  return self->qmlScope();
}

//  QQmlRefPointer<QQmlContextData> QV4::QmlContext::qmlContext() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZNK3QV410QmlContext10qmlContextEv(
    const QV4::QmlContext *self) {
  return new QQmlRefPointer<QQmlContextData>(self->qmlContext());
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QV4::QmlContext gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_QmlContext__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}
