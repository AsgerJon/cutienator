//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhinull_p.h"
#include <qmath.h>
#include <QPainter>
#include "qrhi_p.h"
#include <qmath.h>
#include <QLoggingCategory>
#include "private/qloggingregistry_p.h"
#include "qrhinull_p.h"
#ifndef QT_NO_OPENGL
#include "qrhigles2_p.h"
#endif
#if QT_CONFIG(vulkan)
#endif
#ifdef Q_OS_WIN
#include "qrhid3d11_p.h"
#include "qrhid3d12_p.h"
#endif
#if QT_CONFIG(metal)
#include "qrhimetal_p.h"
#endif
#include <limits>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 626, as _ZN11QNullBufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj
inline QNullBuffer::QNullBuffer(QRhiImplementation *rhi, Type type, UsageFlags usage, quint32 size)
    : QRhiBuffer(rhi, type, usage, size)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 786, as _ZN12QNullSamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_
inline QNullSampler::QNullSampler(QRhiImplementation *rhi, Filter magFilter, Filter minFilter, Filter mipmapMode,
                           AddressMode u, AddressMode v, AddressMode w)
    : QRhiSampler(rhi, magFilter, minFilter, mipmapMode, u, v, w)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 706, as _ZN12QNullTextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE
inline QNullTexture::QNullTexture(QRhiImplementation *rhi, Format format, const QSize &pixelSize, int depth,
                           int arraySize, int sampleCount, Flags flags)
    : QRhiTexture(rhi, format, pixelSize, depth, arraySize, sampleCount, flags)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1042, as _ZN14QNullSwapChainC1EP18QRhiImplementation
