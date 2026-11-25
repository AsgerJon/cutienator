//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  Not written: the constructor taking a 'QMacNotificationObserver &&',
//  and 'swap'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>

//  QMacNotificationObserver::QMacNotificationObserver()
extern "C" Q_DECL_EXPORT
QMacNotificationObserver *ritual_ZN24QMacNotificationObserverC1Ev() {
  return new QMacNotificationObserver();
}

//  void QMacNotificationObserver::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMacNotificationObserver6removeEv(
    QMacNotificationObserver *self) {
  self->remove();
}

//  QMacNotificationObserver::~QMacNotificationObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QMacNotificationObserverD1Ev(
    QMacNotificationObserver *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
