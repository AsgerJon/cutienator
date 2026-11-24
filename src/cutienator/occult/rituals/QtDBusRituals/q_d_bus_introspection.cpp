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
#include <QtCore/qstring.h>

//  Interface QDBusIntrospection::parseInterface(const QString &xml,
//      DiagnosticsReporter *reporter)
extern "C" Q_DECL_EXPORT
QDBusIntrospection::Interface *ritual_ZN18QDBusIntrospection14parseInterfaceERK7QStringPNS_19DiagnosticsReporterE(
    const QString *xml,
    QDBusIntrospection::DiagnosticsReporter *reporter) {
  return new QDBusIntrospection::Interface(
      QDBusIntrospection::parseInterface(
          *xml,
          reporter));
}

//  Object QDBusIntrospection::parseObject(const QString &xml, const QString
//      &service, const QString &path, DiagnosticsReporter *reporter)
extern "C" Q_DECL_EXPORT
QDBusIntrospection::Object *ritual_ZN18QDBusIntrospection11parseObjectERK7QStringS2_S2_PNS_19DiagnosticsReporterE(
    const QString *xml,
    const QString *service,
    const QString *path,
    QDBusIntrospection::DiagnosticsReporter *reporter) {
  return new QDBusIntrospection::Object(
      QDBusIntrospection::parseObject(
          *xml,
          *service,
          *path,
          reporter));
}

//  QDBusIntrospection::~QDBusIntrospection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDBusIntrospectionD1Ev(QDBusIntrospection *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