inline QNullSwapChain::QNullSwapChain(QRhiImplementation *rhi)
    : QRhiSwapChain(rhi),
      rt(rhi, this),
      cb(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 666, as _ZN17QNullRenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE
inline QNullRenderBuffer::QNullRenderBuffer(QRhiImplementation *rhi, Type type, const QSize &pixelSize,
                                     int sampleCount, QRhiRenderBuffer::Flags flags,
                                     QRhiTexture::Format backingFormatHint)
    : QRhiRenderBuffer(rhi, type, pixelSize, sampleCount, flags, backingFormatHint)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1027, as _ZN18QNullCommandBufferC1EP18QRhiImplementation
inline QNullCommandBuffer::QNullCommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1032, as _ZN18QNullCommandBufferD1Ev
inline QNullCommandBuffer::~QNullCommandBuffer()
{
    destroy();
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

//  from src/gui/rhi/qrhinull.cpp, line 1003, as _ZN20QNullComputePipelineC1EP18QRhiImplementation
inline QNullComputePipeline::QNullComputePipeline(QRhiImplementation *rhi)
    : QRhiComputePipeline(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 976, as _ZN21QNullGraphicsPipelineC1EP18QRhiImplementation
inline QNullGraphicsPipeline::QNullGraphicsPipeline(QRhiImplementation *rhi)
    : QRhiGraphicsPipeline(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 877, as _ZN24QNullTextureRenderTargetC1EP18QRhiImplementationRK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QNullTextureRenderTarget::QNullTextureRenderTarget(QRhiImplementation *rhi,
                                                   const QRhiTextureRenderTargetDescription &desc,
                                                   Flags flags)
    : QRhiTextureRenderTarget(rhi, desc, flags),
      d(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 942, as _ZN27QNullShaderResourceBindingsC1EP18QRhiImplementation
inline QNullShaderResourceBindings::QNullShaderResourceBindings(QRhiImplementation *rhi)
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

//  from src/gui/rhi/qrhinull.cpp, line 269, as _ZN8QRhiNull14setVertexInputEP17QRhiCommandBufferiiPKSt4pairIP10QRhiBufferjES4_jNS0_11IndexFormatE
inline void QRhiNull::setVertexInput(QRhiCommandBuffer *cb,
                              int startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput *bindings,
                              QRhiBuffer *indexBuf, quint32 indexOffset, QRhiCommandBuffer::IndexFormat indexFormat)
{
    Q_UNUSED(cb);
    Q_UNUSED(startBinding);
    Q_UNUSED(bindingCount);
    Q_UNUSED(bindings);
    Q_UNUSED(indexBuf);
    Q_UNUSED(indexOffset);
    Q_UNUSED(indexFormat);
}

//  from src/gui/rhi/qrhinull.cpp, line 259, as _ZN8QRhiNull18setShaderResourcesEP17QRhiCommandBufferP26QRhiShaderResourceBindingsiPKSt4pairIijE
inline void QRhiNull::setShaderResources(QRhiCommandBuffer *cb, QRhiShaderResourceBindings *srb,
                                  int dynamicOffsetCount,
                                  const QRhiCommandBuffer::DynamicOffset *dynamicOffsets)
{
    Q_UNUSED(cb);
    Q_UNUSED(srb);
    Q_UNUSED(dynamicOffsetCount);
    Q_UNUSED(dynamicOffsets);
}

//  from src/gui/rhi/qrhinull.cpp, line 422, as _ZN8QRhiNull19beginOffscreenFrameEPP17QRhiCommandBuffer6QFlagsIN4QRhi14BeginFrameFlagEE
inline QRhi::FrameOpResult QRhiNull::beginOffscreenFrame(QRhiCommandBuffer **cb, QRhi::BeginFrameFlags flags)
{
    Q_UNUSED(flags);
    *cb = &offscreenCommandBuffer;
    return QRhi::FrameOpSuccess;
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

//  from src/gui/rhi/qrhi.cpp, line 9181, as _ZNK18QRhiImplementation29enumerateAdaptersBeforeCreateEP17QRhiNativeHandles
inline QRhi::AdapterList QRhiImplementation::enumerateAdaptersBeforeCreate(QRhiNativeHandles *) const
{
    return {};
}

//  from src/gui/rhi/qrhinull.cpp, line 61, as _ZNK8QRhiNull21supportedSampleCountsEv
inline QList<int> QRhiNull::supportedSampleCounts() const
{
    return { 1 };
}

//  from src/gui/rhi/qrhinull.cpp, line 1037, as _ZN18QNullCommandBuffer7destroyEv
inline void QNullCommandBuffer::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhinull.cpp, line 847, as _ZN26QNullSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 853, as _ZN26QNullSwapChainRenderTargetD1Ev
inline QNullSwapChainRenderTarget::~QNullSwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 51, as _ZN8QRhiNull6createE6QFlagsIN4QRhi4FlagEE
inline bool QRhiNull::create(QRhi::Flags flags)
{
    Q_UNUSED(flags);
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 57, as _ZN8QRhiNull7destroyEv
inline void QRhiNull::destroy()
{
}

//  from src/gui/rhi/qrhinull.cpp, line 238, as _ZN8QRhiNull22createGraphicsPipelineEv
inline QRhiGraphicsPipeline *QRhiNull::createGraphicsPipeline()
{
    return new QNullGraphicsPipeline(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 243, as _ZN8QRhiNull21createComputePipelineEv
inline QRhiComputePipeline *QRhiNull::createComputePipeline()
{
    return new QNullComputePipeline(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 248, as _ZN8QRhiNull28createShaderResourceBindingsEv
inline QRhiShaderResourceBindings *QRhiNull::createShaderResourceBindings()
{
    return new QNullShaderResourceBindings(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 77, as _ZN8QRhiNull12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj
inline QRhiBuffer *QRhiNull::createBuffer(QRhiBuffer::Type type, QRhiBuffer::UsageFlags usage, quint32 size)
{
    return new QNullBuffer(this, type, usage, size);
}

//  from src/gui/rhi/qrhinull.cpp, line 206, as _ZN8QRhiNull18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE
inline QRhiRenderBuffer *QRhiNull::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize &pixelSize,
                                               int sampleCount, QRhiRenderBuffer::Flags flags,
                                               QRhiTexture::Format backingFormatHint)
{
    return new QNullRenderBuffer(this, type, pixelSize, sampleCount, flags, backingFormatHint);
}

//  from src/gui/rhi/qrhinull.cpp, line 213, as _ZN8QRhiNull13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE
inline QRhiTexture *QRhiNull::createTexture(QRhiTexture::Format format,
                                     const QSize &pixelSize, int depth, int arraySize,
                                     int sampleCount, QRhiTexture::Flags flags)
{
    return new QNullTexture(this, format, pixelSize, depth, arraySize, sampleCount, flags);
}

//  from src/gui/rhi/qrhinull.cpp, line 220, as _ZN8QRhiNull13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_
inline QRhiSampler *QRhiNull::createSampler(QRhiSampler::Filter magFilter, QRhiSampler::Filter minFilter,
                                     QRhiSampler::Filter mipmapMode,
                                     QRhiSampler::AddressMode u, QRhiSampler::AddressMode v, QRhiSampler::AddressMode w)
{
    return new QNullSampler(this, magFilter, minFilter, mipmapMode, u, v, w);
}

//  from src/gui/rhi/qrhinull.cpp, line 227, as _ZN8QRhiNull25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QRhiTextureRenderTarget *QRhiNull::createTextureRenderTarget(const QRhiTextureRenderTargetDescription &desc,
                                                             QRhiTextureRenderTarget::Flags flags)
{
    return new QNullTextureRenderTarget(this, desc, flags);
}

//  from src/gui/rhi/qrhinull.cpp, line 233, as _ZN8QRhiNull20createShadingRateMapEv
inline QRhiShadingRateMap *QRhiNull::createShadingRateMap()
{
    return nullptr;
}

//  from src/gui/rhi/qrhinull.cpp, line 72, as _ZN8QRhiNull15createSwapChainEv
inline QRhiSwapChain *QRhiNull::createSwapChain()
{
    return new QNullSwapChain(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 406, as _ZN8QRhiNull10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE
inline QRhi::FrameOpResult QRhiNull::beginFrame(QRhiSwapChain *swapChain, QRhi::BeginFrameFlags flags)
{
    Q_UNUSED(flags);
    currentSwapChain = swapChain;
    return QRhi::FrameOpSuccess;
}

//  from src/gui/rhi/qrhinull.cpp, line 413, as _ZN8QRhiNull8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE
inline QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain *swapChain, QRhi::EndFrameFlags flags)
{
    Q_UNUSED(flags);
    QNullSwapChain *swapChainD = QRHI_RES(QNullSwapChain, swapChain);
    swapChainD->frameCount += 1;
    currentSwapChain = nullptr;
    return QRhi::FrameOpSuccess;
}

//  from src/gui/rhi/qrhinull.cpp, line 429, as _ZN8QRhiNull17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE
inline QRhi::FrameOpResult QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags flags)
{
    Q_UNUSED(flags);
    return QRhi::FrameOpSuccess;
}

//  from src/gui/rhi/qrhinull.cpp, line 435, as _ZN8QRhiNull6finishEv
inline QRhi::FrameOpResult QRhiNull::finish()
{
    return QRhi::FrameOpSuccess;
}

//  from src/gui/rhi/qrhinull.cpp, line 515, as _ZN8QRhiNull14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiNull::resourceUpdate(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    Q_UNUSED(cb);
    QRhiResourceUpdateBatchPrivate *ud = QRhiResourceUpdateBatchPrivate::get(resourceUpdates);
    for (int opIdx = 0; opIdx < ud->activeBufferOpCount; ++opIdx) {
        const QRhiResourceUpdateBatchPrivate::BufferOp &u(ud->bufferOps[opIdx]);
        if (u.type == QRhiResourceUpdateBatchPrivate::BufferOp::DynamicUpdate
                || u.type == QRhiResourceUpdateBatchPrivate::BufferOp::StaticUpload)
        {
            QNullBuffer *bufD = QRHI_RES(QNullBuffer, u.buf);
            memcpy(bufD->data + u.offset, u.data.constData(), size_t(u.data.size()));
        } else if (u.type == QRhiResourceUpdateBatchPrivate::BufferOp::Read) {
            QRhiReadbackResult *result = u.result;
            result->data.resize(u.readSize);
            QNullBuffer *bufD = QRHI_RES(QNullBuffer, u.buf);
            memcpy(result->data.data(), bufD->data + u.offset, size_t(u.readSize));
            if (result->completed)
                result->completed();
        }
    }
    for (int opIdx = 0; opIdx < ud->activeTextureOpCount; ++opIdx) {
        const QRhiResourceUpdateBatchPrivate::TextureOp &u(ud->textureOps[opIdx]);
        if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Upload) {
            if (u.dst->format() == QRhiTexture::RGBA8)
                simulateTextureUpload(u);
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Copy) {
            if (u.src->format() == QRhiTexture::RGBA8 && u.dst->format() == QRhiTexture::RGBA8)
                simulateTextureCopy(u);
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Read) {
            QRhiReadbackResult *result = u.result;
            QNullTexture *texD = QRHI_RES(QNullTexture, u.rb.texture());
            if (texD) {
                result->format = texD->format();
                if (u.rb.rect().isValid())
                    result->pixelSize = u.rb.rect().size();
                else
                    result->pixelSize = q->sizeForMipLevel(u.rb.level(), texD->pixelSize());
            } else {
                Q_ASSERT(currentSwapChain);
                result->format = QRhiTexture::RGBA8;
                if (u.rb.rect().isValid())
                    result->pixelSize = u.rb.rect().size();
                else
                    result->pixelSize = currentSwapChain->currentPixelSize();
            }
            quint32 bytesPerLine = 0;
            quint32 byteSize = 0;
            textureFormatInfo(result->format, result->pixelSize, &bytesPerLine, &byteSize, nullptr);
            if (texD && texD->format() == QRhiTexture::RGBA8) {
                result->data.resize(int(byteSize));
                const QImage &src(texD->image[u.rb.layer()][u.rb.level()]);
                char *dst = result->data.data();
                for (int y = 0, h = src.height(); y < h; ++y) {
                    memcpy(dst, src.constScanLine(y), bytesPerLine);
                    dst += bytesPerLine;
                }
            } else {
                result->data.fill(0, int(byteSize));
            }
            if (result->completed)
                result->completed();
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::GenMips) {
            if (u.dst->format() == QRhiTexture::RGBA8)
                simulateTextureGenMips(u);
        }
    }
    ud->free();
}

//  from src/gui/rhi/qrhinull.cpp, line 584, as _ZN8QRhiNull9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiNull::beginPass(QRhiCommandBuffer *cb,
                         QRhiRenderTarget *rt,
                         const QColor &colorClearValue,
                         const QRhiDepthStencilClearValue &depthStencilClearValue,
                         QRhiResourceUpdateBatch *resourceUpdates,
                         QRhiCommandBuffer::BeginPassFlags flags)
{
    Q_UNUSED(colorClearValue);
    Q_UNUSED(depthStencilClearValue);
    Q_UNUSED(flags);

    if (resourceUpdates)
        resourceUpdate(cb, resourceUpdates);

    if (rt->resourceType() == QRhiRenderTarget::TextureRenderTarget) {
        QNullTextureRenderTarget *rtTex = QRHI_RES(QNullTextureRenderTarget, rt);
        if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QNullTexture, QNullRenderBuffer>(rtTex->description(), rtTex->d.currentResIdList))
            rtTex->create();
    }
}

//  from src/gui/rhi/qrhinull.cpp, line 605, as _ZN8QRhiNull7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiNull::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    if (resourceUpdates)
        resourceUpdate(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhinull.cpp, line 253, as _ZN8QRhiNull19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline
inline void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb, QRhiGraphicsPipeline *ps)
{
    Q_UNUSED(cb);
    Q_UNUSED(ps);
}

//  from src/gui/rhi/qrhinull.cpp, line 282, as _ZN8QRhiNull11setViewportEP17QRhiCommandBufferRK12QRhiViewport
inline void QRhiNull::setViewport(QRhiCommandBuffer *cb, const QRhiViewport &viewport)
{
    Q_UNUSED(cb);
    Q_UNUSED(viewport);
}

//  from src/gui/rhi/qrhinull.cpp, line 288, as _ZN8QRhiNull10setScissorEP17QRhiCommandBufferRK11QRhiScissor
inline void QRhiNull::setScissor(QRhiCommandBuffer *cb, const QRhiScissor &scissor)
{
    Q_UNUSED(cb);
    Q_UNUSED(scissor);
}

//  from src/gui/rhi/qrhinull.cpp, line 294, as _ZN8QRhiNull17setBlendConstantsEP17QRhiCommandBufferRK6QColor
inline void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
{
    Q_UNUSED(cb);
    Q_UNUSED(c);
}

//  from src/gui/rhi/qrhinull.cpp, line 300, as _ZN8QRhiNull13setStencilRefEP17QRhiCommandBufferj
inline void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
{
    Q_UNUSED(cb);
    Q_UNUSED(refValue);
}

//  from src/gui/rhi/qrhinull.cpp, line 306, as _ZN8QRhiNull14setShadingRateEP17QRhiCommandBufferRK5QSize
inline void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const QSize &coarsePixelSize)
{
    Q_UNUSED(cb);
    Q_UNUSED(coarsePixelSize);
}

//  from src/gui/rhi/qrhinull.cpp, line 312, as _ZN8QRhiNull4drawEP17QRhiCommandBufferjjjj
inline void QRhiNull::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
                    quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
{
    Q_UNUSED(cb);
    Q_UNUSED(vertexCount);
    Q_UNUSED(instanceCount);
    Q_UNUSED(firstVertex);
    Q_UNUSED(firstInstance);
}

//  from src/gui/rhi/qrhinull.cpp, line 322, as _ZN8QRhiNull11drawIndexedEP17QRhiCommandBufferjjjij
inline void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
                           quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32 firstInstance)
{
    Q_UNUSED(cb);
    Q_UNUSED(indexCount);
    Q_UNUSED(instanceCount);
    Q_UNUSED(firstIndex);
    Q_UNUSED(vertexOffset);
    Q_UNUSED(firstInstance);
}

//  from src/gui/rhi/qrhinull.cpp, line 333, as _ZN8QRhiNull12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj
inline void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                            quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    Q_UNUSED(cb);
    Q_UNUSED(indirectBuffer);
    Q_UNUSED(indirectBufferOffset);
    Q_UNUSED(drawCount);
    Q_UNUSED(stride);
}

//  from src/gui/rhi/qrhinull.cpp, line 343, as _ZN8QRhiNull19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj
inline void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                                   quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    Q_UNUSED(cb);
    Q_UNUSED(indirectBuffer);
    Q_UNUSED(indirectBufferOffset);
    Q_UNUSED(drawCount);
    Q_UNUSED(stride);
}

//  from src/gui/rhi/qrhinull.cpp, line 353, as _ZN8QRhiNull14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray
inline void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray &name)
{
    Q_UNUSED(cb);
    Q_UNUSED(name);
}

//  from src/gui/rhi/qrhinull.cpp, line 359, as _ZN8QRhiNull12debugMarkEndEP17QRhiCommandBuffer
inline void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
}

//  from src/gui/rhi/qrhinull.cpp, line 364, as _ZN8QRhiNull12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray
inline void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
{
    Q_UNUSED(cb);
    Q_UNUSED(msg);
}

//  from src/gui/rhi/qrhinull.cpp, line 611, as _ZN8QRhiNull16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
                                QRhiResourceUpdateBatch *resourceUpdates,
                                QRhiCommandBuffer::BeginPassFlags flags)
{
    Q_UNUSED(flags);
    if (resourceUpdates)
        resourceUpdate(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhinull.cpp, line 620, as _ZN8QRhiNull14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiNull::endComputePass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    if (resourceUpdates)
        resourceUpdate(cb, resourceUpdates);
}

//  from src/gui/rhi/qrhinull.cpp, line 370, as _ZN8QRhiNull18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline
inline void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb, QRhiComputePipeline *ps)
{
    Q_UNUSED(cb);
    Q_UNUSED(ps);
}

