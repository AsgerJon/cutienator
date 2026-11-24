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

//  from src/network/access/qnetworkdiskcache.cpp, line 667, as _ZNK10QCacheItem19writeCompressedDataEP11QFileDevice
inline void QCacheItem::writeCompressedData(QFileDevice *device) const
{
    QDataStream out(device);

    out << qCompress(data.data());
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
