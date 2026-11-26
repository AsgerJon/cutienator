//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: the include of Qt's 'qrhivulkan_p.h' also stands under
//  '__has_include(<vulkan/vulkan.h>)', since it does not compile on a
//  machine without the headers of Vulkan. The OpenGL headers of macOS
//  lack 'GL_ALL_BARRIER_BITS' and 'GL_SHADER_STORAGE_BUFFER', which
//  Qt's code of 'QRhiGles2::beginExternal' uses, so the file defines
//  every constant of the code taken from Qt that Qt's 'qrhigles2.cpp'
//  defines for itself, with Qt's own '#ifndef' lines and values. The
//  line pulling in 'qrhid3d12_p.h' stands under
//  '__has_include(<D3D12MemAlloc.h>)': that header includes
//  'D3D12MemAlloc.h', a library Qt keeps in its source and never
//  installs, and no ritual here needs it. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#include <QtGui/6.12.0/QtGui/rhi/qshaderdescription.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhigles2_p.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpa/qplatformopenglcontext.h>
#include <QtCore/qmath.h>
#include <limits>
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  The constants Qt defines for itself where the OpenGL headers
//  lack them.
//  from src/gui/rhi/qrhigles2.cpp, line 293
#ifndef GL_DEPTH_STENCIL_ATTACHMENT
#define GL_DEPTH_STENCIL_ATTACHMENT       0x821A
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 337
#ifndef GL_SHADER_STORAGE_BUFFER
#define GL_SHADER_STORAGE_BUFFER          0x90D2
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 401
#ifndef GL_ALL_BARRIER_BITS
#define GL_ALL_BARRIER_BITS               0xFFFFFFFF
#endif
//  from src/gui/rhi/qrhigles2.cpp, line 457
#ifndef GL_PROGRAM_BINARY_LENGTH
#define GL_PROGRAM_BINARY_LENGTH          0x8741
#endif

//  from src/gui/rhi/qrhigles2.cpp, line 5870, as _ZN12QGles2BufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj
inline QGles2Buffer::QGles2Buffer(QRhiImplementation *rhi, Type type, UsageFlags usage, quint32 size)
    : QRhiBuffer(rhi, type, usage, size)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6428, as _ZN13QGles2SamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_
inline QGles2Sampler::QGles2Sampler(QRhiImplementation *rhi, Filter magFilter, Filter minFilter, Filter mipmapMode,
                             AddressMode u, AddressMode v, AddressMode w)
    : QRhiSampler(rhi, magFilter, minFilter, mipmapMode, u, v, w)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6151, as _ZN13QGles2TextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE
inline QGles2Texture::QGles2Texture(QRhiImplementation *rhi, Format format, const QSize &pixelSize, int depth,
                             int arraySize, int sampleCount, Flags flags)
    : QRhiTexture(rhi, format, pixelSize, depth, arraySize, sampleCount, flags)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 7211, as _ZN15QGles2SwapChainC1EP18QRhiImplementation
inline QGles2SwapChain::QGles2SwapChain(QRhiImplementation *rhi)
    : QRhiSwapChain(rhi),
      rt(rhi, this),
      rtLeft(rhi, this),
      rtRight(rhi, this),
      cb(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 5991, as _ZN18QGles2RenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE
inline QGles2RenderBuffer::QGles2RenderBuffer(QRhiImplementation *rhi, Type type, const QSize &pixelSize,
                                       int sampleCount, QRhiRenderBuffer::Flags flags,
                                       QRhiTexture::Format backingFormatHint)
    : QRhiRenderBuffer(rhi, type, pixelSize, sampleCount, flags, backingFormatHint)
{
}

//  from src/gui/rhi/qrhi.cpp, line 12217, as _ZN18QRhiImplementation28clampedSubResourceUploadSizeE5QSize6QPointiS0_b
inline QSize QRhiImplementation::clampedSubResourceUploadSize(QSize size, QPoint dstPos, int level, QSize textureSizeAtLevelZero, bool warn)
{
    const QSize subResSize = q->sizeForMipLevel(level, textureSizeAtLevelZero);
    const bool outOfBoundsHoriz = dstPos.x() + size.width() > subResSize.width();
    const bool outOfBoundsVert = dstPos.y() + size.height() > subResSize.height();
    if (Q_UNLIKELY(outOfBoundsHoriz || outOfBoundsVert)) {
        if (warn) {
            qWarning("Invalid texture upload issued; size %dx%d dst.position %d,%d dst.subresource size %dx%d; size will be clamped",
                     size.width(), size.height(), dstPos.x(), dstPos.y(), subResSize.width(), subResSize.height());
        }
        if (outOfBoundsHoriz)
            size.setWidth(subResSize.width() - dstPos.x());
        if (outOfBoundsVert)
            size.setHeight(subResSize.height() - dstPos.y());
    }
    return size;
}

//  from src/gui/rhi/qrhi.cpp, line 12239, as _ZN18QRhiImplementation41clampedSubResourceUploadSizeForSourceDataE5QSizejjxb
inline QSize QRhiImplementation::clampedSubResourceUploadSizeForSourceData(QSize size, quint32 bpl,
                                                                    quint32 bytesPerPixel,
                                                                    qsizetype dataSize, bool warn)
{
    if (size.isEmpty() || !bytesPerPixel)
        return size;

    const quint64 rowBytes = quint64(bytesPerPixel) * quint64(size.width());
    if (!bpl)
        bpl = quint32(qMin(rowBytes, quint64(std::numeric_limits<quint32>::max())));

    if (quint64(bpl) < rowBytes) {
        if (warn) {
            qWarning("Invalid texture upload issued; source row stride %u is smaller than the %llu "
                     "bytes a row of %d pixels needs; upload will be skipped",
                     bpl, rowBytes, size.width());
        }
        return QSize(size.width(), 0);
    }

    // Row y is read from y * bpl and needs rowBytes bytes, so the last row ends
    // at (height - 1) * bpl + rowBytes.
    const quint64 needed = quint64(bpl) * quint64(size.height() - 1) + rowBytes;
    if (quint64(dataSize) >= needed)
        return size;

    int rows = 0;
    if (quint64(dataSize) >= rowBytes)
        rows = int((quint64(dataSize) - rowBytes) / quint64(bpl)) + 1;

    if (warn) {
        qWarning("Invalid texture upload issued; %lld bytes of data cannot back a %dx%d upload with "
                 "source row stride %u (needs %llu bytes); height will be clamped to %d",
                 qint64(dataSize), size.width(), size.height(), bpl, needed, rows);
    }

    return QSize(size.width(), rows);
}

//  from src/gui/rhi/qrhigles2.cpp, line 7195, as _ZN19QGles2CommandBufferC1EP18QRhiImplementation
inline QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7201, as _ZN19QGles2CommandBufferD1Ev
inline QGles2CommandBuffer::~QGles2CommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7089, as _ZN21QGles2ComputePipelineC1EP18QRhiImplementation
inline QGles2ComputePipeline::QGles2ComputePipeline(QRhiImplementation *rhi)
    : QRhiComputePipeline(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6904, as _ZN22QGles2GraphicsPipelineC1EP18QRhiImplementation
inline QGles2GraphicsPipeline::QGles2GraphicsPipeline(QRhiImplementation *rhi)
    : QRhiGraphicsPipeline(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6529, as _ZN25QGles2TextureRenderTargetC1EP18QRhiImplementationRK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QGles2TextureRenderTarget::QGles2TextureRenderTarget(QRhiImplementation *rhi,
                                                     const QRhiTextureRenderTargetDescription &desc,
                                                     Flags flags)
    : QRhiTextureRenderTarget(rhi, desc, flags),
      d(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6857, as _ZN28QGles2ShaderResourceBindingsC1EP18QRhiImplementation
inline QGles2ShaderResourceBindings::QGles2ShaderResourceBindings(QRhiImplementation *rhi)
    : QRhiShaderResourceBindings(rhi)
{
}

//  from src/gui/rhi/qrhi.cpp, line 10208, as _ZN30QRhiResourceUpdateBatchPrivate4freeEv
inline void QRhiResourceUpdateBatchPrivate::free()
{
    Q_ASSERT(poolIndex >= 0 && rhi->resUpdPool[poolIndex] == q);

    quint32 bufferDataTotal = 0;
    quint32 bufferLargeAllocTotal = 0;
    for (const BufferOp &op : std::as_const(bufferOps)) {
        bufferDataTotal += op.data.size();
        bufferLargeAllocTotal += op.data.largeAlloc(); // alloc when > 1 KB
    }

    if (QRHI_LOG_RUB().isDebugEnabled()) {
        qDebug() << "[rub] release to pool upd.batch #" << poolIndex
                << "/ bufferOps active" << activeBufferOpCount
                << "of" << bufferOps.count()
                << "data" << bufferDataTotal
                << "largeAlloc" << bufferLargeAllocTotal
                << "textureOps active" << activeTextureOpCount
                << "of" << textureOps.count();
    }

    activeBufferOpCount = 0;
    activeTextureOpCount = 0;

    const quint64 mask = 1ULL << quint64(poolIndex);
    rhi->resUpdPoolMap &= ~mask;
    poolIndex = -1;

    // textureOps is cleared, to not keep the potentially large image pixel
    // data alive, but it is expected that the container keeps the list alloc
    // at least. Only trimOpList() goes for the more aggressive route with squeeze.
    textureOps.clear();

    // bufferOps is not touched in many cases, to allow reusing allocations
    // (incl. in the elements' QRhiBufferData) as much as possible when this
    // batch is used again in the future, which is important for performance, in
    // particular with Qt Quick where it is easy for scenes to produce lots of,
    // typically small buffer changes on every frame.
    //
    // However, ensure that even in the unlikely case of having the max number
    // of batches (64) created in resUpdPool, no more than 64 MB in total is
    // used up by buffer data just to help future reuse. For simplicity, if
    // there is more than 1 MB data -> clear. Applications with frequent, huge
    // buffer updates probably have other bottlenecks anyway.
    if (bufferLargeAllocTotal > 1024 * 1024)
        bufferOps.clear();
}

//  from src/gui/rhi/qrhigles2.cpp, line 2162, as _ZN9QRhiGles214setVertexInputEP17QRhiCommandBufferiiPKSt4pairIP10QRhiBufferjES4_jNS0_11IndexFormatE
inline void QRhiGles2::setVertexInput(QRhiCommandBuffer *cb,
                               int startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput *bindings,
                               QRhiBuffer *indexBuf, quint32 indexOffset, QRhiCommandBuffer::IndexFormat indexFormat)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);
    QRhiPassResourceTracker &passResTracker(cbD->passResTrackers[cbD->currentPassResTrackerIndex]);

    for (int i = 0; i < bindingCount; ++i) {
        QRhiBuffer *buf = bindings[i].first;
        quint32 ofs = bindings[i].second;
        QGles2Buffer *bufD = QRHI_RES(QGles2Buffer, buf);
        Q_ASSERT(bufD->m_usage.testFlag(QRhiBuffer::VertexBuffer));

        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::BindVertexBuffer;
        cmd.args.bindVertexBuffer.ps = cbD->currentGraphicsPipeline;
        cmd.args.bindVertexBuffer.buffer = bufD->buffer;
        cmd.args.bindVertexBuffer.offset = ofs;
        cmd.args.bindVertexBuffer.binding = startBinding + i;

        if (cbD->passNeedsResourceTracking) {
            trackedRegisterBuffer(&passResTracker, bufD, QRhiPassResourceTracker::BufVertexInput,
                                  QRhiPassResourceTracker::BufVertexInputStage);
        }
    }

    if (indexBuf) {
        QGles2Buffer *ibufD = QRHI_RES(QGles2Buffer, indexBuf);
        Q_ASSERT(ibufD->m_usage.testFlag(QRhiBuffer::IndexBuffer));

        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::BindIndexBuffer;
        cmd.args.bindIndexBuffer.buffer = ibufD->buffer;
        cmd.args.bindIndexBuffer.offset = indexOffset;
        cmd.args.bindIndexBuffer.type = indexFormat == QRhiCommandBuffer::IndexUInt16 ? GL_UNSIGNED_SHORT : GL_UNSIGNED_INT;

        if (cbD->passNeedsResourceTracking) {
            trackedRegisterBuffer(&passResTracker, ibufD, QRhiPassResourceTracker::BufIndexRead,
                                  QRhiPassResourceTracker::BufVertexInputStage);
        }
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 2030, as _ZN9QRhiGles218setShaderResourcesEP17QRhiCommandBufferP26QRhiShaderResourceBindingsiPKSt4pairIijE
inline void QRhiGles2::setShaderResources(QRhiCommandBuffer *cb, QRhiShaderResourceBindings *srb,
                                   int dynamicOffsetCount,
                                   const QRhiCommandBuffer::DynamicOffset *dynamicOffsets)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass != QGles2CommandBuffer::NoPass);
    QGles2GraphicsPipeline *gfxPsD = QRHI_RES(QGles2GraphicsPipeline, cbD->currentGraphicsPipeline);
    QGles2ComputePipeline *compPsD = QRHI_RES(QGles2ComputePipeline, cbD->currentComputePipeline);

    if (!srb) {
        if (gfxPsD)
            srb = gfxPsD->m_shaderResourceBindings;
        else
            srb = compPsD->m_shaderResourceBindings;
    }

    QGles2ShaderResourceBindings *srbD = QRHI_RES(QGles2ShaderResourceBindings, srb);
    if (cbD->passNeedsResourceTracking) {
        QRhiPassResourceTracker &passResTracker(cbD->passResTrackers[cbD->currentPassResTrackerIndex]);
        for (int i = 0, ie = srbD->m_bindings.size(); i != ie; ++i) {
            const QRhiShaderResourceBinding::Data *b = shaderResourceBindingData(srbD->m_bindings.at(i));
            switch (b->type) {
            case QRhiShaderResourceBinding::UniformBuffer:
                // no BufUniformRead / AccessUniform because no real uniform buffers are used
                break;
            case QRhiShaderResourceBinding::SampledTexture:
            case QRhiShaderResourceBinding::Texture:
                for (int elem = 0; elem < b->u.stex.count; ++elem) {
                    QGles2Texture *texD = QRHI_RES(QGles2Texture, b->u.stex.texSamplers[elem].tex);
                    sanityCheckResourceOwnership(texD);
                    trackedRegisterTexture(&passResTracker,
                                           texD,
                                           QRhiPassResourceTracker::TexSample,
                                           QRhiPassResourceTracker::toPassTrackerTextureStage(b->stage));
                }
                break;
            case QRhiShaderResourceBinding::ImageLoad:
            case QRhiShaderResourceBinding::ImageStore:
            case QRhiShaderResourceBinding::ImageLoadStore:
            {
                QGles2Texture *texD = QRHI_RES(QGles2Texture, b->u.simage.tex);
                sanityCheckResourceOwnership(texD);
                QRhiPassResourceTracker::TextureAccess access;
                if (b->type == QRhiShaderResourceBinding::ImageLoad)
                    access = QRhiPassResourceTracker::TexStorageLoad;
                else if (b->type == QRhiShaderResourceBinding::ImageStore)
                    access = QRhiPassResourceTracker::TexStorageStore;
                else
                    access = QRhiPassResourceTracker::TexStorageLoadStore;
                trackedRegisterTexture(&passResTracker, texD, access,
                                       QRhiPassResourceTracker::toPassTrackerTextureStage(b->stage));
            }
                break;
            case QRhiShaderResourceBinding::BufferLoad:
            case QRhiShaderResourceBinding::BufferStore:
            case QRhiShaderResourceBinding::BufferLoadStore:
            {
                QGles2Buffer *bufD = QRHI_RES(QGles2Buffer, b->u.sbuf.buf);
                sanityCheckResourceOwnership(bufD);
                QRhiPassResourceTracker::BufferAccess access;
                if (b->type == QRhiShaderResourceBinding::BufferLoad)
                    access = QRhiPassResourceTracker::BufStorageLoad;
                else if (b->type == QRhiShaderResourceBinding::BufferStore)
                    access = QRhiPassResourceTracker::BufStorageStore;
                else
                    access = QRhiPassResourceTracker::BufStorageLoadStore;
                trackedRegisterBuffer(&passResTracker, bufD, access,
                                      QRhiPassResourceTracker::toPassTrackerBufferStage(b->stage));
            }
                break;
            default:
                break;
            }
        }
    }

    bool srbChanged = gfxPsD ? (cbD->currentGraphicsSrb != srb) : (cbD->currentComputeSrb != srb);

    // The Command::BindShaderResources command generated below is what will
    // cause uniforms to be set (glUniformNxx). This needs some special
    // handling here in this backend without real uniform buffers, because,
    // like in other backends, we optimize out the setShaderResources when the
    // srb that was set before is attempted to be set again on the command
    // buffer, but that is incorrect if the same srb is now used with another
    // pipeline. (because that could mean a glUseProgram not followed by
    // up-to-date glUniform calls, i.e. with GL we have a strong dependency
    // between the pipeline (== program) and the srb, unlike other APIs) This
    // is the reason there is a second level of srb(+generation) tracking in
    // the pipeline objects.
    if (gfxPsD && (gfxPsD->currentSrb != srb || gfxPsD->currentSrbGeneration != srbD->generation)) {
        srbChanged = true;
        gfxPsD->currentSrb = srb;
        gfxPsD->currentSrbGeneration = srbD->generation;
    } else if (compPsD && (compPsD->currentSrb != srb || compPsD->currentSrbGeneration != srbD->generation)) {
        srbChanged = true;
        compPsD->currentSrb = srb;
        compPsD->currentSrbGeneration = srbD->generation;
    }

    if (srbChanged || cbD->currentSrbGeneration != srbD->generation || srbD->hasDynamicOffset) {
        if (gfxPsD) {
            cbD->currentGraphicsSrb = srb;
            cbD->currentComputeSrb = nullptr;
        } else {
            cbD->currentGraphicsSrb = nullptr;
            cbD->currentComputeSrb = srb;
        }
        cbD->currentSrbGeneration = srbD->generation;

        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::BindShaderResources;
        cmd.args.bindShaderResources.maybeGraphicsPs = gfxPsD;
        cmd.args.bindShaderResources.maybeComputePs = compPsD;
        cmd.args.bindShaderResources.srb = srb;
        cmd.args.bindShaderResources.dynamicOffsetCount = 0;
        if (srbD->hasDynamicOffset) {
            if (dynamicOffsetCount < QGles2CommandBuffer::MAX_DYNAMIC_OFFSET_COUNT) {
                cmd.args.bindShaderResources.dynamicOffsetCount = dynamicOffsetCount;
                uint *p = cmd.args.bindShaderResources.dynamicOffsetPairs;
                for (int i = 0; i < dynamicOffsetCount; ++i) {
                    const QRhiCommandBuffer::DynamicOffset &dynOfs(dynamicOffsets[i]);
                    *p++ = uint(dynOfs.first);
                    *p++ = dynOfs.second;
                }
            } else {
                qWarning("Too many dynamic offsets (%d, max is %d)",
                         dynamicOffsetCount, QGles2CommandBuffer::MAX_DYNAMIC_OFFSET_COUNT);
            }
        }
    }
}

//  from src/gui/rhi/qrhi.cpp, line 8782, as _ZNK18QRhiImplementation17textureFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_S5_
inline bool QRhiImplementation::textureFormatInfo(QRhiTexture::Format format, const QSize &size,
                                           quint32 *bpl, quint32 *byteSize, quint32 *bytesPerPixel) const
{
    if (isCompressedFormat(format))
        return compressedFormatInfo(format, size, bpl, byteSize, nullptr);

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
        Q_UNREACHABLE();
        break;
    }

    const quint32 width = uint(qMax(0, size.width()));
    const quint32 height = uint(qMax(0, size.height()));

    if (bytesPerPixel)
        *bytesPerPixel = bpc;

    // Compute in 64-bit, as safety for extreme geometry that would not fit.
    const quint64 bytesPerLine = quint64(width) * quint64(bpc);
    const quint64 pixelCount = quint64(width) * quint64(height);
    if (bytesPerLine > std::numeric_limits<quint32>::max()
        || pixelCount > std::numeric_limits<quint32>::max() / bpc)
    {
        qWarning("Texture of size %dx%d with format %d has a byte size "
                 "which is too large to be handled",
                 size.width(), size.height(), int(format));
        if (bpl)
            *bpl = 0;
        if (byteSize)
            *byteSize = 0;
        return false;
    }

    if (bpl)
        *bpl = quint32(bytesPerLine);
    if (byteSize)
        *byteSize = quint32(pixelCount * quint64(bpc));

    return true;
}

//  from src/gui/rhi/qrhi.cpp, line 8635, as _ZNK18QRhiImplementation18isCompressedFormatEN11QRhiTexture6FormatE
inline bool QRhiImplementation::isCompressedFormat(QRhiTexture::Format format) const
{
    return (format >= QRhiTexture::BC1 && format <= QRhiTexture::BC7)
            || (format >= QRhiTexture::ETC2_RGB8 && format <= QRhiTexture::ETC2_RGBA8)
            || (format >= QRhiTexture::ASTC_4x4 && format <= QRhiTexture::ASTC_12x12);
}

//  from src/gui/rhi/qrhi.cpp, line 8642, as _ZNK18QRhiImplementation20compressedFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_PS2_
inline bool QRhiImplementation::compressedFormatInfo(QRhiTexture::Format format, const QSize &size,
                                              quint32 *bpl, quint32 *byteSize,
                                              QSize *blockDim) const
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
        Q_UNREACHABLE();
        break;
    }

    const quint32 wblocks = quint32((qint64(qMax(0, size.width())) + xdim - 1) / xdim);
    const quint32 hblocks = quint32((qint64(qMax(0, size.height())) + ydim - 1) / ydim);

    if (blockDim)
        *blockDim = QSize(xdim, ydim);

    // Compute in 64-bit, as safety for extreme geometry that would not fit.
    // wblocks and hblocks are at most 2^29 and blockSize at most 16.
    const quint64 bytesPerLine = quint64(wblocks) * quint64(blockSize);
    const quint64 totalSize = quint64(wblocks) * quint64(hblocks) * quint64(blockSize);
    if (bytesPerLine > std::numeric_limits<quint32>::max()
        || totalSize > std::numeric_limits<quint32>::max())
    {
        qWarning("Compressed texture of size %dx%d with format %d has a byte size of %llu "
                 "which is too large to be handled",
                 size.width(), size.height(), int(format), totalSize);
        if (bpl)
            *bpl = 0;
        if (byteSize)
            *byteSize = 0;
        return false;
    }

    if (bpl)
        *bpl = quint32(bytesPerLine);
    if (byteSize)
        *byteSize = quint32(totalSize);

    return true;
}