//  from src/gui/rhi/qrhinull.cpp, line 376, as _ZN8QRhiNull8dispatchEP17QRhiCommandBufferiii
inline void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
{
    Q_UNUSED(cb);
    Q_UNUSED(x);
    Q_UNUSED(y);
    Q_UNUSED(z);
}

//  from src/gui/rhi/qrhinull.cpp, line 384, as _ZN8QRhiNull13nativeHandlesEP17QRhiCommandBuffer
inline const QRhiNativeHandles *QRhiNull::nativeHandles(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
    return nullptr;
}

//  from src/gui/rhi/qrhinull.cpp, line 390, as _ZN8QRhiNull13beginExternalEP17QRhiCommandBuffer
inline void QRhiNull::beginExternal(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
}

//  from src/gui/rhi/qrhinull.cpp, line 395, as _ZN8QRhiNull11endExternalEP17QRhiCommandBuffer
inline void QRhiNull::endExternal(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
}

//  from src/gui/rhi/qrhinull.cpp, line 400, as _ZN8QRhiNull20lastCompletedGpuTimeEP17QRhiCommandBuffer
inline double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
    return 0;
}

//  from src/gui/rhi/qrhinull.cpp, line 66, as _ZNK8QRhiNull21supportedShadingRatesEi
inline QList<QSize> QRhiNull::supportedShadingRates(int sampleCount) const
{
    Q_UNUSED(sampleCount);
    return { QSize(1, 1) };
}

//  from src/gui/rhi/qrhinull.cpp, line 82, as _ZNK8QRhiNull13ubufAlignmentEv
inline int QRhiNull::ubufAlignment() const
{
    return 256;
}

//  from src/gui/rhi/qrhinull.cpp, line 87, as _ZNK8QRhiNull18isYUpInFramebufferEv
inline bool QRhiNull::isYUpInFramebuffer() const
{
    return false;
}

