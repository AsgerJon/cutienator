//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtextstream_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-27: code taken from Qt's source no longer stands under
//  defined(Q_OS_LINUX), which Qt does not write there; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qtextstream.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtextstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtextstream.h>
#include <QtCore/private/qtextstream_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qfile.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/private/qdebug_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qtools_p.h>
#include <locale.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <stdlib.h>
#include <limits.h>
#include <new>
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

//  from src/corelib/serialization/qtextstream.cpp, line 252, as local:qtextstream.cpp:QTEXTSTREAM_BUFFERSIZE
static const qsizetype QTEXTSTREAM_BUFFERSIZE = 16384;

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

//  from src/corelib/serialization/qtextstream.cpp, line 348, as _ZN18QTextStreamPrivate14fillReadBufferEx
inline bool QTextStreamPrivate::fillReadBuffer(qint64 maxBytes)
{
    // no buffer next to the QString itself; this function should only
    // be called internally, for devices.
    Q_ASSERT(!string);
    Q_ASSERT(device);

    // handle text translation and bypass the Text flag in the device.
    bool textModeEnabled = device->isTextModeEnabled();
    if (textModeEnabled)
        device->setTextModeEnabled(false);

    // read raw data into a temporary buffer
    char buf[QTEXTSTREAM_BUFFERSIZE];
    qint64 bytesRead = 0;
#if defined(Q_OS_WIN)
    // On Windows, there is no non-blocking stdin - so we fall back to reading
    // lines instead. If there is no QOBJECT, we read lines for all sequential
    // devices; otherwise, we read lines only for stdin.
    QFile *file = 0;
    Q_UNUSED(file);
    if (device->isSequential()
#if !defined(QT_NO_QOBJECT)
        && (file = qobject_cast<QFile *>(device)) && file->handle() == 0
#endif
        ) {
        if (maxBytes != -1)
            bytesRead = device->readLine(buf, qMin<qint64>(sizeof(buf), maxBytes));
        else
            bytesRead = device->readLine(buf, sizeof(buf));
    } else
#endif
    {
        if (maxBytes != -1)
            bytesRead = device->read(buf, qMin<qint64>(sizeof(buf), maxBytes));
        else
            bytesRead = device->read(buf, sizeof(buf));
    }

    // reset the Text flag.
    if (textModeEnabled)
        device->setTextModeEnabled(true);

    if (bytesRead <= 0)
        return false;

#ifndef QT_BOOTSTRAPPED
    if (autoDetectUnicode) {
        autoDetectUnicode = false;

        auto e = QStringConverter::encodingForData(QByteArrayView(buf, bytesRead));
        // QStringConverter::Locale implies unknown, so keep the current encoding
        if (e) {
            encoding = *e;
            toUtf16 = QStringDecoder(encoding);
            fromUtf16 = QStringEncoder(encoding);
        }
    }
#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::fillReadBuffer(), using %s encoding", QStringConverter::nameForEncoding(encoding));
#endif
#endif

#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::fillReadBuffer(), device->read(\"%s\", %d) == %d",
           QtDebugUtils::toPrintable(buf, bytesRead, 32).constData(),
           int(sizeof(buf)), int(bytesRead));
#endif

    qsizetype oldReadBufferSize = readBuffer.size();
    readBuffer += toUtf16(QByteArrayView(buf, bytesRead));

    // remove all '\r\n' in the string.
    if (readBuffer.size() > oldReadBufferSize && textModeEnabled) {
        QChar CR = u'\r';
        QChar *writePtr = readBuffer.data() + oldReadBufferSize;
        QChar *readPtr = readBuffer.data() + oldReadBufferSize;
        QChar *endPtr = readBuffer.data() + readBuffer.size();

        qsizetype n = oldReadBufferSize;
        if (readPtr < endPtr) {
            // Cut-off to avoid unnecessary self-copying.
            while (*readPtr++ != CR) {
                ++n;
                if (++writePtr == endPtr)
                    break;
            }
        }
        while (readPtr < endPtr) {
            QChar ch = *readPtr++;
            if (ch != CR) {
                *writePtr++ = ch;
            } else {
                if (n < readBufferOffset)
                    --readBufferOffset;
                --bytesRead;
            }
            ++n;
        }
        readBuffer.resize(writePtr - readBuffer.data());
    }

#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::fillReadBuffer() read %d bytes from device. readBuffer = [%s]",
           int(bytesRead),
           QtDebugUtils::toPrintable(readBuffer.toLatin1(), readBuffer.size(),
                                     readBuffer.size()).constData());
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

