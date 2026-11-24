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

//  QQmlProfilerHelper::QQmlProfilerHelper(QQmlProfiler *profiler)
extern "C" Q_DECL_EXPORT
QQmlProfilerHelper *ritual_ZN18QQmlProfilerHelperC1EP12QQmlProfiler(
    QQmlProfiler *profiler) {
  return new QQmlProfilerHelper(profiler);
}

//  QQmlProfilerHelper::~QQmlProfilerHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlProfilerHelperD1Ev(QQmlProfilerHelper *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
