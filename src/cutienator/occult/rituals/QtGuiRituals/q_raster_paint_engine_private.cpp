//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrasterizer_p.h"
#include <QPoint>
#include <QRect>
#include <private/qmath_p.h>
#include <private/qdatabuffer_p.h>
#include <private/qdrawhelper_p.h>
#include <QtGui/qpainterpath.h>
#include <algorithm>
#include <QtCore/qglobal.h>
#include <QtCore/qmutex.h>
#include <private/qrasterdefs_p.h>
#include <private/qgrayraster_p.h>
#include <qpainterpath.h>
#include <qdebug.h>
#include <qbitmap.h>
#include "qmath_p.h"
#include <qrandom.h>
#include <private/qtextengine_p.h>
#include <private/qfontengine_p.h>
#include <private/qpixmap_raster_p.h>
#include <private/qimage_p.h>
#include <private/qstatictext_p.h>
#include <private/qcosmeticstroker_p.h>
#include <private/qdrawhelper_p.h>
#include <private/qmemrotate_p.h>
#include <private/qpixellayout_p.h>
#include <private/qrgba64_p.h>
#include "qpaintengine_raster_p.h"
#include "qoutlinemapper_p.h"
#include <limits.h>
#include <algorithm>
#ifdef Q_OS_WIN
#  include <qvarlengtharray.h>
#  include <private/qfontengine_p.h>
#  include <qt_windows.h>
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

