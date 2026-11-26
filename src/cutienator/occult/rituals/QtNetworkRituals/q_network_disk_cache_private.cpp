//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkdiskcache.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkdiskcache.h>
#include <QtNetwork/private/qnetworkdiskcache_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qdir.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qurl.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qtools_p.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qnetworkdiskcache.cpp, line 24, as local:qnetworkdiskcache.cpp:CACHE_POSTFIX
#define CACHE_POSTFIX ".d"_L1

//  from src/network/access/qnetworkdiskcache.cpp, line 25, as local:qnetworkdiskcache.cpp:CACHE_VERSION
#define CACHE_VERSION 9

//  from src/network/access/qnetworkdiskcache.cpp, line 28, as local:qnetworkdiskcache.cpp:MAX_COMPRESSION_SIZE
#define MAX_COMPRESSION_SIZE (1024 * 1024 * 3)

//  from src/network/access/qnetworkdiskcache.cpp, line 649, as local:qnetworkdiskcache.cpp:CacheMagic
enum
{
    CacheMagic = 0xe8,
    CurrentCacheVersion = CACHE_VERSION
};

//  from src/network/access/qnetworkdiskcache.cpp, line 337, as _ZN24QNetworkDiskCachePrivate10removeFileERK7QString
inline bool QNetworkDiskCachePrivate::removeFile(const QString &file)
{
#if defined(QNETWORKDISKCACHE_DEBUG)
    qDebug() << "QNetworkDiskCache::removFile()" << file;
#endif
    if (file.isEmpty())
        return false;
    QFileInfo info(file);
    QString fileName = info.fileName();
    if (!fileName.endsWith(CACHE_POSTFIX))
        return false;
    qint64 size = info.size();
    if (QFile::remove(file)) {
        currentCacheSize -= size;
        return true;
    }
    return false;
}

//  from src/network/access/qnetworkdiskcache.cpp, line 655, as _ZNK10QCacheItem11writeHeaderEP11QFileDevice
inline void QCacheItem::writeHeader(QFileDevice *device) const
{
    QDataStream out(device);

    out << qint32(CacheMagic);
    out << qint32(CurrentCacheVersion);
    out << static_cast<qint32>(out.version());
    out << metaData;
    bool compressed = canCompress();
    out << compressed;
}

//  from src/network/access/qnetworkdiskcache.cpp, line 667, as _ZNK10QCacheItem19writeCompressedDataEP11QFileDevice
inline void QCacheItem::writeCompressedData(QFileDevice *device) const
{
    QDataStream out(device);

    out << qCompress(data.data());
}

//  from src/network/access/qnetworkdiskcache.cpp, line 624, as _ZNK10QCacheItem11canCompressEv
inline bool QCacheItem::canCompress() const
{
    const auto h = metaData.headers();

    const auto sizeValue = h.value(QHttpHeaders::WellKnownHeader::ContentLength);
    if (sizeValue.empty())
        return false;

    qint64 size = sizeValue.toLongLong();
    if (size > MAX_COMPRESSION_SIZE)
        return false;

    const auto type = h.value(QHttpHeaders::WellKnownHeader::ContentType);
    if (!type.empty())
        return false;

    if (!type.startsWith("text/")
        && !(type.startsWith("application/")
            && (type.endsWith("javascript") || type.endsWith("ecmascript")))) {
        return false;
    }

    return true;
}

//  from src/network/access/qnetworkdiskcache.cpp, line 588, as _ZN24QNetworkDiskCachePrivate14uniqueFileNameERK4QUrl
inline QString QNetworkDiskCachePrivate::uniqueFileName(const QUrl &url)
{
    QUrl cleanUrl = url;
    cleanUrl.setPassword(QString());
    cleanUrl.setFragment(QString());

    const QByteArray hash = QCryptographicHash::hash(cleanUrl.toEncoded(), QCryptographicHash::Sha1);
    // convert sha1 to base36 form and return first 8 bytes for use as string
    const QByteArray id = QByteArray::number(*(qlonglong*)hash.data(), 36).left(8);
    // generates <one-char subdir>/<8-char filename.d>
    uint code = (uint)id.at(id.size()-1) % 16;
    QString pathFragment = QString::number(code, 16) + u'/' + QLatin1StringView(id) + CACHE_POSTFIX;

    return pathFragment;
}

//  from src/network/access/qnetworkdiskcache.cpp, line 607, as _ZNK24QNetworkDiskCachePrivate13cacheFileNameERK4QUrl
inline QString QNetworkDiskCachePrivate::cacheFileName(const QUrl &url) const
{
    if (!url.isValid())
        return QString();

    QString fullpath = dataDirectory + uniqueFileName(url);
    return  fullpath;
}

