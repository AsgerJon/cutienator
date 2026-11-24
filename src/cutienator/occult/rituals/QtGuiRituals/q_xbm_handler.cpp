//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxbmhandler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_IMAGEFORMAT_XBM)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxbmhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h>
#include "private/qxbmhandler_p.h"
#ifndef QT_NO_IMAGEFORMAT_XBM
#include <qimage.h>
#include <qiodevice.h>
#include <qloggingcategory.h>
#include <qvariant.h>
#include <private/qtools_p.h>
#include <private/qimage_p.h>
#include <cstdio>
#include <stdio.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
