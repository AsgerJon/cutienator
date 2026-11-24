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

//  QDBusConnectionPrivate::Watcher::Watcher()
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::Watcher *ritual_ZN22QDBusConnectionPrivate7WatcherC1Ev() {
  return new QDBusConnectionPrivate::Watcher();
}

//  QDBusConnectionPrivate::Watcher::~Watcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate7WatcherD1Ev(
    QDBusConnectionPrivate::Watcher *self) {
  delete self;
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
