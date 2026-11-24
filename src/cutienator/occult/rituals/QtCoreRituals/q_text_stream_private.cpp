//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtextstream_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qtextstream.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtextstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qchar.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qtextstream.h"
#include "private/qtextstream_p.h"
#include "qbuffer.h"
#include "qfile.h"
#include "qnumeric.h"
#include "qvarlengtharray.h"
#include <private/qdebug_p.h>
#include <private/qnumeric_p.h>
#include <private/qtools_p.h>
#include <locale.h>
#include "private/qlocale_p.h"
#include "private/qstringconverter_p.h"
#include <stdlib.h>
#include <limits.h>
#include <new>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/serialization/qtextstream.cpp, line 281, as _ZN18QTextStreamPrivate6Params5resetEv
inline void QTextStreamPrivate::Params::reset()
{
    realNumberPrecision = 6;
    integerBase = 0;
    fieldWidth = 0;
    padChar = u' ';
    fieldAlignment = QTextStream::AlignRight;
    realNumberNotation = QTextStream::SmartNotation;
    numberFlags = { };
}

//  from src/corelib/serialization/qtextstream.cpp, line 561, as _ZN18QTextStreamPrivate4scanEPPK5QCharPxxNS_14TokenDelimiterE
inline bool QTextStreamPrivate::scan(const QChar **ptr, qsizetype *length, qsizetype maxlen,
                              TokenDelimiter delimiter)
{
    qsizetype totalSize = 0;
    qsizetype delimSize = 0;
    bool consumeDelimiter = false;
    bool foundToken = false;
    qsizetype startOffset = device ? readBufferOffset : stringOffset;
    QChar lastChar;

    do {
        qsizetype endOffset;
        const QChar *chPtr;
        if (device) {
            chPtr = readBuffer.constData();
            endOffset = readBuffer.size();
        } else {
            chPtr = string->constData();
            endOffset = string->size();
        }
        chPtr += startOffset;

        for (; !foundToken && startOffset < endOffset && (!maxlen || totalSize < maxlen); ++startOffset) {
            const QChar ch = *chPtr++;
            ++totalSize;

            switch (delimiter) {
            case Space:
                if (ch.isSpace()) {
                    foundToken = true;
                    delimSize = 1;
                }
                break;
            case NotSpace:
                if (!ch.isSpace()) {
                    foundToken = true;
                    delimSize = 1;
                }
                break;
            case EndOfLine:
                if (ch == u'\n') {
                    foundToken = true;
                    delimSize = (lastChar == u'\r') ? 2 : 1;
                    consumeDelimiter = true;
                }
                lastChar = ch;
                break;
            }
        }
    } while (!foundToken
             && (!maxlen || totalSize < maxlen)
             && device && fillReadBuffer());

    if (totalSize == 0) {
#if defined (QTEXTSTREAM_DEBUG)
        qDebug("QTextStreamPrivate::scan() reached the end of input.");
#endif
        return false;
    }

    // if we find a '\r' at the end of the data when reading lines,
    // don't make it part of the line.
    if (delimiter == EndOfLine && totalSize > 0 && !foundToken) {
        if (((string && stringOffset + totalSize == string->size()) || (device && device->atEnd()))
            && lastChar == u'\r') {
            consumeDelimiter = true;
            ++delimSize;
        }
    }

    // set the read offset and length of the token
    if (length)
        *length = totalSize - delimSize;
    if (ptr)
        *ptr = readPtr();

    // update last token size. the callee will call consumeLastToken() when
    // done.
    lastTokenSize = totalSize;
    if (!consumeDelimiter)
        lastTokenSize -= delimSize;

#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::scan(%p, %p, %d, %x) token length = %d, delimiter = %d",
           ptr, length, int(maxlen), uint(delimiter), int(totalSize - delimSize), int(delimSize));
#endif
    return true;
}

//  from src/corelib/serialization/qtextstream.cpp, line 259, as _ZN18QTextStreamPrivateC1EP11QTextStream
inline QTextStreamPrivate::QTextStreamPrivate(QTextStream *q_ptr)
    : readConverterSavedStateOffset(0),
      locale(QLocale::c())
{
    this->q_ptr = q_ptr;
    reset();
}

//  from src/corelib/serialization/qtextstream.cpp, line 270, as _ZN18QTextStreamPrivateD1Ev
inline QTextStreamPrivate::~QTextStreamPrivate()
{
    disconnectFromDevice();
    if (deleteDevice) {
#ifndef QT_NO_QOBJECT
        device->blockSignals(true);
#endif
        delete device;
    }
}

