//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlmetatypedata_p.h>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtQml/private/qqmltypemodule_p.h>
#include <QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 45, as _ZN16QQmlMetaTypeData12VersionedUriC1ERKSt10unique_ptrI14QQmlTypeModuleSt14default_deleteIS2_EE
inline QQmlMetaTypeData::VersionedUri::VersionedUri(const std::unique_ptr<QQmlTypeModule> &module)
    : uri(module->module()), majorVersion(module->majorVersion())
{
}
//  -----------------------------------------------------------------------

//  QQmlMetaTypeData::VersionedUri::VersionedUri()
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData::VersionedUri *ritual_ZN16QQmlMetaTypeData12VersionedUriC1Ev() {
  return new QQmlMetaTypeData::VersionedUri();
}

//  QQmlMetaTypeData::VersionedUri::VersionedUri(const QString &uri,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData::VersionedUri *ritual_ZN16QQmlMetaTypeData12VersionedUriC1ERK7QString13QTypeRevision(
    const QString *uri,
    const QTypeRevision *version) {
  return new QQmlMetaTypeData::VersionedUri(*uri, *version);
}

//  QQmlMetaTypeData::VersionedUri::VersionedUri(const
//      std::unique_ptr<QQmlTypeModule> &module)
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData::VersionedUri *ritual_ZN16QQmlMetaTypeData12VersionedUriC1ERKSt10unique_ptrI14QQmlTypeModuleSt14default_deleteIS2_EE(
    const std::unique_ptr<QQmlTypeModule> *module) {
  return new QQmlMetaTypeData::VersionedUri(*module);
}

//  bool operator==(const VersionedUri &a, const VersionedUri &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN16QQmlMetaTypeData12VersionedUriES2_(
    const QQmlMetaTypeData::VersionedUri *a,
    const QQmlMetaTypeData::VersionedUri *b) {
  return operator==(*a, *b);
}

//  bool operator<(const QQmlMetaTypeData::VersionedUri &a, const
//      QQmlMetaTypeData::VersionedUri &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN16QQmlMetaTypeData12VersionedUriES2_(
    const QQmlMetaTypeData::VersionedUri *a,
    const QQmlMetaTypeData::VersionedUri *b) {
  return operator<(*a, *b);
}

//  QQmlMetaTypeData::VersionedUri::~VersionedUri()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData12VersionedUriD1Ev(
    QQmlMetaTypeData::VersionedUri *self) {
  delete self;
}