//  from src/gui/rhi/qrhinull.cpp, line 92, as _ZNK8QRhiNull10isYUpInNDCEv
inline bool QRhiNull::isYUpInNDC() const
{
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 97, as _ZNK8QRhiNull20isClipDepthZeroToOneEv
inline bool QRhiNull::isClipDepthZeroToOne() const
{
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 102, as _ZNK8QRhiNull19clipSpaceCorrMatrixEv
inline QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const
{
    return QMatrix4x4(); // identity
}

//  from src/gui/rhi/qrhinull.cpp, line 107, as _ZNK8QRhiNull24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE
inline bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format format, QRhiTexture::Flags flags) const
{
    Q_UNUSED(format);
    Q_UNUSED(flags);
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 114, as _ZNK8QRhiNull18isFeatureSupportedEN4QRhi7FeatureE
inline bool QRhiNull::isFeatureSupported(QRhi::Feature feature) const
{
    Q_UNUSED(feature);
    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 120, as _ZNK8QRhiNull13resourceLimitEN4QRhi13ResourceLimitE
inline int QRhiNull::resourceLimit(QRhi::ResourceLimit limit) const
{
    switch (limit) {
    case QRhi::TextureSizeMin:
        return 1;
    case QRhi::TextureSizeMax:
        return 16384;
    case QRhi::MaxColorAttachments:
        return 8;
    case QRhi::FramesInFlight:
        return 1;
    case QRhi::MaxAsyncReadbackFrames:
        return 1;
    case QRhi::MaxThreadGroupsPerDimension:
        return 0;
    case QRhi::MaxThreadsPerThreadGroup:
        return 0;
    case QRhi::MaxThreadGroupX:
        return 0;
    case QRhi::MaxThreadGroupY:
        return 0;
    case QRhi::MaxThreadGroupZ:
        return 0;
    case QRhi::TextureArraySizeMax:
        return 2048;
    case QRhi::MaxUniformBufferRange:
        return 65536;
    case QRhi::MaxVertexInputs:
        return 32;
    case QRhi::MaxVertexOutputs:
        return 32;
    case QRhi::ShadingRateImageTileSize:
        return 0;
    }

    Q_UNREACHABLE_RETURN(0);
}

//  from src/gui/rhi/qrhinull.cpp, line 158, as _ZN8QRhiNull13nativeHandlesEv
inline const QRhiNativeHandles *QRhiNull::nativeHandles()
{
    return &nativeHandlesStruct;
}

//  from src/gui/rhi/qrhinull.cpp, line 163, as _ZNK8QRhiNull10driverInfoEv
inline QRhiDriverInfo QRhiNull::driverInfo() const
{
    QRhiDriverInfo info;
    info.deviceName = QByteArrayLiteral("Null");
    return info;
}

//  from src/gui/rhi/qrhinull.cpp, line 170, as _ZN8QRhiNull10statisticsEv
inline QRhiStats QRhiNull::statistics()
{
    return {};
}

//  from src/gui/rhi/qrhinull.cpp, line 175, as _ZN8QRhiNull35makeThreadLocalNativeContextCurrentEv
inline bool QRhiNull::makeThreadLocalNativeContextCurrent()
{
    // not applicable
    return false;
}

//  from src/gui/rhi/qrhinull.cpp, line 181, as _ZN8QRhiNull20setQueueSubmitParamsEP17QRhiNativeHandles
inline void QRhiNull::setQueueSubmitParams(QRhiNativeHandles *)
{
    // not applicable
}

//  from src/gui/rhi/qrhinull.cpp, line 186, as _ZN8QRhiNull22releaseCachedResourcesEv
inline void QRhiNull::releaseCachedResources()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhinull.cpp, line 191, as _ZNK8QRhiNull12isDeviceLostEv
inline bool QRhiNull::isDeviceLost() const
{
    return false;
}

//  from src/gui/rhi/qrhinull.cpp, line 196, as _ZN8QRhiNull17pipelineCacheDataEv
inline QByteArray QRhiNull::pipelineCacheData()
{
    return QByteArray();
}

//  from src/gui/rhi/qrhinull.cpp, line 201, as _ZN8QRhiNull20setPipelineCacheDataERK10QByteArray
inline void QRhiNull::setPipelineCacheData(const QByteArray &data)
{
    Q_UNUSED(data);
}

//  from src/gui/rhi/qrhinull.cpp, line 440, as _ZN8QRhiNull21simulateTextureUploadERKN30QRhiResourceUpdateBatchPrivate9TextureOpE
inline void QRhiNull::simulateTextureUpload(const QRhiResourceUpdateBatchPrivate::TextureOp &u)
{
    QNullTexture *texD = QRHI_RES(QNullTexture, u.dst);
    for (int layer = 0, maxLayer = u.subresDesc.size(); layer < maxLayer; ++layer) {
        for (int level = 0; level < QRhi::MAX_MIP_LEVELS; ++level) {
            for (const QRhiTextureSubresourceUploadDescription &subresDesc : std::as_const(u.subresDesc[layer][level])) {
                if (!subresDesc.image().isNull()) {
                    const QImage src = subresDesc.image();
                    QPainter painter(&texD->image[layer][level]);
                    const QSize srcSize = subresDesc.sourceSize().isEmpty()
                            ? src.size() : subresDesc.sourceSize();
                    painter.setCompositionMode(QPainter::CompositionMode_Source);
                    painter.drawImage(subresDesc.destinationTopLeft(), src,
                                      QRect(subresDesc.sourceTopLeft(), srcSize));
                } else if (!subresDesc.data().isEmpty()) {
                    const QSize subresSize = q->sizeForMipLevel(level, texD->pixelSize());
                    int w = subresSize.width();
                    int h = subresSize.height();
                    if (!subresDesc.sourceSize().isEmpty()) {
                        w = subresDesc.sourceSize().width();
                        h = subresDesc.sourceSize().height();
                    }
                    // sourceTopLeft is not supported on this path as per QRhi docs
                    const QByteArray srcData = subresDesc.data();
                    const QPoint dstOffset = subresDesc.destinationTopLeft();
                    QSize size = clampedSubResourceUploadSize(QSize(w, h), dstOffset, level,
                                                              texD->pixelSize());
                    size = clampedSubResourceUploadSizeForSourceData(size, subresDesc.dataStride(),
                                                                     4, srcData.size());
                    if (size.isEmpty())
                        continue;
                    w = size.width();
                    h = size.height();
                    const char *src = srcData.constData();
                    const int srcBpl = w * 4;
                    int srcStride = srcBpl;
                    if (subresDesc.dataStride())
                        srcStride = subresDesc.dataStride();
                    uchar *dst = texD->image[layer][level].bits();
                    const int dstBpl = texD->image[layer][level].bytesPerLine();
                    for (int y = 0; y < h; ++y) {
                        memcpy(dst + dstOffset.x() * 4 + (y + dstOffset.y()) * dstBpl,
                               src + y * srcStride,
                               size_t(srcBpl));
                    }
                }
            }
        }
    }
}

//  from src/gui/rhi/qrhinull.cpp, line 491, as _ZN8QRhiNull19simulateTextureCopyERKN30QRhiResourceUpdateBatchPrivate9TextureOpE
inline void QRhiNull::simulateTextureCopy(const QRhiResourceUpdateBatchPrivate::TextureOp &u)
{
    QNullTexture *srcD = QRHI_RES(QNullTexture, u.src);
    QNullTexture *dstD = QRHI_RES(QNullTexture, u.dst);
    const QImage &srcImage(srcD->image[u.desc.sourceLayer()][u.desc.sourceLevel()]);
    QImage &dstImage(dstD->image[u.desc.destinationLayer()][u.desc.destinationLevel()]);
    const QPoint dstPos = u.desc.destinationTopLeft();
    const QSize size = u.desc.pixelSize().isEmpty() ? srcD->pixelSize() : u.desc.pixelSize();
    const QPoint srcPos = u.desc.sourceTopLeft();

    QPainter painter(&dstImage);
    painter.setCompositionMode(QPainter::CompositionMode_Source);
    painter.drawImage(QRect(dstPos, size), srcImage, QRect(srcPos, size));
}

//  from src/gui/rhi/qrhinull.cpp, line 506, as _ZN8QRhiNull22simulateTextureGenMipsERKN30QRhiResourceUpdateBatchPrivate9TextureOpE
inline void QRhiNull::simulateTextureGenMips(const QRhiResourceUpdateBatchPrivate::TextureOp &u)
{
    QNullTexture *texD = QRHI_RES(QNullTexture, u.dst);
    const QSize baseSize = texD->pixelSize();
    const int levelCount = q->mipLevelsForSize(baseSize);
    for (int level = 1; level < levelCount; ++level)
        texD->image[0][level] = texD->image[0][0].scaled(q->sizeForMipLevel(level, baseSize));
}
//  -----------------------------------------------------------------------

//  A QRhiNull that Python can take functions over in. Every QRhiNull
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRhiNullCall0)(const void *, int, int *);
typedef void (*CuteQRhiNullCall1)(const void *, int *);
typedef void * (*CuteQRhiNullCall2)(const void *, int *);
typedef void * (*CuteQRhiNullCall3)(const void *, int *);
typedef void * (*CuteQRhiNullCall4)(const void *, int *);
typedef void * (*CuteQRhiNullCall5)(const void *, int, int, quint32, int *);
typedef void * (*CuteQRhiNullCall6)(const void *, int, const QSize *, int, int, int, int *);
typedef void * (*CuteQRhiNullCall7)(const void *, int, const QSize *, int, int, int, int, int *);
typedef void * (*CuteQRhiNullCall8)(const void *, int, int, int, int, int, int, int *);
typedef void * (*CuteQRhiNullCall9)(const void *, const QRhiTextureRenderTargetDescription *, int, int *);
typedef void * (*CuteQRhiNullCall10)(const void *, int *);
typedef void * (*CuteQRhiNullCall11)(const void *, int *);
typedef int (*CuteQRhiNullCall12)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiNullCall13)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiNullCall14)(const void *, int, int *);
typedef int (*CuteQRhiNullCall15)(const void *, int *);
typedef void (*CuteQRhiNullCall16)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiNullCall17)(const void *, QRhiCommandBuffer *, QRhiRenderTarget *, const QColor *, const QRhiDepthStencilClearValue *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiNullCall18)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiNullCall19)(const void *, QRhiCommandBuffer *, QRhiGraphicsPipeline *, int *);
typedef void (*CuteQRhiNullCall20)(const void *, QRhiCommandBuffer *, const QRhiViewport *, int *);
typedef void (*CuteQRhiNullCall21)(const void *, QRhiCommandBuffer *, const QRhiScissor *, int *);
typedef void (*CuteQRhiNullCall22)(const void *, QRhiCommandBuffer *, const QColor *, int *);
typedef void (*CuteQRhiNullCall23)(const void *, QRhiCommandBuffer *, quint32, int *);
typedef void (*CuteQRhiNullCall24)(const void *, QRhiCommandBuffer *, const QSize *, int *);
typedef void (*CuteQRhiNullCall25)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiNullCall26)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, qint32, quint32, int *);
typedef void (*CuteQRhiNullCall27)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiNullCall28)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiNullCall29)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiNullCall30)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiNullCall31)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiNullCall32)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiNullCall33)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiNullCall34)(const void *, QRhiCommandBuffer *, QRhiComputePipeline *, int *);
typedef void (*CuteQRhiNullCall35)(const void *, QRhiCommandBuffer *, int, int, int, int *);
typedef void * (*CuteQRhiNullCall36)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiNullCall37)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiNullCall38)(const void *, QRhiCommandBuffer *, int *);
typedef double (*CuteQRhiNullCall39)(const void *, QRhiCommandBuffer *, int *);
typedef int (*CuteQRhiNullCall40)(const void *, int *);
typedef bool (*CuteQRhiNullCall41)(const void *, int *);
typedef bool (*CuteQRhiNullCall42)(const void *, int *);
typedef bool (*CuteQRhiNullCall43)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQRhiNullCall44)(const void *, int *);
typedef bool (*CuteQRhiNullCall45)(const void *, int, int, int *);
typedef bool (*CuteQRhiNullCall46)(const void *, int, int *);
typedef int (*CuteQRhiNullCall47)(const void *, int, int *);
typedef void * (*CuteQRhiNullCall48)(const void *, int *);
typedef const QRhiDriverInfo * (*CuteQRhiNullCall49)(const void *, int *);
typedef const QRhiStats * (*CuteQRhiNullCall50)(const void *, int *);
typedef bool (*CuteQRhiNullCall51)(const void *, int *);
typedef void (*CuteQRhiNullCall52)(const void *, QRhiNativeHandles *, int *);
typedef void (*CuteQRhiNullCall53)(const void *, int *);
typedef bool (*CuteQRhiNullCall54)(const void *, int *);
typedef const QByteArray * (*CuteQRhiNullCall55)(const void *, int *);
typedef void (*CuteQRhiNullCall56)(const void *, const QByteArray *, int *);
class CuteQRhiNull : public QRhiNull {
public:
  using QRhiNull::QRhiNull;
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

