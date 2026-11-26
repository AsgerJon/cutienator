//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if (defined(Q_OS_WASM)) || (QT_CONFIG(http))
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include "qplatformdefs.h"
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qhttpheadershelper_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttp1configuration.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtNetwork/private/http2protocol_p.h>
#endif
#include "QtCore/qdatetime.h"
#include "QtCore/qlocale.h"
#include "QtCore/qshareddata.h"
#include "QtCore/qtimezone.h"
#include "QtCore/private/qduplicatetracker_p.h"
#include "QtCore/private/qtools_p.h"
#if QT_CONFIG(datestring)
# include <stdio.h>
#endif
#include <algorithm>
#include <QtCore/q20algorithm.h>
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/private/qhttpmultipart_p.h>
#include "QtCore/qdatetime.h" // for initializing the random number generator with QTime
#include <QtCore/qdebug.h>
#include "QtCore/qmutex.h"
#include "QtCore/qrandom.h"
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

//  from src/network/access/qnetworkrequest.cpp, line 1669, as _ZNK22QNetworkHeadersPrivate7headersEv
inline QHttpHeaders QNetworkHeadersPrivate::headers() const
{
    return httpHeaders;
}

//  from src/network/access/qhttpmultipart.cpp, line 317, as _ZNK16QHttpPartPrivate14bytesAvailableEv
inline qint64 QHttpPartPrivate::bytesAvailable() const
{
    checkHeaderCreated();
    qint64 bytesAvailable = header.size();
    if (bodyDevice) {
        bytesAvailable += bodyDevice->bytesAvailable() - readPointer;
    } else {
        bytesAvailable += body.size() - readPointer;
    }
    // the device might have closed etc., so make sure we do not return a negative value
    return qMax(bytesAvailable, (qint64) 0);
}

//  from src/network/access/qhttpmultipart.cpp, line 330, as _ZN16QHttpPartPrivate8readDataEPcx
inline qint64 QHttpPartPrivate::readData(char *data, qint64 maxSize)
{
    checkHeaderCreated();
    qint64 bytesRead = 0;
    qint64 headerDataCount = header.size();

    // read header if it has not been read yet
    if (readPointer < headerDataCount) {
        bytesRead = qMin(headerDataCount - readPointer, maxSize);
        const char *headerData = header.constData();
        memcpy(data, headerData + readPointer, bytesRead);
        readPointer += bytesRead;
    }
    // read content if there is still space
    if (bytesRead < maxSize) {
        if (bodyDevice) {
            qint64 dataBytesRead = bodyDevice->read(data + bytesRead, maxSize - bytesRead);
            if (dataBytesRead == -1)
                return -1;
            bytesRead += dataBytesRead;
            readPointer += dataBytesRead;
        } else {
            qint64 contentBytesRead = qMin(body.size() - readPointer + headerDataCount, maxSize - bytesRead);
            const char *contentData = body.constData();
            // if this method is called several times, we need to find the
            // right offset in the content ourselves:
            memcpy(data + bytesRead, contentData + readPointer - headerDataCount, contentBytesRead);
            bytesRead += contentBytesRead;
            readPointer += contentBytesRead;
        }
    }
    return bytesRead;
}

//  from src/network/access/qhttpmultipart.cpp, line 364, as _ZNK16QHttpPartPrivate4sizeEv
inline qint64 QHttpPartPrivate::size() const
{
    checkHeaderCreated();
    qint64 size = header.size();
    if (bodyDevice) {
        size += bodyDevice->size();
    } else {
        size += body.size();
    }
    return size;
}

//  from src/network/access/qhttpmultipart.cpp, line 376, as _ZN16QHttpPartPrivate5resetEv
inline bool QHttpPartPrivate::reset()
{
    bool ret = true;
    if (bodyDevice)
        if (!bodyDevice->reset())
            ret = false;
    readPointer = 0;
    return ret;
}

//  from src/network/access/qhttpmultipart.cpp, line 385, as _ZNK16QHttpPartPrivate18checkHeaderCreatedEv
inline void QHttpPartPrivate::checkHeaderCreated() const
{
    if (!headerCreated) {
        // copied from QHttpNetworkRequestPrivate::header() and adapted
        const auto h = headers();
        for (qsizetype i = 0; i < h.size(); ++i) {
            const auto name = h.nameAt(i);
            header += QByteArrayView(name.data(), name.size()) + ": " + h.valueAt(i) + "\r\n";
        }

        header += "\r\n";
        headerCreated = true;
    }
}
//  -----------------------------------------------------------------------

//  QHttpPartPrivate::QHttpPartPrivate()
extern "C" Q_DECL_EXPORT
QHttpPartPrivate *ritual_ZN16QHttpPartPrivateC1Ev() {
  return new QHttpPartPrivate();
}

//  QHttpPartPrivate::~QHttpPartPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttpPartPrivateD1Ev(QHttpPartPrivate *self) {
  delete self;
}

//  QHttpPartPrivate::QHttpPartPrivate(const QHttpPartPrivate &other)
extern "C" Q_DECL_EXPORT
QHttpPartPrivate *ritual_ZN16QHttpPartPrivateC1ERKS_(
    const QHttpPartPrivate *other) {
  return new QHttpPartPrivate(*other);
}

//  bool QHttpPartPrivate::operator==(const QHttpPartPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHttpPartPrivateeqERKS_(
    const QHttpPartPrivate *self,
    const QHttpPartPrivate *other) {
  return self->operator==(*other);
}

//  void QHttpPartPrivate::setBodyDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttpPartPrivate13setBodyDeviceEP9QIODevice(
    QHttpPartPrivate *self,
    QIODevice *device) {
  self->setBodyDevice(device);
}

//  void QHttpPartPrivate::setBody(const QByteArray &newBody)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttpPartPrivate7setBodyERK10QByteArray(
    QHttpPartPrivate *self,
    const QByteArray *newBody) {
  self->setBody(*newBody);
}

//  qint64 QHttpPartPrivate::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QHttpPartPrivate14bytesAvailableEv(
    const QHttpPartPrivate *self) {
  return self->bytesAvailable();
}

//  qint64 QHttpPartPrivate::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QHttpPartPrivate8readDataEPcx(
    QHttpPartPrivate *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  qint64 QHttpPartPrivate::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QHttpPartPrivate4sizeEv(const QHttpPartPrivate *self) {
  return self->size();
}

//  bool QHttpPartPrivate::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttpPartPrivate5resetEv(QHttpPartPrivate *self) {
  return self->reset();
}

//  void QHttpPartPrivate::checkHeaderCreated() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QHttpPartPrivate18checkHeaderCreatedEv(
    const QHttpPartPrivate *self) {
  self->checkHeaderCreated();
}

//  QHttpPartPrivate as the QNetworkHeadersPrivate it is built on
extern "C" Q_DECL_EXPORT
QNetworkHeadersPrivate *ritual_cast_QHttpPartPrivate_QNetworkHeadersPrivate(
    QHttpPartPrivate *self) {
  return static_cast<QNetworkHeadersPrivate *>(self);
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