//  from src/corelib/serialization/qtextstream.cpp, line 534, as _ZN18QTextStreamPrivate4readEx
inline QString QTextStreamPrivate::read(qsizetype maxlen)
{
    QString ret;
    if (string) {
        lastTokenSize = qMin(maxlen, string->size() - stringOffset);
        ret = string->mid(stringOffset, lastTokenSize);
    } else {
        while (readBuffer.size() - readBufferOffset < maxlen && fillReadBuffer()) {}
        lastTokenSize = qMin(maxlen, readBuffer.size() - readBufferOffset);
        ret = readBuffer.mid(readBufferOffset, lastTokenSize);
    }
    consumeLastToken();

#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::read() maxlen = %d, token length = %d",
           int(maxlen), int(ret.length()));
#endif
    return ret;
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

//  from src/corelib/serialization/qtextstream.cpp, line 653, as _ZNK18QTextStreamPrivate7readPtrEv
inline const QChar *QTextStreamPrivate::readPtr() const
{
    Q_ASSERT(readBufferOffset <= readBuffer.size());
    if (string)
        return string->constData() + stringOffset;
    return readBuffer.constData() + readBufferOffset;
}

//  from src/corelib/serialization/qtextstream.cpp, line 664, as _ZN18QTextStreamPrivate16consumeLastTokenEv
inline void QTextStreamPrivate::consumeLastToken()
{
    if (lastTokenSize)
        consume(lastTokenSize);
    lastTokenSize = 0;
}