  //  bool QRhiNull::create(QRhi::Flags flags)
  bool create(QRhi::Flags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiNullCall0 call = reinterpret_cast<CuteQRhiNullCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiNull::create(flags);
  }

  //  void QRhiNull::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiNullCall1 call = reinterpret_cast<CuteQRhiNullCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiNull::destroy();
  }

  //  QRhiGraphicsPipeline *QRhiNull::createGraphicsPipeline()
  QRhiGraphicsPipeline *createGraphicsPipeline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiNullCall2 call = reinterpret_cast<CuteQRhiNullCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiGraphicsPipeline *>(given);
    }
    return QRhiNull::createGraphicsPipeline();
  }

  //  QRhiComputePipeline *QRhiNull::createComputePipeline()
  QRhiComputePipeline *createComputePipeline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiNullCall3 call = reinterpret_cast<CuteQRhiNullCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiComputePipeline *>(given);
    }
    return QRhiNull::createComputePipeline();
  }

  //  QRhiShaderResourceBindings *QRhiNull::createShaderResourceBindings()
  QRhiShaderResourceBindings *createShaderResourceBindings() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiNullCall4 call = reinterpret_cast<CuteQRhiNullCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShaderResourceBindings *>(given);
    }
    return QRhiNull::createShaderResourceBindings();
  }

  //  QRhiBuffer *QRhiNull::createBuffer(QRhiBuffer::Type type,
  //      QRhiBuffer::UsageFlags usage, quint32 size)
  QRhiBuffer *createBuffer(
      QRhiBuffer::Type type,
      QRhiBuffer::UsageFlags usage,
      quint32 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiNullCall5 call = reinterpret_cast<CuteQRhiNullCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), static_cast<int>(usage.toInt()), size, &handled);
      if (handled) return static_cast<QRhiBuffer *>(given);
    }
    return QRhiNull::createBuffer(type, usage, size);
  }

  //  QRhiRenderBuffer *QRhiNull::createRenderBuffer(QRhiRenderBuffer::Type
  //      type, const QSize &pixelSize, int sampleCount,
  //      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
  //      backingFormatHint)
  QRhiRenderBuffer *createRenderBuffer(
      QRhiRenderBuffer::Type type,
      const QSize &pixelSize,
      int sampleCount,
      QRhiRenderBuffer::Flags flags,
      QRhiTexture::Format backingFormatHint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiNullCall6 call = reinterpret_cast<CuteQRhiNullCall6>(taken[6]);
      void * given = call(this, static_cast<int>(type), &pixelSize, sampleCount, static_cast<int>(flags.toInt()), static_cast<int>(backingFormatHint), &handled);
      if (handled) return static_cast<QRhiRenderBuffer *>(given);
    }
    return QRhiNull::createRenderBuffer(type, pixelSize, sampleCount, flags, backingFormatHint);
  }

  //  QRhiTexture *QRhiNull::createTexture(QRhiTexture::Format format,
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
      CuteQRhiNullCall7 call = reinterpret_cast<CuteQRhiNullCall7>(taken[7]);
      void * given = call(this, static_cast<int>(format), &pixelSize, depth, arraySize, sampleCount, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QRhiNull::createTexture(format, pixelSize, depth, arraySize, sampleCount, flags);
  }

  //  QRhiSampler *QRhiNull::createSampler(QRhiSampler::Filter magFilter,
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
      CuteQRhiNullCall8 call = reinterpret_cast<CuteQRhiNullCall8>(taken[8]);
      void * given = call(this, static_cast<int>(magFilter), static_cast<int>(minFilter), static_cast<int>(mipmapMode), static_cast<int>(u), static_cast<int>(v), static_cast<int>(w), &handled);
      if (handled) return static_cast<QRhiSampler *>(given);
    }
    return QRhiNull::createSampler(magFilter, minFilter, mipmapMode, u, v, w);
  }

  //  QRhiTextureRenderTarget *QRhiNull::createTextureRenderTarget(const
  //      QRhiTextureRenderTargetDescription &desc,
  //      QRhiTextureRenderTarget::Flags flags)
  QRhiTextureRenderTarget *createTextureRenderTarget(
      const QRhiTextureRenderTargetDescription &desc,
      QRhiTextureRenderTarget::Flags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiNullCall9 call = reinterpret_cast<CuteQRhiNullCall9>(taken[9]);
      void * given = call(this, &desc, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTextureRenderTarget *>(given);
    }
    return QRhiNull::createTextureRenderTarget(desc, flags);
  }

  //  QRhiShadingRateMap *QRhiNull::createShadingRateMap()
  QRhiShadingRateMap *createShadingRateMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiNullCall10 call = reinterpret_cast<CuteQRhiNullCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShadingRateMap *>(given);
    }
    return QRhiNull::createShadingRateMap();
  }

  //  QRhiSwapChain *QRhiNull::createSwapChain()
  QRhiSwapChain *createSwapChain() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiNullCall11 call = reinterpret_cast<CuteQRhiNullCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiSwapChain *>(given);
    }
    return QRhiNull::createSwapChain();
  }

  //  QRhi::FrameOpResult QRhiNull::beginFrame(QRhiSwapChain *swapChain,
  //      QRhi::BeginFrameFlags flags)
  QRhi::FrameOpResult beginFrame(
      QRhiSwapChain *swapChain,
      QRhi::BeginFrameFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiNullCall12 call = reinterpret_cast<CuteQRhiNullCall12>(taken[12]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiNull::beginFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain *swapChain,
  //      QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endFrame(
      QRhiSwapChain *swapChain,
      QRhi::EndFrameFlags flags) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiNullCall13 call = reinterpret_cast<CuteQRhiNullCall13>(taken[13]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiNull::endFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags
  //      flags)
  QRhi::FrameOpResult endOffscreenFrame(QRhi::EndFrameFlags flags) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiNullCall14 call = reinterpret_cast<CuteQRhiNullCall14>(taken[14]);
      int given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiNull::endOffscreenFrame(flags);
  }

  //  QRhi::FrameOpResult QRhiNull::finish()
  QRhi::FrameOpResult finish() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiNullCall15 call = reinterpret_cast<CuteQRhiNullCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiNull::finish();
  }

  //  void QRhiNull::resourceUpdate(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void resourceUpdate(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiNullCall16 call = reinterpret_cast<CuteQRhiNullCall16>(taken[16]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiNull::resourceUpdate(cb, resourceUpdates);
  }

  //  void QRhiNull::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
  //      const QColor &colorClearValue, const QRhiDepthStencilClearValue
  //      &depthStencilClearValue, QRhiResourceUpdateBatch
  //      *resourceUpdates, QRhiCommandBuffer::BeginPassFlags flags)
  void beginPass(
      QRhiCommandBuffer *cb,
      QRhiRenderTarget *rt,
      const QColor &colorClearValue,
      const QRhiDepthStencilClearValue &depthStencilClearValue,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRhiNullCall17 call = reinterpret_cast<CuteQRhiNullCall17>(taken[17]);
      call(this, cb, rt, &colorClearValue, &depthStencilClearValue, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiNull::beginPass(cb, rt, colorClearValue, depthStencilClearValue, resourceUpdates, flags);
  }

  //  void QRhiNull::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
  //      *resourceUpdates)
  void endPass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiNullCall18 call = reinterpret_cast<CuteQRhiNullCall18>(taken[18]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiNull::endPass(cb, resourceUpdates);
  }

  //  void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb,
  //      QRhiGraphicsPipeline *ps)
  void setGraphicsPipeline(
      QRhiCommandBuffer *cb,
      QRhiGraphicsPipeline *ps) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiNullCall19 call = reinterpret_cast<CuteQRhiNullCall19>(taken[19]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiNull::setGraphicsPipeline(cb, ps);
  }

  //  void QRhiNull::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
  //      &viewport)
  void setViewport(
      QRhiCommandBuffer *cb,
      const QRhiViewport &viewport) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiNullCall20 call = reinterpret_cast<CuteQRhiNullCall20>(taken[20]);
      call(this, cb, &viewport, &handled);
      if (handled) return;
    }
    QRhiNull::setViewport(cb, viewport);
  }

  //  void QRhiNull::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
  //      &scissor)
  void setScissor(
      QRhiCommandBuffer *cb,
      const QRhiScissor &scissor) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiNullCall21 call = reinterpret_cast<CuteQRhiNullCall21>(taken[21]);
      call(this, cb, &scissor, &handled);
      if (handled) return;
    }
    QRhiNull::setScissor(cb, scissor);
  }

  //  void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const QColor
  //      &c)
  void setBlendConstants(QRhiCommandBuffer *cb, const QColor &c) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiNullCall22 call = reinterpret_cast<CuteQRhiNullCall22>(taken[22]);
      call(this, cb, &c, &handled);
      if (handled) return;
    }
    QRhiNull::setBlendConstants(cb, c);
  }

  //  void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
  void setStencilRef(QRhiCommandBuffer *cb, quint32 refValue) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiNullCall23 call = reinterpret_cast<CuteQRhiNullCall23>(taken[23]);
      call(this, cb, refValue, &handled);
      if (handled) return;
    }
    QRhiNull::setStencilRef(cb, refValue);
  }

  //  void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const QSize
  //      &coarsePixelSize)
  void setShadingRate(
      QRhiCommandBuffer *cb,
      const QSize &coarsePixelSize) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiNullCall24 call = reinterpret_cast<CuteQRhiNullCall24>(taken[24]);
      call(this, cb, &coarsePixelSize, &handled);
      if (handled) return;
    }
    QRhiNull::setShadingRate(cb, coarsePixelSize);
  }

  //  void QRhiNull::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
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
      CuteQRhiNullCall25 call = reinterpret_cast<CuteQRhiNullCall25>(taken[25]);
      call(this, cb, vertexCount, instanceCount, firstVertex, firstInstance, &handled);
      if (handled) return;
    }
    QRhiNull::draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
  }

  //  void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
  //      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
  //      quint32 firstInstance)
  void drawIndexed(
      QRhiCommandBuffer *cb,
      quint32 indexCount,
      quint32 instanceCount,
      quint32 firstIndex,
      qint32 vertexOffset,
      quint32 firstInstance) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRhiNullCall26 call = reinterpret_cast<CuteQRhiNullCall26>(taken[26]);
      call(this, cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance, &handled);
      if (handled) return;
    }
    QRhiNull::drawIndexed(cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance);
  }

  //  void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
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
      CuteQRhiNullCall27 call = reinterpret_cast<CuteQRhiNullCall27>(taken[27]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiNull::drawIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
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
      CuteQRhiNullCall28 call = reinterpret_cast<CuteQRhiNullCall28>(taken[28]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiNull::drawIndexedIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
  //      &name)
  void debugMarkBegin(
      QRhiCommandBuffer *cb,
      const QByteArray &name) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiNullCall29 call = reinterpret_cast<CuteQRhiNullCall29>(taken[29]);
      call(this, cb, &name, &handled);
      if (handled) return;
    }
    QRhiNull::debugMarkBegin(cb, name);
  }

  //  void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)
  void debugMarkEnd(QRhiCommandBuffer *cb) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiNullCall30 call = reinterpret_cast<CuteQRhiNullCall30>(taken[30]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiNull::debugMarkEnd(cb);
  }

  //  void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
  //      &msg)
  void debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiNullCall31 call = reinterpret_cast<CuteQRhiNullCall31>(taken[31]);
      call(this, cb, &msg, &handled);
      if (handled) return;
    }
    QRhiNull::debugMarkMsg(cb, msg);
  }

  //  void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiNullCall32 call = reinterpret_cast<CuteQRhiNullCall32>(taken[32]);
      call(this, cb, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiNull::beginComputePass(cb, resourceUpdates, flags);
  }

  //  void QRhiNull::endComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiNullCall33 call = reinterpret_cast<CuteQRhiNullCall33>(taken[33]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiNull::endComputePass(cb, resourceUpdates);
  }

  //  void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb,
  //      QRhiComputePipeline *ps)
  void setComputePipeline(
      QRhiCommandBuffer *cb,
      QRhiComputePipeline *ps) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiNullCall34 call = reinterpret_cast<CuteQRhiNullCall34>(taken[34]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiNull::setComputePipeline(cb, ps);
  }

  //  void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
  void dispatch(QRhiCommandBuffer *cb, int x, int y, int z) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiNullCall35 call = reinterpret_cast<CuteQRhiNullCall35>(taken[35]);
      call(this, cb, x, y, z, &handled);
      if (handled) return;
    }
    QRhiNull::dispatch(cb, x, y, z);
  }

  //  const QRhiNativeHandles *QRhiNull::nativeHandles(QRhiCommandBuffer
  //      *cb)
  const QRhiNativeHandles *nativeHandles(QRhiCommandBuffer *cb) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiNullCall36 call = reinterpret_cast<CuteQRhiNullCall36>(taken[36]);
      void * given = call(this, cb, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiNull::nativeHandles(cb);
  }

  //  void QRhiNull::beginExternal(QRhiCommandBuffer *cb)
  void beginExternal(QRhiCommandBuffer *cb) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiNullCall37 call = reinterpret_cast<CuteQRhiNullCall37>(taken[37]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiNull::beginExternal(cb);
  }

  //  void QRhiNull::endExternal(QRhiCommandBuffer *cb)
  void endExternal(QRhiCommandBuffer *cb) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiNullCall38 call = reinterpret_cast<CuteQRhiNullCall38>(taken[38]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiNull::endExternal(cb);
  }

  //  double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer *cb)
  double lastCompletedGpuTime(QRhiCommandBuffer *cb) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiNullCall39 call = reinterpret_cast<CuteQRhiNullCall39>(taken[39]);
      double given = call(this, cb, &handled);
      if (handled) return given;
    }
    return QRhiNull::lastCompletedGpuTime(cb);
  }

  //  int QRhiNull::ubufAlignment() const
  int ubufAlignment() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiNullCall40 call = reinterpret_cast<CuteQRhiNullCall40>(taken[40]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::ubufAlignment();
  }

  //  bool QRhiNull::isYUpInFramebuffer() const
  bool isYUpInFramebuffer() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiNullCall41 call = reinterpret_cast<CuteQRhiNullCall41>(taken[41]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::isYUpInFramebuffer();
  }

  //  bool QRhiNull::isYUpInNDC() const
  bool isYUpInNDC() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiNullCall42 call = reinterpret_cast<CuteQRhiNullCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::isYUpInNDC();
  }

  //  bool QRhiNull::isClipDepthZeroToOne() const
  bool isClipDepthZeroToOne() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRhiNullCall43 call = reinterpret_cast<CuteQRhiNullCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::isClipDepthZeroToOne();
  }

  //  QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const
  QMatrix4x4 clipSpaceCorrMatrix() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQRhiNullCall44 call = reinterpret_cast<CuteQRhiNullCall44>(taken[44]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiNull::clipSpaceCorrMatrix();
  }

  //  bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format format,
  //      QRhiTexture::Flags flags) const
  bool isTextureFormatSupported(
      QRhiTexture::Format format,
      QRhiTexture::Flags flags) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQRhiNullCall45 call = reinterpret_cast<CuteQRhiNullCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiNull::isTextureFormatSupported(format, flags);
  }

  //  bool QRhiNull::isFeatureSupported(QRhi::Feature feature) const
  bool isFeatureSupported(QRhi::Feature feature) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQRhiNullCall46 call = reinterpret_cast<CuteQRhiNullCall46>(taken[46]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return QRhiNull::isFeatureSupported(feature);
  }

  //  int QRhiNull::resourceLimit(QRhi::ResourceLimit limit) const
  int resourceLimit(QRhi::ResourceLimit limit) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQRhiNullCall47 call = reinterpret_cast<CuteQRhiNullCall47>(taken[47]);
      int given = call(this, static_cast<int>(limit), &handled);
      if (handled) return given;
    }
    return QRhiNull::resourceLimit(limit);
  }

  //  const QRhiNativeHandles *QRhiNull::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[48]) {
      int handled = 0;
      CuteQRhiNullCall48 call = reinterpret_cast<CuteQRhiNullCall48>(taken[48]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiNull::nativeHandles();
  }

  //  QRhiDriverInfo QRhiNull::driverInfo() const
  QRhiDriverInfo driverInfo() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQRhiNullCall49 call = reinterpret_cast<CuteQRhiNullCall49>(taken[49]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiNull::driverInfo();
  }

  //  QRhiStats QRhiNull::statistics()
  QRhiStats statistics() override {
    if (taken[50]) {
      int handled = 0;
      CuteQRhiNullCall50 call = reinterpret_cast<CuteQRhiNullCall50>(taken[50]);
      const QRhiStats * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiNull::statistics();
  }

  //  bool QRhiNull::makeThreadLocalNativeContextCurrent()
  bool makeThreadLocalNativeContextCurrent() override {
    if (taken[51]) {
      int handled = 0;
      CuteQRhiNullCall51 call = reinterpret_cast<CuteQRhiNullCall51>(taken[51]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::makeThreadLocalNativeContextCurrent();
  }

  //  void QRhiNull::setQueueSubmitParams(QRhiNativeHandles *params)
  void setQueueSubmitParams(QRhiNativeHandles *params) override {
    if (taken[52]) {
      int handled = 0;
      CuteQRhiNullCall52 call = reinterpret_cast<CuteQRhiNullCall52>(taken[52]);
      call(this, params, &handled);
      if (handled) return;
    }
    QRhiNull::setQueueSubmitParams(params);
  }

  //  void QRhiNull::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[53]) {
      int handled = 0;
      CuteQRhiNullCall53 call = reinterpret_cast<CuteQRhiNullCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiNull::releaseCachedResources();
  }

  //  bool QRhiNull::isDeviceLost() const
  bool isDeviceLost() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQRhiNullCall54 call = reinterpret_cast<CuteQRhiNullCall54>(taken[54]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiNull::isDeviceLost();
  }

  //  QByteArray QRhiNull::pipelineCacheData()
  QByteArray pipelineCacheData() override {
    if (taken[55]) {
      int handled = 0;
      CuteQRhiNullCall55 call = reinterpret_cast<CuteQRhiNullCall55>(taken[55]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiNull::pipelineCacheData();
  }

  //  void QRhiNull::setPipelineCacheData(const QByteArray &data)
  void setPipelineCacheData(const QByteArray &data) override {
    if (taken[56]) {
      int handled = 0;
      CuteQRhiNullCall56 call = reinterpret_cast<CuteQRhiNullCall56>(taken[56]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QRhiNull::setPipelineCacheData(data);
  }
};

//  bool QRhiNull::create(QRhi::Flags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QRhiNull6createE6QFlagsIN4QRhi4FlagEE(
    QRhiNull *self,
    int flags) {
  return self->create(QFlags<QRhi::Flag>::fromInt(flags));
}

//  void QRhiNull::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull7destroyEv(QRhiNull *self) {
  self->destroy();
}

//  QRhiGraphicsPipeline *QRhiNull::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN8QRhiNull22createGraphicsPipelineEv(
    QRhiNull *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiNull::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN8QRhiNull21createComputePipelineEv(
    QRhiNull *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings *QRhiNull::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN8QRhiNull28createShaderResourceBindingsEv(
    QRhiNull *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiNull::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN8QRhiNull12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiNull *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer *QRhiNull::createRenderBuffer(QRhiRenderBuffer::Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN8QRhiNull18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiNull *self,
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

//  QRhiTexture *QRhiNull::createTexture(QRhiTexture::Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN8QRhiNull13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiNull *self,
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

//  QRhiSampler *QRhiNull::createSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN8QRhiNull13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiNull *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget *QRhiNull::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN8QRhiNull25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiNull *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiNull::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN8QRhiNull20createShadingRateMapEv(
    QRhiNull *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiNull::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN8QRhiNull15createSwapChainEv(QRhiNull *self) {
  return self->createSwapChain();
}

//  QRhi::FrameOpResult QRhiNull::beginFrame(QRhiSwapChain *swapChain,
//      QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN8QRhiNull10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiNull *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->beginFrame(
      swapChain,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain *swapChain,
//      QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN8QRhiNull8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiNull *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->endFrame(
      swapChain,
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN8QRhiNull17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiNull *self,
    int flags) {
  return self->endOffscreenFrame(QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN8QRhiNull6finishEv(QRhiNull *self) {
  return self->finish();
}

//  void QRhiNull::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiNull::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiNull *self,
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

//  void QRhiNull::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(cb, ps);
}

//  void QRhiNull::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull11setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->setViewport(cb, *viewport);
}

//  void QRhiNull::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull10setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->setScissor(cb, *scissor);
}

//  void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull17setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->setBlendConstants(cb, *c);
}

//  void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull13setStencilRefEP17QRhiCommandBufferj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->setStencilRef(cb, refValue);
}

//  void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiNull::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull4drawEP17QRhiCommandBufferjjjj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull11drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiNull *self,
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

//  void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiNull *self,
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

//  void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiNull *self,
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

//  void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull12debugMarkEndEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiNull::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(cb, ps);
}

//  void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull8dispatchEP17QRhiCommandBufferiii(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    int x,
    int y,
    int z) {
  self->dispatch(cb, x, y, z);
}

