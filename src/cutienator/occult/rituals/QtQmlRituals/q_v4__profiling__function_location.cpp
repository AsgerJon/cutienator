//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4profiling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QV4::Profiling::FunctionLocation::FunctionLocation(const QString &name,
//      const QString &file, int line, int column)
extern "C" Q_DECL_EXPORT
QV4::Profiling::FunctionLocation *ritual_ZN3QV49Profiling16FunctionLocationC1ERK7QStringS4_ii(
    const QString *name,
    const QString *file,
    int line,
    int column) {
  return new QV4::Profiling::FunctionLocation(*name, *file, line, column);
}

//  bool QV4::Profiling::FunctionLocation::isValid()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV49Profiling16FunctionLocation7isValidEv(
    QV4::Profiling::FunctionLocation *self) {
  return self->isValid();
}

//  QV4::Profiling::FunctionLocation::~FunctionLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Profiling16FunctionLocationD1Ev(
    QV4::Profiling::FunctionLocation *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(qml_debug))
