//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h>

//  QEventDispatcherWin32 *QEventDispatcherWin32Private::q_func()
extern "C" Q_DECL_EXPORT
QEventDispatcherWin32 *ritual_ZN28QEventDispatcherWin32Private6q_funcEv(
    QEventDispatcherWin32Private *self) {
  return self->q_func();
}

//  const QEventDispatcherWin32 *QEventDispatcherWin32Private::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QEventDispatcherWin32 *ritual_ZNK28QEventDispatcherWin32Private6q_funcEv(
    const QEventDispatcherWin32Private *self) {
  return self->q_func();
}

//  QEventDispatcherWin32Private::QEventDispatcherWin32Private()
extern "C" Q_DECL_EXPORT
QEventDispatcherWin32Private *ritual_ZN28QEventDispatcherWin32PrivateC1Ev() {
  return new QEventDispatcherWin32Private();
}

//  QEventDispatcherWin32Private::~QEventDispatcherWin32Private()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32PrivateD1Ev(
    QEventDispatcherWin32Private *self) {
  delete self;
}

//  void QEventDispatcherWin32Private::startPostedEventsTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private22startPostedEventsTimerEv(
    QEventDispatcherWin32Private *self) {
  self->startPostedEventsTimer();
}

//  void QEventDispatcherWin32Private::registerTimer(WinTimerInfo *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private13registerTimerEP12WinTimerInfo(
    QEventDispatcherWin32Private *self,
    WinTimerInfo *t) {
  self->registerTimer(t);
}

//  void QEventDispatcherWin32Private::unregisterTimer(WinTimerInfo *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private15unregisterTimerEP12WinTimerInfo(
    QEventDispatcherWin32Private *self,
    WinTimerInfo *t) {
  self->unregisterTimer(t);
}

//  void QEventDispatcherWin32Private::sendTimerEvent(int timerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private14sendTimerEventEi(
    QEventDispatcherWin32Private *self,
    int timerId) {
  self->sendTimerEvent(timerId);
}

//  void QEventDispatcherWin32Private::postActivateSocketNotifiers()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private27postActivateSocketNotifiersEv(
    QEventDispatcherWin32Private *self) {
  self->postActivateSocketNotifiers();
}

//  void QEventDispatcherWin32Private::doWsaAsyncSelect(qintptr socket, long
//      event)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QEventDispatcherWin32Private16doWsaAsyncSelectExl(
    QEventDispatcherWin32Private *self,
    qintptr socket,
    long event) {
  self->doWsaAsyncSelect(socket, event);
}

#endif  // defined(Q_OS_WIN)
