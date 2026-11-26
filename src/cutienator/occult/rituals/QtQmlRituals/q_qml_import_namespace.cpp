//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlimport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
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

//  from ../qtdeclarative/src/qml/qml/qqmlimport.cpp, line 786, as _ZNK19QQmlImportNamespace21findImportByModuleUriERK7QString13QTypeRevision
inline QQmlImportInstance *QQmlImportNamespace::findImportByModuleUri(
        const QString &moduleUri, QTypeRevision version) const
{
    const auto end = imports.cend();
    const auto it = std::find_if(imports.cbegin(), end, [&](const QQmlImportInstance *import) {
        return import->uri == moduleUri && import->version == version;
    });
    return it == end ? nullptr : *it;
}

//  from ../qtdeclarative/src/qml/qml/qqmlimport.cpp, line 796, as _ZNK19QQmlImportNamespace20findImportByLocationERK7QString13QTypeRevision
inline QQmlImportInstance *QQmlImportNamespace::findImportByLocation(
        const QString &location, QTypeRevision version) const
{
    const auto end = imports.cend();
    const auto it = std::find_if(imports.cbegin(), end, [&](const QQmlImportInstance *import) {
        return import->url == location && import->version == version;
    });
    return it == end ? nullptr : *it;
}
//  -----------------------------------------------------------------------

//  QQmlImportNamespace::QQmlImportNamespace()
extern "C" Q_DECL_EXPORT
QQmlImportNamespace *ritual_ZN19QQmlImportNamespaceC1Ev() {
  return new QQmlImportNamespace();
}

//  QQmlImportNamespace::~QQmlImportNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlImportNamespaceD1Ev(QQmlImportNamespace *self) {
  delete self;
}

//  QQmlImportInstance *QQmlImportNamespace::findImportByModuleUri(const
//      QString &moduleUri, QTypeRevision version) const
extern "C" Q_DECL_EXPORT
QQmlImportInstance *ritual_ZNK19QQmlImportNamespace21findImportByModuleUriERK7QString13QTypeRevision(
    const QQmlImportNamespace *self,
    const QString *moduleUri,
    const QTypeRevision *version) {
  return self->findImportByModuleUri(*moduleUri, *version);
}

//  QQmlImportInstance *QQmlImportNamespace::findImportByLocation(const
//      QString &location, QTypeRevision version) const
extern "C" Q_DECL_EXPORT
QQmlImportInstance *ritual_ZNK19QQmlImportNamespace20findImportByLocationERK7QString13QTypeRevision(
    const QQmlImportNamespace *self,
    const QString *location,
    const QTypeRevision *version) {
  return self->findImportByLocation(*location, *version);
}

//  bool QQmlImportNamespace::needsSorting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlImportNamespace12needsSortingEv(
    const QQmlImportNamespace *self) {
  return self->needsSorting();
}

//  void QQmlImportNamespace::setNeedsSorting(bool needsSorting)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlImportNamespace15setNeedsSortingEb(
    QQmlImportNamespace *self,
    bool needsSorting) {
  self->setNeedsSorting(needsSorting);
}