//  const QRhiNativeHandles *QRhiNull::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN8QRhiNull13nativeHandlesEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  void QRhiNull::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull13beginExternalEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->beginExternal(cb);
}

//  void QRhiNull::endExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull11endExternalEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->endExternal(cb);
}

//  double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN8QRhiNull20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  QList<QSize> QRhiNull::supportedShadingRates(int sampleCount) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK8QRhiNull21supportedShadingRatesEi(
    const QRhiNull *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  int QRhiNull::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QRhiNull13ubufAlignmentEv(const QRhiNull *self) {
  return self->ubufAlignment();
}

//  bool QRhiNull::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull18isYUpInFramebufferEv(const QRhiNull *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiNull::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull10isYUpInNDCEv(const QRhiNull *self) {
  return self->isYUpInNDC();
}

//  bool QRhiNull::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull20isClipDepthZeroToOneEv(const QRhiNull *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK8QRhiNull19clipSpaceCorrMatrixEv(
    const QRhiNull *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format format,
//      QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhiNull *self,
    QRhiTexture::Format format,
    int flags) {
  return self->isTextureFormatSupported(
      format,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhiNull::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiNull *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiNull::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QRhiNull13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiNull *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiNull::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN8QRhiNull13nativeHandlesEv(
    QRhiNull *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiNull::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK8QRhiNull10driverInfoEv(const QRhiNull *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  QRhiStats QRhiNull::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZN8QRhiNull10statisticsEv(QRhiNull *self) {
  return new QRhiStats(self->statistics());
}

//  bool QRhiNull::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QRhiNull35makeThreadLocalNativeContextCurrentEv(
    QRhiNull *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiNull::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiNull *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiNull::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull22releaseCachedResourcesEv(QRhiNull *self) {
  self->releaseCachedResources();
}

//  bool QRhiNull::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRhiNull12isDeviceLostEv(const QRhiNull *self) {
  return self->isDeviceLost();
}

//  QByteArray QRhiNull::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QRhiNull17pipelineCacheDataEv(QRhiNull *self) {
  return new QByteArray(self->pipelineCacheData());
}

//  void QRhiNull::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull20setPipelineCacheDataERK10QByteArray(
    QRhiNull *self,
    const QByteArray *data) {
  self->setPipelineCacheData(*data);
}

//  void QRhiNull::simulateTextureUpload(const
//      QRhiResourceUpdateBatchPrivate::TextureOp &u)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull21simulateTextureUploadERKN30QRhiResourceUpdateBatchPrivate9TextureOpE(
    QRhiNull *self,
    const QRhiResourceUpdateBatchPrivate::TextureOp *u) {
  self->simulateTextureUpload(*u);
}

