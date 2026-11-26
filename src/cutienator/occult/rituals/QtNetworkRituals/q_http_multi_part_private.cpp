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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/private/qhttpmultipart_p.h>
#include "QtCore/qdatetime.h" // for initializing the random number generator with QTime
#include <QtCore/qdebug.h>
#include "QtCore/qmutex.h"
#include "QtCore/qrandom.h"
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttpmultipart.cpp, line 412, as _ZN21QHttpMultiPartPrivateD1Ev
inline QHttpMultiPartPrivate::~QHttpMultiPartPrivate()
{
    delete device;
}

//  from src/network/access/qhttpmultipart.cpp, line 417, as _ZN22QHttpMultiPartIODeviceD1Ev
inline QHttpMultiPartIODevice::~QHttpMultiPartIODevice()
    = default;

//  from src/network/access/qhttpmultipart.cpp, line 420, as _ZNK22QHttpMultiPartIODevice4sizeEv
inline qint64 QHttpMultiPartIODevice::size() const
{
    // if not done yet, we calculate the size and the offsets of each part,
    // including boundary (needed later in readData)
    if (deviceSize == -1) {
        qint64 currentSize = 0;
        qint64 boundaryCount = multiPart->boundary.size();
        for (int a = 0; a < multiPart->parts.size(); a++) {
            partOffsets.append(currentSize);
            // 4 additional bytes for the "--" before and the "\r\n" after the boundary,
            // and 2 bytes for the "\r\n" after the content
            currentSize += boundaryCount + 4 + multiPart->parts.at(a).d->size() + 2;
        }
        currentSize += boundaryCount + 6; // size for ending boundary, 2 beginning and ending dashes and "\r\n"
        deviceSize = currentSize;
    }
    return deviceSize;
}

//  from src/network/access/qhttpmultipart.cpp, line 439, as _ZNK22QHttpMultiPartIODevice12isSequentialEv
inline bool QHttpMultiPartIODevice::isSequential() const
{
    for (int a = 0; a < multiPart->parts.size(); a++) {
        QIODevice *device = multiPart->parts.at(a).d->bodyDevice;
        // we are sequential if any of the bodyDevices of our parts are sequential;
        // when reading from a byte array, we are not sequential
        if (device && device->isSequential())
            return true;
    }
    return false;
}

//  from src/network/access/qhttpmultipart.cpp, line 451, as _ZN22QHttpMultiPartIODevice5resetEv
inline bool QHttpMultiPartIODevice::reset()
{
    // Reset QIODevice's data
    QIODevice::reset();
    for (int a = 0; a < multiPart->parts.size(); a++)
        if (!multiPart->parts[a].d->reset())
            return false;
    readPointer = 0;
    return true;
}

