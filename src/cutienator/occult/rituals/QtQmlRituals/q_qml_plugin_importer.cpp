//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpluginimporter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpluginimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpluginimporter_p.h>
#include <QtQml/private/qqmlimport_p.h>
#include <QtQml/private/qqmlextensionplugin_p.h>
#include <QtQml/private/qqmltypeloader_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qpluginloader.h>
#include <QtCore/qdir.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qjsonarray.h>
#include <unordered_map>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpluginimporter.cpp, line 285, as _ZN18QQmlPluginImporter19truncateToDirectoryERK7QString
inline QString QQmlPluginImporter::truncateToDirectory(const QString &qmldirFilePath)
{
    const int slash = qmldirFilePath.lastIndexOf(u'/');
    return slash > 0 ? qmldirFilePath.left(slash) : qmldirFilePath;
}
//  -----------------------------------------------------------------------

//  QQmlPluginImporter::~QQmlPluginImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPluginImporterD1Ev(QQmlPluginImporter *self) {
  delete self;
}

//  QString QQmlPluginImporter::truncateToDirectory(const QString
//      &qmldirFilePath)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlPluginImporter19truncateToDirectoryERK7QString(
    const QString *qmldirFilePath) {
  return new QString(
      QQmlPluginImporter::truncateToDirectory(
          *qmldirFilePath));
}
