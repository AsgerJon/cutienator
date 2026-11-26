//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Objective-C++: Qt writes these functions only in 'qrhimetal.mm', the
//  Metal backend of QRhi, and Qt's library has no name for them, so their
//  code is copied here, with the structures of private data of the backend
//  and the functions of the file they call, which only a compiler of
//  Objective-C++ on Apple's systems reads; 'summon' builds this file there
//  only. They work on objects Qt made, whose data has the layout of these
//  same structures. The virtual functions of the classes made elsewhere are
//  reached through the object; a class a ritual here makes has every
//  function of it copied, its virtual ones among them, so that the compiler
//  writes its table of virtual functions here, which Qt's library keeps to
//  itself.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#include <QtGui/6.12.0/QtGui/private/qrhimetal_icb_p.h>
#include <QtGui/6.12.0/QtGui/private/qshader_p.h>
#include <QGuiApplication>
#include <QWindow>
#include <QUrl>
#include <QFile>
#include <QTemporaryFile>
#include <QFileInfo>
#include <qmath.h>
#include <QOperatingSystemVersion>
#include <QtCore/private/qcore_mac_p.h>
#include <QtGui/private/qmetallayer_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#ifdef Q_OS_MACOS
#include <AppKit/AppKit.h>
#else
#include <UIKit/UIKit.h>
#endif
#include <QuartzCore/CATransaction.h>
#include <Metal/Metal.h>
#include <utility> // for std::pair

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from qtbase/src/gui/rhi/qrhimetal.mm, lines 56 and 61
#define QRHI_METAL_DISABLE_BINARY_ARCHIVE
#define QRHI_METAL_COMMAND_BUFFERS_WITH_UNRETAINED_REFERENCES
QT_BEGIN_NAMESPACE

//  from qtbase/src/gui/rhi/qrhimetal.mm, lines 155-505
struct QMetalShader
{
    id<MTLLibrary> lib = nil;
    id<MTLFunction> func = nil;
    std::array<uint, 3> localSize = {};
    uint outputVertexCount = 0;
    QShaderDescription desc;
    QShader::NativeResourceBindingMap nativeResourceBindingMap;
    QShader::NativeShaderInfo nativeShaderInfo;

    void destroy() {
        nativeResourceBindingMap.clear();
        [lib release];
        lib = nil;
        [func release];
        func = nil;
    }
};

struct QRhiMetalData
{
    QRhiMetalData(QRhiMetal *rhi) : q(rhi), ofr(rhi) { }

    QRhiMetal *q;
    id<MTLDevice> dev = nil;
    id<MTLCommandQueue> cmdQueue = nil;
    id<MTLBinaryArchive> binArch = nil;

    id<MTLCommandBuffer> newCommandBuffer();
    MTLRenderPassDescriptor *createDefaultRenderPass(bool hasDepthStencil,
                                                     const QColor &colorClearValue,
                                                     const QRhiDepthStencilClearValue &depthStencilClearValue,
                                                     int colorAttCount,
                                                     QRhiShadingRateMap *shadingRateMap);
    id<MTLLibrary> createMetalLib(const QShader &shader, QShader::Variant shaderVariant,
                                  QString *error, QByteArray *entryPoint, QShaderKey *activeKey);
    id<MTLFunction> createMSLShaderFunction(id<MTLLibrary> lib, const QByteArray &entryPoint);
    bool setupBinaryArchive(NSURL *sourceFileUrl = nil);
    void addRenderPipelineToBinaryArchive(MTLRenderPipelineDescriptor *rpDesc);
    void trySeedingRenderPipelineFromBinaryArchive(MTLRenderPipelineDescriptor *rpDesc);
    void addComputePipelineToBinaryArchive(MTLComputePipelineDescriptor *cpDesc);
    void trySeedingComputePipelineFromBinaryArchive(MTLComputePipelineDescriptor *cpDesc);

    struct DeferredReleaseEntry {
        enum Type {
            Buffer,
            RenderBuffer,
            Texture,
            Sampler,
            StagingBuffer,
            GraphicsPipeline,
            ComputePipeline,
            ShadingRateMap,
            StagingIcbBuffer
        };
        Type type;
        int lastActiveFrameSlot; // -1 if not used otherwise 0..FRAMES_IN_FLIGHT-1
        union {
            struct {
                id<MTLBuffer> buffers[QMTL_FRAMES_IN_FLIGHT];
            } buffer;
            struct {
                id<MTLTexture> texture;
            } renderbuffer;
            struct {
                id<MTLTexture> texture;
                id<MTLBuffer> stagingBuffers[QMTL_FRAMES_IN_FLIGHT];
                id<MTLTexture> views[QRhi::MAX_MIP_LEVELS];
            } texture;
            struct {
                id<MTLSamplerState> samplerState;
            } sampler;
            struct {
                id<MTLBuffer> buffer;
            } stagingBuffer;
            struct {
                id<MTLRenderPipelineState> pipelineState;
                id<MTLDepthStencilState> depthStencilState;
                std::array<id<MTLComputePipelineState>, 3> tessVertexComputeState;
                id<MTLComputePipelineState> tessTessControlComputeState;
            } graphicsPipeline;
            struct {
                id<MTLComputePipelineState> pipelineState;
            } computePipeline;
            struct {
                id<MTLRasterizationRateMap> rateMap;
            } shadingRateMap;
            struct {
                id<MTLIndirectCommandBuffer> icb;
                id<MTLBuffer> argBuffer;
            } stagingIcbBuffer;
        };
    };
    QVector<DeferredReleaseEntry> releaseQueue;

    struct OffscreenFrame {
        OffscreenFrame(QRhiImplementation *rhi) : cbWrapper(rhi) { }
        bool active = false;
        double lastGpuTime = 0;
        QMetalCommandBuffer cbWrapper;
    } ofr;

    struct TextureReadback {
        int activeFrameSlot = -1;
        QRhiReadbackDescription desc;
        QRhiReadbackResult *result;
        id<MTLBuffer> buf;
        quint32 bufSize;
        QSize pixelSize;
        QRhiTexture::Format format;
    };
    QVarLengthArray<TextureReadback, 2> activeTextureReadbacks;

    struct BufferReadback
    {
        int activeFrameSlot = -1;
        QRhiReadbackResult *result;
        quint32 offset;
        quint32 readSize;
        id<MTLBuffer> buf;
    };

    QVarLengthArray<BufferReadback, 2> activeBufferReadbacks;

    MTLCaptureManager *captureMgr;
    id<MTLCaptureScope> captureScope = nil;

    // Indirect Command Buffer (ICB) infrastructure for GPU-driven multi-draw
    id<MTLIndirectCommandBuffer> icb = nil;
    NSUInteger icbCapacity = 0;
    id<MTLComputePipelineState> icbEncodePipelineU32 = nil;
    id<MTLComputePipelineState> icbEncodePipelineU16 = nil;
    id<MTLFunction> icbEncodeFunctionU32 = nil;
    id<MTLFunction> icbEncodeFunctionU16 = nil;
    id<MTLBuffer> icbArgumentBuffer = nil;

    static const int TEXBUF_ALIGN = 256; // probably not accurate

    QHash<QRhiShaderStage, QMetalShader> shaderCache;
};

Q_DECLARE_TYPEINFO(QRhiMetalData::DeferredReleaseEntry, Q_RELOCATABLE_TYPE);
Q_DECLARE_TYPEINFO(QRhiMetalData::TextureReadback, Q_RELOCATABLE_TYPE);

struct QMetalBufferData
{
    bool managed;
    bool slotted;
    id<MTLBuffer> buf[QMTL_FRAMES_IN_FLIGHT];
    struct BufferUpdate {
        quint32 offset;
        QRhiBufferData data;
    };
    QVarLengthArray<BufferUpdate, 16> pendingUpdates[QMTL_FRAMES_IN_FLIGHT];
};

struct QMetalRenderBufferData
{
    MTLPixelFormat format;
    id<MTLTexture> tex = nil;
};

struct QMetalTextureData
{
    QMetalTextureData(QMetalTexture *t) : q(t) { }

    QMetalTexture *q;
    MTLPixelFormat format;
    id<MTLTexture> tex = nil;
    id<MTLBuffer> stagingBuf[QMTL_FRAMES_IN_FLIGHT];
    bool owns = true;
    id<MTLTexture> perLevelViews[QRhi::MAX_MIP_LEVELS];

    id<MTLTexture> viewForLevel(int level);
};

struct QMetalSamplerData
{
    id<MTLSamplerState> samplerState = nil;
};

struct QMetalShadingRateMapData
{
    id<MTLRasterizationRateMap> rateMap = nil;
};

struct QMetalShaderResourceBindingsData {
    struct Stage {
        struct Buffer {
            int nativeBinding;
            id<MTLBuffer> mtlbuf;
            quint32 offset;
        };
        struct Texture {
            int nativeBinding;
            id<MTLTexture> mtltex;
        };
        struct Sampler {
            int nativeBinding;
            id<MTLSamplerState> mtlsampler;
        };
        QVarLengthArray<Buffer, 8> buffers;
        QVarLengthArray<Texture, 8> textures;
        QVarLengthArray<Sampler, 8> samplers;
        QRhiBatchedBindings<id<MTLBuffer> > bufferBatches;
        QRhiBatchedBindings<NSUInteger> bufferOffsetBatches;
        QRhiBatchedBindings<id<MTLTexture> > textureBatches;
        QRhiBatchedBindings<id<MTLSamplerState> > samplerBatches;
    } res[QRhiMetal::SUPPORTED_STAGES];
    enum { VERTEX = 0, FRAGMENT = 1, COMPUTE = 2, TESSCTRL = 3, TESSEVAL = 4 };
};

struct QMetalCommandBufferData
{
    id<MTLCommandBuffer> cb;
    double lastGpuTime = 0;
    id<MTLRenderCommandEncoder> currentRenderPassEncoder;
    id<MTLComputeCommandEncoder> currentComputePassEncoder;
    id<MTLComputeCommandEncoder> tessellationComputeEncoder;
    MTLRenderPassDescriptor *currentPassRpDesc;
    int currentFirstVertexBinding;
    QRhiBatchedBindings<id<MTLBuffer> > currentVertexInputsBuffers;
    QRhiBatchedBindings<NSUInteger> currentVertexInputOffsets;
    id<MTLDepthStencilState> currentDepthStencilState;
    QMetalShaderResourceBindingsData currentShaderResourceBindingState;
    // Intended final store actions for the attachments whose store action is
    // deferred. MTLStoreActionUnknown for depth and stencil means not deferred.
    // See beginPass().
    QVarLengthArray<std::pair<uint, MTLStoreAction>, 4> deferredColorStoreActions;
    MTLStoreAction deferredDepthStoreAction;
    MTLStoreAction deferredStencilStoreAction;
};

struct QMetalRenderTargetData
{
    QSize pixelSize;
    float dpr = 1;
    int sampleCount = 1;
    int colorAttCount = 0;
    int dsAttCount = 0;

    struct ColorAtt {
        bool needsDrawableForTex = false;
        id<MTLTexture> tex = nil;
        int arrayLayer = 0;
        int slice = 0;
        int level = 0;
        bool needsDrawableForResolveTex = false;
        id<MTLTexture> resolveTex = nil;
        int resolveLayer = 0;
        int resolveLevel = 0;
    };

    struct {
        ColorAtt colorAtt[QMetalRenderPassDescriptor::MAX_COLOR_ATTACHMENTS];
        id<MTLTexture> dsTex = nil;
        id<MTLTexture> dsResolveTex = nil;
        bool hasStencil = false;
        bool depthNeedsStore = false;
        bool preserveColor = false;
        bool preserveDs = false;
    } fb;

    QRhiRenderTargetAttachmentTracker::ResIdList currentResIdList;
};

struct QMetalGraphicsPipelineData
{
    QMetalGraphicsPipeline *q = nullptr;
    id<MTLRenderPipelineState> ps = nil;
    id<MTLDepthStencilState> ds = nil;
    MTLPrimitiveType primitiveType;
    MTLWinding winding;
    MTLCullMode cullMode;
    MTLTriangleFillMode triangleFillMode;
    MTLDepthClipMode depthClipMode;
    float depthBias;
    float slopeScaledDepthBias;
    QMetalShader vs;
    QMetalShader fs;
    struct ExtraBufferManager {
        enum class WorkBufType {
            DeviceLocal,
            HostVisible
        };
        QMetalBuffer *acquireWorkBuffer(QRhiMetal *rhiD, quint32 size, WorkBufType type = WorkBufType::DeviceLocal);
        QVector<QMetalBuffer *> deviceLocalWorkBuffers;
        QVector<QMetalBuffer *> hostVisibleWorkBuffers;
    } extraBufMgr;
    struct Tessellation {
        QMetalGraphicsPipelineData *q = nullptr;
        bool enabled = false;
        bool failed = false;
        uint inControlPointCount;
        uint outControlPointCount;
        QMetalShader compVs[3];
        std::array<id<MTLComputePipelineState>, 3> vertexComputeState = {};
        id<MTLComputePipelineState> tessControlComputeState = nil;
        QMetalShader compTesc;
        QMetalShader vertTese;
        quint32 vsCompOutputBufferSize(quint32 vertexOrIndexCount, quint32 instanceCount) const
        {
            // max vertex output components = resourceLimit(MaxVertexOutputs) * 4 = 60
            return vertexOrIndexCount * instanceCount * sizeof(float) * 60;
        }
        quint32 tescCompOutputBufferSize(quint32 patchCount) const
        {
            return outControlPointCount * patchCount * sizeof(float) * 60;
        }
        quint32 tescCompPatchOutputBufferSize(quint32 patchCount) const
        {
            // assume maxTessellationControlPerPatchOutputComponents is 128
            return patchCount * sizeof(float) * 128;
        }
        quint32 patchCountForDrawCall(quint32 vertexOrIndexCount, quint32 instanceCount) const
        {
            return ((vertexOrIndexCount + inControlPointCount - 1) / inControlPointCount) * instanceCount;
        }
        static int vsCompVariantToIndex(QShader::Variant vertexCompVariant);
        id<MTLComputePipelineState> vsCompPipeline(QRhiMetal *rhiD, QShader::Variant vertexCompVariant);
        id<MTLComputePipelineState> tescCompPipeline(QRhiMetal *rhiD);
        id<MTLRenderPipelineState> teseFragRenderPipeline(QRhiMetal *rhiD, QMetalGraphicsPipeline *pipeline);
    } tess;
    void setupVertexInputDescriptor(MTLVertexDescriptor *desc);
    void setupStageInputDescriptor(MTLStageInputOutputDescriptor *desc);

    // SPIRV-Cross buffer size buffers
    QMetalBuffer *bufferSizeBuffer = nullptr;
};

struct QMetalComputePipelineData
{
    id<MTLComputePipelineState> ps = nil;
    QMetalShader cs;
    MTLSize localSize;

    // SPIRV-Cross buffer size buffers
    QMetalBuffer *bufferSizeBuffer = nullptr;
};

