//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpainterrhirenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qsize.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 142, as local:qcpainterrhirenderer.cpp:QCRHICommonUniforms
struct QCRHICommonUniforms {
    // Total size 112 + 112 = 224 bytes.
    // Built-in variables size is 112 bytes
    float scissorMat[12]; // matrices are actually 3 vec4s
    float scissorExt[2];
    float scissorScale[2];
    float alphaMult;
    float strokeThr;
    float fontAlphaMin;
    float fontAlphaMax;
    float colorEffects[4];
    int texType;
    int type;
    float globalAlpha;
    // Take this into use when needed
    int unusedInt;
    // Custom input size is 112 bytes.
    float paintMat[12];
    QCColor innerCol;
    QCColor outerCol;
    float extent[2];
    float radius;
    float feather;
    // Take these into use when needed
    float unused2[4];
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 169, as local:qcpainterrhirenderer.cpp:QCRHISamplerDesc
struct QCRHISamplerDesc
{
    QRhiSampler::Filter minFilter;
    QRhiSampler::Filter magFilter;
    QRhiSampler::Filter mipmap;
    QRhiSampler::AddressMode hTiling;
    QRhiSampler::AddressMode vTiling;
    QRhiSampler::AddressMode zTiling;
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 321, as local:qcpainterrhirenderer.cpp:QCRHISrbKey
struct QCRHISrbKey {
    int passId;
    int imageId;
    int fontId;
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3415, as local:qcpainterrhirenderer.cpp:isCompressedFormat
static inline bool isCompressedFormat(QRhiTexture::Format format)
{
    return (format >= QRhiTexture::BC1 && format <= QRhiTexture::BC7)
            || (format >= QRhiTexture::ETC2_RGB8 && format <= QRhiTexture::ETC2_RGBA8)
            || (format >= QRhiTexture::ASTC_4x4 && format <= QRhiTexture::ASTC_12x12);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3422, as local:qcpainterrhirenderer.cpp:compressedFormatInfo
static void compressedFormatInfo(QRhiTexture::Format format, QSize size, quint32 *bpl, quint32 *byteSize, QSize *blockDim)
{
    int xdim = 4;
    int ydim = 4;
    quint32 blockSize = 0;

    switch (format) {
    case QRhiTexture::BC1:
        blockSize = 8;
        break;
    case QRhiTexture::BC2:
        blockSize = 16;
        break;
    case QRhiTexture::BC3:
        blockSize = 16;
        break;
    case QRhiTexture::BC4:
        blockSize = 8;
        break;
    case QRhiTexture::BC5:
        blockSize = 16;
        break;
    case QRhiTexture::BC6H:
        blockSize = 16;
        break;
    case QRhiTexture::BC7:
        blockSize = 16;
        break;

    case QRhiTexture::ETC2_RGB8:
        blockSize = 8;
        break;
    case QRhiTexture::ETC2_RGB8A1:
        blockSize = 8;
        break;
    case QRhiTexture::ETC2_RGBA8:
        blockSize = 16;
        break;

    case QRhiTexture::ASTC_4x4:
        blockSize = 16;
        break;
    case QRhiTexture::ASTC_5x4:
        blockSize = 16;
        xdim = 5;
        break;
    case QRhiTexture::ASTC_5x5:
        blockSize = 16;
        xdim = ydim = 5;
        break;
    case QRhiTexture::ASTC_6x5:
        blockSize = 16;
        xdim = 6;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_6x6:
        blockSize = 16;
        xdim = ydim = 6;
        break;
    case QRhiTexture::ASTC_8x5:
        blockSize = 16;
        xdim = 8;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_8x6:
        blockSize = 16;
        xdim = 8;
        ydim = 6;
        break;
    case QRhiTexture::ASTC_8x8:
        blockSize = 16;
        xdim = ydim = 8;
        break;
    case QRhiTexture::ASTC_10x5:
        blockSize = 16;
        xdim = 10;
        ydim = 5;
        break;
    case QRhiTexture::ASTC_10x6:
        blockSize = 16;
        xdim = 10;
        ydim = 6;
        break;
    case QRhiTexture::ASTC_10x8:
        blockSize = 16;
        xdim = 10;
        ydim = 8;
        break;
    case QRhiTexture::ASTC_10x10:
        blockSize = 16;
        xdim = ydim = 10;
        break;
    case QRhiTexture::ASTC_12x10:
        blockSize = 16;
        xdim = 12;
        ydim = 10;
        break;
    case QRhiTexture::ASTC_12x12:
        blockSize = 16;
        xdim = ydim = 12;
        break;

    default:
        qWarning("Unhandled compressed texture format %d in QCanvasPainter compressedFormatInfo", int(format));
        break;
    }

    const quint32 wblocks = uint((size.width() + xdim - 1) / xdim);
    const quint32 hblocks = uint((size.height() + ydim - 1) / ydim);

    if (bpl)
        *bpl = wblocks * blockSize;
    if (byteSize)
        *byteSize = wblocks * hblocks * blockSize;
    if (blockDim)
        *blockDim = QSize(xdim, ydim);
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcpainterrhirenderer.cpp, line 3540, as _ZN20QCPainterRhiRenderer17textureFormatInfoEN11QRhiTexture6FormatE5QSizePjS3_S3_
inline void QCPainterRhiRenderer::textureFormatInfo(QRhiTexture::Format format, QSize size,
                                             quint32 *bpl, quint32 *byteSize, quint32 *bytesPerPixel)
{
    if (isCompressedFormat(format)) {
        compressedFormatInfo(format, size, bpl, byteSize, nullptr);
        return;
    }

    quint32 bpc = 0;
    switch (format) {
    case QRhiTexture::RGBA8:
        bpc = 4;
        break;
    case QRhiTexture::BGRA8:
        bpc = 4;
        break;
    case QRhiTexture::R8:
        bpc = 1;
        break;
    case QRhiTexture::RG8:
        bpc = 2;
        break;
    case QRhiTexture::R16:
        bpc = 2;
        break;
    case QRhiTexture::RG16:
        bpc = 4;
        break;
    case QRhiTexture::RED_OR_ALPHA8:
        bpc = 1;
        break;

    case QRhiTexture::RGBA16F:
        bpc = 8;
        break;
    case QRhiTexture::RGBA32F:
        bpc = 16;
        break;
    case QRhiTexture::R16F:
        bpc = 2;
        break;
    case QRhiTexture::R32F:
        bpc = 4;
        break;

    case QRhiTexture::RGB10A2:
        bpc = 4;
        break;

    case QRhiTexture::D16:
        bpc = 2;
        break;
    case QRhiTexture::D24:
    case QRhiTexture::D24S8:
    case QRhiTexture::D32F:
        bpc = 4;
        break;

    case QRhiTexture::D32FS8:
        bpc = 8;
        break;

    case QRhiTexture::R8SI:
    case QRhiTexture::R8UI:
        bpc = 1;
        break;
    case QRhiTexture::R32SI:
    case QRhiTexture::R32UI:
        bpc = 4;
        break;
    case QRhiTexture::RG32SI:
    case QRhiTexture::RG32UI:
        bpc = 8;
        break;
    case QRhiTexture::RGBA32SI:
    case QRhiTexture::RGBA32UI:
        bpc = 16;
        break;

    default:
        qWarning("Unhandled texture format %d in QCanvasPainter textureFormatInfo", int(format));
        break;
    }

    if (bpl)
        *bpl = uint(size.width()) * bpc;
    if (byteSize)
        *byteSize = uint(size.width() * size.height()) * bpc;
    if (bytesPerPixel)
        *bytesPerPixel = bpc;
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

//  void QCPainterRhiRenderer::textureFormatInfo(QRhiTexture::Format format,
//      QSize size, quint32 *bpl, quint32 *byteSize, quint32 *bytesPerPixel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCPainterRhiRenderer17textureFormatInfoEN11QRhiTexture6FormatE5QSizePjS3_S3_(
    QRhiTexture::Format format,
    const QSize *size,
    quint32 *bpl,
    quint32 *byteSize,
    quint32 *bytesPerPixel) {
  QCPainterRhiRenderer::textureFormatInfo(
      format,
      *size,
      bpl,
      byteSize,
      bytesPerPixel);
}
