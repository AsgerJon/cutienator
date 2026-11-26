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
#include <QtCore/qmetaobject.h>
#include <cstring>
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

//  from src/network/access/qhttpmultipart.cpp, line 417, as _ZN22QHttpMultiPartIODeviceD2Ev
inline QHttpMultiPartIODevice::~QHttpMultiPartIODevice()
    = default;

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
//  -----------------------------------------------------------------------

//  A QHttpMultiPartIODevice that Python can take functions over in. Every QHttpMultiPartIODevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef bool (*CuteQHttpMultiPartIODeviceCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpMultiPartIODeviceCall1)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpMultiPartIODeviceCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpMultiPartIODeviceCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpMultiPartIODeviceCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQHttpMultiPartIODeviceCall5)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQHttpMultiPartIODeviceCall6)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpMultiPartIODeviceCall7)(const void *, char *, qint64, int *);
#endif  // QT_CONFIG(http)
typedef bool (*CuteQHttpMultiPartIODeviceCall8)(const void *, int, int *);
typedef qint64 (*CuteQHttpMultiPartIODeviceCall9)(const void *, int *);
typedef bool (*CuteQHttpMultiPartIODeviceCall10)(const void *, qint64, int *);
typedef bool (*CuteQHttpMultiPartIODeviceCall11)(const void *, int *);
typedef bool (*CuteQHttpMultiPartIODeviceCall12)(const void *, int, int *);
typedef bool (*CuteQHttpMultiPartIODeviceCall13)(const void *, int, int *);
typedef qint64 (*CuteQHttpMultiPartIODeviceCall14)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQHttpMultiPartIODeviceCall15)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpMultiPartIODeviceCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpMultiPartIODeviceCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartIODeviceCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartIODeviceCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartIODeviceCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartIODeviceCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartIODeviceCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpMultiPartIODevice : public QHttpMultiPartIODevice {
public:
  using QHttpMultiPartIODevice::QHttpMultiPartIODevice;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(http)
  //  bool QHttpMultiPartIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall0 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::atEnd();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpMultiPartIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall1 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::bytesAvailable();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpMultiPartIODevice::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall2 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QHttpMultiPartIODevice::close();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpMultiPartIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall3 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::bytesToWrite();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpMultiPartIODevice::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall4 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::size();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QHttpMultiPartIODevice::isSequential() const
  bool isSequential() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall5 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::isSequential();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QHttpMultiPartIODevice::reset()
  bool reset() override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall6 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::reset();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpMultiPartIODevice::readData(char *data, qint64 maxSize)
  qint64 readData(char *data, qint64 maxSize) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall7 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall7>(taken[7]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QHttpMultiPartIODevice::readData(data, maxSize);
  }
#endif  // QT_CONFIG(http)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall8 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall8>(taken[8]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall9 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall10 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall10>(taken[10]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall11 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall12 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall13 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall14 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall14>(taken[14]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall15 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall15>(taken[15]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall16 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall17 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall18 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall19 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall20 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall21 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQHttpMultiPartIODeviceCall22 call = reinterpret_cast<CuteQHttpMultiPartIODeviceCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QHttpMultiPartIODevice::QHttpMultiPartIODevice(QHttpMultiPartPrivate
//      *parentMultiPart)
extern "C" Q_DECL_EXPORT
QHttpMultiPartIODevice *ritual_ZN22QHttpMultiPartIODeviceC1EP21QHttpMultiPartPrivate(
    QHttpMultiPartPrivate *parentMultiPart) {
  return new CuteQHttpMultiPartIODevice(parentMultiPart);
}

//  QHttpMultiPartIODevice::~QHttpMultiPartIODevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpMultiPartIODeviceD1Ev(QHttpMultiPartIODevice *self) {
  delete self;
}

//  bool QHttpMultiPartIODevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHttpMultiPartIODevice5atEndEv(
    const QHttpMultiPartIODevice *self) {
  return self->atEnd();
}

//  qint64 QHttpMultiPartIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QHttpMultiPartIODevice14bytesAvailableEv(
    const QHttpMultiPartIODevice *self) {
  return self->bytesAvailable();
}

//  void QHttpMultiPartIODevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpMultiPartIODevice5closeEv(
    QHttpMultiPartIODevice *self) {
  self->close();
}

//  qint64 QHttpMultiPartIODevice::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QHttpMultiPartIODevice12bytesToWriteEv(
    const QHttpMultiPartIODevice *self) {
  return self->bytesToWrite();
}

//  qint64 QHttpMultiPartIODevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QHttpMultiPartIODevice4sizeEv(
    const QHttpMultiPartIODevice *self) {
  return self->size();
}

//  bool QHttpMultiPartIODevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHttpMultiPartIODevice12isSequentialEv(
    const QHttpMultiPartIODevice *self) {
  return self->isSequential();
}

//  bool QHttpMultiPartIODevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QHttpMultiPartIODevice5resetEv(
    QHttpMultiPartIODevice *self) {
  return self->reset();
}

//  qint64 QHttpMultiPartIODevice::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN22QHttpMultiPartIODevice8readDataEPcx(
    QHttpMultiPartIODevice *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  qint64 QHttpMultiPartIODevice::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN22QHttpMultiPartIODevice9writeDataEPKcx(
    QHttpMultiPartIODevice *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  a Python function taken by a CuteQHttpMultiPartIODevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpMultiPartIODevice(
    QHttpMultiPartIODevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpMultiPartIODevice *>(self)->take(key, call);
}

//  bool QHttpMultiPartIODevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QHttpMultiPartIODevice5atEndEv(
    const QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::atEnd();
}

//  qint64 QHttpMultiPartIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK22QHttpMultiPartIODevice14bytesAvailableEv(
    const QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::bytesAvailable();
}

//  void QHttpMultiPartIODevice::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QHttpMultiPartIODevice5closeEv(
    QHttpMultiPartIODevice *self) {
  self->QHttpMultiPartIODevice::close();
}

//  qint64 QHttpMultiPartIODevice::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK22QHttpMultiPartIODevice12bytesToWriteEv(
    const QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::bytesToWrite();
}

//  qint64 QHttpMultiPartIODevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK22QHttpMultiPartIODevice4sizeEv(
    const QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::size();
}

//  bool QHttpMultiPartIODevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QHttpMultiPartIODevice12isSequentialEv(
    const QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::isSequential();
}

//  bool QHttpMultiPartIODevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QHttpMultiPartIODevice5resetEv(
    QHttpMultiPartIODevice *self) {
  return self->QHttpMultiPartIODevice::reset();
}

//  qint64 QHttpMultiPartIODevice::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN22QHttpMultiPartIODevice8readDataEPcx(
    QHttpMultiPartIODevice *self,
    char *data,
    qint64 maxSize) {
  return self->QHttpMultiPartIODevice::readData(data, maxSize);
}

#endif  // QT_CONFIG(http)
#endif  // (defined(Q_OS_WASM)) || (QT_CONFIG(http))