//  void QRhiNull::simulateTextureCopy(const
//      QRhiResourceUpdateBatchPrivate::TextureOp &u)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull19simulateTextureCopyERKN30QRhiResourceUpdateBatchPrivate9TextureOpE(
    QRhiNull *self,
    const QRhiResourceUpdateBatchPrivate::TextureOp *u) {
  self->simulateTextureCopy(*u);
}

//  void QRhiNull::simulateTextureGenMips(const
//      QRhiResourceUpdateBatchPrivate::TextureOp &u)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRhiNull22simulateTextureGenMipsERKN30QRhiResourceUpdateBatchPrivate9TextureOpE(
    QRhiNull *self,
    const QRhiResourceUpdateBatchPrivate::TextureOp *u) {
  self->simulateTextureGenMips(*u);
}

//  a Python function taken by a CuteQRhiNull, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiNull(QRhiNull *self, const char *key, void *call) {
  return static_cast<CuteQRhiNull *>(self)->take(key, call);
}

//  bool QRhiNull::create(QRhi::Flags flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QRhiNull6createE6QFlagsIN4QRhi4FlagEE(
    QRhiNull *self,
    int flags) {
  return self->QRhiNull::create(QFlags<QRhi::Flag>::fromInt(flags));
}

//  void QRhiNull::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull7destroyEv(QRhiNull *self) {
  self->QRhiNull::destroy();
}

