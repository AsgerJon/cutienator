//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_raster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>
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

//  from src/gui/painting/qpaintengine_raster.cpp, line 3782, as _ZN9QClipDataC1Ei
inline QClipData::QClipData(int height)
{
    clipSpanHeight = height;
    m_clipLines = nullptr;

    allocated = 0;
    m_spans = nullptr;
    xmin = xmax = ymin = ymax = 0;
    count = 0;

    enabled = true;
    hasRectClip = hasRegionClip = false;
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3796, as _ZN9QClipDataD1Ev
inline QClipData::~QClipData()
{
    if (m_clipLines)
        free(m_clipLines);
    if (m_spans)
        free(m_spans);
}

//  from src/gui/painting/qpaintengine_raster.cpp, line 3804, as _ZN9QClipData10initializeEv
inline void QClipData::initialize()
{
    if (m_spans)
        return;

    if (!m_clipLines)
        m_clipLines = (ClipLine *)calloc(clipSpanHeight, sizeof(ClipLine));

    Q_CHECK_PTR(m_clipLines);
    QT_TRY {
        allocated = clipSpanHeight;
        count = 0;
        QT_TRY {
            if (hasRegionClip) {
                const auto rects = clipRegion.begin();
                const int numRects = clipRegion.rectCount();
                const int maxSpans = (ymax - ymin) * numRects;
                allocated = qMax(allocated, maxSpans);
                m_spans = (QT_FT_Span *)malloc(allocated * sizeof(QT_FT_Span));
                Q_CHECK_PTR(m_spans);

                int y = 0;
                int firstInBand = 0;
                while (firstInBand < numRects) {
                    const int currMinY = rects[firstInBand].y();
                    const int currMaxY = currMinY + rects[firstInBand].height();

                    while (y < currMinY) {
                        m_clipLines[y].spans = nullptr;
                        m_clipLines[y].count = 0;
                        ++y;
                    }

                    int lastInBand = firstInBand;
                    while (lastInBand + 1 < numRects && rects[lastInBand+1].top() == y)
                        ++lastInBand;

                    while (y < currMaxY) {

                        m_clipLines[y].spans = m_spans + count;
                        m_clipLines[y].count = lastInBand - firstInBand + 1;

                        for (int r = firstInBand; r <= lastInBand; ++r) {
                            const QRect &currRect = rects[r];
                            QT_FT_Span *span = m_spans + count;
                            span->x = currRect.x();
                            span->len = currRect.width();
                            span->y = y;
                            span->coverage = 255;
                            ++count;
                        }
                        ++y;
                    }

                    firstInBand = lastInBand + 1;
                }

                Q_ASSERT(count <= allocated);

                while (y < clipSpanHeight) {
                    m_clipLines[y].spans = nullptr;
                    m_clipLines[y].count = 0;
                    ++y;
                }

                return;
            }

            m_spans = (QT_FT_Span *)malloc(allocated * sizeof(QT_FT_Span));
            Q_CHECK_PTR(m_spans);

            if (hasRectClip) {
                int y = 0;
                while (y < ymin) {
                    m_clipLines[y].spans = nullptr;
                    m_clipLines[y].count = 0;
                    ++y;
                }

                const int len = clipRect.width();
                while (y < ymax) {
                    QT_FT_Span *span = m_spans + count;
                    span->x = xmin;
                    span->len = len;
                    span->y = y;
                    span->coverage = 255;
                    ++count;

                    m_clipLines[y].spans = span;
                    m_clipLines[y].count = 1;
                    ++y;
                }

                while (y < clipSpanHeight) {
                    m_clipLines[y].spans = nullptr;
                    m_clipLines[y].count = 0;
                    ++y;
                }
            }
        } QT_CATCH(...) {
            free(m_spans); // have to free m_spans again or someone might think that we were successfully initialized.
            m_spans = nullptr;
            QT_RETHROW;
        }
    } QT_CATCH(...) {
        free(m_clipLines); // same for clipLines
        m_clipLines = nullptr;
        QT_RETHROW;
    }
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

//  from src/gui/painting/qpaintengine_raster.cpp, line 3915, as _ZN9QClipData5fixupEv
inline void QClipData::fixup()
{
    Q_ASSERT(m_spans);

    if (count == 0) {
        ymin = ymax = xmin = xmax = 0;
        return;
    }

    int y = -1;
    ymin = m_spans[0].y;
    ymax = m_spans[count-1].y + 1;
    xmin = INT_MAX;
    xmax = 0;

    const int firstLeft = m_spans[0].x;
    const int firstRight = m_spans[0].x + m_spans[0].len;
    bool isRect = true;

    for (int i = 0; i < count; ++i) {
        QT_FT_Span_& span = m_spans[i];

        if (span.y != y) {
            if (span.y != y + 1 && y != -1)
                isRect = false;
            y = span.y;
            m_clipLines[y].spans = &span;
            m_clipLines[y].count = 1;
        } else
            ++m_clipLines[y].count;

        const int spanLeft = span.x;
        const int spanRight = spanLeft + span.len;

        if (spanLeft < xmin)
            xmin = spanLeft;

        if (spanRight > xmax)
            xmax = spanRight;

        if (spanLeft != firstLeft || spanRight != firstRight)
            isRect = false;
    }

    if (isRect) {
        hasRectClip = true;
        clipRect.setRect(xmin, ymin, xmax - xmin, ymax - ymin);
    }
}
//  -----------------------------------------------------------------------

//  QClipData::QClipData(int height)
extern "C" Q_DECL_EXPORT
QClipData *ritual_ZN9QClipDataC1Ei(int height) {
  return new QClipData(height);
}

//  QClipData::~QClipData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipDataD1Ev(QClipData *self) {
  delete self;
}

//  void QClipData::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipData10initializeEv(QClipData *self) {
  self->initialize();
}

//  ClipLine *QClipData::clipLines()
extern "C" Q_DECL_EXPORT
QClipData::ClipLine *ritual_ZN9QClipData9clipLinesEv(QClipData *self) {
  return self->clipLines();
}

//  void QClipData::appendSpan(int x, int length, int y, int coverage)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipData10appendSpanEiiii(
    QClipData *self,
    int x,
    int length,
    int y,
    int coverage) {
  self->appendSpan(x, length, y, coverage);
}

//  void QClipData::setClipRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipData11setClipRectERK5QRect(
    QClipData *self,
    const QRect *rect) {
  self->setClipRect(*rect);
}

//  void QClipData::setClipRegion(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipData13setClipRegionERK7QRegion(
    QClipData *self,
    const QRegion *region) {
  self->setClipRegion(*region);
}

//  void QClipData::fixup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QClipData5fixupEv(QClipData *self) {
  self->fixup();
}