//  from src/network/access/qnetworkdiskcache.cpp, line 269, as _ZN24QNetworkDiskCachePrivate9storeItemEP10QCacheItem
inline void QNetworkDiskCachePrivate::storeItem(QCacheItem *cacheItem)
{
    Q_Q(QNetworkDiskCache);
    Q_ASSERT(cacheItem->metaData.saveToDisk());

    QString fileName = cacheFileName(cacheItem->metaData.url());
    Q_ASSERT(!fileName.isEmpty());

    if (QFile::exists(fileName)) {
        if (!removeFile(fileName)) {
            qWarning() << "QNetworkDiskCache: couldn't remove the cache file " << fileName;
            return;
        }
    }

    currentCacheSize = q->expire();
    if (!cacheItem->file) {
        cacheItem->file = new QSaveFile(fileName, &cacheItem->data);
        if (cacheItem->file->open(QFileDevice::WriteOnly)) {
            cacheItem->writeHeader(cacheItem->file);
            cacheItem->writeCompressedData(cacheItem->file);
        }
    }

    if (cacheItem->file
        && cacheItem->file->isOpen()
        && cacheItem->file->error() == QFileDevice::NoError) {
        // We have to call size() here instead of inside the if-body because
        // commit() invalidates the file-engine, and size() will create a new
        // one, pointing at an empty filename.
        qint64 size = cacheItem->file->size();
        if (cacheItem->file->commit())
            currentCacheSize += size;
        // Delete and unset the QSaveFile, it's invalid now.
        delete std::exchange(cacheItem->file, nullptr);
    }
    if (cacheItem->metaData.url() == lastItem.metaData.url())
        lastItem.reset();
}

//  from src/network/access/qnetworkdiskcache.cpp, line 245, as _ZN24QNetworkDiskCachePrivate13prepareLayoutEv
inline void QNetworkDiskCachePrivate::prepareLayout()
{
    QDir helper;
    static constexpr auto dirPermissions =
        QFileDevice::ReadOwner | QFileDevice::WriteOwner | QFileDevice::ExeOwner;

    //Create directory and subdirectories 0-F
    //Ensure the cache directory and any parents exist.
    helper.mkpath(cacheDirectory);
    // Create the data directory with owner-only permissions.
    // If it already exists, tighten its permissions
    if (!helper.mkdir(dataDirectory, dirPermissions)
        && !QFile::setPermissions(dataDirectory, dirPermissions)) {
        qWarning("QNetworkDiskCache::prepareLayout: could not create or set permissions on %ls",
                 qUtf16Printable(dataDirectory));
        return;
    }
    for (uint i = 0; i < 16 ; i++) {
        QString subdir = dataDirectory + char16_t(QtMiscUtils::toHexLower(i));
        helper.mkdir(subdir, dirPermissions);
    }
}
//  -----------------------------------------------------------------------

//  QNetworkDiskCachePrivate::QNetworkDiskCachePrivate()
extern "C" Q_DECL_EXPORT
QNetworkDiskCachePrivate *ritual_ZN24QNetworkDiskCachePrivateC1Ev() {
  return new QNetworkDiskCachePrivate();
}

//  QString QNetworkDiskCachePrivate::uniqueFileName(const QUrl &url)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QNetworkDiskCachePrivate14uniqueFileNameERK4QUrl(
    const QUrl *url) {
  return new QString(QNetworkDiskCachePrivate::uniqueFileName(*url));
}

//  QString QNetworkDiskCachePrivate::cacheFileName(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QNetworkDiskCachePrivate13cacheFileNameERK4QUrl(
    const QNetworkDiskCachePrivate *self,
    const QUrl *url) {
  return new QString(self->cacheFileName(*url));
}

//  void QNetworkDiskCachePrivate::storeItem(QCacheItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkDiskCachePrivate9storeItemEP10QCacheItem(
    QNetworkDiskCachePrivate *self,
    QCacheItem *item) {
  self->storeItem(item);
}

//  void QNetworkDiskCachePrivate::prepareLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkDiskCachePrivate13prepareLayoutEv(
    QNetworkDiskCachePrivate *self) {
  self->prepareLayout();
}

//  QNetworkDiskCache *QNetworkDiskCachePrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkDiskCache *ritual_ZN24QNetworkDiskCachePrivate6q_funcEv(
    QNetworkDiskCachePrivate *self) {
  return self->q_func();
}

//  const QNetworkDiskCache *QNetworkDiskCachePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkDiskCache *ritual_ZNK24QNetworkDiskCachePrivate6q_funcEv(
    const QNetworkDiskCachePrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(networkdiskcache)
#endif  // QT_CONFIG(networkdiskcache)
