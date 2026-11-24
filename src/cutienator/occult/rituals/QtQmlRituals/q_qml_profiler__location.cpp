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
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  QQmlProfiler::Location::Location(const QQmlSourceLocation &location,
//      const QUrl &url)
extern "C" Q_DECL_EXPORT
QQmlProfiler::Location *ritual_ZN12QQmlProfiler8LocationC1ERK18QQmlSourceLocationRK4QUrl(
    const QQmlSourceLocation *location,
    const QUrl *url) {
  return new QQmlProfiler::Location(*location, *url);
}

//  QQmlProfiler::Location::~Location()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler8LocationD1Ev(QQmlProfiler::Location *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
