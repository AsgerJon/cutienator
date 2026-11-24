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

//  QCtfTracePointEvent::QCtfTracePointEvent(const QCtfTracePointProvider
//      &provider, const QString &name, const QString &metadata, int size,
//      bool variableSize)
extern "C" Q_DECL_EXPORT
QCtfTracePointEvent *ritual_ZN19QCtfTracePointEventC1ERK22QCtfTracePointProviderRK7QStringS5_ib(
    const QCtfTracePointProvider *provider,
    const QString *name,
    const QString *metadata,
    int size,
    bool variableSize) {
  return new QCtfTracePointEvent(
      *provider,
      *name,
      *metadata,
      size,
      variableSize);
}

//  QCtfTracePointEvent::~QCtfTracePointEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCtfTracePointEventD1Ev(QCtfTracePointEvent *self) {
  delete self;
}

#endif  // QT_CONFIG(ctf)
