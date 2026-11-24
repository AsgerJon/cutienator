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
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "private/qppmhandler_p.h"
#ifndef QT_NO_IMAGEFORMAT_PPM
#include <qdebug.h>
#include <qimage.h>
#include <qlist.h>
#include <qloggingcategory.h>
#include <qrgba64.h>
#include <qvariant.h>
#include <private/qlocale_p.h>
#include <private/qtools_p.h>
#include <private/qimage_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  bool QPpmHandler::canRead() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPpmHandler7canReadEv(const QPpmHandler *self) {
  return self->canRead();
}

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
