//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>

//  QQmlDirParser::Component::Component()
extern "C" Q_DECL_EXPORT
QQmlDirParser::Component *ritual_ZN13QQmlDirParser9ComponentC1Ev() {
  return new QQmlDirParser::Component();
}

//  QQmlDirParser::Component::Component(const QString &typeName, const
//      QString &fileName, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlDirParser::Component *ritual_ZN13QQmlDirParser9ComponentC1ERK7QStringS3_13QTypeRevision(
    const QString *typeName,
    const QString *fileName,
    const QTypeRevision *version) {
  return new QQmlDirParser::Component(*typeName, *fileName, *version);
}

//  QQmlDirParser::Component::~Component()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser9ComponentD1Ev(QQmlDirParser::Component *self) {
  delete self;
}