//  from src/gui/rhi/qrhi.cpp, line 9181, as _ZNK18QRhiImplementation29enumerateAdaptersBeforeCreateEP17QRhiNativeHandles
inline QRhi::AdapterList QRhiImplementation::enumerateAdaptersBeforeCreate(QRhiNativeHandles *) const
{
    return {};
}

//  from src/gui/rhi/qrhigles2.cpp, line 1351, as _ZNK9QRhiGles221supportedSampleCountsEv
inline QList<int> QRhiGles2::supportedSampleCounts() const
{
    if (supportedSampleCountList.isEmpty()) {
        // 1, 2, 4, 8, ...
        for (int i = 1; i <= caps.maxSamples; i *= 2)
            supportedSampleCountList.append(i);
    }
    return supportedSampleCountList;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7206, as _ZN19QGles2CommandBuffer7destroyEv
inline void QGles2CommandBuffer::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhigles2.cpp, line 6498, as _ZN27QGles2SwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QGles2SwapChainRenderTarget::QGles2SwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6504, as _ZN27QGles2SwapChainRenderTargetD1Ev
inline QGles2SwapChainRenderTarget::~QGles2SwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 1290, as _ZN9QRhiGles27destroyEv
inline void QRhiGles2::destroy()
{
    if (!f)
        return;

    if (ensureContext()) {
        executeDeferredReleases();

        if (ofr.tsQueries[0]) {
            f->glDeleteQueries(2, ofr.tsQueries);
            ofr.tsQueries[0] = ofr.tsQueries[1] = 0;
        }

        if (vao) {
            f->glDeleteVertexArrays(1, &vao);
            vao = 0;
        }

        for (uint shader : std::as_const(m_shaderCache))
            f->glDeleteShader(shader);
        m_shaderCache.clear();
    }

    if (!importedContext) {
        delete ctx;
        ctx = nullptr;
    }

    f = nullptr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1992, as _ZN9QRhiGles222createGraphicsPipelineEv
inline QRhiGraphicsPipeline *QRhiGles2::createGraphicsPipeline()
{
    return new QGles2GraphicsPipeline(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2002, as _ZN9QRhiGles221createComputePipelineEv
inline QRhiComputePipeline *QRhiGles2::createComputePipeline()
{
    return new QGles2ComputePipeline(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1997, as _ZN9QRhiGles228createShaderResourceBindingsEv
inline QRhiShaderResourceBindings *QRhiGles2::createShaderResourceBindings()
{
    return new QGles2ShaderResourceBindings(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1372, as _ZN9QRhiGles212createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj
inline QRhiBuffer *QRhiGles2::createBuffer(QRhiBuffer::Type type, QRhiBuffer::UsageFlags usage, quint32 size)
{
    return new QGles2Buffer(this, type, usage, size);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1960, as _ZN9QRhiGles218createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE
inline QRhiRenderBuffer *QRhiGles2::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize &pixelSize,
                                                int sampleCount, QRhiRenderBuffer::Flags flags,
                                                QRhiTexture::Format backingFormatHint)
{
    return new QGles2RenderBuffer(this, type, pixelSize, sampleCount, flags, backingFormatHint);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1967, as _ZN9QRhiGles213createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE
inline QRhiTexture *QRhiGles2::createTexture(QRhiTexture::Format format,
                                      const QSize &pixelSize, int depth, int arraySize,
                                      int sampleCount, QRhiTexture::Flags flags)
{
    return new QGles2Texture(this, format, pixelSize, depth, arraySize, sampleCount, flags);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1974, as _ZN9QRhiGles213createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_
inline QRhiSampler *QRhiGles2::createSampler(QRhiSampler::Filter magFilter, QRhiSampler::Filter minFilter,
                                      QRhiSampler::Filter mipmapMode,
                                      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v, QRhiSampler::AddressMode w)
{
    return new QGles2Sampler(this, magFilter, minFilter, mipmapMode, u, v, w);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1986, as _ZN9QRhiGles225createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QRhiTextureRenderTarget *QRhiGles2::createTextureRenderTarget(const QRhiTextureRenderTargetDescription &desc,
                                                              QRhiTextureRenderTarget::Flags flags)
{
    return new QGles2TextureRenderTarget(this, desc, flags);
}

//  from src/gui/rhi/qrhigles2.cpp, line 1981, as _ZN9QRhiGles220createShadingRateMapEv
inline QRhiShadingRateMap *QRhiGles2::createShadingRateMap()
{
    return nullptr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1367, as _ZN9QRhiGles215createSwapChainEv
inline QRhiSwapChain *QRhiGles2::createSwapChain()
{
    return new QGles2SwapChain(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2580, as _ZN9QRhiGles26finishEv
inline QRhi::FrameOpResult QRhiGles2::finish()
{
    if (inFrame) {
        if (ofr.active) {
            Q_ASSERT(!currentSwapChain);
            Q_ASSERT(ofr.cbWrapper.recordingPass == QGles2CommandBuffer::NoPass);
            if (!ensureContext())
                return contextLost ? QRhi::FrameOpDeviceLost : QRhi::FrameOpError;
            executeCommandBuffer(&ofr.cbWrapper);
            ofr.cbWrapper.resetCommands();
        } else {
            Q_ASSERT(currentSwapChain);
            Q_ASSERT(currentSwapChain->cb.recordingPass == QGles2CommandBuffer::NoPass);
            if (!ensureContext(currentSwapChain->surface))
                return contextLost ? QRhi::FrameOpDeviceLost : QRhi::FrameOpError;
            executeCommandBuffer(&currentSwapChain->cb);
            currentSwapChain->cb.resetCommands();
        }
        // Do an actual glFinish(). May seem superfluous, but this is what
        // matches most other backends e.g. Vulkan/Metal that do a heavyweight
        // wait-for-idle blocking in their finish(). More importantly, this
        // allows clients simply call finish() in threaded or shared context
        // situations where one explicitly needs to do a glFlush or Finish.
        f->glFinish();
    }
    return QRhi::FrameOpSuccess;
}

//  from src/gui/rhi/qrhigles2.cpp, line 4958, as _ZN9QRhiGles214resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiGles2::resourceUpdate(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    Q_ASSERT(QRHI_RES(QGles2CommandBuffer, cb)->recordingPass == QGles2CommandBuffer::NoPass);

    enqueueResourceUpdates(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhigles2.cpp, line 5047, as _ZN9QRhiGles29beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiGles2::beginPass(QRhiCommandBuffer *cb,
                          QRhiRenderTarget *rt,
                          const QColor &colorClearValue,
                          const QRhiDepthStencilClearValue &depthStencilClearValue,
                          QRhiResourceUpdateBatch *resourceUpdates,
                          QRhiCommandBuffer::BeginPassFlags flags)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);

    // Get a new resource tracker. Then add a command that will generate
    // glMemoryBarrier() calls based on that tracker when submitted.
    enqueueBarriersForPass(cbD);

    if (rt->resourceType() == QRhiRenderTarget::TextureRenderTarget) {
        QGles2TextureRenderTarget *rtTex = QRHI_RES(QGles2TextureRenderTarget, rt);
        if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QGles2Texture, QGles2RenderBuffer>(rtTex->description(), rtTex->d.currentResIdList))
            rtTex->create();
    }

    bool wantsColorClear, wantsDsClear;
    QGles2RenderTargetData *rtD = enqueueBindFramebuffer(rt, cbD, &wantsColorClear, &wantsDsClear);

    QGles2CommandBuffer::Command &clearCmd(cbD->commands.get());
    clearCmd.cmd = QGles2CommandBuffer::Command::Clear;
    clearCmd.args.clear.mask = 0;
    if (rtD->colorAttCount && wantsColorClear)
        clearCmd.args.clear.mask |= GL_COLOR_BUFFER_BIT;
    if (rtD->dsAttCount && wantsDsClear)
        clearCmd.args.clear.mask |= GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT;
    clearCmd.args.clear.c[0] = colorClearValue.redF();
    clearCmd.args.clear.c[1] = colorClearValue.greenF();
    clearCmd.args.clear.c[2] = colorClearValue.blueF();
    clearCmd.args.clear.c[3] = colorClearValue.alphaF();
    clearCmd.args.clear.d = depthStencilClearValue.depthClearValue();
    clearCmd.args.clear.s = depthStencilClearValue.stencilClearValue();

    cbD->recordingPass = QGles2CommandBuffer::RenderPass;
    cbD->passNeedsResourceTracking = !flags.testFlag(QRhiCommandBuffer::DoNotTrackResourcesForCompute);
    cbD->currentTarget = rt;

    cbD->resetCachedState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 5094, as _ZN9QRhiGles27endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiGles2::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    if (cbD->currentTarget->resourceType() == QRhiResource::TextureRenderTarget) {
        QGles2TextureRenderTarget *rtTex = QRHI_RES(QGles2TextureRenderTarget, cbD->currentTarget);
        for (auto it = rtTex->m_desc.cbeginColorAttachments(), itEnd = rtTex->m_desc.cendColorAttachments();
             it != itEnd; ++it)
        {
            const QRhiColorAttachment &colorAtt(*it);
            if (!colorAtt.resolveTexture())
                continue;

            QGles2Texture *resolveTexD = QRHI_RES(QGles2Texture, colorAtt.resolveTexture());
            const QSize size = resolveTexD->pixelSize();
            if (colorAtt.renderBuffer()) {
                QGles2RenderBuffer *rbD = QRHI_RES(QGles2RenderBuffer, colorAtt.renderBuffer());
                if (rbD->pixelSize() != size) {
                    qWarning("Resolve source (%dx%d) and target (%dx%d) size does not match",
                             rbD->pixelSize().width(), rbD->pixelSize().height(), size.width(), size.height());
                }
                if (caps.glesMultisampleRenderToTexture) {
                    // colorAtt.renderBuffer() is not actually used for anything if OpenGL ES'
                    // auto-resolving GL_EXT_multisampled_render_to_texture is used.
                } else {
                    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
                    cmd.cmd = QGles2CommandBuffer::Command::BlitFromRenderbuffer;
                    cmd.args.blitFromRenderbuffer.renderbuffer = rbD->renderbuffer;
                    cmd.args.blitFromRenderbuffer.w = size.width();
                    cmd.args.blitFromRenderbuffer.h = size.height();
                    if (resolveTexD->m_flags.testFlag(QRhiTexture::CubeMap))
                        cmd.args.blitFromRenderbuffer.target = GL_TEXTURE_CUBE_MAP_POSITIVE_X + uint(colorAtt.resolveLayer());
                    else
                        cmd.args.blitFromRenderbuffer.target = resolveTexD->target;
                    cmd.args.blitFromRenderbuffer.dstTexture = resolveTexD->texture;
                    cmd.args.blitFromRenderbuffer.dstLevel = colorAtt.resolveLevel();
                    const bool hasZ = resolveTexD->m_flags.testFlag(QRhiTexture::ThreeDimensional)
                        || resolveTexD->m_flags.testFlag(QRhiTexture::TextureArray);
                    cmd.args.blitFromRenderbuffer.dstLayer = hasZ ? colorAtt.resolveLayer() : 0;
                    cmd.args.blitFromRenderbuffer.isDepthStencil = false;
                }
            } else if (caps.glesMultisampleRenderToTexture) {
                // Nothing to do, resolving into colorAtt.resolveTexture() is automatic,
                // colorAtt.texture() is in fact not used for anything.
            } else {
                Q_ASSERT(colorAtt.texture());
                QGles2Texture *texD = QRHI_RES(QGles2Texture, colorAtt.texture());
                if (texD->pixelSize() != size) {
                    qWarning("Resolve source (%dx%d) and target (%dx%d) size does not match",
                             texD->pixelSize().width(), texD->pixelSize().height(), size.width(), size.height());
                }
                const int resolveCount = colorAtt.multiViewCount() >= 2 ? colorAtt.multiViewCount() : 1;
                for (int resolveIdx = 0; resolveIdx < resolveCount; ++resolveIdx) {
                    const int srcLayer = colorAtt.layer() + resolveIdx;
                    const int dstLayer = colorAtt.resolveLayer() + resolveIdx;
                    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
                    cmd.cmd = QGles2CommandBuffer::Command::BlitFromTexture;
                    if (texD->m_flags.testFlag(QRhiTexture::CubeMap))
                        cmd.args.blitFromTexture.srcTarget = GL_TEXTURE_CUBE_MAP_POSITIVE_X + uint(srcLayer);
                    else
                        cmd.args.blitFromTexture.srcTarget = texD->target;
                    cmd.args.blitFromTexture.srcTexture = texD->texture;
                    cmd.args.blitFromTexture.srcLevel = colorAtt.level();
                    cmd.args.blitFromTexture.srcLayer = 0;
                    if (texD->m_flags.testFlag(QRhiTexture::ThreeDimensional) || texD->m_flags.testFlag(QRhiTexture::TextureArray))
                        cmd.args.blitFromTexture.srcLayer = srcLayer;
                    cmd.args.blitFromTexture.w = size.width();
                    cmd.args.blitFromTexture.h = size.height();
                    if (resolveTexD->m_flags.testFlag(QRhiTexture::CubeMap))
                        cmd.args.blitFromTexture.dstTarget = GL_TEXTURE_CUBE_MAP_POSITIVE_X + uint(dstLayer);
                    else
                        cmd.args.blitFromTexture.dstTarget = resolveTexD->target;
                    cmd.args.blitFromTexture.dstTexture = resolveTexD->texture;
                    cmd.args.blitFromTexture.dstLevel = colorAtt.resolveLevel();
                    cmd.args.blitFromTexture.dstLayer = 0;
                    if (resolveTexD->m_flags.testFlag(QRhiTexture::ThreeDimensional) || resolveTexD->m_flags.testFlag(QRhiTexture::TextureArray))
                        cmd.args.blitFromTexture.dstLayer = dstLayer;
                    cmd.args.blitFromTexture.isDepthStencil = false;
                }
            }
        }

        if (rtTex->m_desc.depthResolveTexture()) {
            QGles2Texture *depthResolveTexD = QRHI_RES(QGles2Texture, rtTex->m_desc.depthResolveTexture());
            const QSize size = depthResolveTexD->pixelSize();
            if (rtTex->m_desc.depthStencilBuffer()) {
                QGles2RenderBuffer *rbD = QRHI_RES(QGles2RenderBuffer, rtTex->m_desc.depthStencilBuffer());
                QGles2CommandBuffer::Command &cmd(cbD->commands.get());
                cmd.cmd = QGles2CommandBuffer::Command::BlitFromRenderbuffer;
                cmd.args.blitFromRenderbuffer.renderbuffer = rbD->renderbuffer;
                cmd.args.blitFromRenderbuffer.w = size.width();
                cmd.args.blitFromRenderbuffer.h = size.height();
                cmd.args.blitFromRenderbuffer.target = depthResolveTexD->target;
                cmd.args.blitFromRenderbuffer.dstTexture = depthResolveTexD->texture;
                cmd.args.blitFromRenderbuffer.dstLevel = 0;
                cmd.args.blitFromRenderbuffer.dstLayer = 0;
                cmd.args.blitFromRenderbuffer.isDepthStencil = true;
            } else if (caps.glesMultisampleRenderToTexture) {
                // Nothing to do, resolving into depthResolveTexture() is automatic.
            } else {
                QGles2Texture *depthTexD = QRHI_RES(QGles2Texture, rtTex->m_desc.depthTexture());
                const int resolveCount = depthTexD->arraySize() >= 2 ? depthTexD->arraySize() : 1;
                for (int resolveIdx = 0; resolveIdx < resolveCount; ++resolveIdx) {
                    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
                    cmd.cmd = QGles2CommandBuffer::Command::BlitFromTexture;
                    cmd.args.blitFromTexture.srcTarget = depthTexD->target;
                    cmd.args.blitFromTexture.srcTexture = depthTexD->texture;
                    cmd.args.blitFromTexture.srcLevel = 0;
                    cmd.args.blitFromTexture.srcLayer = resolveIdx;
                    cmd.args.blitFromTexture.w = size.width();
                    cmd.args.blitFromTexture.h = size.height();
                    cmd.args.blitFromTexture.dstTarget = depthResolveTexD->target;
                    cmd.args.blitFromTexture.dstTexture = depthResolveTexD->texture;
                    cmd.args.blitFromTexture.dstLevel = 0;
                    cmd.args.blitFromTexture.dstLayer = resolveIdx;
                    cmd.args.blitFromTexture.isDepthStencil = true;
                }
            }
        }

        const bool mayDiscardDepthStencil =
            (rtTex->m_desc.depthStencilBuffer()
             || (rtTex->m_desc.depthTexture() && rtTex->m_flags.testFlag(QRhiTextureRenderTarget::DoNotStoreDepthStencilContents)))
            && !rtTex->m_desc.depthResolveTexture();
        if (mayDiscardDepthStencil) {
            QGles2CommandBuffer::Command &cmd(cbD->commands.get());
            cmd.cmd = QGles2CommandBuffer::Command::InvalidateFramebuffer;
            cmd.args.invalidateFramebuffer.fbo = rtTex->framebuffer;
            if (caps.needsDepthStencilCombinedAttach) {
                cmd.args.invalidateFramebuffer.attCount = 1;
                cmd.args.invalidateFramebuffer.att[0] = GL_DEPTH_STENCIL_ATTACHMENT;
            } else {
                cmd.args.invalidateFramebuffer.attCount = 2;
                cmd.args.invalidateFramebuffer.att[0] = GL_DEPTH_ATTACHMENT;
                cmd.args.invalidateFramebuffer.att[1] = GL_STENCIL_ATTACHMENT;
            }
        }
    }

    cbD->recordingPass = QGles2CommandBuffer::NoPass;
    cbD->currentTarget = nullptr;

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2007, as _ZN9QRhiGles219setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline
inline void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb, QRhiGraphicsPipeline *ps)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);
    QGles2GraphicsPipeline *psD = QRHI_RES(QGles2GraphicsPipeline, ps);
    const bool pipelineChanged = cbD->currentGraphicsPipeline != ps || cbD->currentPipelineGeneration != psD->generation;

    if (pipelineChanged) {
        cbD->currentGraphicsPipeline = ps;
        cbD->currentComputePipeline = nullptr;
        cbD->currentPipelineGeneration = psD->generation;
        if (psD->lastUsedInFrameNo != frameNo) {
            psD->lastUsedInFrameNo = frameNo;
            psD->currentSrb = nullptr;
            psD->currentSrbGeneration = 0;
        }

        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::BindGraphicsPipeline;
        cmd.args.bindGraphicsPipeline.ps = ps;
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 2206, as _ZN9QRhiGles211setViewportEP17QRhiCommandBufferRK12QRhiViewport
inline void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const QRhiViewport &viewport)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    const std::array<float, 4> r = viewport.viewport();
    // A negative width or height is an error. A negative x or y is not.
    if (r[2] < 0.0f || r[3] < 0.0f)
        return;

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::Viewport;
    cmd.args.viewport.x = r[0];
    cmd.args.viewport.y = r[1];
    cmd.args.viewport.w = r[2];
    cmd.args.viewport.h = r[3];
    cmd.args.viewport.d0 = viewport.minDepth();
    cmd.args.viewport.d1 = viewport.maxDepth();
}

//  from src/gui/rhi/qrhigles2.cpp, line 2226, as _ZN9QRhiGles210setScissorEP17QRhiCommandBufferRK11QRhiScissor
inline void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const QRhiScissor &scissor)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    const std::array<int, 4> r = scissor.scissor();
    // A negative width or height is an error. A negative x or y is not.
    if (r[2] < 0 || r[3] < 0)
        return;

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::Scissor;
    cmd.args.scissor.x = r[0];
    cmd.args.scissor.y = r[1];
    cmd.args.scissor.w = r[2];
    cmd.args.scissor.h = r[3];
}

//  from src/gui/rhi/qrhigles2.cpp, line 2244, as _ZN9QRhiGles217setBlendConstantsEP17QRhiCommandBufferRK6QColor
inline void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::BlendConstants;
    cmd.args.blendConstants.r = c.redF();
    cmd.args.blendConstants.g = c.greenF();
    cmd.args.blendConstants.b = c.blueF();
    cmd.args.blendConstants.a = c.alphaF();
}

//  from src/gui/rhi/qrhigles2.cpp, line 2257, as _ZN9QRhiGles213setStencilRefEP17QRhiCommandBufferj
inline void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::StencilRef;
    cmd.args.stencilRef.ref = refValue;
    cmd.args.stencilRef.ps = cbD->currentGraphicsPipeline;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2268, as _ZN9QRhiGles214setShadingRateEP17QRhiCommandBufferRK5QSize
inline void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const QSize &coarsePixelSize)
{
    Q_UNUSED(cb);
    Q_UNUSED(coarsePixelSize);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2274, as _ZN9QRhiGles24drawEP17QRhiCommandBufferjjjj
inline void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
                     quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::Draw;
    cmd.args.draw.ps = cbD->currentGraphicsPipeline;
    cmd.args.draw.vertexCount = vertexCount;
    cmd.args.draw.firstVertex = firstVertex;
    cmd.args.draw.instanceCount = instanceCount;
    cmd.args.draw.baseInstance = firstInstance;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2289, as _ZN9QRhiGles211drawIndexedEP17QRhiCommandBufferjjjij
inline void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
                            quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32 firstInstance)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::DrawIndexed;
    cmd.args.drawIndexed.ps = cbD->currentGraphicsPipeline;
    cmd.args.drawIndexed.indexCount = indexCount;
    cmd.args.drawIndexed.firstIndex = firstIndex;
    cmd.args.drawIndexed.instanceCount = instanceCount;
    cmd.args.drawIndexed.baseInstance = firstInstance;
    cmd.args.drawIndexed.baseVertex = vertexOffset;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2305, as _ZN9QRhiGles212drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj
inline void QRhiGles2::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                             quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    if (!caps.drawIndirect)
        return;

    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2Buffer *indirectBufD = QRHI_RES(QGles2Buffer, indirectBuffer);

    if (cbD->passNeedsResourceTracking) {
        QRhiPassResourceTracker &passResTracker(cbD->passResTrackers[cbD->currentPassResTrackerIndex]);
        trackedRegisterBuffer(&passResTracker, indirectBufD,
                              QRhiPassResourceTracker::BufIndirectDraw,
                              QRhiPassResourceTracker::BufIndirectDrawStage);
    }

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::DrawIndirect;
    cmd.args.drawIndirect.ps = cbD->currentGraphicsPipeline;
    cmd.args.drawIndirect.buffer = indirectBufD->buffer;
    cmd.args.drawIndirect.offset = indirectBufferOffset;
    cmd.args.drawIndirect.drawCount = drawCount;
    cmd.args.drawIndirect.stride = stride;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2332, as _ZN9QRhiGles219drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj
inline void QRhiGles2::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                                    quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    if (!caps.drawIndirect)
        return;

    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::RenderPass);

    QGles2Buffer *indirectBufD = QRHI_RES(QGles2Buffer, indirectBuffer);

    if (cbD->passNeedsResourceTracking) {
        QRhiPassResourceTracker &passResTracker(cbD->passResTrackers[cbD->currentPassResTrackerIndex]);
        trackedRegisterBuffer(&passResTracker, indirectBufD,
                              QRhiPassResourceTracker::BufIndirectDraw,
                              QRhiPassResourceTracker::BufIndirectDrawStage);
    }

    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::DrawIndexedIndirect;
    cmd.args.drawIndexedIndirect.ps = cbD->currentGraphicsPipeline;
    cmd.args.drawIndexedIndirect.buffer = indirectBufD->buffer;
    cmd.args.drawIndexedIndirect.offset = indirectBufferOffset;
    cmd.args.drawIndexedIndirect.drawCount = drawCount;
    cmd.args.drawIndexedIndirect.stride = stride;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2359, as _ZN9QRhiGles214debugMarkBeginEP17QRhiCommandBufferRK10QByteArray
inline void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray &name)
{
    if (!debugMarkers)
        return;

    Q_UNUSED(cb);
    Q_UNUSED(name);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2368, as _ZN9QRhiGles212debugMarkEndEP17QRhiCommandBuffer
inline void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)
{
    if (!debugMarkers)
        return;

    Q_UNUSED(cb);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2376, as _ZN9QRhiGles212debugMarkMsgEP17QRhiCommandBufferRK10QByteArray
inline void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
{
    if (!debugMarkers)
        return;

    Q_UNUSED(cb);
    Q_UNUSED(msg);
}

//  from src/gui/rhi/qrhigles2.cpp, line 5241, as _ZN9QRhiGles216beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiGles2::beginComputePass(QRhiCommandBuffer *cb,
                                 QRhiResourceUpdateBatch *resourceUpdates,
                                 QRhiCommandBuffer::BeginPassFlags)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);

    enqueueBarriersForPass(cbD);

    cbD->recordingPass = QGles2CommandBuffer::ComputePass;

    cbD->resetCachedState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 5258, as _ZN9QRhiGles214endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiGles2::endComputePass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::ComputePass);

    cbD->recordingPass = QGles2CommandBuffer::NoPass;

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhigles2.cpp, line 5269, as _ZN9QRhiGles218setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline
inline void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb, QRhiComputePipeline *ps)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QGles2CommandBuffer::ComputePass);
    QGles2ComputePipeline *psD = QRHI_RES(QGles2ComputePipeline, ps);
    const bool pipelineChanged = cbD->currentComputePipeline != ps || cbD->currentPipelineGeneration != psD->generation;

    if (pipelineChanged) {
        cbD->currentGraphicsPipeline = nullptr;
        cbD->currentComputePipeline = ps;
        cbD->currentPipelineGeneration = psD->generation;
        if (psD->lastUsedInFrameNo != frameNo) {
            psD->lastUsedInFrameNo = frameNo;
            psD->currentSrb = nullptr;
            psD->currentSrbGeneration = 0;
        }

        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::BindComputePipeline;
        cmd.args.bindComputePipeline.ps = ps;
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 2385, as _ZN9QRhiGles213nativeHandlesEP17QRhiCommandBuffer
inline const QRhiNativeHandles *QRhiGles2::nativeHandles(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
    return nullptr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 2401, as _ZN9QRhiGles213beginExternalEP17QRhiCommandBuffer
inline void QRhiGles2::beginExternal(QRhiCommandBuffer *cb)
{
    if (ofr.active) {
        Q_ASSERT(!currentSwapChain);
        if (!ensureContext())
            return;
    } else {
        Q_ASSERT(currentSwapChain);
        if (!ensureContext(currentSwapChain->surface))
            return;
    }

    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);

    if (cbD->recordingPass == QGles2CommandBuffer::ComputePass
            && !cbD->computePassState.writtenResources.isEmpty())
    {
        QGles2CommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QGles2CommandBuffer::Command::Barrier;
        cmd.args.barrier.barriers = GL_ALL_BARRIER_BITS;
    }

    executeCommandBuffer(cbD);

    cbD->resetCommands();

    // ARRAY_BUFFER and SHADER_STORAGE_BUFFER are context state, not vertex
    // array object state, so going back to object 0 does not clear them.
    if (vao)
        f->glBindVertexArray(0);
    f->glBindBuffer(GL_ARRAY_BUFFER, 0);
    f->glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    if (caps.compute)
        f->glBindBuffer(GL_SHADER_STORAGE_BUFFER, 0);
}

//  from src/gui/rhi/qrhigles2.cpp, line 2458, as _ZN9QRhiGles220lastCompletedGpuTimeEP17QRhiCommandBuffer
inline double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer *cb)
{
    QGles2CommandBuffer *cbD = QRHI_RES(QGles2CommandBuffer, cb);
    return cbD->lastGpuTime;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1361, as _ZNK9QRhiGles221supportedShadingRatesEi
inline QList<QSize> QRhiGles2::supportedShadingRates(int sampleCount) const
{
    Q_UNUSED(sampleCount);
    return { QSize(1, 1) };
}

//  from src/gui/rhi/qrhigles2.cpp, line 1377, as _ZNK9QRhiGles213ubufAlignmentEv
inline int QRhiGles2::ubufAlignment() const
{
    // No real uniform buffers are used so no need to pretend there is any
    // alignment requirement.
    return 1;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1384, as _ZNK9QRhiGles218isYUpInFramebufferEv
inline bool QRhiGles2::isYUpInFramebuffer() const
{
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1389, as _ZNK9QRhiGles210isYUpInNDCEv
inline bool QRhiGles2::isYUpInNDC() const
{
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1394, as _ZNK9QRhiGles220isClipDepthZeroToOneEv
inline bool QRhiGles2::isClipDepthZeroToOne() const
{
    return false;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1399, as _ZNK9QRhiGles219clipSpaceCorrMatrixEv
inline QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const
{
    return QMatrix4x4(); // identity
}

//  from src/gui/rhi/qrhigles2.cpp, line 1632, as _ZNK9QRhiGles218isFeatureSupportedEN4QRhi7FeatureE
inline bool QRhiGles2::isFeatureSupported(QRhi::Feature feature) const
{
    switch (feature) {
    case QRhi::MultisampleTexture:
        return caps.multisampledTexture;
    case QRhi::MultisampleRenderBuffer:
        return caps.msaaRenderBuffer;
    case QRhi::DebugMarkers:
        return false;
    case QRhi::Timestamps:
        return caps.timestamps;
    case QRhi::Instancing:
        return caps.instancing;
    case QRhi::CustomInstanceStepRate:
        return false;
    case QRhi::PrimitiveRestart:
        return caps.fixedIndexPrimitiveRestart;
    case QRhi::NonDynamicUniformBuffers:
        return true;
    case QRhi::NonFourAlignedEffectiveIndexBufferOffset:
        return true;
    case QRhi::NPOTTextureRepeat:
        return caps.npotTextureFull;
    case QRhi::RedOrAlpha8IsRed:
        return caps.coreProfile;
    case QRhi::ElementIndexUint:
        return caps.elementIndexUint;
    case QRhi::Compute:
        return caps.compute;
    case QRhi::WideLines:
        return !caps.coreProfile;
    case QRhi::VertexShaderPointSize:
        return true;
    case QRhi::BaseVertex:
        return caps.baseVertex;
    case QRhi::BaseInstance:
        // The glDraw*BaseInstance variants of draw calls are not in GLES 3.2,
        // so won't bother, even though they would be available in GL 4.2+.
        // Furthermore, not supporting this avoids having to deal with the
        // gl_InstanceID vs gl_InstanceIndex mess in shaders and in the shader
        // transpiling pipeline.
        return false;
    case QRhi::TriangleFanTopology:
        return true;
    case QRhi::ReadBackNonUniformBuffer:
        return !caps.gles || caps.properMapBuffer;
    case QRhi::ReadBackNonBaseMipLevel:
        return caps.nonBaseLevelFramebufferTexture;
    case QRhi::TexelFetch:
        return caps.texelFetch;
    case QRhi::RenderToNonBaseMipLevel:
        return caps.nonBaseLevelFramebufferTexture;
    case QRhi::IntAttributes:
        return caps.intAttributes;
    case QRhi::ScreenSpaceDerivatives:
        return caps.screenSpaceDerivatives;
    case QRhi::ReadBackAnyTextureFormat:
        return false;
    case QRhi::PipelineCacheDataLoadSave:
        return caps.programBinary;
    case QRhi::ImageDataStride:
        return caps.unpackRowLength;
    case QRhi::RenderBufferImport:
        return true;
    case QRhi::ThreeDimensionalTextures:
        return caps.texture3D;
    case QRhi::RenderTo3DTextureSlice:
        return caps.texture3D;
    case QRhi::TextureArrays:
        return caps.maxTextureArraySize > 0;
    case QRhi::Tessellation:
        return caps.tessellation;
    case QRhi::GeometryShader:
        return caps.geometryShader;
    case QRhi::TextureArrayRange:
        return false;
    case QRhi::NonFillPolygonMode:
        return !caps.gles;
    case QRhi::OneDimensionalTextures:
        return caps.texture1D;
    case QRhi::OneDimensionalTextureMipmaps:
        return caps.texture1D;
    case QRhi::HalfAttributes:
        return caps.halfAttributes;
    case QRhi::RenderToOneDimensionalTexture:
        return caps.texture1D;
    case QRhi::ThreeDimensionalTextureMipmaps:
        return caps.texture3D;
    case QRhi::MultiView:
        return caps.multiView && caps.maxTextureArraySize > 0;
    case QRhi::TextureViewFormat:
        return false;
    case QRhi::ResolveDepthStencil:
        return true;
    case QRhi::VariableRateShading:
        return false;
    case QRhi::VariableRateShadingMap:
    case QRhi::VariableRateShadingMapWithTexture:
        return false;
    case QRhi::PerRenderTargetBlending:
        return caps.perRenderTargetBlending;
    case QRhi::SampleVariables:
        return caps.sampleVariables;
    case QRhi::InstanceIndexIncludesBaseInstance:
        return false; // because BaseInstance is always false
    case QRhi::DepthClamp:
        return caps.depthClamp;
    case QRhi::DrawIndirect:
        return caps.drawIndirect;
    case QRhi::DrawIndirectMulti:
        return caps.drawIndirectMulti;
    case QRhi::ShaderDrawParameters:
        return caps.shaderDrawParameters;
    default:
        Q_UNREACHABLE_RETURN(false);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 1750, as _ZNK9QRhiGles213resourceLimitEN4QRhi13ResourceLimitE
inline int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit) const
{
    switch (limit) {
    case QRhi::TextureSizeMin:
        return 1;
    case QRhi::TextureSizeMax:
        return caps.maxTextureSize;
    case QRhi::MaxColorAttachments:
        return caps.maxDrawBuffers;
    case QRhi::FramesInFlight:
        // From our perspective. What the GL impl does internally is another
        // question, but that's out of our hands and does not concern us here.
        return 1;
    case QRhi::MaxAsyncReadbackFrames:
        return 1;
    case QRhi::MaxThreadGroupsPerDimension:
        return caps.maxThreadGroupsPerDimension;
    case QRhi::MaxThreadsPerThreadGroup:
        return caps.maxThreadsPerThreadGroup;
    case QRhi::MaxThreadGroupX:
        return caps.maxThreadGroupsX;
    case QRhi::MaxThreadGroupY:
        return caps.maxThreadGroupsY;
    case QRhi::MaxThreadGroupZ:
        return caps.maxThreadGroupsZ;
    case QRhi::TextureArraySizeMax:
        return 2048;
    case QRhi::MaxUniformBufferRange:
        return int(qMin<qint64>(INT_MAX, caps.maxUniformVectors * qint64(16)));
    case QRhi::MaxVertexInputs:
        return caps.maxVertexInputs;
    case QRhi::MaxVertexOutputs:
        return caps.maxVertexOutputs;
    case QRhi::ShadingRateImageTileSize:
        return 0;
    default:
        Q_UNREACHABLE_RETURN(0);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 1790, as _ZN9QRhiGles213nativeHandlesEv
inline const QRhiNativeHandles *QRhiGles2::nativeHandles()
{
    return &nativeHandlesStruct;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1795, as _ZNK9QRhiGles210driverInfoEv
inline QRhiDriverInfo QRhiGles2::driverInfo() const
{
    return driverInfoStruct;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1800, as _ZN9QRhiGles210statisticsEv
inline QRhiStats QRhiGles2::statistics()
{
    QRhiStats result;
    result.totalPipelineCreationTime = totalPipelineCreationTime();
    return result;
}

//  from src/gui/rhi/qrhigles2.cpp, line 1807, as _ZN9QRhiGles235makeThreadLocalNativeContextCurrentEv
inline bool QRhiGles2::makeThreadLocalNativeContextCurrent()
{
    if (inFrame && !ofr.active)
        return ensureContext(currentSwapChain->surface);
    else
        return ensureContext();
}

//  from src/gui/rhi/qrhigles2.cpp, line 1815, as _ZN9QRhiGles220setQueueSubmitParamsEP17QRhiNativeHandles
inline void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles *)
{
    // not applicable
}

//  from src/gui/rhi/qrhigles2.cpp, line 1820, as _ZN9QRhiGles222releaseCachedResourcesEv
inline void QRhiGles2::releaseCachedResources()
{
    if (!ensureContext())
        return;

    for (uint shader : std::as_const(m_shaderCache))
        f->glDeleteShader(shader);

    m_shaderCache.clear();

    m_pipelineCache.clear();
}

//  from src/gui/rhi/qrhigles2.cpp, line 1833, as _ZNK9QRhiGles212isDeviceLostEv
inline bool QRhiGles2::isDeviceLost() const
{
    return contextLost;
}

//  from src/gui/rhi/qrhigles2.cpp, line 694, as _ZNK9QRhiGles223evaluateFallbackSurfaceEv
#if defined(Q_OS_LINUX)
inline QSurface *QRhiGles2::evaluateFallbackSurface() const
{
    // With Apple's deprecated OpenGL support we need to minimize the usage of
    // QOffscreenSurface since delicate problems can pop up with
    // NSOpenGLContext and drawables.
#if defined(Q_OS_MACOS)
    return maybeWindow && maybeWindow->handle() ? static_cast<QSurface *>(maybeWindow) : fallbackSurface;
#else
    return fallbackSurface;
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/gui/rhi/qrhigles2.cpp, line 1321, as _ZN9QRhiGles223executeDeferredReleasesEv
inline void QRhiGles2::executeDeferredReleases()
{
    for (int i = releaseQueue.size() - 1; i >= 0; --i) {
        const QRhiGles2::DeferredReleaseEntry &e(releaseQueue[i]);
        switch (e.type) {
        case QRhiGles2::DeferredReleaseEntry::Buffer:
            f->glDeleteBuffers(1, &e.buffer.buffer);
            break;
        case QRhiGles2::DeferredReleaseEntry::Pipeline:
            f->glDeleteProgram(e.pipeline.program);
            break;
        case QRhiGles2::DeferredReleaseEntry::Texture:
            f->glDeleteTextures(1, &e.texture.texture);
            break;
        case QRhiGles2::DeferredReleaseEntry::RenderBuffer:
            f->glDeleteRenderbuffers(1, &e.renderbuffer.renderbuffer);
            f->glDeleteRenderbuffers(1, &e.renderbuffer.renderbuffer2);
            break;
        case QRhiGles2::DeferredReleaseEntry::TextureRenderTarget:
            f->glDeleteFramebuffers(1, &e.textureRenderTarget.framebuffer);
            f->glDeleteTextures(1, &e.textureRenderTarget.nonMsaaThrowawayDepthTexture);
            break;
        default:
            Q_UNREACHABLE();
            break;
        }
        releaseQueue.removeAt(i);
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5038, as _ZN9QRhiGles222enqueueBarriersForPassEP19QGles2CommandBuffer
inline void QRhiGles2::enqueueBarriersForPass(QGles2CommandBuffer *cbD)
{
    cbD->passResTrackers.emplace_back();
    cbD->currentPassResTrackerIndex = cbD->passResTrackers.size() - 1;
    QGles2CommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QGles2CommandBuffer::Command::BarriersForPass;
    cmd.args.barriersForPass.trackerIndex = cbD->currentPassResTrackerIndex;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5418, as _ZNK9QRhiGles217glslVersionsToTryEv
inline QList<QShaderVersion> QRhiGles2::glslVersionsToTry() const
{
    QList<int> versionsToTry;
    if (caps.gles) {
        if (caps.ctxMajor > 3 || (caps.ctxMajor == 3 && caps.ctxMinor >= 2)) {
            versionsToTry << 320 << 310 << 300 << 100;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 1) {
            versionsToTry << 310 << 300 << 100;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 0) {
            versionsToTry << 300 << 100;
        } else {
            versionsToTry << 100;
        }
    } else {
        if (caps.ctxMajor > 4 || (caps.ctxMajor == 4 && caps.ctxMinor >= 6)) {
            versionsToTry << 460 << 450 << 440 << 430 << 420 << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 5) {
            versionsToTry << 450 << 440 << 430 << 420 << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 4) {
            versionsToTry << 440 << 430 << 420 << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 3) {
            versionsToTry << 430 << 420 << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 2) {
            versionsToTry << 420 << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 1) {
            versionsToTry << 410 << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 4 && caps.ctxMinor == 0) {
            versionsToTry << 400 << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 3) {
            versionsToTry << 330 << 150 << 140 << 130;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 2) {
            versionsToTry << 150 << 140 << 130;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 1) {
            versionsToTry << 140 << 130;
        } else if (caps.ctxMajor == 3 && caps.ctxMinor == 0) {
            versionsToTry << 130;
        }
        if (!caps.coreProfile)
            versionsToTry << 120;
    }

    const QShaderVersion::Flags flags = caps.gles ? QShaderVersion::GlslEs : QShaderVersion::Flags();
    QList<QShaderVersion> versions;
    versions.reserve(versionsToTry.size());
    for (int v : std::as_const(versionsToTry))
        versions.append(QShaderVersion(v, flags));
    return versions;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5569, as _ZN9QRhiGles211linkProgramEj
inline bool QRhiGles2::linkProgram(GLuint program)
{
    f->glLinkProgram(program);
    GLint linked = 0;
    f->glGetProgramiv(program, GL_LINK_STATUS, &linked);
    if (!linked) {
        GLint infoLogLength = 0;
        f->glGetProgramiv(program, GL_INFO_LOG_LENGTH, &infoLogLength);
        QByteArray log;
        if (infoLogLength > 1) {
            GLsizei length = 0;
            log.resize(infoLogLength);
            f->glGetProgramInfoLog(program, infoLogLength, &length, log.data());
        }
        qWarning("Failed to link shader program: %s", log.constData());
        return false;
    }
    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 5695, as _ZN9QRhiGles234sanityCheckVertexFragmentInterfaceERK18QShaderDescriptionS2_
inline void QRhiGles2::sanityCheckVertexFragmentInterface(const QShaderDescription &vsDesc, const QShaderDescription &fsDesc)
{
    if (!vsDesc.isValid() || !fsDesc.isValid())
        return;

    // Print a warning if the fragment shader input for a given location uses a
    // name that does not match the vertex shader output at the same location.
    // This is not an error with any other API and not with GLSL >= 330 either,
    // but matters for older GLSL code that has no location qualifiers.
    const auto vsOutputs = vsDesc.outputVariables();
    const auto fsInputs = fsDesc.inputVariables();
    for (const QShaderDescription::InOutVariable &outVar : vsOutputs) {
        for (const QShaderDescription::InOutVariable &inVar : fsInputs) {
            if (inVar.location == outVar.location) {
                if (inVar.name != outVar.name) {
                    qWarning("Vertex output name '%s' does not match fragment input '%s'. "
                             "This should be avoided because it causes problems with older GLSL versions.",
                             outVar.name.constData(), inVar.name.constData());
                }
                break;
            }
        }
    }
}

//  from src/gui/rhi/qrhigles2.cpp, line 5720, as _ZNK9QRhiGles231isProgramBinaryDiskCacheEnabledEv
inline bool QRhiGles2::isProgramBinaryDiskCacheEnabled() const
{
    static QOpenGLProgramBinarySupportCheckWrapper checker;
    return checker.get(ctx)->isSupported();
}

//  from src/gui/rhi/qrhigles2.cpp, line 5853, as _ZN9QRhiGles222trySaveToPipelineCacheEjRK10QByteArrayb
inline void QRhiGles2::trySaveToPipelineCache(GLuint program, const QByteArray &cacheKey, bool force)
{
    // This handles our own simulated "pipeline cache". (specific to QRhi, not
    // shared with legacy QOpenGL* stuff)

    if (caps.programBinary && (force || !m_pipelineCache.contains(cacheKey))) {
        GLint blobSize = 0;
        f->glGetProgramiv(program, GL_PROGRAM_BINARY_LENGTH, &blobSize);
        QByteArray blob(blobSize, Qt::Uninitialized);
        GLint outSize = 0;
        GLenum binaryFormat = 0;
        f->glGetProgramBinary(program, blobSize, &outSize, &binaryFormat, blob.data());
        if (blobSize == outSize)
            m_pipelineCache.insert(cacheKey, { binaryFormat, blob });
    }
}
//  -----------------------------------------------------------------------

//  A QRhiGles2 that Python can take functions over in. Every QRhiGles2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRhiGles2Call0)(const void *, int, int *);
typedef void (*CuteQRhiGles2Call1)(const void *, int *);
typedef void * (*CuteQRhiGles2Call2)(const void *, int *);
typedef void * (*CuteQRhiGles2Call3)(const void *, int *);
typedef void * (*CuteQRhiGles2Call4)(const void *, int *);
typedef void * (*CuteQRhiGles2Call5)(const void *, int, int, quint32, int *);
typedef void * (*CuteQRhiGles2Call6)(const void *, int, const QSize *, int, int, int, int *);
typedef void * (*CuteQRhiGles2Call7)(const void *, int, const QSize *, int, int, int, int, int *);
typedef void * (*CuteQRhiGles2Call8)(const void *, int, int, int, int, int, int, int *);
typedef void * (*CuteQRhiGles2Call9)(const void *, const QRhiTextureRenderTargetDescription *, int, int *);
typedef void * (*CuteQRhiGles2Call10)(const void *, int *);
typedef void * (*CuteQRhiGles2Call11)(const void *, int *);
typedef int (*CuteQRhiGles2Call12)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiGles2Call13)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiGles2Call14)(const void *, int, int *);
typedef int (*CuteQRhiGles2Call15)(const void *, int *);
typedef void (*CuteQRhiGles2Call16)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiGles2Call17)(const void *, QRhiCommandBuffer *, QRhiRenderTarget *, const QColor *, const QRhiDepthStencilClearValue *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiGles2Call18)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiGles2Call19)(const void *, QRhiCommandBuffer *, QRhiGraphicsPipeline *, int *);
typedef void (*CuteQRhiGles2Call20)(const void *, QRhiCommandBuffer *, const QRhiViewport *, int *);
typedef void (*CuteQRhiGles2Call21)(const void *, QRhiCommandBuffer *, const QRhiScissor *, int *);
typedef void (*CuteQRhiGles2Call22)(const void *, QRhiCommandBuffer *, const QColor *, int *);
typedef void (*CuteQRhiGles2Call23)(const void *, QRhiCommandBuffer *, quint32, int *);
typedef void (*CuteQRhiGles2Call24)(const void *, QRhiCommandBuffer *, const QSize *, int *);
typedef void (*CuteQRhiGles2Call25)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiGles2Call26)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, qint32, quint32, int *);
typedef void (*CuteQRhiGles2Call27)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiGles2Call28)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiGles2Call29)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiGles2Call30)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiGles2Call31)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiGles2Call32)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiGles2Call33)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiGles2Call34)(const void *, QRhiCommandBuffer *, QRhiComputePipeline *, int *);
typedef void (*CuteQRhiGles2Call35)(const void *, QRhiCommandBuffer *, int, int, int, int *);
typedef void * (*CuteQRhiGles2Call36)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiGles2Call37)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiGles2Call38)(const void *, QRhiCommandBuffer *, int *);
typedef double (*CuteQRhiGles2Call39)(const void *, QRhiCommandBuffer *, int *);
typedef int (*CuteQRhiGles2Call40)(const void *, int *);
typedef bool (*CuteQRhiGles2Call41)(const void *, int *);
typedef bool (*CuteQRhiGles2Call42)(const void *, int *);
typedef bool (*CuteQRhiGles2Call43)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQRhiGles2Call44)(const void *, int *);
typedef bool (*CuteQRhiGles2Call45)(const void *, int, int, int *);
typedef bool (*CuteQRhiGles2Call46)(const void *, int, int *);
typedef int (*CuteQRhiGles2Call47)(const void *, int, int *);
typedef void * (*CuteQRhiGles2Call48)(const void *, int *);
typedef const QRhiDriverInfo * (*CuteQRhiGles2Call49)(const void *, int *);
typedef const QRhiStats * (*CuteQRhiGles2Call50)(const void *, int *);
typedef bool (*CuteQRhiGles2Call51)(const void *, int *);
typedef void (*CuteQRhiGles2Call52)(const void *, QRhiNativeHandles *, int *);
typedef void (*CuteQRhiGles2Call53)(const void *, int *);
typedef bool (*CuteQRhiGles2Call54)(const void *, int *);
typedef const QByteArray * (*CuteQRhiGles2Call55)(const void *, int *);
typedef void (*CuteQRhiGles2Call56)(const void *, const QByteArray *, int *);
class CuteQRhiGles2 : public QRhiGles2 {
public:
  using QRhiGles2::QRhiGles2;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QRhiImplementation6createE6QFlagsIN4QRhi4FlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation7destroyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation22createGraphicsPipelineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation21createComputePipelineEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation28createShaderResourceBindingsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20createShadingRateMapEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation15createSwapChainEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation6finishEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11setViewportEP17QRhiCommandBufferRK12QRhiViewport")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10setScissorEP17QRhiCommandBufferRK11QRhiScissor")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17setBlendConstantsEP17QRhiCommandBufferRK6QColor")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13setStencilRefEP17QRhiCommandBufferj")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14setShadingRateEP17QRhiCommandBufferRK5QSize")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation4drawEP17QRhiCommandBufferjjjj")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11drawIndexedEP17QRhiCommandBufferjjjij")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12debugMarkEndEP17QRhiCommandBuffer")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation8dispatchEP17QRhiCommandBufferiii")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13nativeHandlesEP17QRhiCommandBuffer")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13beginExternalEP17QRhiCommandBuffer")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11endExternalEP17QRhiCommandBuffer")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20lastCompletedGpuTimeEP17QRhiCommandBuffer")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation13ubufAlignmentEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation18isYUpInFramebufferEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation10isYUpInNDCEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation20isClipDepthZeroToOneEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation19clipSpaceCorrMatrixEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation18isFeatureSupportedEN4QRhi7FeatureE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation13resourceLimitEN4QRhi13ResourceLimitE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13nativeHandlesEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation10driverInfoEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10statisticsEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation35makeThreadLocalNativeContextCurrentEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20setQueueSubmitParamsEP17QRhiNativeHandles")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation22releaseCachedResourcesEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation12isDeviceLostEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17pipelineCacheDataEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20setPipelineCacheDataERK10QByteArray")) {
      taken[56] = call;
      return true;
    }
    return false;
  }

  //  bool QRhiGles2::create(QRhi::Flags flags)
  bool create(QRhi::Flags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiGles2Call0 call = reinterpret_cast<CuteQRhiGles2Call0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiGles2::create(flags);
  }

  //  void QRhiGles2::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiGles2Call1 call = reinterpret_cast<CuteQRhiGles2Call1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiGles2::destroy();
  }

  //  QRhiGraphicsPipeline *QRhiGles2::createGraphicsPipeline()
  QRhiGraphicsPipeline *createGraphicsPipeline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiGles2Call2 call = reinterpret_cast<CuteQRhiGles2Call2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiGraphicsPipeline *>(given);
    }
    return QRhiGles2::createGraphicsPipeline();
  }

  //  QRhiComputePipeline *QRhiGles2::createComputePipeline()
  QRhiComputePipeline *createComputePipeline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiGles2Call3 call = reinterpret_cast<CuteQRhiGles2Call3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiComputePipeline *>(given);
    }
    return QRhiGles2::createComputePipeline();
  }

  //  QRhiShaderResourceBindings *QRhiGles2::createShaderResourceBindings()
  QRhiShaderResourceBindings *createShaderResourceBindings() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiGles2Call4 call = reinterpret_cast<CuteQRhiGles2Call4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShaderResourceBindings *>(given);
    }
    return QRhiGles2::createShaderResourceBindings();
  }

  //  QRhiBuffer *QRhiGles2::createBuffer(QRhiBuffer::Type type,
  //      QRhiBuffer::UsageFlags usage, quint32 size)
  QRhiBuffer *createBuffer(
      QRhiBuffer::Type type,
      QRhiBuffer::UsageFlags usage,
      quint32 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiGles2Call5 call = reinterpret_cast<CuteQRhiGles2Call5>(taken[5]);
      void * given = call(this, static_cast<int>(type), static_cast<int>(usage.toInt()), size, &handled);
      if (handled) return static_cast<QRhiBuffer *>(given);
    }
    return QRhiGles2::createBuffer(type, usage, size);
  }

  //  QRhiRenderBuffer
  //      *QRhiGles2::createRenderBuffer(QRhiRenderBuffer::Type type, const
  //      QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
  //      QRhiTexture::Format backingFormatHint)
  QRhiRenderBuffer *createRenderBuffer(
      QRhiRenderBuffer::Type type,
      const QSize &pixelSize,
      int sampleCount,
      QRhiRenderBuffer::Flags flags,
      QRhiTexture::Format backingFormatHint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiGles2Call6 call = reinterpret_cast<CuteQRhiGles2Call6>(taken[6]);
      void * given = call(this, static_cast<int>(type), &pixelSize, sampleCount, static_cast<int>(flags.toInt()), static_cast<int>(backingFormatHint), &handled);
      if (handled) return static_cast<QRhiRenderBuffer *>(given);
    }
    return QRhiGles2::createRenderBuffer(type, pixelSize, sampleCount, flags, backingFormatHint);
  }

  //  QRhiTexture *QRhiGles2::createTexture(QRhiTexture::Format format,
  //      const QSize &pixelSize, int depth, int arraySize, int
  //      sampleCount, QRhiTexture::Flags flags)
  QRhiTexture *createTexture(
      QRhiTexture::Format format,
      const QSize &pixelSize,
      int depth,
      int arraySize,
      int sampleCount,
      QRhiTexture::Flags flags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRhiGles2Call7 call = reinterpret_cast<CuteQRhiGles2Call7>(taken[7]);
      void * given = call(this, static_cast<int>(format), &pixelSize, depth, arraySize, sampleCount, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QRhiGles2::createTexture(format, pixelSize, depth, arraySize, sampleCount, flags);
  }

  //  QRhiSampler *QRhiGles2::createSampler(QRhiSampler::Filter magFilter,
  //      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
  //      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
  //      QRhiSampler::AddressMode w)
  QRhiSampler *createSampler(
      QRhiSampler::Filter magFilter,
      QRhiSampler::Filter minFilter,
      QRhiSampler::Filter mipmapMode,
      QRhiSampler::AddressMode u,
      QRhiSampler::AddressMode v,
      QRhiSampler::AddressMode w) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiGles2Call8 call = reinterpret_cast<CuteQRhiGles2Call8>(taken[8]);
      void * given = call(this, static_cast<int>(magFilter), static_cast<int>(minFilter), static_cast<int>(mipmapMode), static_cast<int>(u), static_cast<int>(v), static_cast<int>(w), &handled);
      if (handled) return static_cast<QRhiSampler *>(given);
    }
    return QRhiGles2::createSampler(magFilter, minFilter, mipmapMode, u, v, w);
  }

  //  QRhiTextureRenderTarget *QRhiGles2::createTextureRenderTarget(const
  //      QRhiTextureRenderTargetDescription &desc,
  //      QRhiTextureRenderTarget::Flags flags)
  QRhiTextureRenderTarget *createTextureRenderTarget(
      const QRhiTextureRenderTargetDescription &desc,
      QRhiTextureRenderTarget::Flags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiGles2Call9 call = reinterpret_cast<CuteQRhiGles2Call9>(taken[9]);
      void * given = call(this, &desc, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTextureRenderTarget *>(given);
    }
    return QRhiGles2::createTextureRenderTarget(desc, flags);
  }

  //  QRhiShadingRateMap *QRhiGles2::createShadingRateMap()
  QRhiShadingRateMap *createShadingRateMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiGles2Call10 call = reinterpret_cast<CuteQRhiGles2Call10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShadingRateMap *>(given);
    }
    return QRhiGles2::createShadingRateMap();
  }

  //  QRhiSwapChain *QRhiGles2::createSwapChain()
  QRhiSwapChain *createSwapChain() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiGles2Call11 call = reinterpret_cast<CuteQRhiGles2Call11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiSwapChain *>(given);
    }
    return QRhiGles2::createSwapChain();
  }

  //  QRhi::FrameOpResult QRhiGles2::beginFrame(QRhiSwapChain *swapChain,
  //      QRhi::BeginFrameFlags flags)
  QRhi::FrameOpResult beginFrame(
      QRhiSwapChain *swapChain,
      QRhi::BeginFrameFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiGles2Call12 call = reinterpret_cast<CuteQRhiGles2Call12>(taken[12]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiGles2::beginFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiGles2::endFrame(QRhiSwapChain *swapChain,
  //      QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endFrame(
      QRhiSwapChain *swapChain,
      QRhi::EndFrameFlags flags) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiGles2Call13 call = reinterpret_cast<CuteQRhiGles2Call13>(taken[13]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiGles2::endFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiGles2::endOffscreenFrame(QRhi::EndFrameFlags
  //      flags)
  QRhi::FrameOpResult endOffscreenFrame(QRhi::EndFrameFlags flags) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiGles2Call14 call = reinterpret_cast<CuteQRhiGles2Call14>(taken[14]);
      int given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiGles2::endOffscreenFrame(flags);
  }

  //  QRhi::FrameOpResult QRhiGles2::finish()
  QRhi::FrameOpResult finish() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiGles2Call15 call = reinterpret_cast<CuteQRhiGles2Call15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiGles2::finish();
  }

  //  void QRhiGles2::resourceUpdate(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void resourceUpdate(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiGles2Call16 call = reinterpret_cast<CuteQRhiGles2Call16>(taken[16]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiGles2::resourceUpdate(cb, resourceUpdates);
  }

  //  void QRhiGles2::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget
  //      *rt, const QColor &colorClearValue, const
  //      QRhiDepthStencilClearValue &depthStencilClearValue,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginPass(
      QRhiCommandBuffer *cb,
      QRhiRenderTarget *rt,
      const QColor &colorClearValue,
      const QRhiDepthStencilClearValue &depthStencilClearValue,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRhiGles2Call17 call = reinterpret_cast<CuteQRhiGles2Call17>(taken[17]);
      call(this, cb, rt, &colorClearValue, &depthStencilClearValue, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiGles2::beginPass(cb, rt, colorClearValue, depthStencilClearValue, resourceUpdates, flags);
  }

  //  void QRhiGles2::endPass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endPass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiGles2Call18 call = reinterpret_cast<CuteQRhiGles2Call18>(taken[18]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiGles2::endPass(cb, resourceUpdates);
  }

  //  void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb,
  //      QRhiGraphicsPipeline *ps)
  void setGraphicsPipeline(
      QRhiCommandBuffer *cb,
      QRhiGraphicsPipeline *ps) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiGles2Call19 call = reinterpret_cast<CuteQRhiGles2Call19>(taken[19]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiGles2::setGraphicsPipeline(cb, ps);
  }

  //  void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
  //      &viewport)
  void setViewport(
      QRhiCommandBuffer *cb,
      const QRhiViewport &viewport) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiGles2Call20 call = reinterpret_cast<CuteQRhiGles2Call20>(taken[20]);
      call(this, cb, &viewport, &handled);
      if (handled) return;
    }
    QRhiGles2::setViewport(cb, viewport);
  }

  //  void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
  //      &scissor)
  void setScissor(
      QRhiCommandBuffer *cb,
      const QRhiScissor &scissor) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiGles2Call21 call = reinterpret_cast<CuteQRhiGles2Call21>(taken[21]);
      call(this, cb, &scissor, &handled);
      if (handled) return;
    }
    QRhiGles2::setScissor(cb, scissor);
  }

  //  void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb, const QColor
  //      &c)
  void setBlendConstants(QRhiCommandBuffer *cb, const QColor &c) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiGles2Call22 call = reinterpret_cast<CuteQRhiGles2Call22>(taken[22]);
      call(this, cb, &c, &handled);
      if (handled) return;
    }
    QRhiGles2::setBlendConstants(cb, c);
  }

  //  void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32
  //      refValue)
  void setStencilRef(QRhiCommandBuffer *cb, quint32 refValue) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiGles2Call23 call = reinterpret_cast<CuteQRhiGles2Call23>(taken[23]);
      call(this, cb, refValue, &handled);
      if (handled) return;
    }
    QRhiGles2::setStencilRef(cb, refValue);
  }

  //  void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const QSize
  //      &coarsePixelSize)
  void setShadingRate(
      QRhiCommandBuffer *cb,
      const QSize &coarsePixelSize) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiGles2Call24 call = reinterpret_cast<CuteQRhiGles2Call24>(taken[24]);
      call(this, cb, &coarsePixelSize, &handled);
      if (handled) return;
    }
    QRhiGles2::setShadingRate(cb, coarsePixelSize);
  }

  //  void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
  //      quint32 instanceCount, quint32 firstVertex, quint32
  //      firstInstance)
  void draw(
      QRhiCommandBuffer *cb,
      quint32 vertexCount,
      quint32 instanceCount,
      quint32 firstVertex,
      quint32 firstInstance) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRhiGles2Call25 call = reinterpret_cast<CuteQRhiGles2Call25>(taken[25]);
      call(this, cb, vertexCount, instanceCount, firstVertex, firstInstance, &handled);
      if (handled) return;
    }
    QRhiGles2::draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
  }

  //  void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32
  //      indexCount, quint32 instanceCount, quint32 firstIndex, qint32
  //      vertexOffset, quint32 firstInstance)
  void drawIndexed(
      QRhiCommandBuffer *cb,
      quint32 indexCount,
      quint32 instanceCount,
      quint32 firstIndex,
      qint32 vertexOffset,
      quint32 firstInstance) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRhiGles2Call26 call = reinterpret_cast<CuteQRhiGles2Call26>(taken[26]);
      call(this, cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance, &handled);
      if (handled) return;
    }
    QRhiGles2::drawIndexed(cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance);
  }

  //  void QRhiGles2::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
  //      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
  //      quint32 stride)
  void drawIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 indirectBufferOffset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRhiGles2Call27 call = reinterpret_cast<CuteQRhiGles2Call27>(taken[27]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiGles2::drawIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiGles2::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
  //      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
  //      quint32 stride)
  void drawIndexedIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 indirectBufferOffset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRhiGles2Call28 call = reinterpret_cast<CuteQRhiGles2Call28>(taken[28]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiGles2::drawIndexedIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const
  //      QByteArray &name)
  void debugMarkBegin(
      QRhiCommandBuffer *cb,
      const QByteArray &name) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiGles2Call29 call = reinterpret_cast<CuteQRhiGles2Call29>(taken[29]);
      call(this, cb, &name, &handled);
      if (handled) return;
    }
    QRhiGles2::debugMarkBegin(cb, name);
  }

  //  void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)
  void debugMarkEnd(QRhiCommandBuffer *cb) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiGles2Call30 call = reinterpret_cast<CuteQRhiGles2Call30>(taken[30]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiGles2::debugMarkEnd(cb);
  }

  //  void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
  //      &msg)
  void debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiGles2Call31 call = reinterpret_cast<CuteQRhiGles2Call31>(taken[31]);
      call(this, cb, &msg, &handled);
      if (handled) return;
    }
    QRhiGles2::debugMarkMsg(cb, msg);
  }

  //  void QRhiGles2::beginComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiGles2Call32 call = reinterpret_cast<CuteQRhiGles2Call32>(taken[32]);
      call(this, cb, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiGles2::beginComputePass(cb, resourceUpdates, flags);
  }

  //  void QRhiGles2::endComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiGles2Call33 call = reinterpret_cast<CuteQRhiGles2Call33>(taken[33]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiGles2::endComputePass(cb, resourceUpdates);
  }

  //  void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb,
  //      QRhiComputePipeline *ps)
  void setComputePipeline(
      QRhiCommandBuffer *cb,
      QRhiComputePipeline *ps) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiGles2Call34 call = reinterpret_cast<CuteQRhiGles2Call34>(taken[34]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiGles2::setComputePipeline(cb, ps);
  }

  //  void QRhiGles2::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
  void dispatch(QRhiCommandBuffer *cb, int x, int y, int z) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiGles2Call35 call = reinterpret_cast<CuteQRhiGles2Call35>(taken[35]);
      call(this, cb, x, y, z, &handled);
      if (handled) return;
    }
    QRhiGles2::dispatch(cb, x, y, z);
  }

  //  const QRhiNativeHandles *QRhiGles2::nativeHandles(QRhiCommandBuffer
  //      *cb)
  const QRhiNativeHandles *nativeHandles(QRhiCommandBuffer *cb) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiGles2Call36 call = reinterpret_cast<CuteQRhiGles2Call36>(taken[36]);
      void * given = call(this, cb, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiGles2::nativeHandles(cb);
  }

  //  void QRhiGles2::beginExternal(QRhiCommandBuffer *cb)
  void beginExternal(QRhiCommandBuffer *cb) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiGles2Call37 call = reinterpret_cast<CuteQRhiGles2Call37>(taken[37]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiGles2::beginExternal(cb);
  }

  //  void QRhiGles2::endExternal(QRhiCommandBuffer *cb)
  void endExternal(QRhiCommandBuffer *cb) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiGles2Call38 call = reinterpret_cast<CuteQRhiGles2Call38>(taken[38]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiGles2::endExternal(cb);
  }

  //  double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer *cb)
  double lastCompletedGpuTime(QRhiCommandBuffer *cb) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiGles2Call39 call = reinterpret_cast<CuteQRhiGles2Call39>(taken[39]);
      double given = call(this, cb, &handled);
      if (handled) return given;
    }
    return QRhiGles2::lastCompletedGpuTime(cb);
  }

  //  int QRhiGles2::ubufAlignment() const
  int ubufAlignment() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiGles2Call40 call = reinterpret_cast<CuteQRhiGles2Call40>(taken[40]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::ubufAlignment();
  }

  //  bool QRhiGles2::isYUpInFramebuffer() const
  bool isYUpInFramebuffer() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiGles2Call41 call = reinterpret_cast<CuteQRhiGles2Call41>(taken[41]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::isYUpInFramebuffer();
  }

  //  bool QRhiGles2::isYUpInNDC() const
  bool isYUpInNDC() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiGles2Call42 call = reinterpret_cast<CuteQRhiGles2Call42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::isYUpInNDC();
  }

  //  bool QRhiGles2::isClipDepthZeroToOne() const
  bool isClipDepthZeroToOne() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRhiGles2Call43 call = reinterpret_cast<CuteQRhiGles2Call43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::isClipDepthZeroToOne();
  }

  //  QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const
  QMatrix4x4 clipSpaceCorrMatrix() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQRhiGles2Call44 call = reinterpret_cast<CuteQRhiGles2Call44>(taken[44]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiGles2::clipSpaceCorrMatrix();
  }

  //  bool QRhiGles2::isTextureFormatSupported(QRhiTexture::Format format,
  //      QRhiTexture::Flags flags) const
  bool isTextureFormatSupported(
      QRhiTexture::Format format,
      QRhiTexture::Flags flags) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQRhiGles2Call45 call = reinterpret_cast<CuteQRhiGles2Call45>(taken[45]);
      bool given = call(this, static_cast<int>(format), static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiGles2::isTextureFormatSupported(format, flags);
  }

  //  bool QRhiGles2::isFeatureSupported(QRhi::Feature feature) const
  bool isFeatureSupported(QRhi::Feature feature) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQRhiGles2Call46 call = reinterpret_cast<CuteQRhiGles2Call46>(taken[46]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return QRhiGles2::isFeatureSupported(feature);
  }

  //  int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit) const
  int resourceLimit(QRhi::ResourceLimit limit) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQRhiGles2Call47 call = reinterpret_cast<CuteQRhiGles2Call47>(taken[47]);
      int given = call(this, static_cast<int>(limit), &handled);
      if (handled) return given;
    }
    return QRhiGles2::resourceLimit(limit);
  }

  //  const QRhiNativeHandles *QRhiGles2::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[48]) {
      int handled = 0;
      CuteQRhiGles2Call48 call = reinterpret_cast<CuteQRhiGles2Call48>(taken[48]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiGles2::nativeHandles();
  }

  //  QRhiDriverInfo QRhiGles2::driverInfo() const
  QRhiDriverInfo driverInfo() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQRhiGles2Call49 call = reinterpret_cast<CuteQRhiGles2Call49>(taken[49]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiGles2::driverInfo();
  }

  //  QRhiStats QRhiGles2::statistics()
  QRhiStats statistics() override {
    if (taken[50]) {
      int handled = 0;
      CuteQRhiGles2Call50 call = reinterpret_cast<CuteQRhiGles2Call50>(taken[50]);
      const QRhiStats * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiGles2::statistics();
  }

  //  bool QRhiGles2::makeThreadLocalNativeContextCurrent()
  bool makeThreadLocalNativeContextCurrent() override {
    if (taken[51]) {
      int handled = 0;
      CuteQRhiGles2Call51 call = reinterpret_cast<CuteQRhiGles2Call51>(taken[51]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::makeThreadLocalNativeContextCurrent();
  }

  //  void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles *params)
  void setQueueSubmitParams(QRhiNativeHandles *params) override {
    if (taken[52]) {
      int handled = 0;
      CuteQRhiGles2Call52 call = reinterpret_cast<CuteQRhiGles2Call52>(taken[52]);
      call(this, params, &handled);
      if (handled) return;
    }
    QRhiGles2::setQueueSubmitParams(params);
  }

  //  void QRhiGles2::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[53]) {
      int handled = 0;
      CuteQRhiGles2Call53 call = reinterpret_cast<CuteQRhiGles2Call53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiGles2::releaseCachedResources();
  }

  //  bool QRhiGles2::isDeviceLost() const
  bool isDeviceLost() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQRhiGles2Call54 call = reinterpret_cast<CuteQRhiGles2Call54>(taken[54]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiGles2::isDeviceLost();
  }

  //  QByteArray QRhiGles2::pipelineCacheData()
  QByteArray pipelineCacheData() override {
    if (taken[55]) {
      int handled = 0;
      CuteQRhiGles2Call55 call = reinterpret_cast<CuteQRhiGles2Call55>(taken[55]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiGles2::pipelineCacheData();
  }

  //  void QRhiGles2::setPipelineCacheData(const QByteArray &data)
  void setPipelineCacheData(const QByteArray &data) override {
    if (taken[56]) {
      int handled = 0;
      CuteQRhiGles2Call56 call = reinterpret_cast<CuteQRhiGles2Call56>(taken[56]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QRhiGles2::setPipelineCacheData(data);
  }
};

//  void QRhiGles2::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles27destroyEv(QRhiGles2 *self) {
  self->destroy();
}

//  QRhiGraphicsPipeline *QRhiGles2::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN9QRhiGles222createGraphicsPipelineEv(
    QRhiGles2 *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiGles2::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN9QRhiGles221createComputePipelineEv(
    QRhiGles2 *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings *QRhiGles2::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN9QRhiGles228createShaderResourceBindingsEv(
    QRhiGles2 *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiGles2::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN9QRhiGles212createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiGles2 *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer *QRhiGles2::createRenderBuffer(QRhiRenderBuffer::Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN9QRhiGles218createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiGles2 *self,
    QRhiRenderBuffer::Type type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    QRhiTexture::Format backingFormatHint) {
  return self->createRenderBuffer(
      type,
      *pixelSize,
      sampleCount,
      QFlags<QRhiRenderBuffer::Flag>::fromInt(flags),
      backingFormatHint);
}

//  QRhiTexture *QRhiGles2::createTexture(QRhiTexture::Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN9QRhiGles213createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiGles2 *self,
    QRhiTexture::Format format,
    const QSize *pixelSize,
    int depth,
    int arraySize,
    int sampleCount,
    int flags) {
  return self->createTexture(
      format,
      *pixelSize,
      depth,
      arraySize,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiSampler *QRhiGles2::createSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN9QRhiGles213createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiGles2 *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget *QRhiGles2::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN9QRhiGles225createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiGles2 *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiGles2::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN9QRhiGles220createShadingRateMapEv(
    QRhiGles2 *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiGles2::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN9QRhiGles215createSwapChainEv(QRhiGles2 *self) {
  return self->createSwapChain();
}

//  QRhi::FrameOpResult QRhiGles2::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiGles26finishEv(QRhiGles2 *self) {
  return self->finish();
}

//  void QRhiGles2::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles214resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiGles2::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles29beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QColor *colorClearValue,
    const QRhiDepthStencilClearValue *depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginPass(
      cb,
      rt,
      *colorClearValue,
      *depthStencilClearValue,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiGles2::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles27endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles219setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(cb, ps);
}

//  void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles211setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->setViewport(cb, *viewport);
}

//  void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles210setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->setScissor(cb, *scissor);
}

//  void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles217setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->setBlendConstants(cb, *c);
}

//  void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles213setStencilRefEP17QRhiCommandBufferj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->setStencilRef(cb, refValue);
}

//  void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles214setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles24drawEP17QRhiCommandBufferjjjj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles211drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->drawIndexed(
      cb,
      indexCount,
      instanceCount,
      firstIndex,
      vertexOffset,
      firstInstance);
}

//  void QRhiGles2::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles212drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiGles2::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles219drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndexedIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles214debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles212debugMarkEndEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles212debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiGles2::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles216beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiGles2::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles214endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles218setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(cb, ps);
}

