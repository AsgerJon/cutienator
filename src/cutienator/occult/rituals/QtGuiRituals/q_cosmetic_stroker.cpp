//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcosmeticstroker_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcosmeticstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qcosmeticstroker_p.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtGui/private/qrgba64_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qcosmeticstroker.cpp, line 27, as local:qcosmeticstroker.cpp:FDot16
#if Q_PROCESSOR_WORDSIZE == 8
typedef qint64 FDot16;
#endif  // Q_PROCESSOR_WORDSIZE == 8

//  from src/gui/painting/qcosmeticstroker.cpp, line 32, as local:qcosmeticstroker.cpp:toF26Dot6
#define toF26Dot6(x) static_cast<int>((x) * 64.)

//  from src/gui/painting/qcosmeticstroker.cpp, line 119, as local:qcosmeticstroker.cpp:drawPixel
inline void drawPixel(QCosmeticStroker *stroker, int x, int y, int coverage)
{
    const QRect &cl = stroker->clip;
    if (x < cl.x() || x > cl.right() || y < cl.y() || y > cl.bottom())
        return;

    if (stroker->current_span > 0) {
        const int lastx = stroker->spans[stroker->current_span-1].x + stroker->spans[stroker->current_span-1].len ;
        const int lasty = stroker->spans[stroker->current_span-1].y;

        if (stroker->current_span == QCosmeticStroker::NSPANS || y < lasty || (y == lasty && x < lastx)) {
            stroker->blend(stroker->current_span, stroker->spans, &stroker->state->penData);
            stroker->current_span = 0;
        }
    }

    stroker->spans[stroker->current_span].x = x;
    stroker->spans[stroker->current_span].len = 1;
    stroker->spans[stroker->current_span].y = y;
    stroker->spans[stroker->current_span].coverage = coverage*stroker->opacity >> 8;
    ++stroker->current_span;
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 163, as local:qcosmeticstroker.cpp:FastDraw
enum StrokeSelection {
    Aliased = 0,
    AntiAliased = 1,
    Solid = 0,
    Dashed = 2,
    RegularDraw = 0,
    FastDraw = 4
};

//  from src/gui/painting/qcosmeticstroker.cpp, line 477, as local:qcosmeticstroker.cpp:subPath
static inline const QPainterPath::ElementType *subPath(const QPainterPath::ElementType *t, const QPainterPath::ElementType *end,
                                                 const qreal *points, bool *closed)
{
    const QPainterPath::ElementType *start = t;
    ++t;

    // find out if the subpath is closed
    while (t < end) {
        if (*t == QPainterPath::MoveToElement)
            break;
        ++t;
    }

    int offset = t - start - 1;
//    qDebug() << "subpath" << offset << points[0] << points[1] << points[2*offset] << points[2*offset+1];
    *closed = (points[0] == points[2*offset] && points[1] == points[2*offset + 1]);

    return t;
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 640, as local:qcosmeticstroker.cpp:splitCubic
static void splitCubic(QCosmeticStroker::PointF *points)
{
    const qreal half = .5;
    qreal  a, b, c, d;

    points[6].x = points[3].x;
    c = points[1].x;
    d = points[2].x;
    points[1].x = a = ( points[0].x + c ) * half;
    points[5].x = b = ( points[3].x + d ) * half;
    c = ( c + d ) * half;
    points[2].x = a = ( a + c ) * half;
    points[4].x = b = ( b + c ) * half;
    points[3].x = ( a + b ) * half;

    points[6].y = points[3].y;
    c = points[1].y;
    d = points[2].y;
    points[1].y = a = ( points[0].y + c ) * half;
    points[5].y = b = ( points[3].y + d ) * half;
    c = ( c + d ) * half;
    points[2].y = a = ( a + c ) * half;
    points[4].y = b = ( b + c ) * half;
    points[3].y = ( a + b ) * half;
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 363, as _ZN16QCosmeticStroker10drawPointsEPK6QPointi
inline void QCosmeticStroker::drawPoints(const QPoint *points, int num)
{
    const QPoint *end = points + num;
    while (points < end) {
        QPointF p = QPointF(*points) * state->matrix;
        drawPixel(this, std::floor(p.x()), std::floor(p.y()), 255);
        ++points;
    }

    blend(current_span, spans, &state->penData);
    current_span = 0;
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 619, as _ZN16QCosmeticStroker11renderCubicERK7QPointFS2_S2_S2_i
inline void QCosmeticStroker::renderCubic(const QPointF &p1, const QPointF &p2, const QPointF &p3, const QPointF &p4, int caps)
{
//    qDebug() << ">>>> renderCubic" << p1 << p2 << p3 << p4 << capString(caps);
    const int maxSubDivisions = 6;
    PointF points[3*maxSubDivisions + 4];

    points[3].x = p1.x();
    points[3].y = p1.y();
    points[2].x = p2.x();
    points[2].y = p2.y();
    points[1].x = p3.x();
    points[1].y = p3.y();
    points[0].x = p4.x();
    points[0].y = p4.y();

    PointF *p = points;
    int level = maxSubDivisions;

    renderCubicSubdivision(p, level, caps);
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 666, as _ZN16QCosmeticStroker22renderCubicSubdivisionEPNS_6PointFEii
inline void QCosmeticStroker::renderCubicSubdivision(QCosmeticStroker::PointF *points, int level, int caps)
{
    if (level) {
        qreal dx = points[3].x - points[0].x;
        qreal dy = points[3].y - points[0].y;
        qreal len = static_cast<qreal>(.25) * (qAbs(dx) + qAbs(dy));

        if (qAbs(dx * (points[0].y - points[2].y) - dy * (points[0].x - points[2].x)) >= len ||
            qAbs(dx * (points[0].y - points[1].y) - dy * (points[0].x - points[1].x)) >= len) {
            splitCubic(points);

            --level;
            renderCubicSubdivision(points + 3, level, caps & CapBegin);
            renderCubicSubdivision(points, level, caps & CapEnd);
            return;
        }
    }

    stroke(this, points[3].x, points[3].y, points[0].x, points[0].y, caps);
}

//  from src/gui/painting/qcosmeticstroker.cpp, line 287, as _ZN16QCosmeticStroker8clipLineERdS0_S0_S0_
inline bool QCosmeticStroker::clipLine(qreal &x1, qreal &y1, qreal &x2, qreal &y2)
{
    if (!qIsFinite(x1) || !qIsFinite(y1) || !qIsFinite(x2) || !qIsFinite(y2))
        return true;
    // basic/rough clipping is done in floating point coordinates to avoid
    // integer overflow problems.
    if (x1 < xmin) {
        if (x2 <= xmin)
            goto clipped;
        y1 += (y2 - y1)/(x2 - x1) * (xmin - x1);
        x1 = xmin;
    } else if (x1 > xmax) {
        if (x2 >= xmax)
            goto clipped;
        y1 += (y2 - y1)/(x2 - x1) * (xmax - x1);
        x1 = xmax;
    }
    if (x2 < xmin) {
        lastPixel.x = INT_MIN;
        y2 += (y2 - y1)/(x2 - x1) * (xmin - x2);
        x2 = xmin;
    } else if (x2 > xmax) {
        lastPixel.x = INT_MIN;
        y2 += (y2 - y1)/(x2 - x1) * (xmax - x2);
        x2 = xmax;
    }

    if (y1 < ymin) {
        if (y2 <= ymin)
            goto clipped;
        x1 += (x2 - x1)/(y2 - y1) * (ymin - y1);
        y1 = ymin;
    } else if (y1 > ymax) {
        if (y2 >= ymax)
            goto clipped;
        x1 += (x2 - x1)/(y2 - y1) * (ymax - y1);
        y1 = ymax;
    }
    if (y2 < ymin) {
        lastPixel.x = INT_MIN;
        x2 += (x2 - x1)/(y2 - y1) * (ymin - y2);
        y2 = ymin;
    } else if (y2 > ymax) {
        lastPixel.x = INT_MIN;
        x2 += (x2 - x1)/(y2 - y1) * (ymax - y2);
        y2 = ymax;
    }

    return false;

  clipped:
    lastPixel.x = INT_MIN;
    return true;
}
//  -----------------------------------------------------------------------

//  QCosmeticStroker::~QCosmeticStroker()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCosmeticStrokerD1Ev(QCosmeticStroker *self) {
  delete self;
}

//  void QCosmeticStroker::drawPoints(const QPoint *points, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCosmeticStroker10drawPointsEPK6QPointi(
    QCosmeticStroker *self,
    const QPoint *points,
    int num) {
  self->drawPoints(points, num);
}

//  void QCosmeticStroker::renderCubic(const QPointF &p1, const QPointF &p2,
//      const QPointF &p3, const QPointF &p4, int caps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCosmeticStroker11renderCubicERK7QPointFS2_S2_S2_i(
    QCosmeticStroker *self,
    const QPointF *p1,
    const QPointF *p2,
    const QPointF *p3,
    const QPointF *p4,
    int caps) {
  self->renderCubic(*p1, *p2, *p3, *p4, caps);
}

//  void QCosmeticStroker::renderCubicSubdivision(PointF *points, int level,
//      int caps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QCosmeticStroker22renderCubicSubdivisionEPNS_6PointFEii(
    QCosmeticStroker *self,
    QCosmeticStroker::PointF *points,
    int level,
    int caps) {
  self->renderCubicSubdivision(points, level, caps);
}

//  bool QCosmeticStroker::clipLine(qreal &x1, qreal &y1, qreal &x2, qreal
//      &y2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QCosmeticStroker8clipLineERdS0_S0_S0_(
    QCosmeticStroker *self,
    qreal *x1,
    qreal *y1,
    qreal *x2,
    qreal *y2) {
  return self->clipLine(*x1, *y1, *x2, *y2);
}
