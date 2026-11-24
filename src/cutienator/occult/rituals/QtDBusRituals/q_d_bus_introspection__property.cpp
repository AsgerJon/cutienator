//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusintrospection_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusintrospection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QDBusIntrospection::Property::operator==(const Property &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDBusIntrospection8PropertyeqERKS0_(
    const QDBusIntrospection::Property *self,
    const QDBusIntrospection::Property *other) {
  return self->operator==(*other);
}

//  QDBusIntrospection::Property::~Property()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDBusIntrospection8PropertyD1Ev(
    QDBusIntrospection::Property *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