//  const QRhiNativeHandles *QRhiGles2::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiGles213nativeHandlesEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  void QRhiGles2::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles213beginExternalEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  self->beginExternal(cb);
}

//  double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QRhiGles220lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  QList<QSize> QRhiGles2::supportedShadingRates(int sampleCount) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK9QRhiGles221supportedShadingRatesEi(
    const QRhiGles2 *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  int QRhiGles2::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiGles213ubufAlignmentEv(const QRhiGles2 *self) {
  return self->ubufAlignment();
}

//  bool QRhiGles2::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles218isYUpInFramebufferEv(const QRhiGles2 *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiGles2::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles210isYUpInNDCEv(const QRhiGles2 *self) {
  return self->isYUpInNDC();
}

//  bool QRhiGles2::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles220isClipDepthZeroToOneEv(const QRhiGles2 *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK9QRhiGles219clipSpaceCorrMatrixEv(
    const QRhiGles2 *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhiGles2::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles218isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiGles2 *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiGles213resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiGles2 *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiGles2::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiGles213nativeHandlesEv(
    QRhiGles2 *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiGles2::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK9QRhiGles210driverInfoEv(const QRhiGles2 *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  QRhiStats QRhiGles2::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZN9QRhiGles210statisticsEv(QRhiGles2 *self) {
  return new QRhiStats(self->statistics());
}

//  bool QRhiGles2::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiGles235makeThreadLocalNativeContextCurrentEv(
    QRhiGles2 *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles220setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiGles2 *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiGles2::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles222releaseCachedResourcesEv(QRhiGles2 *self) {
  self->releaseCachedResources();
}

//  bool QRhiGles2::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles212isDeviceLostEv(const QRhiGles2 *self) {
  return self->isDeviceLost();
}

#if defined(Q_OS_LINUX)
//  QSurface *QRhiGles2::evaluateFallbackSurface() const
extern "C" Q_DECL_EXPORT
QSurface *ritual_ZNK9QRhiGles223evaluateFallbackSurfaceEv(
    const QRhiGles2 *self) {
  return self->evaluateFallbackSurface();
}
#endif  // defined(Q_OS_LINUX)

//  void QRhiGles2::executeDeferredReleases()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles223executeDeferredReleasesEv(QRhiGles2 *self) {
  self->executeDeferredReleases();
}

