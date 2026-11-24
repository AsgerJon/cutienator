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

//  bool QDBusIntrospection::Argument::operator==(const Argument &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QDBusIntrospection8ArgumenteqERKS0_(
    const QDBusIntrospection::Argument *self,
    const QDBusIntrospection::Argument *other) {
  return self->operator==(*other);
}

//  QDBusIntrospection::Argument::~Argument()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDBusIntrospection8ArgumentD1Ev(
    QDBusIntrospection::Argument *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
