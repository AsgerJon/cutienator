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

//  QCtfTracePointProvider::QCtfTracePointProvider(const QString &provider)
extern "C" Q_DECL_EXPORT
QCtfTracePointProvider *ritual_ZN22QCtfTracePointProviderC1ERK7QString(
    const QString *provider) {
  return new QCtfTracePointProvider(*provider);
}

//  QCtfTracePointProvider::~QCtfTracePointProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCtfTracePointProviderD1Ev(QCtfTracePointProvider *self) {
  delete self;
}

#endif  // QT_CONFIG(ctf)
