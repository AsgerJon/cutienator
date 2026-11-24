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

//  QQmlObjectCompletionProfiler::QQmlObjectCompletionProfiler(QQmlVmeProfile
//      r *parent)
extern "C" Q_DECL_EXPORT
QQmlObjectCompletionProfiler *ritual_ZN28QQmlObjectCompletionProfilerC1EP15QQmlVmeProfiler(
    QQmlVmeProfiler *parent) {
  return new QQmlObjectCompletionProfiler(parent);
}

//  QQmlObjectCompletionProfiler::~QQmlObjectCompletionProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQmlObjectCompletionProfilerD1Ev(
    QQmlObjectCompletionProfiler *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
