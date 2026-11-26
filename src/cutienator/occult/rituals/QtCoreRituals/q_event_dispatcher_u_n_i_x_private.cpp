//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif

//  QEventDispatcherUNIX *QEventDispatcherUNIXPrivate::q_func()
extern "C" Q_DECL_EXPORT
QEventDispatcherUNIX *ritual_ZN27QEventDispatcherUNIXPrivate6q_funcEv(
    QEventDispatcherUNIXPrivate *self) {
  return self->q_func();
}

//  const QEventDispatcherUNIX *QEventDispatcherUNIXPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QEventDispatcherUNIX *ritual_ZNK27QEventDispatcherUNIXPrivate6q_funcEv(
    const QEventDispatcherUNIXPrivate *self) {
  return self->q_func();
}

//  QEventDispatcherUNIXPrivate::QEventDispatcherUNIXPrivate()
extern "C" Q_DECL_EXPORT
QEventDispatcherUNIXPrivate *ritual_ZN27QEventDispatcherUNIXPrivateC1Ev() {
  return new QEventDispatcherUNIXPrivate();
}

//  QEventDispatcherUNIXPrivate::~QEventDispatcherUNIXPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QEventDispatcherUNIXPrivateD1Ev(
    QEventDispatcherUNIXPrivate *self) {
  delete self;
}

//  int QEventDispatcherUNIXPrivate::activateTimers()
extern "C" Q_DECL_EXPORT
int ritual_ZN27QEventDispatcherUNIXPrivate14activateTimersEv(
    QEventDispatcherUNIXPrivate *self) {
  return self->activateTimers();
}

//  void QEventDispatcherUNIXPrivate::markPendingSocketNotifiers()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QEventDispatcherUNIXPrivate26markPendingSocketNotifiersEv(
    QEventDispatcherUNIXPrivate *self) {
  self->markPendingSocketNotifiers();
}

//  int QEventDispatcherUNIXPrivate::activateSocketNotifiers()
extern "C" Q_DECL_EXPORT
int ritual_ZN27QEventDispatcherUNIXPrivate23activateSocketNotifiersEv(
    QEventDispatcherUNIXPrivate *self) {
  return self->activateSocketNotifiers();
}

//  void
//      QEventDispatcherUNIXPrivate::setSocketNotifierPending(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QEventDispatcherUNIXPrivate24setSocketNotifierPendingEP15QSocketNotifier(
    QEventDispatcherUNIXPrivate *self,
    QSocketNotifier *notifier) {
  self->setSocketNotifierPending(notifier);
}

#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
