//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypeloader_p.h>
#include <QtQml/private/qqmldirdata_p.h>
#include <QtQml/private/qqmlprofiler_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmltypeloaderqmldircontent_p.h>
#include <QtQml/private/qqmltypeloaderthread_p.h>
#include <QtQml/private/qv4compiler_p.h>
#include <QtQml/private/qv4compilercontext_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtQml/qqmlabstracturlinterceptor.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlextensioninterface.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <QtCore/qdir.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qfile.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/qthread.h>
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

//  from ../qtdeclarative/src/qml/qml/qqmltypeloader.cpp, line 706, as _ZN14QQmlTypeLoader4Blob13PendingImportC1ERK14QQmlRefPointerIS0_EPKN3QV412CompiledData6ImportE6QFlagsIN11QQmlImports10ImportFlagEE
inline QQmlTypeLoader::Blob::PendingImport::PendingImport(
        const QQmlRefPointer<Blob> &blob, const QV4::CompiledData::Import *import,
        QQmlImports::ImportFlags flags)
    : uri(blob->stringAt(import->uriIndex))
    , qualifier(blob->stringAt(import->qualifierIndex))
    , type(static_cast<QV4::CompiledData::Import::ImportType>(quint32(import->type)))
    , location(import->location)
    , flags(flags)
    , version(import->version)
{
}
//  -----------------------------------------------------------------------

//  QQmlTypeLoader::Blob::PendingImport::PendingImport()
extern "C" Q_DECL_EXPORT
QQmlTypeLoader::Blob::PendingImport *ritual_ZN14QQmlTypeLoader4Blob13PendingImportC1Ev() {
  return new QQmlTypeLoader::Blob::PendingImport();
}

//  QQmlTypeLoader::Blob::PendingImport::PendingImport(const
//      QQmlRefPointer<Blob> &blob, const QV4::CompiledData::Import *import,
//      QQmlImports::ImportFlags flags)
extern "C" Q_DECL_EXPORT
QQmlTypeLoader::Blob::PendingImport *ritual_ZN14QQmlTypeLoader4Blob13PendingImportC1ERK14QQmlRefPointerIS0_EPKN3QV412CompiledData6ImportE6QFlagsIN11QQmlImports10ImportFlagEE(
    const QQmlRefPointer<QQmlTypeLoader::Blob> *blob,
    const QV4::CompiledData::Import *import,
    int flags) {
  return new QQmlTypeLoader::Blob::PendingImport(
      *blob,
      import,
      QFlags<QQmlImports::ImportFlag>::fromInt(flags));
}

//  QQmlTypeLoader::Blob::PendingImport::~PendingImport()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTypeLoader4Blob13PendingImportD1Ev(
    QQmlTypeLoader::Blob::PendingImport *self) {
  delete self;
}