//  from src/network/access/qhttpmultipart.cpp, line 461, as _ZN22QHttpMultiPartIODevice8readDataEPcx
inline qint64 QHttpMultiPartIODevice::readData(char *data, qint64 maxSize)
{
    qint64 bytesRead = 0, index = 0;

    // skip the parts we have already read
    while (index < multiPart->parts.size() &&
           readPointer >= partOffsets.at(index) + multiPart->parts.at(index).d->size()
           + multiPart->boundary.size() + 6) // 6 == 2 boundary dashes, \r\n after boundary, \r\n after multipart
        index++;

    // read the data
    while (bytesRead < maxSize && index < multiPart->parts.size()) {

        // check whether we need to read the boundary of the current part
        QByteArray boundaryData = "--" + multiPart->boundary + "\r\n";
        qint64 boundaryCount = boundaryData.size();
        qint64 partIndex = readPointer - partOffsets.at(index);
        if (partIndex < boundaryCount) {
            qint64 boundaryBytesRead = qMin(boundaryCount - partIndex, maxSize - bytesRead);
            memcpy(data + bytesRead, boundaryData.constData() + partIndex, boundaryBytesRead);
            bytesRead += boundaryBytesRead;
            readPointer += boundaryBytesRead;
            partIndex += boundaryBytesRead;
        }

        // check whether we need to read the data of the current part
        if (bytesRead < maxSize && partIndex >= boundaryCount && partIndex < boundaryCount + multiPart->parts.at(index).d->size()) {
            qint64 dataBytesRead = multiPart->parts[index].d->readData(data + bytesRead, maxSize - bytesRead);
            if (dataBytesRead == -1)
                return -1;
            bytesRead += dataBytesRead;
            readPointer += dataBytesRead;
            partIndex += dataBytesRead;
        }

        // check whether we need to read the ending CRLF of the current part
        if (bytesRead < maxSize && partIndex >= boundaryCount + multiPart->parts.at(index).d->size()) {
            if (bytesRead == maxSize - 1)
                return bytesRead;
            memcpy(data + bytesRead, "\r\n", 2);
            bytesRead += 2;
            readPointer += 2;
            index++;
        }
    }
    // check whether we need to return the final boundary
    if (bytesRead < maxSize && index == multiPart->parts.size()) {
        QByteArray finalBoundary = "--" + multiPart->boundary + "--\r\n";
        qint64 boundaryIndex = readPointer + finalBoundary.size() - size();
        qint64 lastBoundaryBytesRead = qMin(finalBoundary.size() - boundaryIndex, maxSize - bytesRead);
        memcpy(data + bytesRead, finalBoundary.constData() + boundaryIndex, lastBoundaryBytesRead);
        bytesRead += lastBoundaryBytesRead;
        readPointer += lastBoundaryBytesRead;
    }
    return bytesRead;
}

//  from src/network/access/qhttpmultipart.cpp, line 518, as _ZN22QHttpMultiPartIODevice9writeDataEPKcx
inline qint64 QHttpMultiPartIODevice::writeData(const char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);
    return -1;
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

//  from src/network/access/qnetworkrequest.cpp, line 1669, as _ZNK22QNetworkHeadersPrivate7headersEv
inline QHttpHeaders QNetworkHeadersPrivate::headers() const
{
    return httpHeaders;
}

//  from src/network/access/qhttpmultipart.cpp, line 400, as _ZN21QHttpMultiPartPrivateC1Ev
inline QHttpMultiPartPrivate::QHttpMultiPartPrivate() : contentType(QHttpMultiPart::MixedType), device(new QHttpMultiPartIODevice(this))
{
    // 24 random bytes, becomes 32 characters when encoded to Base64
    quint32 random[6];
    QRandomGenerator::global()->fillRange(random);
    boundary = "boundary_.oOo._"
               + QByteArray::fromRawData(reinterpret_cast<char *>(random), sizeof(random)).toBase64();

    // boundary must not be longer than 70 characters, see RFC 2046, section 5.1.1
    Q_ASSERT(boundary.size() <= 70);
}
//  -----------------------------------------------------------------------

//  QHttpMultiPartPrivate::QHttpMultiPartPrivate()
extern "C" Q_DECL_EXPORT
QHttpMultiPartPrivate *ritual_ZN21QHttpMultiPartPrivateC1Ev() {
  return new QHttpMultiPartPrivate();
}

//  QHttpMultiPartPrivate::~QHttpMultiPartPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttpMultiPartPrivateD1Ev(QHttpMultiPartPrivate *self) {
  delete self;
}

//  QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(QHttpMultiPart
//      *message)
extern "C" Q_DECL_EXPORT
QHttpMultiPartPrivate *ritual_ZN21QHttpMultiPartPrivate3getEP14QHttpMultiPart(
    QHttpMultiPart *message) {
  return QHttpMultiPartPrivate::get(message);
}

//  const QHttpMultiPartPrivate *QHttpMultiPartPrivate::get(const
//      QHttpMultiPart *message)
extern "C" Q_DECL_EXPORT
const QHttpMultiPartPrivate *ritual_ZN21QHttpMultiPartPrivate3getEPK14QHttpMultiPart(
    const QHttpMultiPart *message) {
  return QHttpMultiPartPrivate::get(message);
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
