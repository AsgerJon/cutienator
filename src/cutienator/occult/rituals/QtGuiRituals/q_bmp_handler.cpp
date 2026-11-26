//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbmphandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_BMP)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbmphandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qbmphandler_p.h>
#ifndef QT_NO_IMAGEFORMAT_BMP
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <QtCore/qvariant.h>
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

//  from src/gui/image/qbmphandler.cpp, line 45, as local:qbmphandler.cpp:BMP_FILEHDR_SIZE
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_FILEHDR_SIZE = 14;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 62, as local:qbmphandler.cpp:BMP_OLD
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_OLD  = 12;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 63, as local:qbmphandler.cpp:BMP_WIN
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_WIN  = 40;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 65, as local:qbmphandler.cpp:BMP_WIN4
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_WIN4 = 108;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 68, as local:qbmphandler.cpp:BMP_RGB
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_RGB  = 0;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 71, as local:qbmphandler.cpp:BMP_BITFIELDS
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_BITFIELDS = 3;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 72, as local:qbmphandler.cpp:BMP_ALPHABITFIELDS
#if !defined(QT_NO_IMAGEFORMAT_BMP)
const int BMP_ALPHABITFIELDS = 4;
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 139, as local:qbmphandler.cpp:calc_shift
#if !defined(QT_NO_IMAGEFORMAT_BMP)
static uint calc_shift(uint mask)
{
    uint result = 0;
    while ((mask >= 0x100) || (!(mask & 1) && mask)) {
        result++;
        mask >>= 1;
    }
    return result;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 149, as local:qbmphandler.cpp:calc_scale
#if !defined(QT_NO_IMAGEFORMAT_BMP)
static uint calc_scale(uint low_mask)
{
    uint result = 8;
    while (low_mask && result) {
        result--;
        low_mask >>= 1;
    }
    return result;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 702, as _ZNK11QBmpHandler7canReadEv
#if !defined(QT_NO_IMAGEFORMAT_BMP)
inline bool QBmpHandler::canRead() const
{
    if (m_format == BmpFormat && state == Ready && !canRead(device()))
        return false;

    if (state != Error) {
        setFormat(formatName());
        return true;
    }

    return false;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 897, as _ZN11QBmpHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant
#if !defined(QT_NO_IMAGEFORMAT_BMP)
inline void QBmpHandler::setOption(ImageOption option, const QVariant &value)
{
    Q_UNUSED(option);
    Q_UNUSED(value);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 856, as _ZNK11QBmpHandler14supportsOptionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_BMP)
inline bool QBmpHandler::supportsOption(ImageOption option) const
{
    return option == Size
            || option == ImageFormat;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 715, as _ZN11QBmpHandler7canReadEP9QIODevice
#if !defined(QT_NO_IMAGEFORMAT_BMP)
inline bool QBmpHandler::canRead(QIODevice *device)
{
    if (!device) {
        qWarning("QBmpHandler::canRead() called with 0 pointer");
        return false;
    }

    char head[2];
    if (device->peek(head, sizeof(head)) != sizeof(head))
        return false;

    return (qstrncmp(head, "BM", 2) == 0);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  from src/gui/image/qbmphandler.cpp, line 674, as _ZNK11QBmpHandler10formatNameEv
#if !defined(QT_NO_IMAGEFORMAT_BMP)
inline QByteArray QBmpHandler::formatName() const
{
    return m_format == BmpFormat ? "bmp" : "dib";
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)
//  -----------------------------------------------------------------------

//  bool QBmpHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QBmpHandler7canReadEv(const QBmpHandler *self) {
  return self->canRead();
}

//  bool QBmpHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBmpHandler4readEP6QImage(QBmpHandler *self, QImage *image) {
  return self->read(image);
}

//  bool QBmpHandler::write(const QImage &image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBmpHandler5writeERK6QImage(
    QBmpHandler *self,
    const QImage *image) {
  return self->write(*image);
}

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  bool QBmpHandler::canRead(QIODevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBmpHandler7canReadEP9QIODevice(QIODevice *device) {
  return QBmpHandler::canRead(device);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

//  QVariant QBmpHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QBmpHandler6optionEN15QImageIOHandler11ImageOptionE(
    const QBmpHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QBmpHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBmpHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QBmpHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QBmpHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QBmpHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QBmpHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  QByteArray QBmpHandler::formatName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QBmpHandler10formatNameEv(const QBmpHandler *self) {
  return new QByteArray(self->formatName());
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  bool QBmpHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QBmpHandler7canReadEv(const QBmpHandler *self) {
  return self->QBmpHandler::canRead();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  void QBmpHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QBmpHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QBmpHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->QBmpHandler::setOption(option, *value);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  bool QBmpHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QBmpHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QBmpHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QBmpHandler::supportsOption(option);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)
