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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

#if !defined(QT_NO_IMAGEFORMAT_BMP)
//  bool QBmpHandler::canRead(QIODevice *device)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBmpHandler7canReadEP9QIODevice(QIODevice *device) {
  return QBmpHandler::canRead(device);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_BMP)

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
