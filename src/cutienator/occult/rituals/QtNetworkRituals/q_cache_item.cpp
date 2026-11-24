//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(networkdiskcache)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdiskcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qnetworkdiskcache.h"
#include "qnetworkdiskcache_p.h"
#include <qfile.h>
#include <qdir.h>
#include <qdatastream.h>
#include <qdatetime.h>
#include <qdirlisting.h>
#include <qurl.h>
#include <qcryptographichash.h>
#include <qdebug.h>
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

//  void QCacheItem::writeCompressedData(QFileDevice *device) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QCacheItem19writeCompressedDataEP11QFileDevice(
    const QCacheItem *self,
    QFileDevice *device) {
  self->writeCompressedData(device);
}

#endif  // QT_CONFIG(networkdiskcache)