//  from src/corelib/serialization/qtextstream.cpp, line 674, as _ZN18QTextStreamPrivate7consumeEx
inline void QTextStreamPrivate::consume(qsizetype size)
{
#if defined (QTEXTSTREAM_DEBUG)
    qDebug("QTextStreamPrivate::consume(%d)", int(size));
#endif
    if (string) {
        stringOffset += size;
        if (stringOffset > string->size())
            stringOffset = string->size();
    } else {
        readBufferOffset += size;
        if (readBufferOffset >= readBuffer.size()) {
            readBufferOffset = 0;
            readBuffer.clear();
            saveConverterState(device->pos());
        } else if (readBufferOffset > QTEXTSTREAM_BUFFERSIZE) {
            readBuffer = readBuffer.remove(0,readBufferOffset);
            readConverterSavedStateOffset += readBufferOffset;
            readBufferOffset = 0;
        }
    }
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

//  from src/corelib/serialization/qtextstream.cpp, line 778, as _ZN18QTextStreamPrivate7getCharEP5QChar
inline bool QTextStreamPrivate::getChar(QChar *ch)
{
    if ((string && stringOffset == string->size())
        || (device && readBuffer.isEmpty() && !fillReadBuffer())) {
        if (ch)
            *ch = QChar();
        return false;
    }
    if (ch)
        *ch = *readPtr();
    consume(1);
    return true;
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

//  from src/corelib/serialization/qtextstream.cpp, line 1811, as _ZN18QTextStreamPrivate7getRealEPd
inline bool QTextStreamPrivate::getReal(double *f)
{
    // We use a table-driven FSM to parse floating point numbers
    // strtod() cannot be used directly since we may be reading from a
    // QIODevice.
    enum ParserState {
        Init = 0,
        Sign = 1,
        Mantissa = 2,
        Dot = 3,
        Abscissa = 4,
        ExpMark = 5,
        ExpSign = 6,
        Exponent = 7,
        Nan1 = 8,
        Nan2 = 9,
        Inf1 = 10,
        Inf2 = 11,
        NanInf = 12,
        Done = 13
    };
    enum InputToken {
        None = 0,
        InputSign = 1,
        InputDigit = 2,
        InputDot = 3,
        InputExp = 4,
        InputI = 5,
        InputN = 6,
        InputF = 7,
        InputA = 8,
        InputT = 9
    };

    static const uchar table[13][10] = {
        // None InputSign InputDigit InputDot InputExp InputI    InputN    InputF    InputA    InputT
        { 0,    Sign,     Mantissa,  Dot,     0,       Inf1,     Nan1,     0,        0,        0      }, // 0  Init
        { 0,    0,        Mantissa,  Dot,     0,       Inf1,     Nan1,     0,        0,        0      }, // 1  Sign
        { Done, Done,     Mantissa,  Dot,     ExpMark, 0,        0,        0,        0,        0      }, // 2  Mantissa
        { 0,    0,        Abscissa,  0,       0,       0,        0,        0,        0,        0      }, // 3  Dot
        { Done, Done,     Abscissa,  Done,    ExpMark, 0,        0,        0,        0,        0      }, // 4  Abscissa
        { 0,    ExpSign,  Exponent,  0,       0,       0,        0,        0,        0,        0      }, // 5  ExpMark
        { 0,    0,        Exponent,  0,       0,       0,        0,        0,        0,        0      }, // 6  ExpSign
        { Done, Done,     Exponent,  Done,    Done,    0,        0,        0,        0,        0      }, // 7  Exponent
        { 0,    0,        0,         0,       0,       0,        0,        0,        Nan2,     0      }, // 8  Nan1
        { 0,    0,        0,         0,       0,       0,        NanInf,   0,        0,        0      }, // 9  Nan2
        { 0,    0,        0,         0,       0,       0,        Inf2,     0,        0,        0      }, // 10 Inf1
        { 0,    0,        0,         0,       0,       0,        0,        NanInf,   0,        0      }, // 11 Inf2
        { Done, 0,        0,         0,       0,       0,        0,        0,        0,        0      }, // 11 NanInf
    };

    ParserState state = Init;
    InputToken input = None;

    scan(nullptr, nullptr, 0, NotSpace);
    consumeLastToken();

    const qsizetype BufferSize = 128;
    char buf[BufferSize];
    qsizetype i = 0;

    QChar c;
    while (getChar(&c)) {
        switch (c.unicode()) {
        case u'0': case u'1': case u'2': case u'3': case u'4':
        case u'5': case u'6': case u'7': case u'8': case u'9':
            input = InputDigit;
            break;
        case u'i': case u'I':
            input = InputI;
            break;
        case u'n': case u'N':
            input = InputN;
            break;
        case u'f': case u'F':
            input = InputF;
            break;
        case u'a': case u'A':
            input = InputA;
            break;
        case u't': case u'T':
            input = InputT;
            break;
        default: {
            QChar lc = c.toLower();
            if (lc == locale.decimalPoint().toLower())
                input = InputDot;
            else if (lc == locale.exponential().toLower())
                input = InputExp;
            else if (lc == locale.negativeSign().toLower()
                     || lc == locale.positiveSign().toLower())
                input = InputSign;
            else if (locale != QLocale::c() // backward-compatibility
                     && lc == locale.groupSeparator().toLower())
                input = InputDigit; // well, it isn't a digit, but no one cares.
            else
                input = None;
        }
            break;
        }

        state = ParserState(table[state][input]);

        if  (state == Init || state == Done || i > (BufferSize - 5)) {
            ungetChar(c);
            if (i > (BufferSize - 5)) { // ignore rest of digits
                while (getChar(&c)) {
                    if (!c.isDigit()) {
                        ungetChar(c);
                        break;
                    }
                }
            }
            break;
        }

        buf[i++] = c.toLatin1();
    }

    if (i == 0)
        return false;
    if (!f)
        return true;
    buf[i] = '\0';

    // backward-compatibility. Old implementation supported +nan/-nan
    // for some reason. QLocale only checks for lower-case
    // nan/+inf/-inf, so here we also check for uppercase and mixed
    // case versions.
    if (!qstricmp(buf, "nan") || !qstricmp(buf, "+nan") || !qstricmp(buf, "-nan")) {
        *f = qt_qnan();
        return true;
    } else if (!qstricmp(buf, "+inf") || !qstricmp(buf, "inf")) {
        *f = qt_inf();
        return true;
    } else if (!qstricmp(buf, "-inf")) {
        *f = -qt_inf();
        return true;
    }
    bool ok;
    *f = locale.toDouble(QString::fromLatin1(buf), &ok);
    return ok;
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

//  QString QTextStreamPrivate::read(qsizetype maxlen)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QTextStreamPrivate4readEx(
    QTextStreamPrivate *self,
    qsizetype maxlen) {
  return new QString(self->read(maxlen));
}

//  bool QTextStreamPrivate::scan(const QChar **ptr, qsizetype *tokenLength,
//      qsizetype maxlen, TokenDelimiter delimiter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextStreamPrivate4scanEPPK5QCharPxxNS_14TokenDelimiterE(
    QTextStreamPrivate *self,
    const QChar **ptr,
    qsizetype *tokenLength,
    qsizetype maxlen,
    QTextStreamPrivate::TokenDelimiter delimiter) {
  return self->scan(ptr, tokenLength, maxlen, delimiter);
}

//  const QChar *QTextStreamPrivate::readPtr() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK18QTextStreamPrivate7readPtrEv(
    const QTextStreamPrivate *self) {
  return self->readPtr();
}

//  void QTextStreamPrivate::consumeLastToken()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate16consumeLastTokenEv(
    QTextStreamPrivate *self) {
  self->consumeLastToken();
}

//  void QTextStreamPrivate::consume(qsizetype nchars)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate7consumeEx(
    QTextStreamPrivate *self,
    qsizetype nchars) {
  self->consume(nchars);
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

//  bool QTextStreamPrivate::getChar(QChar *ch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextStreamPrivate7getCharEP5QChar(
    QTextStreamPrivate *self,
    QChar *ch) {
  return self->getChar(ch);
}

//  void QTextStreamPrivate::ungetChar(QChar ch)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate9ungetCharE5QChar(
    QTextStreamPrivate *self,
    const QChar *ch) {
  self->ungetChar(*ch);
}

//  bool QTextStreamPrivate::getReal(double *f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextStreamPrivate7getRealEPd(
    QTextStreamPrivate *self,
    double *f) {
  return self->getReal(f);
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
