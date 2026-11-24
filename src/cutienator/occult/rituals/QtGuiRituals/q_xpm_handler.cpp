//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxpmhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_XPM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxpmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qxpmhandler_p.h>
#ifndef QT_NO_IMAGEFORMAT_XPM
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/qdebug.h>
#include <QtGui/qimage.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmap.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qvariant.h>
#include <QtGui/private/qcolor_p.h>
#include <QtCore/private/qduplicatetracker_p.h> // for easier std::pmr detection
#include <QtCore/private/qtools_p.h>
#include <QtGui/private/qimage_p.h>
#include <algorithm>
#include <array>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/image/qxpmhandler.cpp, line 1171, as _ZNK11QXpmHandler7canReadEv
#if !defined(QT_NO_IMAGEFORMAT_XPM)
inline bool QXpmHandler::canRead() const
{
    if (state == Ready && !canRead(device()))
        return false;

    if (state != Error) {
        setFormat("xpm");
        return true;
    }

    return false;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

//  from src/gui/image/qxpmhandler.cpp, line 1198, as _ZN11QXpmHandler4readEP6QImage
#if !defined(QT_NO_IMAGEFORMAT_XPM)
inline bool QXpmHandler::read(QImage *image)
{
    if (!canRead())
        return false;
    return readImage(image);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

//  from src/gui/image/qxpmhandler.cpp, line 1217, as _ZNK11QXpmHandler6optionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_XPM)
inline QVariant QXpmHandler::option(ImageOption option) const
{
    if (option == Name) {
        return fileName;
    } else if (option == Size) {
        if (state == Error)
            return QVariant();
        if (state == Ready && !const_cast<QXpmHandler*>(this)->readHeader())
            return QVariant();
        return QSize(width, height);
    } else if (option == ImageFormat) {
        if (state == Error)
            return QVariant();
        if (state == Ready && !const_cast<QXpmHandler*>(this)->readHeader())
            return QVariant();
        // If we have more than 256 colors in the table, we need to
        // figure out, if it contains transparency. That means reading
        // the whole color table, which is too much work work pre-checking
        // the image format
        if (ncols <= 256)
            return QImage::Format_Indexed8;
        else
            return QImage::Format_Invalid;
    }

    return QVariant();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

//  from src/gui/image/qxpmhandler.cpp, line 1245, as _ZN11QXpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant
#if !defined(QT_NO_IMAGEFORMAT_XPM)
inline void QXpmHandler::setOption(ImageOption option, const QVariant &value)
{
    if (option == Name)
        fileName = value.toString();
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

//  from src/gui/image/qxpmhandler.cpp, line 1210, as _ZNK11QXpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE
#if !defined(QT_NO_IMAGEFORMAT_XPM)
inline bool QXpmHandler::supportsOption(ImageOption option) const
{
    return option == Name
        || option == Size
        || option == ImageFormat;
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)
//  -----------------------------------------------------------------------

//  bool QXpmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXpmHandler7canReadEv(const QXpmHandler *self) {
  return self->canRead();
}

//  bool QXpmHandler::read(QImage *image)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QXpmHandler4readEP6QImage(QXpmHandler *self, QImage *image) {
  return self->read(image);
}

//  QVariant QXpmHandler::option(ImageOption option) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QXpmHandler6optionEN15QImageIOHandler11ImageOptionE(
    const QXpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return new QVariant(self->option(option));
}

//  void QXpmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QXpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QXpmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->setOption(option, *value);
}

//  bool QXpmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QXpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QXpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->supportsOption(option);
}

#if !defined(QT_NO_IMAGEFORMAT_XPM)
//  void QXpmHandler::setOption(ImageOption option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QXpmHandler9setOptionEN15QImageIOHandler11ImageOptionERK8QVariant(
    QXpmHandler *self,
    QImageIOHandler::ImageOption option,
    const QVariant *value) {
  self->QXpmHandler::setOption(option, *value);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

#if !defined(QT_NO_IMAGEFORMAT_XPM)
//  bool QXpmHandler::supportsOption(ImageOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QXpmHandler14supportsOptionEN15QImageIOHandler11ImageOptionE(
    const QXpmHandler *self,
    QImageIOHandler::ImageOption option) {
  return self->QXpmHandler::supportsOption(option);
}
#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)

#endif  // !defined(QT_NO_IMAGEFORMAT_XPM)
