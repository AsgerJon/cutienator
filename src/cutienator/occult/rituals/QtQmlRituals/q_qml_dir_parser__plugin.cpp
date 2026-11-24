//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlDirParser::Plugin::Plugin()
extern "C" Q_DECL_EXPORT
QQmlDirParser::Plugin *ritual_ZN13QQmlDirParser6PluginC1Ev() {
  return new QQmlDirParser::Plugin();
}

//  QQmlDirParser::Plugin::Plugin(const QString &name, const QString &path,
//      bool optional)
extern "C" Q_DECL_EXPORT
QQmlDirParser::Plugin *ritual_ZN13QQmlDirParser6PluginC1ERK7QStringS3_b(
    const QString *name,
    const QString *path,
    bool optional) {
  return new QQmlDirParser::Plugin(*name, *path, optional);
}

//  QQmlDirParser::Plugin::~Plugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser6PluginD1Ev(QQmlDirParser::Plugin *self) {
  delete self;
}
