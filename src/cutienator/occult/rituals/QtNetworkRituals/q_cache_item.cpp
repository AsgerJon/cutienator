//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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
//  -----------------------------------------------------------------------

//  QCacheItem::QCacheItem()
extern "C" Q_DECL_EXPORT
QCacheItem *ritual_ZN10QCacheItemC1Ev() {
  return new QCacheItem();
}

//  QCacheItem::~QCacheItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCacheItemD1Ev(QCacheItem *self) {
  delete self;
}

//  qint64 QCacheItem::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QCacheItem4sizeEv(const QCacheItem *self) {
  return self->size();
}

//  void QCacheItem::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCacheItem5resetEv(QCacheItem *self) {
  self->reset();
}

//  void QCacheItem::writeHeader(QFileDevice *device) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QCacheItem11writeHeaderEP11QFileDevice(
    const QCacheItem *self,
    QFileDevice *device) {
  self->writeHeader(device);
}

//  void QCacheItem::writeCompressedData(QFileDevice *device) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QCacheItem19writeCompressedDataEP11QFileDevice(
    const QCacheItem *self,
    QFileDevice *device) {
  self->writeCompressedData(device);
}

//  bool QCacheItem::canCompress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCacheItem11canCompressEv(const QCacheItem *self) {
  return self->canCompress();
}

#endif  // QT_CONFIG(networkdiskcache)
#endif  // QT_CONFIG(networkdiskcache)
