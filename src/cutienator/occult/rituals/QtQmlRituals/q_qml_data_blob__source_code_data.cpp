//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldatablob_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldatablob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmldatablob_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlprofiler_p.h>
#include <QtQml/private/qqmlsourcecoordinate_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmltypeloader_p.h>
#include <QtQml/private/qqmltypeloaderthread_p.h>
#include <QtQml/qqmlengine.h>
#include <QtCore/qcryptographichash.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmldatablob.cpp, line 607, as _ZNK12QQmlDataBlob14SourceCodeData7readAllEP7QString
inline QString QQmlDataBlob::SourceCodeData::readAll(QString *error) const
{
    error->clear();
    if (hasInlineSourceCode)
        return inlineSourceCode;

    QFile f(fileInfo.filePath());
    if (!f.open(QIODevice::ReadOnly)) {
        *error = f.errorString();
        return QString();
    }

    const qint64 fileSize = f.size();

    if (uchar *mappedData = f.map(0, fileSize)) {
        QString source = QString::fromUtf8(reinterpret_cast<const char *>(mappedData), fileSize);
        f.unmap(mappedData);
        return source;
    }

    QByteArray data(fileSize, Qt::Uninitialized);
    if (f.read(data.data(), data.size()) != data.size()) {
        *error = f.errorString();
        return QString();
    }
    return QString::fromUtf8(data);
}

//  from ../qtdeclarative/src/qml/qml/qqmldatablob.cpp, line 635, as _ZNK12QQmlDataBlob14SourceCodeData15sourceTimeStampEv
inline QDateTime QQmlDataBlob::SourceCodeData::sourceTimeStamp() const
{
    if (hasInlineSourceCode)
        return QDateTime();

    // If the file is from the resource file system we're never
    // interested in the timestamp. Either it's content-hashed anyway
    // (if we're checking against a .qmlc file), or we use the
    // application timestamp because we don't trust qrc timestamps.
    // So don't query the file system here.
    if (QQmlTypeLoader::isResource(fileInfo.path()))
        return QDateTime();

    return fileInfo.lastModified();
}

//  from ../qtdeclarative/src/qml/qml/qqmldatablob.cpp, line 651, as _ZNK12QQmlDataBlob14SourceCodeData8checksumEv
inline QByteArray QQmlDataBlob::SourceCodeData::checksum() const
{
    QCryptographicHash hash(QCryptographicHash::Md5);
    if (hasInlineSourceCode) {
        hash.addData(inlineSourceCode.toUtf8());
        return hash.result();
    }

    QFile f(fileInfo.filePath());
    if (!f.open(QIODevice::ReadOnly))
        return QByteArray();
    if (!hash.addData(&f))
        return QByteArray();
    return hash.result();
}
//  -----------------------------------------------------------------------

//  QString QQmlDataBlob::SourceCodeData::readAll(QString *error) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQmlDataBlob14SourceCodeData7readAllEP7QString(
    const QQmlDataBlob::SourceCodeData *self,
    QString *error) {
  return new QString(self->readAll(error));
}

//  QDateTime QQmlDataBlob::SourceCodeData::sourceTimeStamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK12QQmlDataBlob14SourceCodeData15sourceTimeStampEv(
    const QQmlDataBlob::SourceCodeData *self) {
  return new QDateTime(self->sourceTimeStamp());
}

//  QByteArray QQmlDataBlob::SourceCodeData::checksum() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QQmlDataBlob14SourceCodeData8checksumEv(
    const QQmlDataBlob::SourceCodeData *self) {
  return new QByteArray(self->checksum());
}

//  bool QQmlDataBlob::SourceCodeData::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob14SourceCodeData6existsEv(
    const QQmlDataBlob::SourceCodeData *self) {
  return self->exists();
}

//  bool QQmlDataBlob::SourceCodeData::isCacheable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob14SourceCodeData11isCacheableEv(
    const QQmlDataBlob::SourceCodeData *self) {
  return self->isCacheable();
}

//  bool QQmlDataBlob::SourceCodeData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQmlDataBlob14SourceCodeData7isValidEv(
    const QQmlDataBlob::SourceCodeData *self) {
  return self->isValid();
}

//  QQmlDataBlob::SourceCodeData::~SourceCodeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlDataBlob14SourceCodeDataD1Ev(
    QQmlDataBlob::SourceCodeData *self) {
  delete self;
}