//  void QRhiGles2::enqueueBarriersForPass(QGles2CommandBuffer *cbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles222enqueueBarriersForPassEP19QGles2CommandBuffer(
    QRhiGles2 *self,
    QGles2CommandBuffer *cbD) {
  self->enqueueBarriersForPass(cbD);
}

//  QList<QShaderVersion> QRhiGles2::glslVersionsToTry() const
extern "C" Q_DECL_EXPORT
QList<QShaderVersion> *ritual_ZNK9QRhiGles217glslVersionsToTryEv(
    const QRhiGles2 *self) {
  return new QList<QShaderVersion>(self->glslVersionsToTry());
}

//  bool QRhiGles2::linkProgram(GLuint program)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiGles211linkProgramEj(QRhiGles2 *self, GLuint program) {
  return self->linkProgram(program);
}

//  void QRhiGles2::sanityCheckVertexFragmentInterface(const
//      QShaderDescription &vsDesc, const QShaderDescription &fsDesc)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles234sanityCheckVertexFragmentInterfaceERK18QShaderDescriptionS2_(
    QRhiGles2 *self,
    const QShaderDescription *vsDesc,
    const QShaderDescription *fsDesc) {
  self->sanityCheckVertexFragmentInterface(*vsDesc, *fsDesc);
}

