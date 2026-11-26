//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdeferredpointer_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdeferredpointer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlComponentPrivate::DeferredState
//      *QQuickUntypedDeferredPointer::deferredState() const
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::DeferredState *ritual_ZNK28QQuickUntypedDeferredPointer13deferredStateEv(
    const QQuickUntypedDeferredPointer *self) {
  return self->deferredState();
}

//  void QQuickUntypedDeferredPointer::clearDeferredState()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUntypedDeferredPointer18clearDeferredStateEv(
    QQuickUntypedDeferredPointer *self) {
  self->clearDeferredState();
}

//  bool QQuickUntypedDeferredPointer::wasExecuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickUntypedDeferredPointer11wasExecutedEv(
    const QQuickUntypedDeferredPointer *self) {
  return self->wasExecuted();
}

//  void QQuickUntypedDeferredPointer::setExecuted()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUntypedDeferredPointer11setExecutedEv(
    QQuickUntypedDeferredPointer *self) {
  self->setExecuted();
}

//  bool QQuickUntypedDeferredPointer::isExecuting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickUntypedDeferredPointer11isExecutingEv(
    const QQuickUntypedDeferredPointer *self) {
  return self->isExecuting();
}

//  bool QQuickUntypedDeferredPointer::setExecuting(bool b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QQuickUntypedDeferredPointer12setExecutingEb(
    QQuickUntypedDeferredPointer *self,
    bool b) {
  return self->setExecuting(b);
}

//  QQuickUntypedDeferredPointer::QQuickUntypedDeferredPointer()
extern "C" Q_DECL_EXPORT
QQuickUntypedDeferredPointer *ritual_ZN28QQuickUntypedDeferredPointerC1Ev() {
  return new QQuickUntypedDeferredPointer();
}

//  QQuickUntypedDeferredPointer::QQuickUntypedDeferredPointer(void *v)
extern "C" Q_DECL_EXPORT
QQuickUntypedDeferredPointer *ritual_ZN28QQuickUntypedDeferredPointerC1EPv(
    void *v) {
  return new QQuickUntypedDeferredPointer(v);
}

//  QQuickUntypedDeferredPointer
//      &QQuickUntypedDeferredPointer::operator=(void *v)
extern "C" Q_DECL_EXPORT
QQuickUntypedDeferredPointer *ritual_ZN28QQuickUntypedDeferredPointeraSEPv(
    QQuickUntypedDeferredPointer *self,
    void *v) {
  return &(self->operator=(v));
}

//  QQuickUntypedDeferredPointer::~QQuickUntypedDeferredPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUntypedDeferredPointerD1Ev(
    QQuickUntypedDeferredPointer *self) {
  delete self;
}

//  void *QQuickUntypedDeferredPointer::data() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK28QQuickUntypedDeferredPointer4dataEv(
    const QQuickUntypedDeferredPointer *self) {
  return self->data();
}