//  from src/corelib/serialization/qtextstream.cpp, line 295, as _ZN18QTextStreamPrivate5resetEv
inline void QTextStreamPrivate::reset()
{
    params.reset();

    device = nullptr;
    deleteDevice = false;
    string = nullptr;
    stringOffset = 0;
    stringOpenMode = QTextStream::NotOpen;

    readBufferOffset = 0;
    readBufferStartDevicePos = 0;
    lastTokenSize = 0;

    hasWrittenData = false;
    generateBOM = false;
    encoding = QStringConverter::Utf8;
    toUtf16 = QStringDecoder(encoding);
    fromUtf16 = QStringEncoder(encoding);
    autoDetectUnicode = true;

    status = QTextStream::Ok;
}

//  from src/corelib/serialization/qtextstream.cpp, line 319, as _ZN18QTextStreamPrivate11setupDeviceEP9QIODevice
inline void QTextStreamPrivate::setupDevice(QIODevice *device)
{
    disconnectFromDevice();

#ifndef QT_NO_QOBJECT
    if (device) {
        // Explicitly set a direct connection (though it would have been so
        // anyway) so that QTextStream can be used from multiple threads when the
        // application code is handling synchronization (see also QTBUG-12055).
        aboutToCloseConnection = QObject::connect(
                device, &QIODevice::aboutToClose, device, [this] { flushWriteBuffer(); },
                Qt::DirectConnection);
    }
#else
    Q_UNUSED(device);
#endif
}

//  from src/corelib/serialization/qtextstream.cpp, line 337, as _ZN18QTextStreamPrivate20disconnectFromDeviceEv
inline void QTextStreamPrivate::disconnectFromDevice()
{
#ifndef QT_NO_QOBJECT
    QObject::disconnect(aboutToCloseConnection);
    aboutToCloseConnection = {};
#endif
}

//  from src/corelib/serialization/qtextstream.cpp, line 653, as _ZNK18QTextStreamPrivate7readPtrEv
inline const QChar *QTextStreamPrivate::readPtr() const
{
    Q_ASSERT(readBufferOffset <= readBuffer.size());
    if (string)
        return string->constData() + stringOffset;
    return readBuffer.constData() + readBufferOffset;
}

//  from src/corelib/serialization/qtextstream.cpp, line 700, as _ZN18QTextStreamPrivate18saveConverterStateEx
inline void QTextStreamPrivate::saveConverterState(qint64 newPos)
{
    // ### Hack, FIXME
    memcpy((void *)&savedToUtf16, (void *)&toUtf16, sizeof(QStringDecoder));
    readBufferStartDevicePos = newPos;
    readConverterSavedStateOffset = 0;
}

//  from src/corelib/serialization/qtextstream.cpp, line 711, as _ZN18QTextStreamPrivate28restoreToSavedConverterStateEv
inline void QTextStreamPrivate::restoreToSavedConverterState()
{
    if (savedToUtf16.isValid())
        memcpy((void *)&toUtf16, (void *)&savedToUtf16, sizeof(QStringDecoder));
    else
        toUtf16.resetState();
    savedToUtf16 = QStringDecoder();
}

//  from src/corelib/serialization/qtextstream.cpp, line 795, as _ZN18QTextStreamPrivate9ungetCharE5QChar
inline void QTextStreamPrivate::ungetChar(QChar ch)
{
    if (string) {
        if (stringOffset == 0)
            string->prepend(ch);
        else
            (*string)[--stringOffset] = ch;
        return;
    }

    if (readBufferOffset == 0) {
        readBuffer.prepend(ch);
        return;
    }

    readBuffer[--readBufferOffset] = ch;
}

//  from src/corelib/serialization/qtextstream.cpp, line 828, as _ZNK18QTextStreamPrivate7paddingEx
inline QTextStreamPrivate::PaddingResult QTextStreamPrivate::padding(qsizetype len) const
{
    Q_ASSERT(params.fieldWidth > len); // calling padding() when no padding is needed is an error

    qsizetype left = 0, right = 0;

    const qsizetype padSize = params.fieldWidth - len;

    switch (params.fieldAlignment) {
    case QTextStream::AlignLeft:
        right = padSize;
        break;
    case QTextStream::AlignRight:
    case QTextStream::AlignAccountingStyle:
        left  = padSize;
        break;
    case QTextStream::AlignCenter:
        left  = padSize/2;
        right = padSize - padSize/2;
        break;
    }
    return { left, right };
}

//  from src/corelib/serialization/qtextstream.cpp, line 462, as _ZN18QTextStreamPrivate15resetReadBufferEv
inline void QTextStreamPrivate::resetReadBuffer()
{
    readBuffer.clear();
    readBufferOffset = 0;
    readBufferStartDevicePos = (device ? device->pos() : 0);
}

