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

//  QQmlBindingProfiler::QQmlBindingProfiler(QQmlProfiler *profiler,
//      QV4::Function *function)
extern "C" Q_DECL_EXPORT
QQmlBindingProfiler *ritual_ZN19QQmlBindingProfilerC1EP12QQmlProfilerPN3QV48FunctionE(
    QQmlProfiler *profiler,
    QV4::Function *function) {
  return new QQmlBindingProfiler(profiler, function);
}

//  QQmlBindingProfiler::~QQmlBindingProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlBindingProfilerD1Ev(QQmlBindingProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
