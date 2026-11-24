//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlCompilingProfiler::QQmlCompilingProfiler(QQmlProfiler *profiler,
//      QQmlDataBlob *blob)
extern "C" Q_DECL_EXPORT
QQmlCompilingProfiler *ritual_ZN21QQmlCompilingProfilerC1EP12QQmlProfilerP12QQmlDataBlob(
    QQmlProfiler *profiler,
    QQmlDataBlob *blob) {
  return new QQmlCompilingProfiler(profiler, blob);
}

//  QQmlCompilingProfiler::~QQmlCompilingProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlCompilingProfilerD1Ev(QQmlCompilingProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
