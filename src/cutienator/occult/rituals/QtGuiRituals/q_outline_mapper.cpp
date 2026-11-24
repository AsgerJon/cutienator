//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qoutlinemapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qoutlinemapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qoutlinemapper_p.h>
#include <QtGui/private/qbezier_p.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qpainterpath_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qoutlinemapper.cpp, line 41, as _ZN14QOutlineMapper11setClipRectE5QRect
inline void QOutlineMapper::setClipRect(QRect clipRect)
{
    auto limitCoords = [](QRect r) {
        const QRect limitRect(QPoint(-QT_RASTER_COORD_LIMIT, -QT_RASTER_COORD_LIMIT),
                              QPoint(QT_RASTER_COORD_LIMIT, QT_RASTER_COORD_LIMIT));
        r &= limitRect;
        r.setWidth(qMin(r.width(), QT_RASTER_COORD_LIMIT));
        r.setHeight(qMin(r.height(), QT_RASTER_COORD_LIMIT));
        return r;
    };

    if (clipRect != m_clip_rect) {
        m_clip_rect = limitCoords(clipRect);
        const int mw = 1 << 10; // margin width. No need to trigger clipping for slight overshooting
        m_clip_trigger_rect = QRectF(limitCoords(m_clip_rect.adjusted(-mw, -mw, mw, mw)));
    }
}
//  -----------------------------------------------------------------------

//  QOutlineMapper::QOutlineMapper()
extern "C" Q_DECL_EXPORT
QOutlineMapper *ritual_ZN14QOutlineMapperC1Ev() {
  return new QOutlineMapper();
}

//  void QOutlineMapper::setMatrix(const QTransform &m)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper9setMatrixERK10QTransform(
    QOutlineMapper *self,
    const QTransform *m) {
  self->setMatrix(*m);
}

//  void QOutlineMapper::setClipRect(QRect clipRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper11setClipRectE5QRect(
    QOutlineMapper *self,
    const QRect *clipRect) {
  self->setClipRect(*clipRect);
}

//  void QOutlineMapper::beginOutline(Qt::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper12beginOutlineEN2Qt8FillRuleE(
    QOutlineMapper *self,
    Qt::FillRule fillRule) {
  self->beginOutline(fillRule);
}

//  void QOutlineMapper::moveTo(const QPointF &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper6moveToERK7QPointF(
    QOutlineMapper *self,
    const QPointF *pt) {
  self->moveTo(*pt);
}

//  void QOutlineMapper::lineTo(const QPointF &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper6lineToERK7QPointF(
    QOutlineMapper *self,
    const QPointF *pt) {
  self->lineTo(*pt);
}

//  void QOutlineMapper::closeSubpath()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOutlineMapper12closeSubpathEv(QOutlineMapper *self) {
  self->closeSubpath();
}
