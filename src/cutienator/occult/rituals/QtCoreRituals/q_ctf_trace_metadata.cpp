//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qctf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(ctf)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qctf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QCtfTraceMetadata::QCtfTraceMetadata(QCtfTracePointProvider &provider,
//      const QString &name, const QString &metadata)
extern "C" Q_DECL_EXPORT
QCtfTraceMetadata *ritual_ZN17QCtfTraceMetadataC1ER22QCtfTracePointProviderRK7QStringS4_(
    QCtfTracePointProvider *provider,
    const QString *name,
    const QString *metadata) {
  return new QCtfTraceMetadata(*provider, *name, *metadata);
}

//  QCtfTraceMetadata::~QCtfTraceMetadata()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCtfTraceMetadataD1Ev(QCtfTraceMetadata *self) {
  delete self;
}

#endif  // QT_CONFIG(ctf)
