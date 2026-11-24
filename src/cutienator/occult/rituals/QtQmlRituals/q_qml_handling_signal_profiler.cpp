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

//  QQmlHandlingSignalProfiler::QQmlHandlingSignalProfiler(QQmlProfiler
//      *profiler, QQmlBoundSignalExpression *expression)
extern "C" Q_DECL_EXPORT
QQmlHandlingSignalProfiler *ritual_ZN26QQmlHandlingSignalProfilerC1EP12QQmlProfilerP25QQmlBoundSignalExpression(
    QQmlProfiler *profiler,
    QQmlBoundSignalExpression *expression) {
  return new QQmlHandlingSignalProfiler(profiler, expression);
}

//  QQmlHandlingSignalProfiler::~QQmlHandlingSignalProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlHandlingSignalProfilerD1Ev(
    QQmlHandlingSignalProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
