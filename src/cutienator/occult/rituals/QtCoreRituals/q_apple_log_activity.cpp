//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  An 'os_activity_t' is passed as an address. Not written: the
//  constructor taking a 'QAppleLogActivity &&', 'enter', which gives
//  one, and 'swap'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN) && !defined(QT_BOOTSTRAPPED) && !__has_feature(objc_arc)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>

//  QAppleLogActivity::QAppleLogActivity()
extern "C" Q_DECL_EXPORT
QAppleLogActivity *ritual_ZN17QAppleLogActivityC1Ev() {
  return new QAppleLogActivity();
}

//  QAppleLogActivity::QAppleLogActivity(os_activity_t activity)
extern "C" Q_DECL_EXPORT
QAppleLogActivity *ritual_ZN17QAppleLogActivityC1EP13os_activity_s(
    os_activity_t activity) {
  return new QAppleLogActivity(activity);
}

//  QAppleLogActivity::~QAppleLogActivity()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAppleLogActivityD1Ev(QAppleLogActivity *self) {
  delete self;
}

//  void QAppleLogActivity::leave()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAppleLogActivity5leaveEv(QAppleLogActivity *self) {
  self->leave();
}

//  os_activity_t QAppleLogActivity::operator os_activity_t()
extern "C" Q_DECL_EXPORT
os_activity_t ritual_ZN17QAppleLogActivitycvP13os_activity_sEv(
    QAppleLogActivity *self) {
  return self->operator os_activity_t();
}

#endif  // defined(Q_OS_DARWIN) && !defined(QT_BOOTSTRAPPED) && !__has_feature(objc_arc)
