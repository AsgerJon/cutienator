//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PDF)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpdf_p.h>
#ifndef QT_NO_PDF
#include "qplatformdefs.h"
#include <QtGui/private/qcmyk_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtGui/qimagewriter.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qtimezone.h>
#include <QtCore/quuid.h>
#include <QtCore/qxmlstream.h>
#include <cstdio>
#include <map>
#ifndef QT_NO_COMPRESS
#include <zlib.h>
#endif
#endif
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

//  from src/gui/painting/qpdf.cpp, line 193, as _ZN4QPdf10ByteStreamC1Eb
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::ByteStream(bool fileBacking)
            : dev(new QBuffer(&ba)),
            fileBackingEnabled(fileBacking),
            fileBackingActive(false),
            handleDirty(false)
    {
        dev->open(QIODevice::ReadWrite);
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 184, as _ZN4QPdf10ByteStreamC1EP10QByteArrayb
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::ByteStream(QByteArray *byteArray, bool fileBacking)
            : dev(new QBuffer(byteArray)),
            fileBackingEnabled(fileBacking),
            fileBackingActive(false),
            handleDirty(false)
    {
        dev->open(QIODevice::ReadWrite | QIODevice::Append);
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 202, as _ZN4QPdf10ByteStreamD1Ev
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::~ByteStream()
    {
        delete dev;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 207, as _ZN4QPdf10ByteStreamlsEc
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream &ByteStream::operator <<(char chr)
    {
        if (handleDirty) prepareBuffer();
        dev->write(&chr, 1);
        return *this;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 214, as _ZN4QPdf10ByteStreamlsEPKc
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream &ByteStream::operator <<(const char *str)
    {
        if (handleDirty) prepareBuffer();
        dev->write(str, strlen(str));
        return *this;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 221, as _ZN4QPdf10ByteStreamlsERK10QByteArray
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream &ByteStream::operator <<(const QByteArray &str)
    {
        if (handleDirty) prepareBuffer();
        dev->write(str);
        return *this;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 228, as _ZN4QPdf10ByteStreamlsERKS0_
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream &ByteStream::operator <<(const ByteStream &src)
    {
        Q_ASSERT(!src.dev->isSequential());
        if (handleDirty) prepareBuffer();
        // We do play nice here, even though it looks ugly.
        // We save the position and restore it afterwards.
        ByteStream &s = const_cast<ByteStream&>(src);
        qint64 pos = s.dev->pos();
        s.dev->reset();
        while (!s.dev->atEnd()) {
            QByteArray buf = s.dev->read(chunkSize());
            dev->write(buf);
        }
        s.dev->seek(pos);
        return *this;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 268, as _ZN4QPdf10ByteStream6streamEv
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline QIODevice *ByteStream::stream()
    {
        dev->reset();
        handleDirty = true;
        return dev;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 275, as _ZN4QPdf10ByteStream5clearEv
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline void ByteStream::clear()
    {
        dev->open(QIODevice::ReadWrite | QIODevice::Truncate);
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 280, as _ZN4QPdf10ByteStream13prepareBufferEv
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline void ByteStream::prepareBuffer()
    {
        Q_ASSERT(!dev->isSequential());
        qint64 size = dev->size();
        if (fileBackingEnabled && !fileBackingActive
                && size > maxMemorySize()) {
            // Switch to file backing.
            QTemporaryFile *newFile = new QTemporaryFile;
            if (newFile->open()) {
                dev->reset();
                while (!dev->atEnd()) {
                    QByteArray buf = dev->read(chunkSize());
                    newFile->write(buf);
                }
                delete dev;
                dev = newFile;
                ba.clear();
                fileBackingActive = true;
            }
        }
        if (dev->pos() != size) {
            dev->seek(size);
            handleDirty = false;
        }
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)
//  -----------------------------------------------------------------------

//  QPdf::ByteStream::ByteStream(bool fileBacking)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamC1Eb(bool fileBacking) {
  return new QPdf::ByteStream(fileBacking);
}

//  QPdf::ByteStream::ByteStream(QByteArray *ba, bool fileBacking)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamC1EP10QByteArrayb(
    QByteArray *ba,
    bool fileBacking) {
  return new QPdf::ByteStream(ba, fileBacking);
}

//  QPdf::ByteStream::~ByteStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPdf10ByteStreamD1Ev(QPdf::ByteStream *self) {
  delete self;
}

#if !defined(QT_NO_PDF)
//  ByteStream &QPdf::ByteStream::operator<<(char chr)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamlsEc(
    QPdf::ByteStream *self,
    char chr) {
  return &(self->operator<<(chr));
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  ByteStream &QPdf::ByteStream::operator<<(const char *str)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamlsEPKc(
    QPdf::ByteStream *self,
    const char *str) {
  return &(self->operator<<(str));
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  ByteStream &QPdf::ByteStream::operator<<(const QByteArray &str)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamlsERK10QByteArray(
    QPdf::ByteStream *self,
    const QByteArray *str) {
  return &(self->operator<<(*str));
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  ByteStream &QPdf::ByteStream::operator<<(const ByteStream &src)
extern "C" Q_DECL_EXPORT
QPdf::ByteStream *ritual_ZN4QPdf10ByteStreamlsERKS0_(
    QPdf::ByteStream *self,
    const QPdf::ByteStream *src) {
  return &(self->operator<<(*src));
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  QIODevice *QPdf::ByteStream::stream()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN4QPdf10ByteStream6streamEv(QPdf::ByteStream *self) {
  return self->stream();
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  void QPdf::ByteStream::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPdf10ByteStream5clearEv(QPdf::ByteStream *self) {
  self->clear();
}
#endif  // !defined(QT_NO_PDF)

//  int QPdf::ByteStream::maxMemorySize()
extern "C" Q_DECL_EXPORT
int ritual_ZN4QPdf10ByteStream13maxMemorySizeEv() {
  return QPdf::ByteStream::maxMemorySize();
}

//  int QPdf::ByteStream::chunkSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN4QPdf10ByteStream9chunkSizeEv() {
  return QPdf::ByteStream::chunkSize();
}

#if !defined(QT_NO_PDF)
//  void QPdf::ByteStream::prepareBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPdf10ByteStream13prepareBufferEv(QPdf::ByteStream *self) {
  self->prepareBuffer();
}
#endif  // !defined(QT_NO_PDF)

#endif  // !defined(QT_NO_PDF)
