//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirdata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmldirdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmldirdata.cpp, line 35, as _ZN14QQmlQmldirData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE
inline void QQmlQmldirData::dataReceived(const SourceCodeData &data)
{
    assertTypeLoaderThread();
    QString error;
    m_content = data.readAll(&error);
    if (!error.isEmpty()) {
        setError(error);
        return;
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmldirdata.cpp, line 46, as _ZN14QQmlQmldirData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE
inline void QQmlQmldirData::initializeFromCachedUnit(const QQmlPrivate::CachedQmlUnit *)
{
    assertTypeLoaderThread();
    Q_UNIMPLEMENTED();
}

//  from ../qtdeclarative/src/qml/qml/qqmldirdata.cpp, line 14, as _ZNK14QQmlQmldirData7contentEv
inline const QString &QQmlQmldirData::content() const
{
    return m_content;
}

//  from ../qtdeclarative/src/qml/qml/qqmldirdata.cpp, line 19, as _ZNK14QQmlQmldirData14importLocationEPN14QQmlTypeLoader4BlobE
inline QV4::CompiledData::Location QQmlQmldirData::importLocation(QQmlTypeLoader::Blob *blob) const
{
    auto it = m_imports.constFind(blob);
    if (it == m_imports.constEnd())
        return QV4::CompiledData::Location();
    return it->import->location;
}
//  -----------------------------------------------------------------------

//  const QString &QQmlQmldirData::content() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlQmldirData7contentEv(const QQmlQmldirData *self) {
  return new QString(self->content());
}

//  QV4::CompiledData::Location QQmlQmldirData::importLocation(Blob *blob)
//      const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Location *ritual_ZNK14QQmlQmldirData14importLocationEPN14QQmlTypeLoader4BlobE(
    const QQmlQmldirData *self,
    QQmlTypeLoader::Blob *blob) {
  return new QV4::CompiledData::Location(self->importLocation(blob));
}

//  void QQmlQmldirData::dataReceived(const SourceCodeData &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlQmldirData12dataReceivedERKN12QQmlDataBlob14SourceCodeDataE(
    QQmlQmldirData *self,
    const QQmlDataBlob::SourceCodeData *a0) {
  self->dataReceived(*a0);
}

//  void QQmlQmldirData::initializeFromCachedUnit(const
//      QQmlPrivate::CachedQmlUnit *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlQmldirData24initializeFromCachedUnitEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlQmldirData *self,
    const QQmlPrivate::CachedQmlUnit *a0) {
  self->initializeFromCachedUnit(a0);
}
