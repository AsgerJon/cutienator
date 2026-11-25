//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcfsocketnotifier_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  A function pointer is passed as an address. Not written:
//  'enableSocketNotifiers', whose 'CFRunLoopActivity' the SDKs of
//  Apple spell in more than one way.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcfsocketnotifier_p.h>
#include <QtCore/qsocketnotifier.h>

//  QCFSocketNotifier::QCFSocketNotifier()
extern "C" Q_DECL_EXPORT
QCFSocketNotifier *ritual_ZN17QCFSocketNotifierC1Ev() {
  return new QCFSocketNotifier();
}

//  QCFSocketNotifier::~QCFSocketNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifierD1Ev(QCFSocketNotifier *self) {
  delete self;
}

//  void QCFSocketNotifier::setHostEventDispatcher(QAbstractEventDispatcher
//      *hostEventDispacher)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier22setHostEventDispatcherEP24QAbstractEventDispatcher(
    QCFSocketNotifier *self,
    QAbstractEventDispatcher *hostEventDispacher) {
  self->setHostEventDispatcher(hostEventDispacher);
}

//  void QCFSocketNotifier::setMaybeCancelWaitForMoreEventsCallback(MaybeCanc
//      elWaitForMoreEventsFn callBack)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier39setMaybeCancelWaitForMoreEventsCallbackEPFvP24QAbstractEventDispatcherE(
    QCFSocketNotifier *self,
    MaybeCancelWaitForMoreEventsFn callBack) {
  self->setMaybeCancelWaitForMoreEventsCallback(callBack);
}

//  void QCFSocketNotifier::registerSocketNotifier(QSocketNotifier *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier22registerSocketNotifierEP15QSocketNotifier(
    QCFSocketNotifier *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void QCFSocketNotifier::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier24unregisterSocketNotifierEP15QSocketNotifier(
    QCFSocketNotifier *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

//  void QCFSocketNotifier::removeSocketNotifiers()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier21removeSocketNotifiersEv(
    QCFSocketNotifier *self) {
  self->removeSocketNotifiers();
}

//  void QCFSocketNotifier::destroyRunLoopObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier22destroyRunLoopObserverEv(
    QCFSocketNotifier *self) {
  self->destroyRunLoopObserver();
}

//  void QCFSocketNotifier::unregisterSocketInfo(MacSocketInfo *socketInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCFSocketNotifier20unregisterSocketInfoEP13MacSocketInfo(
    MacSocketInfo *socketInfo) {
  QCFSocketNotifier::unregisterSocketInfo(socketInfo);
}

#endif  // defined(Q_OS_DARWIN)
