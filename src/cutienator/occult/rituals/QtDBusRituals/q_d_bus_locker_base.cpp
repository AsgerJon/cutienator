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

#if !(QDBUS_THREAD_DEBUG)
//  void QDBusLockerBase::reportThreadAction(int a0, int a1,
//      QDBusConnectionPrivate *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusLockerBase18reportThreadActionEiiP22QDBusConnectionPrivate(
    int a0,
    int a1,
    QDBusConnectionPrivate *a2) {
  QDBusLockerBase::reportThreadAction(a0, a1, a2);
}
#endif  // !(QDBUS_THREAD_DEBUG)

//  QDBusLockerBase::~QDBusLockerBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusLockerBaseD1Ev(QDBusLockerBase *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
