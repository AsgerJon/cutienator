//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: in the code taken for 'initRhi', the
//  part for Vulkan stands under 'QT_CONFIG(vulkan) &&
//  __has_include(<vulkan/vulkan.h>)', the condition under which Qt's
//  'qrhi_platform.h' declares 'QRhiVulkanInitParams': a machine
//  whose Qt has Vulkan may lack Vulkan's headers. Kept as it is when
//  the generator runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qvideowindow_p.h>
#include <QtGui/QPlatformSurfaceEvent>
#include <QtCore/qfile.h>
#include <QtGui/qpainter.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtMultimedia/private/qmemoryvideobuffer_p.h>
#include <QtMultimedia/private/qhwvideobuffer_p.h>
#include <QtMultimedia/private/qmultimediautils_p.h>
#include <QtMultimedia/private/qvideoframe_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 76, as local:qvideowindow.cpp:g_vw_quad
static const float g_vw_quad[] = {
    // 4 clockwise rotation of texture vertexes (the second pair)
    // Rotation 0
    -1.f, -1.f,   0.f, 0.f,
    -1.f, 1.f,    0.f, 1.f,
    1.f, -1.f,    1.f, 0.f,
    1.f, 1.f,     1.f, 1.f,
    // Rotation 90
    -1.f, -1.f,   0.f, 1.f,
    -1.f, 1.f,    1.f, 1.f,
    1.f, -1.f,    0.f, 0.f,
    1.f, 1.f,     1.f, 0.f,

    // Rotation 180
    -1.f, -1.f,   1.f, 1.f,
    -1.f, 1.f,    1.f, 0.f,
    1.f, -1.f,    0.f, 1.f,
    1.f, 1.f,     0.f, 0.f,
    // Rotation 270
    -1.f, -1.f,   1.f, 0.f,
    -1.f, 1.f,    0.f, 0.f,
    1.f, -1.f,    1.f, 1.f,
    1.f, 1.f,     0.f, 1.f
};

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 101, as local:qvideowindow.cpp:vwGetShader
static QShader vwGetShader(const QString &name)
{
    QFile f(name);
    if (f.open(QIODevice::ReadOnly))
        return QShader::fromSerialized(f.readAll());

    return QShader();
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 110, as _ZN19QVideoWindowPrivate7initRhiEv
#if defined(Q_OS_LINUX)
inline void QVideoWindowPrivate::initRhi()
{
    if (m_graphicsApi == QRhi::Null)
        return;

    [[maybe_unused]] QRhi::Flags rhiFlags = {};//QRhi::EnableDebugMarkers | QRhi::EnableProfiling;

#if QT_CONFIG(opengl)
    if (m_graphicsApi == QRhi::OpenGLES2) {
        m_fallbackSurface.reset(QRhiGles2InitParams::newFallbackSurface(q->format()));
        QRhiGles2InitParams params;
        params.fallbackSurface = m_fallbackSurface.get();
        params.window = q;
        params.format = q->format();
        m_rhi.reset(QRhi::create(QRhi::OpenGLES2, &params, rhiFlags));
    }
#endif

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
    if (m_graphicsApi == QRhi::Vulkan) {
        QRhiVulkanInitParams params;
        params.inst = q->vulkanInstance();
        params.window = q;
        m_rhi.reset(QRhi::create(QRhi::Vulkan, &params, rhiFlags));
    }
#endif

#ifdef Q_OS_WIN
    if (m_graphicsApi == QRhi::D3D11) {
        QRhiD3D11InitParams params;
        params.enableDebugLayer = true;
        m_rhi.reset(QRhi::create(QRhi::D3D11, &params, rhiFlags));
    }
#endif

#if QT_CONFIG(metal)
    if (m_graphicsApi == QRhi::Metal) {
        QRhiMetalInitParams params;
        m_rhi.reset(QRhi::create(QRhi::Metal, &params, rhiFlags));
    }
#endif
    if (!m_rhi)
        return;

    m_swapChain.reset(m_rhi->newSwapChain());
    m_swapChain->setWindow(q);
    m_renderPass.reset(m_swapChain->newCompatibleRenderPassDescriptor());
    m_swapChain->setRenderPassDescriptor(m_renderPass.get());

    m_vertexBuf.reset(m_rhi->newBuffer(QRhiBuffer::Immutable, QRhiBuffer::VertexBuffer, sizeof(g_vw_quad)));
    m_vertexBuf->create();
    m_vertexBufReady = false;

    m_uniformBuf.reset(m_rhi->newBuffer(QRhiBuffer::Dynamic, QRhiBuffer::UniformBuffer, sizeof(QVideoTextureHelper::UniformData)));
    m_uniformBuf->create();

    m_textureSampler.reset(m_rhi->newSampler(QRhiSampler::Linear, QRhiSampler::Linear, QRhiSampler::None,
                                             QRhiSampler::ClampToEdge, QRhiSampler::ClampToEdge));
    m_textureSampler->create();

    m_shaderResourceBindings.reset(m_rhi->newShaderResourceBindings());
    m_subtitleResourceBindings.reset(m_rhi->newShaderResourceBindings());

    m_subtitleUniformBuf.reset(m_rhi->newBuffer(QRhiBuffer::Dynamic, QRhiBuffer::UniformBuffer, sizeof(QVideoTextureHelper::UniformData)));
    m_subtitleUniformBuf->create();
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 177, as _ZN19QVideoWindowPrivate21setupGraphicsPipelineEP20QRhiGraphicsPipelineP26QRhiShaderResourceBindingsRK17QVideoFrameFormat
inline void QVideoWindowPrivate::setupGraphicsPipeline(QRhiGraphicsPipeline *pipeline, QRhiShaderResourceBindings *bindings, const QVideoFrameFormat &fmt)
{

    pipeline->setTopology(QRhiGraphicsPipeline::TriangleStrip);
    QShader vs = vwGetShader(QVideoTextureHelper::vertexShaderFileName(fmt));
    Q_ASSERT(vs.isValid());
    QShader fs = vwGetShader(QVideoTextureHelper::fragmentShaderFileName(
            fmt, m_rhi.get(), m_swapChain->format()));
    Q_ASSERT(fs.isValid());
    pipeline->setShaderStages({
        { QRhiShaderStage::Vertex, vs },
        { QRhiShaderStage::Fragment, fs }
    });
    QRhiVertexInputLayout inputLayout;
    inputLayout.setBindings({
        { 4 * sizeof(float) }
    });
    inputLayout.setAttributes({
        { 0, 0, QRhiVertexInputAttribute::Float2, 0 },
        { 0, 1, QRhiVertexInputAttribute::Float2, 2 * sizeof(float) }
    });
    pipeline->setVertexInputLayout(inputLayout);
    pipeline->setShaderResourceBindings(bindings);
    pipeline->setRenderPassDescriptor(m_renderPass.get());
    pipeline->create();
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 70, as _ZN19QVideoWindowPrivateD1Ev
inline QVideoWindowPrivate::~QVideoWindowPrivate()
{
    QObject::disconnect(m_sink.get(), &QVideoSink::videoFrameChanged,
            q, &QVideoWindow::setVideoFrame);
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 279, as _ZN19QVideoWindowPrivate4initEv
inline void QVideoWindowPrivate::init()
{
    if (initialized)
        return;
    initialized = true;

    initRhi();

    if (!m_rhi)
        backingStore = new QBackingStore(q);
    else
        m_sink->setRhi(m_rhi.get());
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 306, as _ZN19QVideoWindowPrivate6renderEv
inline void QVideoWindowPrivate::render()
{
    if (!initialized)
        init();

    if (!q->isExposed() || !isExposed)
        return;

    QRect rect(0, 0, q->width(), q->height());

    if (backingStore) {
        if (backingStore->size() != q->size())
            backingStore->resize(q->size());

        backingStore->beginPaint(rect);

        QPaintDevice *device = backingStore->paintDevice();
        if (!device)
            return;
        QPainter painter(device);

        QVideoFrame frame = m_texturePool.currentFrame();
        frame.paint(&painter, rect, { Qt::black, aspectRatioMode });
        painter.end();

        backingStore->endPaint();
        backingStore->flush(rect);
        return;
    }

    const VideoTransformation frameTransformation =
            qNormalizedFrameTransformation(m_texturePool.currentFrame().surfaceFormat());
    const QSize frameSize = qRotatedFramePresentationSize(m_texturePool.currentFrame());
    const QSize scaled = frameSize.scaled(rect.size(), aspectRatioMode);
    QRect videoRect = QRect(QPoint(0, 0), scaled);
    videoRect.moveCenter(rect.center());
    QRect subtitleRect = videoRect.intersected(rect);

    if (!m_hasSwapChain || (m_swapChain->currentPixelSize() != m_swapChain->surfacePixelSize()))
        resizeSwapChain();

    const auto requiredSwapChainFormat =
            qGetRequiredSwapChainFormat(m_texturePool.currentFrame().surfaceFormat());
    if (qShouldUpdateSwapChainFormat(m_swapChain.get(), requiredSwapChainFormat)) {
        releaseSwapChain();
        m_swapChain->setFormat(requiredSwapChainFormat);
        resizeSwapChain();
    }

    if (!m_hasSwapChain)
        return;

    QRhi::FrameOpResult r = m_rhi->beginFrame(m_swapChain.get());

    if (r == QRhi::FrameOpSwapChainOutOfDate) {
        resizeSwapChain();
        if (!m_hasSwapChain)
            return;
        r = m_rhi->beginFrame(m_swapChain.get());
    }
    if (r != QRhi::FrameOpSuccess) {
        qWarning("beginFrame failed with %d, retry", r);
        q->requestUpdate();
        return;
    }

    QRhiResourceUpdateBatch *rub = m_rhi->nextResourceUpdateBatch();

    if (!m_vertexBufReady) {
        m_vertexBufReady = true;
        rub->uploadStaticBuffer(m_vertexBuf.get(), g_vw_quad);
    }

    updateTextures(rub);

    if (m_subtitleDirty || m_subtitleLayout.videoSize != subtitleRect.size())
        updateSubtitle(rub, subtitleRect.size());

    const float mirrorFrame = frameTransformation.mirroredHorizontallyAfterRotation ? -1.f : 1.f;
    const float xscale = mirrorFrame * float(videoRect.width()) / float(rect.width());
    const float yscale = -1.f * float(videoRect.height()) / float(rect.height());

    QMatrix4x4 transform;
    transform.scale(xscale, yscale);

    float maxNits = 100;
    if (m_swapChain->format() == QRhiSwapChain::HDRExtendedSrgbLinear) {
        auto info = m_swapChain->hdrInfo();
        if (info.limitsType == QRhiSwapChainHdrInfo::ColorComponentValue)
            maxNits = 100 * info.limits.colorComponentValue.maxColorComponentValue;
        else
            maxNits = info.limits.luminanceInNits.maxLuminance;
    }

    QByteArray uniformData;
    QVideoTextureHelper::updateUniformData(&uniformData, m_rhi.get(),
                                           m_texturePool.currentFrame().surfaceFormat(),
                                           m_texturePool.currentFrame(), transform, 1.f, maxNits);
    rub->updateDynamicBuffer(m_uniformBuf.get(), 0, uniformData.size(), uniformData.constData());

    if (m_hasSubtitle) {
        QMatrix4x4 st;
        st.translate(0, -2.f * (float(m_subtitleLayout.bounds.center().y())  + float(subtitleRect.top()))/ float(rect.height()) + 1.f);
        st.scale(float(m_subtitleLayout.bounds.width())/float(rect.width()),
                -1.f * float(m_subtitleLayout.bounds.height())/float(rect.height()));

        QByteArray uniformData;
        QVideoFrameFormat fmt(m_subtitleLayout.bounds.size().toSize(), QVideoFrameFormat::Format_ARGB8888);
        QVideoTextureHelper::updateUniformData(&uniformData, m_rhi.get(), fmt, QVideoFrame(), st,
                                               1.f);
        rub->updateDynamicBuffer(m_subtitleUniformBuf.get(), 0, uniformData.size(), uniformData.constData());
    }

    QRhiCommandBuffer *cb = m_swapChain->currentFrameCommandBuffer();
    cb->beginPass(m_swapChain->currentFrameRenderTarget(), Qt::black, { 1.0f, 0 }, rub);
    cb->setGraphicsPipeline(m_graphicsPipeline.get());
    auto size = m_swapChain->currentPixelSize();
    cb->setViewport({ 0, 0, float(size.width()), float(size.height()) });
    cb->setShaderResources(m_shaderResourceBindings.get());

    const quint32 vertexOffset = quint32(sizeof(float)) * 16 * frameTransformation.rotationIndex();
    const QRhiCommandBuffer::VertexInput vbufBinding(m_vertexBuf.get(), vertexOffset);
    cb->setVertexInput(0, 1, &vbufBinding);
    cb->draw(4);

    if (m_hasSubtitle) {
        cb->setGraphicsPipeline(m_subtitlePipeline.get());
        cb->setShaderResources(m_subtitleResourceBindings.get());
        const QRhiCommandBuffer::VertexInput vbufBinding(m_vertexBuf.get(), 0);
        cb->setVertexInput(0, 1, &vbufBinding);
        cb->draw(4);
    }

    cb->endPass();

    m_rhi->endFrame(m_swapChain.get());

    m_texturePool.onFrameEndInvoked();
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 293, as _ZN19QVideoWindowPrivate15resizeSwapChainEv
inline void QVideoWindowPrivate::resizeSwapChain()
{
    m_hasSwapChain = m_swapChain->createOrResize();
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 298, as _ZN19QVideoWindowPrivate16releaseSwapChainEv
inline void QVideoWindowPrivate::releaseSwapChain()
{
    if (m_hasSwapChain) {
        m_hasSwapChain = false;
        m_swapChain->destroy();
    }
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 204, as _ZN19QVideoWindowPrivate14updateTexturesEP23QRhiResourceUpdateBatch
inline void QVideoWindowPrivate::updateTextures(QRhiResourceUpdateBatch *rub)
{
    // We render a 1x1 black pixel when we don't have a video
    if (!m_texturePool.currentFrame().isValid())
        m_texturePool.setCurrentFrame(QVideoFramePrivate::createFrame(
                std::make_unique<QMemoryVideoBuffer>(QByteArray{ 4, 0 }, 4),
                QVideoFrameFormat(QSize(1, 1), QVideoFrameFormat::Format_RGBA8888)));

    if (!m_texturePool.texturesDirty())
        return;

    QVideoFrameTextures *textures = m_texturePool.updateTextures(*m_rhi, *rub);
    if (!textures)
        return;

    QRhiShaderResourceBinding bindings[4];
    auto *b = bindings;
    *(b++) = QRhiShaderResourceBinding::uniformBuffer(0, QRhiShaderResourceBinding::VertexStage | QRhiShaderResourceBinding::FragmentStage,
                                                   m_uniformBuf.get());

    auto fmt = m_texturePool.currentFrame().surfaceFormat();
    auto textureDesc = QVideoTextureHelper::textureDescription(fmt.pixelFormat());

    for (int i = 0; i < textureDesc->nplanes; ++i)
        (*b++) = QRhiShaderResourceBinding::sampledTexture(
                i + 1, QRhiShaderResourceBinding::FragmentStage, textures->texture(i),
                m_textureSampler.get());
    m_shaderResourceBindings->setBindings(bindings, b);
    m_shaderResourceBindings->create();

    if (fmt != format) {
        format = fmt;
        if (!m_graphicsPipeline)
            m_graphicsPipeline.reset(m_rhi->newGraphicsPipeline());

        setupGraphicsPipeline(m_graphicsPipeline.get(), m_shaderResourceBindings.get(), format);
    }
}

//  from ../qtmultimedia/src/multimedia/video/qvideowindow.cpp, line 243, as _ZN19QVideoWindowPrivate14updateSubtitleEP23QRhiResourceUpdateBatchRK5QSize
inline void QVideoWindowPrivate::updateSubtitle(QRhiResourceUpdateBatch *rub, const QSize &frameSize)
{
    m_subtitleDirty = false;
    m_hasSubtitle = !m_texturePool.currentFrame().subtitleText().isEmpty();
    if (!m_hasSubtitle)
        return;

    m_subtitleLayout.update(frameSize, m_texturePool.currentFrame().subtitleText());
    QSize size = m_subtitleLayout.bounds.size().toSize();

    QImage img = m_subtitleLayout.toImage();

    m_subtitleTexture.reset(m_rhi->newTexture(QRhiTexture::RGBA8, size));
    m_subtitleTexture->create();
    rub->uploadTexture(m_subtitleTexture.get(), img);

    QRhiShaderResourceBinding bindings[2];

    bindings[0] = QRhiShaderResourceBinding::uniformBuffer(0, QRhiShaderResourceBinding::VertexStage | QRhiShaderResourceBinding::FragmentStage,
                                                           m_subtitleUniformBuf.get());

    bindings[1] = QRhiShaderResourceBinding::sampledTexture(1, QRhiShaderResourceBinding::FragmentStage,
                                                            m_subtitleTexture.get(), m_textureSampler.get());
    m_subtitleResourceBindings->setBindings(bindings, bindings + 2);
    m_subtitleResourceBindings->create();

    if (!m_subtitlePipeline) {
        m_subtitlePipeline.reset(m_rhi->newGraphicsPipeline());

        QRhiGraphicsPipeline::TargetBlend blend;
        blend.enable = true;
        m_subtitlePipeline->setTargetBlends({ blend });
        setupGraphicsPipeline(m_subtitlePipeline.get(), m_subtitleResourceBindings.get(), QVideoFrameFormat(QSize(1, 1), QVideoFrameFormat::Format_RGBA8888));
    }
}
//  -----------------------------------------------------------------------

//  QVideoWindowPrivate::~QVideoWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivateD1Ev(QVideoWindowPrivate *self) {
  delete self;
}

//  bool QVideoWindowPrivate::canRender() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QVideoWindowPrivate9canRenderEv(
    const QVideoWindowPrivate *self) {
  return self->canRender();
}

//  QRhi *QVideoWindowPrivate::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK19QVideoWindowPrivate3rhiEv(
    const QVideoWindowPrivate *self) {
  return self->rhi();
}

#if defined(Q_OS_LINUX)
//  void QVideoWindowPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate4initEv(QVideoWindowPrivate *self) {
  self->init();
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QVideoWindowPrivate::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate6renderEv(QVideoWindowPrivate *self) {
  self->render();
}
#endif  // defined(Q_OS_LINUX)

//  void QVideoWindowPrivate::resizeSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate15resizeSwapChainEv(
    QVideoWindowPrivate *self) {
  self->resizeSwapChain();
}

//  void QVideoWindowPrivate::releaseSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate16releaseSwapChainEv(
    QVideoWindowPrivate *self) {
  self->releaseSwapChain();
}

//  void QVideoWindowPrivate::updateTextures(QRhiResourceUpdateBatch *rub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate14updateTexturesEP23QRhiResourceUpdateBatch(
    QVideoWindowPrivate *self,
    QRhiResourceUpdateBatch *rub) {
  self->updateTextures(rub);
}

//  void QVideoWindowPrivate::updateSubtitle(QRhiResourceUpdateBatch *rub,
//      const QSize &frameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVideoWindowPrivate14updateSubtitleEP23QRhiResourceUpdateBatchRK5QSize(
    QVideoWindowPrivate *self,
    QRhiResourceUpdateBatch *rub,
    const QSize *frameSize) {
  self->updateSubtitle(rub, *frameSize);
}