//  from src/gui/painting/qrasterizer.cpp, line 598, as _ZN11QRasterizerD1Ev
inline QRasterizer::~QRasterizer()
{
    delete d;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3750, as _ZN13QRasterBufferD1Ev
inline QRasterBuffer::~QRasterBuffer()
{
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3968, as _ZN9QClipData11setClipRectERK5QRect
inline void QClipData::setClipRect(const QRect &rect)
{
    if (hasRectClip && rect == clipRect)
        return;

//    qDebug() << "setClipRect" << clipSpanHeight << count << allocated << rect;
    hasRectClip = true;
    hasRegionClip = false;
    clipRect = rect;

    xmin = rect.x();
    xmax = rect.x() + rect.width();
    ymin = qMin(rect.y(), clipSpanHeight);
    ymax = qMin(rect.y() + rect.height(), clipSpanHeight);

    if (m_spans) {
        free(m_spans);
        m_spans = nullptr;
    }

//    qDebug() << xmin << xmax << ymin << ymax;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3994, as _ZN9QClipData13setClipRegionERK7QRegion
inline void QClipData::setClipRegion(const QRegion &region)
{
    if (region.rectCount() == 1) {
        setClipRect(region.boundingRect());
        return;
    }

    hasRegionClip = true;
    hasRectClip = false;
    clipRegion = region;

    { // set bounding rect
        const QRect rect = region.boundingRect();
        xmin = rect.x();
        xmax = rect.x() + rect.width();
        ymin = rect.y();
        ymax = rect.y() + rect.height();
    }

    if (m_spans) {
        free(m_spans);
        m_spans = nullptr;
    }

}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3796, as _ZN9QClipDataD1Ev
inline QClipData::~QClipData()
{
    if (m_clipLines)
        free(m_clipLines);
    if (m_spans)
        free(m_spans);
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 4653, as _ZN9QSpanData11setupMatrixERK10QTransformi
inline void QSpanData::setupMatrix(const QTransform &matrix, int bilin)
{
    QTransform delta;
    // make sure we round off correctly in qdrawhelper.cpp
    delta.translate(1.0 / 65536, 1.0 / 65536);

    QTransform inv = (delta * matrix).inverted();
    m11 = inv.m11();
    m12 = inv.m12();
    m13 = inv.m13();
    m21 = inv.m21();
    m22 = inv.m22();
    m23 = inv.m23();
    m33 = inv.m33();
    dx = inv.dx();
    dy = inv.dy();
    txop = inv.type();
    bilinear = bilin;

    const bool affine = inv.isAffine();
    const qreal f1 = m11 * m11 + m21 * m21;
    const qreal f2 = m12 * m12 + m22 * m22;
    fast_matrix = affine
        && f1 < 1e4
        && f2 < 1e4
        && f1 > (1.0 / 65536)
        && f2 > (1.0 / 65536)
        && qAbs(dx) < 1e4
        && qAbs(dy) < 1e4;

    adjustSpanMethods();
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 241, as _ZN25QRasterPaintEnginePrivateC1Ev
inline QRasterPaintEnginePrivate::QRasterPaintEnginePrivate() :
    QPaintEngineExPrivate(),
    cachedLines(0)
{
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 1011, as _ZN25QRasterPaintEnginePrivate18systemStateChangedEv
inline void QRasterPaintEnginePrivate::systemStateChanged()
{
    deviceRectUnclipped = QRect(0, 0,
            qMin(QT_RASTER_COORD_LIMIT, device->width()),
            qMin(QT_RASTER_COORD_LIMIT, device->height()));

    if (!systemClip.isEmpty()) {
        QRegion clippedDeviceRgn = systemClip & deviceRectUnclipped;
        deviceRect = clippedDeviceRgn.boundingRect();
        baseClip->setClipRegion(clippedDeviceRgn);
    } else {
        deviceRect = deviceRectUnclipped;
        baseClip->setClipRect(deviceRect);
    }
#ifdef QT_DEBUG_DRAW
    qDebug() << "systemStateChanged" << this << "deviceRect" << deviceRect << deviceRectUnclipped << systemClip;
#endif

    exDeviceRect = deviceRect;

    Q_Q(QRasterPaintEngine);
    if (q->state()) {
        q->state()->strokeFlags |= QPaintEngine::DirtyClipRegion;
        q->state()->fillFlags |= QPaintEngine::DirtyClipRegion;
        q->state()->pixmapFlags |= QPaintEngine::DirtyClipRegion;
    }
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 935, as _ZN25QRasterPaintEnginePrivate9blitImageERK7QPointFRK6QImageRK5QRectS8_
inline void QRasterPaintEnginePrivate::blitImage(const QPointF &pt,
                                          const QImage &img,
                                          const QRect &clip,
                                          const QRect &sr)
{
    if (!clip.isValid())
        return;
    if (pt.x() > qreal(clip.right()) || pt.y() > qreal(clip.bottom()))
        return;
    if ((pt.x() + img.width()) < qreal(clip.left()) || (pt.y() + img.height()) < qreal(clip.top()))
        return;

    Q_ASSERT(img.depth() >= 8);

    qsizetype srcBPL = img.bytesPerLine();
    const uchar *srcBits = img.bits();
    int srcSize = img.depth() >> 3; // This is the part that is incompatible with lower than 8-bit..
    int iw = img.width();
    int ih = img.height();

    if (!sr.isEmpty()) {
        iw = sr.width();
        ih = sr.height();
        // Adjust the image according to the source offset...
        srcBits += ((sr.y() * srcBPL) + sr.x() * srcSize);
    }

    // adapt the x parameters
    int x = qRound(pt.x());
    int cx1 = clip.x();
    int cx2 = clip.x() + clip.width();
    if (x < cx1) {
        int d = cx1 - x;
        srcBits += srcSize * d;
        iw -= d;
        x = cx1;
    }
    if (x + iw > cx2) {
        int d = x + iw - cx2;
        iw -= d;
    }
    if (iw <= 0)
        return;

    // adapt the y parameters...
    int cy1 = clip.y();
    int cy2 = clip.y() + clip.height();
    int y = qRound(pt.y());
    if (y < cy1) {
        int d = cy1 - y;
        srcBits += srcBPL * d;
        ih -= d;
        y = cy1;
    }
    if (y + ih > cy2) {
        int d = y + ih - cy2;
        ih -= d;
    }
    if (ih <= 0)
        return;

    // blit..
    int dstSize = rasterBuffer->bytesPerPixel();
    qsizetype dstBPL = rasterBuffer->bytesPerLine();
    const uint *src = (const uint *) srcBits;
    uint *dst = reinterpret_cast<uint *>(rasterBuffer->buffer() + x * dstSize + y * dstBPL);

    const int len = iw * (qt_depthForFormat(rasterBuffer->format) >> 3);
    for (int y = 0; y < ih; ++y) {
        memcpy(dst, src, len);
        dst = (quint32 *)(((uchar *) dst) + dstBPL);
        src = (const quint32 *)(((const uchar *) src) + srcBPL);
    }
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 2902, as _ZNK25QRasterPaintEnginePrivate22isUnclipped_normalizedERK5QRect
inline bool QRasterPaintEnginePrivate::isUnclipped_normalized(const QRect &r) const
{
    const QClipData *cl = clip();
    if (!cl) {
        // inline contains() for performance (we know the rects are normalized)
        const QRect &r1 = deviceRect;
        return (r.left() >= r1.left() && r.right() <= r1.right()
                && r.top() >= r1.top() && r.bottom() <= r1.bottom());
    }


    if (cl->hasRectClip) {
        // currently all painting functions clips to deviceRect internally
        if (cl->clipRect == deviceRect)
            return true;

        // inline contains() for performance (we know the rects are normalized)
        const QRect &r1 = cl->clipRect;
        return (r.left() >= r1.left() && r.right() <= r1.right()
                && r.top() >= r1.top() && r.bottom() <= r1.bottom());
    } else {
        return qt_region_strictContains(cl->clipRegion, r);
    }
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 2927, as _ZNK25QRasterPaintEnginePrivate11isUnclippedERK5QRecti
inline bool QRasterPaintEnginePrivate::isUnclipped(const QRect &rect,
                                            int penWidth) const
{
    Q_Q(const QRasterPaintEngine);
    const QRasterPaintEngineState *s = q->state();
    const QClipData *cl = clip();
    QRect r = rect.normalized();
    if (!cl) {
        // inline contains() for performance (we know the rects are normalized)
        const QRect &r1 = deviceRect;
        return (r.left() >= r1.left() && r.right() <= r1.right()
                && r.top() >= r1.top() && r.bottom() <= r1.bottom());
    }


    // currently all painting functions that call this function clip to deviceRect internally
    if (cl->hasRectClip && cl->clipRect == deviceRect)
        return true;

    if (s->flags.antialiased)
        ++penWidth;

    if (penWidth > 0) {
        r.setX(r.x() - penWidth);
        r.setY(r.y() - penWidth);
        r.setWidth(r.width() + 2 * penWidth);
        r.setHeight(r.height() + 2 * penWidth);
    }

    if (cl->hasRectClip) {
        // inline contains() for performance (we know the rects are normalized)
        const QRect &r1 = cl->clipRect;
        return (r.left() >= r1.left() && r.right() <= r1.right()
                && r.top() >= r1.top() && r.bottom() <= r1.bottom());
    } else {
        return qt_region_strictContains(cl->clipRegion, r);
    }
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 2966, as _ZNK25QRasterPaintEnginePrivate11isUnclippedERK6QRectFi
inline bool QRasterPaintEnginePrivate::isUnclipped(const QRectF &rect,
                                                   int penWidth) const
{
    const QRectF norm = rect.normalized();
    if (norm.left() <= qreal(INT_MIN) || norm.top() <= qreal(INT_MIN)
            || norm.right() > qreal(INT_MAX) || norm.bottom() > qreal(INT_MAX)
            || norm.width() > qreal(INT_MAX) || norm.height() > qreal(INT_MAX))
        return false;
    return isUnclipped(norm.toAlignedRect(), penWidth);
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3681, as _ZN25QRasterPaintEnginePrivate21recalculateFastImagesEv
inline void QRasterPaintEnginePrivate::recalculateFastImages()
{
    Q_Q(QRasterPaintEngine);
    QRasterPaintEngineState *s = q->state();

    s->flags.fast_images = !(s->renderHints & QPainter::SmoothPixmapTransform)
                           && s->matrix.type() <= QTransform::TxShear;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3690, as _ZNK25QRasterPaintEnginePrivate23canUseFastImageBlendingEN8QPainter15CompositionModeERK6QImage
inline bool QRasterPaintEnginePrivate::canUseFastImageBlending(QPainter::CompositionMode mode, const QImage &image) const
{
    Q_Q(const QRasterPaintEngine);
    const QRasterPaintEngineState *s = q->state();

    return s->flags.fast_images
           && (mode == QPainter::CompositionMode_SourceOver
               || (mode == QPainter::CompositionMode_Source
                   && !image.hasAlphaChannel()));
}
//  -----------------------------------------------------------------------

//  A QRasterPaintEnginePrivate that Python can take functions over in. Every QRasterPaintEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRasterPaintEnginePrivateCall0)(const void *, int *);
typedef void * (*CuteQRasterPaintEnginePrivateCall1)(const void *, int *);
class CuteQRasterPaintEnginePrivate : public QRasterPaintEnginePrivate {
public:
  using QRasterPaintEnginePrivate::QRasterPaintEnginePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QRasterPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQRasterPaintEnginePrivateCall0 call = reinterpret_cast<CuteQRasterPaintEnginePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QRasterPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRasterPaintEnginePrivateCall1 call = reinterpret_cast<CuteQRasterPaintEnginePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }
};

//  QRasterPaintEngine *QRasterPaintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRasterPaintEngine *ritual_ZN25QRasterPaintEnginePrivate6q_funcEv(
    QRasterPaintEnginePrivate *self) {
  return self->q_func();
}

//  const QRasterPaintEngine *QRasterPaintEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRasterPaintEngine *ritual_ZNK25QRasterPaintEnginePrivate6q_funcEv(
    const QRasterPaintEnginePrivate *self) {
  return self->q_func();
}

//  QRasterPaintEnginePrivate::QRasterPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
QRasterPaintEnginePrivate *ritual_ZN25QRasterPaintEnginePrivateC1Ev() {
  return new CuteQRasterPaintEnginePrivate();
}

//  void QRasterPaintEnginePrivate::systemStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRasterPaintEnginePrivate18systemStateChangedEv(
    QRasterPaintEnginePrivate *self) {
  self->systemStateChanged();
}

//  void QRasterPaintEnginePrivate::blitImage(const QPointF &pt, const QImage
//      &img, const QRect &clip, const QRect &sr)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRasterPaintEnginePrivate9blitImageERK7QPointFRK6QImageRK5QRectS8_(
    QRasterPaintEnginePrivate *self,
    const QPointF *pt,
    const QImage *img,
    const QRect *clip,
    const QRect *sr) {
  self->blitImage(*pt, *img, *clip, *sr);
}

//  QTransform QRasterPaintEnginePrivate::brushMatrix() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK25QRasterPaintEnginePrivate11brushMatrixEv(
    const QRasterPaintEnginePrivate *self) {
  return new QTransform(self->brushMatrix());
}

//  bool QRasterPaintEnginePrivate::isUnclipped_normalized(const QRect &rect)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QRasterPaintEnginePrivate22isUnclipped_normalizedERK5QRect(
    const QRasterPaintEnginePrivate *self,
    const QRect *rect) {
  return self->isUnclipped_normalized(*rect);
}

//  bool QRasterPaintEnginePrivate::isUnclipped(const QRect &rect, int
//      penWidth) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QRasterPaintEnginePrivate11isUnclippedERK5QRecti(
    const QRasterPaintEnginePrivate *self,
    const QRect *rect,
    int penWidth) {
  return self->isUnclipped(*rect, penWidth);
}

//  bool QRasterPaintEnginePrivate::isUnclipped(const QRectF &rect, int
//      penWidth) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QRasterPaintEnginePrivate11isUnclippedERK6QRectFi(
    const QRasterPaintEnginePrivate *self,
    const QRectF *rect,
    int penWidth) {
  return self->isUnclipped(*rect, penWidth);
}

//  const QClipData *QRasterPaintEnginePrivate::clip() const
extern "C" Q_DECL_EXPORT
const QClipData *ritual_ZNK25QRasterPaintEnginePrivate4clipEv(
    const QRasterPaintEnginePrivate *self) {
  return self->clip();
}

//  void QRasterPaintEnginePrivate::recalculateFastImages()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRasterPaintEnginePrivate21recalculateFastImagesEv(
    QRasterPaintEnginePrivate *self) {
  self->recalculateFastImages();
}

//  bool QRasterPaintEnginePrivate::canUseFastImageBlending(QPainter::Composi
//      tionMode mode, const QImage &image) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QRasterPaintEnginePrivate23canUseFastImageBlendingEN8QPainter15CompositionModeERK6QImage(
    const QRasterPaintEnginePrivate *self,
    QPainter::CompositionMode mode,
    const QImage *image) {
  return self->canUseFastImageBlending(mode, *image);
}

//  a Python function taken by a CuteQRasterPaintEnginePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRasterPaintEnginePrivate(
    QRasterPaintEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRasterPaintEnginePrivate *>(self)->take(key, call);
}

//  void QRasterPaintEnginePrivate::systemStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QRasterPaintEnginePrivate18systemStateChangedEv(
    QRasterPaintEnginePrivate *self) {
  self->QRasterPaintEnginePrivate::systemStateChanged();
}