struct QMetalSwapChainData
{
    CAMetalLayer *layer = nullptr;
    id<CAMetalDrawable> curDrawable = nil;
    dispatch_semaphore_t sem[QMTL_FRAMES_IN_FLIGHT];
    double lastGpuTime[QMTL_FRAMES_IN_FLIGHT];
    MTLRenderPassDescriptor *rp = nullptr;
    id<MTLTexture> msaaTex[QMTL_FRAMES_IN_FLIGHT];
    QRhiTexture::Format rhiColorFormat;
    MTLPixelFormat colorFormat;
};

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 532
template <class Int>
inline Int aligned(Int v, Int byteAlign)
{
    return (v + byteAlign - 1) & ~(byteAlign - 1);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 551
inline id<MTLCommandBuffer> QRhiMetalData::newCommandBuffer()
{
#ifdef QRHI_METAL_COMMAND_BUFFERS_WITH_UNRETAINED_REFERENCES
    // Do not let the command buffer mess with the refcount of objects. We do
    // have a proper render loop and will manage lifetimes similarly to other
    // backends (Vulkan).
    return [cmdQueue commandBufferWithUnretainedReferences];
#else
    return [cmdQueue commandBuffer];
#endif
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 563
inline bool QRhiMetalData::setupBinaryArchive(NSURL *sourceFileUrl)
{
#ifdef QRHI_METAL_DISABLE_BINARY_ARCHIVE
    return false;
#endif

    [binArch release];
    MTLBinaryArchiveDescriptor *binArchDesc = [MTLBinaryArchiveDescriptor new];
    binArchDesc.url = sourceFileUrl;
    NSError *err = nil;
    binArch = [dev newBinaryArchiveWithDescriptor: binArchDesc error: &err];
    [binArchDesc release];
    if (!binArch) {
        const QString msg = QString::fromNSString(err.localizedDescription);
        qWarning("newBinaryArchiveWithDescriptor failed: %s", qPrintable(msg));
        return false;
    }
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1201
static inline int mapBinding(int binding,
                             int stageIndex,
                             const QShader::NativeResourceBindingMap *nativeResourceBindingMaps[],
                             BindingType type)
{
    const QShader::NativeResourceBindingMap *map = nativeResourceBindingMaps[stageIndex];
    if (!map || map->isEmpty())
        return binding; // old QShader versions do not have this map, assume 1:1 mapping then

    auto it = map->constFind(binding);
    if (it != map->cend())
        return type == BindingType::Sampler ? it->second : it->first; // may be -1, if the resource is inactive

    // Hitting this path is normal too. It is not given that the resource (for
    // example, a uniform block) is present in the shaders for all the stages
    // specified by the visibility mask in the QRhiShaderResourceBinding.
    return -1;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1220
static inline void bindStageBuffers(QMetalCommandBuffer *cbD,
                                    int stage,
                                    const QRhiBatchedBindings<id<MTLBuffer>>::Batch &bufferBatch,
                                    const QRhiBatchedBindings<NSUInteger>::Batch &offsetBatch)
{
    switch (stage) {
    case QMetalShaderResourceBindingsData::VERTEX:
        [cbD->d->currentRenderPassEncoder setVertexBuffers: bufferBatch.resources.constData()
          offsets: offsetBatch.resources.constData()
          withRange: NSMakeRange(bufferBatch.startBinding, NSUInteger(bufferBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::FRAGMENT:
        [cbD->d->currentRenderPassEncoder setFragmentBuffers: bufferBatch.resources.constData()
          offsets: offsetBatch.resources.constData()
          withRange: NSMakeRange(bufferBatch.startBinding, NSUInteger(bufferBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::COMPUTE:
        [cbD->d->currentComputePassEncoder setBuffers: bufferBatch.resources.constData()
          offsets: offsetBatch.resources.constData()
          withRange: NSMakeRange(bufferBatch.startBinding, NSUInteger(bufferBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::TESSCTRL:
    case QMetalShaderResourceBindingsData::TESSEVAL:
        // do nothing.  These are used later for tessellation
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1251
static inline void bindStageTextures(QMetalCommandBuffer *cbD,
                                     int stage,
                                     const QRhiBatchedBindings<id<MTLTexture>>::Batch &textureBatch)
{
    switch (stage) {
    case QMetalShaderResourceBindingsData::VERTEX:
        [cbD->d->currentRenderPassEncoder setVertexTextures: textureBatch.resources.constData()
          withRange: NSMakeRange(textureBatch.startBinding, NSUInteger(textureBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::FRAGMENT:
        [cbD->d->currentRenderPassEncoder setFragmentTextures: textureBatch.resources.constData()
          withRange: NSMakeRange(textureBatch.startBinding, NSUInteger(textureBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::COMPUTE:
        [cbD->d->currentComputePassEncoder setTextures: textureBatch.resources.constData()
          withRange: NSMakeRange(textureBatch.startBinding, NSUInteger(textureBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::TESSCTRL:
    case QMetalShaderResourceBindingsData::TESSEVAL:
        // do nothing.  These are used later for tessellation
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1278
static inline void bindStageSamplers(QMetalCommandBuffer *cbD,
                                     int encoderStage,
                                     const QRhiBatchedBindings<id<MTLSamplerState>>::Batch &samplerBatch)
{
    switch (encoderStage) {
    case QMetalShaderResourceBindingsData::VERTEX:
        [cbD->d->currentRenderPassEncoder setVertexSamplerStates: samplerBatch.resources.constData()
          withRange: NSMakeRange(samplerBatch.startBinding, NSUInteger(samplerBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::FRAGMENT:
        [cbD->d->currentRenderPassEncoder setFragmentSamplerStates: samplerBatch.resources.constData()
          withRange: NSMakeRange(samplerBatch.startBinding, NSUInteger(samplerBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::COMPUTE:
        [cbD->d->currentComputePassEncoder setSamplerStates: samplerBatch.resources.constData()
          withRange: NSMakeRange(samplerBatch.startBinding, NSUInteger(samplerBatch.resources.count()))];
        break;
    case QMetalShaderResourceBindingsData::TESSCTRL:
    case QMetalShaderResourceBindingsData::TESSEVAL:
        // do nothing.  These are used later for tessellation
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1310
static inline void rebindShaderResources(QMetalCommandBuffer *cbD, int resourceStage, int encoderStage,
                                         const QMetalShaderResourceBindingsData *customBindingState = nullptr)
{
    const QMetalShaderResourceBindingsData *bindingData = customBindingState ? customBindingState : &cbD->d->currentShaderResourceBindingState;

    for (int i = 0, ie = bindingData->res[resourceStage].bufferBatches.batches.count(); i != ie; ++i) {
        const auto &bufferBatch(bindingData->res[resourceStage].bufferBatches.batches[i]);
        const auto &offsetBatch(bindingData->res[resourceStage].bufferOffsetBatches.batches[i]);
        bindStageBuffers(cbD, encoderStage, bufferBatch, offsetBatch);
    }

    for (int i = 0, ie = bindingData->res[resourceStage].textureBatches.batches.count(); i != ie; ++i) {
        const auto &batch(bindingData->res[resourceStage].textureBatches.batches[i]);
        bindStageTextures(cbD, encoderStage, batch);
    }

    for (int i = 0, ie = bindingData->res[resourceStage].samplerBatches.batches.count(); i != ie; ++i) {
        const auto &batch(bindingData->res[resourceStage].samplerBatches.batches[i]);
        bindStageSamplers(cbD, encoderStage, batch);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1332
static inline QRhiShaderResourceBinding::StageFlag toRhiSrbStage(int stage)
{
    switch (stage) {
    case QMetalShaderResourceBindingsData::VERTEX:
        return QRhiShaderResourceBinding::StageFlag::VertexStage;
    case QMetalShaderResourceBindingsData::TESSCTRL:
        return QRhiShaderResourceBinding::StageFlag::TessellationControlStage;
    case QMetalShaderResourceBindingsData::TESSEVAL:
        return QRhiShaderResourceBinding::StageFlag::TessellationEvaluationStage;
    case QMetalShaderResourceBindingsData::FRAGMENT:
        return QRhiShaderResourceBinding::StageFlag::FragmentStage;
    case QMetalShaderResourceBindingsData::COMPUTE:
        return QRhiShaderResourceBinding::StageFlag::ComputeStage;
    }

    Q_UNREACHABLE_RETURN(QRhiShaderResourceBinding::StageFlag::VertexStage);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2080
static QMetalRenderTargetData *currentRenderTargetData(QMetalCommandBuffer *cbD)
{
    switch (cbD->currentTarget->resourceType()) {
    case QRhiResource::SwapChainRenderTarget:
        return QRHI_RES(QMetalSwapChainRenderTarget, cbD->currentTarget)->d;
    case QRhiResource::TextureRenderTarget:
        return QRHI_RES(QMetalTextureRenderTarget, cbD->currentTarget)->d;
    default:
        return nullptr;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2094
static inline bool canStoreAttachment(id<MTLTexture> tex)
{
    return tex && tex.storageMode != MTLStorageModeMemoryless;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2147
static void endTempComputeEncoding(QRhiMetal *rhiD, QMetalCommandBuffer *cbD,
                                   id<MTLComputeCommandEncoder> computeEncoder)
{
    if (computeEncoder) {
        [computeEncoder endEncoding];
        computeEncoder = nil;
    }

    QMetalRenderTargetData *rtD = currentRenderTargetData(cbD);
    Q_ASSERT(rtD);

    QVarLengthArray<MTLLoadAction, 4> oldColorLoad;
    for (uint i = 0; i < uint(rtD->colorAttCount); ++i) {
        oldColorLoad.append(cbD->d->currentPassRpDesc.colorAttachments[i].loadAction);
        if (cbD->d->currentPassRpDesc.colorAttachments[i].storeAction != MTLStoreActionDontCare)
            cbD->d->currentPassRpDesc.colorAttachments[i].loadAction = MTLLoadActionLoad;
    }

    MTLLoadAction oldDepthLoad;
    MTLLoadAction oldStencilLoad;
    if (rtD->dsAttCount) {
        oldDepthLoad = cbD->d->currentPassRpDesc.depthAttachment.loadAction;
        if (cbD->d->currentPassRpDesc.depthAttachment.storeAction != MTLStoreActionDontCare)
            cbD->d->currentPassRpDesc.depthAttachment.loadAction = MTLLoadActionLoad;

        oldStencilLoad = cbD->d->currentPassRpDesc.stencilAttachment.loadAction;
        if (cbD->d->currentPassRpDesc.stencilAttachment.storeAction != MTLStoreActionDontCare)
            cbD->d->currentPassRpDesc.stencilAttachment.loadAction = MTLLoadActionLoad;
    }

    // The state below is not tied to the pipeline, so it is not restored by the
    // callers when they reactivate it on the new encoder. Preserve it here,
    // otherwise the pass would silently continue with a full-target viewport,
    // no scissor, and default blend constants and stencil reference.
    const QRhiViewport prevViewport = cbD->currentViewport;
    const bool prevHasScissor = cbD->hasCustomScissorSet;
    const QRhiScissor prevScissor = cbD->currentScissor;
    const bool prevHasBlendConstants = cbD->hasBlendConstantsSet;
    const QColor prevBlendConstants = cbD->currentBlendConstants;
    const bool prevHasStencilRef = cbD->hasStencilRefSet;
    const quint32 prevStencilRef = cbD->currentStencilRef;
    // Whether the pipeline was relying on the viewport-derived default scissor,
    // which setViewport() below cannot reapply on its own: it only does so when
    // a pipeline is already current, and there is none at that point.
    const bool prevHasDefaultScissor = cbD->currentGraphicsPipeline
            && !cbD->currentGraphicsPipeline->flags().testFlag(QRhiGraphicsPipeline::UsesScissor);

    cbD->d->currentRenderPassEncoder = [cbD->d->cb renderCommandEncoderWithDescriptor: cbD->d->currentPassRpDesc];
    cbD->resetPerPassCachedState();

    // Must come before the callers reactivate the pipeline: setScissor()
    // expects no pipeline to be current yet, and setDefaultScissor() consults
    // the viewport.
    if (!qFuzzyIsNull(prevViewport.viewport()[2]) || !qFuzzyIsNull(prevViewport.viewport()[3]))
        rhiD->setViewport(cbD, prevViewport);
    if (prevHasScissor)
        rhiD->setScissor(cbD, prevScissor);
    else if (prevHasDefaultScissor)
        rhiD->setDefaultScissor(cbD);
    if (prevHasBlendConstants)
        rhiD->setBlendConstants(cbD, prevBlendConstants);
    if (prevHasStencilRef)
        rhiD->setStencilRef(cbD, prevStencilRef);

    for (uint i = 0; i < uint(rtD->colorAttCount); ++i) {
        cbD->d->currentPassRpDesc.colorAttachments[i].loadAction = oldColorLoad[i];
    }

    if (rtD->dsAttCount) {
        cbD->d->currentPassRpDesc.depthAttachment.loadAction = oldDepthLoad;
        cbD->d->currentPassRpDesc.stencilAttachment.loadAction = oldStencilLoad;
    }

}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3059
inline MTLRenderPassDescriptor *QRhiMetalData::createDefaultRenderPass(bool hasDepthStencil,
                                                                const QColor &colorClearValue,
                                                                const QRhiDepthStencilClearValue &depthStencilClearValue,
                                                                int colorAttCount,
                                                                QRhiShadingRateMap *shadingRateMap)
{
    MTLRenderPassDescriptor *rp = [MTLRenderPassDescriptor renderPassDescriptor];
    MTLClearColor c = MTLClearColorMake(colorClearValue.redF(), colorClearValue.greenF(), colorClearValue.blueF(),
                                        colorClearValue.alphaF());

    for (uint i = 0; i < uint(colorAttCount); ++i) {
        rp.colorAttachments[i].loadAction = MTLLoadActionClear;
        rp.colorAttachments[i].storeAction = MTLStoreActionStore;
        rp.colorAttachments[i].clearColor = c;
    }

    if (hasDepthStencil) {
        rp.depthAttachment.loadAction = MTLLoadActionClear;
        rp.depthAttachment.storeAction = MTLStoreActionDontCare;
        rp.stencilAttachment.loadAction = MTLLoadActionClear;
        rp.stencilAttachment.storeAction = MTLStoreActionDontCare;
        rp.depthAttachment.clearDepth = double(depthStencilClearValue.depthClearValue());
        rp.stencilAttachment.clearStencil = depthStencilClearValue.stencilClearValue();
    }

    if (shadingRateMap)
        rp.rasterizationRateMap = QRHI_RES(QMetalShadingRateMap, shadingRateMap)->d->rateMap;

    return rp;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3708
static void qrhimtl_releaseBuffer(const QRhiMetalData::DeferredReleaseEntry &e)
{
    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i)
        [e.buffer.buffers[i] release];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3714
static void qrhimtl_releaseRenderBuffer(const QRhiMetalData::DeferredReleaseEntry &e)
{
    [e.renderbuffer.texture release];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3719
static void qrhimtl_releaseTexture(const QRhiMetalData::DeferredReleaseEntry &e)
{
    [e.texture.texture release];
    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i)
        [e.texture.stagingBuffers[i] release];
    for (int i = 0; i < QRhi::MAX_MIP_LEVELS; ++i)
        [e.texture.views[i] release];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3728
static void qrhimtl_releaseSampler(const QRhiMetalData::DeferredReleaseEntry &e)
{
    [e.sampler.samplerState release];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3952
static inline MTLPixelFormat toMetalTextureFormat(QRhiTexture::Format format, QRhiTexture::Flags flags, const QRhiMetal *d)
{
#ifndef Q_OS_MACOS
    Q_UNUSED(d);
#endif

    const bool srgb = flags.testFlag(QRhiTexture::sRGB);
    switch (format) {
    case QRhiTexture::RGBA8:
        return srgb ? MTLPixelFormatRGBA8Unorm_sRGB : MTLPixelFormatRGBA8Unorm;
    case QRhiTexture::BGRA8:
        return srgb ? MTLPixelFormatBGRA8Unorm_sRGB : MTLPixelFormatBGRA8Unorm;
    case QRhiTexture::R8:
#ifdef Q_OS_MACOS
        return MTLPixelFormatR8Unorm;
#else
        return srgb ? MTLPixelFormatR8Unorm_sRGB : MTLPixelFormatR8Unorm;
#endif
    case QRhiTexture::R8SI:
        return MTLPixelFormatR8Sint;
    case QRhiTexture::R8UI:
        return MTLPixelFormatR8Uint;
    case QRhiTexture::RG8:
#ifdef Q_OS_MACOS
        return MTLPixelFormatRG8Unorm;
#else
        return srgb ? MTLPixelFormatRG8Unorm_sRGB : MTLPixelFormatRG8Unorm;
#endif
    case QRhiTexture::R16:
        return MTLPixelFormatR16Unorm;
    case QRhiTexture::RG16:
        return MTLPixelFormatRG16Unorm;
    case QRhiTexture::RED_OR_ALPHA8:
        return MTLPixelFormatR8Unorm;

    case QRhiTexture::RGBA16F:
        return MTLPixelFormatRGBA16Float;
    case QRhiTexture::RGBA32F:
        return MTLPixelFormatRGBA32Float;
    case QRhiTexture::R16F:
        return MTLPixelFormatR16Float;
    case QRhiTexture::R32F:
        return MTLPixelFormatR32Float;

    case QRhiTexture::RGB10A2:
        return MTLPixelFormatRGB10A2Unorm;

    case QRhiTexture::R32SI:
        return MTLPixelFormatR32Sint;
    case QRhiTexture::R32UI:
        return MTLPixelFormatR32Uint;
    case QRhiTexture::RG32SI:
        return MTLPixelFormatRG32Sint;
    case QRhiTexture::RG32UI:
        return MTLPixelFormatRG32Uint;
    case QRhiTexture::RGBA32SI:
        return MTLPixelFormatRGBA32Sint;
    case QRhiTexture::RGBA32UI:
        return MTLPixelFormatRGBA32Uint;

#ifdef Q_OS_MACOS
    case QRhiTexture::D16:
        return MTLPixelFormatDepth16Unorm;
    case QRhiTexture::D24:
        return [d->d->dev isDepth24Stencil8PixelFormatSupported] ? MTLPixelFormatDepth24Unorm_Stencil8 : MTLPixelFormatDepth32Float;
    case QRhiTexture::D24S8:
        return [d->d->dev isDepth24Stencil8PixelFormatSupported] ? MTLPixelFormatDepth24Unorm_Stencil8 : MTLPixelFormatDepth32Float_Stencil8;
#else
    case QRhiTexture::D16:
        return MTLPixelFormatDepth32Float;
    case QRhiTexture::D24:
        return MTLPixelFormatDepth32Float;
    case QRhiTexture::D24S8:
        return MTLPixelFormatDepth32Float_Stencil8;
#endif
    case QRhiTexture::D32F:
        return MTLPixelFormatDepth32Float;
    case QRhiTexture::D32FS8:
        return MTLPixelFormatDepth32Float_Stencil8;

#ifdef Q_OS_MACOS
    case QRhiTexture::BC1:
        return srgb ? MTLPixelFormatBC1_RGBA_sRGB : MTLPixelFormatBC1_RGBA;
    case QRhiTexture::BC2:
        return srgb ? MTLPixelFormatBC2_RGBA_sRGB : MTLPixelFormatBC2_RGBA;
    case QRhiTexture::BC3:
        return srgb ? MTLPixelFormatBC3_RGBA_sRGB : MTLPixelFormatBC3_RGBA;
    case QRhiTexture::BC4:
        return MTLPixelFormatBC4_RUnorm;
    case QRhiTexture::BC5:
        qWarning("QRhiMetal does not support BC5");
        return MTLPixelFormatInvalid;
    case QRhiTexture::BC6H:
        return MTLPixelFormatBC6H_RGBUfloat;
    case QRhiTexture::BC7:
        return srgb ? MTLPixelFormatBC7_RGBAUnorm_sRGB : MTLPixelFormatBC7_RGBAUnorm;
#else
    case QRhiTexture::BC1:
    case QRhiTexture::BC2:
    case QRhiTexture::BC3:
    case QRhiTexture::BC4:
    case QRhiTexture::BC5:
    case QRhiTexture::BC6H:
    case QRhiTexture::BC7:
        qWarning("QRhiMetal: BCx compression not supported on this platform");
        return MTLPixelFormatInvalid;
#endif

#ifndef Q_OS_MACOS
    case QRhiTexture::ETC2_RGB8:
        return srgb ? MTLPixelFormatETC2_RGB8_sRGB : MTLPixelFormatETC2_RGB8;
    case QRhiTexture::ETC2_RGB8A1:
        return srgb ? MTLPixelFormatETC2_RGB8A1_sRGB : MTLPixelFormatETC2_RGB8A1;
    case QRhiTexture::ETC2_RGBA8:
        return srgb ? MTLPixelFormatEAC_RGBA8_sRGB : MTLPixelFormatEAC_RGBA8;

    case QRhiTexture::ASTC_4x4:
        return srgb ? MTLPixelFormatASTC_4x4_sRGB : MTLPixelFormatASTC_4x4_LDR;
    case QRhiTexture::ASTC_5x4:
        return srgb ? MTLPixelFormatASTC_5x4_sRGB : MTLPixelFormatASTC_5x4_LDR;
    case QRhiTexture::ASTC_5x5:
        return srgb ? MTLPixelFormatASTC_5x5_sRGB : MTLPixelFormatASTC_5x5_LDR;
    case QRhiTexture::ASTC_6x5:
        return srgb ? MTLPixelFormatASTC_6x5_sRGB : MTLPixelFormatASTC_6x5_LDR;
    case QRhiTexture::ASTC_6x6:
        return srgb ? MTLPixelFormatASTC_6x6_sRGB : MTLPixelFormatASTC_6x6_LDR;
    case QRhiTexture::ASTC_8x5:
        return srgb ? MTLPixelFormatASTC_8x5_sRGB : MTLPixelFormatASTC_8x5_LDR;
    case QRhiTexture::ASTC_8x6:
        return srgb ? MTLPixelFormatASTC_8x6_sRGB : MTLPixelFormatASTC_8x6_LDR;
    case QRhiTexture::ASTC_8x8:
        return srgb ? MTLPixelFormatASTC_8x8_sRGB : MTLPixelFormatASTC_8x8_LDR;
    case QRhiTexture::ASTC_10x5:
        return srgb ? MTLPixelFormatASTC_10x5_sRGB : MTLPixelFormatASTC_10x5_LDR;
    case QRhiTexture::ASTC_10x6:
        return srgb ? MTLPixelFormatASTC_10x6_sRGB : MTLPixelFormatASTC_10x6_LDR;
    case QRhiTexture::ASTC_10x8:
        return srgb ? MTLPixelFormatASTC_10x8_sRGB : MTLPixelFormatASTC_10x8_LDR;
    case QRhiTexture::ASTC_10x10:
        return srgb ? MTLPixelFormatASTC_10x10_sRGB : MTLPixelFormatASTC_10x10_LDR;
    case QRhiTexture::ASTC_12x10:
        return srgb ? MTLPixelFormatASTC_12x10_sRGB : MTLPixelFormatASTC_12x10_LDR;
    case QRhiTexture::ASTC_12x12:
        return srgb ? MTLPixelFormatASTC_12x12_sRGB : MTLPixelFormatASTC_12x12_LDR;
#else
    case QRhiTexture::ETC2_RGB8:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatETC2_RGB8_sRGB : MTLPixelFormatETC2_RGB8;
        qWarning("QRhiMetal: ETC2 compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ETC2_RGB8A1:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatETC2_RGB8A1_sRGB : MTLPixelFormatETC2_RGB8A1;
        qWarning("QRhiMetal: ETC2 compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ETC2_RGBA8:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatEAC_RGBA8_sRGB : MTLPixelFormatEAC_RGBA8;
        qWarning("QRhiMetal: ETC2 compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_4x4:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_4x4_sRGB : MTLPixelFormatASTC_4x4_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_5x4:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_5x4_sRGB : MTLPixelFormatASTC_5x4_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_5x5:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_5x5_sRGB : MTLPixelFormatASTC_5x5_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_6x5:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_6x5_sRGB : MTLPixelFormatASTC_6x5_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_6x6:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_6x6_sRGB : MTLPixelFormatASTC_6x6_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_8x5:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_8x5_sRGB : MTLPixelFormatASTC_8x5_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_8x6:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_8x6_sRGB : MTLPixelFormatASTC_8x6_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_8x8:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_8x8_sRGB : MTLPixelFormatASTC_8x8_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_10x5:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_10x5_sRGB : MTLPixelFormatASTC_10x5_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_10x6:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_10x6_sRGB : MTLPixelFormatASTC_10x6_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_10x8:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_10x8_sRGB : MTLPixelFormatASTC_10x8_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_10x10:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_10x10_sRGB : MTLPixelFormatASTC_10x10_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_12x10:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_12x10_sRGB : MTLPixelFormatASTC_12x10_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
    case QRhiTexture::ASTC_12x12:
        if (d->caps.isAppleGPU)
            return srgb ? MTLPixelFormatASTC_12x12_sRGB : MTLPixelFormatASTC_12x12_LDR;
        qWarning("QRhiMetal: ASTC compression not supported on this platform");
        return MTLPixelFormatInvalid;
#endif

    default:
        Q_UNREACHABLE();
        return MTLPixelFormatInvalid;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4490
inline id<MTLTexture> QMetalTextureData::viewForLevel(int level)
{
    Q_ASSERT(level >= 0 && level < int(q->mipLevelCount));
    if (perLevelViews[level])
        return perLevelViews[level];

    const MTLTextureType type = [tex textureType];
    const bool isCube = q->m_flags.testFlag(QRhiTexture::CubeMap);
    const bool isArray = q->m_flags.testFlag(QRhiTexture::TextureArray);
    id<MTLTexture> view = [tex newTextureViewWithPixelFormat: format textureType: type
            levels: NSMakeRange(NSUInteger(level), 1)
            slices: NSMakeRange(0, isCube ? 6 : (isArray ? qMax(0, q->m_arraySize) : 1))];

    perLevelViews[level] = view;
    return view;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4539
static inline MTLSamplerMinMagFilter toMetalFilter(QRhiSampler::Filter f)
{
    switch (f) {
    case QRhiSampler::Nearest:
        return MTLSamplerMinMagFilterNearest;
    case QRhiSampler::Linear:
        return MTLSamplerMinMagFilterLinear;
    default:
        Q_UNREACHABLE();
        return MTLSamplerMinMagFilterNearest;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4552
static inline MTLSamplerMipFilter toMetalMipmapMode(QRhiSampler::Filter f)
{
    switch (f) {
    case QRhiSampler::None:
        return MTLSamplerMipFilterNotMipmapped;
    case QRhiSampler::Nearest:
        return MTLSamplerMipFilterNearest;
    case QRhiSampler::Linear:
        return MTLSamplerMipFilterLinear;
    default:
        Q_UNREACHABLE();
        return MTLSamplerMipFilterNotMipmapped;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4567
static inline MTLSamplerAddressMode toMetalAddressMode(QRhiSampler::AddressMode m)
{
    switch (m) {
    case QRhiSampler::Repeat:
        return MTLSamplerAddressModeRepeat;
    case QRhiSampler::ClampToEdge:
        return MTLSamplerAddressModeClampToEdge;
    case QRhiSampler::Mirror:
        return MTLSamplerAddressModeMirrorRepeat;
    default:
        Q_UNREACHABLE();
        return MTLSamplerAddressModeClampToEdge;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4582
static inline MTLCompareFunction toMetalTextureCompareFunction(QRhiSampler::CompareOp op)
{
    switch (op) {
    case QRhiSampler::Never:
        return MTLCompareFunctionNever;
    case QRhiSampler::Less:
        return MTLCompareFunctionLess;
    case QRhiSampler::Equal:
        return MTLCompareFunctionEqual;
    case QRhiSampler::LessOrEqual:
        return MTLCompareFunctionLessEqual;
    case QRhiSampler::Greater:
        return MTLCompareFunctionGreater;
    case QRhiSampler::NotEqual:
        return MTLCompareFunctionNotEqual;
    case QRhiSampler::GreaterOrEqual:
        return MTLCompareFunctionGreaterEqual;
    case QRhiSampler::Always:
        return MTLCompareFunctionAlways;
    default:
        Q_UNREACHABLE();
        return MTLCompareFunctionNever;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5066
static inline MTLVertexFormat toMetalAttributeFormat(QRhiVertexInputAttribute::Format format)
{
    switch (format) {
    case QRhiVertexInputAttribute::Float4:
        return MTLVertexFormatFloat4;
    case QRhiVertexInputAttribute::Float3:
        return MTLVertexFormatFloat3;
    case QRhiVertexInputAttribute::Float2:
        return MTLVertexFormatFloat2;
    case QRhiVertexInputAttribute::Float:
        return MTLVertexFormatFloat;
    case QRhiVertexInputAttribute::UNormByte4:
        return MTLVertexFormatUChar4Normalized;
    case QRhiVertexInputAttribute::UNormByte2:
        return MTLVertexFormatUChar2Normalized;
    case QRhiVertexInputAttribute::UNormByte:
        return MTLVertexFormatUCharNormalized;
    case QRhiVertexInputAttribute::UInt4:
        return MTLVertexFormatUInt4;
    case QRhiVertexInputAttribute::UInt3:
        return MTLVertexFormatUInt3;
    case QRhiVertexInputAttribute::UInt2:
        return MTLVertexFormatUInt2;
    case QRhiVertexInputAttribute::UInt:
        return MTLVertexFormatUInt;
    case QRhiVertexInputAttribute::SInt4:
        return MTLVertexFormatInt4;
    case QRhiVertexInputAttribute::SInt3:
        return MTLVertexFormatInt3;
    case QRhiVertexInputAttribute::SInt2:
        return MTLVertexFormatInt2;
    case QRhiVertexInputAttribute::SInt:
        return MTLVertexFormatInt;
    case QRhiVertexInputAttribute::Half4:
        return MTLVertexFormatHalf4;
    case QRhiVertexInputAttribute::Half3:
        return MTLVertexFormatHalf3;
    case QRhiVertexInputAttribute::Half2:
        return MTLVertexFormatHalf2;
    case QRhiVertexInputAttribute::Half:
        return MTLVertexFormatHalf;
    case QRhiVertexInputAttribute::UShort4:
        return MTLVertexFormatUShort4;
    case QRhiVertexInputAttribute::UShort3:
        return MTLVertexFormatUShort3;
    case QRhiVertexInputAttribute::UShort2:
        return MTLVertexFormatUShort2;
    case QRhiVertexInputAttribute::UShort:
        return MTLVertexFormatUShort;
    case QRhiVertexInputAttribute::SShort4:
        return MTLVertexFormatShort4;
    case QRhiVertexInputAttribute::SShort3:
        return MTLVertexFormatShort3;
    case QRhiVertexInputAttribute::SShort2:
        return MTLVertexFormatShort2;
    case QRhiVertexInputAttribute::SShort:
        return MTLVertexFormatShort;
    default:
        Q_UNREACHABLE();
        return MTLVertexFormatFloat4;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5129
static inline MTLBlendFactor toMetalBlendFactor(QRhiGraphicsPipeline::BlendFactor f)
{
    switch (f) {
    case QRhiGraphicsPipeline::Zero:
        return MTLBlendFactorZero;
    case QRhiGraphicsPipeline::One:
        return MTLBlendFactorOne;
    case QRhiGraphicsPipeline::SrcColor:
        return MTLBlendFactorSourceColor;
    case QRhiGraphicsPipeline::OneMinusSrcColor:
        return MTLBlendFactorOneMinusSourceColor;
    case QRhiGraphicsPipeline::DstColor:
        return MTLBlendFactorDestinationColor;
    case QRhiGraphicsPipeline::OneMinusDstColor:
        return MTLBlendFactorOneMinusDestinationColor;
    case QRhiGraphicsPipeline::SrcAlpha:
        return MTLBlendFactorSourceAlpha;
    case QRhiGraphicsPipeline::OneMinusSrcAlpha:
        return MTLBlendFactorOneMinusSourceAlpha;
    case QRhiGraphicsPipeline::DstAlpha:
        return MTLBlendFactorDestinationAlpha;
    case QRhiGraphicsPipeline::OneMinusDstAlpha:
        return MTLBlendFactorOneMinusDestinationAlpha;
    case QRhiGraphicsPipeline::ConstantColor:
        return MTLBlendFactorBlendColor;
    case QRhiGraphicsPipeline::ConstantAlpha:
        return MTLBlendFactorBlendAlpha;
    case QRhiGraphicsPipeline::OneMinusConstantColor:
        return MTLBlendFactorOneMinusBlendColor;
    case QRhiGraphicsPipeline::OneMinusConstantAlpha:
        return MTLBlendFactorOneMinusBlendAlpha;
    case QRhiGraphicsPipeline::SrcAlphaSaturate:
        return MTLBlendFactorSourceAlphaSaturated;
    case QRhiGraphicsPipeline::Src1Color:
        return MTLBlendFactorSource1Color;
    case QRhiGraphicsPipeline::OneMinusSrc1Color:
        return MTLBlendFactorOneMinusSource1Color;
    case QRhiGraphicsPipeline::Src1Alpha:
        return MTLBlendFactorSource1Alpha;
    case QRhiGraphicsPipeline::OneMinusSrc1Alpha:
        return MTLBlendFactorOneMinusSource1Alpha;
    default:
        Q_UNREACHABLE();
        return MTLBlendFactorZero;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5176
static inline MTLBlendOperation toMetalBlendOp(QRhiGraphicsPipeline::BlendOp op)
{
    switch (op) {
    case QRhiGraphicsPipeline::Add:
        return MTLBlendOperationAdd;
    case QRhiGraphicsPipeline::Subtract:
        return MTLBlendOperationSubtract;
    case QRhiGraphicsPipeline::ReverseSubtract:
        return MTLBlendOperationReverseSubtract;
    case QRhiGraphicsPipeline::Min:
        return MTLBlendOperationMin;
    case QRhiGraphicsPipeline::Max:
        return MTLBlendOperationMax;
    default:
        Q_UNREACHABLE();
        return MTLBlendOperationAdd;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5195
static inline uint toMetalColorWriteMask(QRhiGraphicsPipeline::ColorMask c)
{
    uint f = 0;
    if (c.testFlag(QRhiGraphicsPipeline::R))
        f |= MTLColorWriteMaskRed;
    if (c.testFlag(QRhiGraphicsPipeline::G))
        f |= MTLColorWriteMaskGreen;
    if (c.testFlag(QRhiGraphicsPipeline::B))
        f |= MTLColorWriteMaskBlue;
    if (c.testFlag(QRhiGraphicsPipeline::A))
        f |= MTLColorWriteMaskAlpha;
    return f;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5209
static inline MTLCompareFunction toMetalCompareOp(QRhiGraphicsPipeline::CompareOp op)
{
    switch (op) {
    case QRhiGraphicsPipeline::Never:
        return MTLCompareFunctionNever;
    case QRhiGraphicsPipeline::Less:
        return MTLCompareFunctionLess;
    case QRhiGraphicsPipeline::Equal:
        return MTLCompareFunctionEqual;
    case QRhiGraphicsPipeline::LessOrEqual:
        return MTLCompareFunctionLessEqual;
    case QRhiGraphicsPipeline::Greater:
        return MTLCompareFunctionGreater;
    case QRhiGraphicsPipeline::NotEqual:
        return MTLCompareFunctionNotEqual;
    case QRhiGraphicsPipeline::GreaterOrEqual:
        return MTLCompareFunctionGreaterEqual;
    case QRhiGraphicsPipeline::Always:
        return MTLCompareFunctionAlways;
    default:
        Q_UNREACHABLE();
        return MTLCompareFunctionAlways;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5234
static inline MTLStencilOperation toMetalStencilOp(QRhiGraphicsPipeline::StencilOp op)
{
    switch (op) {
    case QRhiGraphicsPipeline::StencilZero:
        return MTLStencilOperationZero;
    case QRhiGraphicsPipeline::Keep:
        return MTLStencilOperationKeep;
    case QRhiGraphicsPipeline::Replace:
        return MTLStencilOperationReplace;
    case QRhiGraphicsPipeline::IncrementAndClamp:
        return MTLStencilOperationIncrementClamp;
    case QRhiGraphicsPipeline::DecrementAndClamp:
        return MTLStencilOperationDecrementClamp;
    case QRhiGraphicsPipeline::Invert:
        return MTLStencilOperationInvert;
    case QRhiGraphicsPipeline::IncrementAndWrap:
        return MTLStencilOperationIncrementWrap;
    case QRhiGraphicsPipeline::DecrementAndWrap:
        return MTLStencilOperationDecrementWrap;
    default:
        Q_UNREACHABLE();
        return MTLStencilOperationKeep;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5259
static inline MTLPrimitiveType toMetalPrimitiveType(QRhiGraphicsPipeline::Topology t)
{
    switch (t) {
    case QRhiGraphicsPipeline::Triangles:
        return MTLPrimitiveTypeTriangle;
    case QRhiGraphicsPipeline::TriangleStrip:
        return MTLPrimitiveTypeTriangleStrip;
    case QRhiGraphicsPipeline::Lines:
        return MTLPrimitiveTypeLine;
    case QRhiGraphicsPipeline::LineStrip:
        return MTLPrimitiveTypeLineStrip;
    case QRhiGraphicsPipeline::Points:
        return MTLPrimitiveTypePoint;
    default:
        Q_UNREACHABLE();
        return MTLPrimitiveTypeTriangle;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5278
static inline MTLPrimitiveTopologyClass toMetalPrimitiveTopologyClass(QRhiGraphicsPipeline::Topology t)
{
    switch (t) {
    case QRhiGraphicsPipeline::Triangles:
    case QRhiGraphicsPipeline::TriangleStrip:
    case QRhiGraphicsPipeline::TriangleFan:
        return MTLPrimitiveTopologyClassTriangle;
    case QRhiGraphicsPipeline::Lines:
    case QRhiGraphicsPipeline::LineStrip:
        return MTLPrimitiveTopologyClassLine;
    case QRhiGraphicsPipeline::Points:
        return MTLPrimitiveTopologyClassPoint;
    default:
        Q_UNREACHABLE();
        return MTLPrimitiveTopologyClassTriangle;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5296
static inline MTLCullMode toMetalCullMode(QRhiGraphicsPipeline::CullMode c)
{
    switch (c) {
    case QRhiGraphicsPipeline::None:
        return MTLCullModeNone;
    case QRhiGraphicsPipeline::Front:
        return MTLCullModeFront;
    case QRhiGraphicsPipeline::Back:
        return MTLCullModeBack;
    default:
        Q_UNREACHABLE();
        return MTLCullModeNone;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5311
static inline MTLTriangleFillMode toMetalTriangleFillMode(QRhiGraphicsPipeline::PolygonMode mode)
{
    switch (mode) {
    case QRhiGraphicsPipeline::Fill:
        return MTLTriangleFillModeFill;
    case QRhiGraphicsPipeline::Line:
        return MTLTriangleFillModeLines;
    default:
        Q_UNREACHABLE();
        return MTLTriangleFillModeFill;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5352
static inline MTLLanguageVersion toMetalLanguageVersion(const QShaderVersion &version)
{
    int v = version.version();
    return MTLLanguageVersion(((v / 10) << 16) + (v % 10));
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5358
inline id<MTLLibrary> QRhiMetalData::createMetalLib(const QShader &shader, QShader::Variant shaderVariant,
                                             QString *error, QByteArray *entryPoint, QShaderKey *activeKey)
{
    QVarLengthArray<int, 8> versions;
    versions << 30 << 24 << 23 << 22 << 21 << 20 << 12;

    const QList<QShaderKey> shaders = shader.availableShaders();

    QShaderKey key;

    for (const int &version : versions) {
        key = { QShader::Source::MetalLibShader, version, shaderVariant };
        if (shaders.contains(key))
            break;
    }

    QShaderCode mtllib = shader.shader(key);
    if (!mtllib.shader().isEmpty()) {
        dispatch_data_t data = dispatch_data_create(mtllib.shader().constData(),
                                                    size_t(mtllib.shader().size()),
                                                    dispatch_get_global_queue(0, 0),
                                                    DISPATCH_DATA_DESTRUCTOR_DEFAULT);
        NSError *err = nil;
        id<MTLLibrary> lib = [dev newLibraryWithData: data error: &err];
        dispatch_release(data);
        if (!err) {
            *entryPoint = mtllib.entryPoint();
            *activeKey = key;
            return lib;
        } else {
            const QString msg = QString::fromNSString(err.localizedDescription);
            qWarning("Failed to load metallib from baked shader: %s", qPrintable(msg));
        }
    }

    for (const int &version : versions) {
        key = { QShader::Source::MslShader, version, shaderVariant };
        if (shaders.contains(key))
            break;
    }

    QShaderCode mslSource = shader.shader(key);
    if (mslSource.shader().isEmpty()) {
        qWarning() << "No MSL 2.0 or 1.2 code found in baked shader" << shader;
        return nil;
    }

    NSString *src = [NSString stringWithUTF8String: mslSource.shader().constData()];
    MTLCompileOptions *opts = [[MTLCompileOptions alloc] init];
    opts.languageVersion = toMetalLanguageVersion(key.sourceVersion());
    NSError *err = nil;
    id<MTLLibrary> lib = [dev newLibraryWithSource: src options: opts error: &err];
    [opts release];
    // src is autoreleased

    // if lib is null and err is non-null, we had errors (fail)
    // if lib is non-null and err is non-null, we had warnings (success)
    // if lib is non-null and err is null, there were no errors or warnings (success)
    if (!lib) {
        const QString msg = QString::fromNSString(err.localizedDescription);
        *error = msg;
        return nil;
    }

    *entryPoint = mslSource.entryPoint();
    *activeKey = key;
    return lib;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5427
inline id<MTLFunction> QRhiMetalData::createMSLShaderFunction(id<MTLLibrary> lib, const QByteArray &entryPoint)
{
    return [lib newFunctionWithName:[NSString stringWithUTF8String:entryPoint.constData()]];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5511
inline void QMetalGraphicsPipelineData::setupVertexInputDescriptor(MTLVertexDescriptor *desc)
{
    // same binding space for vertex and constant buffers - work it around
    // should be in native resource binding not SPIR-V, but this will work anyway
    const int firstVertexBinding = QRHI_RES(QMetalShaderResourceBindings, q->shaderResourceBindings())->maxBinding + 1;

    QRhiVertexInputLayout vertexInputLayout = q->vertexInputLayout();
    for (auto it = vertexInputLayout.cbeginAttributes(), itEnd = vertexInputLayout.cendAttributes();
         it != itEnd; ++it)
    {
        const uint loc = uint(it->location());
        desc.attributes[loc].format = decltype(desc.attributes[loc].format)(toMetalAttributeFormat(it->format()));
        desc.attributes[loc].offset = NSUInteger(it->offset());
        desc.attributes[loc].bufferIndex = NSUInteger(firstVertexBinding + it->binding());
    }
    int bindingIndex = 0;
    const NSUInteger viewCount = qMax<NSUInteger>(1, q->multiViewCount());
    for (auto it = vertexInputLayout.cbeginBindings(), itEnd = vertexInputLayout.cendBindings();
         it != itEnd; ++it, ++bindingIndex)
    {
        const uint layoutIdx = uint(firstVertexBinding + bindingIndex);
        desc.layouts[layoutIdx].stepFunction =
                    it->classification() == QRhiVertexInputBinding::PerInstance
                    ? MTLVertexStepFunctionPerInstance : MTLVertexStepFunctionPerVertex;
        desc.layouts[layoutIdx].stepRate = NSUInteger(it->instanceStepRate());
        if (desc.layouts[layoutIdx].stepFunction == MTLVertexStepFunctionPerInstance)
            desc.layouts[layoutIdx].stepRate *= viewCount;
        desc.layouts[layoutIdx].stride = it->stride();
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5576
inline void QRhiMetalData::trySeedingRenderPipelineFromBinaryArchive(MTLRenderPipelineDescriptor *rpDesc)
{
    if (binArch)  {
        NSArray *binArchArray = [NSArray arrayWithObjects: binArch, nil];
        rpDesc.binaryArchives = binArchArray;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5584
inline void QRhiMetalData::addRenderPipelineToBinaryArchive(MTLRenderPipelineDescriptor *rpDesc)
{
    if (binArch) {
        NSError *err = nil;
        if (![binArch addRenderPipelineFunctionsWithDescriptor: rpDesc error: &err]) {
            const QString msg = QString::fromNSString(err.localizedDescription);
            qWarning("Failed to collect render pipeline functions to binary archive: %s", qPrintable(msg));
        }
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5842
static inline int aligned(quint32 offset, quint32 alignment)
{
    return ((offset + alignment - 1) / alignment) * alignment;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6561
inline void QRhiMetalData::trySeedingComputePipelineFromBinaryArchive(MTLComputePipelineDescriptor *cpDesc)
{
    if (binArch) {
        NSArray *binArchArray = [NSArray arrayWithObjects: binArch, nil];
        cpDesc.binaryArchives = binArchArray;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6569
inline void QRhiMetalData::addComputePipelineToBinaryArchive(MTLComputePipelineDescriptor *cpDesc)
{
    if (binArch) {
        NSError *err = nil;
        if (![binArch addComputePipelineFunctionsWithDescriptor: cpDesc error: &err]) {
            const QString msg = QString::fromNSString(err.localizedDescription);
            qWarning("Failed to collect compute pipeline functions to binary archive: %s", qPrintable(msg));
        }
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6814
static inline CAMetalLayer *layerForWindow(QWindow *window)
{
    Q_ASSERT(window);
    CALayer *layer = nullptr;
#ifdef Q_OS_MACOS
    if (auto *cocoaWindow = window->nativeInterface<QNativeInterface::Private::QCocoaWindow>())
        layer = cocoaWindow->contentLayer();
#else
    layer = reinterpret_cast<UIView *>(window->winId()).layer;
#endif
    Q_ASSERT(layer);
    return static_cast<CAMetalLayer *>(layer);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 538
inline bool QRhiMetal::probe(QRhiMetalInitParams *params)
{
    QMacAutoReleasePool pool;

    Q_UNUSED(params);
    id<MTLDevice> dev = MTLCreateSystemDefaultDevice();
    if (dev) {
        [dev release];
        return true;
    }
    return false;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 583
inline bool QRhiMetal::create(QRhi::Flags flags)
{
    rhiFlags = flags;

    if (importedDevice)
        [d->dev retain];
    else
        d->dev = MTLCreateSystemDefaultDevice();

    if (!d->dev) {
        qWarning("No MTLDevice");
        return false;
    }

    const QString deviceName = QString::fromNSString([d->dev name]);
    qCDebug(QRHI_LOG_INFO, "Metal device: %s", qPrintable(deviceName));
    driverInfoStruct.deviceName = deviceName.toUtf8();

    // deviceId and vendorId stay unset for now. Note that registryID is not
    // suitable as deviceId because it does not seem stable on macOS and can
    // apparently change when the system is rebooted.

#ifdef Q_OS_MACOS
    const MTLDeviceLocation deviceLocation = [d->dev location];
    switch (deviceLocation) {
    case MTLDeviceLocationBuiltIn:
        driverInfoStruct.deviceType = QRhiDriverInfo::IntegratedDevice;
        break;
    case MTLDeviceLocationSlot:
        driverInfoStruct.deviceType = QRhiDriverInfo::DiscreteDevice;
        break;
    case MTLDeviceLocationExternal:
        driverInfoStruct.deviceType = QRhiDriverInfo::ExternalDevice;
        break;
    default:
        break;
    }
#else
    driverInfoStruct.deviceType = QRhiDriverInfo::IntegratedDevice;
#endif

    const QOperatingSystemVersion ver = QOperatingSystemVersion::current();
    osMajor = ver.majorVersion();
    osMinor = ver.minorVersion();

    if (importedCmdQueue)
        [d->cmdQueue retain];
    else
        d->cmdQueue = [d->dev newCommandQueue];

    d->captureMgr = [MTLCaptureManager sharedCaptureManager];
    // Have a custom capture scope as well which then shows up in XCode as
    // an option when capturing, and becomes especially useful when having
    // multiple windows with multiple QRhis.
    d->captureScope = [d->captureMgr newCaptureScopeWithCommandQueue: d->cmdQueue];
    const QString label = QString::asprintf("Qt capture scope for QRhi %p", this);
    d->captureScope.label = label.toNSString();

#if defined(Q_OS_MACOS) || defined(Q_OS_VISIONOS)
    caps.maxTextureSize = 16384;
    caps.baseVertexAndInstance = true;
    caps.isAppleGPU = [d->dev supportsFamily:MTLGPUFamilyApple7];
    caps.maxThreadGroupSize = 1024;
    caps.multiView = true;
#elif defined(Q_OS_TVOS)
    if ([d->dev supportsFamily:MTLGPUFamilyApple3])
        caps.maxTextureSize = 16384;
    else
        caps.maxTextureSize = 8192;
    caps.baseVertexAndInstance = false;
    caps.isAppleGPU = true;
#elif defined(Q_OS_IOS)
    if ([d->dev supportsFamily:MTLGPUFamilyApple3]) {
        caps.maxTextureSize = 16384;
        caps.baseVertexAndInstance = true;
    } else if ([d->dev supportsFamily:MTLGPUFamilyApple2]) {
        caps.maxTextureSize = 8192;
        caps.baseVertexAndInstance = false;
    } else {
        caps.maxTextureSize = 4096;
        caps.baseVertexAndInstance = false;
    }
    caps.isAppleGPU = true;
    if ([d->dev supportsFamily:MTLGPUFamilyApple4])
        caps.maxThreadGroupSize = 1024;
    if ([d->dev supportsFamily:MTLGPUFamilyApple5])
        caps.multiView = true;
#endif

    caps.supportedSampleCounts = { 1 };
    for (int sampleCount : { 2, 4, 8 }) {
        if ([d->dev supportsTextureSampleCount: sampleCount])
            caps.supportedSampleCounts.append(sampleCount);
    }

    caps.indirectCommandBuffers = ([d->dev supportsFamily:MTLGPUFamilyApple5]
        || [d->dev supportsFamily:MTLGPUFamilyMac2])
        && [d->dev supportsFamily:MTLGPUFamilyMetal3];

    caps.shadingRateMap = [d->dev supportsRasterizationRateMapWithLayerCount: 1];
    if (caps.shadingRateMap && caps.multiView)
        caps.shadingRateMap = [d->dev supportsRasterizationRateMapWithLayerCount: 2];

    // QTBUG-144444: setDepthClipMode is not available on the Simulator
    caps.depthClamp = [d->dev supportsFamily:MTLGPUFamilyApple3];

    if (rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave))
        d->setupBinaryArchive();

    nativeHandlesStruct.dev = (MTLDevice *) d->dev;
    nativeHandlesStruct.cmdQueue = (MTLCommandQueue *) d->cmdQueue;

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 698
inline void QRhiMetal::destroy()
{
    executeDeferredReleases(true);
    finishActiveReadbacks(true);

    for (QMetalShader &s : d->shaderCache)
        s.destroy();
    d->shaderCache.clear();

    [d->captureScope release];
    d->captureScope = nil;

    [d->icbArgumentBuffer release];
    d->icbArgumentBuffer = nil;

    [d->icbEncodeFunctionU32 release];
    d->icbEncodeFunctionU32 = nil;

    [d->icbEncodeFunctionU16 release];
    d->icbEncodeFunctionU16 = nil;

    [d->icbEncodePipelineU32 release];
    d->icbEncodePipelineU32 = nil;

    [d->icbEncodePipelineU16 release];
    d->icbEncodePipelineU16 = nil;

    [d->icb release];
    d->icb = nil;

    d->icbCapacity = 0;

    [d->binArch release];
    d->binArch = nil;

    [d->cmdQueue release];
    if (!importedCmdQueue)
        d->cmdQueue = nil;

    [d->dev release];
    if (!importedDevice)
        d->dev = nil;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 742
inline QVector<int> QRhiMetal::supportedSampleCounts() const
{
    return caps.supportedSampleCounts;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 747
inline QVector<QSize> QRhiMetal::supportedShadingRates(int sampleCount) const
{
    Q_UNUSED(sampleCount);
    return { QSize(1, 1) };
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 753
inline QRhiSwapChain *QRhiMetal::createSwapChain()
{
    return new QMetalSwapChain(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 758
inline QRhiBuffer *QRhiMetal::createBuffer(QRhiBuffer::Type type, QRhiBuffer::UsageFlags usage, quint32 size)
{
    return new QMetalBuffer(this, type, usage, size);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 763
inline int QRhiMetal::ubufAlignment() const
{
    return 256;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 768
inline bool QRhiMetal::isYUpInFramebuffer() const
{
    return false;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 773
inline bool QRhiMetal::isYUpInNDC() const
{
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 778
inline bool QRhiMetal::isClipDepthZeroToOne() const
{
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 783
inline QMatrix4x4 QRhiMetal::clipSpaceCorrMatrix() const
{
    // depth range 0..1
    static QMatrix4x4 m;
    if (m.isIdentity()) {
        // NB the ctor takes row-major
        m = QMatrix4x4(1.0f, 0.0f, 0.0f, 0.0f,
                       0.0f, 1.0f, 0.0f, 0.0f,
                       0.0f, 0.0f, 0.5f, 0.5f,
                       0.0f, 0.0f, 0.0f, 1.0f);
    }
    return m;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 797
inline bool QRhiMetal::isTextureFormatSupported(QRhiTexture::Format format, QRhiTexture::Flags flags) const
{
    Q_UNUSED(flags);

    bool supportsFamilyMac2 = false; // needed for BC* formats
    bool supportsFamilyApple3 = false;

#ifdef Q_OS_MACOS
    supportsFamilyMac2 = true;
    if (caps.isAppleGPU)
        supportsFamilyApple3 = true;
#else
    supportsFamilyApple3 = true;
#endif

    // BC5 is not available for any Apple hardare
    if (format == QRhiTexture::BC5)
        return false;

    if (!supportsFamilyApple3) {
        if (format >= QRhiTexture::ETC2_RGB8 && format <= QRhiTexture::ETC2_RGBA8)
            return false;
        if (format >= QRhiTexture::ASTC_4x4 && format <= QRhiTexture::ASTC_12x12)
            return false;
    }

    if (!supportsFamilyMac2)
        if (format >= QRhiTexture::BC1 && format <= QRhiTexture::BC7)
            return false;

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 830
inline bool QRhiMetal::isFeatureSupported(QRhi::Feature feature) const
{
    switch (feature) {
    case QRhi::MultisampleTexture:
        return true;
    case QRhi::MultisampleRenderBuffer:
        return true;
    case QRhi::DebugMarkers:
        return true;
    case QRhi::Timestamps:
        return true;
    case QRhi::Instancing:
        return true;
    case QRhi::CustomInstanceStepRate:
        return true;
    case QRhi::PrimitiveRestart:
        return true;
    case QRhi::NonDynamicUniformBuffers:
        return true;
    case QRhi::NonFourAlignedEffectiveIndexBufferOffset:
        return false;
    case QRhi::NPOTTextureRepeat:
        return true;
    case QRhi::RedOrAlpha8IsRed:
        return true;
    case QRhi::ElementIndexUint:
        return true;
    case QRhi::Compute:
        return true;
    case QRhi::WideLines:
        return false;
    case QRhi::VertexShaderPointSize:
        return true;
    case QRhi::BaseVertex:
        return caps.baseVertexAndInstance;
    case QRhi::BaseInstance:
        return caps.baseVertexAndInstance;
    case QRhi::TriangleFanTopology:
        return false;
    case QRhi::ReadBackNonUniformBuffer:
        return true;
    case QRhi::ReadBackNonBaseMipLevel:
        return true;
    case QRhi::TexelFetch:
        return true;
    case QRhi::RenderToNonBaseMipLevel:
        return true;
    case QRhi::IntAttributes:
        return true;
    case QRhi::ScreenSpaceDerivatives:
        return true;
    case QRhi::ReadBackAnyTextureFormat:
        return true;
    case QRhi::PipelineCacheDataLoadSave:
        return true;
    case QRhi::ImageDataStride:
        return true;
    case QRhi::RenderBufferImport:
        return false;
    case QRhi::ThreeDimensionalTextures:
        return true;
    case QRhi::RenderTo3DTextureSlice:
        return true;
    case QRhi::TextureArrays:
        return true;
    case QRhi::Tessellation:
        return true;
    case QRhi::GeometryShader:
        return false;
    case QRhi::TextureArrayRange:
        return false;
    case QRhi::NonFillPolygonMode:
        return true;
    case QRhi::OneDimensionalTextures:
        return true;
    case QRhi::OneDimensionalTextureMipmaps:
        return false;
    case QRhi::HalfAttributes:
        return true;
    case QRhi::RenderToOneDimensionalTexture:
        return false;
    case QRhi::ThreeDimensionalTextureMipmaps:
        return true;
    case QRhi::MultiView:
        return caps.multiView;
    case QRhi::TextureViewFormat:
        return false;
    case QRhi::ResolveDepthStencil:
        return true;
    case QRhi::VariableRateShading:
        return false;
    case QRhi::VariableRateShadingMap:
        return caps.shadingRateMap;
    case QRhi::VariableRateShadingMapWithTexture:
        return false;
    case QRhi::PerRenderTargetBlending:
    case QRhi::SampleVariables:
        return true;
    case QRhi::InstanceIndexIncludesBaseInstance:
        return true;
    case QRhi::DepthClamp:
        return caps.depthClamp;
    case QRhi::DrawIndirect:
        return true;
    case QRhi::DrawIndirectMulti:
    case QRhi::ShaderDrawParameters:
        return false;
    default:
        Q_UNREACHABLE();
        return false;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 943
inline int QRhiMetal::resourceLimit(QRhi::ResourceLimit limit) const
{
    switch (limit) {
    case QRhi::TextureSizeMin:
        return 1;
    case QRhi::TextureSizeMax:
        return caps.maxTextureSize;
    case QRhi::MaxColorAttachments:
        return 8;
    case QRhi::FramesInFlight:
        return QMTL_FRAMES_IN_FLIGHT;
    case QRhi::MaxAsyncReadbackFrames:
        return QMTL_FRAMES_IN_FLIGHT;
    case QRhi::MaxThreadGroupsPerDimension:
        return 65535;
    case QRhi::MaxThreadsPerThreadGroup:
        Q_FALLTHROUGH();
    case QRhi::MaxThreadGroupX:
        Q_FALLTHROUGH();
    case QRhi::MaxThreadGroupY:
        Q_FALLTHROUGH();
    case QRhi::MaxThreadGroupZ:
        return caps.maxThreadGroupSize;
    case QRhi::TextureArraySizeMax:
        return 2048;
    case QRhi::MaxUniformBufferRange:
        return 65536;
    case QRhi::MaxVertexInputs:
        return 31;
    case QRhi::MaxVertexOutputs:
        return 15; // use the minimum from MTLGPUFamily1/2/3
    case QRhi::ShadingRateImageTileSize:
        return 0;
    default:
        Q_UNREACHABLE();
        return 0;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 982
inline const QRhiNativeHandles *QRhiMetal::nativeHandles()
{
    return &nativeHandlesStruct;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 987
inline QRhiDriverInfo QRhiMetal::driverInfo() const
{
    return driverInfoStruct;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 992
inline QRhiStats QRhiMetal::statistics()
{
    QRhiStats result;
    result.totalPipelineCreationTime = totalPipelineCreationTime();
    return result;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 999
inline bool QRhiMetal::makeThreadLocalNativeContextCurrent()
{
    // not applicable
    return false;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1005
inline void QRhiMetal::setQueueSubmitParams(QRhiNativeHandles *)
{
    // not applicable
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1010
inline void QRhiMetal::releaseCachedResources()
{
    for (QMetalShader &s : d->shaderCache)
        s.destroy();

    d->shaderCache.clear();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1018
inline bool QRhiMetal::isDeviceLost() const
{
    return false;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1033
inline QByteArray QRhiMetal::pipelineCacheData()
{
    Q_STATIC_ASSERT(sizeof(QMetalPipelineCacheDataHeader) == 256);
    QByteArray data;
    if (!d->binArch || !rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave))
        return data;

    QTemporaryFile tmp;
    if (!tmp.open()) {
        qCDebug(QRHI_LOG_INFO, "pipelineCacheData: Failed to create temporary file for Metal");
        return data;
    }
    tmp.close(); // the file exists until the tmp dtor runs

    const QString fn = QFileInfo(tmp.fileName()).absoluteFilePath();
    NSURL *url = QUrl::fromLocalFile(fn).toNSURL();
    NSError *err = nil;
    if (![d->binArch serializeToURL: url error: &err]) {
        const QString msg = QString::fromNSString(err.localizedDescription);
        // Some of these "errors" are not actual errors. (think of "Nothing to serialize")
        qCDebug(QRHI_LOG_INFO, "Failed to serialize MTLBinaryArchive: %s", qPrintable(msg));
        return data;
    }

    QFile f(fn);
    if (!f.open(QIODevice::ReadOnly)) {
        qCDebug(QRHI_LOG_INFO, "pipelineCacheData: Failed to reopen temporary file");
        return data;
    }
    const QByteArray blob = f.readAll();
    f.close();

    const size_t headerSize = sizeof(QMetalPipelineCacheDataHeader);
    const quint32 dataSize = quint32(blob.size());

    data.resize(headerSize + dataSize);

    QMetalPipelineCacheDataHeader header = {};
    header.rhiId = pipelineCacheRhiId();
    header.arch = quint32(sizeof(void*));
    header.dataSize = quint32(dataSize);
    header.osMajor = osMajor;
    header.osMinor = osMinor;
    const size_t driverStrLen = qMin(sizeof(header.driver) - 1, size_t(driverInfoStruct.deviceName.length()));
    if (driverStrLen)
        memcpy(header.driver, driverInfoStruct.deviceName.constData(), driverStrLen);
    header.driver[driverStrLen] = '\0';

    memcpy(data.data(), &header, headerSize);
    memcpy(data.data() + headerSize, blob.constData(), dataSize);
    return data;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1086
inline void QRhiMetal::setPipelineCacheData(const QByteArray &data)
{
    if (data.isEmpty())
        return;

    const size_t headerSize = sizeof(QMetalPipelineCacheDataHeader);
    if (data.size() < qsizetype(headerSize)) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: Invalid blob size (header incomplete)");
        return;
    }

    const size_t dataOffset = headerSize;
    QMetalPipelineCacheDataHeader header;
    memcpy(&header, data.constData(), headerSize);

    const quint32 rhiId = pipelineCacheRhiId();
    if (header.rhiId != rhiId) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: The data is for a different QRhi version or backend (%u, %u)",
                rhiId, header.rhiId);
        return;
    }

    const quint32 arch = quint32(sizeof(void*));
    if (header.arch != arch) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: Architecture does not match (%u, %u)",
                arch, header.arch);
        return;
    }

    if (header.osMajor != osMajor || header.osMinor != osMinor) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: OS version does not match (%u.%u, %u.%u)",
                osMajor, osMinor, header.osMajor, header.osMinor);
        return;
    }

    const size_t driverStrLen = qMin(sizeof(header.driver) - 1, size_t(driverInfoStruct.deviceName.length()));
    if (strncmp(header.driver, driverInfoStruct.deviceName.constData(), driverStrLen)) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: Metal device name does not match");
        return;
    }

    if (quint64(data.size()) < quint64(dataOffset) + header.dataSize) {
        qCDebug(QRHI_LOG_INFO, "setPipelineCacheData: Invalid blob size (data incomplete)");
        return;
    }

    const char *p = data.constData() + dataOffset;

    QTemporaryFile tmp;
    if (!tmp.open()) {
        qCDebug(QRHI_LOG_INFO, "pipelineCacheData: Failed to create temporary file for Metal");
        return;
    }
    tmp.write(p, header.dataSize);
    tmp.close(); // the file exists until the tmp dtor runs

    const QString fn = QFileInfo(tmp.fileName()).absoluteFilePath();
    NSURL *url = QUrl::fromLocalFile(fn).toNSURL();
    if (d->setupBinaryArchive(url))
        qCDebug(QRHI_LOG_INFO, "Created MTLBinaryArchive with initial data of %u bytes", header.dataSize);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1148
inline QRhiRenderBuffer *QRhiMetal::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize &pixelSize,
                                                int sampleCount, QRhiRenderBuffer::Flags flags,
                                                QRhiTexture::Format backingFormatHint)
{
    return new QMetalRenderBuffer(this, type, pixelSize, sampleCount, flags, backingFormatHint);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1155
inline QRhiTexture *QRhiMetal::createTexture(QRhiTexture::Format format,
                                      const QSize &pixelSize, int depth, int arraySize,
                                      int sampleCount, QRhiTexture::Flags flags)
{
    return new QMetalTexture(this, format, pixelSize, depth, arraySize, sampleCount, flags);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1162
inline QRhiSampler *QRhiMetal::createSampler(QRhiSampler::Filter magFilter, QRhiSampler::Filter minFilter,
                                      QRhiSampler::Filter mipmapMode,
                                      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v, QRhiSampler::AddressMode w)
{
    return new QMetalSampler(this, magFilter, minFilter, mipmapMode, u, v, w);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1169
inline QRhiShadingRateMap *QRhiMetal::createShadingRateMap()
{
    return new QMetalShadingRateMap(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1174
inline QRhiTextureRenderTarget *QRhiMetal::createTextureRenderTarget(const QRhiTextureRenderTargetDescription &desc,
                                                              QRhiTextureRenderTarget::Flags flags)
{
    return new QMetalTextureRenderTarget(this, desc, flags);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1180
inline QRhiGraphicsPipeline *QRhiMetal::createGraphicsPipeline()
{
    return new QMetalGraphicsPipeline(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1185
inline QRhiComputePipeline *QRhiMetal::createComputePipeline()
{
    return new QMetalComputePipeline(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1190
inline QRhiShaderResourceBindings *QRhiMetal::createShaderResourceBindings()
{
    return new QMetalShaderResourceBindings(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1350
inline void QRhiMetal::enqueueShaderResourceBindings(QMetalShaderResourceBindings *srbD,
                                              QMetalCommandBuffer *cbD,
                                              int dynamicOffsetCount,
                                              const QRhiCommandBuffer::DynamicOffset *dynamicOffsets,
                                              bool offsetOnlyChange,
                                              const QShader::NativeResourceBindingMap *nativeResourceBindingMaps[SUPPORTED_STAGES])
{
    QMetalShaderResourceBindingsData bindingData;

    for (const QRhiShaderResourceBinding &binding : std::as_const(srbD->sortedBindings)) {
        const QRhiShaderResourceBinding::Data *b = shaderResourceBindingData(binding);
        switch (b->type) {
        case QRhiShaderResourceBinding::UniformBuffer:
        {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, b->u.ubuf.buf);
            id<MTLBuffer> mtlbuf = bufD->d->buf[bufD->d->slotted ? currentFrameSlot : 0];
            quint32 offset = b->u.ubuf.offset;
            for (int i = 0; i < dynamicOffsetCount; ++i) {
                const QRhiCommandBuffer::DynamicOffset &dynOfs(dynamicOffsets[i]);
                if (dynOfs.first == b->binding) {
                    offset = dynOfs.second;
                    break;
                }
            }

            for (int stage = 0; stage < SUPPORTED_STAGES; ++stage) {
                if (b->stage.testFlag(toRhiSrbStage(stage))) {
                    const int nativeBinding = mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Buffer);
                    if (nativeBinding >= 0)
                        bindingData.res[stage].buffers.append({ nativeBinding, mtlbuf, offset });
                }
            }
        }
            break;
        case QRhiShaderResourceBinding::SampledTexture:
        case QRhiShaderResourceBinding::Texture:
        case QRhiShaderResourceBinding::Sampler:
        {
            const QRhiShaderResourceBinding::Data::TextureAndOrSamplerData *data = &b->u.stex;
            for (int elem = 0; elem < data->count; ++elem) {
                QMetalTexture *texD = QRHI_RES(QMetalTexture, b->u.stex.texSamplers[elem].tex);
                QMetalSampler *samplerD = QRHI_RES(QMetalSampler, b->u.stex.texSamplers[elem].sampler);

                for (int stage = 0; stage < SUPPORTED_STAGES; ++stage) {
                    if (b->stage.testFlag(toRhiSrbStage(stage))) {
                        // Must handle all three cases (combined, separate, separate):
                        //   first = texture binding, second = sampler binding
                        //   first = texture binding
                        //   first = sampler binding (i.e. BindingType::Texture...)
                        const int textureBinding = mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Texture);
                        const int samplerBinding = texD && samplerD ? mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Sampler)
                                                                    : (samplerD ? mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Texture) : -1);
                        if (textureBinding >= 0 && texD)
                            bindingData.res[stage].textures.append({ textureBinding + elem, texD->d->tex });
                        if (samplerBinding >= 0)
                            bindingData.res[stage].samplers.append({ samplerBinding + elem, samplerD->d->samplerState });
                    }
                }
            }
        }
            break;
        case QRhiShaderResourceBinding::ImageLoad:
        case QRhiShaderResourceBinding::ImageStore:
        case QRhiShaderResourceBinding::ImageLoadStore:
        {
            QMetalTexture *texD = QRHI_RES(QMetalTexture, b->u.simage.tex);
            id<MTLTexture> t = texD->d->viewForLevel(b->u.simage.level);

            for (int stage = 0; stage < SUPPORTED_STAGES; ++stage) {
                if (b->stage.testFlag(toRhiSrbStage(stage))) {
                    const int nativeBinding = mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Texture);
                    if (nativeBinding >= 0)
                        bindingData.res[stage].textures.append({ nativeBinding, t });
                }
            }
        }
            break;
        case QRhiShaderResourceBinding::BufferLoad:
        case QRhiShaderResourceBinding::BufferStore:
        case QRhiShaderResourceBinding::BufferLoadStore:
        {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, b->u.sbuf.buf);
            id<MTLBuffer> mtlbuf = bufD->d->buf[0];
            quint32 offset = b->u.sbuf.offset;
            for (int stage = 0; stage < SUPPORTED_STAGES; ++stage) {
                if (b->stage.testFlag(toRhiSrbStage(stage))) {
                    const int nativeBinding = mapBinding(b->binding, stage, nativeResourceBindingMaps, BindingType::Buffer);
                    if (nativeBinding >= 0)
                        bindingData.res[stage].buffers.append({ nativeBinding, mtlbuf, offset });
                }
            }
        }
            break;
        default:
            Q_UNREACHABLE();
            break;
        }
    }

    for (int stage = 0; stage < SUPPORTED_STAGES; ++stage) {
        if (cbD->recordingPass != QMetalCommandBuffer::RenderPass && (stage == QMetalShaderResourceBindingsData::VERTEX || stage == QMetalShaderResourceBindingsData::FRAGMENT
                || stage == QMetalShaderResourceBindingsData::TESSCTRL || stage == QMetalShaderResourceBindingsData::TESSEVAL))
            continue;
        if (cbD->recordingPass != QMetalCommandBuffer::ComputePass && (stage == QMetalShaderResourceBindingsData::COMPUTE))
            continue;

        // QRhiBatchedBindings works with the native bindings and expects
        // sorted input. The pre-sorted QRhiShaderResourceBinding list (based
        // on the QRhi (SPIR-V) binding) is not helpful in this regard, so we
        // have to sort here every time.

        std::sort(bindingData.res[stage].buffers.begin(), bindingData.res[stage].buffers.end(), [](const QMetalShaderResourceBindingsData::Stage::Buffer &a, const QMetalShaderResourceBindingsData::Stage::Buffer &b) {
            return a.nativeBinding < b.nativeBinding;
        });

        for (const QMetalShaderResourceBindingsData::Stage::Buffer &buf : std::as_const(bindingData.res[stage].buffers)) {
            bindingData.res[stage].bufferBatches.feed(buf.nativeBinding, buf.mtlbuf);
            bindingData.res[stage].bufferOffsetBatches.feed(buf.nativeBinding, buf.offset);
        }

        bindingData.res[stage].bufferBatches.finish();
        bindingData.res[stage].bufferOffsetBatches.finish();

        for (int i = 0, ie = bindingData.res[stage].bufferBatches.batches.count(); i != ie; ++i) {
            const auto &bufferBatch(bindingData.res[stage].bufferBatches.batches[i]);
            const auto &offsetBatch(bindingData.res[stage].bufferOffsetBatches.batches[i]);
            // skip setting Buffer binding if the current state is already correct
            if (cbD->d->currentShaderResourceBindingState.res[stage].bufferBatches.batches.count() > i
                    && cbD->d->currentShaderResourceBindingState.res[stage].bufferOffsetBatches.batches.count() > i
                    && bufferBatch == cbD->d->currentShaderResourceBindingState.res[stage].bufferBatches.batches[i]
                    && offsetBatch == cbD->d->currentShaderResourceBindingState.res[stage].bufferOffsetBatches.batches[i])
            {
                continue;
            }
            bindStageBuffers(cbD, stage, bufferBatch, offsetBatch);
        }

        if (offsetOnlyChange)
            continue;

        std::sort(bindingData.res[stage].textures.begin(), bindingData.res[stage].textures.end(), [](const QMetalShaderResourceBindingsData::Stage::Texture &a, const QMetalShaderResourceBindingsData::Stage::Texture &b) {
            return a.nativeBinding < b.nativeBinding;
        });

        std::sort(bindingData.res[stage].samplers.begin(), bindingData.res[stage].samplers.end(), [](const QMetalShaderResourceBindingsData::Stage::Sampler &a, const QMetalShaderResourceBindingsData::Stage::Sampler &b) {
            return a.nativeBinding < b.nativeBinding;
        });

        for (const QMetalShaderResourceBindingsData::Stage::Texture &t : std::as_const(bindingData.res[stage].textures))
            bindingData.res[stage].textureBatches.feed(t.nativeBinding, t.mtltex);

        for (const QMetalShaderResourceBindingsData::Stage::Sampler &s : std::as_const(bindingData.res[stage].samplers))
            bindingData.res[stage].samplerBatches.feed(s.nativeBinding, s.mtlsampler);

        bindingData.res[stage].textureBatches.finish();
        bindingData.res[stage].samplerBatches.finish();

        for (int i = 0, ie = bindingData.res[stage].textureBatches.batches.count(); i != ie; ++i) {
            const auto &batch(bindingData.res[stage].textureBatches.batches[i]);
            // skip setting Texture binding if the current state is already correct
            if (cbD->d->currentShaderResourceBindingState.res[stage].textureBatches.batches.count() > i
                    && batch == cbD->d->currentShaderResourceBindingState.res[stage].textureBatches.batches[i])
            {
                continue;
            }
            bindStageTextures(cbD, stage, batch);
        }

        for (int i = 0, ie = bindingData.res[stage].samplerBatches.batches.count(); i != ie; ++i) {
            const auto &batch(bindingData.res[stage].samplerBatches.batches[i]);
            // skip setting Sampler State if the current state is already correct
            if (cbD->d->currentShaderResourceBindingState.res[stage].samplerBatches.batches.count() > i
                && batch == cbD->d->currentShaderResourceBindingState.res[stage].samplerBatches.batches[i])
            {
                continue;
            }
            bindStageSamplers(cbD, stage, batch);
        }
    }

    cbD->d->currentShaderResourceBindingState = bindingData;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1533
inline void QMetalGraphicsPipeline::makeActiveForCurrentRenderPassEncoder(QMetalCommandBuffer *cbD)
{
    QRHI_RES_RHI(QRhiMetal);

    // Also update the tracked state, so that the callers that reactivate a
    // pipeline on a new encoder after interrupting the pass do not have to.
    cbD->currentGraphicsPipeline = this;
    cbD->currentComputePipeline = nullptr;
    cbD->currentPipelineGeneration = generation;

    [cbD->d->currentRenderPassEncoder setRenderPipelineState: d->ps];

    if (cbD->d->currentDepthStencilState != d->ds) {
        [cbD->d->currentRenderPassEncoder setDepthStencilState: d->ds];
        cbD->d->currentDepthStencilState = d->ds;
    }
    if (cbD->currentCullMode == -1 || d->cullMode != uint(cbD->currentCullMode)) {
        [cbD->d->currentRenderPassEncoder setCullMode: d->cullMode];
        cbD->currentCullMode = int(d->cullMode);
    }
    if (cbD->currentTriangleFillMode == -1 || d->triangleFillMode != uint(cbD->currentTriangleFillMode)) {
        [cbD->d->currentRenderPassEncoder setTriangleFillMode: d->triangleFillMode];
        cbD->currentTriangleFillMode = int(d->triangleFillMode);
    }
    if (rhiD->caps.depthClamp) {
        if (cbD->currentDepthClipMode == -1 || d->depthClipMode != uint(cbD->currentDepthClipMode)) {
            [cbD->d->currentRenderPassEncoder setDepthClipMode: d->depthClipMode];
            cbD->currentDepthClipMode = int(d->depthClipMode);
        }
    }
    if (cbD->currentFrontFaceWinding == -1 || d->winding != uint(cbD->currentFrontFaceWinding)) {
        [cbD->d->currentRenderPassEncoder setFrontFacingWinding: d->winding];
        cbD->currentFrontFaceWinding = int(d->winding);
    }
    if (!qFuzzyCompare(d->depthBias, cbD->currentDepthBiasValues.first)
            || !qFuzzyCompare(d->slopeScaledDepthBias, cbD->currentDepthBiasValues.second))
    {
        [cbD->d->currentRenderPassEncoder setDepthBias: d->depthBias
                                                        slopeScale: d->slopeScaledDepthBias
                                                        clamp: 0.0f];
        cbD->currentDepthBiasValues = { d->depthBias, d->slopeScaledDepthBias };
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1577
inline void QRhiMetal::setGraphicsPipeline(QRhiCommandBuffer *cb, QRhiGraphicsPipeline *ps)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);
    QMetalGraphicsPipeline *psD = QRHI_RES(QMetalGraphicsPipeline, ps);

    if (cbD->currentGraphicsPipeline == psD && cbD->currentPipelineGeneration == psD->generation)
        return;

    cbD->currentGraphicsPipeline = psD;
    cbD->currentComputePipeline = nullptr;
    cbD->currentPipelineGeneration = psD->generation;

    if (cbD->hasCustomScissorSet && !psD->m_flags.testFlag(QRhiGraphicsPipeline::UsesScissor))
        setDefaultScissor(cbD);

    if (!psD->d->tess.enabled && !psD->d->tess.failed)
        psD->makeActiveForCurrentRenderPassEncoder(cbD);

    // mark work buffers that can now be safely reused as reusable
    // NOTE: These are  usually empty unless tessellation or mutiview is used.
    for (QMetalBuffer *workBuf : psD->d->extraBufMgr.deviceLocalWorkBuffers) {
        if (workBuf && workBuf->lastActiveFrameSlot == currentFrameSlot)
            workBuf->lastActiveFrameSlot = -1;
    }
    for (QMetalBuffer *workBuf : psD->d->extraBufMgr.hostVisibleWorkBuffers) {
        if (workBuf && workBuf->lastActiveFrameSlot == currentFrameSlot)
            workBuf->lastActiveFrameSlot = -1;
    }

    psD->lastActiveFrameSlot = currentFrameSlot;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1610
inline void QRhiMetal::setShaderResources(QRhiCommandBuffer *cb, QRhiShaderResourceBindings *srb,
                                   int dynamicOffsetCount,
                                   const QRhiCommandBuffer::DynamicOffset *dynamicOffsets)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass != QMetalCommandBuffer::NoPass);
    QMetalGraphicsPipeline *gfxPsD = cbD->currentGraphicsPipeline;
    QMetalComputePipeline *compPsD = cbD->currentComputePipeline;

    if (!srb) {
        if (gfxPsD)
            srb = gfxPsD->m_shaderResourceBindings;
        else
            srb = compPsD->m_shaderResourceBindings;
    }

    QMetalShaderResourceBindings *srbD = QRHI_RES(QMetalShaderResourceBindings, srb);
    bool hasSlottedResourceInSrb = false;
    bool hasDynamicOffsetInSrb = false;
    bool resNeedsRebind = false;

    bool pipelineChanged = false;
    if (gfxPsD) {
        pipelineChanged = srbD->lastUsedGraphicsPipeline != gfxPsD;
        srbD->lastUsedGraphicsPipeline = gfxPsD;
    } else {
        pipelineChanged = srbD->lastUsedComputePipeline != compPsD;
        srbD->lastUsedComputePipeline = compPsD;
    }

    // SPIRV-Cross buffer size buffers
    // Need to determine storage buffer sizes here as this is the last opportunity for storage
    // buffer bindings (offset, size) to be specified before draw / dispatch call
    const bool needsBufferSizeBuffer = (compPsD && compPsD->d->bufferSizeBuffer) || (gfxPsD && gfxPsD->d->bufferSizeBuffer);
    QMap<QRhiShaderResourceBinding::StageFlag, QMap<int, quint32>> storageBufferSizes;

    // do buffer writes, figure out if we need to rebind, and mark as in-use
    for (int i = 0, ie = srbD->sortedBindings.count(); i != ie; ++i) {
        const QRhiShaderResourceBinding::Data *b = shaderResourceBindingData(srbD->sortedBindings.at(i));
        QMetalShaderResourceBindings::BoundResourceData &bd(srbD->boundResourceData[i]);
        switch (b->type) {
        case QRhiShaderResourceBinding::UniformBuffer:
        {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, b->u.ubuf.buf);
            Q_ASSERT(bufD->m_usage.testFlag(QRhiBuffer::UniformBuffer));
            sanityCheckResourceOwnership(bufD);
            executeBufferHostWritesForCurrentFrame(bufD);
            if (bufD->d->slotted)
                hasSlottedResourceInSrb = true;
            if (b->u.ubuf.hasDynamicOffset)
                hasDynamicOffsetInSrb = true;
            if (bufD->generation != bd.ubuf.generation || bufD->m_id != bd.ubuf.id) {
                resNeedsRebind = true;
                bd.ubuf.id = bufD->m_id;
                bd.ubuf.generation = bufD->generation;
            }
            bufD->lastActiveFrameSlot = currentFrameSlot;
        }
            break;
        case QRhiShaderResourceBinding::SampledTexture:
        case QRhiShaderResourceBinding::Texture:
        case QRhiShaderResourceBinding::Sampler:
        {
            const QRhiShaderResourceBinding::Data::TextureAndOrSamplerData *data = &b->u.stex;
            if (bd.stex.count != data->count) {
                bd.stex.count = data->count;
                resNeedsRebind = true;
            }
            for (int elem = 0; elem < data->count; ++elem) {
                QMetalTexture *texD = QRHI_RES(QMetalTexture, data->texSamplers[elem].tex);
                QMetalSampler *samplerD = QRHI_RES(QMetalSampler, data->texSamplers[elem].sampler);
                Q_ASSERT(texD || samplerD);
                sanityCheckResourceOwnership(texD);
                sanityCheckResourceOwnership(samplerD);
                const quint64 texId = texD ? texD->m_id : 0;
                const uint texGen = texD ? texD->generation : 0;
                const quint64 samplerId = samplerD ? samplerD->m_id : 0;
                const uint samplerGen = samplerD ? samplerD->generation : 0;
                if (texGen != bd.stex.d[elem].texGeneration
                        || texId != bd.stex.d[elem].texId
                        || samplerGen != bd.stex.d[elem].samplerGeneration
                        || samplerId != bd.stex.d[elem].samplerId)
                {
                    resNeedsRebind = true;
                    bd.stex.d[elem].texId = texId;
                    bd.stex.d[elem].texGeneration = texGen;
                    bd.stex.d[elem].samplerId = samplerId;
                    bd.stex.d[elem].samplerGeneration = samplerGen;
                }
                if (texD)
                    texD->lastActiveFrameSlot = currentFrameSlot;
                if (samplerD)
                    samplerD->lastActiveFrameSlot = currentFrameSlot;
            }
        }
            break;
        case QRhiShaderResourceBinding::ImageLoad:
        case QRhiShaderResourceBinding::ImageStore:
        case QRhiShaderResourceBinding::ImageLoadStore:
        {
            QMetalTexture *texD = QRHI_RES(QMetalTexture, b->u.simage.tex);
            sanityCheckResourceOwnership(texD);
            if (texD->generation != bd.simage.generation || texD->m_id != bd.simage.id) {
                resNeedsRebind = true;
                bd.simage.id = texD->m_id;
                bd.simage.generation = texD->generation;
            }
            texD->lastActiveFrameSlot = currentFrameSlot;
        }
            break;
        case QRhiShaderResourceBinding::BufferLoad:
        case QRhiShaderResourceBinding::BufferStore:
        case QRhiShaderResourceBinding::BufferLoadStore:
        {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, b->u.sbuf.buf);
            Q_ASSERT(bufD->m_usage.testFlag(QRhiBuffer::StorageBuffer));
            sanityCheckResourceOwnership(bufD);

            if (needsBufferSizeBuffer) {
                for (int i = 0; i < 6; ++i) {
                    const QRhiShaderResourceBinding::StageFlag stage =
                            QRhiShaderResourceBinding::StageFlag(1 << i);
                    if (b->stage.testFlag(stage)) {
                        storageBufferSizes[stage][b->binding] = b->u.sbuf.maybeSize ? b->u.sbuf.maybeSize : bufD->size();
                    }
                }
            }

            executeBufferHostWritesForCurrentFrame(bufD);
            if (bufD->generation != bd.sbuf.generation || bufD->m_id != bd.sbuf.id) {
                resNeedsRebind = true;
                bd.sbuf.id = bufD->m_id;
                bd.sbuf.generation = bufD->generation;
            }
            bufD->lastActiveFrameSlot = currentFrameSlot;
        }
            break;
        default:
            Q_UNREACHABLE();
            break;
        }
    }

    if (needsBufferSizeBuffer) {
        QMetalBuffer *bufD = nullptr;
        QVarLengthArray<std::pair<QMetalShader *, QRhiShaderResourceBinding::StageFlag>, 4> shaders;

        if (compPsD) {
            bufD = compPsD->d->bufferSizeBuffer;
            Q_ASSERT(compPsD->d->cs.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding));
            shaders.append({&compPsD->d->cs, QRhiShaderResourceBinding::StageFlag::ComputeStage});
        } else {
            bufD = gfxPsD->d->bufferSizeBuffer;
            if (gfxPsD->d->tess.enabled) {

                // Assumptions
                // * We only use one of the compute vertex shader variants in a pipeline at any one time
                // * The vertex shader variants all have the same storage block bindings
                // * The vertex shader variants all have the same native resource binding map
                // * The vertex shader variants all have the same MslBufferSizeBufferBinding requirement
                // * The vertex shader variants all have the same MslBufferSizeBufferBinding binding
                // => We only need to use one vertex shader variant to generate the identical shader
                // resource bindings
                Q_ASSERT(gfxPsD->d->tess.compVs[0].desc.storageBlocks() == gfxPsD->d->tess.compVs[1].desc.storageBlocks());
                Q_ASSERT(gfxPsD->d->tess.compVs[0].desc.storageBlocks() == gfxPsD->d->tess.compVs[2].desc.storageBlocks());
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeResourceBindingMap == gfxPsD->d->tess.compVs[1].nativeResourceBindingMap);
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeResourceBindingMap == gfxPsD->d->tess.compVs[2].nativeResourceBindingMap);
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding)
                         == gfxPsD->d->tess.compVs[1].nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding));
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding)
                         == gfxPsD->d->tess.compVs[2].nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding));
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding]
                         == gfxPsD->d->tess.compVs[1].nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding]);
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding]
                         == gfxPsD->d->tess.compVs[2].nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding]);

                if (gfxPsD->d->tess.compVs[0].nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding))
                    shaders.append({&gfxPsD->d->tess.compVs[0], QRhiShaderResourceBinding::StageFlag::VertexStage});

                if (gfxPsD->d->tess.compTesc.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding))
                    shaders.append({&gfxPsD->d->tess.compTesc, QRhiShaderResourceBinding::StageFlag::TessellationControlStage});

                if (gfxPsD->d->tess.vertTese.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding))
                    shaders.append({&gfxPsD->d->tess.vertTese, QRhiShaderResourceBinding::StageFlag::TessellationEvaluationStage});

            } else {
                if (gfxPsD->d->vs.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding))
                    shaders.append({&gfxPsD->d->vs, QRhiShaderResourceBinding::StageFlag::VertexStage});
            }
            if (gfxPsD->d->fs.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding))
                shaders.append({&gfxPsD->d->fs, QRhiShaderResourceBinding::StageFlag::FragmentStage});
        }

        quint32 offset = 0;
        for (const auto &shader : shaders) {

            const int binding = shader.first->nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding];

            // if we don't have a srb entry for the buffer size buffer
            if (!(storageBufferSizes.contains(shader.second) && storageBufferSizes[shader.second].contains(binding))) {

                int maxNativeBinding = 0;
                for (const QShaderDescription::StorageBlock &block : shader.first->desc.storageBlocks())
                    maxNativeBinding = qMax(maxNativeBinding, shader.first->nativeResourceBindingMap[block.binding].first);

                const int size = (maxNativeBinding + 1) * sizeof(int);

                Q_ASSERT(offset + size <= bufD->size());
                srbD->sortedBindings.append(QRhiShaderResourceBinding::bufferLoad(binding, shader.second, bufD, offset, size));

                QMetalShaderResourceBindings::BoundResourceData bd;
                bd.sbuf.id = bufD->m_id;
                bd.sbuf.generation = bufD->generation;
                srbD->boundResourceData.append(bd);
            }

            // create the buffer size buffer data
            QVarLengthArray<int, 8> bufferSizeBufferData;
            Q_ASSERT(storageBufferSizes.contains(shader.second));
            const QMap<int, quint32> &sizes(storageBufferSizes[shader.second]);
            for (const QShaderDescription::StorageBlock &block : shader.first->desc.storageBlocks()) {
                const int index = shader.first->nativeResourceBindingMap[block.binding].first;

                // if the native binding is -1, the buffer is present but not accessed in the shader
                if (index < 0)
                    continue;

                if (bufferSizeBufferData.size() <= index)
                    bufferSizeBufferData.resize(index + 1);

                Q_ASSERT(sizes.contains(block.binding));
                bufferSizeBufferData[index] = sizes[block.binding];
            }

            QRhiBufferData data;
            const quint32 size = bufferSizeBufferData.size() * sizeof(int);
            data.assign(reinterpret_cast<const char *>(bufferSizeBufferData.constData()), size);
            Q_ASSERT(offset + size <= bufD->size());
            bufD->d->pendingUpdates[bufD->d->slotted ? currentFrameSlot : 0].append({ offset, data });

            // buffer offsets must be 32byte aligned
            offset += ((size + 31) / 32) * 32;
        }

        executeBufferHostWritesForCurrentFrame(bufD);
        bufD->lastActiveFrameSlot = currentFrameSlot;
    }

    // make sure the resources for the correct slot get bound
    const int resSlot = hasSlottedResourceInSrb ? currentFrameSlot : 0;
    if (hasSlottedResourceInSrb && cbD->currentResSlot != resSlot)
        resNeedsRebind = true;

    const bool srbChanged = gfxPsD ? (cbD->currentGraphicsSrb != srbD) : (cbD->currentComputeSrb != srbD);
    const bool srbRebuilt = cbD->currentSrbGeneration != srbD->generation;

    // dynamic uniform buffer offsets always trigger a rebind
    if (hasDynamicOffsetInSrb || resNeedsRebind || srbChanged || srbRebuilt || pipelineChanged) {
        const QShader::NativeResourceBindingMap *resBindMaps[SUPPORTED_STAGES] = { nullptr, nullptr, nullptr, nullptr, nullptr };
        if (gfxPsD) {
            cbD->currentGraphicsSrb = srbD;
            cbD->currentComputeSrb = nullptr;
            if (gfxPsD->d->tess.enabled) {
                // If tessellating, we don't know which compVs shader to use until the draw call is
                // made. They should all have the same native resource binding map, so pick one.
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeResourceBindingMap == gfxPsD->d->tess.compVs[1].nativeResourceBindingMap);
                Q_ASSERT(gfxPsD->d->tess.compVs[0].nativeResourceBindingMap == gfxPsD->d->tess.compVs[2].nativeResourceBindingMap);
                resBindMaps[QMetalShaderResourceBindingsData::VERTEX] = &gfxPsD->d->tess.compVs[0].nativeResourceBindingMap;
                resBindMaps[QMetalShaderResourceBindingsData::TESSCTRL] = &gfxPsD->d->tess.compTesc.nativeResourceBindingMap;
                resBindMaps[QMetalShaderResourceBindingsData::TESSEVAL] = &gfxPsD->d->tess.vertTese.nativeResourceBindingMap;
            } else {
                resBindMaps[QMetalShaderResourceBindingsData::VERTEX] = &gfxPsD->d->vs.nativeResourceBindingMap;
            }
            resBindMaps[QMetalShaderResourceBindingsData::FRAGMENT] = &gfxPsD->d->fs.nativeResourceBindingMap;
        } else {
            cbD->currentGraphicsSrb = nullptr;
            cbD->currentComputeSrb = srbD;
            resBindMaps[QMetalShaderResourceBindingsData::COMPUTE] = &compPsD->d->cs.nativeResourceBindingMap;
        }
        cbD->currentSrbGeneration = srbD->generation;
        cbD->currentResSlot = resSlot;

        const bool offsetOnlyChange = hasDynamicOffsetInSrb && !resNeedsRebind
                && !srbChanged && !srbRebuilt && !pipelineChanged;
        enqueueShaderResourceBindings(srbD, cbD, dynamicOffsetCount, dynamicOffsets, offsetOnlyChange, resBindMaps);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1898
inline void QRhiMetal::setVertexInput(QRhiCommandBuffer *cb,
                               int startBinding, int bindingCount, const QRhiCommandBuffer::VertexInput *bindings,
                               QRhiBuffer *indexBuf, quint32 indexOffset, QRhiCommandBuffer::IndexFormat indexFormat)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    QRhiBatchedBindings<id<MTLBuffer> > buffers;
    QRhiBatchedBindings<NSUInteger> offsets;
    for (int i = 0; i < bindingCount; ++i) {
        QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, bindings[i].first);
        executeBufferHostWritesForCurrentFrame(bufD);
        bufD->lastActiveFrameSlot = currentFrameSlot;
        id<MTLBuffer> mtlbuf = bufD->d->buf[bufD->d->slotted ? currentFrameSlot : 0];
        buffers.feed(startBinding + i, mtlbuf);
        offsets.feed(startBinding + i, bindings[i].second);
    }
    buffers.finish();
    offsets.finish();

    // same binding space for vertex and constant buffers - work it around
    QMetalShaderResourceBindings *srbD = cbD->currentGraphicsSrb;
    // There's nothing guaranteeing setShaderResources() was called before
    // setVertexInput()... but whatever srb will get bound will have to be
    // layout-compatible anyways so maxBinding is the same.
    if (!srbD)
        srbD = QRHI_RES(QMetalShaderResourceBindings, cbD->currentGraphicsPipeline->shaderResourceBindings());
    const int firstVertexBinding = srbD->maxBinding + 1;

    if (firstVertexBinding != cbD->d->currentFirstVertexBinding
            || buffers != cbD->d->currentVertexInputsBuffers
            || offsets != cbD->d->currentVertexInputOffsets)
    {
        cbD->d->currentFirstVertexBinding = firstVertexBinding;
        cbD->d->currentVertexInputsBuffers = buffers;
        cbD->d->currentVertexInputOffsets = offsets;

        for (int i = 0, ie = buffers.batches.count(); i != ie; ++i) {
            const auto &bufferBatch(buffers.batches[i]);
            const auto &offsetBatch(offsets.batches[i]);
            [cbD->d->currentRenderPassEncoder setVertexBuffers:
                bufferBatch.resources.constData()
              offsets: offsetBatch.resources.constData()
              withRange: NSMakeRange(uint(firstVertexBinding) + bufferBatch.startBinding, NSUInteger(bufferBatch.resources.count()))];
        }
    }

    if (indexBuf) {
        QMetalBuffer *ibufD = QRHI_RES(QMetalBuffer, indexBuf);
        executeBufferHostWritesForCurrentFrame(ibufD);
        ibufD->lastActiveFrameSlot = currentFrameSlot;
        cbD->currentIndexBuffer = ibufD;
        cbD->currentIndexOffset = indexOffset;
        cbD->currentIndexFormat = indexFormat;
    } else {
        cbD->currentIndexBuffer = nullptr;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1957
inline void QRhiMetal::setDefaultScissor(QMetalCommandBuffer *cbD)
{
    cbD->hasCustomScissorSet = false;

    const QSize outputSize = cbD->currentTarget->pixelSize();
    std::array<float, 4> vp = cbD->currentViewport.viewport();
    float x = 0, y = 0, w = 0, h = 0;

    if (qFuzzyIsNull(vp[2]) && qFuzzyIsNull(vp[3])) {
        x = 0;
        y = 0;
        w = outputSize.width();
        h = outputSize.height();
    } else {
        // x,y is top-left in MTLScissorRect but bottom-left in QRhiScissor
        qrhi_toTopLeftRenderTargetRect<Bounded>(outputSize, vp, &x, &y, &w, &h);
    }

    MTLScissorRect s;
    s.x = NSUInteger(x);
    s.y = NSUInteger(y);
    s.width = NSUInteger(w);
    s.height = NSUInteger(h);
    [cbD->d->currentRenderPassEncoder setScissorRect: s];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 1983
inline void QRhiMetal::setViewport(QRhiCommandBuffer *cb, const QRhiViewport &viewport)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);
    QSize outputSize = cbD->currentTarget->pixelSize();

    // If we have a shading rate map check and use the output size as given by the "screenSize"
    // call. This is important for the viewport to be correct when using a shading rate map, as
    // the pixel size of the target will likely be smaller then what will be rendered to the output.
    // This is specifically needed for visionOS.
    if (cbD->currentTarget->resourceType() == QRhiResource::TextureRenderTarget) {
        QRhiTextureRenderTarget *rt = static_cast<QRhiTextureRenderTarget *>(cbD->currentTarget);
        if (QRhiShadingRateMap *srm = rt->description().shadingRateMap()) {
            if (id<MTLRasterizationRateMap> rateMap = QRHI_RES(QMetalShadingRateMap, srm)->d->rateMap) {
                auto screenSize = [rateMap screenSize];
                outputSize = QSize(screenSize.width, screenSize.height);
            }
        }
    }

    // x,y is top-left in MTLViewportRect but bottom-left in QRhiViewport
    float x, y, w, h;
    if (!qrhi_toTopLeftRenderTargetRect<UnBounded>(outputSize, viewport.viewport(), &x, &y, &w, &h))
        return;

    MTLViewport vp;
    vp.originX = double(x);
    vp.originY = double(y);
    vp.width = double(w);
    vp.height = double(h);
    vp.znear = double(viewport.minDepth());
    vp.zfar = double(viewport.maxDepth());

    [cbD->d->currentRenderPassEncoder setViewport: vp];

    cbD->currentViewport = viewport;
    if (cbD->currentGraphicsPipeline
        && !cbD->currentGraphicsPipeline->m_flags.testFlag(QRhiGraphicsPipeline::UsesScissor))
    {
        setDefaultScissor(cbD);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2026
inline void QRhiMetal::setScissor(QRhiCommandBuffer *cb, const QRhiScissor &scissor)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);
    Q_ASSERT(!cbD->currentGraphicsPipeline
             || cbD->currentGraphicsPipeline->m_flags.testFlag(QRhiGraphicsPipeline::UsesScissor));
    const QSize outputSize = cbD->currentTarget->pixelSize();

    // x,y is top-left in MTLScissorRect but bottom-left in QRhiScissor
    int x, y, w, h;
    if (!qrhi_toTopLeftRenderTargetRect<Bounded>(outputSize, scissor.scissor(), &x, &y, &w, &h))
        return;

    MTLScissorRect s;
    s.x = NSUInteger(x);
    s.y = NSUInteger(y);
    s.width = NSUInteger(w);
    s.height = NSUInteger(h);

    [cbD->d->currentRenderPassEncoder setScissorRect: s];

    cbD->hasCustomScissorSet = true;
    cbD->currentScissor = scissor;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2051
inline void QRhiMetal::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    [cbD->d->currentRenderPassEncoder setBlendColorRed: c.redF()
      green: c.greenF() blue: c.blueF() alpha: c.alphaF()];

    cbD->hasBlendConstantsSet = true;
    cbD->currentBlendConstants = c;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2063
inline void QRhiMetal::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    [cbD->d->currentRenderPassEncoder setStencilReferenceValue: refValue];

    cbD->hasStencilRefSet = true;
    cbD->currentStencilRef = refValue;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2074
inline void QRhiMetal::setShadingRate(QRhiCommandBuffer *cb, const QSize &coarsePixelSize)
{
    Q_UNUSED(cb);
    Q_UNUSED(coarsePixelSize);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2103
inline void QRhiMetal::finalizeDeferredStoreActions(QMetalCommandBuffer *cbD, bool passIsEnding)
{
    for (const auto &[index, finalAction] : std::as_const(cbD->d->deferredColorStoreActions)) {
        // Also store, not just resolve, when the pass continues on a new
        // encoder afterwards: the multisample contents are needed there.
        const MTLStoreAction action = passIsEnding ? finalAction
                                                   : MTLStoreActionStoreAndMultisampleResolve;
        [cbD->d->currentRenderPassEncoder setColorStoreAction: action atIndex: index];
    }

    if (cbD->d->deferredDepthStoreAction != MTLStoreActionUnknown) {
        const MTLStoreAction action = passIsEnding ? cbD->d->deferredDepthStoreAction
                                                   : MTLStoreActionStoreAndMultisampleResolve;
        [cbD->d->currentRenderPassEncoder setDepthStoreAction: action];
    }
    if (cbD->d->deferredStencilStoreAction != MTLStoreActionUnknown) {
        const MTLStoreAction action = passIsEnding ? cbD->d->deferredStencilStoreAction
                                                   : MTLStoreActionStoreAndMultisampleResolve;
        [cbD->d->currentRenderPassEncoder setStencilStoreAction: action];
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2127
inline void QRhiMetal::interruptRenderPass(QMetalCommandBuffer *cbD)
{
    finalizeDeferredStoreActions(cbD, false);
    [cbD->d->currentRenderPassEncoder endEncoding];
    cbD->d->currentRenderPassEncoder = nil;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2222
inline void QRhiMetal::tessellatedDraw(const TessDrawArgs &args)
{
    QMetalCommandBuffer *cbD = args.cbD;
    QMetalGraphicsPipeline *graphicsPipeline = cbD->currentGraphicsPipeline;
    if (graphicsPipeline->d->tess.failed)
        return;

    const bool indexed = args.type != TessDrawArgs::NonIndexed;
    const quint32 instanceCount = indexed ? args.drawIndexed.instanceCount : args.draw.instanceCount;
    const quint32 vertexOrIndexCount = indexed ? args.drawIndexed.indexCount : args.draw.vertexCount;

    QMetalGraphicsPipelineData::Tessellation &tess(graphicsPipeline->d->tess);
    QMetalGraphicsPipelineData::ExtraBufferManager &extraBufMgr(graphicsPipeline->d->extraBufMgr);
    const quint32 patchCount = tess.patchCountForDrawCall(vertexOrIndexCount, instanceCount);
    QMetalBuffer *vertOutBuf = nullptr;
    QMetalBuffer *tescOutBuf = nullptr;
    QMetalBuffer *tescPatchOutBuf = nullptr;
    QMetalBuffer *tescFactorBuf = nullptr;
    QMetalBuffer *tescParamsBuf = nullptr;
    id<MTLComputeCommandEncoder> vertTescComputeEncoder
            = tempComputeEncoder(this, cbD, cbD->d->tessellationComputeEncoder);
    cbD->d->tessellationComputeEncoder = vertTescComputeEncoder;

    // Step 1: vertex shader (as compute)
    {
        id<MTLComputeCommandEncoder> computeEncoder = vertTescComputeEncoder;
        QShader::Variant shaderVariant = QShader::NonIndexedVertexAsComputeShader;
        if (args.type == TessDrawArgs::U16Indexed)
            shaderVariant = QShader::UInt16IndexedVertexAsComputeShader;
        else if (args.type == TessDrawArgs::U32Indexed)
            shaderVariant = QShader::UInt32IndexedVertexAsComputeShader;
        const int varIndex = QMetalGraphicsPipelineData::Tessellation::vsCompVariantToIndex(shaderVariant);
        id<MTLComputePipelineState> computePipelineState = tess.vsCompPipeline(this, shaderVariant);
        [computeEncoder setComputePipelineState: computePipelineState];

        // Make uniform buffers, textures, and samplers (meant for the
        // vertex stage from the client's point of view) visible in the
        // "vertex as compute" shader
        cbD->d->currentComputePassEncoder = computeEncoder;
        rebindShaderResources(cbD, QMetalShaderResourceBindingsData::VERTEX, QMetalShaderResourceBindingsData::COMPUTE);
        cbD->d->currentComputePassEncoder = nil;

        const QMap<int, int> &ebb(tess.compVs[varIndex].nativeShaderInfo.extraBufferBindings);
        const int outputBufferBinding = ebb.value(QShaderPrivate::MslTessVertTescOutputBufferBinding, -1);
        const int indexBufferBinding = ebb.value(QShaderPrivate::MslTessVertIndicesBufferBinding, -1);

        if (outputBufferBinding >= 0) {
            const quint32 workBufSize = tess.vsCompOutputBufferSize(vertexOrIndexCount, instanceCount);
            vertOutBuf = extraBufMgr.acquireWorkBuffer(this, workBufSize);
            if (!vertOutBuf)
                return;
            [computeEncoder setBuffer: vertOutBuf->d->buf[0] offset: 0 atIndex: outputBufferBinding];
        }

        if (indexBufferBinding >= 0)
            [computeEncoder setBuffer: (id<MTLBuffer>) args.drawIndexed.indexBuffer offset: 0 atIndex: indexBufferBinding];

        for (int i = 0, ie = cbD->d->currentVertexInputsBuffers.batches.count(); i != ie; ++i) {
            const auto &bufferBatch(cbD->d->currentVertexInputsBuffers.batches[i]);
            const auto &offsetBatch(cbD->d->currentVertexInputOffsets.batches[i]);
            [computeEncoder setBuffers: bufferBatch.resources.constData()
              offsets: offsetBatch.resources.constData()
              withRange: NSMakeRange(uint(cbD->d->currentFirstVertexBinding) + bufferBatch.startBinding, NSUInteger(bufferBatch.resources.count()))];
        }

        if (indexed) {
            [computeEncoder setStageInRegion: MTLRegionMake2D(args.drawIndexed.vertexOffset, args.drawIndexed.firstInstance,
                                                              args.drawIndexed.indexCount, args.drawIndexed.instanceCount)];
        } else {
            [computeEncoder setStageInRegion: MTLRegionMake2D(args.draw.firstVertex, args.draw.firstInstance,
                                                              args.draw.vertexCount, args.draw.instanceCount)];
        }

        [computeEncoder dispatchThreads: MTLSizeMake(vertexOrIndexCount, instanceCount, 1)
          threadsPerThreadgroup: MTLSizeMake(computePipelineState.threadExecutionWidth, 1, 1)];
    }

    // Step 2: tessellation control shader (as compute)
    {
        id<MTLComputeCommandEncoder> computeEncoder = vertTescComputeEncoder;
        id<MTLComputePipelineState> computePipelineState = tess.tescCompPipeline(this);
        [computeEncoder setComputePipelineState: computePipelineState];

        cbD->d->currentComputePassEncoder = computeEncoder;
        rebindShaderResources(cbD, QMetalShaderResourceBindingsData::TESSCTRL, QMetalShaderResourceBindingsData::COMPUTE);
        cbD->d->currentComputePassEncoder = nil;

        const QMap<int, int> &ebb(tess.compTesc.nativeShaderInfo.extraBufferBindings);
        const int outputBufferBinding = ebb.value(QShaderPrivate::MslTessVertTescOutputBufferBinding, -1);
        const int patchOutputBufferBinding = ebb.value(QShaderPrivate::MslTessTescPatchOutputBufferBinding, -1);
        const int tessFactorBufferBinding = ebb.value(QShaderPrivate::MslTessTescTessLevelBufferBinding, -1);
        const int paramsBufferBinding = ebb.value(QShaderPrivate::MslTessTescParamsBufferBinding, -1);
        const int inputBufferBinding = ebb.value(QShaderPrivate::MslTessTescInputBufferBinding, -1);

        if (outputBufferBinding >= 0) {
            const quint32 workBufSize = tess.tescCompOutputBufferSize(patchCount);
            tescOutBuf = extraBufMgr.acquireWorkBuffer(this, workBufSize);
            if (!tescOutBuf)
                return;
            [computeEncoder setBuffer: tescOutBuf->d->buf[0] offset: 0 atIndex: outputBufferBinding];
        }

        if (patchOutputBufferBinding >= 0) {
            const quint32 workBufSize = tess.tescCompPatchOutputBufferSize(patchCount);
            tescPatchOutBuf = extraBufMgr.acquireWorkBuffer(this, workBufSize);
            if (!tescPatchOutBuf)
                return;
            [computeEncoder setBuffer: tescPatchOutBuf->d->buf[0] offset: 0 atIndex: patchOutputBufferBinding];
        }

        if (tessFactorBufferBinding >= 0) {
            tescFactorBuf = extraBufMgr.acquireWorkBuffer(this, patchCount * sizeof(MTLQuadTessellationFactorsHalf));
            [computeEncoder setBuffer: tescFactorBuf->d->buf[0] offset: 0 atIndex: tessFactorBufferBinding];
        }

        if (paramsBufferBinding >= 0) {
            struct {
                quint32 inControlPointCount;
                quint32 patchCount;
            } params;
            tescParamsBuf = extraBufMgr.acquireWorkBuffer(this, sizeof(params), QMetalGraphicsPipelineData::ExtraBufferManager::WorkBufType::HostVisible);
            if (!tescParamsBuf)
                return;
            params.inControlPointCount = tess.inControlPointCount;
            params.patchCount = patchCount;
            id<MTLBuffer> paramsBuf = tescParamsBuf->d->buf[0];
            char *p = reinterpret_cast<char *>([paramsBuf contents]);
            memcpy(p, &params, sizeof(params));
            [computeEncoder setBuffer: paramsBuf offset: 0 atIndex: paramsBufferBinding];
        }

        if (vertOutBuf && inputBufferBinding >= 0)
            [computeEncoder setBuffer: vertOutBuf->d->buf[0] offset: 0 atIndex: inputBufferBinding];

        int sgSize = int(computePipelineState.threadExecutionWidth);
        int wgSize = std::lcm(tess.outControlPointCount, sgSize);
        while (wgSize > caps.maxThreadGroupSize) {
            sgSize /= 2;
            wgSize = std::lcm(tess.outControlPointCount, sgSize);
        }
        [computeEncoder dispatchThreads: MTLSizeMake(patchCount * tess.outControlPointCount, 1, 1)
          threadsPerThreadgroup: MTLSizeMake(wgSize, 1, 1)];
    }

    // Much of the state in the QMetalCommandBuffer is going to be reset
    // when we get a new render encoder. Save what we need. (cheaper than
    // starting to walk over the srb again)
    const QMetalShaderResourceBindingsData resourceBindings = cbD->d->currentShaderResourceBindingState;

    endTempComputeEncoding(this, cbD, cbD->d->tessellationComputeEncoder);
    cbD->d->tessellationComputeEncoder = nil;

    // Step 3: tessellation evaluation (as vertex) + fragment shader
    {
        // No need to call tess.teseFragRenderPipeline because it was done
        // once and we know the result is stored in the standard place
        // (graphicsPipeline->d->ps).

        graphicsPipeline->makeActiveForCurrentRenderPassEncoder(cbD);
        id<MTLRenderCommandEncoder> renderEncoder = cbD->d->currentRenderPassEncoder;

        rebindShaderResources(cbD, QMetalShaderResourceBindingsData::TESSEVAL, QMetalShaderResourceBindingsData::VERTEX, &resourceBindings);
        rebindShaderResources(cbD, QMetalShaderResourceBindingsData::FRAGMENT, QMetalShaderResourceBindingsData::FRAGMENT, &resourceBindings);

        const QMap<int, int> &ebb(tess.compTesc.nativeShaderInfo.extraBufferBindings);
        const int outputBufferBinding = ebb.value(QShaderPrivate::MslTessVertTescOutputBufferBinding, -1);
        const int patchOutputBufferBinding = ebb.value(QShaderPrivate::MslTessTescPatchOutputBufferBinding, -1);
        const int tessFactorBufferBinding = ebb.value(QShaderPrivate::MslTessTescTessLevelBufferBinding, -1);

        if (outputBufferBinding >= 0 && tescOutBuf)
            [renderEncoder setVertexBuffer: tescOutBuf->d->buf[0] offset: 0 atIndex: outputBufferBinding];

        if (patchOutputBufferBinding >= 0 && tescPatchOutBuf)
            [renderEncoder setVertexBuffer: tescPatchOutBuf->d->buf[0] offset: 0 atIndex: patchOutputBufferBinding];

        if (tessFactorBufferBinding >= 0 && tescFactorBuf) {
            [renderEncoder setTessellationFactorBuffer: tescFactorBuf->d->buf[0] offset: 0 instanceStride: 0];
            [renderEncoder setVertexBuffer: tescFactorBuf->d->buf[0] offset: 0 atIndex: tessFactorBufferBinding];
        }

        [cbD->d->currentRenderPassEncoder drawPatches: tess.outControlPointCount
                                                       patchStart: 0
                                                       patchCount: patchCount
                                                       patchIndexBuffer: nil
                                                       patchIndexBufferOffset: 0
                                                       instanceCount: 1
                                                       baseInstance: 0];
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2412
inline void QRhiMetal::adjustForMultiViewDraw(quint32 *instanceCount, QRhiCommandBuffer *cb)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    const int multiViewCount = cbD->currentGraphicsPipeline->m_multiViewCount;
    if (multiViewCount <= 1)
        return;

    const QMap<int, int> &ebb(cbD->currentGraphicsPipeline->d->vs.nativeShaderInfo.extraBufferBindings);
    const int viewMaskBufBinding = ebb.value(QShaderPrivate::MslMultiViewMaskBufferBinding, -1);
    if (viewMaskBufBinding == -1) {
        qWarning("No extra buffer for multiview in the vertex shader; was it built with --view-count specified?");
        return;
    }
    struct {
        quint32 viewOffset;
        quint32 viewCount;
    } multiViewInfo;
    multiViewInfo.viewOffset = 0;
    multiViewInfo.viewCount = quint32(multiViewCount);
    QMetalBuffer *buf = cbD->currentGraphicsPipeline->d->extraBufMgr.acquireWorkBuffer(this, sizeof(multiViewInfo),
        QMetalGraphicsPipelineData::ExtraBufferManager::WorkBufType::HostVisible);
    if (buf) {
        id<MTLBuffer> mtlbuf = buf->d->buf[0];
        char *p = reinterpret_cast<char *>([mtlbuf contents]);
        memcpy(p, &multiViewInfo, sizeof(multiViewInfo));
        [cbD->d->currentRenderPassEncoder setVertexBuffer: mtlbuf offset: 0 atIndex: viewMaskBufBinding];
        // The instance count is adjusted for layered rendering. The vertex shader is expected to contain something like:
        // uint gl_ViewIndex = spvViewMask[0] + (gl_InstanceIndex - gl_BaseInstance) % spvViewMask[1];
        // where spvViewMask is the buffer with multiViewInfo passed in above.
        *instanceCount *= multiViewCount;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2445
inline void QRhiMetal::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
                     quint32 instanceCount, quint32 firstVertex, quint32 firstInstance)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    if (cbD->currentGraphicsPipeline->d->tess.enabled) {
        TessDrawArgs a;
        a.cbD = cbD;
        a.type = TessDrawArgs::NonIndexed;
        a.draw.vertexCount = vertexCount;
        a.draw.instanceCount = instanceCount;
        a.draw.firstVertex = firstVertex;
        a.draw.firstInstance = firstInstance;
        tessellatedDraw(a);
        return;
    }

    adjustForMultiViewDraw(&instanceCount, cb);

    if (caps.baseVertexAndInstance) {
        [cbD->d->currentRenderPassEncoder drawPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
                                                          vertexStart: firstVertex vertexCount: vertexCount instanceCount: instanceCount baseInstance: firstInstance];
    } else {
        [cbD->d->currentRenderPassEncoder drawPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
                                                          vertexStart: firstVertex vertexCount: vertexCount instanceCount: instanceCount];
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2474
inline void QRhiMetal::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
                            quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset, quint32 firstInstance)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    if (!cbD->currentIndexBuffer)
        return;

    const quint32 indexOffset = cbD->currentIndexOffset + firstIndex * (cbD->currentIndexFormat == QRhiCommandBuffer::IndexUInt16 ? 2 : 4);
    Q_ASSERT(indexOffset == aligned(indexOffset, 4u));

    QMetalBuffer *ibufD = cbD->currentIndexBuffer;
    id<MTLBuffer> mtlibuf = ibufD->d->buf[ibufD->d->slotted ? currentFrameSlot : 0];

    if (cbD->currentGraphicsPipeline->d->tess.enabled) {
        TessDrawArgs a;
        a.cbD = cbD;
        a.type = cbD->currentIndexFormat == QRhiCommandBuffer::IndexUInt16 ? TessDrawArgs::U16Indexed : TessDrawArgs::U32Indexed;
        a.drawIndexed.indexCount = indexCount;
        a.drawIndexed.instanceCount = instanceCount;
        a.drawIndexed.firstIndex = firstIndex;
        a.drawIndexed.vertexOffset = vertexOffset;
        a.drawIndexed.firstInstance = firstInstance;
        a.drawIndexed.indexBuffer = mtlibuf;
        tessellatedDraw(a);
        return;
    }

    adjustForMultiViewDraw(&instanceCount, cb);

    if (caps.baseVertexAndInstance) {
        [cbD->d->currentRenderPassEncoder drawIndexedPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
          indexCount: indexCount
          indexType: cbD->currentIndexFormat == QRhiCommandBuffer::IndexUInt16 ? MTLIndexTypeUInt16 : MTLIndexTypeUInt32
          indexBuffer: mtlibuf
          indexBufferOffset: indexOffset
          instanceCount: instanceCount
          baseVertex: vertexOffset
          baseInstance: firstInstance];
    } else {
        [cbD->d->currentRenderPassEncoder drawIndexedPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
          indexCount: indexCount
          indexType: cbD->currentIndexFormat == QRhiCommandBuffer::IndexUInt16 ? MTLIndexTypeUInt16 : MTLIndexTypeUInt32
          indexBuffer: mtlibuf
          indexBufferOffset: indexOffset
          instanceCount: instanceCount];
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2524
inline void QRhiMetal::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                             quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    QMetalBuffer *indirectBufD = QRHI_RES(QMetalBuffer, indirectBuffer);
    executeBufferHostWritesForCurrentFrame(indirectBufD);
    indirectBufD->lastActiveFrameSlot = currentFrameSlot;
    id<MTLBuffer> indirectBufMtl = indirectBufD->d->buf[indirectBufD->d->slotted ? currentFrameSlot : 0];

    NSUInteger offset = indirectBufferOffset;
    for (quint32 i = 0; i < drawCount; ++i) {
        [cbD->d->currentRenderPassEncoder drawPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
          indirectBuffer: indirectBufMtl
          indirectBufferOffset: offset];
        offset += stride;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2544
inline void QRhiMetal::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer *indirectBuffer,
                                    quint32 indirectBufferOffset, quint32 drawCount, quint32 stride)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    if (!cbD->currentIndexBuffer)
        return;

    QMetalBuffer *indexBufD = cbD->currentIndexBuffer;
    id<MTLBuffer> indexBufMtl = indexBufD->d->buf[indexBufD->d->slotted ? currentFrameSlot : 0];

    QMetalBuffer *indirectBufD = QRHI_RES(QMetalBuffer, indirectBuffer);
    executeBufferHostWritesForCurrentFrame(indirectBufD);
    indirectBufD->lastActiveFrameSlot = currentFrameSlot;
    id<MTLBuffer> indirectBufMtl = indirectBufD->d->buf[indirectBufD->d->slotted ? currentFrameSlot : 0];

    // ICB (Indirect Command Buffer) path: uses a GPU compute kernel to encode
    // draw commands into an MTLIndirectCommandBuffer, then executes them in a
    // single executeCommandsInBuffer call. This eliminates per-draw CPU overhead
    // for large batch counts. Requires the pipeline to declare UsesIndirectDraws
    // (which enables supportIndirectCommandBuffers on the Metal pipeline descriptor).

    // The ICB encoding overhead (compute pass + render pass restart)
    // can be around 100-150 microseconds, whereas an individual drawIndexedPrimitives call
    // typically takes 1-2 microseconds. A default threshold of 128 is intended to strike a
    // reasonable crossover balance, aiming to utilize the GPU-driven approach
    // when it is most likely to outweigh the fixed setup cost.
    static const quint32 ICB_DRAW_COUNT_THRESHOLD = 128;
    const bool useIcb = cbD->currentGraphicsPipeline
            && caps.indirectCommandBuffers
            && cbD->currentGraphicsPipeline->m_flags.testFlag(QRhiGraphicsPipeline::UsesIndirectDraws)
            && drawCount > ICB_DRAW_COUNT_THRESHOLD;

    if (useIcb) {
        bool icbOk = true;

        // Lazy-compile MSL compute kernels for ICB encoding (once per QRhi lifetime)
        if (!d->icbEncodePipelineU32) {
            NSError *err = nil;
            NSString *src = [NSString stringWithUTF8String:s_icbEncodeMsl];
            MTLCompileOptions *opts = [MTLCompileOptions new];
            opts.languageVersion = MTLLanguageVersion2_1;
            id<MTLLibrary> lib = [d->dev newLibraryWithSource:src options:opts error:&err];
            [opts release];
            if (!lib) {
                qWarning("Failed to compile ICB encode kernel: %s",
                         qPrintable(QString::fromNSString(err.localizedDescription)));
                icbOk = false;
            }
            if (icbOk) {
                d->icbEncodeFunctionU32 = [lib newFunctionWithName:@"encode_icb_indexed_u32"];
                d->icbEncodeFunctionU16 = [lib newFunctionWithName:@"encode_icb_indexed_u16"];
                [lib release];
                if (!d->icbEncodeFunctionU32 || !d->icbEncodeFunctionU16) {
                    qWarning("ICB encode kernel functions not found");
                    icbOk = false;
                }
            }
            if (icbOk) {
                d->icbEncodePipelineU32 = [d->dev newComputePipelineStateWithFunction:d->icbEncodeFunctionU32 error:&err];
                if (!d->icbEncodePipelineU32) {
                    qWarning("Failed to create ICB encode compute pipeline (u32): %s",
                             qPrintable(QString::fromNSString(err.localizedDescription)));
                    icbOk = false;
                }
            }
            if (icbOk) {
                d->icbEncodePipelineU16 = [d->dev newComputePipelineStateWithFunction:d->icbEncodeFunctionU16 error:&err];
                if (!d->icbEncodePipelineU16) {
                    qWarning("Failed to create ICB encode compute pipeline (u16): %s",
                             qPrintable(QString::fromNSString(err.localizedDescription)));
                    icbOk = false;
                }
            }
        }

        // Ensure ICB has enough capacity (grows on demand, never shrinks).
        // Old ICB resources are deferred-released to avoid use-after-free when
        // a previous frame's compute pass is still in flight (the command buffer
        // uses commandBufferWithUnretainedReferences).
        if (icbOk && (!d->icb || d->icbCapacity < drawCount)) {
            if (d->icb) {
                QRhiMetalData::DeferredReleaseEntry e;
                e.type = QRhiMetalData::DeferredReleaseEntry::StagingIcbBuffer;
                e.lastActiveFrameSlot = currentFrameSlot;
                e.stagingIcbBuffer.icb = d->icb;
                e.stagingIcbBuffer.argBuffer = d->icbArgumentBuffer;
                d->releaseQueue.append(e);
            }
            d->icb = nil;
            d->icbArgumentBuffer = nil;

            MTLIndirectCommandBufferDescriptor *icbDesc = [MTLIndirectCommandBufferDescriptor new];
            icbDesc.commandTypes = MTLIndirectCommandTypeDrawIndexed;
            icbDesc.inheritPipelineState = YES;
            icbDesc.inheritBuffers = YES;
            icbDesc.maxVertexBufferBindCount = 0;
            icbDesc.maxFragmentBufferBindCount = 0;
            d->icb = [d->dev newIndirectCommandBufferWithDescriptor:icbDesc
                                                    maxCommandCount:drawCount
                                                            options:MTLResourceStorageModePrivate];
            [icbDesc release];
            if (!d->icb) {
                qWarning("Failed to create MTLIndirectCommandBuffer");
                d->icbCapacity = 0;
                icbOk = false;
            } else {
                d->icbCapacity = drawCount;

                id<MTLArgumentEncoder> argEnc = [d->icbEncodeFunctionU32 newArgumentEncoderWithBufferIndex:1];
                d->icbArgumentBuffer = [d->dev newBufferWithLength:argEnc.encodedLength
                                                           options:MTLResourceStorageModeShared];
                [argEnc setArgumentBuffer:d->icbArgumentBuffer offset:0];
                [argEnc setIndirectCommandBuffer:d->icb atIndex:0];
                [argEnc release];
            }
        }

        if (icbOk) {
            // Save state before render pass interruption (following tessellation pattern).
            QMetalGraphicsPipeline *savedPipeline = cbD->currentGraphicsPipeline;
            const QMetalShaderResourceBindingsData savedResourceBindings = cbD->d->currentShaderResourceBindingState;
            const int savedFirstVertexBinding = cbD->d->currentFirstVertexBinding;
            const auto savedVertexBuffers = cbD->d->currentVertexInputsBuffers;
            const auto savedVertexOffsets = cbD->d->currentVertexInputOffsets;
            const quint32 savedIndexOffset = cbD->currentIndexOffset;
            const QRhiCommandBuffer::IndexFormat savedIndexFormat = cbD->currentIndexFormat;

            // End the current render encoder to make room for the compute pass.
            interruptRenderPass(cbD);

            // Dispatch compute kernel to encode draw commands into the ICB.
            id<MTLComputeCommandEncoder> computeEncoder;
            {
                const bool useU16 = (savedIndexFormat == QRhiCommandBuffer::IndexUInt16);
                id<MTLComputePipelineState> computePipeline = useU16 ? d->icbEncodePipelineU16 : d->icbEncodePipelineU32;

                computeEncoder = [cbD->d->cb computeCommandEncoder];
                uint32_t drawCountVal = drawCount;
                uint32_t metalPrimType = uint32_t(savedPipeline->d->primitiveType);
                uint32_t strideVal = stride;

                [computeEncoder setComputePipelineState:computePipeline];
                [computeEncoder setBuffer:indirectBufMtl offset:indirectBufferOffset atIndex:0];
                [computeEncoder setBuffer:d->icbArgumentBuffer offset:0 atIndex:1];
                [computeEncoder setBytes:&drawCountVal length:sizeof(uint32_t) atIndex:2];
                [computeEncoder setBuffer:indexBufMtl offset:savedIndexOffset atIndex:3];
                [computeEncoder setBytes:&metalPrimType length:sizeof(uint32_t) atIndex:4];
                [computeEncoder setBytes:&strideVal length:sizeof(uint32_t) atIndex:5];
                [computeEncoder useResource:d->icb usage:MTLResourceUsageWrite];
                [computeEncoder useResource:indirectBufMtl usage:MTLResourceUsageRead];
                [computeEncoder useResource:indexBufMtl usage:MTLResourceUsageRead];

                NSUInteger tw = computePipeline.threadExecutionWidth;
                [computeEncoder dispatchThreads:MTLSizeMake(drawCount, 1, 1)
                          threadsPerThreadgroup:MTLSizeMake(tw, 1, 1)];
            }

            // Restart the render pass with Load actions to preserve existing content.
            endTempComputeEncoding(this, cbD, computeEncoder);

            // Restore pipeline, shader resources, and vertex bindings on the new encoder.
            savedPipeline->makeActiveForCurrentRenderPassEncoder(cbD);
            rebindShaderResources(cbD, QMetalShaderResourceBindingsData::VERTEX,
                                  QMetalShaderResourceBindingsData::VERTEX, &savedResourceBindings);
            rebindShaderResources(cbD, QMetalShaderResourceBindingsData::FRAGMENT,
                                  QMetalShaderResourceBindingsData::FRAGMENT, &savedResourceBindings);

            if (savedFirstVertexBinding >= 0) {
                cbD->d->currentFirstVertexBinding = savedFirstVertexBinding;
                cbD->d->currentVertexInputsBuffers = savedVertexBuffers;
                cbD->d->currentVertexInputOffsets = savedVertexOffsets;
                for (int i = 0, ie = savedVertexBuffers.batches.count(); i != ie; ++i) {
                    const auto &bufferBatch(savedVertexBuffers.batches[i]);
                    const auto &offsetBatch(savedVertexOffsets.batches[i]);
                    [cbD->d->currentRenderPassEncoder setVertexBuffers:
                        bufferBatch.resources.constData()
                      offsets: offsetBatch.resources.constData()
                      withRange: NSMakeRange(uint(savedFirstVertexBinding) + bufferBatch.startBinding,
                                             NSUInteger(bufferBatch.resources.count()))];
                }
            }

            cbD->currentIndexBuffer = indexBufD;
            cbD->currentIndexOffset = savedIndexOffset;
            cbD->currentIndexFormat = savedIndexFormat;

            // Declare buffer dependencies and execute the GPU-encoded ICB.
            [cbD->d->currentRenderPassEncoder useResource:indirectBufMtl
                                                    usage:MTLResourceUsageRead
                                                   stages:MTLRenderStageVertex | MTLRenderStageFragment];
            [cbD->d->currentRenderPassEncoder useResource:indexBufMtl
                                                    usage:MTLResourceUsageRead
                                                   stages:MTLRenderStageVertex | MTLRenderStageFragment];
            [cbD->d->currentRenderPassEncoder executeCommandsInBuffer:d->icb
                                                            withRange:NSMakeRange(0, drawCount)];
            return;
        }
    }

    // CPU-side for-loop fallback: used when ICB is not applicable or setup failed.
    NSUInteger offset = indirectBufferOffset;
    for (quint32 i = 0; i < drawCount; ++i) {
        [cbD->d->currentRenderPassEncoder drawIndexedPrimitives: cbD->currentGraphicsPipeline->d->primitiveType
          indexType: cbD->currentIndexFormat == QRhiCommandBuffer::IndexUInt16 ? MTLIndexTypeUInt16 : MTLIndexTypeUInt32
          indexBuffer: indexBufMtl
          indexBufferOffset: cbD->currentIndexOffset
          indirectBuffer: indirectBufMtl
          indirectBufferOffset: offset];
        offset += stride;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2758
inline void QRhiMetal::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray &name)
{
    if (!debugMarkers)
        return;

    NSString *str = [NSString stringWithUTF8String: name.constData()];
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    if (cbD->recordingPass != QMetalCommandBuffer::NoPass)
        [cbD->d->currentRenderPassEncoder pushDebugGroup: str];
    else
        [cbD->d->cb pushDebugGroup: str];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2771
inline void QRhiMetal::debugMarkEnd(QRhiCommandBuffer *cb)
{
    if (!debugMarkers)
        return;

    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    if (cbD->recordingPass != QMetalCommandBuffer::NoPass)
        [cbD->d->currentRenderPassEncoder popDebugGroup];
    else
        [cbD->d->cb popDebugGroup];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2783
inline void QRhiMetal::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
{
    if (!debugMarkers)
        return;

    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    if (cbD->recordingPass != QMetalCommandBuffer::NoPass)
        [cbD->d->currentRenderPassEncoder insertDebugSignpost: [NSString stringWithUTF8String: msg.constData()]];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2793
inline const QRhiNativeHandles *QRhiMetal::nativeHandles(QRhiCommandBuffer *cb)
{
    return QRHI_RES(QMetalCommandBuffer, cb)->nativeHandles();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2798
inline void QRhiMetal::beginExternal(QRhiCommandBuffer *cb)
{
    Q_UNUSED(cb);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2803
inline void QRhiMetal::endExternal(QRhiCommandBuffer *cb)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    cbD->resetPerPassCachedState();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2809
inline double QRhiMetal::lastCompletedGpuTime(QRhiCommandBuffer *cb)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    return cbD->d->lastGpuTime;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2815
inline QRhi::FrameOpResult QRhiMetal::beginFrame(QRhiSwapChain *swapChain, QRhi::BeginFrameFlags flags)
{
    Q_UNUSED(flags);

    QMetalSwapChain *swapChainD = QRHI_RES(QMetalSwapChain, swapChain);
    currentSwapChain = swapChainD;
    currentFrameSlot = swapChainD->currentFrameSlot;

    // If we are too far ahead, block. This is also what ensures that any
    // resource used in the previous frame for this slot is now not in use
    // anymore by the GPU.
    dispatch_semaphore_wait(swapChainD->d->sem[currentFrameSlot], DISPATCH_TIME_FOREVER);

    // Do this also for any other swapchain's commands with the same frame slot
    // While this reduces concurrency, it keeps resource usage safe: swapchain
    // A starting its frame 0, followed by swapchain B starting its own frame 0
    // will make B wait for A's frame 0 commands, so if a resource is written
    // in B's frame or when B checks for pending resource releases, that won't
    // mess up A's in-flight commands (as they are not in flight anymore).
    for (QMetalSwapChain *sc : std::as_const(swapchains)) {
        if (sc != swapChainD)
            sc->waitUntilCompleted(currentFrameSlot); // wait+signal
    }

    [d->captureScope beginScope];

    swapChainD->cbWrapper.d->cb = d->newCommandBuffer();

    QMetalRenderTargetData::ColorAtt colorAtt;
    if (swapChainD->samples > 1) {
        colorAtt.tex = swapChainD->d->msaaTex[currentFrameSlot];
        colorAtt.needsDrawableForResolveTex = true;
    } else {
        colorAtt.needsDrawableForTex = true;
    }

    swapChainD->rtWrapper.d->fb.colorAtt[0] = colorAtt;
    swapChainD->rtWrapper.d->fb.dsTex = swapChainD->ds ? swapChainD->ds->d->tex : nil;
    swapChainD->rtWrapper.d->fb.dsResolveTex = nil;
    swapChainD->rtWrapper.d->fb.hasStencil = swapChainD->ds ? true : false;
    swapChainD->rtWrapper.d->fb.depthNeedsStore = false;

    if (swapChainD->ds)
        swapChainD->ds->lastActiveFrameSlot = currentFrameSlot;

    executeDeferredReleases();
    swapChainD->cbWrapper.resetState(swapChainD->d->lastGpuTime[currentFrameSlot]);
    swapChainD->d->lastGpuTime[currentFrameSlot] = 0;
    finishActiveReadbacks();

    return QRhi::FrameOpSuccess;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2868
inline QRhi::FrameOpResult QRhiMetal::endFrame(QRhiSwapChain *swapChain, QRhi::EndFrameFlags flags)
{
    QMetalSwapChain *swapChainD = QRHI_RES(QMetalSwapChain, swapChain);
    Q_ASSERT(currentSwapChain == swapChainD);

    // Keep strong reference to command buffer
    id<MTLCommandBuffer> commandBuffer = swapChainD->cbWrapper.d->cb;

    __block int thisFrameSlot = currentFrameSlot;
    [commandBuffer addCompletedHandler: ^(id<MTLCommandBuffer> cb) {
        swapChainD->d->lastGpuTime[thisFrameSlot] += cb.GPUEndTime - cb.GPUStartTime;
        dispatch_semaphore_signal(swapChainD->d->sem[thisFrameSlot]);
    }];

#ifdef QRHI_METAL_COMMAND_BUFFERS_WITH_UNRETAINED_REFERENCES
    // When Metal API validation diagnostics is enabled in Xcode the texture is
    // released before the command buffer is done with it. Manually keep it alive
    // to work around this.
    id<MTLTexture> drawableTexture = [swapChainD->d->curDrawable.texture retain];
    [commandBuffer addCompletedHandler:^(id<MTLCommandBuffer>) {
        [drawableTexture release];
    }];
#endif

    if (flags.testFlag(QRhi::SkipPresent)) {
        // Just need to commit, that's it
        [commandBuffer commit];
    } else {
        if (id<CAMetalDrawable> drawable = swapChainD->d->curDrawable) {
            // Got something to present
            if (swapChainD->d->layer.presentsWithTransaction) {
                [commandBuffer commit];
                // Keep strong reference to Metal layer
                auto *metalLayer = swapChainD->d->layer;
                auto presentWithTransaction = ^{
                    [commandBuffer waitUntilScheduled];
                    // If the layer has been resized while we waited to be scheduled we bail out,
                    // as the drawable is no longer valid for the layer, and we'll get a follow-up
                    // display with the right size. We know we are on the main thread here, which
                    // means we can access the layer directly. We also know that the layer is valid,
                    // since the block keeps a strong reference to it, compared to the QRhiSwapChain
                    // that can go away under our feet by the time we're scheduled.
                    const auto surfaceSize = QSizeF::fromCGSize(metalLayer.bounds.size) * metalLayer.contentsScale;
                    const auto textureSize = QSizeF(drawable.texture.width, drawable.texture.height);
                    if (textureSize == surfaceSize) {
                        [drawable present];
                    } else {
                        qCDebug(QRHI_LOG_INFO) << "Skipping" << drawable << "due to texture size"
                            << textureSize << "not matching surface size" << surfaceSize;
                    }
                };

                if (NSThread.currentThread == NSThread.mainThread) {
                    presentWithTransaction();
                } else {
                    auto *qtMetalLayer = qt_objc_cast<QMetalLayer*>(swapChainD->d->layer);
                    Q_ASSERT(qtMetalLayer);
                    // Let the main thread present the drawable from displayLayer
                    qtMetalLayer.mainThreadPresentation = presentWithTransaction;
                }
            } else {
                // Keep strong reference to Metal layer so it's valid in the block
                auto *qtMetalLayer = qt_objc_cast<QMetalLayer*>(swapChainD->d->layer);
                [commandBuffer addScheduledHandler:^(id<MTLCommandBuffer>) {
                    if (qtMetalLayer) {
                        // The schedule handler comes in on the com.Metal.CompletionQueueDispatch
                        // thread, which means we might be racing against a display cycle on the
                        // main thread. If the displayLayer is already in progress, we don't want
                        // to step on its toes.
                        if (qtMetalLayer.displayLock.tryLockForRead()) {
                            [drawable present];
                            qtMetalLayer.displayLock.unlock();
                        } else {
                            qCDebug(QRHI_LOG_INFO) << "Skipping" << drawable
                                << "due to" << qtMetalLayer << "needing display";
                        }
                    } else {
                        [drawable present];
                    }
                }];
                [commandBuffer commit];
            }
        } else {
            // Still need to commit, even if we don't have a drawable
            [commandBuffer commit];
        }

        swapChainD->currentFrameSlot = (swapChainD->currentFrameSlot + 1) % QMTL_FRAMES_IN_FLIGHT;
    }

    // Must not hold on to the drawable, regardless of needsPresent
    [swapChainD->d->curDrawable release];
    swapChainD->d->curDrawable = nil;

    [d->captureScope endScope];

    swapChainD->frameCount += 1;
    currentSwapChain = nullptr;
    return QRhi::FrameOpSuccess;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2969
inline QRhi::FrameOpResult QRhiMetal::beginOffscreenFrame(QRhiCommandBuffer **cb, QRhi::BeginFrameFlags flags)
{
    Q_UNUSED(flags);

    currentFrameSlot = (currentFrameSlot + 1) % QMTL_FRAMES_IN_FLIGHT;

    for (QMetalSwapChain *sc : std::as_const(swapchains))
        sc->waitUntilCompleted(currentFrameSlot);

    d->ofr.active = true;
    *cb = &d->ofr.cbWrapper;
    d->ofr.cbWrapper.d->cb = d->newCommandBuffer();

    executeDeferredReleases();
    d->ofr.cbWrapper.resetState(d->ofr.lastGpuTime);
    d->ofr.lastGpuTime = 0;
    finishActiveReadbacks();

    return QRhi::FrameOpSuccess;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 2990
inline QRhi::FrameOpResult QRhiMetal::endOffscreenFrame(QRhi::EndFrameFlags flags)
{
    Q_UNUSED(flags);
    Q_ASSERT(d->ofr.active);
    d->ofr.active = false;

    id<MTLCommandBuffer> cb = d->ofr.cbWrapper.d->cb;
    [cb commit];

    // offscreen frames wait for completion, unlike swapchain ones
    [cb waitUntilCompleted];

    d->ofr.lastGpuTime += cb.GPUEndTime - cb.GPUStartTime;

    finishActiveReadbacks(true);

    return QRhi::FrameOpSuccess;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3009
inline QRhi::FrameOpResult QRhiMetal::finish()
{
    id<MTLCommandBuffer> cb = nil;
    QMetalSwapChain *swapChainD = nullptr;
    if (inFrame) {
        if (d->ofr.active) {
            Q_ASSERT(!currentSwapChain);
            Q_ASSERT(d->ofr.cbWrapper.recordingPass == QMetalCommandBuffer::NoPass);
            cb = d->ofr.cbWrapper.d->cb;
        } else {
            Q_ASSERT(currentSwapChain);
            swapChainD = currentSwapChain;
            Q_ASSERT(swapChainD->cbWrapper.recordingPass == QMetalCommandBuffer::NoPass);
            cb = swapChainD->cbWrapper.d->cb;
        }
    }

    for (QMetalSwapChain *sc : std::as_const(swapchains)) {
        for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
            if (currentSwapChain && sc == currentSwapChain && i == currentFrameSlot) {
                // no wait as this is the thing we're going to be commit below and
                // beginFrame decremented sem already and going to be signaled by endFrame
                continue;
            }
            sc->waitUntilCompleted(i);
        }
    }

    if (cb) {
        [cb commit];
        [cb waitUntilCompleted];
    }

    if (inFrame) {
        if (d->ofr.active) {
            d->ofr.lastGpuTime += cb.GPUEndTime - cb.GPUStartTime;
            d->ofr.cbWrapper.d->cb = d->newCommandBuffer();
        } else {
            swapChainD->d->lastGpuTime[currentFrameSlot] += cb.GPUEndTime - cb.GPUStartTime;
            swapChainD->cbWrapper.d->cb = d->newCommandBuffer();
        }
    }

    executeDeferredReleases(true);

    finishActiveReadbacks(true);

    return QRhi::FrameOpSuccess;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3090
inline qsizetype QRhiMetal::subresUploadByteSize(const QRhiTextureSubresourceUploadDescription &subresDesc) const
{
    qsizetype size = 0;
    const qsizetype imageSizeBytes = subresDesc.image().isNull() ?
                subresDesc.data().size() : subresDesc.image().sizeInBytes();
    if (imageSizeBytes > 0)
        size += aligned<qsizetype>(imageSizeBytes, QRhiMetalData::TEXBUF_ALIGN);
    return size;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3100
inline void QRhiMetal::enqueueSubresUpload(QMetalTexture *texD, void *mp, void *blitEncPtr,
                                    int layer, int level, const QRhiTextureSubresourceUploadDescription &subresDesc,
                                    qsizetype *curOfs)
{
    const QPoint dp = subresDesc.destinationTopLeft();
    const QByteArray rawData = subresDesc.data();
    QImage img = subresDesc.image();
    const bool is3D = texD->m_flags.testFlag(QRhiTexture::ThreeDimensional);
    id<MTLBlitCommandEncoder> blitEnc = (id<MTLBlitCommandEncoder>) blitEncPtr;

    if (!img.isNull()) {
        const qsizetype fullImageSizeBytes = img.sizeInBytes();
        QSize size = img.size();
        int bpl = img.bytesPerLine();

        if (!subresDesc.sourceSize().isEmpty() || !subresDesc.sourceTopLeft().isNull()) {
            const int sx = subresDesc.sourceTopLeft().x();
            const int sy = subresDesc.sourceTopLeft().y();
            if (!subresDesc.sourceSize().isEmpty())
                size = subresDesc.sourceSize();
            size = clampedSubResourceUploadSize(size, dp, level, texD->m_pixelSize);
            if (size.width() == img.width()) {
                const int bpc = qMax(1, img.depth() / 8);
                Q_ASSERT(size.height() * img.bytesPerLine() <= fullImageSizeBytes);
                memcpy(reinterpret_cast<char *>(mp) + *curOfs,
                       img.constBits() + sy * img.bytesPerLine() + sx * bpc,
                       size.height() * img.bytesPerLine());
            } else {
                img = img.copy(sx, sy, size.width(), size.height());
                bpl = img.bytesPerLine();
                Q_ASSERT(img.sizeInBytes() <= fullImageSizeBytes);
                memcpy(reinterpret_cast<char *>(mp) + *curOfs, img.constBits(), size_t(img.sizeInBytes()));
            }
        } else {
            size = clampedSubResourceUploadSize(size, dp, level, texD->m_pixelSize);
            memcpy(reinterpret_cast<char *>(mp) + *curOfs, img.constBits(), size_t(fullImageSizeBytes));
        }

        [blitEnc copyFromBuffer: texD->d->stagingBuf[currentFrameSlot]
                                 sourceOffset: NSUInteger(*curOfs)
                                 sourceBytesPerRow: NSUInteger(bpl)
                                 sourceBytesPerImage: 0
                                 sourceSize: MTLSizeMake(NSUInteger(size.width()), NSUInteger(size.height()), 1)
          toTexture: texD->d->tex
          destinationSlice: NSUInteger(is3D ? 0 : layer)
          destinationLevel: NSUInteger(level)
          destinationOrigin: MTLOriginMake(NSUInteger(dp.x()), NSUInteger(dp.y()), NSUInteger(is3D ? layer : 0))
          options: MTLBlitOptionNone];

        *curOfs += aligned<qsizetype>(fullImageSizeBytes, QRhiMetalData::TEXBUF_ALIGN);
    } else if (!rawData.isEmpty() && isCompressedFormat(texD->m_format)) {
        const QSize subresSize = q->sizeForMipLevel(level, texD->m_pixelSize);
        const int subresw = subresSize.width();
        const int subresh = subresSize.height();
        int w, h;
        if (subresDesc.sourceSize().isEmpty()) {
            w = subresw;
            h = subresh;
        } else {
            w = subresDesc.sourceSize().width();
            h = subresDesc.sourceSize().height();
        }

        quint32 bpl = 0;
        QSize blockDim;
        compressedFormatInfo(texD->m_format, QSize(w, h), &bpl, nullptr, &blockDim);

        const int dx = aligned(dp.x(), blockDim.width());
        const int dy = aligned(dp.y(), blockDim.height());
        if (dx + w != subresw)
            w = aligned(w, blockDim.width());
        if (dy + h != subresh)
            h = aligned(h, blockDim.height());

        memcpy(reinterpret_cast<char *>(mp) + *curOfs, rawData.constData(), size_t(rawData.size()));

        [blitEnc copyFromBuffer: texD->d->stagingBuf[currentFrameSlot]
                                 sourceOffset: NSUInteger(*curOfs)
                                 sourceBytesPerRow: bpl
                                 sourceBytesPerImage: 0
                                 sourceSize: MTLSizeMake(NSUInteger(w), NSUInteger(h), 1)
          toTexture: texD->d->tex
          destinationSlice: NSUInteger(is3D ? 0 : layer)
          destinationLevel: NSUInteger(level)
          destinationOrigin: MTLOriginMake(NSUInteger(dx), NSUInteger(dy), NSUInteger(is3D ? layer : 0))
          options: MTLBlitOptionNone];

        *curOfs += aligned<qsizetype>(rawData.size(), QRhiMetalData::TEXBUF_ALIGN);
    } else if (!rawData.isEmpty()) {
        const QSize subresSize = q->sizeForMipLevel(level, texD->m_pixelSize);
        const int subresw = subresSize.width();
        const int subresh = subresSize.height();
        int w, h;
        if (subresDesc.sourceSize().isEmpty()) {
            w = subresw;
            h = subresh;
        } else {
            w = subresDesc.sourceSize().width();
            h = subresDesc.sourceSize().height();
        }

        QSize size = clampedSubResourceUploadSize(QSize(w, h), dp, level, texD->m_pixelSize);
        quint32 bytesPerPixel = 0;
        textureFormatInfo(texD->m_format, size, nullptr, nullptr, &bytesPerPixel);
        size = clampedSubResourceUploadSizeForSourceData(size, subresDesc.dataStride(),
                                                        bytesPerPixel, rawData.size());
        w = size.width();
        h = size.height();

        quint32 bpl = 0;
        if (subresDesc.dataStride())
            bpl = subresDesc.dataStride();
        else
            textureFormatInfo(texD->m_format, QSize(w, h), &bpl, nullptr, nullptr);

        memcpy(reinterpret_cast<char *>(mp) + *curOfs, rawData.constData(), size_t(rawData.size()));

        if (!size.isEmpty()) {
            [blitEnc copyFromBuffer: texD->d->stagingBuf[currentFrameSlot]
                                     sourceOffset: NSUInteger(*curOfs)
                                     sourceBytesPerRow: bpl
                                     sourceBytesPerImage: 0
                                     sourceSize: MTLSizeMake(NSUInteger(w), NSUInteger(h), 1)
              toTexture: texD->d->tex
              destinationSlice: NSUInteger(is3D ? 0 : layer)
              destinationLevel: NSUInteger(level)
              destinationOrigin: MTLOriginMake(NSUInteger(dp.x()), NSUInteger(dp.y()), NSUInteger(is3D ? layer : 0))
              options: MTLBlitOptionNone];
        }

        *curOfs += aligned<qsizetype>(rawData.size(), QRhiMetalData::TEXBUF_ALIGN);
    } else {
        qWarning("Invalid texture upload for %p layer=%d mip=%d", texD, layer, level);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3236
inline void QRhiMetal::enqueueResourceUpdates(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    QRhiResourceUpdateBatchPrivate *ud = QRhiResourceUpdateBatchPrivate::get(resourceUpdates);

    id<MTLBlitCommandEncoder> blitEnc = nil;
    auto ensureBlit = [&blitEnc, cbD, this]() {
        if (!blitEnc) {
            blitEnc = [cbD->d->cb blitCommandEncoder];
            if (debugMarkers)
                [blitEnc pushDebugGroup: @"Texture upload/copy"];
        }
    };

    for (int opIdx = 0; opIdx < ud->activeBufferOpCount; ++opIdx) {
        const QRhiResourceUpdateBatchPrivate::BufferOp &u(ud->bufferOps[opIdx]);
        if (u.type == QRhiResourceUpdateBatchPrivate::BufferOp::DynamicUpdate) {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, u.buf);
            Q_ASSERT(bufD->m_type == QRhiBuffer::Dynamic);
            for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
                if (u.offset == 0 && u.data.size() == bufD->m_size)
                    bufD->d->pendingUpdates[i].clear();
                bufD->d->pendingUpdates[i].append({ u.offset, u.data });
            }
        } else if (u.type == QRhiResourceUpdateBatchPrivate::BufferOp::StaticUpload) {
            // Due to the Metal API the handling of static and dynamic buffers is
            // basically the same. So go through the same pendingUpdates machinery.
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, u.buf);
            Q_ASSERT(bufD->m_type != QRhiBuffer::Dynamic);
            Q_ASSERT(u.offset + u.data.size() <= bufD->m_size);
            for (int i = 0, ie = bufD->d->slotted ? QMTL_FRAMES_IN_FLIGHT : 1; i != ie; ++i)
                bufD->d->pendingUpdates[i].append({ u.offset, u.data });
        } else if (u.type == QRhiResourceUpdateBatchPrivate::BufferOp::Read) {
            QMetalBuffer *bufD = QRHI_RES(QMetalBuffer, u.buf);
            executeBufferHostWritesForCurrentFrame(bufD);
            const int idx = bufD->d->slotted ? currentFrameSlot : 0;
            if (bufD->m_type == QRhiBuffer::Dynamic) {
                char *p = reinterpret_cast<char *>([bufD->d->buf[idx] contents]);
                if (p) {
                    u.result->data.resize(u.readSize);
                    memcpy(u.result->data.data(), p + u.offset, size_t(u.readSize));
                }
                if (u.result->completed)
                    u.result->completed();
            } else {
                QRhiMetalData::BufferReadback readback;
                readback.activeFrameSlot = idx;
                readback.buf = bufD->d->buf[idx];
                readback.offset = u.offset;
                readback.readSize = u.readSize;
                readback.result = u.result;
                d->activeBufferReadbacks.append(readback);
#ifdef Q_OS_MACOS
                if (bufD->d->managed) {
                    // On non-Apple Silicon, manually synchronize memory from GPU to CPU
                    ensureBlit();
                    [blitEnc synchronizeResource:readback.buf];
                }
#endif
            }
        }
    }

    for (int opIdx = 0; opIdx < ud->activeTextureOpCount; ++opIdx) {
        const QRhiResourceUpdateBatchPrivate::TextureOp &u(ud->textureOps[opIdx]);
        if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Upload) {
            QMetalTexture *utexD = QRHI_RES(QMetalTexture, u.dst);
            qsizetype stagingSize = 0;
            for (int layer = 0, maxLayer = u.subresDesc.count(); layer < maxLayer; ++layer) {
                for (int level = 0; level < QRhi::MAX_MIP_LEVELS; ++level) {
                    for (const QRhiTextureSubresourceUploadDescription &subresDesc : std::as_const(u.subresDesc[layer][level]))
                        stagingSize += subresUploadByteSize(subresDesc);
                }
            }

            ensureBlit();
            Q_ASSERT(!utexD->d->stagingBuf[currentFrameSlot]);
            utexD->d->stagingBuf[currentFrameSlot] = [d->dev newBufferWithLength: NSUInteger(stagingSize)
                        options: MTLResourceStorageModeShared];

            void *mp = [utexD->d->stagingBuf[currentFrameSlot] contents];
            qsizetype curOfs = 0;
            for (int layer = 0, maxLayer = u.subresDesc.count(); layer < maxLayer; ++layer) {
                for (int level = 0; level < QRhi::MAX_MIP_LEVELS; ++level) {
                    for (const QRhiTextureSubresourceUploadDescription &subresDesc : std::as_const(u.subresDesc[layer][level]))
                        enqueueSubresUpload(utexD, mp, blitEnc, layer, level, subresDesc, &curOfs);
                }
            }

            utexD->lastActiveFrameSlot = currentFrameSlot;

            QRhiMetalData::DeferredReleaseEntry e;
            e.type = QRhiMetalData::DeferredReleaseEntry::StagingBuffer;
            e.lastActiveFrameSlot = currentFrameSlot;
            e.stagingBuffer.buffer = utexD->d->stagingBuf[currentFrameSlot];
            utexD->d->stagingBuf[currentFrameSlot] = nil;
            d->releaseQueue.append(e);
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Copy) {
            Q_ASSERT(u.src && u.dst);
            QMetalTexture *srcD = QRHI_RES(QMetalTexture, u.src);
            QMetalTexture *dstD = QRHI_RES(QMetalTexture, u.dst);
            const bool srcIs3D = srcD->m_flags.testFlag(QRhiTexture::ThreeDimensional);
            const bool dstIs3D = dstD->m_flags.testFlag(QRhiTexture::ThreeDimensional);
            const QPoint dp = u.desc.destinationTopLeft();
            const QSize mipSize = q->sizeForMipLevel(u.desc.sourceLevel(), srcD->m_pixelSize);
            const QSize copySize = u.desc.pixelSize().isEmpty() ? mipSize : u.desc.pixelSize();
            const QPoint sp = u.desc.sourceTopLeft();

            ensureBlit();
            [blitEnc copyFromTexture: srcD->d->tex
                                      sourceSlice: NSUInteger(srcIs3D ? 0 : u.desc.sourceLayer())
                                      sourceLevel: NSUInteger(u.desc.sourceLevel())
                                      sourceOrigin: MTLOriginMake(NSUInteger(sp.x()), NSUInteger(sp.y()), NSUInteger(srcIs3D ? u.desc.sourceLayer() : 0))
                                      sourceSize: MTLSizeMake(NSUInteger(copySize.width()), NSUInteger(copySize.height()), 1)
                                      toTexture: dstD->d->tex
                                      destinationSlice: NSUInteger(dstIs3D ? 0 : u.desc.destinationLayer())
                                      destinationLevel: NSUInteger(u.desc.destinationLevel())
                                      destinationOrigin: MTLOriginMake(NSUInteger(dp.x()), NSUInteger(dp.y()), NSUInteger(dstIs3D ? u.desc.destinationLayer() : 0))];

            srcD->lastActiveFrameSlot = dstD->lastActiveFrameSlot = currentFrameSlot;
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::Read) {
            QRhiMetalData::TextureReadback readback;
            readback.activeFrameSlot = currentFrameSlot;
            readback.desc = u.rb;
            readback.result = u.result;

            QMetalTexture *texD = QRHI_RES(QMetalTexture, u.rb.texture());
            QMetalSwapChain *swapChainD = nullptr;
            id<MTLTexture> src;
            QRect rect;
            bool is3D = false;
            if (texD) {
                if (texD->samples > 1) {
                    qWarning("Multisample texture cannot be read back");
                    continue;
                }
                is3D = texD->m_flags.testFlag(QRhiTexture::ThreeDimensional);
                if (u.rb.rect().isValid())
                    rect = u.rb.rect();
                else
                    rect = QRect({0, 0}, q->sizeForMipLevel(u.rb.level(), texD->m_pixelSize));
                readback.format = texD->m_format;
                src = texD->d->tex;
                texD->lastActiveFrameSlot = currentFrameSlot;
            } else {
                Q_ASSERT(currentSwapChain);
                swapChainD = QRHI_RES(QMetalSwapChain, currentSwapChain);
                if (u.rb.rect().isValid())
                    rect = u.rb.rect();
                else
                    rect = QRect({0, 0}, swapChainD->pixelSize);
                readback.format = swapChainD->d->rhiColorFormat;
                // Multisample swapchains need nothing special since resolving
                // happens when ending a renderpass.
                const QMetalRenderTargetData::ColorAtt &colorAtt(swapChainD->rtWrapper.d->fb.colorAtt[0]);
                src = colorAtt.resolveTex ? colorAtt.resolveTex : colorAtt.tex;
            }
            readback.pixelSize = rect.size();

            quint32 bpl = 0;
            textureFormatInfo(readback.format, readback.pixelSize, &bpl, &readback.bufSize, nullptr);
            readback.buf = [d->dev newBufferWithLength: readback.bufSize options: MTLResourceStorageModeShared];

            ensureBlit();
            [blitEnc copyFromTexture: src
                                      sourceSlice: NSUInteger(is3D ? 0 : u.rb.layer())
                                      sourceLevel: NSUInteger(u.rb.level())
                                      sourceOrigin: MTLOriginMake(NSUInteger(rect.x()), NSUInteger(rect.y()), NSUInteger(is3D ? u.rb.layer() : 0))
                                      sourceSize: MTLSizeMake(NSUInteger(rect.width()), NSUInteger(rect.height()), 1)
                                      toBuffer: readback.buf
                                      destinationOffset: 0
                                      destinationBytesPerRow: bpl
                                      destinationBytesPerImage: 0
                                      options: MTLBlitOptionNone];

            d->activeTextureReadbacks.append(readback);
        } else if (u.type == QRhiResourceUpdateBatchPrivate::TextureOp::GenMips) {
            QMetalTexture *utexD = QRHI_RES(QMetalTexture, u.dst);
            ensureBlit();
            [blitEnc generateMipmapsForTexture: utexD->d->tex];
            utexD->lastActiveFrameSlot = currentFrameSlot;
        }
    }

    if (blitEnc) {
        if (debugMarkers)
            [blitEnc popDebugGroup];
        [blitEnc endEncoding];
    }

    ud->free();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3430
inline void QRhiMetal::executeBufferHostWritesForSlot(QMetalBuffer *bufD, int slot)
{
    if (bufD->d->pendingUpdates[slot].isEmpty())
        return;

    void *p = [bufD->d->buf[slot] contents];
    quint32 changeBegin = UINT32_MAX;
    quint32 changeEnd = 0;
    for (const QMetalBufferData::BufferUpdate &u : std::as_const(bufD->d->pendingUpdates[slot])) {
        memcpy(static_cast<char *>(p) + u.offset, u.data.constData(), size_t(u.data.size()));
        if (u.offset < changeBegin)
            changeBegin = u.offset;
        if (u.offset + u.data.size() > changeEnd)
            changeEnd = u.offset + u.data.size();
    }
#ifdef Q_OS_MACOS
    if (changeBegin < UINT32_MAX && changeBegin < changeEnd && bufD->d->managed)
        [bufD->d->buf[slot] didModifyRange: NSMakeRange(NSUInteger(changeBegin), NSUInteger(changeEnd - changeBegin))];
#endif

    bufD->d->pendingUpdates[slot].clear();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3453
inline void QRhiMetal::executeBufferHostWritesForCurrentFrame(QMetalBuffer *bufD)
{
    executeBufferHostWritesForSlot(bufD, bufD->d->slotted ? currentFrameSlot : 0);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3458
inline void QRhiMetal::resourceUpdate(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    Q_ASSERT(QRHI_RES(QMetalCommandBuffer, cb)->recordingPass == QMetalCommandBuffer::NoPass);

    enqueueResourceUpdates(cb, resourceUpdates);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3465
inline void QRhiMetal::beginPass(QRhiCommandBuffer *cb,
                          QRhiRenderTarget *rt,
                          const QColor &colorClearValue,
                          const QRhiDepthStencilClearValue &depthStencilClearValue,
                          QRhiResourceUpdateBatch *resourceUpdates,
                          QRhiCommandBuffer::BeginPassFlags)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);

    QMetalRenderTargetData *rtD = nullptr;
    switch (rt->resourceType()) {
    case QRhiResource::SwapChainRenderTarget:
    {
        QMetalSwapChainRenderTarget *rtSc = QRHI_RES(QMetalSwapChainRenderTarget, rt);
        rtD = rtSc->d;
        QRhiShadingRateMap *shadingRateMap = rtSc->swapChain()->shadingRateMap();
        cbD->d->currentPassRpDesc = d->createDefaultRenderPass(rtD->dsAttCount,
                                                               colorClearValue,
                                                               depthStencilClearValue,
                                                               rtD->colorAttCount,
                                                               shadingRateMap);
        if (rtD->colorAttCount) {
            QMetalRenderTargetData::ColorAtt &color0(rtD->fb.colorAtt[0]);
            if (color0.needsDrawableForTex || color0.needsDrawableForResolveTex) {
                Q_ASSERT(currentSwapChain);
                QMetalSwapChain *swapChainD = QRHI_RES(QMetalSwapChain, currentSwapChain);
                if (!swapChainD->d->curDrawable) {
                    QMacAutoReleasePool pool;
                    swapChainD->d->curDrawable = [[swapChainD->d->layer nextDrawable] retain];
                }
                if (!swapChainD->d->curDrawable) {
                    qWarning("No drawable");
                    return;
                }
                id<MTLTexture> scTex = swapChainD->d->curDrawable.texture;
                if (color0.needsDrawableForTex) {
                    color0.tex = scTex;
                    color0.needsDrawableForTex = false;
                } else {
                    color0.resolveTex = scTex;
                    color0.needsDrawableForResolveTex = false;
                }
            }
        }
        if (shadingRateMap)
            QRHI_RES(QMetalShadingRateMap, shadingRateMap)->lastActiveFrameSlot = currentFrameSlot;
    }
        break;
    case QRhiResource::TextureRenderTarget:
    {
        QMetalTextureRenderTarget *rtTex = QRHI_RES(QMetalTextureRenderTarget, rt);
        rtD = rtTex->d;
        if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QMetalTexture, QMetalRenderBuffer>(rtTex->description(), rtD->currentResIdList))
            rtTex->create();
        cbD->d->currentPassRpDesc = d->createDefaultRenderPass(rtD->dsAttCount,
                                                               colorClearValue,
                                                               depthStencilClearValue,
                                                               rtD->colorAttCount,
                                                               rtTex->m_desc.shadingRateMap());
        if (rtD->fb.preserveColor) {
            for (uint i = 0; i < uint(rtD->colorAttCount); ++i)
                cbD->d->currentPassRpDesc.colorAttachments[i].loadAction = MTLLoadActionLoad;
        }
        if (rtD->dsAttCount && rtD->fb.preserveDs) {
            cbD->d->currentPassRpDesc.depthAttachment.loadAction = MTLLoadActionLoad;
            cbD->d->currentPassRpDesc.stencilAttachment.loadAction = MTLLoadActionLoad;
        }
        int colorAttCount = 0;
        for (auto it = rtTex->m_desc.cbeginColorAttachments(), itEnd = rtTex->m_desc.cendColorAttachments();
             it != itEnd; ++it)
        {
            colorAttCount += 1;
            if (it->texture()) {
                QRHI_RES(QMetalTexture, it->texture())->lastActiveFrameSlot = currentFrameSlot;
                if (it->multiViewCount() >= 2)
                    cbD->d->currentPassRpDesc.renderTargetArrayLength = NSUInteger(it->multiViewCount());
            } else if (it->renderBuffer()) {
                QRHI_RES(QMetalRenderBuffer, it->renderBuffer())->lastActiveFrameSlot = currentFrameSlot;
            }
            if (it->resolveTexture())
                QRHI_RES(QMetalTexture, it->resolveTexture())->lastActiveFrameSlot = currentFrameSlot;
        }
        if (rtTex->m_desc.depthStencilBuffer())
            QRHI_RES(QMetalRenderBuffer, rtTex->m_desc.depthStencilBuffer())->lastActiveFrameSlot = currentFrameSlot;
        if (rtTex->m_desc.depthTexture()) {
            QMetalTexture *depthTexture = QRHI_RES(QMetalTexture, rtTex->m_desc.depthTexture());
            depthTexture->lastActiveFrameSlot = currentFrameSlot;
            if (depthTexture->arraySize() >= 2) {
                const int depthLayer = rtTex->m_desc.depthLayer();
                if (depthLayer >= 0) {
                    cbD->d->currentPassRpDesc.depthAttachment.slice = NSUInteger(depthLayer);
                    cbD->d->currentPassRpDesc.stencilAttachment.slice = NSUInteger(depthLayer);
                    if (colorAttCount == 0)
                        cbD->d->currentPassRpDesc.renderTargetArrayLength = 1;
                } else if (colorAttCount == 0) {
                    cbD->d->currentPassRpDesc.renderTargetArrayLength = NSUInteger(depthTexture->arraySize());
                }
            }
        }
        if (rtTex->m_desc.depthResolveTexture())
            QRHI_RES(QMetalTexture, rtTex->m_desc.depthResolveTexture())->lastActiveFrameSlot = currentFrameSlot;
        if (rtTex->m_desc.shadingRateMap())
            QRHI_RES(QMetalShadingRateMap, rtTex->m_desc.shadingRateMap())->lastActiveFrameSlot = currentFrameSlot;
    }
        break;
    default:
        Q_UNREACHABLE();
        break;
    }

    cbD->d->deferredColorStoreActions.clear();
    cbD->d->deferredDepthStoreAction = MTLStoreActionUnknown;
    cbD->d->deferredStencilStoreAction = MTLStoreActionUnknown;
    for (uint i = 0; i < uint(rtD->colorAttCount); ++i) {
        cbD->d->currentPassRpDesc.colorAttachments[i].texture = rtD->fb.colorAtt[i].tex;
        cbD->d->currentPassRpDesc.colorAttachments[i].slice = NSUInteger(rtD->fb.colorAtt[i].arrayLayer);
        cbD->d->currentPassRpDesc.colorAttachments[i].depthPlane = NSUInteger(rtD->fb.colorAtt[i].slice);
        cbD->d->currentPassRpDesc.colorAttachments[i].level = NSUInteger(rtD->fb.colorAtt[i].level);
        if (rtD->fb.colorAtt[i].resolveTex) {
            const MTLStoreAction storeAction = rtD->fb.preserveColor ? MTLStoreActionStoreAndMultisampleResolve
                                                                     : MTLStoreActionMultisampleResolve;
            // Defer, so that the multisample contents can be kept if the pass
            // ends up being interrupted. finalizeDeferredStoreActions() sets the
            // real action before the encoder ends.
            cbD->d->currentPassRpDesc.colorAttachments[i].storeAction = MTLStoreActionUnknown;
            cbD->d->deferredColorStoreActions.append({ i, storeAction });
            cbD->d->currentPassRpDesc.colorAttachments[i].resolveTexture = rtD->fb.colorAtt[i].resolveTex;
            cbD->d->currentPassRpDesc.colorAttachments[i].resolveSlice = NSUInteger(rtD->fb.colorAtt[i].resolveLayer);
            cbD->d->currentPassRpDesc.colorAttachments[i].resolveLevel = NSUInteger(rtD->fb.colorAtt[i].resolveLevel);
        }
    }

    if (rtD->dsAttCount) {
        Q_ASSERT(rtD->fb.dsTex);
        cbD->d->currentPassRpDesc.depthAttachment.texture = rtD->fb.dsTex;
        cbD->d->currentPassRpDesc.stencilAttachment.texture = rtD->fb.hasStencil ? rtD->fb.dsTex : nil;
        if (rtD->fb.depthNeedsStore) // Depth/Stencil is set to DontCare by default, override if  needed
            cbD->d->currentPassRpDesc.depthAttachment.storeAction = MTLStoreActionStore;
        if (rtD->fb.dsResolveTex) {
            const MTLStoreAction dsStoreAction = rtD->fb.depthNeedsStore ? MTLStoreActionStoreAndMultisampleResolve
                                                                         : MTLStoreActionMultisampleResolve;
            // Deferred for the same reason as the color attachments above, but
            // only when there is something to defer to: a memoryless
            // depth-stencil buffer, which is what a QRhiRenderBuffer is on Apple
            // GPUs, cannot be stored at all, and rejects the store-and-resolve
            // action that an interruption would need.
            const bool deferrable = canStoreAttachment(rtD->fb.dsTex);
            cbD->d->currentPassRpDesc.depthAttachment.storeAction = deferrable ? MTLStoreActionUnknown
                                                                              : dsStoreAction;
            if (deferrable)
                cbD->d->deferredDepthStoreAction = dsStoreAction;
            cbD->d->currentPassRpDesc.depthAttachment.resolveTexture = rtD->fb.dsResolveTex;
            if (rtD->fb.hasStencil) {
                cbD->d->currentPassRpDesc.stencilAttachment.resolveTexture = rtD->fb.dsResolveTex;
                cbD->d->currentPassRpDesc.stencilAttachment.storeAction = deferrable ? MTLStoreActionUnknown
                                                                                    : dsStoreAction;
                if (deferrable)
                    cbD->d->deferredStencilStoreAction = dsStoreAction;
            }
        }
    }

    cbD->d->currentRenderPassEncoder = [cbD->d->cb renderCommandEncoderWithDescriptor: cbD->d->currentPassRpDesc];

    cbD->resetPerPassState();

    cbD->recordingPass = QMetalCommandBuffer::RenderPass;
    cbD->currentTarget = rt;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3639
inline void QRhiMetal::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::RenderPass);

    finalizeDeferredStoreActions(cbD, true);
    [cbD->d->currentRenderPassEncoder endEncoding];

    cbD->recordingPass = QMetalCommandBuffer::NoPass;
    cbD->currentTarget = nullptr;

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3654
inline void QRhiMetal::beginComputePass(QRhiCommandBuffer *cb,
                                 QRhiResourceUpdateBatch *resourceUpdates,
                                 QRhiCommandBuffer::BeginPassFlags)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);

    cbD->d->currentComputePassEncoder = [cbD->d->cb computeCommandEncoder];
    cbD->resetPerPassState();
    cbD->recordingPass = QMetalCommandBuffer::ComputePass;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3669
inline void QRhiMetal::endComputePass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::ComputePass);

    [cbD->d->currentComputePassEncoder endEncoding];
    cbD->recordingPass = QMetalCommandBuffer::NoPass;

    if (resourceUpdates)
        enqueueResourceUpdates(cb, resourceUpdates);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3681
inline void QRhiMetal::setComputePipeline(QRhiCommandBuffer *cb, QRhiComputePipeline *ps)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::ComputePass);
    QMetalComputePipeline *psD = QRHI_RES(QMetalComputePipeline, ps);

    if (cbD->currentComputePipeline != psD || cbD->currentPipelineGeneration != psD->generation) {
        cbD->currentGraphicsPipeline = nullptr;
        cbD->currentComputePipeline = psD;
        cbD->currentPipelineGeneration = psD->generation;

        [cbD->d->currentComputePassEncoder setComputePipelineState: psD->d->ps];
    }

    psD->lastActiveFrameSlot = currentFrameSlot;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3698
inline void QRhiMetal::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
{
    QMetalCommandBuffer *cbD = QRHI_RES(QMetalCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QMetalCommandBuffer::ComputePass);
    QMetalComputePipeline *psD = QRHI_RES(QMetalComputePipeline, cbD->currentComputePipeline);

    [cbD->d->currentComputePassEncoder dispatchThreadgroups: MTLSizeMake(NSUInteger(x), NSUInteger(y), NSUInteger(z))
      threadsPerThreadgroup: psD->d->localSize];
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3733
inline void QRhiMetal::executeDeferredReleases(bool forced)
{
    for (int i = d->releaseQueue.count() - 1; i >= 0; --i) {
        const QRhiMetalData::DeferredReleaseEntry &e(d->releaseQueue[i]);
        if (forced || currentFrameSlot == e.lastActiveFrameSlot || e.lastActiveFrameSlot < 0) {
            switch (e.type) {
            case QRhiMetalData::DeferredReleaseEntry::Buffer:
                qrhimtl_releaseBuffer(e);
                break;
            case QRhiMetalData::DeferredReleaseEntry::RenderBuffer:
                qrhimtl_releaseRenderBuffer(e);
                break;
            case QRhiMetalData::DeferredReleaseEntry::Texture:
                qrhimtl_releaseTexture(e);
                break;
            case QRhiMetalData::DeferredReleaseEntry::Sampler:
                qrhimtl_releaseSampler(e);
                break;
            case QRhiMetalData::DeferredReleaseEntry::StagingBuffer:
                [e.stagingBuffer.buffer release];
                break;
            case QRhiMetalData::DeferredReleaseEntry::GraphicsPipeline:
                [e.graphicsPipeline.pipelineState release];
                [e.graphicsPipeline.depthStencilState release];
                [e.graphicsPipeline.tessVertexComputeState[0] release];
                [e.graphicsPipeline.tessVertexComputeState[1] release];
                [e.graphicsPipeline.tessVertexComputeState[2] release];
                [e.graphicsPipeline.tessTessControlComputeState release];
                break;
            case QRhiMetalData::DeferredReleaseEntry::ComputePipeline:
                [e.computePipeline.pipelineState release];
                break;
            case QRhiMetalData::DeferredReleaseEntry::ShadingRateMap:
                [e.shadingRateMap.rateMap release];
                break;
            case QRhiMetalData::DeferredReleaseEntry::StagingIcbBuffer:
                [e.stagingIcbBuffer.icb release];
                [e.stagingIcbBuffer.argBuffer release];
                break;
            default:
                break;
            }
            d->releaseQueue.removeAt(i);
        }
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3780
inline void QRhiMetal::finishActiveReadbacks(bool forced)
{
    QVarLengthArray<std::function<void()>, 4> completedCallbacks;

    for (int i = d->activeTextureReadbacks.count() - 1; i >= 0; --i) {
        const QRhiMetalData::TextureReadback &readback(d->activeTextureReadbacks[i]);
        if (forced || currentFrameSlot == readback.activeFrameSlot || readback.activeFrameSlot < 0) {
            readback.result->format = readback.format;
            readback.result->pixelSize = readback.pixelSize;
            readback.result->data.resize(int(readback.bufSize));
            void *p = [readback.buf contents];
            memcpy(readback.result->data.data(), p, readback.bufSize);
            [readback.buf release];

            if (readback.result->completed)
                completedCallbacks.append(readback.result->completed);

            d->activeTextureReadbacks.remove(i);
        }
    }

    for (int i = d->activeBufferReadbacks.count() - 1; i >= 0; --i) {
        const QRhiMetalData::BufferReadback &readback(d->activeBufferReadbacks[i]);
        if (forced || currentFrameSlot == readback.activeFrameSlot
                || readback.activeFrameSlot < 0) {
            readback.result->data.resize(readback.readSize);
            char *p = reinterpret_cast<char *>([readback.buf contents]);
            Q_ASSERT(p);
            memcpy(readback.result->data.data(), p + readback.offset, size_t(readback.readSize));

            if (readback.result->completed)
                completedCallbacks.append(readback.result->completed);

            d->activeBufferReadbacks.remove(i);
        }
    }

    for (auto f : completedCallbacks)
        f();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3835
inline void QMetalBuffer::destroy()
{
    if (!d->buf[0])
        return;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::Buffer;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        e.buffer.buffers[i] = d->buf[i];
        d->buf[i] = nil;
        d->pendingUpdates[i].clear();
    }

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3857
inline bool QMetalBuffer::create()
{
    if (d->buf[0])
        destroy();

    if (m_usage.testFlag(QRhiBuffer::StorageBuffer) && m_type == Dynamic) {
        qWarning("StorageBuffer cannot be combined with Dynamic");
        return false;
    }

    const quint32 nonZeroSize = m_size <= 0 ? 256 : m_size;
    const quint32 roundedSize = m_usage.testFlag(QRhiBuffer::UniformBuffer) ? aligned(nonZeroSize, 256u) : nonZeroSize;

    d->managed = false;
    MTLResourceOptions opts = MTLResourceStorageModeShared;

    QRHI_RES_RHI(QRhiMetal);
#ifdef Q_OS_MACOS
    if (!rhiD->caps.isAppleGPU && m_type != Dynamic) {
        opts = MTLResourceStorageModeManaged;
        d->managed = true;
    }
#endif

    // Have QMTL_FRAMES_IN_FLIGHT versions regardless of the type, for now.
    // This is because writing to a Managed buffer (which is what Immutable and
    // Static maps to on macOS) is not safe when another frame reading from the
    // same buffer is still in flight.
    d->slotted = !m_usage.testFlag(QRhiBuffer::StorageBuffer); // except for SSBOs written in the shader
    // and a special case for internal work buffers
    if (int(m_usage) == WorkBufPoolUsage)
        d->slotted = false;

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        if (i == 0 || d->slotted) {
            d->buf[i] = [rhiD->d->dev newBufferWithLength: roundedSize options: opts];
            if (!m_objectName.isEmpty()) {
                if (!d->slotted) {
                    d->buf[i].label = [NSString stringWithUTF8String: m_objectName.constData()];
                } else {
                    const QByteArray name = m_objectName + '/' + QByteArray::number(i);
                    d->buf[i].label = [NSString stringWithUTF8String: name.constData()];
                }
            }
        }
    }

    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3910
inline QRhiBuffer::NativeBuffer QMetalBuffer::nativeBuffer()
{
    if (d->slotted) {
        NativeBuffer b;
        Q_ASSERT(sizeof(b.objects) / sizeof(b.objects[0]) >= size_t(QMTL_FRAMES_IN_FLIGHT));
        for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
            QRHI_RES_RHI(QRhiMetal);
            rhiD->executeBufferHostWritesForSlot(this, i);
            b.objects[i] = &d->buf[i];
        }
        b.slotCount = QMTL_FRAMES_IN_FLIGHT;
        return b;
    }
    return { { &d->buf[0] }, 1 };
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3926
inline char *QMetalBuffer::beginFullDynamicBufferUpdateForCurrentFrame()
{
    // Shortcut the entire buffer update mechanism and allow the client to do
    // the host writes directly to the buffer. This will lead to unexpected
    // results when combined with QRhiResourceUpdateBatch-based updates for the
    // buffer, but provides a fast path for dynamic buffers that have all their
    // content changed in every frame.
    Q_ASSERT(m_type == Dynamic);
    QRHI_RES_RHI(QRhiMetal);
    Q_ASSERT(rhiD->inFrame);
    const int slot = rhiD->currentFrameSlot;
    void *p = [d->buf[slot] contents];
    return static_cast<char *>(p);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 3941
inline void QMetalBuffer::endFullDynamicBufferUpdateForCurrentFrame()
{
#ifdef Q_OS_MACOS
    if (d->managed) {
        QRHI_RES_RHI(QRhiMetal);
        const int slot = rhiD->currentFrameSlot;
        [d->buf[slot] didModifyRange: NSMakeRange(0, NSUInteger(m_size))];
    }
#endif
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4204
inline void QMetalRenderBuffer::destroy()
{
    if (!d->tex)
        return;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::RenderBuffer;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.renderbuffer.texture = d->tex;
    d->tex = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4223
inline bool QMetalRenderBuffer::create()
{
    if (d->tex)
        destroy();

    if (m_pixelSize.isEmpty())
        return false;

    QRHI_RES_RHI(QRhiMetal);
    samples = rhiD->effectiveSampleCount(m_sampleCount);

    MTLTextureDescriptor *desc = [[MTLTextureDescriptor alloc] init];
    desc.textureType = samples > 1 ? MTLTextureType2DMultisample : MTLTextureType2D;
    desc.width = NSUInteger(m_pixelSize.width());
    desc.height = NSUInteger(m_pixelSize.height());
    if (samples > 1)
        desc.sampleCount = NSUInteger(samples);
    desc.resourceOptions = MTLResourceStorageModePrivate;
    desc.usage = MTLTextureUsageRenderTarget;

    switch (m_type) {
    case DepthStencil:
#ifdef Q_OS_MACOS
        if (rhiD->caps.isAppleGPU) {
            desc.storageMode = MTLStorageModeMemoryless;
            d->format = MTLPixelFormatDepth32Float_Stencil8;
        } else {
            desc.storageMode = MTLStorageModePrivate;
            d->format = rhiD->d->dev.depth24Stencil8PixelFormatSupported
                    ? MTLPixelFormatDepth24Unorm_Stencil8 : MTLPixelFormatDepth32Float_Stencil8;
        }
#else
        desc.storageMode = MTLStorageModeMemoryless;
        d->format = MTLPixelFormatDepth32Float_Stencil8;
#endif
        desc.pixelFormat = d->format;
        break;
    case Color:
        desc.storageMode = MTLStorageModePrivate;
        if (m_backingFormatHint != QRhiTexture::UnknownFormat)
            d->format = toMetalTextureFormat(m_backingFormatHint, {}, rhiD);
        else
            d->format = MTLPixelFormatRGBA8Unorm;
        desc.pixelFormat = d->format;
        break;
    default:
        Q_UNREACHABLE();
        break;
    }

    d->tex = [rhiD->d->dev newTextureWithDescriptor: desc];
    [desc release];

    if (!m_objectName.isEmpty())
        d->tex.label = [NSString stringWithUTF8String: m_objectName.constData()];

    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4285
inline QRhiTexture::Format QMetalRenderBuffer::backingFormat() const
{
    if (m_backingFormatHint != QRhiTexture::UnknownFormat)
        return m_backingFormatHint;
    else
        return m_type == Color ? QRhiTexture::RGBA8 : QRhiTexture::UnknownFormat;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4311
inline void QMetalTexture::destroy()
{
    if (!d->tex)
        return;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::Texture;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.texture.texture = d->owns ? d->tex : nil;
    d->tex = nil;

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        e.texture.stagingBuffers[i] = d->stagingBuf[i];
        d->stagingBuf[i] = nil;
    }

    for (int i = 0; i < QRhi::MAX_MIP_LEVELS; ++i) {
        e.texture.views[i] = d->perLevelViews[i];
        d->perLevelViews[i] = nil;
    }

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4340
inline bool QMetalTexture::prepareCreate(QSize *adjustedSize)
{
    if (d->tex)
        destroy();

    const bool isCube = m_flags.testFlag(CubeMap);
    const bool is3D = m_flags.testFlag(ThreeDimensional);
    const bool isArray = m_flags.testFlag(TextureArray);
    const bool hasMipMaps = m_flags.testFlag(MipMapped);
    const bool is1D = m_flags.testFlag(OneDimensional);

    const QSize size = is1D ? QSize(qMax(1, m_pixelSize.width()), 1)
                            : (m_pixelSize.isEmpty() ? QSize(1, 1) : m_pixelSize);

    QRHI_RES_RHI(QRhiMetal);
    d->format = toMetalTextureFormat(m_format, m_flags, rhiD);
    mipLevelCount = hasMipMaps ? rhiD->q->mipLevelsForSize(size) : 1;
    samples = rhiD->effectiveSampleCount(m_sampleCount);
    if (samples > 1) {
        if (isCube) {
            qWarning("Cubemap texture cannot be multisample");
            return false;
        }
        if (is3D) {
            qWarning("3D texture cannot be multisample");
            return false;
        }
        if (hasMipMaps) {
            qWarning("Multisample texture cannot have mipmaps");
            return false;
        }
    }
    if (isCube && is3D) {
        qWarning("Texture cannot be both cube and 3D");
        return false;
    }
    if (isArray && is3D) {
        qWarning("Texture cannot be both array and 3D");
        return false;
    }
    if (is1D && is3D) {
        qWarning("Texture cannot be both 1D and 3D");
        return false;
    }
    if (is1D && isCube) {
        qWarning("Texture cannot be both 1D and cube");
        return false;
    }
    if (m_depth > 1 && !is3D) {
        qWarning("Texture cannot have a depth of %d when it is not 3D", m_depth);
        return false;
    }
    if (m_arraySize > 0 && !isArray) {
        qWarning("Texture cannot have an array size of %d when it is not an array", m_arraySize);
        return false;
    }
    if (m_arraySize < 1 && isArray) {
        qWarning("Texture is an array but array size is %d", m_arraySize);
        return false;
    }

    if (!rhiD->textureFormatInfo(m_format, size, nullptr, nullptr, nullptr))
        return false;

    if (adjustedSize)
        *adjustedSize = size;

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4410
inline bool QMetalTexture::create()
{
    QSize size;
    if (!prepareCreate(&size))
        return false;

    MTLTextureDescriptor *desc = [[MTLTextureDescriptor alloc] init];

    const bool isCube = m_flags.testFlag(CubeMap);
    const bool is3D = m_flags.testFlag(ThreeDimensional);
    const bool isArray = m_flags.testFlag(TextureArray);
    const bool is1D = m_flags.testFlag(OneDimensional);
    if (isCube) {
        desc.textureType = MTLTextureTypeCube;
    } else if (is3D) {
        desc.textureType = MTLTextureType3D;
    } else if (is1D) {
        desc.textureType = isArray ? MTLTextureType1DArray : MTLTextureType1D;
    } else if (isArray) {
        desc.textureType = samples > 1 ? MTLTextureType2DMultisampleArray : MTLTextureType2DArray;
    } else {
        desc.textureType = samples > 1 ? MTLTextureType2DMultisample : MTLTextureType2D;
    }
    desc.pixelFormat = d->format;
    desc.width = NSUInteger(size.width());
    desc.height = NSUInteger(size.height());
    desc.depth = is3D ? qMax(1, m_depth) : 1;
    desc.mipmapLevelCount = NSUInteger(mipLevelCount);
    if (samples > 1)
        desc.sampleCount = NSUInteger(samples);
    if (isArray)
        desc.arrayLength = NSUInteger(qMax(0, m_arraySize));
    desc.resourceOptions = MTLResourceStorageModePrivate;
    desc.storageMode = MTLStorageModePrivate;
    desc.usage = MTLTextureUsageShaderRead;
    if (m_flags.testFlag(RenderTarget))
        desc.usage |= MTLTextureUsageRenderTarget;
    if (m_flags.testFlag(UsedWithLoadStore))
        desc.usage |= MTLTextureUsageShaderWrite;

    QRHI_RES_RHI(QRhiMetal);
    d->tex = [rhiD->d->dev newTextureWithDescriptor: desc];
    [desc release];

    if (!m_objectName.isEmpty())
        d->tex.label = [NSString stringWithUTF8String: m_objectName.constData()];

    d->owns = true;

    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4465
inline bool QMetalTexture::createFrom(QRhiTexture::NativeTexture src)
{
    id<MTLTexture> tex = id<MTLTexture>(src.object);
    if (tex == 0)
        return false;

    if (!prepareCreate())
        return false;

    d->tex = tex;

    d->owns = false;

    lastActiveFrameSlot = -1;
    generation += 1;
    QRHI_RES_RHI(QRhiMetal);
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4485
inline QRhiTexture::NativeTexture QMetalTexture::nativeTexture()
{
    return {quint64(d->tex), 0};
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4520
inline void QMetalSampler::destroy()
{
    if (!d->samplerState)
        return;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::Sampler;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.sampler.samplerState = d->samplerState;
    d->samplerState = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4607
inline bool QMetalSampler::create()
{
    if (d->samplerState)
        destroy();

    MTLSamplerDescriptor *desc = [[MTLSamplerDescriptor alloc] init];
    desc.minFilter = toMetalFilter(m_minFilter);
    desc.magFilter = toMetalFilter(m_magFilter);
    desc.mipFilter = toMetalMipmapMode(m_mipmapMode);
    desc.sAddressMode = toMetalAddressMode(m_addressU);
    desc.tAddressMode = toMetalAddressMode(m_addressV);
    desc.rAddressMode = toMetalAddressMode(m_addressW);
    desc.compareFunction = toMetalTextureCompareFunction(m_compareOp);

    QRHI_RES_RHI(QRhiMetal);
    d->samplerState = [rhiD->d->dev newSamplerStateWithDescriptor: desc];
    [desc release];

    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4643
inline void QMetalShadingRateMap::destroy()
{
    if (!d->rateMap)
        return;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::ShadingRateMap;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.shadingRateMap.rateMap = d->rateMap;
    d->rateMap = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4662
inline bool QMetalShadingRateMap::createFrom(NativeShadingRateMap src)
{
    if (d->rateMap)
        destroy();

    d->rateMap = (id<MTLRasterizationRateMap>) (quintptr(src.object));
    if (!d->rateMap)
        return false;

    [d->rateMap retain];

    lastActiveFrameSlot = -1;
    generation += 1;
    QRHI_RES_RHI(QRhiMetal);
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4693
inline void QMetalRenderPassDescriptor::destroy()
{
    QRHI_RES_RHI(QRhiMetal);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4700
inline bool QMetalRenderPassDescriptor::isCompatible(const QRhiRenderPassDescriptor *other) const
{
    if (!other)
        return false;

    const QMetalRenderPassDescriptor *o = QRHI_RES(const QMetalRenderPassDescriptor, other);

    if (colorAttachmentCount != o->colorAttachmentCount)
        return false;

    if (hasDepthStencil != o->hasDepthStencil)
         return false;

    for (int i = 0; i < colorAttachmentCount; ++i) {
        if (colorFormat[i] != o->colorFormat[i])
            return false;
    }

    if (hasDepthStencil) {
        if (dsFormat != o->dsFormat)
            return false;
    }

    if (hasShadingRateMap != o->hasShadingRateMap)
        return false;

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4729
inline void QMetalRenderPassDescriptor::updateSerializedFormat()
{
    serializedFormatData.clear();
    auto p = std::back_inserter(serializedFormatData);

    *p++ = colorAttachmentCount;
    *p++ = hasDepthStencil;
    for (int i = 0; i < colorAttachmentCount; ++i)
        *p++ = colorFormat[i];
    *p++ = hasDepthStencil ? dsFormat : 0;
    *p++ = hasShadingRateMap;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4742
inline QRhiRenderPassDescriptor *QMetalRenderPassDescriptor::newCompatibleRenderPassDescriptor() const
{
    QMetalRenderPassDescriptor *rpD = new QMetalRenderPassDescriptor(m_rhi);
    rpD->colorAttachmentCount = colorAttachmentCount;
    rpD->hasDepthStencil = hasDepthStencil;
    memcpy(rpD->colorFormat, colorFormat, sizeof(colorFormat));
    rpD->dsFormat = dsFormat;
    rpD->hasShadingRateMap = hasShadingRateMap;

    rpD->updateSerializedFormat();

    QRHI_RES_RHI(QRhiMetal);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4758
inline QVector<quint32> QMetalRenderPassDescriptor::serializedFormat() const
{
    return serializedFormatData;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4775
inline void QMetalSwapChainRenderTarget::destroy()
{
    // nothing to do here
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4780
inline QSize QMetalSwapChainRenderTarget::pixelSize() const
{
    return d->pixelSize;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4785
inline float QMetalSwapChainRenderTarget::devicePixelRatio() const
{
    return d->dpr;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4790
inline int QMetalSwapChainRenderTarget::sampleCount() const
{
    return d->sampleCount;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4809
inline void QMetalTextureRenderTarget::destroy()
{
    QRHI_RES_RHI(QRhiMetal);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4816
inline QRhiRenderPassDescriptor *QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor()
{
    const int colorAttachmentCount = int(m_desc.colorAttachmentCount());
    QMetalRenderPassDescriptor *rpD = new QMetalRenderPassDescriptor(m_rhi);
    rpD->colorAttachmentCount = colorAttachmentCount;
    rpD->hasDepthStencil = m_desc.depthStencilBuffer() || m_desc.depthTexture();

    for (int i = 0; i < colorAttachmentCount; ++i) {
        const QRhiColorAttachment *colorAtt = m_desc.colorAttachmentAt(i);
        QMetalTexture *texD = QRHI_RES(QMetalTexture, colorAtt->texture());
        QMetalRenderBuffer *rbD = QRHI_RES(QMetalRenderBuffer, colorAtt->renderBuffer());
        rpD->colorFormat[i] = int(texD ? texD->d->format : rbD->d->format);
    }

    if (m_desc.depthTexture())
        rpD->dsFormat = int(QRHI_RES(QMetalTexture, m_desc.depthTexture())->d->format);
    else if (m_desc.depthStencilBuffer())
        rpD->dsFormat = int(QRHI_RES(QMetalRenderBuffer, m_desc.depthStencilBuffer())->d->format);

    rpD->hasShadingRateMap = m_desc.shadingRateMap() != nullptr;

    rpD->updateSerializedFormat();

    QRHI_RES_RHI(QRhiMetal);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4844
inline bool QMetalTextureRenderTarget::create()
{
    QRHI_RES_RHI(QRhiMetal);
    Q_ASSERT(m_desc.colorAttachmentCount() > 0 || m_desc.depthTexture());
    Q_ASSERT(!m_desc.depthStencilBuffer() || !m_desc.depthTexture());
    const bool hasDepthStencil = m_desc.depthStencilBuffer() || m_desc.depthTexture();

    d->colorAttCount = 0;
    int attIndex = 0;
    for (auto it = m_desc.cbeginColorAttachments(), itEnd = m_desc.cendColorAttachments(); it != itEnd; ++it, ++attIndex) {
        d->colorAttCount += 1;
        QMetalTexture *texD = QRHI_RES(QMetalTexture, it->texture());
        QMetalRenderBuffer *rbD = QRHI_RES(QMetalRenderBuffer, it->renderBuffer());
        Q_ASSERT(texD || rbD);
        id<MTLTexture> dst = nil;
        bool is3D = false;
        if (texD) {
            dst = texD->d->tex;
            if (attIndex == 0) {
                d->pixelSize = rhiD->q->sizeForMipLevel(it->level(), texD->pixelSize());
                d->sampleCount = texD->samples;
            }
            is3D = texD->flags().testFlag(QRhiTexture::ThreeDimensional);
        } else if (rbD) {
            dst = rbD->d->tex;
            if (attIndex == 0) {
                d->pixelSize = rbD->pixelSize();
                d->sampleCount = rbD->samples;
            }
        }
        QMetalRenderTargetData::ColorAtt colorAtt;
        colorAtt.tex = dst;
        colorAtt.arrayLayer = is3D ? 0 : it->layer();
        colorAtt.slice = is3D ? it->layer() : 0;
        colorAtt.level = it->level();
        QMetalTexture *resTexD = QRHI_RES(QMetalTexture, it->resolveTexture());
        colorAtt.resolveTex = resTexD ? resTexD->d->tex : nil;
        colorAtt.resolveLayer = it->resolveLayer();
        colorAtt.resolveLevel = it->resolveLevel();
        d->fb.colorAtt[attIndex] = colorAtt;
    }
    d->dpr = 1;

    if (hasDepthStencil) {
        if (m_desc.depthTexture()) {
            QMetalTexture *depthTexD = QRHI_RES(QMetalTexture, m_desc.depthTexture());
            d->fb.dsTex = depthTexD->d->tex;
            d->fb.hasStencil = rhiD->isStencilSupportingFormat(depthTexD->format());
            d->fb.depthNeedsStore = !m_flags.testFlag(DoNotStoreDepthStencilContents) && !m_desc.depthResolveTexture();
            d->fb.preserveDs = m_flags.testFlag(QRhiTextureRenderTarget::PreserveDepthStencilContents);
            if (d->colorAttCount == 0) {
                d->pixelSize = depthTexD->pixelSize();
                d->sampleCount = depthTexD->samples;
            }
        } else {
            QMetalRenderBuffer *depthRbD = QRHI_RES(QMetalRenderBuffer, m_desc.depthStencilBuffer());
            d->fb.dsTex = depthRbD->d->tex;
            d->fb.hasStencil = true;
            d->fb.depthNeedsStore = false;
            d->fb.preserveDs = false;
            if (d->colorAttCount == 0) {
                d->pixelSize = depthRbD->pixelSize();
                d->sampleCount = depthRbD->samples;
            }
        }
        if (m_desc.depthResolveTexture()) {
            QMetalTexture *depthResolveTexD = QRHI_RES(QMetalTexture, m_desc.depthResolveTexture());
            d->fb.dsResolveTex = depthResolveTexD->d->tex;
        }
        d->dsAttCount = 1;
    } else {
        d->dsAttCount = 0;
    }

    if (d->colorAttCount > 0)
        d->fb.preserveColor = m_flags.testFlag(QRhiTextureRenderTarget::PreserveColorContents);

    QRhiRenderTargetAttachmentTracker::updateResIdList<QMetalTexture, QMetalRenderBuffer>(m_desc, &d->currentResIdList);

    rhiD->registerResource(this, false);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4927
inline QSize QMetalTextureRenderTarget::pixelSize() const
{
    if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QMetalTexture, QMetalRenderBuffer>(m_desc, d->currentResIdList))
        const_cast<QMetalTextureRenderTarget *>(this)->create();

    return d->pixelSize;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4935
inline float QMetalTextureRenderTarget::devicePixelRatio() const
{
    return d->dpr;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4940
inline int QMetalTextureRenderTarget::sampleCount() const
{
    return d->sampleCount;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4955
inline void QMetalShaderResourceBindings::destroy()
{
    sortedBindings.clear();
    maxBinding = -1;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4965
inline bool QMetalShaderResourceBindings::create()
{
    if (!sortedBindings.isEmpty())
        destroy();

    QRHI_RES_RHI(QRhiMetal);
    if (!rhiD->sanityCheckShaderResourceBindings(this))
        return false;

    rhiD->updateLayoutDesc(this);

    std::copy(m_bindings.cbegin(), m_bindings.cend(), std::back_inserter(sortedBindings));
    std::sort(sortedBindings.begin(), sortedBindings.end(), QRhiImplementation::sortedBindingLessThan);
    if (!sortedBindings.isEmpty())
        maxBinding = QRhiImplementation::shaderResourceBindingData(sortedBindings.last())->binding;
    else
        maxBinding = -1;

    boundResourceData.resize(sortedBindings.count());

    for (BoundResourceData &bd : boundResourceData)
        memset(&bd, 0, sizeof(BoundResourceData));

    generation += 1;
    rhiD->registerResource(this, false);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 4993
inline void QMetalShaderResourceBindings::updateResources(UpdateFlags flags)
{
    sortedBindings.clear();
    std::copy(m_bindings.cbegin(), m_bindings.cend(), std::back_inserter(sortedBindings));
    if (!flags.testFlag(BindingsAreSorted))
        std::sort(sortedBindings.begin(), sortedBindings.end(), QRhiImplementation::sortedBindingLessThan);

    for (BoundResourceData &bd : boundResourceData)
        memset(&bd, 0, sizeof(BoundResourceData));

    generation += 1;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5020
inline void QMetalGraphicsPipeline::destroy()
{
    d->vs.destroy();
    d->fs.destroy();

    d->tess.compVs[0].destroy();
    d->tess.compVs[1].destroy();
    d->tess.compVs[2].destroy();

    d->tess.compTesc.destroy();
    d->tess.vertTese.destroy();

    qDeleteAll(d->extraBufMgr.deviceLocalWorkBuffers);
    d->extraBufMgr.deviceLocalWorkBuffers.clear();
    qDeleteAll(d->extraBufMgr.hostVisibleWorkBuffers);
    d->extraBufMgr.hostVisibleWorkBuffers.clear();

    delete d->bufferSizeBuffer;
    d->bufferSizeBuffer = nullptr;

    if (!d->ps && !d->ds
            && !d->tess.vertexComputeState[0] && !d->tess.vertexComputeState[1] && !d->tess.vertexComputeState[2]
            && !d->tess.tessControlComputeState)
    {
        return;
    }

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::GraphicsPipeline;
    e.lastActiveFrameSlot = lastActiveFrameSlot;
    e.graphicsPipeline.pipelineState = d->ps;
    e.graphicsPipeline.depthStencilState = d->ds;
    e.graphicsPipeline.tessVertexComputeState = d->tess.vertexComputeState;
    e.graphicsPipeline.tessTessControlComputeState = d->tess.tessControlComputeState;
    d->ps = nil;
    d->ds = nil;
    d->tess.vertexComputeState = {};
    d->tess.tessControlComputeState = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5432
inline void QMetalGraphicsPipeline::setupAttachmentsInMetalRenderPassDescriptor(void *metalRpDesc, QMetalRenderPassDescriptor *rpD)
{
    MTLRenderPipelineDescriptor *rpDesc = reinterpret_cast<MTLRenderPipelineDescriptor *>(metalRpDesc);

    if (rpD->colorAttachmentCount) {
        // defaults when no targetBlends are provided
        rpDesc.colorAttachments[0].pixelFormat = MTLPixelFormat(rpD->colorFormat[0]);
        rpDesc.colorAttachments[0].writeMask = MTLColorWriteMaskAll;
        rpDesc.colorAttachments[0].blendingEnabled = false;

        Q_ASSERT(m_targetBlends.count() == rpD->colorAttachmentCount
                 || (m_targetBlends.isEmpty() && rpD->colorAttachmentCount == 1));

        for (uint i = 0, ie = uint(m_targetBlends.count()); i != ie; ++i) {
            const QRhiGraphicsPipeline::TargetBlend &b(m_targetBlends[int(i)]);
            rpDesc.colorAttachments[i].pixelFormat = MTLPixelFormat(rpD->colorFormat[i]);
            rpDesc.colorAttachments[i].blendingEnabled = b.enable;
            rpDesc.colorAttachments[i].sourceRGBBlendFactor = toMetalBlendFactor(b.srcColor);
            rpDesc.colorAttachments[i].destinationRGBBlendFactor = toMetalBlendFactor(b.dstColor);
            rpDesc.colorAttachments[i].rgbBlendOperation = toMetalBlendOp(b.opColor);
            rpDesc.colorAttachments[i].sourceAlphaBlendFactor = toMetalBlendFactor(b.srcAlpha);
            rpDesc.colorAttachments[i].destinationAlphaBlendFactor = toMetalBlendFactor(b.dstAlpha);
            rpDesc.colorAttachments[i].alphaBlendOperation = toMetalBlendOp(b.opAlpha);
            rpDesc.colorAttachments[i].writeMask = toMetalColorWriteMask(b.colorWrite);
        }
    }

    if (rpD->hasDepthStencil) {
        // Must only be set when a depth-stencil buffer will actually be bound,
        // validation blows up otherwise.
        MTLPixelFormat fmt = MTLPixelFormat(rpD->dsFormat);
        rpDesc.depthAttachmentPixelFormat = fmt;
#if defined(Q_OS_MACOS)
        if (fmt != MTLPixelFormatDepth16Unorm && fmt != MTLPixelFormatDepth32Float)
#else
        if (fmt != MTLPixelFormatDepth32Float)
#endif
            rpDesc.stencilAttachmentPixelFormat = fmt;
    }

    QRHI_RES_RHI(QRhiMetal);
    rpDesc.rasterSampleCount = NSUInteger(rhiD->effectiveSampleCount(m_sampleCount));
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5476
inline void QMetalGraphicsPipeline::setupMetalDepthStencilDescriptor(void *metalDsDesc)
{
    MTLDepthStencilDescriptor *dsDesc = reinterpret_cast<MTLDepthStencilDescriptor *>(metalDsDesc);

    dsDesc.depthCompareFunction = m_depthTest ? toMetalCompareOp(m_depthOp) : MTLCompareFunctionAlways;
    dsDesc.depthWriteEnabled = m_depthWrite;
    if (m_stencilTest) {
        dsDesc.frontFaceStencil = [[MTLStencilDescriptor alloc] init];
        dsDesc.frontFaceStencil.stencilFailureOperation = toMetalStencilOp(m_stencilFront.failOp);
        dsDesc.frontFaceStencil.depthFailureOperation = toMetalStencilOp(m_stencilFront.depthFailOp);
        dsDesc.frontFaceStencil.depthStencilPassOperation = toMetalStencilOp(m_stencilFront.passOp);
        dsDesc.frontFaceStencil.stencilCompareFunction = toMetalCompareOp(m_stencilFront.compareOp);
        dsDesc.frontFaceStencil.readMask = m_stencilReadMask;
        dsDesc.frontFaceStencil.writeMask = m_stencilWriteMask;

        dsDesc.backFaceStencil = [[MTLStencilDescriptor alloc] init];
        dsDesc.backFaceStencil.stencilFailureOperation = toMetalStencilOp(m_stencilBack.failOp);
        dsDesc.backFaceStencil.depthFailureOperation = toMetalStencilOp(m_stencilBack.depthFailOp);
        dsDesc.backFaceStencil.depthStencilPassOperation = toMetalStencilOp(m_stencilBack.passOp);
        dsDesc.backFaceStencil.stencilCompareFunction = toMetalCompareOp(m_stencilBack.compareOp);
        dsDesc.backFaceStencil.readMask = m_stencilReadMask;
        dsDesc.backFaceStencil.writeMask = m_stencilWriteMask;
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5501
inline void QMetalGraphicsPipeline::mapStates()
{
    d->winding = m_frontFace == CCW ? MTLWindingCounterClockwise : MTLWindingClockwise;
    d->cullMode = toMetalCullMode(m_cullMode);
    d->triangleFillMode = toMetalTriangleFillMode(m_polygonMode);
    d->depthClipMode = m_depthClamp ? MTLDepthClipModeClamp : MTLDepthClipModeClip;
    d->depthBias = float(m_depthBias);
    d->slopeScaledDepthBias = m_slopeScaledDepthBias;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 5595
inline bool QMetalGraphicsPipeline::createVertexFragmentPipeline()
{
    QRHI_RES_RHI(QRhiMetal);

    MTLVertexDescriptor *vertexDesc = [MTLVertexDescriptor vertexDescriptor];
    d->setupVertexInputDescriptor(vertexDesc);

    MTLRenderPipelineDescriptor *rpDesc = [[MTLRenderPipelineDescriptor alloc] init];
    rpDesc.vertexDescriptor = vertexDesc;

    // Mutability cannot be determined (slotted buffers could be set as
    // MTLMutabilityImmutable, but then we potentially need a different
    // descriptor for each buffer combination as this depends on the actual
    // buffers not just the resource binding layout), so leave
    // rpDesc.vertex/fragmentBuffers at the defaults.

    for (const QRhiShaderStage &shaderStage : std::as_const(m_shaderStages)) {
        auto cacheIt = rhiD->d->shaderCache.constFind(shaderStage);
        if (cacheIt != rhiD->d->shaderCache.constEnd()) {
            switch (shaderStage.type()) {
            case QRhiShaderStage::Vertex:
                d->vs = *cacheIt;
                [d->vs.lib retain];
                [d->vs.func retain];
                rpDesc.vertexFunction = d->vs.func;
                break;
            case QRhiShaderStage::Fragment:
                d->fs = *cacheIt;
                [d->fs.lib retain];
                [d->fs.func retain];
                rpDesc.fragmentFunction = d->fs.func;
                break;
            default:
                break;
            }
        } else {
            const QShader shader = shaderStage.shader();
            QString error;
            QByteArray entryPoint;
            QShaderKey activeKey;
            id<MTLLibrary> lib = rhiD->d->createMetalLib(shader, shaderStage.shaderVariant(),
                                                         &error, &entryPoint, &activeKey);
            if (!lib) {
                qWarning("MSL shader compilation failed: %s", qPrintable(error));
                return false;
            }
            id<MTLFunction> func = rhiD->d->createMSLShaderFunction(lib, entryPoint);
            if (!func) {
                qWarning("MSL function for entry point %s not found", entryPoint.constData());
                [lib release];
                return false;
            }
            if (rhiD->d->shaderCache.count() >= QRhiMetal::MAX_SHADER_CACHE_ENTRIES) {
                // Use the simplest strategy: too many cached shaders -> drop them all.
                for (QMetalShader &s : rhiD->d->shaderCache)
                    s.destroy();
                rhiD->d->shaderCache.clear();
            }
            switch (shaderStage.type()) {
            case QRhiShaderStage::Vertex:
                d->vs.lib = lib;
                d->vs.func = func;
                d->vs.nativeResourceBindingMap = shader.nativeResourceBindingMap(activeKey);
                d->vs.desc = shader.description();
                d->vs.nativeShaderInfo = shader.nativeShaderInfo(activeKey);
                rhiD->d->shaderCache.insert(shaderStage, d->vs);
                [d->vs.lib retain];
                [d->vs.func retain];
                rpDesc.vertexFunction = func;
                break;
            case QRhiShaderStage::Fragment:
                d->fs.lib = lib;
                d->fs.func = func;
                d->fs.nativeResourceBindingMap = shader.nativeResourceBindingMap(activeKey);
                d->fs.desc = shader.description();
                d->fs.nativeShaderInfo = shader.nativeShaderInfo(activeKey);
                rhiD->d->shaderCache.insert(shaderStage, d->fs);
                [d->fs.lib retain];
                [d->fs.func retain];
                rpDesc.fragmentFunction = func;
                break;
            default:
                [func release];
                [lib release];
                break;
            }
        }
    }

    QMetalRenderPassDescriptor *rpD = QRHI_RES(QMetalRenderPassDescriptor, m_renderPassDesc);
    setupAttachmentsInMetalRenderPassDescriptor(rpDesc, rpD);

    if (m_flags.testFlag(UsesIndirectDraws) && rhiD->caps.indirectCommandBuffers)
        rpDesc.supportIndirectCommandBuffers = YES;

    if (m_multiViewCount >= 2)
        rpDesc.inputPrimitiveTopology = toMetalPrimitiveTopologyClass(m_topology);

    rhiD->d->trySeedingRenderPipelineFromBinaryArchive(rpDesc);

    if (rhiD->rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave))
        rhiD->d->addRenderPipelineToBinaryArchive(rpDesc);

    NSError *err = nil;
    d->ps = [rhiD->d->dev newRenderPipelineStateWithDescriptor: rpDesc error: &err];
    [rpDesc release];
    if (!d->ps) {
        const QString msg = QString::fromNSString(err.localizedDescription);
        qWarning("Failed to create render pipeline state: %s", qPrintable(msg));
        return false;
    }

    MTLDepthStencilDescriptor *dsDesc = [[MTLDepthStencilDescriptor alloc] init];
    setupMetalDepthStencilDescriptor(dsDesc);
    d->ds = [rhiD->d->dev newDepthStencilStateWithDescriptor: dsDesc];
    [dsDesc release];

    d->primitiveType = toMetalPrimitiveType(m_topology);
    mapStates();

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6260
inline bool QMetalGraphicsPipeline::createTessellationPipelines(const QShader &tessVert, const QShader &tesc, const QShader &tese, const QShader &tessFrag)
{
    QRHI_RES_RHI(QRhiMetal);
    QString error;
    QByteArray entryPoint;
    QShaderKey activeKey;

    const QShaderDescription tescDesc = tesc.description();
    const QShaderDescription teseDesc = tese.description();
    d->tess.inControlPointCount = uint(m_patchControlPointCount);
    d->tess.outControlPointCount = tescDesc.tessellationOutputVertexCount();
    if (!d->tess.outControlPointCount)
        d->tess.outControlPointCount = teseDesc.tessellationOutputVertexCount();

    if (!d->tess.outControlPointCount) {
        qWarning("Failed to determine output vertex count from the tessellation control or evaluation shader, cannot tessellate");
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }

    if (m_multiViewCount >= 2)
        qWarning("Multiview is not supported with tessellation");

    // Now the vertex shader is a compute shader.
    // It should have three dedicated *VertexAsComputeShader variants.
    // What the requested variant was (Standard or Batchable) plays no role here.
    // (the Qt Quick scenegraph does not use tessellation with its materials)
    // Create all three versions.

    bool variantsPresent[3] = {};
    const QVector<QShaderKey> tessVertKeys = tessVert.availableShaders();
    for (const QShaderKey &k : tessVertKeys) {
        switch (k.sourceVariant()) {
        case QShader::NonIndexedVertexAsComputeShader:
            variantsPresent[0] = true;
            break;
        case QShader::UInt32IndexedVertexAsComputeShader:
            variantsPresent[1] = true;
            break;
        case QShader::UInt16IndexedVertexAsComputeShader:
            variantsPresent[2] = true;
            break;
        default:
            break;
        }
    }
    if (!(variantsPresent[0] && variantsPresent[1] && variantsPresent[2])) {
        qWarning("Vertex shader is not prepared for Metal tessellation. Cannot tessellate. "
                 "Perhaps the relevant variants (UInt32IndexedVertexAsComputeShader et al) were not generated? "
                 "Try passing --msltess to qsb.");
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }

    int varIndex = 0; // Will map NonIndexed as 0, UInt32 as 1, UInt16 as 2. Do not change this ordering.
    for (QShader::Variant variant : {
         QShader::NonIndexedVertexAsComputeShader,
         QShader::UInt32IndexedVertexAsComputeShader,
         QShader::UInt16IndexedVertexAsComputeShader })
    {
        id<MTLLibrary> lib = rhiD->d->createMetalLib(tessVert, variant, &error, &entryPoint, &activeKey);
        if (!lib) {
            qWarning("MSL shader compilation failed for vertex-as-compute shader %d: %s", int(variant), qPrintable(error));
            d->tess.enabled = false;
            d->tess.failed = true;
            return false;
        }
        id<MTLFunction> func = rhiD->d->createMSLShaderFunction(lib, entryPoint);
        if (!func) {
            qWarning("MSL function for entry point %s not found", entryPoint.constData());
            [lib release];
            d->tess.enabled = false;
            d->tess.failed = true;
            return false;
        }
        QMetalShader &compVs(d->tess.compVs[varIndex]);
        compVs.lib = lib;
        compVs.func = func;
        compVs.desc = tessVert.description();
        compVs.nativeResourceBindingMap = tessVert.nativeResourceBindingMap(activeKey);
        compVs.nativeShaderInfo = tessVert.nativeShaderInfo(activeKey);

        // pre-create all three MTLComputePipelineStates
        if (!d->tess.vsCompPipeline(rhiD, variant)) {
            qWarning("Failed to pre-generate compute pipeline for vertex compute shader (tessellation variant %d)", int(variant));
            d->tess.enabled = false;
            d->tess.failed = true;
            return false;
        }

        ++varIndex;
    }

    // Pipeline #2 is a compute that runs the tessellation control (compute) shader
    id<MTLLibrary> tessControlLib = rhiD->d->createMetalLib(tesc, QShader::StandardShader, &error, &entryPoint, &activeKey);
    if (!tessControlLib) {
        qWarning("MSL shader compilation failed for tessellation control compute shader: %s", qPrintable(error));
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    id<MTLFunction> tessControlFunc = rhiD->d->createMSLShaderFunction(tessControlLib, entryPoint);
    if (!tessControlFunc) {
        qWarning("MSL function for entry point %s not found", entryPoint.constData());
        [tessControlLib release];
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    d->tess.compTesc.lib = tessControlLib;
    d->tess.compTesc.func = tessControlFunc;
    d->tess.compTesc.desc = tesc.description();
    d->tess.compTesc.nativeResourceBindingMap = tesc.nativeResourceBindingMap(activeKey);
    d->tess.compTesc.nativeShaderInfo = tesc.nativeShaderInfo(activeKey);
    if (!d->tess.tescCompPipeline(rhiD)) {
        qWarning("Failed to pre-generate compute pipeline for tessellation control shader");
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }

    // Pipeline #3 is a render pipeline with the tessellation evaluation (vertex) + the fragment shader
    id<MTLLibrary> tessEvalLib = rhiD->d->createMetalLib(tese, QShader::StandardShader, &error, &entryPoint, &activeKey);
    if (!tessEvalLib) {
        qWarning("MSL shader compilation failed for tessellation evaluation vertex shader: %s", qPrintable(error));
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    id<MTLFunction> tessEvalFunc = rhiD->d->createMSLShaderFunction(tessEvalLib, entryPoint);
    if (!tessEvalFunc) {
        qWarning("MSL function for entry point %s not found", entryPoint.constData());
        [tessEvalLib release];
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    d->tess.vertTese.lib = tessEvalLib;
    d->tess.vertTese.func = tessEvalFunc;
    d->tess.vertTese.desc = tese.description();
    d->tess.vertTese.nativeResourceBindingMap = tese.nativeResourceBindingMap(activeKey);
    d->tess.vertTese.nativeShaderInfo = tese.nativeShaderInfo(activeKey);

    id<MTLLibrary> fragLib = rhiD->d->createMetalLib(tessFrag, QShader::StandardShader, &error, &entryPoint, &activeKey);
    if (!fragLib) {
        qWarning("MSL shader compilation failed for fragment shader: %s", qPrintable(error));
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    id<MTLFunction> fragFunc = rhiD->d->createMSLShaderFunction(fragLib, entryPoint);
    if (!fragFunc) {
        qWarning("MSL function for entry point %s not found", entryPoint.constData());
        [fragLib release];
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }
    d->fs.lib = fragLib;
    d->fs.func = fragFunc;
    d->fs.desc = tessFrag.description();
    d->fs.nativeShaderInfo = tessFrag.nativeShaderInfo(activeKey);
    d->fs.nativeResourceBindingMap = tessFrag.nativeResourceBindingMap(activeKey);

    if (!d->tess.teseFragRenderPipeline(rhiD, this)) {
        qWarning("Failed to pre-generate render pipeline for tessellation evaluation + fragment shader");
        d->tess.enabled = false;
        d->tess.failed = true;
        return false;
    }

    MTLDepthStencilDescriptor *dsDesc = [[MTLDepthStencilDescriptor alloc] init];
    setupMetalDepthStencilDescriptor(dsDesc);
    d->ds = [rhiD->d->dev newDepthStencilStateWithDescriptor: dsDesc];
    [dsDesc release];

    // no primitiveType
    mapStates();

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6444
inline bool QMetalGraphicsPipeline::create()
{
    destroy(); // no early test, always invoke and leave it to destroy to decide what to clean up

    QRHI_RES_RHI(QRhiMetal);
    rhiD->pipelineCreationStart();
    if (!rhiD->sanityCheckGraphicsPipeline(this))
        return false;

    // See if tessellation is involved. Things will be very different, if so.
    QShader tessVert;
    QShader tesc;
    QShader tese;
    QShader tessFrag;
    for (const QRhiShaderStage &shaderStage : std::as_const(m_shaderStages)) {
        switch (shaderStage.type()) {
        case QRhiShaderStage::Vertex:
            tessVert = shaderStage.shader();
            break;
        case QRhiShaderStage::TessellationControl:
            tesc = shaderStage.shader();
            break;
        case QRhiShaderStage::TessellationEvaluation:
            tese = shaderStage.shader();
            break;
        case QRhiShaderStage::Fragment:
            tessFrag = shaderStage.shader();
            break;
        default:
            break;
        }
    }
    d->tess.enabled = tesc.isValid() && tese.isValid() && m_topology == Patches && m_patchControlPointCount > 0;
    d->tess.failed = false;

    bool ok = d->tess.enabled ? createTessellationPipelines(tessVert, tesc, tese, tessFrag) : createVertexFragmentPipeline();
    if (!ok)
        return false;

    // SPIRV-Cross buffer size buffers
    int buffers = 0;
    QVarLengthArray<QMetalShader *, 6> shaders;
    if (d->tess.enabled) {
        shaders.append(&d->tess.compVs[0]);
        shaders.append(&d->tess.compVs[1]);
        shaders.append(&d->tess.compVs[2]);
        shaders.append(&d->tess.compTesc);
        shaders.append(&d->tess.vertTese);
    } else {
        shaders.append(&d->vs);
    }
    shaders.append(&d->fs);

    for (QMetalShader *shader : shaders) {
        if (shader->nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding)) {
            const int binding = shader->nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding];
            shader->nativeResourceBindingMap[binding] = {binding, -1};
            int maxNativeBinding = 0;
            for (const QShaderDescription::StorageBlock &block : shader->desc.storageBlocks())
                maxNativeBinding = qMax(maxNativeBinding, shader->nativeResourceBindingMap[block.binding].first);

            // we use one buffer to hold data for all graphics shader stages, each with a different offset.
            // buffer offsets must be 32byte aligned - adjust buffer count accordingly
            buffers += ((maxNativeBinding + 1 + 7) / 8) * 8;
        }
    }

    if (buffers) {
        if (!d->bufferSizeBuffer)
            d->bufferSizeBuffer = new QMetalBuffer(rhiD, QRhiBuffer::Static, QRhiBuffer::StorageBuffer, buffers * sizeof(int));

        d->bufferSizeBuffer->setSize(buffers * sizeof(int));
        d->bufferSizeBuffer->create();
    }

    rhiD->pipelineCreationEnd();
    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6538
inline void QMetalComputePipeline::destroy()
{
    d->cs.destroy();

    if (!d->ps)
        return;

    delete d->bufferSizeBuffer;
    d->bufferSizeBuffer = nullptr;

    QRhiMetalData::DeferredReleaseEntry e;
    e.type = QRhiMetalData::DeferredReleaseEntry::ComputePipeline;
    e.lastActiveFrameSlot = lastActiveFrameSlot;
    e.computePipeline.pipelineState = d->ps;
    d->ps = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->d->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6580
inline bool QMetalComputePipeline::create()
{
    if (d->ps)
        destroy();

    QRHI_RES_RHI(QRhiMetal);
    rhiD->pipelineCreationStart();

    auto cacheIt = rhiD->d->shaderCache.constFind(m_shaderStage);
    if (cacheIt != rhiD->d->shaderCache.constEnd()) {
        d->cs = *cacheIt;
    } else {
        const QShader shader = m_shaderStage.shader();
        QString error;
        QByteArray entryPoint;
        QShaderKey activeKey;
        id<MTLLibrary> lib = rhiD->d->createMetalLib(shader, m_shaderStage.shaderVariant(),
                                                     &error, &entryPoint, &activeKey);
        if (!lib) {
            qWarning("MSL shader compilation failed: %s", qPrintable(error));
            return false;
        }
        id<MTLFunction> func = rhiD->d->createMSLShaderFunction(lib, entryPoint);
        if (!func) {
            qWarning("MSL function for entry point %s not found", entryPoint.constData());
            [lib release];
            return false;
        }
        d->cs.lib = lib;
        d->cs.func = func;
        d->cs.localSize = shader.description().computeShaderLocalSize();
        d->cs.nativeResourceBindingMap = shader.nativeResourceBindingMap(activeKey);
        d->cs.desc = shader.description();
        d->cs.nativeShaderInfo = shader.nativeShaderInfo(activeKey);

        // SPIRV-Cross buffer size buffers
        if (d->cs.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding)) {
            const int binding = d->cs.nativeShaderInfo.extraBufferBindings[QShaderPrivate::MslBufferSizeBufferBinding];
            d->cs.nativeResourceBindingMap[binding] = {binding, -1};
        }

        if (rhiD->d->shaderCache.count() >= QRhiMetal::MAX_SHADER_CACHE_ENTRIES) {
            for (QMetalShader &s : rhiD->d->shaderCache)
                s.destroy();
            rhiD->d->shaderCache.clear();
        }
        rhiD->d->shaderCache.insert(m_shaderStage, d->cs);
    }

    [d->cs.lib retain];
    [d->cs.func retain];

    d->localSize = MTLSizeMake(d->cs.localSize[0], d->cs.localSize[1], d->cs.localSize[2]);

    MTLComputePipelineDescriptor *cpDesc = [MTLComputePipelineDescriptor new];
    cpDesc.computeFunction = d->cs.func;

    rhiD->d->trySeedingComputePipelineFromBinaryArchive(cpDesc);

    if (rhiD->rhiFlags.testFlag(QRhi::EnablePipelineCacheDataSave))
        rhiD->d->addComputePipelineToBinaryArchive(cpDesc);

    NSError *err = nil;
    d->ps = [rhiD->d->dev newComputePipelineStateWithDescriptor: cpDesc
            options: MTLPipelineOptionNone
            reflection: nil
            error: &err];
    [cpDesc release];
    if (!d->ps) {
        const QString msg = QString::fromNSString(err.localizedDescription);
        qWarning("Failed to create compute pipeline state: %s", qPrintable(msg));
        return false;
    }

    // SPIRV-Cross buffer size buffers
    if (d->cs.nativeShaderInfo.extraBufferBindings.contains(QShaderPrivate::MslBufferSizeBufferBinding)) {
        int buffers = 0;
        for (const QShaderDescription::StorageBlock &block : d->cs.desc.storageBlocks())
            buffers = qMax(buffers, d->cs.nativeResourceBindingMap[block.binding].first);

        buffers += 1;

        if (!d->bufferSizeBuffer)
            d->bufferSizeBuffer = new QMetalBuffer(rhiD, QRhiBuffer::Static, QRhiBuffer::StorageBuffer, buffers * sizeof(int));

        d->bufferSizeBuffer->setSize(buffers * sizeof(int));
        d->bufferSizeBuffer->create();
    }

    rhiD->pipelineCreationEnd();
    lastActiveFrameSlot = -1;
    generation += 1;
    rhiD->registerResource(this);
    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6689
inline void QMetalCommandBuffer::destroy()
{
    // nothing to do here, we do not own the MTL cb object
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6694
inline const QRhiNativeHandles *QMetalCommandBuffer::nativeHandles()
{
    nativeHandlesStruct.commandBuffer = (MTLCommandBuffer *) d->cb;
    nativeHandlesStruct.encoder = (MTLRenderCommandEncoder *) d->currentRenderPassEncoder;
    return &nativeHandlesStruct;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6701
inline void QMetalCommandBuffer::resetState(double lastGpuTime)
{
    d->lastGpuTime = lastGpuTime;
    d->currentRenderPassEncoder = nil;
    d->currentComputePassEncoder = nil;
    d->tessellationComputeEncoder = nil;
    d->currentPassRpDesc = nil;
    resetPerPassState();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6711
inline void QMetalCommandBuffer::resetPerPassState()
{
    recordingPass = NoPass;
    currentTarget = nullptr;
    resetPerPassCachedState();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6718
inline void QMetalCommandBuffer::resetPerPassCachedState()
{
    currentGraphicsPipeline = nullptr;
    currentComputePipeline = nullptr;
    currentPipelineGeneration = 0;
    currentGraphicsSrb = nullptr;
    currentComputeSrb = nullptr;
    currentSrbGeneration = 0;
    currentResSlot = -1;
    currentIndexBuffer = nullptr;
    currentIndexOffset = 0;
    currentIndexFormat = QRhiCommandBuffer::IndexUInt16;
    currentCullMode = -1;
    currentTriangleFillMode = -1;
    currentDepthClipMode = -1;
    currentFrontFaceWinding = -1;
    currentDepthBiasValues = { 0.0f, 0.0f };
    hasCustomScissorSet = false;
    currentScissor = {};
    currentViewport = {};
    hasBlendConstantsSet = false;
    currentBlendConstants = {};
    hasStencilRefSet = false;
    currentStencilRef = 0;

    d->currentShaderResourceBindingState = {};
    d->currentDepthStencilState = nil;
    d->currentFirstVertexBinding = -1;
    d->currentVertexInputsBuffers.clear();
    d->currentVertexInputOffsets.clear();
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6768
inline void QMetalSwapChain::destroy()
{
    if (!d->layer)
        return;

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        if (d->sem[i]) {
            // the semaphores cannot be released if they do not have the initial value
            waitUntilCompleted(i);

            dispatch_release(d->sem[i]);
            d->sem[i] = nullptr;
        }
    }

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        [d->msaaTex[i] release];
        d->msaaTex[i] = nil;
    }

    d->layer = nullptr;
    m_proxyData = {};

    [d->curDrawable release];
    d->curDrawable = nil;

    QRHI_RES_RHI(QRhiMetal);
    if (rhiD) {
        rhiD->swapchains.remove(this);
        rhiD->unregisterResource(this);
    }
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6801
inline QRhiCommandBuffer *QMetalSwapChain::currentFrameCommandBuffer()
{
    return &cbWrapper;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6806
inline QRhiRenderTarget *QMetalSwapChain::currentFrameRenderTarget()
{
    return &rtWrapper;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6831
inline QRhiSwapChainProxyData QRhiMetal::updateSwapChainProxyData(QWindow *window)
{
    QRhiSwapChainProxyData d;
    d.reserved[0] = layerForWindow(window);
    return d;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6838
inline QSize QMetalSwapChain::surfacePixelSize()
{
    Q_ASSERT(m_window);
    CAMetalLayer *layer = d->layer;
    if (!layer)
        layer = qrhi_objectFromProxyData<CAMetalLayer>(&m_proxyData, m_window, QRhi::Metal, 0);

    Q_ASSERT(layer);
    int height = (int)layer.bounds.size.height;
    int width = (int)layer.bounds.size.width;
    width *= layer.contentsScale;
    height *= layer.contentsScale;
    return QSize(width, height);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6853
inline bool QMetalSwapChain::isFormatSupported(Format f)
{
    if (f == HDRExtendedSrgbLinear) {
        return hdrInfo().limits.colorComponentValue.maxPotentialColorComponentValue > 1.0f;
    } else if (f == HDR10) {
        return hdrInfo().limits.colorComponentValue.maxPotentialColorComponentValue > 1.0f;
    } else if (f == HDRExtendedDisplayP3Linear) {
        return hdrInfo().limits.colorComponentValue.maxPotentialColorComponentValue > 1.0f;
    }
    return f == SDR;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6865
inline QRhiRenderPassDescriptor *QMetalSwapChain::newCompatibleRenderPassDescriptor()
{
    QRHI_RES_RHI(QRhiMetal);

    chooseFormats(); // ensure colorFormat and similar are filled out

    QMetalRenderPassDescriptor *rpD = new QMetalRenderPassDescriptor(m_rhi);
    rpD->colorAttachmentCount = 1;
    rpD->hasDepthStencil = m_depthStencil != nullptr;

    rpD->colorFormat[0] = int(d->colorFormat);

#ifdef Q_OS_MACOS
    // m_depthStencil may not be built yet so cannot rely on computed fields in it
    rpD->dsFormat = rhiD->d->dev.depth24Stencil8PixelFormatSupported
            ? MTLPixelFormatDepth24Unorm_Stencil8 : MTLPixelFormatDepth32Float_Stencil8;
#else
    rpD->dsFormat = MTLPixelFormatDepth32Float_Stencil8;
#endif

    rpD->hasShadingRateMap = m_shadingRateMap != nullptr;

    rpD->updateSerializedFormat();

    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6893
inline void QMetalSwapChain::chooseFormats()
{
    QRHI_RES_RHI(QRhiMetal);
    samples = rhiD->effectiveSampleCount(m_sampleCount);
    // pick a format that is allowed for CAMetalLayer.pixelFormat
    if (m_format == HDRExtendedSrgbLinear || m_format == HDRExtendedDisplayP3Linear) {
        d->colorFormat = MTLPixelFormatRGBA16Float;
        d->rhiColorFormat = QRhiTexture::RGBA16F;
        return;
    }
    if (m_format == HDR10) {
        d->colorFormat = MTLPixelFormatRGB10A2Unorm;
        d->rhiColorFormat = QRhiTexture::RGB10A2;
        return;
    }
    d->colorFormat = m_flags.testFlag(sRGB) ? MTLPixelFormatBGRA8Unorm_sRGB : MTLPixelFormatBGRA8Unorm;
    d->rhiColorFormat = QRhiTexture::BGRA8;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6912
inline void QMetalSwapChain::waitUntilCompleted(int slot)
{
    // wait+signal is the general pattern to ensure the commands for a
    // given frame slot have completed (if sem is 1, we go 0 then 1; if
    // sem is 0 we go -1, block, completion increments to 0, then us to 1)

    dispatch_semaphore_t sem = d->sem[slot];
    dispatch_semaphore_wait(sem, DISPATCH_TIME_FOREVER);
    dispatch_semaphore_signal(sem);
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 6923
inline bool QMetalSwapChain::createOrResize()
{
    Q_ASSERT(m_window);

    const bool needsRegistration = !window || window != m_window;

    if (window && window != m_window)
        destroy();
    // else no destroy(), this is intentional

    QRHI_RES_RHI(QRhiMetal);
    if (needsRegistration || !rhiD->swapchains.contains(this))
        rhiD->swapchains.insert(this);

    window = m_window;

    if (window->surfaceType() != QSurface::MetalSurface) {
        qWarning("QMetalSwapChain only supports MetalSurface windows");
        return false;
    }

    d->layer = qrhi_objectFromProxyData<CAMetalLayer>(&m_proxyData, window, QRhi::Metal, 0);
    Q_ASSERT(d->layer);

    chooseFormats();
    if (d->colorFormat != d->layer.pixelFormat)
        d->layer.pixelFormat = d->colorFormat;

    if (m_format == HDRExtendedSrgbLinear) {
        d->layer.colorspace = CGColorSpaceCreateWithName(kCGColorSpaceExtendedLinearSRGB);
        d->layer.wantsExtendedDynamicRangeContent = YES;
    } else if (m_format == HDR10) {
        d->layer.colorspace = CGColorSpaceCreateWithName(kCGColorSpaceITUR_2100_PQ);
        d->layer.wantsExtendedDynamicRangeContent = YES;
    } else if (m_format == HDRExtendedDisplayP3Linear) {
        d->layer.colorspace = CGColorSpaceCreateWithName(kCGColorSpaceExtendedLinearDisplayP3);
        d->layer.wantsExtendedDynamicRangeContent = YES;
    }

    if (m_flags.testFlag(UsedAsTransferSource))
        d->layer.framebufferOnly = NO;

#ifdef Q_OS_MACOS
    if (m_flags.testFlag(NoVSync))
        d->layer.displaySyncEnabled = NO;
#endif

    if (m_flags.testFlag(SurfaceHasPreMulAlpha)) {
        d->layer.opaque = NO;
    } else if (m_flags.testFlag(SurfaceHasNonPreMulAlpha)) {
        // The CoreAnimation compositor is said to expect premultiplied alpha,
        // so this is then wrong when it comes to the blending operations but
        // there's nothing we can do. Fortunately Qt Quick always outputs
        // premultiplied alpha so it is not a problem there.
        d->layer.opaque = NO;
    } else {
        d->layer.opaque = YES;
    }

    // Now set the layer's drawableSize which will stay set to the same value
    // until the next createOrResize(), thus ensuring atomicity with regards to
    // the drawable size in frames.
    int width = (int)d->layer.bounds.size.width;
    int height = (int)d->layer.bounds.size.height;
    CGSize layerSize = CGSizeMake(width, height);
    const float scaleFactor = d->layer.contentsScale;
    layerSize.width *= scaleFactor;
    layerSize.height *= scaleFactor;
    d->layer.drawableSize = layerSize;

    m_currentPixelSize = QSizeF::fromCGSize(layerSize).toSize();
    pixelSize = m_currentPixelSize;

    [d->layer setDevice: rhiD->d->dev];

    [d->curDrawable release];
    d->curDrawable = nil;

    for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
        d->lastGpuTime[i] = 0;
        if (!d->sem[i])
            d->sem[i] = dispatch_semaphore_create(QMTL_FRAMES_IN_FLIGHT - 1);
    }

    currentFrameSlot = 0;
    frameCount = 0;

    ds = m_depthStencil ? QRHI_RES(QMetalRenderBuffer, m_depthStencil) : nullptr;
    if (m_depthStencil && m_depthStencil->sampleCount() != m_sampleCount) {
        qWarning("Depth-stencil buffer's sampleCount (%d) does not match color buffers' sample count (%d). Expect problems.",
                 m_depthStencil->sampleCount(), m_sampleCount);
    }
    if (m_depthStencil && m_depthStencil->pixelSize() != pixelSize) {
        if (m_depthStencil->flags().testFlag(QRhiRenderBuffer::UsedWithSwapChainOnly)) {
            m_depthStencil->setPixelSize(pixelSize);
            if (!m_depthStencil->create())
                qWarning("Failed to rebuild swapchain's associated depth-stencil buffer for size %dx%d",
                         pixelSize.width(), pixelSize.height());
        } else {
            qWarning("Depth-stencil buffer's size (%dx%d) does not match the layer size (%dx%d). Expect problems.",
                     m_depthStencil->pixelSize().width(), m_depthStencil->pixelSize().height(),
                     pixelSize.width(), pixelSize.height());
        }
    }

    rtWrapper.setRenderPassDescriptor(m_renderPassDesc); // for the public getter in QRhiRenderTarget
    rtWrapper.d->pixelSize = pixelSize;
    rtWrapper.d->dpr = scaleFactor;
    rtWrapper.d->sampleCount = samples;
    rtWrapper.d->colorAttCount = 1;
    rtWrapper.d->dsAttCount = ds ? 1 : 0;

    qCDebug(QRHI_LOG_INFO, "got CAMetalLayer, pixel size %dx%d (scale %.2f)",
            pixelSize.width(), pixelSize.height(), scaleFactor);

    if (samples > 1) {
        MTLTextureDescriptor *desc = [[MTLTextureDescriptor alloc] init];
        desc.textureType = MTLTextureType2DMultisample;
        desc.pixelFormat = d->colorFormat;
        desc.width = NSUInteger(pixelSize.width());
        desc.height = NSUInteger(pixelSize.height());
        desc.sampleCount = NSUInteger(samples);
        desc.resourceOptions = MTLResourceStorageModePrivate;
        desc.storageMode = MTLStorageModePrivate;
        desc.usage = MTLTextureUsageRenderTarget;
        for (int i = 0; i < QMTL_FRAMES_IN_FLIGHT; ++i) {
            if (d->msaaTex[i]) {
                QRhiMetalData::DeferredReleaseEntry e;
                e.type = QRhiMetalData::DeferredReleaseEntry::RenderBuffer;
                e.lastActiveFrameSlot = 1; // because currentFrameSlot is reset to 0
                e.renderbuffer.texture = d->msaaTex[i];
                rhiD->d->releaseQueue.append(e);
            }
            d->msaaTex[i] = [rhiD->d->dev newTextureWithDescriptor: desc];
        }
        [desc release];
    }

    rhiD->registerResource(this);

    return true;
}

//  from qtbase/src/gui/rhi/qrhimetal.mm, line 7066
inline QRhiSwapChainHdrInfo QMetalSwapChain::hdrInfo()
{
    QRhiSwapChainHdrInfo info;
    info.limitsType = QRhiSwapChainHdrInfo::ColorComponentValue;
    info.limits.colorComponentValue.maxColorComponentValue = 1;
    info.limits.colorComponentValue.maxPotentialColorComponentValue = 1;
    info.luminanceBehavior = QRhiSwapChainHdrInfo::DisplayReferred; // 1.0 = SDR white
    info.sdrWhiteLevel = 200; // typical value, but dummy (don't know the real one); won't matter due to being display-referred

    if (m_window) {
        // Must use m_window, not window, given this may be called before createOrResize().
#if defined(Q_OS_MACOS)
        NSView *view = reinterpret_cast<NSView *>(m_window->winId());
        NSScreen *screen = view.window.screen;
        info.limits.colorComponentValue.maxColorComponentValue = screen.maximumExtendedDynamicRangeColorComponentValue;
        info.limits.colorComponentValue.maxPotentialColorComponentValue = screen.maximumPotentialExtendedDynamicRangeColorComponentValue;
#elif defined(Q_OS_IOS)
        UIView *view = reinterpret_cast<UIView *>(m_window->winId());
        UIScreen *screen = view.window.windowScene.screen;
        info.limits.colorComponentValue.maxColorComponentValue =
                view.window.windowScene.screen.currentEDRHeadroom;
        info.limits.colorComponentValue.maxPotentialColorComponentValue =
                screen.potentialEDRHeadroom;
#endif
    }

    return info;
}

QT_END_NAMESPACE
//  ---------------------------------------------------------------------

//  void QMetalCommandBuffer::resetState(double lastGpuTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMetalCommandBuffer10resetStateEd(
    QMetalCommandBuffer *self,
    double lastGpuTime) {
  self->resetState(lastGpuTime);
}

//  void QMetalCommandBuffer::resetPerPassState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMetalCommandBuffer17resetPerPassStateEv(
    QMetalCommandBuffer *self) {
  self->resetPerPassState();
}

//  void QMetalCommandBuffer::resetPerPassCachedState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMetalCommandBuffer23resetPerPassCachedStateEv(
    QMetalCommandBuffer *self) {
  self->resetPerPassCachedState();
}

//  void QMetalSwapChain::chooseFormats()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMetalSwapChain13chooseFormatsEv(
    QMetalSwapChain *self) {
  self->chooseFormats();
}

//  void QMetalSwapChain::waitUntilCompleted(int slot)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMetalSwapChain18waitUntilCompletedEi(
    QMetalSwapChain *self,
    int slot) {
  self->waitUntilCompleted(slot);
}

//  void QMetalRenderPassDescriptor::updateSerializedFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QMetalRenderPassDescriptor22updateSerializedFormatEv(
    QMetalRenderPassDescriptor *self) {
  self->updateSerializedFormat();
}

//  bool QMetalTexture::prepareCreate(QSize *adjustedSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMetalTexture13prepareCreateEP5QSize(
    QMetalTexture *self,
    QSize *adjustedSize) {
  return self->prepareCreate(adjustedSize);
}

//  void QMetalGraphicsPipeline::mapStates()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMetalGraphicsPipeline9mapStatesEv(
    QMetalGraphicsPipeline *self) {
  self->mapStates();
}

//  void QMetalGraphicsPipeline::setupMetalDepthStencilDescriptor(void
//      *metalDsDesc)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMetalGraphicsPipeline32setupMetalDepthStencilDescriptorEPv(
    QMetalGraphicsPipeline *self,
    void *metalDsDesc) {
  self->setupMetalDepthStencilDescriptor(metalDsDesc);
}

//  static bool QRhiMetal::probe(QRhiMetalInitParams *params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiMetal5probeEP19QRhiMetalInitParams(
    QRhiMetalInitParams *params) {
  return QRhiMetal::probe(params);
}

//  void QRhiMetal::executeDeferredReleases(bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal23executeDeferredReleasesEb(
    QRhiMetal *self,
    bool forced) {
  self->executeDeferredReleases(forced);
}

//  void QRhiMetal::finishActiveReadbacks(bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal21finishActiveReadbacksEb(
    QRhiMetal *self,
    bool forced) {
  self->finishActiveReadbacks(forced);
}

//  qsizetype QRhiMetal::subresUploadByteSize(const
//      QRhiTextureSubresourceUploadDescription &subresDesc) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QRhiMetal20subresUploadByteSizeERK39QRhiTextureSubresourceUploadDescription(
    const QRhiMetal *self,
    const QRhiTextureSubresourceUploadDescription *subresDesc) {
  return self->subresUploadByteSize(*subresDesc);
}

//  void QRhiMetal::executeBufferHostWritesForSlot(QMetalBuffer *bufD, int
//      slot)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal30executeBufferHostWritesForSlotEP12QMetalBufferi(
    QRhiMetal *self,
    QMetalBuffer *bufD,
    int slot) {
  self->executeBufferHostWritesForSlot(bufD, slot);
}

//  void QRhiMetal::executeBufferHostWritesForCurrentFrame(QMetalBuffer
//      *bufD)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal38executeBufferHostWritesForCurrentFrameEP12QMetalBuffer(
    QRhiMetal *self,
    QMetalBuffer *bufD) {
  self->executeBufferHostWritesForCurrentFrame(bufD);
}

//  void QRhiMetal::setDefaultScissor(QMetalCommandBuffer *cbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal17setDefaultScissorEP19QMetalCommandBuffer(
    QRhiMetal *self,
    QMetalCommandBuffer *cbD) {
  self->setDefaultScissor(cbD);
}

//  void QRhiMetal::finalizeDeferredStoreActions(QMetalCommandBuffer *cbD,
//      bool passIsEnding)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal28finalizeDeferredStoreActionsEP19QMetalCommandBufferb(
    QRhiMetal *self,
    QMetalCommandBuffer *cbD,
    bool passIsEnding) {
  self->finalizeDeferredStoreActions(cbD, passIsEnding);
}

//  void QRhiMetal::interruptRenderPass(QMetalCommandBuffer *cbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal19interruptRenderPassEP19QMetalCommandBuffer(
    QRhiMetal *self,
    QMetalCommandBuffer *cbD) {
  self->interruptRenderPass(cbD);
}

//  void QRhiMetal::adjustForMultiViewDraw(quint32 *instanceCount,
//      QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal22adjustForMultiViewDrawEPjP17QRhiCommandBuffer(
    QRhiMetal *self,
    quint32 *instanceCount,
    QRhiCommandBuffer *cb) {
  self->adjustForMultiViewDraw(instanceCount, cb);
}

//  static QRhiSwapChainProxyData QRhiMetal::updateSwapChainProxyData(QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QRhiSwapChainProxyData *ritual_ZN9QRhiMetal24updateSwapChainProxyDataEP7QWindow(
    QWindow *window) {
  return new QRhiSwapChainProxyData(
      QRhiMetal::updateSwapChainProxyData(window));
}

//  void QMetalGraphicsPipeline::makeActiveForCurrentRenderPassEncoder(QMetal
//      CommandBuffer *cbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMetalGraphicsPipeline37makeActiveForCurrentRenderPassEncoderEP19QMetalCommandBuffer(
    QMetalGraphicsPipeline *self,
    QMetalCommandBuffer *cbD) {
  self->makeActiveForCurrentRenderPassEncoder(cbD);
}

//  void
//      QMetalGraphicsPipeline::setupAttachmentsInMetalRenderPassDescriptor(v
//      oid *metalRpDesc, QMetalRenderPassDescriptor *rpD)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMetalGraphicsPipeline43setupAttachmentsInMetalRenderPassDescriptorEPvP26QMetalRenderPassDescriptor(
    QMetalGraphicsPipeline *self,
    void *metalRpDesc,
    QMetalRenderPassDescriptor *rpD) {
  self->setupAttachmentsInMetalRenderPassDescriptor(metalRpDesc, rpD);
}

//  bool QMetalGraphicsPipeline::createVertexFragmentPipeline()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QMetalGraphicsPipeline28createVertexFragmentPipelineEv(
    QMetalGraphicsPipeline *self) {
  return self->createVertexFragmentPipeline();
}

//  bool QMetalGraphicsPipeline::createTessellationPipelines(const QShader
//      &tessVert, const QShader &tesc, const QShader &tese, const QShader
//      &tessFrag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QMetalGraphicsPipeline27createTessellationPipelinesERK7QShaderS2_S2_S2_(
    QMetalGraphicsPipeline *self,
    const QShader *tessVert,
    const QShader *tesc,
    const QShader *tese,
    const QShader *tessFrag) {
  return self->createTessellationPipelines(
      *tessVert, *tesc, *tese, *tessFrag);
}

//  void QRhiMetal::enqueueSubresUpload(QMetalTexture *texD, void *mp, void
//      *blitEncPtr, int layer, int level, const
//      QRhiTextureSubresourceUploadDescription &subresDesc, qsizetype
//      *curOfs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal19enqueueSubresUploadEP13QMetalTexturePvS2_iiRK39QRhiTextureSubresourceUploadDescriptionPx(
    QRhiMetal *self,
    QMetalTexture *texD,
    void *mp,
    void *blitEncPtr,
    int layer,
    int level,
    const QRhiTextureSubresourceUploadDescription *subresDesc,
    qsizetype *curOfs) {
  self->enqueueSubresUpload(
      texD, mp, blitEncPtr, layer, level, *subresDesc, curOfs);
}

//  void QRhiMetal::enqueueResourceUpdates(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal22enqueueResourceUpdatesEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->enqueueResourceUpdates(cb, resourceUpdates);
}

//  void QRhiMetal::tessellatedDraw(const TessDrawArgs &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal15tessellatedDrawERKNS_12TessDrawArgsE(
    QRhiMetal *self,
    const QRhiMetal::TessDrawArgs *args) {
  self->tessellatedDraw(*args);
}

//  QMetalBuffer::QMetalBuffer(QRhiImplementation *rhi, Type type, UsageFlags
//      usage, quint32 size)
extern "C" Q_DECL_EXPORT
QMetalBuffer *ritual_ZN12QMetalBufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj(
    QRhiImplementation *rhi,
    int type,
    int usage,
    quint32 size) {
  return new QMetalBuffer(
      rhi, static_cast<QRhiBuffer::Type>(type),
      QRhiBuffer::UsageFlags::fromInt(usage), size);
}

//  QMetalCommandBuffer::QMetalCommandBuffer(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QMetalCommandBuffer *ritual_ZN19QMetalCommandBufferC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalCommandBuffer(rhi);
}

//  QMetalComputePipeline::QMetalComputePipeline(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QMetalComputePipeline *ritual_ZN21QMetalComputePipelineC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalComputePipeline(rhi);
}

//  QMetalRenderBuffer::QMetalRenderBuffer(QRhiImplementation *rhi, Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QMetalRenderBuffer *ritual_ZN18QMetalRenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE(
    QRhiImplementation *rhi,
    int type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    int backingFormatHint) {
  return new QMetalRenderBuffer(
      rhi, static_cast<QRhiRenderBuffer::Type>(type), *pixelSize,
      sampleCount, QRhiRenderBuffer::Flags::fromInt(flags),
      static_cast<QRhiTexture::Format>(backingFormatHint));
}

//  QMetalRenderPassDescriptor::QMetalRenderPassDescriptor(QRhiImplementation
//      *rhi)
extern "C" Q_DECL_EXPORT
QMetalRenderPassDescriptor *ritual_ZN26QMetalRenderPassDescriptorC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalRenderPassDescriptor(rhi);
}

//  QMetalSampler::QMetalSampler(QRhiImplementation *rhi, Filter magFilter,
//      Filter minFilter, Filter mipmapMode, AddressMode u, AddressMode v,
//      AddressMode w)
extern "C" Q_DECL_EXPORT
QMetalSampler *ritual_ZN13QMetalSamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_(
    QRhiImplementation *rhi,
    int magFilter,
    int minFilter,
    int mipmapMode,
    int u,
    int v,
    int w) {
  using Sampler = QRhiSampler;
  return new QMetalSampler(
      rhi, static_cast<Sampler::Filter>(magFilter),
      static_cast<Sampler::Filter>(minFilter),
      static_cast<Sampler::Filter>(mipmapMode),
      static_cast<Sampler::AddressMode>(u),
      static_cast<Sampler::AddressMode>(v),
      static_cast<Sampler::AddressMode>(w));
}

//  QMetalShaderResourceBindings::QMetalShaderResourceBindings(QRhiImplementa
//      tion *rhi)
extern "C" Q_DECL_EXPORT
QMetalShaderResourceBindings *ritual_ZN28QMetalShaderResourceBindingsC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalShaderResourceBindings(rhi);
}

//  QMetalShadingRateMap::QMetalShadingRateMap(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QMetalShadingRateMap *ritual_ZN20QMetalShadingRateMapC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalShadingRateMap(rhi);
}

//  QMetalSwapChain::QMetalSwapChain(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QMetalSwapChain *ritual_ZN15QMetalSwapChainC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalSwapChain(rhi);
}

//  QMetalTexture::QMetalTexture(QRhiImplementation *rhi, Format format,
//      const QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      Flags flags)
extern "C" Q_DECL_EXPORT
QMetalTexture *ritual_ZN13QMetalTextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE(
    QRhiImplementation *rhi,
    int format,
    const QSize *pixelSize,
    int depth,
    int arraySize,
    int sampleCount,
    int flags) {
  return new QMetalTexture(
      rhi, static_cast<QRhiTexture::Format>(format), *pixelSize, depth,
      arraySize, sampleCount, QRhiTexture::Flags::fromInt(flags));
}

//  QMetalTextureRenderTarget::QMetalTextureRenderTarget(QRhiImplementation
//      *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)
extern "C" Q_DECL_EXPORT
QMetalTextureRenderTarget *ritual_ZN25QMetalTextureRenderTargetC1EP18QRhiImplementationRK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiImplementation *rhi,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return new QMetalTextureRenderTarget(
      rhi, *desc, QRhiTextureRenderTarget::Flags::fromInt(flags));
}

//  QMetalGraphicsPipeline::QMetalGraphicsPipeline(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QMetalGraphicsPipeline *ritual_ZN22QMetalGraphicsPipelineC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new QMetalGraphicsPipeline(rhi);
}

//  QMetalSwapChainRenderTarget::QMetalSwapChainRenderTarget(QRhiImplementati
//      on *rhi, QRhiSwapChain *swapchain)
extern "C" Q_DECL_EXPORT
QMetalSwapChainRenderTarget *ritual_ZN27QMetalSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain(
    QRhiImplementation *rhi,
    QRhiSwapChain *swapchain) {
  return new QMetalSwapChainRenderTarget(rhi, swapchain);
}

//  QRhiMetal::QRhiMetal(QRhiMetalInitParams *params, QRhiMetalNativeHandles
//      *importDevice)
extern "C" Q_DECL_EXPORT
QRhiMetal *ritual_ZN9QRhiMetalC1EP19QRhiMetalInitParamsP22QRhiMetalNativeHandles(
    QRhiMetalInitParams *params,
    QRhiMetalNativeHandles *importDevice) {
  return new QRhiMetal(params, importDevice);
}

#endif
