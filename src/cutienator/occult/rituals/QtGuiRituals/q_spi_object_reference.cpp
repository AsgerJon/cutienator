//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qspi_struct_marshallers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbusextratypes.h>

//  QSpiObjectReference::QSpiObjectReference(const QDBusConnection
//      &connection, const QDBusObjectPath &path)
extern "C" Q_DECL_EXPORT
QSpiObjectReference *ritual_ZN19QSpiObjectReferenceC1ERK15QDBusConnectionRK15QDBusObjectPath(
    const QDBusConnection *connection,
    const QDBusObjectPath *path) {
  return new QSpiObjectReference(*connection, *path);
}

//  QSpiObjectReference::~QSpiObjectReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSpiObjectReferenceD1Ev(QSpiObjectReference *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
