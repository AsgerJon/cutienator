//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDBusConnectionPrivate::SignalHook::SignalHook()
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::SignalHook *ritual_ZN22QDBusConnectionPrivate10SignalHookC1Ev() {
  return new QDBusConnectionPrivate::SignalHook();
}

//  QDBusConnectionPrivate::SignalHook::~SignalHook()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate10SignalHookD1Ev(
    QDBusConnectionPrivate::SignalHook *self) {
  delete self;
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
