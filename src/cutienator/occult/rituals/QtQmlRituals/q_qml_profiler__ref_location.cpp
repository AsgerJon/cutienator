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
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  QQmlProfiler::RefLocation::RefLocation()
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1Ev() {
  return new QQmlProfiler::RefLocation();
}

//  QQmlProfiler::RefLocation::RefLocation(QV4::Function *ref)
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1EPN3QV48FunctionE(
    QV4::Function *ref) {
  return new QQmlProfiler::RefLocation(ref);
}

//  QQmlProfiler::RefLocation::RefLocation(QV4::ExecutableCompilationUnit
//      *ref, const QUrl &url, const QV4::CompiledData::Object *obj, const
//      QString &type)
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1EPN3QV425ExecutableCompilationUnitERK4QUrlPKNS1_12CompiledData6ObjectERK7QString(
    QV4::ExecutableCompilationUnit *ref,
    const QUrl *url,
    const QV4::CompiledData::Object *obj,
    const QString *type) {
  return new QQmlProfiler::RefLocation(ref, *url, obj, *type);
}

//  QQmlProfiler::RefLocation::RefLocation(QQmlBoundSignalExpression *ref)
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1EP25QQmlBoundSignalExpression(
    QQmlBoundSignalExpression *ref) {
  return new QQmlProfiler::RefLocation(ref);
}

//  QQmlProfiler::RefLocation::RefLocation(QQmlDataBlob *ref)
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1EP12QQmlDataBlob(
    QQmlDataBlob *ref) {
  return new QQmlProfiler::RefLocation(ref);
}

//  QQmlProfiler::RefLocation::RefLocation(const RefLocation &other)
extern "C" Q_DECL_EXPORT
QQmlProfiler::RefLocation *ritual_ZN12QQmlProfiler11RefLocationC1ERKS0_(
    const QQmlProfiler::RefLocation *other) {
  return new QQmlProfiler::RefLocation(*other);
}

//  QQmlProfiler::RefLocation::~RefLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler11RefLocationD1Ev(
    QQmlProfiler::RefLocation *self) {
  delete self;
}

//  void QQmlProfiler::RefLocation::addref()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler11RefLocation6addrefEv(
    QQmlProfiler::RefLocation *self) {
  self->addref();
}

//  void QQmlProfiler::RefLocation::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler11RefLocation7releaseEv(
    QQmlProfiler::RefLocation *self) {
  self->release();
}

//  bool QQmlProfiler::RefLocation::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProfiler11RefLocation7isValidEv(
    const QQmlProfiler::RefLocation *self) {
  return self->isValid();
}

//  bool QQmlProfiler::RefLocation::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlProfiler11RefLocation6isNullEv(
    const QQmlProfiler::RefLocation *self) {
  return self->isNull();
}

#endif  // !(!QT_CONFIG(qml_debug))
