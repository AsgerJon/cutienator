//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolrpaintgraphrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolrpaintgraphrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcolrpaintgraphrenderer_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qcolrpaintgraphrenderer.cpp, line 9, as _ZN23QColrPaintGraphRendererD1Ev
inline QColrPaintGraphRenderer::~QColrPaintGraphRenderer()
{
    Q_ASSERT(m_oldPaths.isEmpty());
    Q_ASSERT(m_oldTransforms.isEmpty());

    delete m_painter;
}
//  -----------------------------------------------------------------------

//  QColrPaintGraphRenderer::~QColrPaintGraphRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRendererD1Ev(QColrPaintGraphRenderer *self) {
  delete self;
}

//  void QColrPaintGraphRenderer::setBoundingRect(QRectF boundingRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QColrPaintGraphRenderer15setBoundingRectE6QRectF(
    QColrPaintGraphRenderer *self,
    const QRectF *boundingRect) {
  self->setBoundingRect(*boundingRect);
}

//  QRectF QColrPaintGraphRenderer::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QColrPaintGraphRenderer12boundingRectEv(
    const QColrPaintGraphRenderer *self) {
  return new QRectF(self->boundingRect());
}

//  QTransform QColrPaintGraphRenderer::currentTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK23QColrPaintGraphRenderer16currentTransformEv(
    const QColrPaintGraphRenderer *self) {
  return new QTransform(self->currentTransform());
}

//  QPainterPath QColrPaintGraphRenderer::currentPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK23QColrPaintGraphRenderer11currentPathEv(
    const QColrPaintGraphRenderer *self) {
  return new QPainterPath(self->currentPath());
}

//  bool QColrPaintGraphRenderer::isRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QColrPaintGraphRenderer11isRenderingEv(
    const QColrPaintGraphRenderer *self) {
  return self->isRendering();
}
