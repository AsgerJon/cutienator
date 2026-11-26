//  Edited by hand on 2026-11-25: the header 'qdbusconnection_p.h',
//  which declares 'QDBusConnectionPrivate' in full, is included before
//  'qdbusthreaddebug_p.h': its inline functions reach into that class,
//  and the compiler had only the name of it. Kept as it is when the
//  generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusthreaddebug_p.h, Qt 6.12.0.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/6.12.0/QtDBus/private/qdbusthreaddebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDBusReadLocker::QDBusReadLocker(ThreadAction a, QDBusConnectionPrivate
//      *s)
extern "C" Q_DECL_EXPORT
QDBusReadLocker *ritual_ZN15QDBusReadLockerC1E12ThreadActionP22QDBusConnectionPrivate(
    ThreadAction a,
    QDBusConnectionPrivate *s) {
  return new QDBusReadLocker(a, s);
}

//  QDBusReadLocker::~QDBusReadLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusReadLockerD1Ev(QDBusReadLocker *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
