//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhi_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
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
#if QT_CONFIG(vulkan)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#include <QtGui/private/qrhid3d12_p.h>
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
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

//  from src/gui/rhi/qrhivulkan.cpp, line 434, as _ZN10QRhiVulkanC1EP20QRhiVulkanInitParamsP23QRhiVulkanNativeHandles
inline QRhiVulkan::QRhiVulkan(QRhiVulkanInitParams *params, QRhiVulkanNativeHandles *importParams)
    : ofr(this)
{
    inst = params->inst;
    if (!inst) {
        // This builds on the fact that Qt Quick also uses QVulkanDefaultInstance. While
        // this way we can support a null inst, it has consequences, so only do it with a
        // warning. (e.g. if Qt Quick initializes afterwards, its attempt to set flags on
        // QVulkanDefaultInstance will be futile)
        qWarning("QRhi for Vulkan attempted to be initialized without a QVulkanInstance; using QVulkanDefaultInstance.");
        inst = QVulkanDefaultInstance::instance();
    }

    maybeWindow = params->window; // may be null
    requestedDeviceExtensions = params->deviceExtensions;

    if (importParams) {
        physDev = importParams->physDev;
        dev = importParams->dev;
        if (dev && physDev) {
            importedDevice = true;
            gfxQueueFamilyIdx = importParams->gfxQueueFamilyIdx;
            gfxQueueIdx = importParams->gfxQueueIdx;
            // gfxQueue is output only, no point in accepting it as input
            if (importParams->vmemAllocator) {
                importedAllocator = true;
                allocator = importParams->vmemAllocator;
            }
        }
    }
}

//  from src/gui/rhi/qrhinull.cpp, line 45, as _ZN8QRhiNullC1EP18QRhiNullInitParams
inline QRhiNull::QRhiNull(QRhiNullInitParams *params)
    : offscreenCommandBuffer(this)
{
    Q_UNUSED(params);
}

//  from src/gui/rhi/qrhigles2.cpp, line 656, as _ZN9QRhiGles2C1EP19QRhiGles2InitParamsP22QRhiGles2NativeHandles
inline QRhiGles2::QRhiGles2(QRhiGles2InitParams *params, QRhiGles2NativeHandles *importDevice)
    : ofr(this)
{
    requestedFormat = params->format;
    fallbackSurface = params->fallbackSurface;
    maybeWindow = params->window; // may be null
    maybeShareContext = params->shareContext; // may be null

    importedContext = importDevice != nullptr;
    if (importedContext) {
        ctx = importDevice->context;
        if (!ctx) {
            qWarning("No OpenGL context given, cannot import");
            importedContext = false;
        }
    }
}

