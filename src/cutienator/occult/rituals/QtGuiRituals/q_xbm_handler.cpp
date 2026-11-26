//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxbmhandler_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: the code taken for 'write_xbm_image' no
//  longer stands under 'defined(Q_OS_LINUX)', which Qt's qxbmhandler.cpp
//  does not write: Qt builds it on every system, and 'write', which
//  calls it, stands on every system here. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_XBM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxbmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include <QtGui/private/qxbmhandler_p.h>
#ifndef QT_NO_IMAGEFORMAT_XBM
#include <QtGui/qimage.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvariant.h>
#include <QtCore/private/qtools_p.h>
#include <QtGui/private/qimage_p.h>
#include <cstdio>
#include <stdio.h>
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

//  from src/gui/image/qxbmhandler.cpp, line 29, as local:qxbmhandler.cpp:hex2byte
#if !defined(QT_NO_IMAGEFORMAT_XBM)
static inline int hex2byte(char *p)
{
    return QtMiscUtils::fromHex(p[0]) * 16 | QtMiscUtils::fromHex(p[1]);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 98, as local:qxbmhandler.cpp:read_xbm_body
#if !defined(QT_NO_IMAGEFORMAT_XBM)
static bool read_xbm_body(QIODevice *device, int w, int h, QImage *outImage)
{
    const int buflen = 300;
    char buf[buflen + 1];

    qint64 readBytes = 0;

    char *p;

    // scan for database
    do {
        if ((readBytes = device->readLine(buf, buflen)) <= 0) {
            // end of file
            return false;
        }

        buf[readBytes] = '\0';
        p = strstr(buf, "0x");
    } while (!p);

    if (!QImageIOHandler::allocateImage(QSize(w, h), QImage::Format_MonoLSB, outImage))
        return false;

    outImage->fill(Qt::color0);       // in case the image data does not cover the full image

    outImage->setColorCount(2);
    outImage->setColor(0, qRgb(255,255,255));        // white
    outImage->setColor(1, qRgb(0,0,0));                // black

    int           x = 0, y = 0;
    uchar *b = outImage->scanLine(0);
    w = (w+7)/8;                                // byte width

    while (y < h) {                                // for all encoded bytes...
        if (p && p < (buf + readBytes - 3)) {      // p = "0x.."
            const int byte = hex2byte(p + 2);
            if (byte < 0) // non-hex char encountered
                return false;
            *b++ = byte;
            p += 2;
            if (++x == w && ++y < h) {
                b = outImage->scanLine(y);
                x = 0;
            }
            p = strstr(p, "0x");
        } else {                                // read another line
            if ((readBytes = device->readLine(buf,buflen)) <= 0)        // EOF ==> truncated image
                break;
            buf[readBytes] = '\0';
            p = strstr(buf, "0x");
        }
    }

    return true;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 162, as local:qxbmhandler.cpp:write_xbm_image
#if !defined(QT_NO_IMAGEFORMAT_XBM)
static bool write_xbm_image(const QImage &sourceImage, QIODevice *device, const QString &fileName)
{
    QImage image = sourceImage;
    int        w = image.width();
    int        h = image.height();
    int        i;
    const QByteArray s = fileName.toUtf8(); // get file base name
    const auto msize = s.size() + 100;
    char *buf = new char[msize];

    std::snprintf(buf, msize, "#define %s_width %d\n", s.data(), w);
    device->write(buf, qstrlen(buf));
    std::snprintf(buf, msize, "#define %s_height %d\n", s.data(), h);
    device->write(buf, qstrlen(buf));
    std::snprintf(buf, msize, "static char %s_bits[] = {\n ", s.data());
    device->write(buf, qstrlen(buf));

    if (image.format() != QImage::Format_MonoLSB)
        image = image.convertToFormat(QImage::Format_MonoLSB);

    bool invert = qGray(image.color(0)) < qGray(image.color(1));
    char hexrep[16];
    for (i=0; i<10; i++)
        hexrep[i] = '0' + i;
    for (i=10; i<16; i++)
        hexrep[i] = 'a' -10 + i;
    if (invert) {
        char t;
        for (i=0; i<8; i++) {
            t = hexrep[15-i];
            hexrep[15-i] = hexrep[i];
            hexrep[i] = t;
        }
    }
    int bcnt = 0;
    char *p = buf;
    int bpl = (w+7)/8;
    for (int y = 0; y < h; ++y) {
        const uchar *b = image.constScanLine(y);
        for (i = 0; i < bpl; ++i) {
            *p++ = '0'; *p++ = 'x';
            *p++ = hexrep[*b >> 4];
            *p++ = hexrep[*b++ & 0xf];

            if (i < bpl - 1 || y < h - 1) {
                *p++ = ',';
                if (++bcnt > 14) {
                    *p++ = '\n';
                    *p++ = ' ';
                    *p   = '\0';
                    if ((int)qstrlen(buf) != device->write(buf, qstrlen(buf))) {
                        delete [] buf;
                        return false;
                    }
                    p = buf;
                    bcnt = 0;
                }
            }
        }
    }
#ifdef Q_CC_MSVC
    strcpy_s(p, sizeof(" };\n"), " };\n");
#else
    strcpy(p, " };\n");
#endif
    if ((int)qstrlen(buf) != device->write(buf, qstrlen(buf))) {
        delete [] buf;
        return false;
    }

    delete [] buf;
    return true;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 250, as _ZNK11QXbmHandler7canReadEv
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline bool QXbmHandler::canRead() const
{
    if (state == Ready && !canRead(device()))
        return false;

    if (state != Error) {
        setFormat("xbm");
        return true;
    }

    return false;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 284, as _ZN11QXbmHandler4readEP6QImage
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline bool QXbmHandler::read(QImage *image)
{
    if (state == Error)
        return false;

    if (state == Ready && !readHeader()) {
        state = Error;
        return false;
    }

    if (!read_xbm_body(device(), width, height, image)) {
        state = Error;
        return false;
    }

    state = Ready;
    return true;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 303, as _ZN11QXbmHandler5writeERK6QImage
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline bool QXbmHandler::write(const QImage &image)
{
    return write_xbm_image(image, device(), fileName);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 315, as _ZNK11QXbmHandler6optionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline QVariant QXbmHandler::option(ImageOption option) const
{
    if (option == Name) {
        return fileName;
    } else if (option == Size) {
        if (state == Error)
            return QVariant();
        if (state == Ready && !const_cast<QXbmHandler*>(this)->readHeader())
            return QVariant();
        return QSize(width, height);
    } else if (option == ImageFormat) {
        return QImage::Format_MonoLSB;
    }
    return QVariant();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 331, as _ZN11QXbmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline void QXbmHandler::setOption(ImageOption option, const QVariant &value)
{
    if (option == Name)
        fileName = value.toString();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

//  from src/gui/image/qxbmhandler.cpp, line 308, as _ZNK11QXbmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_XBM)
inline bool QXbmHandler::supportsOption(ImageOption option) const
{
    return option == Name
        || option == Size
        || option == ImageFormat;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)
//  -----------------------------------------------------------------------

//  bool QXbmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXbmHandler7canReadEv(const QXbmHandler *self) {
  return self->canRead();
}

//  bool QXbmHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QXbmHandler4readEP6QImage(QXbmHandler *self, QImage *image) {
  return self->read(image);
}

//  bool QXbmHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QXbmHandler5writeERK6QImage(
    QXbmHandler *self,
    const QImage *image) {
  return self->write(*image);
}

//  QVariant QXbmHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QXbmHandler6optionEN15QImageIOHandler11ImageOptionE(
    const QXbmHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QXbmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QXbmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QXbmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QXbmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXbmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QXbmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

#if !defined(QT_NO_IMAGEFORMAT_XBM)
//  bool QXbmHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QXbmHandler5writeERK6QImage(
    QXbmHandler *self,
    const QImage *image) {
  return self->QXbmHandler::write(*image);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

#if !defined(QT_NO_IMAGEFORMAT_XBM)
//  void QXbmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QXbmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QXbmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->QXbmHandler::setOption(option, *value);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

#if !defined(QT_NO_IMAGEFORMAT_XBM)
//  bool QXbmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QXbmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QXbmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QXbmHandler::supportsOption(option);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)

#endif  // !defined(QT_NO_IMAGEFORMAT_XBM)
