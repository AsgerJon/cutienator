//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QDBusCallDeliveryEvent::placeMetaCall(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusCallDeliveryEvent13placeMetaCallEP7QObject(
    QDBusCallDeliveryEvent *self,
    QObject *object) {
  self->placeMetaCall(object);
}

//  QDBusCallDeliveryEvent::~QDBusCallDeliveryEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusCallDeliveryEventD1Ev(QDBusCallDeliveryEvent *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