//  from src/gui/rhi/qrhi.cpp, line 9169, as _ZN18QRhiImplementation16prepareForCreateEP4QRhiNS0_14ImplementationE6QFlagsINS0_4FlagEEP11QRhiAdapter
inline void QRhiImplementation::prepareForCreate(QRhi *rhi, QRhi::Implementation impl, QRhi::Flags flags, QRhiAdapter *adapter)
{
    q = rhi;

    debugMarkers = flags.testFlag(QRhi::EnableDebugMarkers);

    implType = impl;
    implThread = QThread::currentThread();

    requestedRhiAdapter = adapter;
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

//  from src/gui/rhi/qrhi.cpp, line 8894, as _ZNK18QRhiImplementation25isStencilSupportingFormatEN11QRhiTexture6FormatE
inline bool QRhiImplementation::isStencilSupportingFormat(QRhiTexture::Format format) const
{
    switch (format) {
    case QRhiTexture::D24S8:
    case QRhiTexture::D32FS8:
        return true;
    default:
        break;
    }
    return false;
}

//  from src/gui/rhi/qrhi.cpp, line 8906, as _ZN18QRhiImplementation27sanityCheckGraphicsPipelineEP20QRhiGraphicsPipeline
inline bool QRhiImplementation::sanityCheckGraphicsPipeline(QRhiGraphicsPipeline *ps)
{
    if (ps->cbeginShaderStages() == ps->cendShaderStages()) {
        qWarning("Cannot build a graphics pipeline without any stages");
        return false;
    }

    bool hasVertexStage = false;
    for (auto it = ps->cbeginShaderStages(), itEnd = ps->cendShaderStages(); it != itEnd; ++it) {
        if (!it->shader().isValid()) {
            qWarning("Empty shader passed to graphics pipeline");
            return false;
        }
        if (it->type() == QRhiShaderStage::Vertex)
            hasVertexStage = true;
    }
    if (!hasVertexStage) {
        qWarning("Cannot build a graphics pipeline without a vertex stage");
        return false;
    }

    if (!ps->renderPassDescriptor()) {
        qWarning("Cannot build a graphics pipeline without a QRhiRenderPassDescriptor");
        return false;
    }

    if (!ps->shaderResourceBindings()) {
        qWarning("Cannot build a graphics pipeline without QRhiShaderResourceBindings");
        return false;
    }

    return true;
}

//  from src/gui/rhi/qrhi.cpp, line 8940, as _ZN18QRhiImplementation33sanityCheckShaderResourceBindingsEP26QRhiShaderResourceBindings
inline bool QRhiImplementation::sanityCheckShaderResourceBindings(QRhiShaderResourceBindings *srb)
{
#ifndef QT_NO_DEBUG
    bool bindingsOk = true;
    const int CHECKED_BINDINGS_COUNT = 64;
    bool bindingSeen[CHECKED_BINDINGS_COUNT] = {};
    for (auto it = srb->cbeginBindings(), end = srb->cendBindings(); it != end; ++it) {
        const int binding = shaderResourceBindingData(*it)->binding;
        if (binding >= CHECKED_BINDINGS_COUNT)
            continue;
        if (binding < 0) {
            qWarning("Invalid binding number %d", binding);
            bindingsOk = false;
            continue;
        }
        switch (shaderResourceBindingData(*it)->type) {
        case QRhiShaderResourceBinding::UniformBuffer:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Uniform buffer duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::SampledTexture:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Combined image sampler duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::Texture:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Texture duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::Sampler:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Sampler duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::ImageLoad:
        case QRhiShaderResourceBinding::ImageStore:
        case QRhiShaderResourceBinding::ImageLoadStore:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Image duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        case QRhiShaderResourceBinding::BufferLoad:
        case QRhiShaderResourceBinding::BufferStore:
        case QRhiShaderResourceBinding::BufferLoadStore:
            if (!bindingSeen[binding]) {
                bindingSeen[binding] = true;
            } else {
                qWarning("Buffer duplicates an existing binding number %d", binding);
                bindingsOk = false;
            }
            break;
        default:
            qWarning("Unknown binding type %d", int(shaderResourceBindingData(*it)->type));
            bindingsOk = false;
            break;
        }
    }

    if (!bindingsOk) {
        qWarning() << *srb;
        return false;
    }
#else
    Q_UNUSED(srb);
#endif
    return true;
}

//  from src/gui/rhi/qrhi.cpp, line 5819, as _ZN18QRhiImplementation16updateLayoutDescEP26QRhiShaderResourceBindings
inline void QRhiImplementation::updateLayoutDesc(QRhiShaderResourceBindings *srb)
{
    srb->m_layoutDescHash = 0;
    srb->m_layoutDesc.clear();
    auto layoutDescAppender = std::back_inserter(srb->m_layoutDesc);
    for (const QRhiShaderResourceBinding &b : std::as_const(srb->m_bindings)) {
        const QRhiShaderResourceBinding::Data *d = &b.d;
        srb->m_layoutDescHash ^= uint(d->binding) ^ uint(d->stage) ^ uint(d->type)
            ^ uint(d->arraySize());
        layoutDescAppender = d->serialize(layoutDescAppender);
    }
}

//  from src/gui/rhi/qrhi.cpp, line 1966, as _ZNK18QRhiImplementation43shaderDescVariableFormatToVertexInputFormatEN18QShaderDescription12VariableTypeE
inline QRhiVertexInputAttribute::Format QRhiImplementation::shaderDescVariableFormatToVertexInputFormat(QShaderDescription::VariableType type) const
{
    switch (type) {
    case QShaderDescription::Vec4:
        return QRhiVertexInputAttribute::Float4;
    case QShaderDescription::Vec3:
        return QRhiVertexInputAttribute::Float3;
    case QShaderDescription::Vec2:
        return QRhiVertexInputAttribute::Float2;
    case QShaderDescription::Float:
        return QRhiVertexInputAttribute::Float;

    case QShaderDescription::Int4:
        return QRhiVertexInputAttribute::SInt4;
    case QShaderDescription::Int3:
        return QRhiVertexInputAttribute::SInt3;
    case QShaderDescription::Int2:
        return QRhiVertexInputAttribute::SInt2;
    case QShaderDescription::Int:
        return QRhiVertexInputAttribute::SInt;

    case QShaderDescription::Uint4:
        return QRhiVertexInputAttribute::UInt4;
    case QShaderDescription::Uint3:
        return QRhiVertexInputAttribute::UInt3;
    case QShaderDescription::Uint2:
        return QRhiVertexInputAttribute::UInt2;
    case QShaderDescription::Uint:
        return QRhiVertexInputAttribute::UInt;

    case QShaderDescription::Half4:
        return QRhiVertexInputAttribute::Half4;
    case QShaderDescription::Half3:
        return QRhiVertexInputAttribute::Half3;
    case QShaderDescription::Half2:
        return QRhiVertexInputAttribute::Half2;
    case QShaderDescription::Half:
        return QRhiVertexInputAttribute::Half;

    default:
        Q_UNREACHABLE_RETURN(QRhiVertexInputAttribute::Float);
    }
}

//  from src/gui/rhi/qrhi.cpp, line 2010, as _ZNK18QRhiImplementation37byteSizePerVertexForVertexInputFormatEN24QRhiVertexInputAttribute6FormatE
inline quint32 QRhiImplementation::byteSizePerVertexForVertexInputFormat(QRhiVertexInputAttribute::Format format) const
{
    switch (format) {
    case QRhiVertexInputAttribute::Float4:
        return 4 * sizeof(float);
    case QRhiVertexInputAttribute::Float3:
        return 4 * sizeof(float); // vec3 still takes 16 bytes
    case QRhiVertexInputAttribute::Float2:
        return 2 * sizeof(float);
    case QRhiVertexInputAttribute::Float:
        return sizeof(float);

    case QRhiVertexInputAttribute::UNormByte4:
        return 4 * sizeof(quint8);
    case QRhiVertexInputAttribute::UNormByte2:
        return 2 * sizeof(quint8);
    case QRhiVertexInputAttribute::UNormByte:
        return sizeof(quint8);

    case QRhiVertexInputAttribute::UInt4:
        return 4 * sizeof(quint32);
    case QRhiVertexInputAttribute::UInt3:
        return 4 * sizeof(quint32); // ivec3 still takes 16 bytes
    case QRhiVertexInputAttribute::UInt2:
        return 2 * sizeof(quint32);
    case QRhiVertexInputAttribute::UInt:
        return sizeof(quint32);

    case QRhiVertexInputAttribute::SInt4:
        return 4 * sizeof(qint32);
    case QRhiVertexInputAttribute::SInt3:
        return 4 * sizeof(qint32); // uvec3 still takes 16 bytes
    case QRhiVertexInputAttribute::SInt2:
        return 2 * sizeof(qint32);
    case QRhiVertexInputAttribute::SInt:
        return sizeof(qint32);

    case QRhiVertexInputAttribute::Half4:
        return 4 * sizeof(qfloat16);
    case QRhiVertexInputAttribute::Half3:
        return 4 * sizeof(qfloat16); // half3 still takes 8 bytes
    case QRhiVertexInputAttribute::Half2:
        return 2 * sizeof(qfloat16);
    case QRhiVertexInputAttribute::Half:
        return sizeof(qfloat16);

    case QRhiVertexInputAttribute::UShort4:
        return 4 * sizeof(quint16);
    case QRhiVertexInputAttribute::UShort3:
        return 4 * sizeof(quint16); // ivec3 still takes 8 bytes
    case QRhiVertexInputAttribute::UShort2:
        return 2 * sizeof(quint16);
    case QRhiVertexInputAttribute::UShort:
        return sizeof(quint16);

    case QRhiVertexInputAttribute::SShort4:
        return 4 * sizeof(qint16);
    case QRhiVertexInputAttribute::SShort3:
        return 4 * sizeof(qint16); // uvec3 still takes 8 bytes
    case QRhiVertexInputAttribute::SShort2:
        return 2 * sizeof(qint16);
    case QRhiVertexInputAttribute::SShort:
        return sizeof(qint16);

    default:
        Q_UNREACHABLE_RETURN(1);
    }
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

//  from src/gui/rhi/qrhi.cpp, line 9673, as _ZN18QRhiImplementation10runCleanupEv
inline void QRhiImplementation::runCleanup()
{
    for (const QRhi::CleanupCallback &f : std::as_const(cleanupCallbacks))
        f(q);

    cleanupCallbacks.clear();

    for (auto it = keyedCleanupCallbacks.cbegin(), end = keyedCleanupCallbacks.cend(); it != end; ++it)
        it.value()(q);

    keyedCleanupCallbacks.clear();
}
//  -----------------------------------------------------------------------

//  A QRhiImplementation that Python can take functions over in. Every QRhiImplementation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRhiImplementationCall0)(const void *, int, int *);
typedef void (*CuteQRhiImplementationCall1)(const void *, int *);
typedef void * (*CuteQRhiImplementationCall2)(const void *, int *);
typedef void * (*CuteQRhiImplementationCall3)(const void *, int *);
typedef void * (*CuteQRhiImplementationCall4)(const void *, int *);
typedef void * (*CuteQRhiImplementationCall5)(const void *, int, int, quint32, int *);
typedef void * (*CuteQRhiImplementationCall6)(const void *, int, const QSize *, int, int, int, int *);
typedef void * (*CuteQRhiImplementationCall7)(const void *, int, const QSize *, int, int, int, int, int *);
typedef void * (*CuteQRhiImplementationCall8)(const void *, int, int, int, int, int, int, int *);
typedef void * (*CuteQRhiImplementationCall9)(const void *, const QRhiTextureRenderTargetDescription *, int, int *);
typedef void * (*CuteQRhiImplementationCall10)(const void *, int *);
typedef void * (*CuteQRhiImplementationCall11)(const void *, int *);
typedef int (*CuteQRhiImplementationCall12)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiImplementationCall13)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiImplementationCall14)(const void *, int, int *);
typedef int (*CuteQRhiImplementationCall15)(const void *, int *);
typedef void (*CuteQRhiImplementationCall16)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiImplementationCall17)(const void *, QRhiCommandBuffer *, QRhiRenderTarget *, const QColor *, const QRhiDepthStencilClearValue *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiImplementationCall18)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiImplementationCall19)(const void *, QRhiCommandBuffer *, QRhiGraphicsPipeline *, int *);
typedef void (*CuteQRhiImplementationCall20)(const void *, QRhiCommandBuffer *, const QRhiViewport *, int *);
typedef void (*CuteQRhiImplementationCall21)(const void *, QRhiCommandBuffer *, const QRhiScissor *, int *);
typedef void (*CuteQRhiImplementationCall22)(const void *, QRhiCommandBuffer *, const QColor *, int *);
typedef void (*CuteQRhiImplementationCall23)(const void *, QRhiCommandBuffer *, quint32, int *);
typedef void (*CuteQRhiImplementationCall24)(const void *, QRhiCommandBuffer *, const QSize *, int *);
typedef void (*CuteQRhiImplementationCall25)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiImplementationCall26)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, qint32, quint32, int *);
typedef void (*CuteQRhiImplementationCall27)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiImplementationCall28)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiImplementationCall29)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiImplementationCall30)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiImplementationCall31)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiImplementationCall32)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiImplementationCall33)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiImplementationCall34)(const void *, QRhiCommandBuffer *, QRhiComputePipeline *, int *);
typedef void (*CuteQRhiImplementationCall35)(const void *, QRhiCommandBuffer *, int, int, int, int *);
typedef void * (*CuteQRhiImplementationCall36)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiImplementationCall37)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiImplementationCall38)(const void *, QRhiCommandBuffer *, int *);
typedef double (*CuteQRhiImplementationCall39)(const void *, QRhiCommandBuffer *, int *);
typedef int (*CuteQRhiImplementationCall40)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall41)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall42)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall43)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQRhiImplementationCall44)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall45)(const void *, int, int, int *);
typedef bool (*CuteQRhiImplementationCall46)(const void *, int, int *);
typedef int (*CuteQRhiImplementationCall47)(const void *, int, int *);
typedef void * (*CuteQRhiImplementationCall48)(const void *, int *);
typedef const QRhiDriverInfo * (*CuteQRhiImplementationCall49)(const void *, int *);
typedef const QRhiStats * (*CuteQRhiImplementationCall50)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall51)(const void *, int *);
typedef void (*CuteQRhiImplementationCall52)(const void *, QRhiNativeHandles *, int *);
typedef void (*CuteQRhiImplementationCall53)(const void *, int *);
typedef bool (*CuteQRhiImplementationCall54)(const void *, int *);
typedef const QByteArray * (*CuteQRhiImplementationCall55)(const void *, int *);
typedef void (*CuteQRhiImplementationCall56)(const void *, const QByteArray *, int *);
class CuteQRhiImplementation : public QRhiImplementation {
public:
  using QRhiImplementation::QRhiImplementation;
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

