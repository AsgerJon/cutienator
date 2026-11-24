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
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  QQmlObjectCreationProfiler::QQmlObjectCreationProfiler(QQmlProfiler
//      *profiler, const QV4::CompiledData::Object *obj)
extern "C" Q_DECL_EXPORT
QQmlObjectCreationProfiler *ritual_ZN26QQmlObjectCreationProfilerC1EP12QQmlProfilerPKN3QV412CompiledData6ObjectE(
    QQmlProfiler *profiler,
    const QV4::CompiledData::Object *obj) {
  return new QQmlObjectCreationProfiler(profiler, obj);
}

//  QQmlObjectCreationProfiler::~QQmlObjectCreationProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlObjectCreationProfilerD1Ev(
    QQmlObjectCreationProfiler *self) {
  delete self;
}

//  void QQmlObjectCreationProfiler::update(QV4::ExecutableCompilationUnit
//      *ref, const QV4::CompiledData::Object *obj, const QString &typeName,
//      const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlObjectCreationProfiler6updateEPN3QV425ExecutableCompilationUnitEPKNS0_12CompiledData6ObjectERK7QStringRK4QUrl(
    QQmlObjectCreationProfiler *self,
    QV4::ExecutableCompilationUnit *ref,
    const QV4::CompiledData::Object *obj,
    const QString *typeName,
    const QUrl *url) {
  self->update(ref, obj, *typeName, *url);
}

#endif  // !(!QT_CONFIG(qml_debug))
