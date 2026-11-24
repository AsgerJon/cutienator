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

//  QQmlDirParser::Script::Script()
extern "C" Q_DECL_EXPORT
QQmlDirParser::Script *ritual_ZN13QQmlDirParser6ScriptC1Ev() {
  return new QQmlDirParser::Script();
}

//  QQmlDirParser::Script::Script(const QString &nameSpace, const QString
//      &fileName, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlDirParser::Script *ritual_ZN13QQmlDirParser6ScriptC1ERK7QStringS3_13QTypeRevision(
    const QString *nameSpace,
    const QString *fileName,
    const QTypeRevision *version) {
  return new QQmlDirParser::Script(*nameSpace, *fileName, *version);
}

//  QQmlDirParser::Script::~Script()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser6ScriptD1Ev(QQmlDirParser::Script *self) {
  delete self;
}