  //  bool QRhiImplementation::create(QRhi::Flags flags)
  bool create(QRhi::Flags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiImplementationCall0 call = reinterpret_cast<CuteQRhiImplementationCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiImplementation::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiImplementationCall1 call = reinterpret_cast<CuteQRhiImplementationCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QRhiGraphicsPipeline *QRhiImplementation::createGraphicsPipeline()
  QRhiGraphicsPipeline *createGraphicsPipeline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiImplementationCall2 call = reinterpret_cast<CuteQRhiImplementationCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiGraphicsPipeline *>(given);
    }
    return {};
  }

  //  QRhiComputePipeline *QRhiImplementation::createComputePipeline()
  QRhiComputePipeline *createComputePipeline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiImplementationCall3 call = reinterpret_cast<CuteQRhiImplementationCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiComputePipeline *>(given);
    }
    return {};
  }

  //  QRhiShaderResourceBindings
  //      *QRhiImplementation::createShaderResourceBindings()
  QRhiShaderResourceBindings *createShaderResourceBindings() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiImplementationCall4 call = reinterpret_cast<CuteQRhiImplementationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShaderResourceBindings *>(given);
    }
    return {};
  }

  //  QRhiBuffer *QRhiImplementation::createBuffer(QRhiBuffer::Type type,
  //      QRhiBuffer::UsageFlags usage, quint32 size)
  QRhiBuffer *createBuffer(
      QRhiBuffer::Type type,
      QRhiBuffer::UsageFlags usage,
      quint32 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiImplementationCall5 call = reinterpret_cast<CuteQRhiImplementationCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), static_cast<int>(usage.toInt()), size, &handled);
      if (handled) return static_cast<QRhiBuffer *>(given);
    }
    return {};
  }

  //  QRhiRenderBuffer
  //      *QRhiImplementation::createRenderBuffer(QRhiRenderBuffer::Type
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
      CuteQRhiImplementationCall6 call = reinterpret_cast<CuteQRhiImplementationCall6>(taken[6]);
      void * given = call(this, static_cast<int>(type), &pixelSize, sampleCount, static_cast<int>(flags.toInt()), static_cast<int>(backingFormatHint), &handled);
      if (handled) return static_cast<QRhiRenderBuffer *>(given);
    }
    return {};
  }

  //  QRhiTexture *QRhiImplementation::createTexture(QRhiTexture::Format
  //      format, const QSize &pixelSize, int depth, int arraySize, int
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
      CuteQRhiImplementationCall7 call = reinterpret_cast<CuteQRhiImplementationCall7>(taken[7]);
      void * given = call(this, static_cast<int>(format), &pixelSize, depth, arraySize, sampleCount, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return {};
  }

  //  QRhiSampler *QRhiImplementation::createSampler(QRhiSampler::Filter
  //      magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter
  //      mipmapMode, QRhiSampler::AddressMode u, QRhiSampler::AddressMode
  //      v, QRhiSampler::AddressMode w)
  QRhiSampler *createSampler(
      QRhiSampler::Filter magFilter,
      QRhiSampler::Filter minFilter,
      QRhiSampler::Filter mipmapMode,
      QRhiSampler::AddressMode u,
      QRhiSampler::AddressMode v,
      QRhiSampler::AddressMode w) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiImplementationCall8 call = reinterpret_cast<CuteQRhiImplementationCall8>(taken[8]);
      void * given = call(this, static_cast<int>(magFilter), static_cast<int>(minFilter), static_cast<int>(mipmapMode), static_cast<int>(u), static_cast<int>(v), static_cast<int>(w), &handled);
      if (handled) return static_cast<QRhiSampler *>(given);
    }
    return {};
  }

  //  QRhiTextureRenderTarget
  //      *QRhiImplementation::createTextureRenderTarget(const
  //      QRhiTextureRenderTargetDescription &desc,
  //      QRhiTextureRenderTarget::Flags flags)
  QRhiTextureRenderTarget *createTextureRenderTarget(
      const QRhiTextureRenderTargetDescription &desc,
      QRhiTextureRenderTarget::Flags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiImplementationCall9 call = reinterpret_cast<CuteQRhiImplementationCall9>(taken[9]);
      void * given = call(this, &desc, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTextureRenderTarget *>(given);
    }
    return {};
  }

  //  QRhiShadingRateMap *QRhiImplementation::createShadingRateMap()
  QRhiShadingRateMap *createShadingRateMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiImplementationCall10 call = reinterpret_cast<CuteQRhiImplementationCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShadingRateMap *>(given);
    }
    return {};
  }

  //  QRhiSwapChain *QRhiImplementation::createSwapChain()
  QRhiSwapChain *createSwapChain() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiImplementationCall11 call = reinterpret_cast<CuteQRhiImplementationCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiSwapChain *>(given);
    }
    return {};
  }

  //  QRhi::FrameOpResult QRhiImplementation::beginFrame(QRhiSwapChain
  //      *swapChain, QRhi::BeginFrameFlags flags)
  QRhi::FrameOpResult beginFrame(
      QRhiSwapChain *swapChain,
      QRhi::BeginFrameFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiImplementationCall12 call = reinterpret_cast<CuteQRhiImplementationCall12>(taken[12]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return {};
  }

  //  QRhi::FrameOpResult QRhiImplementation::endFrame(QRhiSwapChain
  //      *swapChain, QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endFrame(
      QRhiSwapChain *swapChain,
      QRhi::EndFrameFlags flags) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiImplementationCall13 call = reinterpret_cast<CuteQRhiImplementationCall13>(taken[13]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return {};
  }

  //  QRhi::FrameOpResult
  //      QRhiImplementation::endOffscreenFrame(QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endOffscreenFrame(QRhi::EndFrameFlags flags) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiImplementationCall14 call = reinterpret_cast<CuteQRhiImplementationCall14>(taken[14]);
      int given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return {};
  }

  //  QRhi::FrameOpResult QRhiImplementation::finish()
  QRhi::FrameOpResult finish() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiImplementationCall15 call = reinterpret_cast<CuteQRhiImplementationCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return {};
  }

  //  void QRhiImplementation::resourceUpdate(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void resourceUpdate(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiImplementationCall16 call = reinterpret_cast<CuteQRhiImplementationCall16>(taken[16]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::beginPass(QRhiCommandBuffer *cb,
  //      QRhiRenderTarget *rt, const QColor &colorClearValue, const
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
      CuteQRhiImplementationCall17 call = reinterpret_cast<CuteQRhiImplementationCall17>(taken[17]);
      call(this, cb, rt, &colorClearValue, &depthStencilClearValue, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::endPass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endPass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiImplementationCall18 call = reinterpret_cast<CuteQRhiImplementationCall18>(taken[18]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setGraphicsPipeline(QRhiCommandBuffer *cb,
  //      QRhiGraphicsPipeline *ps)
  void setGraphicsPipeline(
      QRhiCommandBuffer *cb,
      QRhiGraphicsPipeline *ps) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiImplementationCall19 call = reinterpret_cast<CuteQRhiImplementationCall19>(taken[19]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setViewport(QRhiCommandBuffer *cb, const
  //      QRhiViewport &viewport)
  void setViewport(
      QRhiCommandBuffer *cb,
      const QRhiViewport &viewport) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiImplementationCall20 call = reinterpret_cast<CuteQRhiImplementationCall20>(taken[20]);
      call(this, cb, &viewport, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setScissor(QRhiCommandBuffer *cb, const
  //      QRhiScissor &scissor)
  void setScissor(
      QRhiCommandBuffer *cb,
      const QRhiScissor &scissor) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiImplementationCall21 call = reinterpret_cast<CuteQRhiImplementationCall21>(taken[21]);
      call(this, cb, &scissor, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setBlendConstants(QRhiCommandBuffer *cb,
  //      const QColor &c)
  void setBlendConstants(QRhiCommandBuffer *cb, const QColor &c) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiImplementationCall22 call = reinterpret_cast<CuteQRhiImplementationCall22>(taken[22]);
      call(this, cb, &c, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setStencilRef(QRhiCommandBuffer *cb, quint32
  //      refValue)
  void setStencilRef(QRhiCommandBuffer *cb, quint32 refValue) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiImplementationCall23 call = reinterpret_cast<CuteQRhiImplementationCall23>(taken[23]);
      call(this, cb, refValue, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setShadingRate(QRhiCommandBuffer *cb, const
  //      QSize &coarsePixelSize)
  void setShadingRate(
      QRhiCommandBuffer *cb,
      const QSize &coarsePixelSize) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiImplementationCall24 call = reinterpret_cast<CuteQRhiImplementationCall24>(taken[24]);
      call(this, cb, &coarsePixelSize, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::draw(QRhiCommandBuffer *cb, quint32
  //      vertexCount, quint32 instanceCount, quint32 firstVertex, quint32
  //      firstInstance)
  void draw(
      QRhiCommandBuffer *cb,
      quint32 vertexCount,
      quint32 instanceCount,
      quint32 firstVertex,
      quint32 firstInstance) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRhiImplementationCall25 call = reinterpret_cast<CuteQRhiImplementationCall25>(taken[25]);
      call(this, cb, vertexCount, instanceCount, firstVertex, firstInstance, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::drawIndexed(QRhiCommandBuffer *cb, quint32
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
      CuteQRhiImplementationCall26 call = reinterpret_cast<CuteQRhiImplementationCall26>(taken[26]);
      call(this, cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::drawIndirect(QRhiCommandBuffer *cb,
  //      QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount,
  //      quint32 stride)
  void drawIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 offset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRhiImplementationCall27 call = reinterpret_cast<CuteQRhiImplementationCall27>(taken[27]);
      call(this, cb, indirectBuffer, offset, drawCount, stride, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::drawIndexedIndirect(QRhiCommandBuffer *cb,
  //      QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount,
  //      quint32 stride)
  void drawIndexedIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 offset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRhiImplementationCall28 call = reinterpret_cast<CuteQRhiImplementationCall28>(taken[28]);
      call(this, cb, indirectBuffer, offset, drawCount, stride, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::debugMarkBegin(QRhiCommandBuffer *cb, const
  //      QByteArray &name)
  void debugMarkBegin(
      QRhiCommandBuffer *cb,
      const QByteArray &name) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiImplementationCall29 call = reinterpret_cast<CuteQRhiImplementationCall29>(taken[29]);
      call(this, cb, &name, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::debugMarkEnd(QRhiCommandBuffer *cb)
  void debugMarkEnd(QRhiCommandBuffer *cb) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiImplementationCall30 call = reinterpret_cast<CuteQRhiImplementationCall30>(taken[30]);
      call(this, cb, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::debugMarkMsg(QRhiCommandBuffer *cb, const
  //      QByteArray &msg)
  void debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiImplementationCall31 call = reinterpret_cast<CuteQRhiImplementationCall31>(taken[31]);
      call(this, cb, &msg, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::beginComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiImplementationCall32 call = reinterpret_cast<CuteQRhiImplementationCall32>(taken[32]);
      call(this, cb, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::endComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiImplementationCall33 call = reinterpret_cast<CuteQRhiImplementationCall33>(taken[33]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::setComputePipeline(QRhiCommandBuffer *cb,
  //      QRhiComputePipeline *ps)
  void setComputePipeline(
      QRhiCommandBuffer *cb,
      QRhiComputePipeline *ps) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiImplementationCall34 call = reinterpret_cast<CuteQRhiImplementationCall34>(taken[34]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::dispatch(QRhiCommandBuffer *cb, int x, int
  //      y, int z)
  void dispatch(QRhiCommandBuffer *cb, int x, int y, int z) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiImplementationCall35 call = reinterpret_cast<CuteQRhiImplementationCall35>(taken[35]);
      call(this, cb, x, y, z, &handled);
      if (handled) return;
    }
  }

  //  const QRhiNativeHandles
  //      *QRhiImplementation::nativeHandles(QRhiCommandBuffer *cb)
  const QRhiNativeHandles *nativeHandles(QRhiCommandBuffer *cb) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiImplementationCall36 call = reinterpret_cast<CuteQRhiImplementationCall36>(taken[36]);
      void * given = call(this, cb, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return {};
  }

  //  void QRhiImplementation::beginExternal(QRhiCommandBuffer *cb)
  void beginExternal(QRhiCommandBuffer *cb) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiImplementationCall37 call = reinterpret_cast<CuteQRhiImplementationCall37>(taken[37]);
      call(this, cb, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::endExternal(QRhiCommandBuffer *cb)
  void endExternal(QRhiCommandBuffer *cb) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiImplementationCall38 call = reinterpret_cast<CuteQRhiImplementationCall38>(taken[38]);
      call(this, cb, &handled);
      if (handled) return;
    }
  }

  //  double QRhiImplementation::lastCompletedGpuTime(QRhiCommandBuffer
  //      *cb)
  double lastCompletedGpuTime(QRhiCommandBuffer *cb) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiImplementationCall39 call = reinterpret_cast<CuteQRhiImplementationCall39>(taken[39]);
      double given = call(this, cb, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QRhiImplementation::ubufAlignment() const
  int ubufAlignment() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiImplementationCall40 call = reinterpret_cast<CuteQRhiImplementationCall40>(taken[40]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRhiImplementation::isYUpInFramebuffer() const
  bool isYUpInFramebuffer() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiImplementationCall41 call = reinterpret_cast<CuteQRhiImplementationCall41>(taken[41]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRhiImplementation::isYUpInNDC() const
  bool isYUpInNDC() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiImplementationCall42 call = reinterpret_cast<CuteQRhiImplementationCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRhiImplementation::isClipDepthZeroToOne() const
  bool isClipDepthZeroToOne() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRhiImplementationCall43 call = reinterpret_cast<CuteQRhiImplementationCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QMatrix4x4 QRhiImplementation::clipSpaceCorrMatrix() const
  QMatrix4x4 clipSpaceCorrMatrix() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQRhiImplementationCall44 call = reinterpret_cast<CuteQRhiImplementationCall44>(taken[44]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QRhiImplementation::isTextureFormatSupported(QRhiTexture::Format
  //      format, QRhiTexture::Flags flags) const
  bool isTextureFormatSupported(
      QRhiTexture::Format format,
      QRhiTexture::Flags flags) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQRhiImplementationCall45 call = reinterpret_cast<CuteQRhiImplementationCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRhiImplementation::isFeatureSupported(QRhi::Feature feature)
  //      const
  bool isFeatureSupported(QRhi::Feature feature) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQRhiImplementationCall46 call = reinterpret_cast<CuteQRhiImplementationCall46>(taken[46]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QRhiImplementation::resourceLimit(QRhi::ResourceLimit limit)
  //      const
  int resourceLimit(QRhi::ResourceLimit limit) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQRhiImplementationCall47 call = reinterpret_cast<CuteQRhiImplementationCall47>(taken[47]);
      int given = call(this, static_cast<int>(limit), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QRhiNativeHandles *QRhiImplementation::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[48]) {
      int handled = 0;
      CuteQRhiImplementationCall48 call = reinterpret_cast<CuteQRhiImplementationCall48>(taken[48]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return {};
  }

  //  QRhiDriverInfo QRhiImplementation::driverInfo() const
  QRhiDriverInfo driverInfo() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQRhiImplementationCall49 call = reinterpret_cast<CuteQRhiImplementationCall49>(taken[49]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QRhiStats QRhiImplementation::statistics()
  QRhiStats statistics() override {
    if (taken[50]) {
      int handled = 0;
      CuteQRhiImplementationCall50 call = reinterpret_cast<CuteQRhiImplementationCall50>(taken[50]);
      const QRhiStats * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QRhiImplementation::makeThreadLocalNativeContextCurrent()
  bool makeThreadLocalNativeContextCurrent() override {
    if (taken[51]) {
      int handled = 0;
      CuteQRhiImplementationCall51 call = reinterpret_cast<CuteQRhiImplementationCall51>(taken[51]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiImplementation::setQueueSubmitParams(QRhiNativeHandles
  //      *params)
  void setQueueSubmitParams(QRhiNativeHandles *params) override {
    if (taken[52]) {
      int handled = 0;
      CuteQRhiImplementationCall52 call = reinterpret_cast<CuteQRhiImplementationCall52>(taken[52]);
      call(this, params, &handled);
      if (handled) return;
    }
  }

  //  void QRhiImplementation::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[53]) {
      int handled = 0;
      CuteQRhiImplementationCall53 call = reinterpret_cast<CuteQRhiImplementationCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QRhiImplementation::isDeviceLost() const
  bool isDeviceLost() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQRhiImplementationCall54 call = reinterpret_cast<CuteQRhiImplementationCall54>(taken[54]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArray QRhiImplementation::pipelineCacheData()
  QByteArray pipelineCacheData() override {
    if (taken[55]) {
      int handled = 0;
      CuteQRhiImplementationCall55 call = reinterpret_cast<CuteQRhiImplementationCall55>(taken[55]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QRhiImplementation::setPipelineCacheData(const QByteArray &data)
  void setPipelineCacheData(const QByteArray &data) override {
    if (taken[56]) {
      int handled = 0;
      CuteQRhiImplementationCall56 call = reinterpret_cast<CuteQRhiImplementationCall56>(taken[56]);
      call(this, &data, &handled);
      if (handled) return;
    }
  }
};

//  QRhiImplementation::~QRhiImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementationD1Ev(QRhiImplementation *self) {
  delete self;
}

//  bool QRhiImplementation::create(QRhi::Flags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiImplementation6createE6QFlagsIN4QRhi4FlagEE(
    QRhiImplementation *self,
    int flags) {
  return self->create(QFlags<QRhi::Flag>::fromInt(flags));
}

//  void QRhiImplementation::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation7destroyEv(QRhiImplementation *self) {
  self->destroy();
}

//  QRhi::AdapterList
//      QRhiImplementation::enumerateAdaptersBeforeCreate(QRhiNativeHandles
//      *nativeHandles) const
extern "C" Q_DECL_EXPORT
QList<QRhiAdapter *> *ritual_ZNK18QRhiImplementation29enumerateAdaptersBeforeCreateEP17QRhiNativeHandles(
    const QRhiImplementation *self,
    QRhiNativeHandles *nativeHandles) {
  return new QList<QRhiAdapter *>(
      self->enumerateAdaptersBeforeCreate(
          nativeHandles));
}

//  QRhiGraphicsPipeline *QRhiImplementation::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN18QRhiImplementation22createGraphicsPipelineEv(
    QRhiImplementation *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiImplementation::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN18QRhiImplementation21createComputePipelineEv(
    QRhiImplementation *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings
//      *QRhiImplementation::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN18QRhiImplementation28createShaderResourceBindingsEv(
    QRhiImplementation *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiImplementation::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN18QRhiImplementation12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiImplementation *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer
//      *QRhiImplementation::createRenderBuffer(QRhiRenderBuffer::Type type,
//      const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags
//      flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN18QRhiImplementation18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiImplementation *self,
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

//  QRhiTexture *QRhiImplementation::createTexture(QRhiTexture::Format
//      format, const QSize &pixelSize, int depth, int arraySize, int
//      sampleCount, QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN18QRhiImplementation13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiImplementation *self,
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

//  QRhiSampler *QRhiImplementation::createSampler(QRhiSampler::Filter
//      magFilter, QRhiSampler::Filter minFilter, QRhiSampler::Filter
//      mipmapMode, QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN18QRhiImplementation13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiImplementation *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget
//      *QRhiImplementation::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN18QRhiImplementation25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiImplementation *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiImplementation::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN18QRhiImplementation20createShadingRateMapEv(
    QRhiImplementation *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiImplementation::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN18QRhiImplementation15createSwapChainEv(
    QRhiImplementation *self) {
  return self->createSwapChain();
}

//  QRhi::FrameOpResult QRhiImplementation::beginFrame(QRhiSwapChain
//      *swapChain, QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN18QRhiImplementation10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiImplementation *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->beginFrame(
      swapChain,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiImplementation::endFrame(QRhiSwapChain
//      *swapChain, QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN18QRhiImplementation8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiImplementation *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->endFrame(
      swapChain,
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult
//      QRhiImplementation::endOffscreenFrame(QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN18QRhiImplementation17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiImplementation *self,
    int flags) {
  return self->endOffscreenFrame(QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiImplementation::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN18QRhiImplementation6finishEv(
    QRhiImplementation *self) {
  return self->finish();
}

//  void QRhiImplementation::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiImplementation::beginPass(QRhiCommandBuffer *cb,
//      QRhiRenderTarget *rt, const QColor &colorClearValue, const
//      QRhiDepthStencilClearValue &depthStencilClearValue,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiImplementation *self,
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

//  void QRhiImplementation::endPass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiImplementation::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(cb, ps);
}

//  void QRhiImplementation::setViewport(QRhiCommandBuffer *cb, const
//      QRhiViewport &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation11setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->setViewport(cb, *viewport);
}

//  void QRhiImplementation::setScissor(QRhiCommandBuffer *cb, const
//      QRhiScissor &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation10setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->setScissor(cb, *scissor);
}

//  void QRhiImplementation::setBlendConstants(QRhiCommandBuffer *cb, const
//      QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation17setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->setBlendConstants(cb, *c);
}

//  void QRhiImplementation::setStencilRef(QRhiCommandBuffer *cb, quint32
//      refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation13setStencilRefEP17QRhiCommandBufferj(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->setStencilRef(cb, refValue);
}

//  void QRhiImplementation::setShadingRate(QRhiCommandBuffer *cb, const
//      QSize &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiImplementation::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
//      quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation4drawEP17QRhiCommandBufferjjjj(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiImplementation::drawIndexed(QRhiCommandBuffer *cb, quint32
//      indexCount, quint32 instanceCount, quint32 firstIndex, qint32
//      vertexOffset, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation11drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiImplementation *self,
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

//  void QRhiImplementation::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 offset, quint32 drawCount, quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 offset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndirect(cb, indirectBuffer, offset, drawCount, stride);
}

//  void QRhiImplementation::drawIndexedIndirect(QRhiCommandBuffer *cb,
//      QRhiBuffer *indirectBuffer, quint32 offset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 offset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndexedIndirect(cb, indirectBuffer, offset, drawCount, stride);
}

//  void QRhiImplementation::debugMarkBegin(QRhiCommandBuffer *cb, const
//      QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiImplementation::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation12debugMarkEndEP17QRhiCommandBuffer(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiImplementation::debugMarkMsg(QRhiCommandBuffer *cb, const
//      QByteArray &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiImplementation::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiImplementation::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  void QRhiImplementation::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(cb, ps);
}

//  void QRhiImplementation::dispatch(QRhiCommandBuffer *cb, int x, int y,
//      int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation8dispatchEP17QRhiCommandBufferiii(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb,
    int x,
    int y,
    int z) {
  self->dispatch(cb, x, y, z);
}

//  const QRhiNativeHandles
//      *QRhiImplementation::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN18QRhiImplementation13nativeHandlesEP17QRhiCommandBuffer(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  void QRhiImplementation::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation13beginExternalEP17QRhiCommandBuffer(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb) {
  self->beginExternal(cb);
}

//  void QRhiImplementation::endExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation11endExternalEP17QRhiCommandBuffer(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb) {
  self->endExternal(cb);
}

//  double QRhiImplementation::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN18QRhiImplementation20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiImplementation *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  int QRhiImplementation::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QRhiImplementation13ubufAlignmentEv(
    const QRhiImplementation *self) {
  return self->ubufAlignment();
}

//  QList<QSize> QRhiImplementation::supportedShadingRates(int sampleCount)
//      const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK18QRhiImplementation21supportedShadingRatesEi(
    const QRhiImplementation *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  bool QRhiImplementation::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation18isYUpInFramebufferEv(
    const QRhiImplementation *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiImplementation::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation10isYUpInNDCEv(
    const QRhiImplementation *self) {
  return self->isYUpInNDC();
}

//  bool QRhiImplementation::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation20isClipDepthZeroToOneEv(
    const QRhiImplementation *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiImplementation::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK18QRhiImplementation19clipSpaceCorrMatrixEv(
    const QRhiImplementation *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhiImplementation::isTextureFormatSupported(QRhiTexture::Format
//      format, QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhiImplementation *self,
    QRhiTexture::Format format,
    int flags) {
  return self->isTextureFormatSupported(
      format,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhiImplementation::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiImplementation *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiImplementation::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QRhiImplementation13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiImplementation *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiImplementation::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN18QRhiImplementation13nativeHandlesEv(
    QRhiImplementation *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiImplementation::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK18QRhiImplementation10driverInfoEv(
    const QRhiImplementation *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  QRhiStats QRhiImplementation::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZN18QRhiImplementation10statisticsEv(
    QRhiImplementation *self) {
  return new QRhiStats(self->statistics());
}

//  bool QRhiImplementation::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiImplementation35makeThreadLocalNativeContextCurrentEv(
    QRhiImplementation *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiImplementation::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiImplementation *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiImplementation::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation22releaseCachedResourcesEv(
    QRhiImplementation *self) {
  self->releaseCachedResources();
}

//  bool QRhiImplementation::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation12isDeviceLostEv(
    const QRhiImplementation *self) {
  return self->isDeviceLost();
}

//  QByteArray QRhiImplementation::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QRhiImplementation17pipelineCacheDataEv(
    QRhiImplementation *self) {
  return new QByteArray(self->pipelineCacheData());
}

//  void QRhiImplementation::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation20setPipelineCacheDataERK10QByteArray(
    QRhiImplementation *self,
    const QByteArray *data) {
  self->setPipelineCacheData(*data);
}

//  void QRhiImplementation::prepareForCreate(QRhi *rhi, QRhi::Implementation
//      impl, QRhi::Flags flags, QRhiAdapter *adapter)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation16prepareForCreateEP4QRhiNS0_14ImplementationE6QFlagsINS0_4FlagEEP11QRhiAdapter(
    QRhiImplementation *self,
    QRhi *rhi,
    QRhi::Implementation impl,
    int flags,
    QRhiAdapter *adapter) {
  self->prepareForCreate(
      rhi,
      impl,
      QFlags<QRhi::Flag>::fromInt(flags),
      adapter);
}

//  bool QRhiImplementation::isCompressedFormat(QRhiTexture::Format format)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation18isCompressedFormatEN11QRhiTexture6FormatE(
    const QRhiImplementation *self,
    QRhiTexture::Format format) {
  return self->isCompressedFormat(format);
}

//  bool QRhiImplementation::compressedFormatInfo(QRhiTexture::Format format,
//      const QSize &size, quint32 *bpl, quint32 *byteSize, QSize *blockDim)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation20compressedFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_PS2_(
    const QRhiImplementation *self,
    QRhiTexture::Format format,
    const QSize *size,
    quint32 *bpl,
    quint32 *byteSize,
    QSize *blockDim) {
  return self->compressedFormatInfo(format, *size, bpl, byteSize, blockDim);
}

//  bool QRhiImplementation::textureFormatInfo(QRhiTexture::Format format,
//      const QSize &size, quint32 *bpl, quint32 *byteSize, quint32
//      *bytesPerPixel) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation17textureFormatInfoEN11QRhiTexture6FormatERK5QSizePjS5_S5_(
    const QRhiImplementation *self,
    QRhiTexture::Format format,
    const QSize *size,
    quint32 *bpl,
    quint32 *byteSize,
    quint32 *bytesPerPixel) {
  return self->textureFormatInfo(
      format,
      *size,
      bpl,
      byteSize,
      bytesPerPixel);
}

//  bool QRhiImplementation::isStencilSupportingFormat(QRhiTexture::Format
//      format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRhiImplementation25isStencilSupportingFormatEN11QRhiTexture6FormatE(
    const QRhiImplementation *self,
    QRhiTexture::Format format) {
  return self->isStencilSupportingFormat(format);
}

//  void QRhiImplementation::registerResource(QRhiResource *res, bool
//      ownsNativeResources)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation16registerResourceEP12QRhiResourceb(
    QRhiImplementation *self,
    QRhiResource *res,
    bool ownsNativeResources) {
  self->registerResource(res, ownsNativeResources);
}

//  void QRhiImplementation::unregisterResource(QRhiResource *res)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation18unregisterResourceEP12QRhiResource(
    QRhiImplementation *self,
    QRhiResource *res) {
  self->unregisterResource(res);
}

//  void QRhiImplementation::addDeleteLater(QRhiResource *res)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation14addDeleteLaterEP12QRhiResource(
    QRhiImplementation *self,
    QRhiResource *res) {
  self->addDeleteLater(res);
}

//  bool QRhiImplementation::sanityCheckGraphicsPipeline(QRhiGraphicsPipeline
//      *ps)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiImplementation27sanityCheckGraphicsPipelineEP20QRhiGraphicsPipeline(
    QRhiImplementation *self,
    QRhiGraphicsPipeline *ps) {
  return self->sanityCheckGraphicsPipeline(ps);
}

//  bool QRhiImplementation::sanityCheckShaderResourceBindings(QRhiShaderReso
//      urceBindings *srb)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiImplementation33sanityCheckShaderResourceBindingsEP26QRhiShaderResourceBindings(
    QRhiImplementation *self,
    QRhiShaderResourceBindings *srb) {
  return self->sanityCheckShaderResourceBindings(srb);
}

//  void QRhiImplementation::updateLayoutDesc(QRhiShaderResourceBindings
//      *srb)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation16updateLayoutDescEP26QRhiShaderResourceBindings(
    QRhiImplementation *self,
    QRhiShaderResourceBindings *srb) {
  self->updateLayoutDesc(srb);
}

//  quint32 QRhiImplementation::pipelineCacheRhiId() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK18QRhiImplementation18pipelineCacheRhiIdEv(
    const QRhiImplementation *self) {
  return self->pipelineCacheRhiId();
}

//  void QRhiImplementation::pipelineCreationStart()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation21pipelineCreationStartEv(
    QRhiImplementation *self) {
  self->pipelineCreationStart();
}

//  void QRhiImplementation::pipelineCreationEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation19pipelineCreationEndEv(
    QRhiImplementation *self) {
  self->pipelineCreationEnd();
}

//  qint64 QRhiImplementation::totalPipelineCreationTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QRhiImplementation25totalPipelineCreationTimeEv(
    const QRhiImplementation *self) {
  return self->totalPipelineCreationTime();
}

//  QRhiVertexInputAttribute::Format QRhiImplementation::shaderDescVariableFo
//      rmatToVertexInputFormat(QShaderDescription::VariableType type) const
extern "C" Q_DECL_EXPORT
QRhiVertexInputAttribute::Format ritual_ZNK18QRhiImplementation43shaderDescVariableFormatToVertexInputFormatEN18QShaderDescription12VariableTypeE(
    const QRhiImplementation *self,
    QShaderDescription::VariableType type) {
  return self->shaderDescVariableFormatToVertexInputFormat(type);
}

//  quint32 QRhiImplementation::byteSizePerVertexForVertexInputFormat(QRhiVer
//      texInputAttribute::Format format) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK18QRhiImplementation37byteSizePerVertexForVertexInputFormatEN24QRhiVertexInputAttribute6FormatE(
    const QRhiImplementation *self,
    QRhiVertexInputAttribute::Format format) {
  return self->byteSizePerVertexForVertexInputFormat(format);
}

//  const QRhiShaderResourceBinding::Data
//      *QRhiImplementation::shaderResourceBindingData(const
//      QRhiShaderResourceBinding &binding)
extern "C" Q_DECL_EXPORT
const QRhiShaderResourceBinding::Data *ritual_ZN18QRhiImplementation25shaderResourceBindingDataERK25QRhiShaderResourceBinding(
    const QRhiShaderResourceBinding *binding) {
  return QRhiImplementation::shaderResourceBindingData(*binding);
}

//  bool QRhiImplementation::sortedBindingLessThan(const
//      QRhiShaderResourceBinding &a, const QRhiShaderResourceBinding &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRhiImplementation21sortedBindingLessThanERK25QRhiShaderResourceBindingS2_(
    const QRhiShaderResourceBinding *a,
    const QRhiShaderResourceBinding *b) {
  return QRhiImplementation::sortedBindingLessThan(*a, *b);
}

//  QSize QRhiImplementation::clampedSubResourceUploadSize(QSize size, QPoint
//      dstPos, int level, QSize textureSizeAtLevelZero, bool warn)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN18QRhiImplementation28clampedSubResourceUploadSizeE5QSize6QPointiS0_b(
    QRhiImplementation *self,
    const QSize *size,
    const QPoint *dstPos,
    int level,
    const QSize *textureSizeAtLevelZero,
    bool warn) {
  return new QSize(
      self->clampedSubResourceUploadSize(
          *size,
          *dstPos,
          level,
          *textureSizeAtLevelZero,
          warn));
}

//  QSize QRhiImplementation::clampedSubResourceUploadSizeForSourceData(QSize
//      size, quint32 bpl, quint32 bytesPerPixel, qsizetype dataSize, bool
//      warn)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN18QRhiImplementation41clampedSubResourceUploadSizeForSourceDataE5QSizejjxb(
    QRhiImplementation *self,
    const QSize *size,
    quint32 bpl,
    quint32 bytesPerPixel,
    qsizetype dataSize,
    bool warn) {
  return new QSize(
      self->clampedSubResourceUploadSizeForSourceData(
          *size,
          bpl,
          bytesPerPixel,
          dataSize,
          warn));
}

//  void QRhiImplementation::runCleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRhiImplementation10runCleanupEv(QRhiImplementation *self) {
  self->runCleanup();
}

//  a Python function taken by a CuteQRhiImplementation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiImplementation(
    QRhiImplementation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiImplementation *>(self)->take(key, call);
}
