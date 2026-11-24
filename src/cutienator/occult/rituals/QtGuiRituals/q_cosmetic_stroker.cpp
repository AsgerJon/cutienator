//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcosmeticstroker_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcosmeticstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qcosmeticstroker_p.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtGui/private/qrgba64_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
