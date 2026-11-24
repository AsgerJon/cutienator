//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusabstractadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>

//  bool QDBusAdaptorConnector::AdaptorData::operator<(const AdaptorData
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltERKS0_(
    const QDBusAdaptorConnector::AdaptorData *self,
    const QDBusAdaptorConnector::AdaptorData *other) {
  return self->operator<(*other);
}

//  bool QDBusAdaptorConnector::AdaptorData::operator<(const QString &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltERK7QString(
    const QDBusAdaptorConnector::AdaptorData *self,
    const QString *other) {
  return self->operator<(*other);
}

//  bool QDBusAdaptorConnector::AdaptorData::operator<(QByteArrayView other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusAdaptorConnector11AdaptorDataltE14QByteArrayView(
    const QDBusAdaptorConnector::AdaptorData *self,
    const QByteArrayView *other) {
  return self->operator<(*other);
}

//  QDBusAdaptorConnector::AdaptorData::~AdaptorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusAdaptorConnector11AdaptorDataD1Ev(
    QDBusAdaptorConnector::AdaptorData *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