//  bool QRhiGles2::isProgramBinaryDiskCacheEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiGles231isProgramBinaryDiskCacheEnabledEv(
    const QRhiGles2 *self) {
  return self->isProgramBinaryDiskCacheEnabled();
}

//  void QRhiGles2::trySaveToPipelineCache(GLuint program, const QByteArray
//      &cacheKey, bool force)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiGles222trySaveToPipelineCacheEjRK10QByteArrayb(
    QRhiGles2 *self,
    GLuint program,
    const QByteArray *cacheKey,
    bool force) {
  self->trySaveToPipelineCache(program, *cacheKey, force);
}

//  a Python function taken by a CuteQRhiGles2, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiGles2(QRhiGles2 *self, const char *key, void *call) {
  return static_cast<CuteQRhiGles2 *>(self)->take(key, call);
}

//  QRhiShadingRateMap *QRhiGles2::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_own_ZN9QRhiGles220createShadingRateMapEv(
    QRhiGles2 *self) {
  return self->QRhiGles2::createShadingRateMap();
}

//  void QRhiGles2::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles219setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->QRhiGles2::setGraphicsPipeline(cb, ps);
}

//  void QRhiGles2::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles211setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->QRhiGles2::setViewport(cb, *viewport);
}

//  void QRhiGles2::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles210setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->QRhiGles2::setScissor(cb, *scissor);
}

