//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterengine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterengineutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcpainterengine_p.h>
#include <QtCanvasPainter/private/qcpainterrhirenderer_p.h>
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <QtCanvasPainter/private/qcanvascustombrush_p.h>
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
#include <QtCanvasPainter/private/qctextlayout_p.h>
#include <QtGui/private/qdistancefield_p.h>
#endif
#include <QtCore/qdebug.h>
#include <float.h>
#include <QtGui/private/qvectorpath_p.h>
#include <QtCanvasPainter/private/qctextlayout_p.h>
#include <QtGui/QTransform>
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
#include <QtCanvasPainter/private/qcdistancefieldglyphcache_p.h>
#include <QtGui/private/qrawfont_p.h>
#endif
#include <QtCanvasPainter/private/qcpainterengine_p.h>
#include <QtCanvasPainter/private/qcpainterrhirenderer_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <QtCore/QFile>
#include <QtGui/private/qvectorpath_p.h>
#include <QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 26, as local:qcpainterengine.cpp:QCPAINTER_INITIAL_COMMANDS_SIZE
#define QCPAINTER_INITIAL_COMMANDS_SIZE 256

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 29, as local:qcpainterengine.cpp:QCPAINTER_INITIAL_COMMANDS_DATA_SIZE
#define QCPAINTER_INITIAL_COMMANDS_DATA_SIZE 512

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 32, as local:qcpainterengine.cpp:QCPAINTER_INITIAL_VERTICES_SIZE
#define QCPAINTER_INITIAL_VERTICES_SIZE 4096

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 35, as local:qcpainterengine.cpp:QCPAINTER_INITIAL_POINTS_SIZE
#define QCPAINTER_INITIAL_POINTS_SIZE 1024

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 38, as local:qcpainterengine.cpp:QCPAINTER_INITIAL_PATHS_SIZE
#define QCPAINTER_INITIAL_PATHS_SIZE 64

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 41, as local:qcpainterengine.cpp:QCPAINTER_MAX_STATES
#define QCPAINTER_MAX_STATES 32

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 45, as local:qcpainterengine.cpp:QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY
#define QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY (64 * 1024)

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 52, as local:qcpainterengine.cpp:QCPAINTER_MAX_STROKE_WIDTH
static const float QCPAINTER_MAX_STROKE_WIDTH = 1000.0f;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 53, as local:qcpainterengine.cpp:QCPAINTER_MAX_ANTIALIAS_WIDTH
static const float QCPAINTER_MAX_ANTIALIAS_WIDTH = 10.0f;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 54, as local:qcpainterengine.cpp:QCPAINTER_MAX_TESSELLATION_LEVEL
static const int QCPAINTER_MAX_TESSELLATION_LEVEL = 11;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 55, as local:qcpainterengine.cpp:QCPAINTER_ANTIALIAS_MULTIPLIER
static const float QCPAINTER_ANTIALIAS_MULTIPLIER = 1.25f;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 59, as local:qcpainterengine.cpp:qt_qc_envFloat
static float qt_qc_envFloat(const char *name, float defaultValue)
{
    if (Q_LIKELY(!qEnvironmentVariableIsSet(name)))
        return defaultValue;
    bool ok = false;
    const float value = qgetenv(name).toFloat(&ok);
    return ok ? value : defaultValue;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1446, as local:qcpainterengine.cpp:triarea2
static constexpr float triarea2(float ax, float ay, float bx, float by, float cx, float cy) noexcept
{
    const float abx = bx - ax;
    const float aby = by - ay;
    const float acx = cx - ax;
    const float acy = cy - ay;
    return (acx * aby) - (abx * acy);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1945, as local:qcpainterengine.cpp:adjustBevel
static void adjustBevel(bool innerBevel, const QCPoint &p0, const QCPoint &p1, float w,
                        float* x0, float* y0, float* x1, float* y1)
{
    if (innerBevel) {
        *x0 = p1.x + p0.dy * w;
        *y0 = p1.y - p0.dx * w;
        *x1 = p1.x + p1.dy * w;
        *y1 = p1.y - p1.dx * w;
    } else {
        *x0 = p1.x + p1.dmx * w;
        *y0 = p1.y + p1.dmy * w;
        *x1 = p1.x + p1.dmx * w;
        *y1 = p1.y + p1.dmy * w;
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2405, as local:qcpainterengine.cpp:thresholdFunc
#if !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
static float thresholdFunc(float glyphScale)
{
    static const float base = qt_qc_envFloat("QT_DF_BASE", 0.5f);
    static const float baseDev = qt_qc_envFloat("QT_DF_BASEDEVIATION", 0.065f);
    static const float devScaleMin = qt_qc_envFloat("QT_DF_SCALEFORMAXDEV", 0.15f);
    static const float devScaleMax = qt_qc_envFloat("QT_DF_SCALEFORNODEV", 0.3f);
    return base - ((qBound(devScaleMin, glyphScale, devScaleMax) - devScaleMin) / (devScaleMax - devScaleMin) * -baseDev + baseDev);
}
#endif  // !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2414, as local:qcpainterengine.cpp:spreadFunc
#if !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
static float spreadFunc(float glyphScale)
{
    static const float range = qt_qc_envFloat("QT_DF_RANGE", 0.06f);
    return range / glyphScale;
}
#endif  // !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 81, as local:qcpainterrhirenderer.cpp:QCRHICallType
enum QCRHICallType {
    CallFill,
    CallConvexFill,
    CallStroke,
    CallText, // This call and all below do not use paths
    CallStencilClip,
    CallClearStencil,
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 90, as local:qcpainterrhirenderer.cpp:QCRHIBlend
struct QCRHIBlend
{
    bool enable;
    QRhiGraphicsPipeline::BlendFactor srcRGB;
    QRhiGraphicsPipeline::BlendFactor dstRGB;
    QRhiGraphicsPipeline::BlendFactor srcAlpha;
    QRhiGraphicsPipeline::BlendFactor dstAlpha;
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 101, as local:qcpainterrhirenderer.cpp:QCRHICall
struct QCRHICall {
    QCRHICallType type;
    int image;
    int font;
    int pathOffset;
    int pathCount;
    int indexOffset;
    int indexCount;
    int triangleOffset;
    int triangleCount;
    int commonUniformBufferOffset;
    int vertUniformBufferOffset;
    QCPainterRhiRenderer::RenderFlags renderFlags;
    QRhiScissor scissor;
    QCRHIBlend blendFunc;
    QRhiShaderResourceBindings *srb[2];
    QRhiGraphicsPipeline *ps[4];
    QShader customFragShader;
    QShader customVertShader;
    quint64 pathGroupEntryId;
    int pathGroup = -1; // non-zero default
    QCanvasPainter::FillRule fillRule;
    quint8 stencilRef;
    uint simplePathFill : 1;
    uint textTriangleOffsetBakedInToIndices : 1;
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 135, as local:qcpainterrhirenderer.cpp:QCRHIVertUniforms
struct QCRHIVertUniforms {
    // Total size 256 bytes.
    // This is often the minimum uniform buffer offset alignment.
    float vertMat[12]; // matrices are actually 3 vec4s
    float unused[52];
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 321, as local:qcpainterrhirenderer.cpp:QCRHISrbKey
struct QCRHISrbKey {
    int passId;
    int imageId;
    int fontId;
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1306, as _ZN15QCPainterEngine19setDevicePixelRatioEf
inline void QCPainterEngine::setDevicePixelRatio(float ratio)
{
    if (ratio > 0.0f) {
        static const float tessTol = qt_qc_envFloat("QCPAINTER_TESSELLATION_TOLERANCE", 0.25f);
        ctx.tessTol = tessTol / ratio;
        ctx.divsTol = 0.25f / ratio;
        ctx.distTol = 0.01f / ratio;
        // Note: This is not called during the paint operations,
        // so it can set antialias to default value.
        state.antialias = QCPAINTER_ANTIALIAS_MULTIPLIER / ratio;
        ctx.devicePxRatio = ratio;
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1961, as _ZN15QCPainterEngine12addBevelJoinERK7QCPointS2_ffff
inline void QCPainterEngine::addBevelJoin(const QCPoint &p0, const QCPoint &p1,
                                      float lw, float rw, float lu, float ru)
{
    float dlx0 = p0.dy;
    float dly0 = -p0.dx;
    float dlx1 = p1.dy;
    float dly1 = -p1.dx;
    if (p1.flags & PointLeft) {
        float lx0, ly0, lx1, ly1;
        adjustBevel(p1.flags & PointInnerBevel, p0, p1, lw, &lx0, &ly0, &lx1, &ly1);
        addVert(lx0, ly0, lu, 1.0f);
        addVert(p1.x - (dlx0 * rw), p1.y - (dly0 * rw), ru, 1.0f);

        if (p1.flags & PointBevel) {
#ifdef QCPAINTER_FAST_BEVEL_CALCULATIONS
            addVert(lx0, ly0, lu, 1.0f);
            addVert(p1.x - (dlx0 * rw), p1.y - (dly0 * rw), ru, 1.0f);
#else
            float a0 = std::atan2(-dly0, -dlx0);
            float a1 = std::atan2(-dly1, -dlx1);
            if (a1 > a0) a1 -= float(M_PI) * 2;
            for (int i = 0; i < 2; i++) {
                // No extra divs with bevel joins
                float a = a0 + float(i) * (a1 - a0);
                float rx = p1.x + std::cos(a) * rw;
                float ry = p1.y + std::sin(a) * rw;
                addVert(p1.x, p1.y, 0.5f, 1.0f);
                addVert(rx, ry, ru, 1.0f);
            }
#endif
            addVert(lx1, ly1, lu, 1.0f);
            addVert(p1.x - (dlx1 * rw), p1.y - (dly1 * rw), ru, 1.0f);
        } else {
            float rx0 = p1.x - (p1.dmx * rw);
            float ry0 = p1.y - (p1.dmy * rw);
            addVert(p1.x, p1.y, 0.5f, 1.0f);
            addVert(p1.x - (dlx0 * rw), p1.y - (dly0 * rw), ru, 1.0f);
            addVert(rx0, ry0, ru, 1.0f);
            addVert(rx0, ry0, ru, 1.0f);
            addVert(p1.x, p1.y, 0.5f, 1.0f);
            addVert(p1.x - (dlx1 * rw), p1.y - (dly1 * rw), ru, 1.0f);
        }
        addVert(lx1, ly1, lu, 1.0f);
        addVert(p1.x - (dlx1 * rw), p1.y - (dly1 * rw), ru, 1.0f);
    } else {
        float rx0, ry0, rx1, ry1;
        adjustBevel(p1.flags & PointInnerBevel, p0, p1, -rw, &rx0, &ry0, &rx1, &ry1);
        addVert(p1.x + (dlx0 * lw), p1.y + (dly0 * lw), lu, 1.0f);
        addVert(rx0, ry0, ru, 1.0f);

        if (p1.flags & PointBevel) {
#ifdef QCPAINTER_FAST_BEVEL_CALCULATIONS
            addVert(p1.x + (dlx0 * lw), p1.y + (dly0 * lw), lu, 1.0f);
            addVert(rx0, ry0, ru, 1.0f);
#else
            float a0 = std::atan2(dly0, dlx0);
            float a1 = std::atan2(dly1, dlx1);
            if (a1 < a0) a1 += float(M_PI) * 2;
            for (int i = 0; i < 2; i++) {
                // No extra divs with bevel joins
                float a = a0 + float(i) * (a1 - a0);
                float lx = p1.x + std::cos(a) * lw;
                float ly = p1.y + std::sin(a) * lw;
                addVert(lx, ly, lu, 1.0f);
                addVert(p1.x, p1.y, 0.5f, 1.0f);
            }
#endif
            addVert(p1.x + (dlx1 * lw), p1.y + (dly1 * lw), lu, 1.0f);
            addVert(rx1, ry1, ru, 1.0f);
        } else {
            float lx0 = p1.x + (p1.dmx * lw);
            float ly0 = p1.y + (p1.dmy * lw);
            addVert(p1.x + (dlx0 * lw), p1.y + (dly0 * lw), lu, 1.0f);
            addVert(p1.x, p1.y, 0.5f, 1.0f);

            addVert(lx0, ly0, lu, 1.0f);
            addVert(lx0, ly0, lu, 1.0f);

            addVert(p1.x + (dlx1 * lw), p1.y + (dly1 * lw), lu, 1.0f);
            addVert(p1.x, p1.y, 0.5f, 1.0f);
        }
        addVert(p1.x + (dlx1 * lw), p1.y + (dly1 * lw), lu, 1.0f);
        addVert(rx1, ry1, ru, 1.0f);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2047, as _ZN15QCPainterEngine12addRoundJoinERK7QCPointS2_ffffi
inline void QCPainterEngine::addRoundJoin(const QCPoint &p0, const QCPoint &p1,
                                      float lw, float rw, float lu, float ru,
                                      int roundDivs)
{
    float dlx0 = p0.dy;
    float dly0 = -p0.dx;
    float dlx1 = p1.dy;
    float dly1 = -p1.dx;
    if (p1.flags & PointLeft) {
        float lx0, ly0, lx1, ly1;
        adjustBevel(p1.flags & PointInnerBevel, p0, p1, lw, &lx0, &ly0, &lx1, &ly1);
        float a0 = std::atan2(-dly0, -dlx0);
        float a1 = std::atan2(-dly1, -dlx1);
        if (a1 > a0) a1 -= float(M_PI) * 2;

        addVert(lx0, ly0, lu, 1.0f);
        addVert(p1.x - (dlx0 * rw), p1.y - (dly0 * rw), ru, 1.0f);

        int divs = qCeil((a0 - a1) / M_PI) * roundDivs;
        divs = std::clamp(divs, 2, roundDivs);
        for (int i = 0; i < divs; i++) {
            float u = i / float(divs - 1);
            float a = a0 + u * (a1 - a0);
            float rx = p1.x + std::cos(a) * rw;
            float ry = p1.y + std::sin(a) * rw;
            addVert(p1.x, p1.y, 0.5f, 1.0f);
            addVert(rx, ry, ru, 1.0f);
        }

        addVert(lx1, ly1, lu, 1.0f);
        addVert(p1.x - dlx1 * rw, p1.y - dly1 * rw, ru, 1.0f);

    } else {
        float rx0,ry0,rx1,ry1;
        adjustBevel(p1.flags & PointInnerBevel, p0, p1, -rw, &rx0, &ry0, &rx1, &ry1);
        float a0 = std::atan2(dly0, dlx0);
        float a1 = std::atan2(dly1, dlx1);
        if (a1 < a0) a1 += float(M_PI) * 2;

        addVert(p1.x + dlx0 * rw, p1.y + dly0 * rw, lu, 1.0f);
        addVert(rx0, ry0, ru, 1.0f);

        int divs = qCeil((a1 - a0) / M_PI) * roundDivs;
        divs = std::clamp(divs, 2, roundDivs);
        for (int i = 0; i < divs; i++) {
            float u = i / float(divs - 1);
            float a = a0 + u * (a1 - a0);
            float lx = p1.x + std::cos(a) * lw;
            float ly = p1.y + std::sin(a) * lw;
            addVert(lx, ly, lu, 1.0f);
            addVert(p1.x, p1.y, 0.5f, 1.0f);
        }

        addVert(p1.x + dlx1 * rw, p1.y + dly1 * rw, lu, 1.0f);
        addVert(rx1, ry1, ru, 1.0f);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2332, as _ZN15QCPainterEngine14getStrokePaintEPfb
inline QCPaint QCPainterEngine::getStrokePaint(float *strokeWidth, bool ignoreTransform)
{
    float scale = getAverageScale(state.transform);
    *strokeWidth = std::clamp(state.strokeWidth * scale, 0.0f, QCPAINTER_MAX_STROKE_WIDTH);
    float expa = 1.0f;
    if (*strokeWidth < state.antialias) {
        // If the stroke width is less than pixel size, use alpha to emulate coverage.
        float alpha = std::clamp((*strokeWidth * QCPAINTER_ANTIALIAS_MULTIPLIER) / state.antialias, 0.0f, 1.0f);
        // Since coverage is area, scale by alpha*alpha.
        expa = alpha * alpha;
        *strokeWidth = state.antialias;
    }

    QCPaint strokePaint = state.stroke;
    strokePaint.alpha = state.alpha * expa;
    // Apply current transform and optional brush transform
    if (!ignoreTransform &&
        strokePaint.brushType != BrushColor &&
        !(state.transform.isIdentity() && state.brushTransform.isIdentity())) {
        strokePaint.transform *= (state.brushTransform * state.transform);
    }
    return strokePaint;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1134, as _ZN15QCPainterEngine16renderFilledTextEi
#if !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
inline void QCPainterEngine::renderFilledText(int fontTex)
{
    // Monochrome (SDF) glyphs and text decorations.
    if (!textVertices.empty()) {
        const QCPaint p = getFillPaint();
        ctx.fontId = fontTex;
        updateStateFontVars();

        // Decoration rects (underline/overline/strikeout) are appended to
        // textVertices/textIndices by the glyph cache with a texCoord pointing
        // into a reserved 0xFF region of the SDF atlas, so they participate in
        // this same draw call and pick up the same shader as the glyphs.
        if (state.customFill.type() != QCanvasBrush::BrushType::Custom) {
            m_renderer->renderTextFill(p, state, textVertices, textIndices);
        } else {
            // Using custom brush. Avoid detaching the brush.
            auto *customPriv = static_cast<QCanvasCustomBrushPrivate *>(
                    QCanvasBrushPrivate::get(std::as_const(state.customFill)));
            m_renderer->renderTextFillCustom(
                    p, state, customPriv, textVertices, textIndices);
        }
    }

    // Color (emoji) glyphs are drawn by samppling the color atlas directly, so
    // they keep their native colors instead of being tinted by the fill.
    auto colorTex = m_renderer->populateColorFont(colorTextVertices, colorTextIndices);
    if (colorTex != 0 && !colorTextVertices.empty()) {
        ctx.colorFontId = colorTex;
        m_renderer->renderTextFill({}, state, colorTextVertices, colorTextIndices, true);
    }

    // simple memory usage cap; drawing huge texts will not reuse the containers (and their allocations)
    if (textVertices.capacity() > QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY)
        textVertices = {};
    if (textIndices.capacity() > QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY)
        textIndices = {};
    if (colorTextVertices.capacity() > QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY)
        colorTextVertices = {};
    if (colorTextIndices.capacity() > QCPAINTER_TEXT_VERTEX_INDEX_LIST_REUSE_CAPACITY)
        colorTextIndices = {};
}
#endif  // !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 11, as _ZN12QCTextLayout19convertToQtWrapModeEN14QCanvasPainter8WrapModeE
inline QTextOption::WrapMode QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)
{
    switch (mode) {
    case QCanvasPainter::WrapMode::NoWrap:
        return QTextOption::NoWrap;
        break;
    case QCanvasPainter::WrapMode::Wrap:
        return QTextOption::WrapAtWordBoundaryOrAnywhere;
        break;
    case QCanvasPainter::WrapMode::WordWrap:
        return QTextOption::WordWrap;
        break;
    case QCanvasPainter::WrapMode::WrapAnywhere:
        return QTextOption::WrapAnywhere;
        break;
    }
    return QTextOption::NoWrap;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 30, as _ZN12QCTextLayout20convertToQtAlignmentEN14QCanvasPainter9TextAlignE
inline Qt::Alignment QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign alignment)
{
    switch (alignment) {
    case QCanvasPainter::TextAlign::Left:
        return Qt::AlignLeft;
        break;
    case QCanvasPainter::TextAlign::Center:
        return Qt::AlignCenter;
        break;
    case QCanvasPainter::TextAlign::Right:
        return Qt::AlignRight;
        break;
    default:
        break;
    }
    return Qt::AlignLeft;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 48, as _ZN12QCTextLayout26calculateVerticalAlignmentEN14QCanvasPainter12TextBaselineERK6QRectFRK13QFontMetricsFS4_
inline float QCTextLayout::calculateVerticalAlignment(QCanvasPainter::TextBaseline baseline, const QRectF &rect,
                                               const QFontMetricsF &metrics, const QRectF &layoutRect)
{
    float offset = 0;
    switch (baseline) {
    case QCanvasPainter::TextBaseline::Top:
        break;
    case QCanvasPainter::TextBaseline::Hanging:
        offset = -metrics.height() + metrics.ascent();
        break;
    case QCanvasPainter::TextBaseline::Middle:
        offset = rect.height() * 0.5 - layoutRect.height() * 0.5;
        break;
    case QCanvasPainter::TextBaseline::Alphabetic:
        offset = rect.height() - layoutRect.height() + metrics.descent();
        break;
    case QCanvasPainter::TextBaseline::Bottom:
        offset = rect.height() - layoutRect.height();
        break;
    }

    return offset;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 72, as _ZN12QCTextLayout28calculateHorizontalAlignmentEN14QCanvasPainter9TextAlignERK6QRectFfS4_
inline std::pair<float, float> QCTextLayout::calculateHorizontalAlignment(QCanvasPainter::TextAlign align,
                                                                   const QRectF &rect,
                                                                   float layoutWidth,
                                                                   const QRectF &layoutRect)
{
    float offset1 = 0;
    float offset2 = 0;
    float paddingOffset = (layoutRect.width() - layoutWidth);
    float alignOffset = (rect.width() - layoutRect.width());
    switch (align) {
    case QCanvasPainter::TextAlign::Left:
        offset2 = -paddingOffset;
        break;
    case QCanvasPainter::TextAlign::Right:
        offset1 = paddingOffset + alignOffset;
        offset2 = alignOffset;
        break;
    case QCanvasPainter::TextAlign::Center:
        offset1 = (alignOffset + paddingOffset) * 0.5f;
        offset2 = (alignOffset - paddingOffset) * 0.5f;
        break;
    case QCanvasPainter::TextAlign::Start:
    case QCanvasPainter::TextAlign::End:
    default:
        break;
    }
    return { offset1, offset2 };
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 106, as _ZN15QCPainterEngineC1Ev
inline QCPainterEngine::QCPainterEngine()
{
#ifdef QCPAINTER_PERF_DEBUG
    perf.start();
#endif
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 139, as _ZN15QCPainterEngine4saveEv
inline void QCPainterEngine::save()
{
    if (ctx.states.size() >= QCPAINTER_MAX_STATES) {
        qWarning() << "Maximum amount of states reached";
        return;
    }
    ctx.states << state;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 148, as _ZN15QCPainterEngine7restoreEv
inline void QCPainterEngine::restore()
{
    if (ctx.states.isEmpty())
        return;
    state = ctx.states.takeLast();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 209, as _ZN15QCPainterEngine14setStrokeColorE6QColor
inline void QCPainterEngine::setStrokeColor(QColor color)
{
    // Reset other variables
    state.stroke.brushType = BrushColor;
    //state.stroke.transform.reset();
    state.stroke.imageId = 0;
    state.stroke.radius = 0.0f;
    state.stroke.feather = 1.0f;
    // Set inner and outer color
    state.stroke.innerColor = { color.redF(), color.greenF(), color.blueF(), color.alphaF() };
    state.stroke.outerColor = state.stroke.innerColor;
    state.customStroke = {};
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 223, as _ZN15QCPainterEngine14setStrokePaintERK7QCPaint
inline void QCPainterEngine::setStrokePaint(const QCPaint &paint)
{
    state.stroke = paint;
    state.customStroke = {};
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 229, as _ZN15QCPainterEngine12setFillColorE6QColor
inline void QCPainterEngine::setFillColor(QColor color)
{
    // Reset other variables
    state.fill.brushType = BrushColor;
    //state.fill.transform.reset();
    state.fill.imageId = 0;
    state.fill.radius = 0.0f;
    state.fill.feather = 1.0f;
    // Set inner and outer color
    state.fill.innerColor = { color.redF(), color.greenF(), color.blueF(), color.alphaF() };
    state.fill.outerColor = state.fill.innerColor;
    state.customFill = {};
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 243, as _ZN15QCPainterEngine12setFillPaintERK7QCPaint
inline void QCPainterEngine::setFillPaint(const QCPaint &paint)
{
    state.fill = paint;
    state.customFill = {};
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 249, as _ZN15QCPainterEngine12setLineWidthEf
inline void QCPainterEngine::setLineWidth(float width)
{
    state.strokeWidth = width;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 254, as _ZN15QCPainterEngine10setLineCapEN14QCanvasPainter7LineCapE
inline void QCPainterEngine::setLineCap(QCanvasPainter::LineCap lineCap)
{
    state.lineCap = lineCap;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 259, as _ZN15QCPainterEngine11setLineJoinEN14QCanvasPainter8LineJoinE
inline void QCPainterEngine::setLineJoin(QCanvasPainter::LineJoin lineJoin)
{
    state.lineJoin = lineJoin;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 264, as _ZN15QCPainterEngine14setGlobalAlphaEf
inline void QCPainterEngine::setGlobalAlpha(float alpha)
{
    state.alpha = alpha;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 269, as _ZN15QCPainterEngine19setGlobalBrightnessEf
inline void QCPainterEngine::setGlobalBrightness(float value)
{
    state.brightness = value;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 274, as _ZN15QCPainterEngine17setGlobalContrastEf
inline void QCPainterEngine::setGlobalContrast(float value)
{
    state.contrast = value;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 279, as _ZN15QCPainterEngine19setGlobalSaturationEf
inline void QCPainterEngine::setGlobalSaturation(float value)
{
    state.saturation = value;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 284, as _ZN15QCPainterEngine11setFillRuleEN14QCanvasPainter8FillRuleE
inline void QCPainterEngine::setFillRule(QCanvasPainter::FillRule fillRule)
{
    state.fillRule = fillRule;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 289, as _ZNK15QCPainterEngine8fillRuleEv
inline QCanvasPainter::FillRule QCPainterEngine::fillRule() const
{
    return state.fillRule;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 296, as _ZN15QCPainterEngine20setCustomStrokeBrushERK12QCanvasBrush
inline void QCPainterEngine::setCustomStrokeBrush(const QCanvasBrush &brush)
{
    state.customStroke = brush;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 301, as _ZN15QCPainterEngine18setCustomFillBrushERK12QCanvasBrush
inline void QCPainterEngine::setCustomFillBrush(const QCanvasBrush &brush)
{
    state.customFill = brush;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 308, as _ZNK15QCPainterEngine16currentTransformEv
inline QTransform QCPainterEngine::currentTransform() const
{
    return state.transform;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 313, as _ZN15QCPainterEngine9transformERK10QTransform
inline void QCPainterEngine::transform(const QTransform &transform)
{
    state.transform = transform * state.transform;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 318, as _ZN15QCPainterEngine12setTransformERK10QTransform
inline void QCPainterEngine::setTransform(const QTransform &transform)
{
    state.transform = transform;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 323, as _ZN15QCPainterEngine14resetTransformEv
inline void QCPainterEngine::resetTransform()
{
    state.transform.reset();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 328, as _ZN15QCPainterEngine9translateEff
inline void QCPainterEngine::translate(float x, float y)
{
    state.transform = state.transform.translate(x, y);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 333, as _ZN15QCPainterEngine5scaleEff
inline void QCPainterEngine::scale(float x, float y)
{
    state.transform = state.transform.scale(x, y);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 338, as _ZN15QCPainterEngine6rotateEf
inline void QCPainterEngine::rotate(float angle)
{
    state.transform = state.transform.rotateRadians(angle);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 343, as _ZN15QCPainterEngine4skewEff
inline void QCPainterEngine::skew(float angleX, float angleY)
{
    state.transform = state.transform.shear(angleX, angleY);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 348, as _ZN15QCPainterEngine17setBrushTransformERK10QTransform
inline void QCPainterEngine::setBrushTransform(const QTransform &transform)
{
    state.brushTransform = transform;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 400, as _ZN15QCPainterEngine18createImagePatternEffffif6QColor
inline QCPaint QCPainterEngine::createImagePattern(float x, float y, float width, float height,
                                            int imageId, float angle, QColor tintColor)
{
    QCPaint p;
    p.brushType = BrushImage;
    p.transform = p.transform.translate(x, y);
    if (!qFuzzyIsNull(angle))
        p.transform = p.transform.rotateRadians(angle);

    p.extent[0] = width;
    p.extent[1] = height;

    p.imageId = imageId;

    p.innerColor = { tintColor.redF(), tintColor.greenF(), tintColor.blueF(), tintColor.alphaF() };
    // Not used currently
    //p.outerColor = WHITE_COLOR;

    return p;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 423, as _ZN15QCPainterEngine9beginPathEv
inline void QCPainterEngine::beginPath()
{
    ctx.commandsCount = 0;
    ctx.commandsDataCount = 0;
    ctx.pathsCount = 0;
    ctx.pointsCount = 0;
    ctx.currentPath = nullptr;
    ctx.preparedPathSerial = 0;
    ctx.verticesCount = 0;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 434, as _ZN15QCPainterEngine9closePathEv
inline void QCPainterEngine::closePath()
{
    appendCommand(QCCommand::Close);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 439, as _ZN15QCPainterEngine6moveToEff
inline void QCPainterEngine::moveTo(float x, float y)
{
    float data[] = { x, y };
    appendCommandsData(data, 2);
    appendCommand(QCCommand::MoveTo);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 446, as _ZN15QCPainterEngine6lineToEff
inline void QCPainterEngine::lineTo(float x, float y)
{
    float data[] = { x, y };
    appendCommandsData(data, 2);
    appendCommand(QCCommand::LineTo);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 453, as _ZN15QCPainterEngine8bezierToEffffff
inline void QCPainterEngine::bezierTo(float cp1X, float cp1Y, float cp2X, float cp2Y, float x, float y)
{
    float data[] = { cp1X, cp1Y, cp2X, cp2Y, x, y };
    appendCommandsData(data, 6);
    appendCommand(QCCommand::BezierTo);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 460, as _ZN15QCPainterEngine6quadToEffff
inline void QCPainterEngine::quadTo(float cpX, float cpY, float x, float y)
{
    // Continue from previous point
    const float prevX = ctx.prevX;
    const float prevY = ctx.prevY;
    static constexpr float m = 2.0f / 3.0f;
    float cp1X = prevX + m * (cpX - prevX);
    float cp1Y = prevY + m * (cpY - prevY);
    float cp2X = x + m * (cpX - x);
    float cp2Y = y + m * (cpY - y);
    float data[] = { cp1X, cp1Y, cp2X, cp2Y, x, y };
    appendCommandsData(data, 6);
    appendCommand(QCCommand::BezierTo);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 475, as _ZN15QCPainterEngine5arcToEfffff
inline void QCPainterEngine::arcTo(float x1, float y1, float x2, float y2, float radius)
{
    // Continue from previous point
    const float prevX = ctx.prevX;
    const float prevY = ctx.prevY;

#ifdef QCPAINTER_EQUAL_POINTS_CHECKING_ENABLED
    // See if straight line is enough
    if (pointsEquals(prevX, prevY, x1, y1, ctx.distTol) ||
        pointsEquals(x1, y1, x2, y2, ctx.distTol) ||
        pointInSegment(x1, y1, prevX, prevY, x2, y2, ctx.distTol) ||
        radius < ctx.distTol) {
        lineTo(x1, y1);
        return;
    }
#endif

    // Calculate tangential circle to lines (x0,y0)-(x1,y1) and (x1,y1)-(x2,y2).
    float dx0 = prevX - x1;
    float dy0 = prevY - y1;
    float dx1 = x2 - x1;
    float dy1 = y2 - y1;
    normalizePoint(&dx0, &dy0);
    normalizePoint(&dx1, &dy1);
    float a = std::acos(dx0 * dx1 + dy0 * dy1);
    float d = radius / std::tan(a * 0.5f);

    float cx, cy, a0, a1;
    QCanvasPainter::PathWinding direction;
    if (crossProduct(dx0, dy0, dx1, dy1) > 0.0f) {
        direction = QCanvasPainter::PathWinding::ClockWise;
        cx = x1 + dx0 * d + dy0 * radius;
        cy = y1 + dy0 * d - dx0 * radius;
        a0 = std::atan2(dx0, -dy0);
        a1 = std::atan2(-dx1, dy1);
    } else {
        direction = QCanvasPainter::PathWinding::CounterClockWise;
        cx = x1 + dx0 * d - dy0 * radius;
        cy = y1 + dy0 * d + dx0 * radius;
        a0 = std::atan2(-dx0, dy0);
        a1 = std::atan2(dx1, -dy1);
    }

    addArc(cx, cy, radius, a0, a1, direction, true);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 521, as _ZN15QCPainterEngine6addArcEfffffN14QCanvasPainter11PathWindingEb
inline void QCPainterEngine::addArc(float x, float y, float radius,
                                float a0, float a1, QCanvasPainter::PathWinding direction,
                                bool isConnected)
{
    // Clamp angles
    float da = a1 - a0;
    static constexpr float TWOPI = float(M_PI) * 2;
    if (direction == QCanvasPainter::PathWinding::ClockWise) {
        if (std::abs(da) >= TWOPI) {
            da = TWOPI;
        } else {
            while (da < 0.0f) da += TWOPI;
        }
    } else {
        if (std::abs(da) >= TWOPI) {
            da = -TWOPI;
        } else {
            while (da > 0.0f) da -= TWOPI;
        }
    }

    // Split arc into max 90 degree segments.
    const int divsCount = std::clamp(int(std::abs(da) / M_PI_2 + 0.5f), 1, 5);
    float hda = (da / float(divsCount)) * 0.5f;
    float kappa = std::abs(4.0f / 3.0f * (1.0f - std::cos(hda)) / std::sin(hda));

    if (direction == QCanvasPainter::PathWinding::CounterClockWise)
        kappa = -kappa;

    QCCommand firstCmd = ctx.commandsCount == 0 || !isConnected ? QCCommand::MoveTo : QCCommand::LineTo;
    float prevTanX = 0;
    float prevTanY = 0;
    float prevVX = 0;
    float prevVY = 0;
    // divsCount is max 5 and min 1, meaning dSize is 8..32
    const int dSize = 2 + divsCount * 6;
    QVarLengthArray<QCCommand, 6> commands(1 + divsCount);
    QVarLengthArray<float, 32> data(dSize);
    int cCount = 0;
    int dCount = 0;
    for (int i = 0; i <= divsCount; i++) {
        float a = a0 + da * (i / (float)divsCount);
        float dx = std::cos(a);
        float dy = std::sin(a);
        float vx = x + dx * radius;
        float vy = y + dy * radius;
        float tanx = -dy * radius * kappa;
        float tany = dx * radius * kappa;
        if (i == 0) {
            commands[cCount++] = firstCmd;
            data[dCount++] = vx;
            data[dCount++] = vy;
        } else {
            commands[cCount++] = QCCommand::BezierTo;
            data[dCount++] = prevVX + prevTanX;
            data[dCount++] = prevVY + prevTanY;
            data[dCount++] = vx - tanx;
            data[dCount++] = vy - tany;
            data[dCount++] = vx;
            data[dCount++] = vy;
        }
        prevVX = vx;
        prevVY = vy;
        prevTanX = tanx;
        prevTanY = tany;
    }
    appendCommandsData(data.constData(), dCount);
    appendCommands(commands.constData(), cCount);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 591, as _ZN15QCPainterEngine7addRectEffff
inline void QCPainterEngine::addRect(float x, float y, float width, float height)
{
    float data[] = {
        x, y,
        x, y + height,
        x + width, y + height,
        x + width, y
    };
    appendCommandsData(data, 8);
    static constexpr QCCommand commands[] = {
        QCCommand::MoveTo,
        QCCommand::LineTo,
        QCCommand::LineTo,
        QCCommand::LineTo,
        QCCommand::Close
    };
    appendCommands(commands, 5);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 610, as _ZN15QCPainterEngine12addRoundRectEfffff
inline void QCPainterEngine::addRoundRect(float x, float y, float width, float height, float radius)
{
    static const float MINR = 0.1f;
    const bool noRadius = (radius < MINR);
    if (noRadius) {
        addRect(x, y, width, height);
    } else {
        // The maximum radius is slightly less than half of smaller side of the rect,
        // to not grow too big even with some float rounding errors.
        const float maxRad = std::min(std::abs(width), std::abs(height)) * 0.4999f;
        const float cornerRad = std::min(radius, maxRad);
        const float rX = cornerRad * sign(width);
        const float rY = cornerRad * sign(height);
        const float xW = x + width;
        const float yH = y + height;
        const float rYCK = rY * COMP_KAPPA90;
        const float rXCK = rX * COMP_KAPPA90;
        float data[] = {
            x, y + rY,
            x, yH - rY,
            x, yH - rYCK, x + rXCK, yH, x + rX, yH,
            xW - rX, yH,
            xW - rXCK, yH, xW, yH - rYCK, xW, yH - rY,
            xW, y + rY,
            xW, y + rYCK, xW - rXCK, y, xW - rX, y,
            x + rX, y,
            x + rXCK, y, x, y + rYCK, x, y + rY
        };

        appendCommandsData(data, 34);
        static constexpr QCCommand commands[] = {
            QCCommand::MoveTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::Close
        };
        appendCommands(commands, 10);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 656, as _ZN15QCPainterEngine12addRoundRectEffffffff
inline void QCPainterEngine::addRoundRect(float x, float y, float width, float height,
                                   float radiusTopLeft, float radiusTopRight,
                                   float radiusBottomRight, float radiusBottomLeft)
{
    static const float MINR = 0.1f;
    const bool noRadius = (radiusTopLeft < MINR) && (radiusTopRight < MINR) &&
                          (radiusBottomRight < MINR) && (radiusBottomLeft < MINR);
    if (noRadius) {
        addRect(x, y, width, height);
    } else {
        const float top = std::max(MINR, radiusTopLeft + radiusTopRight);
        const float right = std::max(MINR, radiusTopRight + radiusBottomRight);
        const float bottom = std::max(MINR, radiusBottomRight + radiusBottomLeft);
        const float left = std::max(MINR, radiusBottomLeft + radiusTopLeft);
        // Find scale, if all radius don't fit. This is how canvas roundRect() behaves:
        // https://html.spec.whatwg.org/multipage/canvas.html#dom-context-2d-roundrect
        const float scale = std::min({1.0f,
                                      qAbs(width / top),
                                      qAbs(height / right),
                                      qAbs(width / bottom),
                                      qAbs(height / left)});
        const float wScale = scale * sign(width);
        const float hScale = scale * sign(height);
        const float rXBL = radiusBottomLeft * wScale;
        const float rYBL = radiusBottomLeft * hScale;
        const float rXBR = radiusBottomRight * wScale;
        const float rYBR = radiusBottomRight * hScale;
        const float rXTR = radiusTopRight * wScale;
        const float rYTR = radiusTopRight * hScale;
        const float rXTL = radiusTopLeft * wScale;
        const float rYTL = radiusTopLeft * hScale;
        const float xW = x + width;
        const float yH = y + height;
        float data[] = {
            x, y + rYTL,
            x, yH - rYBL,
            x, yH - rYBL * COMP_KAPPA90, x + rXBL * COMP_KAPPA90, yH, x + rXBL, yH,
            xW - rXBR, yH,
            xW - rXBR * COMP_KAPPA90, yH, xW, yH - rYBR * COMP_KAPPA90, xW, yH - rYBR,
            xW, y + rYTR,
            xW, y + rYTR * COMP_KAPPA90, xW - rXTR * COMP_KAPPA90, y, xW - rXTR, y,
            x + rXTL, y,
            x + rXTL * COMP_KAPPA90, y, x, y + rYTL * COMP_KAPPA90, x, y + rYTL
        };

        appendCommandsData(data, 34);
        static constexpr QCCommand commands[] = {
            QCCommand::MoveTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::LineTo,
            QCCommand::BezierTo,
            QCCommand::Close
        };
        appendCommands(commands, 10);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 718, as _ZN15QCPainterEngine10addEllipseEffff
inline void QCPainterEngine::addEllipse(float x, float y, float radiusX, float radiusY)
{
    const float radYK = radiusY * KAPPA90;
    const float radXK = radiusX * KAPPA90;
    const float ymRadY = y - radiusY;
    const float ypRadY = y + radiusY;
    const float xmRadX = x - radiusX;
    const float xpRadX = x + radiusX;
    float data[] = {
        xmRadX, y,
        xmRadX, y + radYK, x - radXK, ypRadY, x, ypRadY,
        x + radXK, ypRadY, xpRadX, y + radYK, xpRadX, y,
        xpRadX, y - radYK, x + radXK, ymRadY, x, ymRadY,
        x - radXK, ymRadY, xmRadX, y - radYK, xmRadX, y,
    };
    appendCommandsData(data, 26);
    static constexpr QCCommand commands[] = {
        QCCommand::MoveTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
    };
    appendCommands(commands, 5);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 744, as _ZN15QCPainterEngine9addCircleEfff
inline void QCPainterEngine::addCircle(float x, float y, float radius)
{
    const float radK = radius * KAPPA90;
    const float ymRad = y - radius;
    const float ypRad = y + radius;
    float data[] = {
        x - radius, y,
        x - radius, y + radK, x - radK, ypRad, x, ypRad,
        x + radK, ypRad, x + radius, y + radK, x + radius, y,
        x + radius, y - radK, x + radK, ymRad, x, ymRad,
        x - radK, ymRad, x - radius, y - radK, x - radius, y,
    };
    appendCommandsData(data, 26);
    static constexpr QCCommand commands[] = {
        QCCommand::MoveTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
        QCCommand::BezierTo,
    };
    appendCommands(commands, 5);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 767, as _ZN15QCPainterEngine7addPathERK12QPainterPath
inline void QCPainterEngine::addPath(const QPainterPath &path)
{
    const int eCount = path.elementCount();
    for (int i = 0; i < eCount; i++) {
        const auto &element = path.elementAt(i);
        switch (element.type) {
        case QPainterPath::MoveToElement:
        {
            moveTo(element.x, element.y);
            break;
        }
        case QPainterPath::LineToElement:
        {
            lineTo(element.x, element.y);
            break;
        }
        case QPainterPath::CurveToElement:
        {
            // 2 CurveToDataElements always follow the CurveToElement
            const auto &data1 = path.elementAt(++i);
            const auto &data2 = path.elementAt(++i);
            bezierTo(element.x, element.y, data1.x, data1.y, data2.x, data2.y);
            break;
        }
        case QPainterPath::CurveToDataElement:
            // Handled in CurveToElement
            break;
        }
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 808, as _ZN15QCPainterEngine14setPathWindingEN14QCanvasPainter11PathWindingE
inline void QCPainterEngine::setPathWinding(QCanvasPainter::PathWinding winding)
{
    QCCommand c = winding == QCanvasPainter::PathWinding::ClockWise ?
                      QCCommand::WindingCW : QCCommand::WindingCCW;
    appendCommand(c);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1018, as _ZN15QCPainterEngine27setGlobalCompositeOperationEN14QCanvasPainter18CompositeOperationE
inline void QCPainterEngine::setGlobalCompositeOperation(QCanvasPainter::CompositeOperation op)
{
    state.compositeOperation = op;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1097, as _ZN15QCPainterEngine15setTextWrapModeEN14QCanvasPainter8WrapModeE
inline void QCPainterEngine::setTextWrapMode(QCanvasPainter::WrapMode wrapMode)
{
    state.textWrapMode = wrapMode;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1102, as _ZN15QCPainterEngine17setTextLineHeightEf
inline void QCPainterEngine::setTextLineHeight(float height)
{
    state.textLineHeight = height;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1107, as _ZN15QCPainterEngine16setTextAntialiasEf
inline void QCPainterEngine::setTextAntialias(float antialias)
{
    state.textAntialias = antialias;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1112, as _ZN15QCPainterEngine16setTextAlignmentEN14QCanvasPainter9TextAlignE
inline void QCPainterEngine::setTextAlignment(QCanvasPainter::TextAlign align)
{
    state.textAlignment = align;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1117, as _ZN15QCPainterEngine15setTextBaselineEN14QCanvasPainter12TextBaselineE
inline void QCPainterEngine::setTextBaseline(QCanvasPainter::TextBaseline baseline)
{
    state.textBaseline = baseline;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1122, as _ZN15QCPainterEngine16setTextDirectionEN14QCanvasPainter13TextDirectionE
inline void QCPainterEngine::setTextDirection(QCanvasPainter::TextDirection direction)
{
    state.textDirection = direction;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1195, as _ZN15QCPainterEngine15textBoundingBoxERK7QStringRK6QRectF
inline QRectF QCPainterEngine::textBoundingBox(const QString &text, const QRectF &rect)
{
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
    auto &font = state.font;
    auto metrics = QFontMetricsF{font};

    // TODO: Duplicate code from QCDistanceFieldGlyphCache::generate()
    // We should move this layouting into a shared method.
    // And cache the result so that textBoundingBox() and fillText() with
    // same data don't do double layouting.
    auto option = QTextOption{};
    option.setWrapMode(QCTextLayout::convertToQtWrapMode(state.textWrapMode));
    option.setAlignment(QCTextLayout::convertToQtAlignment(effectiveTextAlign(text)));
    auto layout = QTextLayout();
    layout.clearLayout();
    layout.setTextOption(option);
    layout.setText(text);
    layout.setFont(font);
    float leading = metrics.leading();
    float layoutHeight = 0;
    float layoutWidth = 0;
    layout.beginLayout();
    while (true) {
        QTextLine line = layout.createLine();
        if (!line.isValid())
            break;

        line.setLineWidth(rect.width());
        layoutHeight += leading;
        line.setPosition(QPointF(rect.x(), rect.y() + layoutHeight));
        layoutHeight += line.height() + state.textLineHeight;
        layoutWidth = qMax(layoutWidth, line.naturalTextWidth());
    }
    layout.endLayout();

    // Adjust rect
    float textOffsetY = QCTextLayout::calculateVerticalAlignment(state.textBaseline,
                                                                 rect, metrics,
                                                                 layout.boundingRect());
    std::pair<float, float> textOffsetX =
            QCTextLayout::calculateHorizontalAlignment(effectiveTextAlign(text),
                                                       rect,layoutWidth,
                                                       layout.boundingRect());
    QRectF textRect = layout.boundingRect();
    textRect.adjust(textOffsetX.first, textOffsetY, textOffsetX.second, textOffsetY);
    return textRect;
#else
    return QRectF();
#endif
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1248, as _ZN15QCPainterEngine18resetDebugCountersEv
inline void QCPainterEngine::resetDebugCounters()
{
    m_renderer->resetDebugCounters();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1260, as _ZNK15QCPainterEngine13debugCountersEv
inline QCDebugCounters QCPainterEngine::debugCounters() const
{
    return ctx.debugCounters;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1265, as _ZN15QCPainterEngine12setAntialiasEf
inline void QCPainterEngine::setAntialias(float antialias)
{
    antialias = std::clamp(antialias, 0.0f, QCPAINTER_MAX_ANTIALIAS_WIDTH);
    state.antialias = QCPAINTER_ANTIALIAS_MULTIPLIER * antialias / ctx.devicePxRatio;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1271, as _ZN15QCPainterEngine13setMiterLimitEf
inline void QCPainterEngine::setMiterLimit(float limit)
{
    state.miterLimit = limit;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 83, as _ZN15QCPainterEngine7cleanupEv
inline void QCPainterEngine::cleanup()
{
    ctx.commands.clear();
    ctx.commandsData.clear();
    ctx.paths.clear();
    ctx.points.clear();
    ctx.currentPath = nullptr;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 92, as _ZN15QCPainterEngine22releaseUnusedResourcesEv
inline void QCPainterEngine::releaseUnusedResources()
{
#ifndef QCPAINTER_DISABLE_TEXT_SUPPORT
    textVertices = {};
    textIndices = {};
#endif

    ctx.commands.squeeze();
    ctx.commandsData.squeeze();
    ctx.vertices.squeeze();
    ctx.paths.squeeze();
    ctx.points.squeeze();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1321, as _ZN15QCPainterEngine13appendCommandE9QCCommand
inline void QCPainterEngine::appendCommand(QCCommand command)
{
    auto &c = ctx.commands;

    if (ctx.commandsCount + 1 > c.size()) {
        // Increase capacity with the commands amount + 20% of the current size.
        int newSize = (ctx.commandsCount + 1) + c.size() * 0.2;
        c.resize(newSize);
    }

    c[ctx.commandsCount++] = command;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1335, as _ZN15QCPainterEngine14appendCommandsEPK9QCCommandi
inline void QCPainterEngine::appendCommands(const QCCommand commands[], int cCount)
{
    Q_ASSERT(cCount > 0);
    auto &c = ctx.commands;

    if (ctx.commandsCount + cCount > c.size()) {
        // Increase capacity with the commands amount + 20% of the current size.
        int newSize = (ctx.commandsCount + cCount) + c.size() * 0.2;
        c.resize(newSize);
    }

    for (int i = 0; i < cCount; i++)
        c[ctx.commandsCount++] = commands[i];
    //memcpy(&c[ctx.commandsCount], commands, sizeof(QCCommand) * cCount);
    //ctx.commandsCount += cCount;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1354, as _ZN15QCPainterEngine18appendCommandsDataEPKfib
inline void QCPainterEngine::appendCommandsData(const float commandsData[], int dCount, bool ignoreTransform)
{
    // There are always even amount of data as they are (x, y) points.
    Q_ASSERT(dCount % 2 == 0);
    Q_ASSERT(dCount >= 2);

    // Store previous point, as untransformed.
    ctx.prevX = commandsData[dCount - 2];
    ctx.prevY = commandsData[dCount - 1];

    auto &c = ctx.commandsData;
    if (ctx.commandsDataCount + dCount > c.size()) {
        // Increase capacity with the commands amount + 20% of the current size.
        int newSize = (ctx.commandsDataCount + dCount) + c.size() * 0.2;
        c.resize(newSize);
    }

    if (ignoreTransform || state.transform.isIdentity()) {
        // Add commands directly
        for (int i = 0; i < dCount; i++)
            c[ctx.commandsDataCount++] = commandsData[i];
        //memcpy(&c[ctx.commandsDataCount], commandsData, sizeof(float) * dCount);
        //ctx.commandsDataCount += dCount;
    } else {
        int i = 0;
        while (i < dCount) {
            qreal p1 = commandsData[i++];
            qreal p2 = commandsData[i++];
            state.transform.map(p1, p2, &p1, &p2);
            c[ctx.commandsDataCount++] = float(p1);
            c[ctx.commandsDataCount++] = float(p2);
        }
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1389, as _ZN15QCPainterEngine20handleSetPathWindingEN14QCanvasPainter11PathWindingE
inline void QCPainterEngine::handleSetPathWinding(QCanvasPainter::PathWinding winding)
{
    state.winding = winding;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1394, as _ZN15QCPainterEngine15handleClosePathEv
inline void QCPainterEngine::handleClosePath()
{
    if (auto *path = ctx.currentPath)
        path->isClosed = true;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1400, as _ZN15QCPainterEngine12handleMoveToEv
inline void QCPainterEngine::handleMoveTo()
{
    // Moving starts a new subpath.
    auto &paths = ctx.paths;
    if (ctx.pathsCount + 1 > paths.size()) {
        // Increase capacity with 1 + 20% of the current size.
        int newSize = (ctx.pathsCount + 1) + paths.size() * 0.2;
        paths.resize(newSize);
    }
    QCPath *path = &paths[ctx.pathsCount++];
    *path = {};
    path->pointsOffset = ctx.pointsCount;
    path->winding = state.winding;
    ctx.currentPath = path;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1416, as _ZN15QCPainterEngine14handleAddPointEffNS_12QCPointFlagsE
inline void QCPainterEngine::handleAddPoint(float x, float y, QCPointFlags flags)
{
    auto *path = ctx.currentPath;
    Q_ASSERT(path); // At this point path always exists.
#ifdef QCPAINTER_EQUAL_POINTS_CHECKING_ENABLED
    if (path->pointsCount > 0 && ctx.pointsCount > 0) {
        QCPoint &pt = ctx.points[ctx.pointsCount - 1];
        if (pointsEquals(pt.x, pt.y, x, y, ctx.distTol)) {
            // Point is close to previous one, just
            // adjust the point flags.
            pt.flags |= flags;
            return;
        }
    }
#endif

    auto &pts = ctx.points;
    if (Q_UNLIKELY(ctx.pointsCount + 1 > pts.size())) {
        // Increase capacity with 1 + 10% of the current size.
        int newSize = (ctx.pointsCount + 1) + pts.size() * 0.1;
        pts.resize(newSize);
    }

    QCPoint &pt = ctx.points[ctx.pointsCount++];
    pt.x = x;
    pt.y = y;
    pt.flags = flags;
    path->pointsCount++;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1595, as _ZN15QCPainterEngine15tesselateBezierEffffffffiNS_12QCPointFlagsE
inline void QCPainterEngine::tesselateBezier(float x1, float y1, float x2, float y2,
                                         float x3, float y3, float x4, float y4,
                                         int level, QCPointFlags flags)
{
    if (Q_UNLIKELY(level > QCPAINTER_MAX_TESSELLATION_LEVEL)) {
        // This shouldn't usually happen, as we will
        // reach the tessTol accuracy. In case of e.g. huge circles, increase
        // the QCPAINTER_MAX_TESSELLATION_LEVEL.
        return;
    }

    const float dx = x4 - x1;
    const float dy = y4 - y1;
    const float d2 = std::abs((x2 - x4) * dy - (y2 - y4) * dx);
    const float d3 = std::abs((x3 - x4) * dy - (y3 - y4) * dx);
    const float d23 = d2 + d3;
    if (d23 * d23 < ctx.tessTol * (dx * dx + dy * dy)) {
        handleAddPoint(x4, y4, flags);
        return;
    }

    const float x12 = (x1 + x2) * 0.5f;
    const float y12 = (y1 + y2) * 0.5f;
    const float x23 = (x2 + x3) * 0.5f;
    const float y23 = (y2 + y3) * 0.5f;
    const float x34 = (x3 + x4) * 0.5f;
    const float y34 = (y3 + y4) * 0.5f;
    const float x234 = (x23 + x34) * 0.5f;
    const float y234 = (y23 + y34) * 0.5f;
    const float x123 = (x12 + x23) * 0.5f;
    const float y123 = (y12 + y23) * 0.5f;
    const float x1234 = (x123 + x234) * 0.5f;
    const float y1234 = (y123 + y234) * 0.5f;

    tesselateBezier(x1, y1, x12, y12, x123, y123, x1234, y1234, (level + 1), {});
    tesselateBezier(x1234, y1234, x234, y234, x34, y34, x4, y4, (level + 1), flags);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1455, as _ZN15QCPainterEngine14enforceWindingEiiN14QCanvasPainter11PathWindingE
inline void QCPainterEngine::enforceWinding(int pointsOffset, int pointsCount, QCanvasPainter::PathWinding winding)
{
    if (pointsCount <= 2)
        return;
    // Calculate if points area is positive or negative
    float area = 0;
    for (int i = 2; i < pointsCount; i++) {
        const QCPoint a = ctx.points.at(pointsOffset);
        const QCPoint b = ctx.points.at(pointsOffset + i - 1);
        const QCPoint c = ctx.points.at(pointsOffset + i);
        area += triarea2(a.x, a.y, b.x, b.y, c.x, c.y);
    }
    // If needed, reverse the points order
    if ((winding == QCanvasPainter::PathWinding::CounterClockWise && area < 0.0f) ||
        (winding == QCanvasPainter::PathWinding::ClockWise && area > 0.0f)) {
        int i = 0;
        int j = pointsCount - 1;
        auto &pts = ctx.points;
        while (i < j) {
            std::swap(pts[pointsOffset + i], pts[pointsOffset + j]);
            i++;
            j--;
        }
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 1858, as _ZN15QCPainterEngine14calculateJoinsEfN14QCanvasPainter8LineJoinEf
inline void QCPainterEngine::calculateJoins(float w, QCanvasPainter::LineJoin join, float miterLimit)
{
    // Inverse of width
    const float iw = (w > 0.0f) ? 1.0f / w : 0.0f;

    const int pCount = ctx.pathsCount;
    // Calculate which joins needs extra vertices to append, and gather vertex count.
    for (int i = 0; i < pCount; i++) {
        QCPath &path = ctx.paths[i];
        const int pointsCount = path.pointsCount;
        if (Q_UNLIKELY(pointsCount == 0))
            continue;

        int p0Index = path.pointsOffset + pointsCount - 1;
        int p1Index = path.pointsOffset;
        int leftCount = 0;
        int bevelCount = 0;
#if QCPAINTER_STRICT_CONVEX_PATH_CHECK
        bool prevPosX = ctx.points[p0Index].dx > 0;
        bool prevPosY = ctx.points[p0Index].dy > 0;
        int xFlips = 0;
        int yFlips = 0;
#endif

        for (int j = 0; j < pointsCount; j++) {
            const QCPoint &p0 = ctx.points[p0Index];
            QCPoint &p1 = ctx.points[p1Index];
#if QCPAINTER_STRICT_CONVEX_PATH_CHECK
            // Count the number of times the path changes direction
            const bool posX = p1.dx > 0;
            const bool posY = p1.dy > 0;
            if (posX != prevPosX)
                xFlips++;
            if (posY != prevPosY)
                yFlips++;
            prevPosX = posX;
            prevPosY = posY;
#endif
            // Calculate extrusions
            p1.dmx = (p0.dy + p1.dy) * 0.5f;
            p1.dmy = (-p0.dx - p1.dx) * 0.5f;
            float dmr2 = p1.dmx * p1.dmx + p1.dmy * p1.dmy;
            if (dmr2 > 0.001f) {
                float scale = 1.0f / dmr2;
                p1.dmx *= scale;
                p1.dmy *= scale;
            }

            // Clear other flags except the corner.
            p1.flags = (p1.flags & PointCorner) ? PointCorner : 0;

            // Keep track of left turns.
            float cross = p1.dx * p0.dy - p0.dx * p1.dy;
            if (cross > 0.0f) {
                leftCount++;
                p1.flags |= PointLeft;
            }

            // Calculate if we should use bevel or miter for inner join.
            float limit = std::max(1.01f, std::min(p0.len, p1.len) * iw);
            if ((dmr2 * limit * limit) < 1.0f)
                p1.flags |= PointInnerBevel;

            // Check if the corner needs to be beveled.
            if (p1.flags & PointCorner) {
                if (join == QCanvasPainter::LineJoin::Bevel || join == QCanvasPainter::LineJoin::Round || (dmr2 * miterLimit * miterLimit) < 1.0f ) {
                    p1.flags |= PointBevel;
                }
            }

            if ((p1.flags & (PointBevel | PointInnerBevel)))
                bevelCount++;

            p0Index = path.pointsOffset + j;
            p1Index = p0Index + 1;
        }
#if QCPAINTER_STRICT_CONVEX_PATH_CHECK
        // A truly convex path with no self-intersections will only change direction
        // twice along the x-axis and twice along the y-axis
        path.isConvex = leftCount == pointsCount && xFlips <= 2 && yFlips <= 2;
#else
        path.isConvex = leftCount == pointsCount;
#endif
        path.bevelCount = bevelCount;
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2105, as _ZN15QCPainterEngine15addButtCapStartERK7QCPointfffffff
inline void QCPainterEngine::addButtCapStart(const QCPoint &p,
                                         float dx, float dy, float w, float d,
                                         float aa, float u0, float u1)
{
    const float px = p.x - dx * d;
    const float py = p.y - dy * d;
    const float dlxw = dy * w;
    const float dlyw = -dx * w;
    addVert(px + dlxw - dx * aa, py + dlyw - dy * aa, u0, 0.0f);
    addVert(px - dlxw - dx * aa, py - dlyw - dy * aa, u1, 0.0f);
    addVert(px + dlxw, py + dlyw, u0, 1.0f);
    addVert(px - dlxw, py - dlyw, u1, 1.0f);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2119, as _ZN15QCPainterEngine16addRoundCapStartERK7QCPointfffiff
inline void QCPainterEngine::addRoundCapStart(const QCPoint &p,
                                          float dx, float dy, float w, int roundDivs,
                                          float u0, float u1)
{
    const float px = p.x;
    const float py = p.y;
    const float dlx = dy;
    const float dly = -dx;
    for (int i = 0; i < roundDivs; i++) {
        float a = i / float(roundDivs - 1) * M_PI;
        float ax = std::cos(a) * w;
        float ay = std::sin(a) * w;
        addVert(px - dlx * ax - dx * ay, py - dly * ax - dy * ay, u0, 1.0);
        addVert(px, py, 0.5f, 1.0f);
    }
    addVert(px + dlx * w, py + dly * w, u0, 1.0f);
    addVert(px - dlx * w, py - dly * w, u1, 1.0f);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2138, as _ZN15QCPainterEngine13addButtCapEndERK7QCPointfffffff
inline void QCPainterEngine::addButtCapEnd(const QCPoint &p,
                                       float dx, float dy, float w, float d,
                                       float aa, float u0, float u1)
{
    const float px = p.x + dx * d;
    const float py = p.y + dy * d;
    const float dlxw = dy * w;
    const float dlyw = -dx * w;
    addVert(px + dlxw, py + dlyw, u0, 1.0f);
    addVert(px - dlxw, py - dlyw, u1, 1.0f);
    addVert(px + dlxw + dx * aa, py + dlyw + dy * aa, u0, 0.0f);
    addVert(px - dlxw + dx * aa, py - dlyw + dy * aa, u1, 0.0f);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2152, as _ZN15QCPainterEngine14addRoundCapEndERK7QCPointfffiff
inline void QCPainterEngine::addRoundCapEnd(const QCPoint &p,
                                        float dx, float dy, float w, int roundDivs,
                                        float u0, float u1)
{
    const float px = p.x;
    const float py = p.y;
    const float dlx = dy;
    const float dly = -dx;
    addVert(px + (dlx * w), py + (dly * w), u0, 1.0f);
    addVert(px - (dlx * w), py - (dly * w), u1, 1.0f);
    for (int i = 0; i < roundDivs; i++) {
        float a = i / float(roundDivs - 1) * M_PI;
        float ax = std::cos(a) * w;
        float ay = std::sin(a) * w;
        addVert(px, py, 0.5f, 1.0f);
        addVert(px - dlx * ax + dx * ay, py - dly * ax + dy * ay, u0, 1.0f);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2172, as _ZN15QCPainterEngine7addVertEffff
inline void QCPainterEngine::addVert(float x, float y, float u, float v) noexcept
{
    auto &vtx = ctx.vertices[ctx.verticesCount++];
    vtx.x = x;
    vtx.y = y;
    vtx.u = u;
    vtx.v = v;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2182, as _ZN15QCPainterEngine14ensureVerticesEi
inline void QCPainterEngine::ensureVertices(int count)
{
    auto &verts = ctx.vertices;
    if (ctx.verticesCount + count > verts.size()) {
        // Increase capacity with the vertices amount + 10% of the current size.
        int newSize = (ctx.verticesCount + count) + verts.size() * 0.1;
        verts.resize(newSize);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2358, as _ZNK15QCPainterEngine18effectiveTextAlignE11QStringView
inline QCanvasPainter::TextAlign QCPainterEngine::effectiveTextAlign(QStringView text) const
{
    QCanvasPainter::TextAlign align = state.textAlignment;
    auto effectiveDirection = state.textDirection;
#if QT_CONFIG(im)
    bool emptyAuto = effectiveDirection == QCanvasPainter::TextDirection::Auto && text.isEmpty();
    if (emptyAuto || effectiveDirection == QCanvasPainter::TextDirection::Inherit) {
        // Get inherited direction from QGuiApplication. Also used for Auto,
        // when the string is empty. See:
        // https://doc.qt.io/qt-6/qtquick-positioning-righttoleft.html#text-alignment
        if (qGuiApp->isRightToLeft())
            effectiveDirection = QCanvasPainter::TextDirection::RightToLeft;
        else
            effectiveDirection = QCanvasPainter::TextDirection::LeftToRight;
    }
#else
    if (effectiveDirection == QCanvasPainter::TextDirection::Inherit) {
        // No access to inputMethod(), so fail to auto detect
        effectiveDirection = QCanvasPainter::TextDirection::Auto;
    }
#endif
    if (effectiveDirection == QCanvasPainter::TextDirection::Auto) {
        // Get automatic direction from QString isRightToLeft().
        if (text.isRightToLeft())
            effectiveDirection = QCanvasPainter::TextDirection::RightToLeft;
        else
            effectiveDirection = QCanvasPainter::TextDirection::LeftToRight;
    }

    if (effectiveDirection == QCanvasPainter::TextDirection::RightToLeft) {
        if (align == QCanvasPainter::TextAlign::Start) {
            align = QCanvasPainter::TextAlign::Right;
        } else if (align == QCanvasPainter::TextAlign::End) {
            align = QCanvasPainter::TextAlign::Left;
        }
    } else if (align == QCanvasPainter::TextAlign::Start) {
        align = QCanvasPainter::TextAlign::Left;
    } else if (align == QCanvasPainter::TextAlign::End) {
        align = QCanvasPainter::TextAlign::Right;
    }

    return align;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2316, as _ZN15QCPainterEngine12getFillPaintEb
inline QCPaint QCPainterEngine::getFillPaint(bool ignoreTransform)
{
    QCPaint fillPaint = state.fill;
    fillPaint.alpha = state.alpha;
    // Apply current transform
    if (!ignoreTransform &&
        fillPaint.brushType != BrushColor &&
        !(state.transform.isIdentity() && state.brushTransform.isIdentity())) {
        fillPaint.transform *= (state.brushTransform * state.transform);
    }
    return fillPaint;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterengine.cpp, line 2420, as _ZN15QCPainterEngine19updateStateFontVarsEv
#if !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
inline void QCPainterEngine::updateStateFontVars()
{
    auto &font = state.font;
    // Calculating optimal font scale.
    // This is how QSGDistanceFieldGlyphNode does it:
    //const float combinedScale = m_fontScale * m_matrixScale;
    const auto rFont = QRawFont::fromFont(font);
    // TODO: This is a heavy operation. If supported, it should be cached.
    //const bool narrowFont = qt_fontHasNarrowOutlines(rFont);
    const bool narrowFont = false;
    const float baseFontSize = QT_DISTANCEFIELD_BASEFONTSIZE(narrowFont);
    const float combinedScale = rFont.pixelSize() / baseFontSize * ctx.devicePxRatio;
    // Then use it to calculate the optimal smoothstep min & max.
    const float base = thresholdFunc(combinedScale);
    const float range = spreadFunc(combinedScale) * state.textAntialias;
    ctx.fontAlphaMin = qMax(0.0f, base - range);
    ctx.fontAlphaMax = qMin(base + range, 1.0f);
}
#endif  // !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
//  -----------------------------------------------------------------------

//  QCPainterEngine::QCPainterEngine()
extern "C" Q_DECL_EXPORT
QCPainterEngine *ritual_ZN15QCPainterEngineC1Ev() {
  return new QCPainterEngine();
}

//  void QCPainterEngine::setCustomMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15setCustomMatrixERK10QMatrix4x4(
    QCPainterEngine *self,
    const QMatrix4x4 *matrix) {
  self->setCustomMatrix(*matrix);
}

//  void QCPainterEngine::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine8endPaintEv(QCPainterEngine *self) {
  self->endPaint();
}

//  void QCPainterEngine::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine4saveEv(QCPainterEngine *self) {
  self->save();
}

//  void QCPainterEngine::restore()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine7restoreEv(QCPainterEngine *self) {
  self->restore();
}

//  void QCPainterEngine::setStrokeColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14setStrokeColorE6QColor(
    QCPainterEngine *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  void QCPainterEngine::setStrokePaint(const QCPaint &paint)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14setStrokePaintERK7QCPaint(
    QCPainterEngine *self,
    const QCPaint *paint) {
  self->setStrokePaint(*paint);
}

//  void QCPainterEngine::setFillColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12setFillColorE6QColor(
    QCPainterEngine *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  void QCPainterEngine::setFillPaint(const QCPaint &paint)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12setFillPaintERK7QCPaint(
    QCPainterEngine *self,
    const QCPaint *paint) {
  self->setFillPaint(*paint);
}

//  void QCPainterEngine::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12setLineWidthEf(
    QCPainterEngine *self,
    float width) {
  self->setLineWidth(width);
}

//  void QCPainterEngine::setLineCap(QCanvasPainter::LineCap lineCap)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine10setLineCapEN14QCanvasPainter7LineCapE(
    QCPainterEngine *self,
    QCanvasPainter::LineCap lineCap) {
  self->setLineCap(lineCap);
}

//  void QCPainterEngine::setLineJoin(QCanvasPainter::LineJoin lineJoin)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine11setLineJoinEN14QCanvasPainter8LineJoinE(
    QCPainterEngine *self,
    QCanvasPainter::LineJoin lineJoin) {
  self->setLineJoin(lineJoin);
}

//  void QCPainterEngine::setGlobalAlpha(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14setGlobalAlphaEf(
    QCPainterEngine *self,
    float alpha) {
  self->setGlobalAlpha(alpha);
}

//  void QCPainterEngine::setGlobalBrightness(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine19setGlobalBrightnessEf(
    QCPainterEngine *self,
    float value) {
  self->setGlobalBrightness(value);
}

//  void QCPainterEngine::setGlobalContrast(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine17setGlobalContrastEf(
    QCPainterEngine *self,
    float value) {
  self->setGlobalContrast(value);
}

//  void QCPainterEngine::setGlobalSaturation(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine19setGlobalSaturationEf(
    QCPainterEngine *self,
    float value) {
  self->setGlobalSaturation(value);
}

//  void QCPainterEngine::setFillRule(QCanvasPainter::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine11setFillRuleEN14QCanvasPainter8FillRuleE(
    QCPainterEngine *self,
    QCanvasPainter::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  QCanvasPainter::FillRule QCPainterEngine::fillRule() const
extern "C" Q_DECL_EXPORT
QCanvasPainter::FillRule ritual_ZNK15QCPainterEngine8fillRuleEv(
    const QCPainterEngine *self) {
  return self->fillRule();
}

//  void QCPainterEngine::setCustomStrokeBrush(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine20setCustomStrokeBrushERK12QCanvasBrush(
    QCPainterEngine *self,
    const QCanvasBrush *brush) {
  self->setCustomStrokeBrush(*brush);
}

//  void QCPainterEngine::setCustomFillBrush(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine18setCustomFillBrushERK12QCanvasBrush(
    QCPainterEngine *self,
    const QCanvasBrush *brush) {
  self->setCustomFillBrush(*brush);
}

//  QTransform QCPainterEngine::currentTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QCPainterEngine16currentTransformEv(
    const QCPainterEngine *self) {
  return new QTransform(self->currentTransform());
}

//  void QCPainterEngine::transform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine9transformERK10QTransform(
    QCPainterEngine *self,
    const QTransform *transform) {
  self->transform(*transform);
}

//  void QCPainterEngine::setTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12setTransformERK10QTransform(
    QCPainterEngine *self,
    const QTransform *transform) {
  self->setTransform(*transform);
}

//  void QCPainterEngine::resetTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14resetTransformEv(QCPainterEngine *self) {
  self->resetTransform();
}

//  void QCPainterEngine::translate(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine9translateEff(
    QCPainterEngine *self,
    float x,
    float y) {
  self->translate(x, y);
}

//  void QCPainterEngine::scale(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine5scaleEff(
    QCPainterEngine *self,
    float x,
    float y) {
  self->scale(x, y);
}

//  void QCPainterEngine::rotate(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine6rotateEf(
    QCPainterEngine *self,
    float angle) {
  self->rotate(angle);
}

//  void QCPainterEngine::skew(float angleX, float angleY)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine4skewEff(
    QCPainterEngine *self,
    float angleX,
    float angleY) {
  self->skew(angleX, angleY);
}

//  void QCPainterEngine::setBrushTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine17setBrushTransformERK10QTransform(
    QCPainterEngine *self,
    const QTransform *transform) {
  self->setBrushTransform(*transform);
}

//  QCPaint QCPainterEngine::createImagePattern(float x, float y, float
//      width, float height, int imageId, float angle, QColor tintColor)
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZN15QCPainterEngine18createImagePatternEffffif6QColor(
    QCPainterEngine *self,
    float x,
    float y,
    float width,
    float height,
    int imageId,
    float angle,
    const QColor *tintColor) {
  return new QCPaint(
      self->createImagePattern(
          x,
          y,
          width,
          height,
          imageId,
          angle,
          *tintColor));
}

//  void QCPainterEngine::beginPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine9beginPathEv(QCPainterEngine *self) {
  self->beginPath();
}

//  void QCPainterEngine::closePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine9closePathEv(QCPainterEngine *self) {
  self->closePath();
}

//  void QCPainterEngine::moveTo(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine6moveToEff(
    QCPainterEngine *self,
    float x,
    float y) {
  self->moveTo(x, y);
}

//  void QCPainterEngine::lineTo(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine6lineToEff(
    QCPainterEngine *self,
    float x,
    float y) {
  self->lineTo(x, y);
}

//  void QCPainterEngine::bezierTo(float cp1X, float cp1Y, float cp2X, float
//      cp2Y, float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine8bezierToEffffff(
    QCPainterEngine *self,
    float cp1X,
    float cp1Y,
    float cp2X,
    float cp2Y,
    float x,
    float y) {
  self->bezierTo(cp1X, cp1Y, cp2X, cp2Y, x, y);
}

//  void QCPainterEngine::quadTo(float cpX, float cpY, float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine6quadToEffff(
    QCPainterEngine *self,
    float cpX,
    float cpY,
    float x,
    float y) {
  self->quadTo(cpX, cpY, x, y);
}

//  void QCPainterEngine::arcTo(float x1, float y1, float x2, float y2, float
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine5arcToEfffff(
    QCPainterEngine *self,
    float x1,
    float y1,
    float x2,
    float y2,
    float radius) {
  self->arcTo(x1, y1, x2, y2, radius);
}

//  void QCPainterEngine::addArc(float x, float y, float radius, float a0,
//      float a1, QCanvasPainter::PathWinding direction, bool isConnected)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine6addArcEfffffN14QCanvasPainter11PathWindingEb(
    QCPainterEngine *self,
    float x,
    float y,
    float radius,
    float a0,
    float a1,
    QCanvasPainter::PathWinding direction,
    bool isConnected) {
  self->addArc(x, y, radius, a0, a1, direction, isConnected);
}

//  void QCPainterEngine::addRect(float x, float y, float width, float
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine7addRectEffff(
    QCPainterEngine *self,
    float x,
    float y,
    float width,
    float height) {
  self->addRect(x, y, width, height);
}

//  void QCPainterEngine::addRoundRect(float x, float y, float width, float
//      height, float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12addRoundRectEfffff(
    QCPainterEngine *self,
    float x,
    float y,
    float width,
    float height,
    float radius) {
  self->addRoundRect(x, y, width, height, radius);
}

//  void QCPainterEngine::addRoundRect(float x, float y, float width, float
//      height, float radiusTopLeft, float radiusTopRight, float
//      radiusBottomRight, float radiusBottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12addRoundRectEffffffff(
    QCPainterEngine *self,
    float x,
    float y,
    float width,
    float height,
    float radiusTopLeft,
    float radiusTopRight,
    float radiusBottomRight,
    float radiusBottomLeft) {
  self->addRoundRect(
      x,
      y,
      width,
      height,
      radiusTopLeft,
      radiusTopRight,
      radiusBottomRight,
      radiusBottomLeft);
}

//  void QCPainterEngine::addEllipse(float x, float y, float radiusX, float
//      radiusY)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine10addEllipseEffff(
    QCPainterEngine *self,
    float x,
    float y,
    float radiusX,
    float radiusY) {
  self->addEllipse(x, y, radiusX, radiusY);
}

//  void QCPainterEngine::addCircle(float x, float y, float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine9addCircleEfff(
    QCPainterEngine *self,
    float x,
    float y,
    float radius) {
  self->addCircle(x, y, radius);
}

//  void QCPainterEngine::addPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine7addPathERK12QPainterPath(
    QCPainterEngine *self,
    const QPainterPath *path) {
  self->addPath(*path);
}

//  void QCPainterEngine::setPathWinding(QCanvasPainter::PathWinding winding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14setPathWindingEN14QCanvasPainter11PathWindingE(
    QCPainterEngine *self,
    QCanvasPainter::PathWinding winding) {
  self->setPathWinding(winding);
}

//  void QCPainterEngine::setGlobalCompositeOperation(QCanvasPainter::Composi
//      teOperation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine27setGlobalCompositeOperationEN14QCanvasPainter18CompositeOperationE(
    QCPainterEngine *self,
    QCanvasPainter::CompositeOperation op) {
  self->setGlobalCompositeOperation(op);
}

//  void QCPainterEngine::setTextWrapMode(QCanvasPainter::WrapMode wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15setTextWrapModeEN14QCanvasPainter8WrapModeE(
    QCPainterEngine *self,
    QCanvasPainter::WrapMode wrapMode) {
  self->setTextWrapMode(wrapMode);
}

//  void QCPainterEngine::setTextLineHeight(float height)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine17setTextLineHeightEf(
    QCPainterEngine *self,
    float height) {
  self->setTextLineHeight(height);
}

//  void QCPainterEngine::setTextAntialias(float antialias)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine16setTextAntialiasEf(
    QCPainterEngine *self,
    float antialias) {
  self->setTextAntialias(antialias);
}

//  void QCPainterEngine::setTextAlignment(QCanvasPainter::TextAlign align)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine16setTextAlignmentEN14QCanvasPainter9TextAlignE(
    QCPainterEngine *self,
    QCanvasPainter::TextAlign align) {
  self->setTextAlignment(align);
}

//  void QCPainterEngine::setTextBaseline(QCanvasPainter::TextBaseline
//      baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15setTextBaselineEN14QCanvasPainter12TextBaselineE(
    QCPainterEngine *self,
    QCanvasPainter::TextBaseline baseline) {
  self->setTextBaseline(baseline);
}

//  void QCPainterEngine::setTextDirection(QCanvasPainter::TextDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine16setTextDirectionEN14QCanvasPainter13TextDirectionE(
    QCPainterEngine *self,
    QCanvasPainter::TextDirection direction) {
  self->setTextDirection(direction);
}

//  QRectF QCPainterEngine::textBoundingBox(const QString &text, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN15QCPainterEngine15textBoundingBoxERK7QStringRK6QRectF(
    QCPainterEngine *self,
    const QString *text,
    const QRectF *rect) {
  return new QRectF(self->textBoundingBox(*text, *rect));
}

//  void QCPainterEngine::resetDebugCounters()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine18resetDebugCountersEv(
    QCPainterEngine *self) {
  self->resetDebugCounters();
}

//  QCDebugCounters QCPainterEngine::debugCounters() const
extern "C" Q_DECL_EXPORT
QCDebugCounters *ritual_ZNK15QCPainterEngine13debugCountersEv(
    const QCPainterEngine *self) {
  return new QCDebugCounters(self->debugCounters());
}

//  void QCPainterEngine::setAntialias(float antialias)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12setAntialiasEf(
    QCPainterEngine *self,
    float antialias) {
  self->setAntialias(antialias);
}

//  void QCPainterEngine::setMiterLimit(float limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine13setMiterLimitEf(
    QCPainterEngine *self,
    float limit) {
  self->setMiterLimit(limit);
}

//  void QCPainterEngine::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine7cleanupEv(QCPainterEngine *self) {
  self->cleanup();
}

//  void QCPainterEngine::releaseUnusedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine22releaseUnusedResourcesEv(
    QCPainterEngine *self) {
  self->releaseUnusedResources();
}

//  void QCPainterEngine::appendCommand(QCCommand command)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine13appendCommandE9QCCommand(
    QCPainterEngine *self,
    QCCommand command) {
  self->appendCommand(command);
}

//  void QCPainterEngine::appendCommands(const QCCommand *commands, int
//      cCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14appendCommandsEPK9QCCommandi(
    QCPainterEngine *self,
    const QCCommand *commands,
    int cCount) {
  self->appendCommands(commands, cCount);
}

//  void QCPainterEngine::appendCommandsData(const float *commandsData, int
//      dCount, bool ignoreTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine18appendCommandsDataEPKfib(
    QCPainterEngine *self,
    const float *commandsData,
    int dCount,
    bool ignoreTransform) {
  self->appendCommandsData(commandsData, dCount, ignoreTransform);
}

//  void QCPainterEngine::handleSetPathWinding(QCanvasPainter::PathWinding
//      winding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine20handleSetPathWindingEN14QCanvasPainter11PathWindingE(
    QCPainterEngine *self,
    QCanvasPainter::PathWinding winding) {
  self->handleSetPathWinding(winding);
}

//  void QCPainterEngine::handleClosePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15handleClosePathEv(QCPainterEngine *self) {
  self->handleClosePath();
}

//  void QCPainterEngine::handleMoveTo()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine12handleMoveToEv(QCPainterEngine *self) {
  self->handleMoveTo();
}

//  void QCPainterEngine::handleAddPoint(float x, float y, QCPointFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14handleAddPointEffNS_12QCPointFlagsE(
    QCPainterEngine *self,
    float x,
    float y,
    QCPainterEngine::QCPointFlags flags) {
  self->handleAddPoint(x, y, flags);
}

//  void QCPainterEngine::tesselateBezier(float x1, float y1, float x2, float
//      y2, float x3, float y3, float x4, float y4, int level, QCPointFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15tesselateBezierEffffffffiNS_12QCPointFlagsE(
    QCPainterEngine *self,
    float x1,
    float y1,
    float x2,
    float y2,
    float x3,
    float y3,
    float x4,
    float y4,
    int level,
    QCPainterEngine::QCPointFlags flags) {
  self->tesselateBezier(x1, y1, x2, y2, x3, y3, x4, y4, level, flags);
}

//  void QCPainterEngine::enforceWinding(int pointsOffset, int pointsCount,
//      QCanvasPainter::PathWinding winding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14enforceWindingEiiN14QCanvasPainter11PathWindingE(
    QCPainterEngine *self,
    int pointsOffset,
    int pointsCount,
    QCanvasPainter::PathWinding winding) {
  self->enforceWinding(pointsOffset, pointsCount, winding);
}

//  void QCPainterEngine::calculateJoins(float w, QCanvasPainter::LineJoin
//      join, float miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14calculateJoinsEfN14QCanvasPainter8LineJoinEf(
    QCPainterEngine *self,
    float w,
    QCanvasPainter::LineJoin join,
    float miterLimit) {
  self->calculateJoins(w, join, miterLimit);
}

//  void QCPainterEngine::addButtCapStart(const QCPoint &p, float dx, float
//      dy, float w, float d, float aa, float u0, float u1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine15addButtCapStartERK7QCPointfffffff(
    QCPainterEngine *self,
    const QCPoint *p,
    float dx,
    float dy,
    float w,
    float d,
    float aa,
    float u0,
    float u1) {
  self->addButtCapStart(*p, dx, dy, w, d, aa, u0, u1);
}

//  void QCPainterEngine::addRoundCapStart(const QCPoint &p, float dx, float
//      dy, float w, int capDivs, float u0, float u1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine16addRoundCapStartERK7QCPointfffiff(
    QCPainterEngine *self,
    const QCPoint *p,
    float dx,
    float dy,
    float w,
    int capDivs,
    float u0,
    float u1) {
  self->addRoundCapStart(*p, dx, dy, w, capDivs, u0, u1);
}

//  void QCPainterEngine::addButtCapEnd(const QCPoint &p, float dx, float dy,
//      float w, float d, float aa, float u0, float u1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine13addButtCapEndERK7QCPointfffffff(
    QCPainterEngine *self,
    const QCPoint *p,
    float dx,
    float dy,
    float w,
    float d,
    float aa,
    float u0,
    float u1) {
  self->addButtCapEnd(*p, dx, dy, w, d, aa, u0, u1);
}

//  void QCPainterEngine::addRoundCapEnd(const QCPoint &p, float dx, float
//      dy, float w, int capDivs, float u0, float u1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14addRoundCapEndERK7QCPointfffiff(
    QCPainterEngine *self,
    const QCPoint *p,
    float dx,
    float dy,
    float w,
    int capDivs,
    float u0,
    float u1) {
  self->addRoundCapEnd(*p, dx, dy, w, capDivs, u0, u1);
}

//  void QCPainterEngine::addVert(float x, float y, float u, float v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine7addVertEffff(
    QCPainterEngine *self,
    float x,
    float y,
    float u,
    float v) {
  self->addVert(x, y, u, v);
}

//  void QCPainterEngine::ensureVertices(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine14ensureVerticesEi(
    QCPainterEngine *self,
    int count) {
  self->ensureVertices(count);
}

//  QCanvasPainter::TextAlign QCPainterEngine::effectiveTextAlign(QStringView
//      text) const
extern "C" Q_DECL_EXPORT
QCanvasPainter::TextAlign ritual_ZNK15QCPainterEngine18effectiveTextAlignE11QStringView(
    const QCPainterEngine *self,
    const QString *text) {
  return self->effectiveTextAlign(QStringView(*text));
}

//  QCPaint QCPainterEngine::getFillPaint(bool ignoreTransform)
extern "C" Q_DECL_EXPORT
QCPaint *ritual_ZN15QCPainterEngine12getFillPaintEb(
    QCPainterEngine *self,
    bool ignoreTransform) {
  return new QCPaint(self->getFillPaint(ignoreTransform));
}

#if !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)
//  void QCPainterEngine::updateStateFontVars()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngine19updateStateFontVarsEv(
    QCPainterEngine *self) {
  self->updateStateFontVars();
}
#endif  // !defined(QCPAINTER_DISABLE_TEXT_SUPPORT)

//  QCPainterEngine::~QCPainterEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCPainterEngineD1Ev(QCPainterEngine *self) {
  delete self;
}