//  QRhiShadingRateMap *QRhiNull::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_own_ZN8QRhiNull20createShadingRateMapEv(
    QRhiNull *self) {
  return self->QRhiNull::createShadingRateMap();
}

//  QRhi::FrameOpResult QRhiNull::beginFrame(QRhiSwapChain *swapChain,
//      QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_own_ZN8QRhiNull10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiNull *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->QRhiNull::beginFrame(
      swapChain,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::endFrame(QRhiSwapChain *swapChain,
//      QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_own_ZN8QRhiNull8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiNull *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->QRhiNull::endFrame(
      swapChain,
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::endOffscreenFrame(QRhi::EndFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_own_ZN8QRhiNull17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiNull *self,
    int flags) {
  return self->QRhiNull::endOffscreenFrame(
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiNull::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_own_ZN8QRhiNull6finishEv(QRhiNull *self) {
  return self->QRhiNull::finish();
}

//  void QRhiNull::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QColor *colorClearValue,
    const QRhiDepthStencilClearValue *depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->QRhiNull::beginPass(
      cb,
      rt,
      *colorClearValue,
      *depthStencilClearValue,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiNull::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QRhiNull::endPass(cb, resourceUpdates);
}

//  void QRhiNull::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->QRhiNull::setGraphicsPipeline(cb, ps);
}

//  void QRhiNull::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull11setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->QRhiNull::setViewport(cb, *viewport);
}

//  void QRhiNull::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull10setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->QRhiNull::setScissor(cb, *scissor);
}

//  void QRhiNull::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull17setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->QRhiNull::setBlendConstants(cb, *c);
}

//  void QRhiNull::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull13setStencilRefEP17QRhiCommandBufferj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->QRhiNull::setStencilRef(cb, refValue);
}

//  void QRhiNull::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->QRhiNull::setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiNull::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull4drawEP17QRhiCommandBufferjjjj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->QRhiNull::draw(
      cb,
      vertexCount,
      instanceCount,
      firstVertex,
      firstInstance);
}

//  void QRhiNull::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull11drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->QRhiNull::drawIndexed(
      cb,
      indexCount,
      instanceCount,
      firstIndex,
      vertexOffset,
      firstInstance);
}

//  void QRhiNull::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->QRhiNull::drawIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiNull::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->QRhiNull::drawIndexedIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiNull::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->QRhiNull::debugMarkBegin(cb, *name);
}

//  void QRhiNull::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull12debugMarkEndEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->QRhiNull::debugMarkEnd(cb);
}

//  void QRhiNull::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->QRhiNull::debugMarkMsg(cb, *msg);
}

//  void QRhiNull::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->QRhiNull::beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiNull::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->QRhiNull::endComputePass(cb, resourceUpdates);
}

//  void QRhiNull::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->QRhiNull::setComputePipeline(cb, ps);
}

//  void QRhiNull::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull8dispatchEP17QRhiCommandBufferiii(
    QRhiNull *self,
    QRhiCommandBuffer *cb,
    int x,
    int y,
    int z) {
  self->QRhiNull::dispatch(cb, x, y, z);
}

//  const QRhiNativeHandles *QRhiNull::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN8QRhiNull13nativeHandlesEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiNull::nativeHandles(cb);
}

//  void QRhiNull::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull13beginExternalEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->QRhiNull::beginExternal(cb);
}

//  void QRhiNull::endExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull11endExternalEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  self->QRhiNull::endExternal(cb);
}

//  double QRhiNull::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_own_ZN8QRhiNull20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiNull *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiNull::lastCompletedGpuTime(cb);
}

//  int QRhiNull::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QRhiNull13ubufAlignmentEv(const QRhiNull *self) {
  return self->QRhiNull::ubufAlignment();
}

//  bool QRhiNull::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull18isYUpInFramebufferEv(const QRhiNull *self) {
  return self->QRhiNull::isYUpInFramebuffer();
}

//  bool QRhiNull::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull10isYUpInNDCEv(const QRhiNull *self) {
  return self->QRhiNull::isYUpInNDC();
}

//  bool QRhiNull::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull20isClipDepthZeroToOneEv(const QRhiNull *self) {
  return self->QRhiNull::isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiNull::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK8QRhiNull19clipSpaceCorrMatrixEv(
    const QRhiNull *self) {
  return new QMatrix4x4(self->QRhiNull::clipSpaceCorrMatrix());
}

//  bool QRhiNull::isTextureFormatSupported(QRhiTexture::Format format,
//      QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhiNull *self,
    QRhiTexture::Format format,
    int flags) {
  return self->QRhiNull::isTextureFormatSupported(
      format,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhiNull::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiNull *self,
    QRhi::Feature feature) {
  return self->QRhiNull::isFeatureSupported(feature);
}

//  int QRhiNull::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK8QRhiNull13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiNull *self,
    QRhi::ResourceLimit limit) {
  return self->QRhiNull::resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiNull::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN8QRhiNull13nativeHandlesEv(
    QRhiNull *self) {
  return self->QRhiNull::nativeHandles();
}

//  QRhiDriverInfo QRhiNull::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_own_ZNK8QRhiNull10driverInfoEv(const QRhiNull *self) {
  return new QRhiDriverInfo(self->QRhiNull::driverInfo());
}

//  QRhiStats QRhiNull::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_own_ZN8QRhiNull10statisticsEv(QRhiNull *self) {
  return new QRhiStats(self->QRhiNull::statistics());
}

//  bool QRhiNull::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8QRhiNull35makeThreadLocalNativeContextCurrentEv(
    QRhiNull *self) {
  return self->QRhiNull::makeThreadLocalNativeContextCurrent();
}

//  void QRhiNull::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiNull *self,
    QRhiNativeHandles *params) {
  self->QRhiNull::setQueueSubmitParams(params);
}

//  void QRhiNull::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull22releaseCachedResourcesEv(QRhiNull *self) {
  self->QRhiNull::releaseCachedResources();
}

//  bool QRhiNull::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QRhiNull12isDeviceLostEv(const QRhiNull *self) {
  return self->QRhiNull::isDeviceLost();
}

//  QByteArray QRhiNull::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZN8QRhiNull17pipelineCacheDataEv(QRhiNull *self) {
  return new QByteArray(self->QRhiNull::pipelineCacheData());
}

//  void QRhiNull::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8QRhiNull20setPipelineCacheDataERK10QByteArray(
    QRhiNull *self,
    const QByteArray *data) {
  self->QRhiNull::setPipelineCacheData(*data);
}
