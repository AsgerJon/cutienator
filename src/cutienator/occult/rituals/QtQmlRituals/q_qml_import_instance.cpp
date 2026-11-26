//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlimport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#include <QtCore/QTypeRevision>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlimport_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qdir.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qpluginloader.h>
#include <QtCore/qloggingcategory.h>
#include <QtQml/qqmlextensioninterface.h>
#include <QtQml/qqmlextensionplugin.h>
#include <QtQml/private/qqmlextensionplugin_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmltypenamecache_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmltypemodule_p.h>
#include <QtQml/private/qqmltypeloaderqmldircontent_p.h>
#include <QtQml/private/qqmlpluginimporter_p.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtQml/private/qqmlimportresolver_p.h>
#include <algorithm>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/qml/qqmlimport.cpp, line 506, as _ZN18QQmlImportInstance19getVersionedScriptsERK5QListIN13QQmlDirParser6ScriptEE13QTypeRevision
inline QQmlDirScripts QQmlImportInstance::getVersionedScripts(const QQmlDirScripts &qmldirscripts,
                                                       QTypeRevision version)
{
    QMap<QString, QQmlDirParser::Script> versioned;

    for (QList<QQmlDirParser::Script>::const_iterator sit = qmldirscripts.constBegin();
         sit != qmldirscripts.constEnd(); ++sit) {
        // Only include scripts that match our requested version
        if ((!version.hasMajorVersion() || (sit->version.majorVersion() == version.majorVersion()))
                && (!version.hasMinorVersion()
                    || (sit->version.minorVersion() <= version.minorVersion()))) {
            // Load the highest version that matches
            const auto vit = versioned.constFind(sit->nameSpace);
            if (vit == versioned.cend()
                    || (vit->version.minorVersion() < sit->version.minorVersion())) {
                versioned.insert(sit->nameSpace, *sit);
            }
        }
    }

    return versioned.values();
}
//  -----------------------------------------------------------------------

//  QQmlDirScripts QQmlImportInstance::getVersionedScripts(const
//      QQmlDirScripts &qmldirscripts, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlDirScripts *ritual_ZN18QQmlImportInstance19getVersionedScriptsERK5QListIN13QQmlDirParser6ScriptEE13QTypeRevision(
    const QQmlDirScripts *qmldirscripts,
    const QTypeRevision *version) {
  return new QQmlDirScripts(
      QQmlImportInstance::getVersionedScripts(
          *qmldirscripts,
          *version));
}

//  QQmlImportInstance::~QQmlImportInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlImportInstanceD1Ev(QQmlImportInstance *self) {
  delete self;
}

//  a QQmlDirScripts a ritual of QQmlImportInstance gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlImportInstance__QQmlDirScripts(QQmlDirScripts *self) {
  delete self;
}
