//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlSourceLocation::QQmlSourceLocation()
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZN18QQmlSourceLocationC1Ev() {
  return new QQmlSourceLocation();
}

//  QQmlSourceLocation::QQmlSourceLocation(const QString &sourceFile, quint16
//      line, quint16 column)
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZN18QQmlSourceLocationC1ERK7QStringtt(
    const QString *sourceFile,
    quint16 line,
    quint16 column) {
  return new QQmlSourceLocation(*sourceFile, line, column);
}

//  QQmlSourceLocation::~QQmlSourceLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSourceLocationD1Ev(QQmlSourceLocation *self) {
  delete self;
}
