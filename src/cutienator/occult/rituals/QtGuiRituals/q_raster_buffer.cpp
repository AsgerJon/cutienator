//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtCore/qmutex.h>
#include <QtGui/private/qrasterdefs_p.h>
#include <QtGui/private/qgrayraster_p.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qdebug.h>
#include <QtGui/qbitmap.h>
#include <QtGui/private/qmath_p.h>
#include <QtCore/qrandom.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qpixmap_raster_p.h>
#include <QtGui/private/qimage_p.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtGui/private/qcosmeticstroker_p.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtGui/private/qmemrotate_p.h>
#include <QtGui/private/qpixellayout_p.h>
#include <QtGui/private/qrgba64_p.h>
#include <QtGui/private/qpaintengine_raster_p.h>
#include <QtGui/private/qoutlinemapper_p.h>
#include <limits.h>
#include <algorithm>
#ifdef Q_OS_WIN
#  include <QtCore/qvarlengtharray.h>
#  include <QtGui/private/qfontengine_p.h>
#  include <QtCore/qt_windows.h>
#ifdef Q_OS_WIN64
#    include <malloc.h>
#  endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpaintengine_raster.cpp, line 3750, as _ZN13QRasterBufferD1Ev
inline QRasterBuffer::~QRasterBuffer()
{
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3754, as _ZN13QRasterBuffer4initEv
inline void QRasterBuffer::init()
{
    compositionMode = QPainter::CompositionMode_SourceOver;
    monoDestinationWithClut = false;
    destColor0 = 0;
    destColor1 = 0;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3762, as _ZN13QRasterBuffer7prepareEP6QImage
inline QImage::Format QRasterBuffer::prepare(QImage *image)
{
    m_buffer = (uchar *)image->bits();
    m_width = qMin(QT_RASTER_COORD_LIMIT, image->width());
    m_height = qMin(QT_RASTER_COORD_LIMIT, image->height());
    bytes_per_pixel = image->depth()/8;
    bytes_per_line = image->bytesPerLine();

    format = image->format();
    colorSpace = image->colorSpace();
    if (image->depth() == 1 && image->colorTable().size() == 2) {
        monoDestinationWithClut = true;
        const QList<QRgb> colorTable = image->colorTable();
        destColor0 = qPremultiply(colorTable[0]);
        destColor1 = qPremultiply(colorTable[1]);
    }

    return format;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3727, as _ZN13QRasterBuffer14colorizeBitmapERK6QImageRK6QColor
inline QImage QRasterBuffer::colorizeBitmap(const QImage &image, const QColor &color)
{
    Q_ASSERT(image.depth() == 1);

    const QImage sourceImage = image.convertToFormat(QImage::Format_MonoLSB);
    QImage dest = QImage(sourceImage.size(), QImage::Format_ARGB32_Premultiplied);
    if (sourceImage.isNull() || dest.isNull())
        return image; // we must have run out of memory

    QRgb fg = qPremultiply(color.rgba());
    QRgb bg = 0;

    int height = sourceImage.height();
    int width = sourceImage.width();
    for (int y=0; y<height; ++y) {
        const uchar *source = sourceImage.constScanLine(y);
        QRgb *target = reinterpret_cast<QRgb *>(dest.scanLine(y));
        for (int x=0; x < width; ++x)
            target[x] = (source[x>>3] >> (x&7)) & 1 ? fg : bg;
    }
    return dest;
}
//  -----------------------------------------------------------------------

//  QRasterBuffer::QRasterBuffer()
extern "C" Q_DECL_EXPORT
QRasterBuffer *ritual_ZN13QRasterBufferC1Ev() {
  return new QRasterBuffer();
}

//  QRasterBuffer::~QRasterBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRasterBufferD1Ev(QRasterBuffer *self) {
  delete self;
}

//  void QRasterBuffer::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRasterBuffer4initEv(QRasterBuffer *self) {
  self->init();
}

//  QImage::Format QRasterBuffer::prepare(QImage *image)
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZN13QRasterBuffer7prepareEP6QImage(
    QRasterBuffer *self,
    QImage *image) {
  return self->prepare(image);
}

//  int QRasterBuffer::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRasterBuffer5widthEv(const QRasterBuffer *self) {
  return self->width();
}

//  int QRasterBuffer::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRasterBuffer6heightEv(const QRasterBuffer *self) {
  return self->height();
}

//  qsizetype QRasterBuffer::bytesPerLine() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QRasterBuffer12bytesPerLineEv(
    const QRasterBuffer *self) {
  return self->bytesPerLine();
}

//  int QRasterBuffer::bytesPerPixel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRasterBuffer13bytesPerPixelEv(const QRasterBuffer *self) {
  return self->bytesPerPixel();
}

//  QImage QRasterBuffer::colorizeBitmap(const QImage &image, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QRasterBuffer14colorizeBitmapERK6QImageRK6QColor(
    QRasterBuffer *self,
    const QImage *image,
    const QColor *color) {
  return new QImage(self->colorizeBitmap(*image, *color));
}