//  from src/corelib/serialization/qtextstream.cpp, line 472, as _ZN18QTextStreamPrivate16flushWriteBufferEv
inline void QTextStreamPrivate::flushWriteBuffer()
{
    // no buffer next to the QString itself; this function should only
    // be called internally, for devices.
    if (string || !device)
        return;

    // Stream went bye-bye already. Appending further data may succeed again,
    // but would create a corrupted stream anyway.
    if (status != QTextStream::Ok)
        return;

    if (writeBuffer.isEmpty())
        return;

#if defined (Q_OS_WIN)
    // handle text translation and bypass the Text flag in the device.
    bool textModeEnabled = device->isTextModeEnabled();
    if (textModeEnabled) {
        device->setTextModeEnabled(false);
        writeBuffer.replace(u'\n', "\r\n"_L1);
    }
#endif

    QByteArray data = fromUtf16(writeBuffer);
    writeBuffer.clear();
    hasWrittenData = true;

    // write raw data to the device
    qint64 bytesWritten = device->write(data);
#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::flushWriteBuffer(), device->write(\"%s\") == %d",
           QtDebugUtils::toPrintable(data.constData(), data.size(), 32).constData(),
           int(bytesWritten));
#endif

#if defined (Q_OS_WIN)
    // reset the text flag
    if (textModeEnabled)
        device->setTextModeEnabled(true);
#endif

    if (bytesWritten <= 0) {
        status = QTextStream::WriteFailed;
        return;
    }

    // flush the file
#ifndef QT_NO_QOBJECT
    QFileDevice *file = qobject_cast<QFileDevice *>(device);
    bool flushed = !file || file->flush();
#else
    bool flushed = true;
#endif

#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::flushWriteBuffer() wrote %d bytes", int(bytesWritten));
#endif
    if (!flushed || bytesWritten != qint64(data.size()))
        status = QTextStream::WriteFailed;
}
//  -----------------------------------------------------------------------

//  QTextStream *QTextStreamPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextStream *ritual_ZN18QTextStreamPrivate6q_funcEv(
    QTextStreamPrivate *self) {
  return self->q_func();
}

//  const QTextStream *QTextStreamPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextStream *ritual_ZNK18QTextStreamPrivate6q_funcEv(
    const QTextStreamPrivate *self) {
  return self->q_func();
}

//  QTextStreamPrivate::QTextStreamPrivate(QTextStream *q_ptr)
extern "C" Q_DECL_EXPORT
QTextStreamPrivate *ritual_ZN18QTextStreamPrivateC1EP11QTextStream(
    QTextStream *q_ptr) {
  return new QTextStreamPrivate(q_ptr);
}

//  QTextStreamPrivate::~QTextStreamPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivateD1Ev(QTextStreamPrivate *self) {
  delete self;
}

//  void QTextStreamPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate5resetEv(QTextStreamPrivate *self) {
  self->reset();
}

//  void QTextStreamPrivate::setupDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate11setupDeviceEP9QIODevice(
    QTextStreamPrivate *self,
    QIODevice *device) {
  self->setupDevice(device);
}

//  void QTextStreamPrivate::disconnectFromDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate20disconnectFromDeviceEv(
    QTextStreamPrivate *self) {
  self->disconnectFromDevice();
}

//  const QChar *QTextStreamPrivate::readPtr() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK18QTextStreamPrivate7readPtrEv(
    const QTextStreamPrivate *self) {
  return self->readPtr();
}

//  void QTextStreamPrivate::saveConverterState(qint64 newPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate18saveConverterStateEx(
    QTextStreamPrivate *self,
    qint64 newPos) {
  self->saveConverterState(newPos);
}

//  void QTextStreamPrivate::restoreToSavedConverterState()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate28restoreToSavedConverterStateEv(
    QTextStreamPrivate *self) {
  self->restoreToSavedConverterState();
}

//  void QTextStreamPrivate::ungetChar(QChar ch)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate9ungetCharE5QChar(
    QTextStreamPrivate *self,
    const QChar *ch) {
  self->ungetChar(*ch);
}

//  PaddingResult QTextStreamPrivate::padding(qsizetype len) const
extern "C" Q_DECL_EXPORT
QTextStreamPrivate::PaddingResult *ritual_ZNK18QTextStreamPrivate7paddingEx(
    const QTextStreamPrivate *self,
    qsizetype len) {
  return new QTextStreamPrivate::PaddingResult(self->padding(len));
}

//  void QTextStreamPrivate::resetReadBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate15resetReadBufferEv(
    QTextStreamPrivate *self) {
  self->resetReadBuffer();
}

//  void QTextStreamPrivate::flushWriteBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate16flushWriteBufferEv(
    QTextStreamPrivate *self) {
  self->flushWriteBuffer();
}
