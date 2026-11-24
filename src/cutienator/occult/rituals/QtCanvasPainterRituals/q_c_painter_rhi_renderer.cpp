//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcpainterengine_p.h"
#include "qcpainterrhirenderer_p.h"
#include "qcanvascustombrush.h"
#include "qcanvascustombrush_p.h"
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
#include "qctextlayout_p.h"
#include <QtGui/private/qdistancefield_p.h>
#endif
#include <qdebug.h>
#include <float.h>
#include <QtGui/private/qvectorpath_p.h>
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
#include "qcdistancefieldglyphcache_p.h"
#include <private/qrawfont_p.h>
#endif
#include "qcpainterengine_p.h"
#include "qcpainterrhirenderer_p.h"
#include "qcanvaspainter_p.h"
#include "qcanvascustombrush.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <QFile>
#include <QtGui/private/qvectorpath_p.h>
#include <rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 83, as _ZN15QCPainterEngine7cleanupEv
inline void QCPainterEngine::cleanup()
{
    ctx.commands.clear();
    ctx.commandsData.clear();
    ctx.paths.clear();
    ctx.points.clear();
    ctx.currentPath = nullptr;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 115, as _ZN15QCPainterEngine10beginPaintEfff
inline void QCPainterEngine::beginPaint(float logicalWidth, float logicalHeight, float dpr)
{
    ctx.states.clear();
    reset();

    setDevicePixelRatio(dpr);

    m_renderer->setViewport(0.0f, 0.0f, logicalWidth, logicalHeight);

    ctx.view = { 0.0f, 0.0f, logicalWidth, logicalHeight };
    ctx.dpr = dpr;
    ctx.customMatrixValid = false;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 129, as _ZN15QCPainterEngine15setCustomMatrixERK10QMatrix4x4
inline void QCPainterEngine::setCustomMatrix(const QMatrix4x4 &matrix)
{
    ctx.customMatrix = matrix;
    ctx.customMatrixValid = true;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 135, as _ZN15QCPainterEngine8endPaintEv
inline void QCPainterEngine::endPaint()
{
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 155, as _ZN15QCPainterEngine5resetEv
inline void QCPainterEngine::reset()
{
    state.fill = QCPaint();
    state.stroke = QCPaint();
    state.strokeWidth = 1.0f;
    state.antialias = 1.0f;
    state.miterLimit = 10.0f;
    state.lineCap = QCanvasPainter::LineCap::Butt;
    state.lineJoin = QCanvasPainter::LineJoin::Miter;
    state.compositeOperation = QCanvasPainter::CompositeOperation::SourceOver;
    state.alpha = 1.0f;
    state.brightness = 1.0f;
    state.contrast = 1.0f;
    state.saturation = 1.0f;
    state.transform.reset();
    state.brushTransform.reset();
    state.clip.extent[0] = -1.0f;
    state.clip.extent[1] = -1.0f;
    state.customFill = {};
    state.customStroke = {};
    state.textWrapMode = QCanvasPainter::WrapMode::NoWrap;
    state.textAlignment = QCanvasPainter::TextAlign::Start;
    state.textBaseline = QCanvasPainter::TextBaseline::Alphabetic;
    state.textDirection = QCanvasPainter::TextDirection::Inherit;
    state.textLineHeight = 0.0f;
    state.textAntialias = 1.0f;
    state.font = QFont();
    state.winding = QCanvasPainter::PathWinding::CounterClockWise;
    state.fillRule = QCanvasPainter::FillRule::NonZero;

    // Blending is almost always enabled, so e.g. antialiasing,
    // non-opaque colors and composition modes work.
    state.blendEnable = true;

    ctx.fontId = 0;
    ctx.colorFontId = 0;
    ctx.fontAlphaMin = -1.0f;
    ctx.fontAlphaMax = -1.0f;
    ctx.pathsCount = 0;
    ctx.pointsCount = 0;
    ctx.verticesCount = 0;
    ctx.commandsCount = 0;
    ctx.commandsDataCount = 0;
    ctx.currentPath = nullptr;
    ctx.preparedPathSerial = 0;

    ctx.states.clear();

    resetClipRect();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3025, as _ZN20QCPainterRhiRendererC1Ev
inline QCPainterRhiRenderer::QCPainterRhiRenderer()
{
    m_canvasGrabs.reserve(4);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 2758, as _ZN20QCPainterRhiRenderer15setCustomMatrixERK10QMatrix4x4
inline void QCPainterRhiRenderer::setCustomMatrix(const QMatrix4x4 &matrix)
{
    m_e->setCustomMatrix(matrix);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3298, as _ZN20QCPainterRhiRenderer18resetDebugCountersEv
inline void QCPainterRhiRenderer::resetDebugCounters()
{
    logFillDrawCallCount = 0;
    logStrokeDrawCallCount = 0;
    logTextDrawCallCount = 0;
    logFillTriCount = 0;
    logStrokeTriCount = 0;
    logTextTriCount = 0;
}
//  -----------------------------------------------------------------------

//  QCPainterRhiRenderer::QCPainterRhiRenderer()
extern "C" Q_DECL_EXPORT
QCPainterRhiRenderer *ritual_ZN20QCPainterRhiRendererC1Ev() {
  return new QCPainterRhiRenderer();
}

//  bool QCPainterRhiRenderer::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCPainterRhiRenderer7isValidEv(
    const QCPainterRhiRenderer *self) {
  return self->isValid();
}

//  QCPainterEngine *QCPainterRhiRenderer::engine()
extern "C" Q_DECL_EXPORT
QCPainterEngine *ritual_ZN20QCPainterRhiRenderer6engineEv(
    QCPainterRhiRenderer *self) {
  return self->engine();
}

//  void QCPainterRhiRenderer::setCustomMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCPainterRhiRenderer15setCustomMatrixERK10QMatrix4x4(
    QCPainterRhiRenderer *self,
    const QMatrix4x4 *matrix) {
  self->setCustomMatrix(*matrix);
}

//  void QCPainterRhiRenderer::resetDebugCounters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCPainterRhiRenderer18resetDebugCountersEv(
    QCPainterRhiRenderer *self) {
  self->resetDebugCounters();
}
