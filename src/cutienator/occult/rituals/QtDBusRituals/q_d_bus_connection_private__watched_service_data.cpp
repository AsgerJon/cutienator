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
#include <QtCore/qstring.h>

//  QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData()
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::WatchedServiceData *ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataC1Ev() {
  return new QDBusConnectionPrivate::WatchedServiceData();
}

//  QDBusConnectionPrivate::WatchedServiceData::WatchedServiceData(const
//      QString &owner, int refcount)
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate::WatchedServiceData *ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataC1ERK7QStringi(
    const QString *owner,
    int refcount) {
  return new QDBusConnectionPrivate::WatchedServiceData(*owner, refcount);
}

//  QDBusConnectionPrivate::WatchedServiceData::~WatchedServiceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate18WatchedServiceDataD1Ev(
    QDBusConnectionPrivate::WatchedServiceData *self) {
  delete self;
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
