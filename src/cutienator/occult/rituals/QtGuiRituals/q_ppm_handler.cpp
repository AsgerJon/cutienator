//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qppmhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_PPM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qppmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qppmhandler_p.h>
#ifndef QT_NO_IMAGEFORMAT_PPM
#include <QtCore/qdebug.h>
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qrgba64.h>
#include <QtCore/qvariant.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtGui/private/qimage_p.h>
#endif
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qppmhandler.cpp, line 25, as local:qppmhandler.cpp:discard_pbm_line
#if !defined(QT_NO_IMAGEFORMAT_PPM)
static void discard_pbm_line(QIODevice *d)
{
    const int buflen = 100;
    char buf[buflen];
    int res = 0;
    do {
        res = d->readLine(buf, buflen);
    } while (res > 0 && buf[res-1] != '\n');
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 102, as local:qppmhandler.cpp:scale_pbm_color
#if !defined(QT_NO_IMAGEFORMAT_PPM)
static inline QRgb scale_pbm_color(quint16 mx, quint16 rv, quint16 gv, quint16 bv)
{
    return QRgba64::fromRgba64((rv * 0xffffu) / mx, (gv * 0xffffu) / mx, (bv * 0xffffu) / mx, 0xffff).toArgb32();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 280, as local:qppmhandler.cpp:write_pbm_image
#if !defined(QT_NO_IMAGEFORMAT_PPM)
static bool write_pbm_image(QIODevice *out, const QImage &sourceImage, QByteArrayView sourceFormat)
{
    QByteArray str;
    QImage image = sourceImage;
    const QByteArrayView format = sourceFormat.left(3); // ignore RAW part

    bool gray = format == "pgm";

    if (format == "pbm") {
        image = image.convertToFormat(QImage::Format_Mono);
    } else if (gray) {
        image = image.depth() <= 8 ? image.convertToFormat(QImage::Format_Grayscale8) : image.convertToFormat(QImage::Format_Grayscale16);
    } else {
        switch (image.format()) {
        case QImage::Format_Mono:
        case QImage::Format_MonoLSB:
            image = image.convertToFormat(QImage::Format_Indexed8);
            break;
        case QImage::Format_Indexed8:
        case QImage::Format_RGB32:
        case QImage::Format_ARGB32:
            break;
        default:
            if (image.hasAlphaChannel())
                image = image.convertToFormat(QImage::Format_ARGB32);
            else
                image = image.convertToFormat(QImage::Format_RGB32);
            break;
        }
    }

    if (image.depth() == 1 && image.colorCount() == 2) {
        if (qGray(image.color(0)) < qGray(image.color(1))) {
            // 0=dark/black, 1=light/white - invert
            image.detach();
            for (int y=0; y<image.height(); y++) {
                uchar *p = image.scanLine(y);
                uchar *end = p + image.bytesPerLine();
                while (p < end)
                    *p++ ^= 0xff;
            }
        }
    }

    uint w = image.width();
    uint h = image.height();

    str = "P\n";
    str += QByteArray::number(w);
    str += ' ';
    str += QByteArray::number(h);
    str += '\n';

    switch (image.depth()) {
        case 1: {
            str.insert(1, '4');
            if (out->write(str, str.size()) != str.size())
                return false;
            w = (w+7)/8;
            for (uint y=0; y<h; y++) {
                uchar* line = image.scanLine(y);
                if (w != (uint)out->write((char*)line, w))
                    return false;
            }
            }
            break;

        case 8: {
            str.insert(1, gray ? '5' : '6');
            str.append("255\n");
            if (out->write(str, str.size()) != str.size())
                return false;
            qsizetype bpl = qsizetype(w) * (gray ? 1 : 3);
            uchar *buf = new uchar[bpl];
            if (image.format() == QImage::Format_Indexed8) {
                const QList<QRgb> color = image.colorTable();
                for (uint y=0; y<h; y++) {
                    const uchar *b = image.constScanLine(y);
                    uchar *p = buf;
                    uchar *end = buf+bpl;
                    if (gray) {
                        while (p < end) {
                            uchar g = (uchar)qGray(color[*b++]);
                            *p++ = g;
                        }
                    } else {
                        while (p < end) {
                            QRgb rgb = color[*b++];
                            *p++ = qRed(rgb);
                            *p++ = qGreen(rgb);
                            *p++ = qBlue(rgb);
                        }
                    }
                    if (bpl != (qsizetype)out->write((char*)buf, bpl))
                        return false;
                }
            } else {
                for (uint y=0; y<h; y++) {
                    const uchar *b = image.constScanLine(y);
                    uchar *p = buf;
                    uchar *end = buf + bpl;
                    if (gray) {
                        while (p < end)
                            *p++ = *b++;
                    } else {
                        while (p < end) {
                            uchar color = *b++;
                            *p++ = color;
                            *p++ = color;
                            *p++ = color;
                        }
                    }
                    if (bpl != (qsizetype)out->write((char*)buf, bpl))
                        return false;
                }
            }
            delete [] buf;
            break;
        }
        case 16: {
            str.insert(1, gray ? '5' : '6');
            str.append("65535\n");
            if (out->write(str, str.size()) != str.size())
                return false;
            qsizetype bpl = sizeof(uint16_t) * qsizetype(w) * (gray ? 1 : 3);
            uchar *buf = new uchar[bpl];
            for (uint y=0; y<h; y++) {
                const uint16_t *b = reinterpret_cast<const uint16_t *>(image.constScanLine(y));
                uint16_t *p = reinterpret_cast<uint16_t *>(buf);
                uint16_t *end = reinterpret_cast<uint16_t *>(buf + bpl);
                if (gray) {
                    while (p < end)
                        *p++ = qToBigEndian(*b++);
                } else {
                    while (p < end) {
                        uchar color = qToBigEndian(*b++);
                        *p++ = color;
                        *p++ = color;
                        *p++ = color;
                    }
                }
                if (bpl != (qsizetype)out->write((char*)buf, bpl))
                    return false;
            }
            delete [] buf;
            break;
        }

        case 32: {
            str.insert(1, '6');
            str.append("255\n");
            if (out->write(str, str.size()) != str.size())
                return false;
            qsizetype bpl = qsizetype(w) * 3;
            uchar *buf = new uchar[bpl];
            for (uint y=0; y<h; y++) {
                const QRgb  *b = reinterpret_cast<const QRgb *>(image.constScanLine(y));
                uchar *p = buf;
                uchar *end = buf+bpl;
                while (p < end) {
                    QRgb rgb = *b++;
                    *p++ = qRed(rgb);
                    *p++ = qGreen(rgb);
                    *p++ = qBlue(rgb);
                }
                if (bpl != (qsizetype)out->write((char*)buf, bpl))
                    return false;
            }
            delete [] buf;
            break;
        }

    default:
        return false;
    }

    return true;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 473, as _ZNK11QPpmHandler7canReadEv
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline bool QPpmHandler::canRead() const
{
    if (state == Ready && !canRead(device(), &subType))
        return false;

    if (state != Error) {
        setFormat(subType);
        return true;
    }

    return false;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 534, as _ZN11QPpmHandler5writeERK6QImage
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline bool QPpmHandler::write(const QImage &image)
{
    return write_pbm_image(device(), image, subType);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 546, as _ZNK11QPpmHandler6optionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline QVariant QPpmHandler::option(ImageOption option) const
{
    if (option == SubType) {
        return subType;
    } else if (option == Size) {
        if (state == Error)
            return QVariant();
        if (state == Ready && !const_cast<QPpmHandler*>(this)->readHeader())
            return QVariant();
        return QSize(width, height);
    } else if (option == ImageFormat) {
        if (state == Error)
            return QVariant();
        if (state == Ready && !const_cast<QPpmHandler*>(this)->readHeader())
            return QVariant();
        QImage::Format format = QImage::Format_Invalid;
        switch (type) {
            case '1':                                // ascii PBM
            case '4':                                // raw PBM
                format = QImage::Format_Mono;
                break;
            case '2':                                // ascii PGM
            case '5':                                // raw PGM
                if (mcc <= std::numeric_limits<uint8_t>::max())
                    format = QImage::Format_Grayscale8;
                else
                    format = QImage::Format_Grayscale16;
                break;
            case '3':                                // ascii PPM
            case '6':                                // raw PPM
                format = QImage::Format_RGB32;
                break;
            default:
                break;
        }
        return format;
    }
    return QVariant();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 586, as _ZN11QPpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline void QPpmHandler::setOption(ImageOption option, const QVariant &value)
{
    if (option == SubType)
        subType = value.toByteArray().toLower();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qppmhandler.cpp, line 539, as _ZNK11QPpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline bool QPpmHandler::supportsOption(ImageOption option) const
{
    return option == SubType
        || option == Size
        || option == ImageFormat;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  from src/gui/image/qimageiohandler.cpp, line 238, as _Z9lcImageIov
inline const QLoggingCategory &lcImageIo()
{
    static const QLoggingCategory category("qt.gui.imageio");
    return category;
}

//  from src/gui/image/qppmhandler.cpp, line 486, as _ZN11QPpmHandler7canReadEP9QIODeviceP10QByteArray
#if !defined(QT_NO_IMAGEFORMAT_PPM)
inline bool QPpmHandler::canRead(QIODevice *device, QByteArray *subType)
{
    if (!device) {
        qCWarning(lcImageIo, "QPpmHandler::canRead() called with no device");
        return false;
    }

    char head[2];
    if (device->peek(head, sizeof(head)) != sizeof(head))
        return false;

    if (head[0] != 'P')
        return false;

    if (head[1] == '1' || head[1] == '4') {
        if (subType)
            *subType = "pbm";
    } else if (head[1] == '2' || head[1] == '5') {
        if (subType)
            *subType = "pgm";
    } else if (head[1] == '3' || head[1] == '6') {
        if (subType)
            *subType = "ppm";
    } else {
        return false;
    }
    return true;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)
//  -----------------------------------------------------------------------

//  bool QPpmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPpmHandler7canReadEv(const QPpmHandler *self) {
  return self->canRead();
}

//  bool QPpmHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPpmHandler4readEP6QImage(QPpmHandler *self, QImage *image) {
  return self->read(image);
}

//  bool QPpmHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPpmHandler5writeERK6QImage(
    QPpmHandler *self,
    const QImage *image) {
  return self->write(*image);
}

#if !defined(QT_NO_IMAGEFORMAT_PPM)
//  bool QPpmHandler::canRead(QIODevice *device, QByteArray *subType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPpmHandler7canReadEP9QIODeviceP10QByteArray(
    QIODevice *device,
    QByteArray *subType) {
  return QPpmHandler::canRead(device, subType);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

//  QVariant QPpmHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QPpmHandler6optionEN15QImageIOHandler11ImageOptionE(
    const QPpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QPpmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QPpmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QPpmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QPpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

#if !defined(QT_NO_IMAGEFORMAT_PPM)
//  bool QPpmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QPpmHandler7canReadEv(const QPpmHandler *self) {
  return self->QPpmHandler::canRead();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

#if !defined(QT_NO_IMAGEFORMAT_PPM)
//  bool QPpmHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QPpmHandler5writeERK6QImage(
    QPpmHandler *self,
    const QImage *image) {
  return self->QPpmHandler::write(*image);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

#if !defined(QT_NO_IMAGEFORMAT_PPM)
//  void QPpmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QPpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QPpmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->QPpmHandler::setOption(option, *value);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

#if !defined(QT_NO_IMAGEFORMAT_PPM)
//  bool QPpmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QPpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QPpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QPpmHandler::supportsOption(option);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)

#endif  // !defined(QT_NO_IMAGEFORMAT_PPM)
