//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdrawhelper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpaintengine_raster.cpp, line 1758, as local:qpaintengine_raster.cpp:qPremultiplyWithExtraAlpha
static QColor qPremultiplyWithExtraAlpha(const QColor &c, int alpha)
{
    if (alpha == 0)
        return Qt::transparent;
    if (c.spec() == QColor::ExtendedRgb) {
        float r, g, b, a;
        c.getRgbF(&r, &g, &b, &a);
        a = a * alpha * (1.f / 256.f);
        return QColor::fromRgbF(r * a, g * a, b * a, a);
    }
    return qPremultiply(combineAlpha256(c.rgba64(), alpha));
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 4024, as local:qpaintengine_raster.cpp:qt_intersect_spans
static const QT_FT_Span *qt_intersect_spans(const QClipData *clip, int *currentClip,
                                            const QT_FT_Span *spans, const QT_FT_Span *end,
                                            QT_FT_Span **outSpans, int available)
{
    const_cast<QClipData *>(clip)->initialize();

    QT_FT_Span *out = *outSpans;

    const QT_FT_Span *clipSpans = clip->m_spans + *currentClip;
    const QT_FT_Span *clipEnd = clip->m_spans + clip->count;

    while (available && spans < end ) {
        if (clipSpans >= clipEnd) {
            spans = end;
            break;
        }
        if (clipSpans->y > spans->y) {
            ++spans;
            continue;
        }
        if (spans->y != clipSpans->y) {
            if (spans->y < clip->count && clip->m_clipLines[spans->y].spans)
                clipSpans = clip->m_clipLines[spans->y].spans;
            else
                ++clipSpans;
            continue;
        }
        Q_ASSERT(spans->y == clipSpans->y);

        int sx1 = spans->x;
        int sx2 = sx1 + spans->len;
        int cx1 = clipSpans->x;
        int cx2 = cx1 + clipSpans->len;

        if (cx1 < sx1 && cx2 < sx1) {
            ++clipSpans;
            continue;
        } else if (sx1 < cx1 && sx2 < cx1) {
            ++spans;
            continue;
        }
        int x = qMax(sx1, cx1);
        int len = qMin(sx2, cx2) - x;
        if (len) {
            out->x = qMax(sx1, cx1);
            out->len = qMin(sx2, cx2) - out->x;
            out->y = spans->y;
            out->coverage = qt_div_255(spans->coverage * clipSpans->coverage);
            ++out;
            --available;
        }
        if (sx2 < cx2) {
            ++spans;
        } else {
            ++clipSpans;
        }
    }

    *outSpans = out;
    *currentClip = clipSpans - clip->m_spans;
    return spans;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 4087, as local:qpaintengine_raster.cpp:qt_span_fill_clipped
static void qt_span_fill_clipped(int spanCount, const QT_FT_Span *spans, void *userData)
{
//     qDebug() << "qt_span_fill_clipped" << spanCount;
    QSpanData *fillData = reinterpret_cast<QSpanData *>(userData);

    Q_ASSERT(fillData->blend && fillData->unclipped_blend);

    const int NSPANS = 512;
    Q_DECL_UNINITIALIZED QT_FT_Span cspans[NSPANS];
    int currentClip = 0;
    const QT_FT_Span *end = spans + spanCount;
    while (spans < end) {
        QT_FT_Span *clipped = cspans;
        spans = qt_intersect_spans(fillData->clip, &currentClip, spans, end, &clipped, NSPANS);
//         qDebug() << "processed " << spanCount - (end - spans) << "clipped" << clipped-cspans
//                  << "span:" << cspans->x << cspans->y << cspans->len << spans->coverage;

        if (clipped - cspans)
            fillData->unclipped_blend(clipped - cspans, cspans, fillData);
    }
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 4465, as _ZN9QSpanData4initEP13QRasterBufferPK18QRasterPaintEngine
inline void QSpanData::init(QRasterBuffer *rb, const QRasterPaintEngine *pe)
{
    rasterBuffer = rb;
    type = None;
    txop = 0;
    bilinear = false;
    m11 = m22 = m33 = 1.;
    m12 = m13 = m21 = m23 = dx = dy = 0.0;
    clip = pe ? pe->d_func()->clip() : nullptr;
}
//  -----------------------------------------------------------------------

//  QSpanData::QSpanData()
extern "C" Q_DECL_EXPORT
QSpanData *ritual_ZN9QSpanDataC1Ev() {
  return new QSpanData();
}

//  QSpanData::~QSpanData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSpanDataD1Ev(QSpanData *self) {
  delete self;
}

//  void QSpanData::init(QRasterBuffer *rb, const QRasterPaintEngine *pe)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSpanData4initEP13QRasterBufferPK18QRasterPaintEngine(
    QSpanData *self,
    QRasterBuffer *rb,
    const QRasterPaintEngine *pe) {
  self->init(rb, pe);
}
