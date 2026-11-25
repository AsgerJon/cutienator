//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdecompresshelper_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the private 'setEncoding' taking a
//  'ContentEncoding' is left out, with the code taken for it, and so
//  are the lines pulling in 'zlib.h', 'brotli/decode.h' and 'zstd.h':
//  it makes the decoders of zlib, Brotli and zstd, libraries outside
//  Qt. The 'setEncoding' taking a 'QByteArray', which Qt offers,
//  stays. Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdecompresshelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qbytedatabuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qcoreapplication.h>
#include <limits>
#include <array>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qdecompresshelper.cpp, line 386, as _ZN17QDecompressHelper12readInternalEPcx
inline qsizetype QDecompressHelper::readInternal(char *data, qsizetype maxSize)
{
    Q_ASSERT(isValid());

    if (maxSize <= 0)
        return 0;

    if (!hasDataInternal())
        return 0;

    qsizetype bytesRead = -1;
    switch (contentEncoding) {
    case None:
        Q_UNREACHABLE();
        break;
    case Deflate:
    case GZip:
        bytesRead = readZLib(data, maxSize);
        break;
    case Brotli:
        bytesRead = readBrotli(data, maxSize);
        break;
    case Zstandard:
        bytesRead = readZstandard(data, maxSize);
        break;
    }
    if (bytesRead == -1)
        clear();

    totalUncompressedBytes += bytesRead;
    if (isPotentialArchiveBomb()) {
        errorStr = QCoreApplication::translate(
                "QHttp",
                "The decompressed output exceeds the limits specified by "
                "QNetworkRequest::decompressedSafetyCheckThreshold()");
        return -1;
    }

    return bytesRead;
}

//  from src/network/access/qdecompresshelper.cpp, line 440, as _ZNK17QDecompressHelper22isPotentialArchiveBombEv
inline bool QDecompressHelper::isPotentialArchiveBomb() const
{
    if (totalCompressedBytes == 0)
        return false;

    if (totalUncompressedBytes <= archiveBombCheckThreshold)
        return false;

    // Some protection against malicious or corrupted compressed files that expand far more than
    // is reasonable.
    double ratio = double(totalUncompressedBytes) / double(totalCompressedBytes);
    switch (contentEncoding) {
    case None:
        Q_UNREACHABLE();
        break;
    case Deflate:
    case GZip:
        // This value is mentioned in docs for
        // QNetworkRequest::setMinimumArchiveBombSize, keep synchronized
        if (ratio > 40) {
            return true;
        }
        break;
    case Brotli:
    case Zstandard:
        // This value is mentioned in docs for
        // QNetworkRequest::setMinimumArchiveBombSize, keep synchronized
        if (ratio > 100) {
            return true;
        }
        break;
    }
    return false;
}

//  from src/network/access/qdecompresshelper.cpp, line 493, as _ZNK17QDecompressHelper15hasDataInternalEv
inline bool QDecompressHelper::hasDataInternal() const
{
    return encodedBytesAvailable() || decoderHasData;
}

//  from src/network/access/qdecompresshelper.cpp, line 498, as _ZNK17QDecompressHelper21encodedBytesAvailableEv
inline qint64 QDecompressHelper::encodedBytesAvailable() const
{
    return compressedDataBuffer.byteAmount();
}
//  -----------------------------------------------------------------------

//  QDecompressHelper::QDecompressHelper()
extern "C" Q_DECL_EXPORT
QDecompressHelper *ritual_ZN17QDecompressHelperC1Ev() {
  return new QDecompressHelper();
}

//  QDecompressHelper::~QDecompressHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelperD1Ev(QDecompressHelper *self) {
  delete self;
}

//  bool QDecompressHelper::setEncoding(QByteArrayView contentEncoding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDecompressHelper11setEncodingE14QByteArrayView(
    QDecompressHelper *self,
    const QByteArrayView *contentEncoding) {
  return self->setEncoding(*contentEncoding);
}

//  bool QDecompressHelper::isCountingBytes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDecompressHelper15isCountingBytesEv(
    const QDecompressHelper *self) {
  return self->isCountingBytes();
}

//  void QDecompressHelper::setCountingBytesEnabled(bool shouldCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelper23setCountingBytesEnabledEb(
    QDecompressHelper *self,
    bool shouldCount) {
  self->setCountingBytesEnabled(shouldCount);
}

//  qint64 QDecompressHelper::uncompressedSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QDecompressHelper16uncompressedSizeEv(
    const QDecompressHelper *self) {
  return self->uncompressedSize();
}

//  bool QDecompressHelper::hasData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDecompressHelper7hasDataEv(const QDecompressHelper *self) {
  return self->hasData();
}

//  void QDecompressHelper::feed(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelper4feedERK10QByteArray(
    QDecompressHelper *self,
    const QByteArray *data) {
  self->feed(*data);
}

//  void QDecompressHelper::feed(const QByteDataBuffer &buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelper4feedERK15QByteDataBuffer(
    QDecompressHelper *self,
    const QByteDataBuffer *buffer) {
  self->feed(*buffer);
}

//  bool QDecompressHelper::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDecompressHelper7isValidEv(const QDecompressHelper *self) {
  return self->isValid();
}

//  void QDecompressHelper::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelper5clearEv(QDecompressHelper *self) {
  self->clear();
}

//  void QDecompressHelper::setDecompressedSafetyCheckThreshold(qint64
//      threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDecompressHelper35setDecompressedSafetyCheckThresholdEx(
    QDecompressHelper *self,
    qint64 threshold) {
  self->setDecompressedSafetyCheckThreshold(threshold);
}

//  bool QDecompressHelper::isSupportedEncoding(QByteArrayView encoding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDecompressHelper19isSupportedEncodingE14QByteArrayView(
    const QByteArrayView *encoding) {
  return QDecompressHelper::isSupportedEncoding(*encoding);
}

//  QByteArrayList QDecompressHelper::acceptedEncoding()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN17QDecompressHelper16acceptedEncodingEv() {
  return new QList<QByteArray>(QDecompressHelper::acceptedEncoding());
}

//  QString QDecompressHelper::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDecompressHelper11errorStringEv(
    const QDecompressHelper *self) {
  return new QString(self->errorString());
}

//  bool QDecompressHelper::isPotentialArchiveBomb() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDecompressHelper22isPotentialArchiveBombEv(
    const QDecompressHelper *self) {
  return self->isPotentialArchiveBomb();
}

//  bool QDecompressHelper::hasDataInternal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDecompressHelper15hasDataInternalEv(
    const QDecompressHelper *self) {
  return self->hasDataInternal();
}

//  qint64 QDecompressHelper::encodedBytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QDecompressHelper21encodedBytesAvailableEv(
    const QDecompressHelper *self) {
  return self->encodedBytesAvailable();
}

#endif  // QT_CONFIG(http)