//  void QRhiGles2::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles217setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->QRhiGles2::setBlendConstants(cb, *c);
}

//  void QRhiGles2::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles213setStencilRefEP17QRhiCommandBufferj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->QRhiGles2::setStencilRef(cb, refValue);
}

//  void QRhiGles2::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles214setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->QRhiGles2::setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiGles2::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles24drawEP17QRhiCommandBufferjjjj(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->QRhiGles2::draw(
      cb,
      vertexCount,
      instanceCount,
      firstVertex,
      firstInstance);
}

//  void QRhiGles2::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles211drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->QRhiGles2::drawIndexed(
      cb,
      indexCount,
      instanceCount,
      firstIndex,
      vertexOffset,
      firstInstance);
}

//  void QRhiGles2::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles214debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->QRhiGles2::debugMarkBegin(cb, *name);
}

//  void QRhiGles2::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles212debugMarkEndEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  self->QRhiGles2::debugMarkEnd(cb);
}

//  void QRhiGles2::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles212debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->QRhiGles2::debugMarkMsg(cb, *msg);
}

//  void QRhiGles2::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles218setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->QRhiGles2::setComputePipeline(cb, ps);
}

//  const QRhiNativeHandles *QRhiGles2::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN9QRhiGles213nativeHandlesEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiGles2::nativeHandles(cb);
}

//  double QRhiGles2::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_own_ZN9QRhiGles220lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiGles2 *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiGles2::lastCompletedGpuTime(cb);
}

//  int QRhiGles2::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QRhiGles213ubufAlignmentEv(const QRhiGles2 *self) {
  return self->QRhiGles2::ubufAlignment();
}

//  bool QRhiGles2::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QRhiGles218isYUpInFramebufferEv(const QRhiGles2 *self) {
  return self->QRhiGles2::isYUpInFramebuffer();
}

//  bool QRhiGles2::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QRhiGles210isYUpInNDCEv(const QRhiGles2 *self) {
  return self->QRhiGles2::isYUpInNDC();
}

//  bool QRhiGles2::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QRhiGles220isClipDepthZeroToOneEv(
    const QRhiGles2 *self) {
  return self->QRhiGles2::isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiGles2::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK9QRhiGles219clipSpaceCorrMatrixEv(
    const QRhiGles2 *self) {
  return new QMatrix4x4(self->QRhiGles2::clipSpaceCorrMatrix());
}

//  bool QRhiGles2::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QRhiGles218isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiGles2 *self,
    QRhi::Feature feature) {
  return self->QRhiGles2::isFeatureSupported(feature);
}

//  int QRhiGles2::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QRhiGles213resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiGles2 *self,
    QRhi::ResourceLimit limit) {
  return self->QRhiGles2::resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiGles2::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN9QRhiGles213nativeHandlesEv(
    QRhiGles2 *self) {
  return self->QRhiGles2::nativeHandles();
}

//  QRhiDriverInfo QRhiGles2::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_own_ZNK9QRhiGles210driverInfoEv(
    const QRhiGles2 *self) {
  return new QRhiDriverInfo(self->QRhiGles2::driverInfo());
}

//  QRhiStats QRhiGles2::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_own_ZN9QRhiGles210statisticsEv(QRhiGles2 *self) {
  return new QRhiStats(self->QRhiGles2::statistics());
}

//  void QRhiGles2::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QRhiGles220setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiGles2 *self,
    QRhiNativeHandles *params) {
  self->QRhiGles2::setQueueSubmitParams(params);
}

//  bool QRhiGles2::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QRhiGles212isDeviceLostEv(const QRhiGles2 *self) {
  return self->QRhiGles2::isDeviceLost();
}

#endif  // QT_CONFIG(opengl)
