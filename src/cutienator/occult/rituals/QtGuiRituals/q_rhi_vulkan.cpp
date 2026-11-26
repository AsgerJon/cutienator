//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands also under
//  '__has_include(<vulkan/vulkan.h>)', as Qt's 'qvulkaninstance.h'
//  checks it, since 'qrhivulkan_p.h' needs Vulkan's headers, which a
//  machine may lack though its Qt was built with Vulkan. Kept as it is
//  when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 7835, as _ZN10QVkSamplerC1EP18QRhiImplementationN11QRhiSampler6FilterES3_S3_NS2_11AddressModeES4_S4_
inline QVkSampler::QVkSampler(QRhiImplementation *rhi, Filter magFilter, Filter minFilter, Filter mipmapMode,
                       AddressMode u, AddressMode v, AddressMode w)
    : QRhiSampler(rhi, magFilter, minFilter, mipmapMode, u, v, w)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7470, as _ZN10QVkTextureC1EP18QRhiImplementationN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS2_4FlagEE
inline QVkTexture::QVkTexture(QRhiImplementation *rhi, Format format, const QSize &pixelSize, int depth,
                       int arraySize, int sampleCount, Flags flags)
    : QRhiTexture(rhi, format, pixelSize, depth, arraySize, sampleCount, flags)
{
    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        stagingBuffers[i] = VK_NULL_HANDLE;
        stagingAllocations[i] = nullptr;
    }
    for (int i = 0; i < QRhi::MAX_MIP_LEVELS; ++i)
        perLevelImageViews[i] = VK_NULL_HANDLE;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9109, as _ZN12QVkSwapChainC1EP18QRhiImplementation
inline QVkSwapChain::QVkSwapChain(QRhiImplementation *rhi)
    : QRhiSwapChain(rhi),
      rtWrapper(rhi, this),
      rtWrapperRight(rhi, this),
      cbWrapper(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7361, as _ZN15QVkRenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE
inline QVkRenderBuffer::QVkRenderBuffer(QRhiImplementation *rhi, Type type, const QSize &pixelSize,
                                 int sampleCount, Flags flags,
                                 QRhiTexture::Format backingFormatHint)
    : QRhiRenderBuffer(rhi, type, pixelSize, sampleCount, flags, backingFormatHint)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9089, as _ZN16QVkCommandBuffer13nativeHandlesEv
inline const QRhiNativeHandles *QVkCommandBuffer::nativeHandles()
{
    // Ok this is messy but no other way has been devised yet. Outside
    // begin(Compute)Pass - end(Compute)Pass it is simple - just return the
    // primary VkCommandBuffer. Inside, however, we need to provide the current
    // secondary command buffer (typically the one started by beginExternal(),
    // in case we are between beginExternal - endExternal inside a pass).

    if (recordingPass == QVkCommandBuffer::NoPass) {
        nativeHandlesStruct.commandBuffer = cb;
    } else {
        if (passUsesSecondaryCb && !activeSecondaryCbStack.isEmpty())
            nativeHandlesStruct.commandBuffer = activeSecondaryCbStack.last();
        else
            nativeHandlesStruct.commandBuffer = cb;
    }

    return &nativeHandlesStruct;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9073, as _ZN16QVkCommandBufferC1EP18QRhiImplementation
inline QVkCommandBuffer::QVkCommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8141, as _ZN17QVkShadingRateMapC1EP18QRhiImplementation
inline QVkShadingRateMap::QVkShadingRateMap(QRhiImplementation *rhi)
    : QRhiShadingRateMap(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8967, as _ZN18QVkComputePipelineC1EP18QRhiImplementation
inline QVkComputePipeline::QVkComputePipeline(QRhiImplementation *rhi)
    : QRhiComputePipeline(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8672, as _ZN19QVkGraphicsPipelineC1EP18QRhiImplementation
inline QVkGraphicsPipeline::QVkGraphicsPipeline(QRhiImplementation *rhi)
    : QRhiGraphicsPipeline(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8199, as _ZN22QVkTextureRenderTargetC1EP18QRhiImplementationRK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QVkTextureRenderTarget::QVkTextureRenderTarget(QRhiImplementation *rhi,
                                               const QRhiTextureRenderTargetDescription &desc,
                                               Flags flags)
    : QRhiTextureRenderTarget(rhi, desc, flags)
{
    for (int att = 0; att < QVkRenderTargetData::MAX_COLOR_ATTACHMENTS; ++att) {
        rtv[att] = VK_NULL_HANDLE;
        resrtv[att] = VK_NULL_HANDLE;
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8523, as _ZN25QVkShaderResourceBindingsC1EP18QRhiImplementation
inline QVkShaderResourceBindings::QVkShaderResourceBindings(QRhiImplementation *rhi)
    : QRhiShaderResourceBindings(rhi)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7206, as _ZN9QVkBufferC1EP18QRhiImplementationN10QRhiBuffer4TypeE6QFlagsINS2_9UsageFlagEEj
inline QVkBuffer::QVkBuffer(QRhiImplementation *rhi, Type type, UsageFlags usage, quint32 size)
    : QRhiBuffer(rhi, type, usage, size)
{
    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        buffers[i] = stagingBuffers[i] = VK_NULL_HANDLE;
        allocations[i] = stagingAllocations[i] = nullptr;
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8169, as _ZN24QVkSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QVkSwapChainRenderTarget::QVkSwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8174, as _ZN24QVkSwapChainRenderTargetD1Ev
inline QVkSwapChainRenderTarget::~QVkSwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5896, as _ZN10QRhiVulkan22createGraphicsPipelineEv
inline QRhiGraphicsPipeline *QRhiVulkan::createGraphicsPipeline()
{
    return new QVkGraphicsPipeline(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5901, as _ZN10QRhiVulkan21createComputePipelineEv
inline QRhiComputePipeline *QRhiVulkan::createComputePipeline()
{
    return new QVkComputePipeline(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5906, as _ZN10QRhiVulkan28createShaderResourceBindingsEv
inline QRhiShaderResourceBindings *QRhiVulkan::createShaderResourceBindings()
{
    return new QVkShaderResourceBindings(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5457, as _ZN10QRhiVulkan12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj
inline QRhiBuffer *QRhiVulkan::createBuffer(QRhiBuffer::Type type, QRhiBuffer::UsageFlags usage, quint32 size)
{
    return new QVkBuffer(this, type, usage, size);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5864, as _ZN10QRhiVulkan18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE
inline QRhiRenderBuffer *QRhiVulkan::createRenderBuffer(QRhiRenderBuffer::Type type, const QSize &pixelSize,
                                                 int sampleCount, QRhiRenderBuffer::Flags flags,
                                                 QRhiTexture::Format backingFormatHint)
{
    return new QVkRenderBuffer(this, type, pixelSize, sampleCount, flags, backingFormatHint);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5871, as _ZN10QRhiVulkan13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE
inline QRhiTexture *QRhiVulkan::createTexture(QRhiTexture::Format format,
                                       const QSize &pixelSize, int depth, int arraySize,
                                       int sampleCount, QRhiTexture::Flags flags)
{
    return new QVkTexture(this, format, pixelSize, depth, arraySize, sampleCount, flags);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5878, as _ZN10QRhiVulkan13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_
inline QRhiSampler *QRhiVulkan::createSampler(QRhiSampler::Filter magFilter, QRhiSampler::Filter minFilter,
                                       QRhiSampler::Filter mipmapMode,
                                       QRhiSampler::AddressMode u, QRhiSampler::AddressMode v, QRhiSampler::AddressMode w)
{
    return new QVkSampler(this, magFilter, minFilter, mipmapMode, u, v, w);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5890, as _ZN10QRhiVulkan25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE
inline QRhiTextureRenderTarget *QRhiVulkan::createTextureRenderTarget(const QRhiTextureRenderTargetDescription &desc,
                                                               QRhiTextureRenderTarget::Flags flags)
{
    return new QVkTextureRenderTarget(this, desc, flags);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5885, as _ZN10QRhiVulkan20createShadingRateMapEv
inline QRhiShadingRateMap *QRhiVulkan::createShadingRateMap()
{
    return new QVkShadingRateMap(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5444, as _ZN10QRhiVulkan15createSwapChainEv
inline QRhiSwapChain *QRhiVulkan::createSwapChain()
{
    if (!vkGetPhysicalDeviceSurfaceCapabilitiesKHR
        || !vkGetPhysicalDeviceSurfaceFormatsKHR
        || !vkGetPhysicalDeviceSurfacePresentModesKHR)
    {
        qWarning("Physical device surface queries not available");
        return nullptr;
    }

    return new QVkSwapChain(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3306, as _ZN10QRhiVulkan14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiVulkan::resourceUpdate(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::NoPass);

    enqueueResourceUpdates(cbD, resourceUpdates);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3373, as _ZN10QRhiVulkan9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiVulkan::beginPass(QRhiCommandBuffer *cb,
                           QRhiRenderTarget *rt,
                           const QColor &colorClearValue,
                           const QRhiDepthStencilClearValue &depthStencilClearValue,
                           QRhiResourceUpdateBatch *resourceUpdates,
                           QRhiCommandBuffer::BeginPassFlags flags)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cbD, resourceUpdates);

    // Insert a TransitionPassResources into the command stream, pointing to
    // the tracker this pass is going to use. That's how we generate the
    // barriers later during recording the real VkCommandBuffer, right before
    // the vkCmdBeginRenderPass.
    enqueueTransitionPassResources(cbD);

    QVkRenderTargetData *rtD = nullptr;
    switch (rt->resourceType()) {
    case QRhiResource::SwapChainRenderTarget:
        rtD = &QRHI_RES(QVkSwapChainRenderTarget, rt)->d;
        rtD->rp->lastActiveFrameSlot = currentFrameSlot;
        Q_ASSERT(currentSwapChain);
        currentSwapChain->imageRes[currentSwapChain->currentImageIndex].lastUse =
                QVkSwapChain::ImageResources::ScImageUseRender;
        if (currentSwapChain->shadingRateMapView) {
            QVkTexture *texD = QRHI_RES(QVkShadingRateMap, currentSwapChain->shadingRateMap())->texture;
            QRhiPassResourceTracker &passResTracker(cbD->passResTrackers[cbD->currentPassResTrackerIndex]);
            trackedRegisterTexture(&passResTracker, texD,
                                   QRhiPassResourceTracker::TexShadingRate,
                                   QRhiPassResourceTracker::TexColorOutputStage);
            texD->lastActiveFrameSlot = currentFrameSlot;
        }
        break;
    case QRhiResource::TextureRenderTarget:
    {
        QVkTextureRenderTarget *rtTex = QRHI_RES(QVkTextureRenderTarget, rt);
        rtD = &rtTex->d;
        activateTextureRenderTarget(cbD, rtTex);
    }
        break;
    default:
        Q_UNREACHABLE();
        break;
    }

    cbD->recordingPass = QVkCommandBuffer::RenderPass;
    cbD->passUsesSecondaryCb = flags.testFlag(QRhiCommandBuffer::ExternalContent);
    cbD->currentTarget = rt;

    // No copy operations or image layout transitions allowed after this point
    // (up until endPass) as we are going to begin the renderpass.

    VkRenderPassBeginInfo rpBeginInfo = {};
    rpBeginInfo.sType = VK_STRUCTURE_TYPE_RENDER_PASS_BEGIN_INFO;
    rpBeginInfo.renderPass = rtD->rp->rp;
    rpBeginInfo.framebuffer = rtD->fb;
    rpBeginInfo.renderArea.extent.width = uint32_t(rtD->pixelSize.width());
    rpBeginInfo.renderArea.extent.height = uint32_t(rtD->pixelSize.height());

    const bool rpHasAnyClearOp = std::any_of(rtD->rp->attDescs.cbegin(), rtD->rp->attDescs.cend(),
                                             [](const VkAttachmentDescription &attDesc) {
        return (attDesc.loadOp == VK_ATTACHMENT_LOAD_OP_CLEAR
                || attDesc.stencilLoadOp == VK_ATTACHMENT_LOAD_OP_CLEAR);
    });

    QVarLengthArray<VkClearValue, (QVkRenderTargetData::MAX_COLOR_ATTACHMENTS + 1) * 2 + 1> cvs;
    if (rpHasAnyClearOp) {
        for (int i = 0; i < rtD->colorAttCount; ++i) {
            VkClearValue cv = {};
            cv.color = { { colorClearValue.redF(), colorClearValue.greenF(), colorClearValue.blueF(),
                           colorClearValue.alphaF() } };
            cvs.append(cv);
        }
        for (int i = 0; i < rtD->dsAttCount; ++i) {
            VkClearValue cv = {};
            cv.depthStencil = { depthStencilClearValue.depthClearValue(), depthStencilClearValue.stencilClearValue() };
            cvs.append(cv);
        }
        for (int i = 0; i < rtD->resolveAttCount; ++i) {
            VkClearValue cv = {};
            cv.color = { { colorClearValue.redF(), colorClearValue.greenF(), colorClearValue.blueF(),
                           colorClearValue.alphaF() } };
            cvs.append(cv);
        }
        for (int i = 0; i < rtD->dsResolveAttCount; ++i) {
            VkClearValue cv = {};
            cv.depthStencil = { depthStencilClearValue.depthClearValue(), depthStencilClearValue.stencilClearValue() };
            cvs.append(cv);
        }
        for (int i = 0; i < rtD->shadingRateAttCount; ++i) {
            VkClearValue cv = {};
            cv.color = { { 0.0f, 0.0f, 0.0f, 0.0f } };
            cvs.append(cv);
        }
    }
    Q_ASSERT(!rpHasAnyClearOp || cvs.size() == rtD->rp->attDescs.size());
    rpBeginInfo.clearValueCount = uint32_t(cvs.size());

    QVkCommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QVkCommandBuffer::Command::BeginRenderPass;
    cmd.args.beginRenderPass.desc = rpBeginInfo;
    cmd.args.beginRenderPass.clearValueIndex = cbD->pools.clearValue.size();
    cmd.args.beginRenderPass.useSecondaryCb = cbD->passUsesSecondaryCb;
    cbD->pools.clearValue.append(cvs.constData(), cvs.size());

    if (cbD->passUsesSecondaryCb)
        cbD->activeSecondaryCbStack.append(startSecondaryCommandBuffer(rtD));

    if (cbD->hasShadingRateSet) {
        QVkCommandBuffer::Command &rateCmd(cbD->commands.get());
        rateCmd.cmd = QVkCommandBuffer::Command::SetShadingRate;
        rateCmd.args.setShadingRate.w = 1;
        rateCmd.args.setShadingRate.h = 1;
    }

    cbD->resetPerPassState();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3494, as _ZN10QRhiVulkan7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiVulkan::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::RenderPass);

    if (cbD->passUsesSecondaryCb) {
        VkCommandBuffer secondaryCb = cbD->activeSecondaryCbStack.last();
        cbD->activeSecondaryCbStack.removeLast();
        endAndEnqueueSecondaryCommandBuffer(secondaryCb, cbD);
    }

    QVkCommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QVkCommandBuffer::Command::EndRenderPass;

    cbD->recordingPass = QVkCommandBuffer::NoPass;
    cbD->currentTarget = nullptr;

    if (resourceUpdates)
        enqueueResourceUpdates(cbD, resourceUpdates);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6432, as _ZN10QRhiVulkan14setShadingRateEP17QRhiCommandBufferRK5QSize
inline void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const QSize &coarsePixelSize)
{
#ifdef VK_KHR_fragment_shading_rate
    if (!vkCmdSetFragmentShadingRateKHR)
        return;

    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::RenderPass);
    Q_ASSERT(!cbD->currentGraphicsPipeline || QRHI_RES(QVkGraphicsPipeline, cbD->currentGraphicsPipeline)->m_flags.testFlag(QRhiGraphicsPipeline::UsesShadingRate));

    VkFragmentShadingRateCombinerOpKHR ops[2] = {
        VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR,
        VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR
    };
    VkExtent2D size = { uint32_t(coarsePixelSize.width()), uint32_t(coarsePixelSize.height()) };
    if (cbD->passUsesSecondaryCb) {
        vkCmdSetFragmentShadingRateKHR(cbD->activeSecondaryCbStack.last(), &size, ops);
    } else {
        QVkCommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QVkCommandBuffer::Command::SetShadingRate;
        cmd.args.setShadingRate.w = size.width;
        cmd.args.setShadingRate.h = size.height;
    }
    if (coarsePixelSize.width() != 1 || coarsePixelSize.height() != 1)
        cbD->hasShadingRateSet = true;
#else
    Q_UNUSED(cb);
    Q_UNUSED(coarsePixelSize);
#endif
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6609, as _ZN10QRhiVulkan14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray
inline void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray &name)
{
#ifdef VK_EXT_debug_utils
    if (!debugMarkers || !caps.debugUtils)
        return;

    VkDebugUtilsLabelEXT label = {};
    label.sType = VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT;

    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    if (cbD->recordingPass != QVkCommandBuffer::NoPass && cbD->passUsesSecondaryCb) {
        label.pLabelName = name.constData();
        vkCmdBeginDebugUtilsLabelEXT(cbD->activeSecondaryCbStack.last(), &label);
    } else {
        QVkCommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QVkCommandBuffer::Command::DebugMarkerBegin;
        cmd.args.debugMarkerBegin.label = label;
        cmd.args.debugMarkerBegin.labelNameIndex = cbD->pools.debugMarkerData.size();
        cbD->pools.debugMarkerData.append(name);
    }
#else
    Q_UNUSED(cb);
    Q_UNUSED(name);
#endif
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6635, as _ZN10QRhiVulkan12debugMarkEndEP17QRhiCommandBuffer
inline void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)
{
#ifdef VK_EXT_debug_utils
    if (!debugMarkers || !caps.debugUtils)
        return;

    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    if (cbD->recordingPass != QVkCommandBuffer::NoPass && cbD->passUsesSecondaryCb) {
        vkCmdEndDebugUtilsLabelEXT(cbD->activeSecondaryCbStack.last());
    } else {
        QVkCommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QVkCommandBuffer::Command::DebugMarkerEnd;
    }
#else
    Q_UNUSED(cb);
#endif
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6653, as _ZN10QRhiVulkan12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray
inline void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg)
{
#ifdef VK_EXT_debug_utils
    if (!debugMarkers || !caps.debugUtils)
        return;

    VkDebugUtilsLabelEXT label = {};
    label.sType = VK_STRUCTURE_TYPE_DEBUG_UTILS_LABEL_EXT;

    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    if (cbD->recordingPass != QVkCommandBuffer::NoPass && cbD->passUsesSecondaryCb) {
        label.pLabelName = msg.constData();
        vkCmdInsertDebugUtilsLabelEXT(cbD->activeSecondaryCbStack.last(), &label);
    } else {
        QVkCommandBuffer::Command &cmd(cbD->commands.get());
        cmd.cmd = QVkCommandBuffer::Command::DebugMarkerInsert;
        cmd.args.debugMarkerInsert.label = label;
        cmd.args.debugMarkerInsert.labelNameIndex = cbD->pools.debugMarkerData.size();
        cbD->pools.debugMarkerData.append(msg);
    }
#else
    Q_UNUSED(cb);
    Q_UNUSED(msg);
#endif
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3515, as _ZN10QRhiVulkan16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE
inline void QRhiVulkan::beginComputePass(QRhiCommandBuffer *cb,
                                  QRhiResourceUpdateBatch *resourceUpdates,
                                  QRhiCommandBuffer::BeginPassFlags flags)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::NoPass);

    if (resourceUpdates)
        enqueueResourceUpdates(cbD, resourceUpdates);

    enqueueTransitionPassResources(cbD);

    cbD->recordingPass = QVkCommandBuffer::ComputePass;
    cbD->passUsesSecondaryCb = flags.testFlag(QRhiCommandBuffer::ExternalContent);

    cbD->computePassState.reset();

    if (cbD->passUsesSecondaryCb)
        cbD->activeSecondaryCbStack.append(startSecondaryCommandBuffer());

    cbD->resetPerPassState();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3538, as _ZN10QRhiVulkan14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch
inline void QRhiVulkan::endComputePass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch *resourceUpdates)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::ComputePass);

    if (cbD->passUsesSecondaryCb) {
        VkCommandBuffer secondaryCb = cbD->activeSecondaryCbStack.last();
        cbD->activeSecondaryCbStack.removeLast();
        endAndEnqueueSecondaryCommandBuffer(secondaryCb, cbD);
    }

    cbD->recordingPass = QVkCommandBuffer::NoPass;

    if (resourceUpdates)
        enqueueResourceUpdates(cbD, resourceUpdates);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6679, as _ZN10QRhiVulkan13nativeHandlesEP17QRhiCommandBuffer
inline const QRhiNativeHandles *QRhiVulkan::nativeHandles(QRhiCommandBuffer *cb)
{
    return QRHI_RES(QVkCommandBuffer, cb)->nativeHandles();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 6757, as _ZN10QRhiVulkan20lastCompletedGpuTimeEP17QRhiCommandBuffer
inline double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer *cb)
{
    QVkCommandBuffer *cbD = QRHI_RES(QVkCommandBuffer, cb);
    return cbD->lastGpuTime;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5462, as _ZNK10QRhiVulkan13ubufAlignmentEv
inline int QRhiVulkan::ubufAlignment() const
{
    return int(ubufAlign); // typically 256 (bytes)
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5467, as _ZNK10QRhiVulkan18isYUpInFramebufferEv
inline bool QRhiVulkan::isYUpInFramebuffer() const
{
    return false;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5472, as _ZNK10QRhiVulkan10isYUpInNDCEv
inline bool QRhiVulkan::isYUpInNDC() const
{
    return false;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5477, as _ZNK10QRhiVulkan20isClipDepthZeroToOneEv
inline bool QRhiVulkan::isClipDepthZeroToOne() const
{
    return true;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5482, as _ZNK10QRhiVulkan19clipSpaceCorrMatrixEv
inline QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const
{
    // See https://matthewwellings.com/blog/the-new-vulkan-coordinate-system/

    static QMatrix4x4 m;
    if (m.isIdentity()) {
        // NB the ctor takes row-major
        m = QMatrix4x4(1.0f, 0.0f, 0.0f, 0.0f,
                       0.0f, -1.0f, 0.0f, 0.0f,
                       0.0f, 0.0f, 0.5f, 0.5f,
                       0.0f, 0.0f, 0.0f, 1.0f);
    }
    return m;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5523, as _ZNK10QRhiVulkan18isFeatureSupportedEN4QRhi7FeatureE
inline bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature) const
{
    switch (feature) {
    case QRhi::MultisampleTexture:
        return true;
    case QRhi::MultisampleRenderBuffer:
        return true;
    case QRhi::DebugMarkers:
        return caps.debugUtils;
    case QRhi::Timestamps:
        return timestampValidBits != 0;
    case QRhi::Instancing:
        return true;
    case QRhi::CustomInstanceStepRate:
        return caps.vertexAttribDivisor;
    case QRhi::PrimitiveRestart:
        return true;
    case QRhi::NonDynamicUniformBuffers:
        return true;
    case QRhi::NonFourAlignedEffectiveIndexBufferOffset:
        return true;
    case QRhi::NPOTTextureRepeat:
        return true;
    case QRhi::RedOrAlpha8IsRed:
        return true;
    case QRhi::ElementIndexUint:
        return true;
    case QRhi::Compute:
        return caps.compute;
    case QRhi::WideLines:
        return caps.wideLines;
    case QRhi::VertexShaderPointSize:
        return true;
    case QRhi::BaseVertex:
        return true;
    case QRhi::BaseInstance:
        return true;
    case QRhi::TriangleFanTopology:
        return true;
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
        return caps.texture3DSliceAs2D;
    case QRhi::TextureArrays:
        return true;
    case QRhi::Tessellation:
        return caps.tessellation;
    case QRhi::GeometryShader:
        return caps.geometryShader;
    case QRhi::TextureArrayRange:
        return true;
    case QRhi::NonFillPolygonMode:
        return caps.nonFillPolygonMode;
    case QRhi::OneDimensionalTextures:
        return true;
    case QRhi::OneDimensionalTextureMipmaps:
        return true;
    case QRhi::HalfAttributes:
        return true;
    case QRhi::RenderToOneDimensionalTexture:
        return true;
    case QRhi::ThreeDimensionalTextureMipmaps:
        return true;
    case QRhi::MultiView:
        return caps.multiView;
    case QRhi::TextureViewFormat:
        return true;
    case QRhi::ResolveDepthStencil:
        return caps.renderPass2KHR && caps.depthStencilResolveKHR;
    case QRhi::VariableRateShading:
        return caps.renderPass2KHR && caps.perDrawShadingRate;
    case QRhi::VariableRateShadingMap:
    case QRhi::VariableRateShadingMapWithTexture:
        return caps.renderPass2KHR && caps.imageBasedShadingRate;
    case QRhi::PerRenderTargetBlending:
    case QRhi::SampleVariables:
        return true;
    case QRhi::InstanceIndexIncludesBaseInstance:
        return true;
    case QRhi::DepthClamp:
        return caps.depthClamp;
    case QRhi::DrawIndirect:
        return true; // available in Vulkan 1.0
    case QRhi::DrawIndirectMulti:
        return caps.drawIndirectMulti;
    case QRhi::ShaderDrawParameters:
        return caps.shaderDrawParameters;
    default:
        Q_UNREACHABLE_RETURN(false);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5635, as _ZNK10QRhiVulkan13resourceLimitEN4QRhi13ResourceLimitE
inline int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit) const
{
    switch (limit) {
    case QRhi::TextureSizeMin:
        return 1;
    case QRhi::TextureSizeMax:
        return int(physDevProperties.limits.maxImageDimension2D);
    case QRhi::MaxColorAttachments:
        return int(physDevProperties.limits.maxColorAttachments);
    case QRhi::FramesInFlight:
        return QVK_FRAMES_IN_FLIGHT;
    case QRhi::MaxAsyncReadbackFrames:
        return QVK_FRAMES_IN_FLIGHT;
    case QRhi::MaxThreadGroupsPerDimension:
        return int(qMin(physDevProperties.limits.maxComputeWorkGroupCount[0],
                   qMin(physDevProperties.limits.maxComputeWorkGroupCount[1],
                        physDevProperties.limits.maxComputeWorkGroupCount[2])));
    case QRhi::MaxThreadsPerThreadGroup:
        return int(physDevProperties.limits.maxComputeWorkGroupInvocations);
    case QRhi::MaxThreadGroupX:
        return int(physDevProperties.limits.maxComputeWorkGroupSize[0]);
    case QRhi::MaxThreadGroupY:
        return int(physDevProperties.limits.maxComputeWorkGroupSize[1]);
    case QRhi::MaxThreadGroupZ:
        return int(physDevProperties.limits.maxComputeWorkGroupSize[2]);
    case QRhi::TextureArraySizeMax:
        return int(physDevProperties.limits.maxImageArrayLayers);
    case QRhi::MaxUniformBufferRange:
        return int(qMin<uint32_t>(INT_MAX, physDevProperties.limits.maxUniformBufferRange));
    case QRhi::MaxVertexInputs:
        return physDevProperties.limits.maxVertexInputAttributes;
    case QRhi::MaxVertexOutputs:
        return physDevProperties.limits.maxVertexOutputComponents / 4;
    case QRhi::ShadingRateImageTileSize:
        return caps.imageBasedShadingRateTileSize;
    default:
        Q_UNREACHABLE_RETURN(0);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5675, as _ZN10QRhiVulkan13nativeHandlesEv
inline const QRhiNativeHandles *QRhiVulkan::nativeHandles()
{
    return &nativeHandlesStruct;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5680, as _ZNK10QRhiVulkan10driverInfoEv
inline QRhiDriverInfo QRhiVulkan::driverInfo() const
{
    return driverInfoStruct;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5705, as _ZN10QRhiVulkan35makeThreadLocalNativeContextCurrentEv
inline bool QRhiVulkan::makeThreadLocalNativeContextCurrent()
{
    // not applicable
    return false;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5711, as _ZN10QRhiVulkan20setQueueSubmitParamsEP17QRhiNativeHandles
inline void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles *params)
{
    QRhiVulkanQueueSubmitParams *sp = static_cast<QRhiVulkanQueueSubmitParams *>(params);
    if (!sp)
        return;

    waitSemaphoresForQueueSubmit.clear();
    if (sp->waitSemaphoreCount)
        waitSemaphoresForQueueSubmit.append(sp->waitSemaphores, sp->waitSemaphoreCount);

    signalSemaphoresForQueueSubmit.clear();
    if (sp->signalSemaphoreCount)
        signalSemaphoresForQueueSubmit.append(sp->signalSemaphores, sp->signalSemaphoreCount);

    waitSemaphoresForPresent.clear();
    if (sp->presentWaitSemaphoreCount)
        waitSemaphoresForPresent.append(sp->presentWaitSemaphores, sp->presentWaitSemaphoreCount);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5730, as _ZN10QRhiVulkan22releaseCachedResourcesEv
inline void QRhiVulkan::releaseCachedResources()
{
    releaseCachedResourcesCalledBeforeFrameStart = true;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5735, as _ZNK10QRhiVulkan12isDeviceLostEv
inline bool QRhiVulkan::isDeviceLost() const
{
    return deviceLost;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 5007, as _ZN10QRhiVulkan30enqueueTransitionPassResourcesEP16QVkCommandBuffer
inline void QRhiVulkan::enqueueTransitionPassResources(QVkCommandBuffer *cbD)
{
    cbD->passResTrackers.emplace_back();
    cbD->currentPassResTrackerIndex = cbD->passResTrackers.size() - 1;

    QVkCommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QVkCommandBuffer::Command::TransitionPassResources;
    cmd.args.transitionResources.trackerIndex = cbD->passResTrackers.size() - 1;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 3998, as _ZN10QRhiVulkan27depthStencilExplicitBarrierEP16QVkCommandBufferP15QVkRenderBuffer
inline void QRhiVulkan::depthStencilExplicitBarrier(QVkCommandBuffer *cbD, QVkRenderBuffer *rbD)
{
    Q_ASSERT(cbD->recordingPass == QVkCommandBuffer::NoPass);

    VkImageMemoryBarrier barrier = {};
    barrier.sType = VK_STRUCTURE_TYPE_IMAGE_MEMORY_BARRIER;
    barrier.subresourceRange.aspectMask = VK_IMAGE_ASPECT_DEPTH_BIT | VK_IMAGE_ASPECT_STENCIL_BIT;
    barrier.subresourceRange.baseMipLevel = 0;
    barrier.subresourceRange.levelCount = VK_REMAINING_MIP_LEVELS;
    barrier.subresourceRange.baseArrayLayer = 0;
    barrier.subresourceRange.layerCount = VK_REMAINING_ARRAY_LAYERS;
    barrier.oldLayout = VK_IMAGE_LAYOUT_UNDEFINED;
    barrier.newLayout = VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL;
    barrier.srcAccessMask = VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT;
    barrier.dstAccessMask = VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_READ_BIT
        | VK_ACCESS_DEPTH_STENCIL_ATTACHMENT_WRITE_BIT;
    barrier.image = rbD->image;

    const VkPipelineStageFlags stages = VK_PIPELINE_STAGE_EARLY_FRAGMENT_TESTS_BIT
        | VK_PIPELINE_STAGE_LATE_FRAGMENT_TESTS_BIT;

    QVkCommandBuffer::Command &cmd(cbD->commands.get());
    cmd.cmd = QVkCommandBuffer::Command::ImageBarrier;
    cmd.args.imageBarrier.srcStageMask = stages;
    cmd.args.imageBarrier.dstStageMask = stages;
    cmd.args.imageBarrier.count = 1;
    cmd.args.imageBarrier.index = cbD->pools.imageBarrier.size();
    cbD->pools.imageBarrier.append(barrier);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 2677, as _ZN10QRhiVulkan27elapsedSecondsFromTimestampEPyPb
inline double QRhiVulkan::elapsedSecondsFromTimestamp(quint64 timestamp[2], bool *ok)
{
    quint64 mask = 0;
    for (quint64 i = 0; i < timestampValidBits; i += 8)
        mask |= 0xFFULL << i;
    const quint64 ts0 = timestamp[0] & mask;
    const quint64 ts1 = timestamp[1] & mask;
    const float nsecsPerTick = physDevProperties.limits.timestampPeriod;
    if (!qFuzzyIsNull(nsecsPerTick)) {
        const float elapsedMs = float(ts1 - ts0) * nsecsPerTick / 1000000.0f;
        const double elapsedSec = elapsedMs / 1000.0;
        *ok = true;
        return elapsedSec;
    }
    *ok = false;
    return 0;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 4192, as _ZNK10QRhiVulkan24printDeviceLossErrorInfoEv
inline void QRhiVulkan::printDeviceLossErrorInfo() const
{
#ifdef VK_EXT_device_fault
    if (!dev || !caps.deviceFault || !vkGetDeviceFaultInfoEXT)
        return;

    VkDeviceFaultCountsEXT faultCounts{};
    faultCounts.sType = VK_STRUCTURE_TYPE_DEVICE_FAULT_COUNTS_EXT;
    faultCounts.pNext = nullptr;

    VkResult result = vkGetDeviceFaultInfoEXT(dev, &faultCounts, nullptr);
    if (result != VK_SUCCESS && result != VK_INCOMPLETE) {
        qWarning("vkGetDeviceFaultInfoEXT failed with %d", result);
        return;
    }
    faultCounts.vendorBinarySize = 0;

    const auto numAddressInfos = faultCounts.addressInfoCount;
    const auto addressInfos
        = q20::make_unique_for_overwrite<VkDeviceFaultAddressInfoEXT[]>(numAddressInfos);

    const auto numVendorInfos = faultCounts.vendorInfoCount;
    const auto vendorInfos
        = q20::make_unique_for_overwrite<VkDeviceFaultVendorInfoEXT[]>(numVendorInfos);

    VkDeviceFaultInfoEXT info{};
    info.sType             = VK_STRUCTURE_TYPE_DEVICE_FAULT_INFO_EXT;
    info.pNext             = nullptr;
    info.pAddressInfos     = numAddressInfos ? addressInfos.get() : nullptr;
    info.pVendorInfos      = numVendorInfos  ? vendorInfos.get()  : nullptr;
    info.pVendorBinaryData = nullptr;

    result = vkGetDeviceFaultInfoEXT(dev, &faultCounts, &info);
    if (result != VK_SUCCESS && result != VK_INCOMPLETE) {
        qWarning("vkGetDeviceFaultInfoEXT failed with %d", result);
        return;
    }

    const char *desc = info.description[0] ? info.description : "n/a";
    qWarning("VK_ERROR_DEVICE_LOST (VK_EXT_device_fault): %u address infos, %u vendor infos, %llu bytes vendor binary: %s",
             faultCounts.addressInfoCount,
             faultCounts.vendorInfoCount,
             (unsigned long long)faultCounts.vendorBinarySize,
             desc);

    for (uint32_t i = 0; i < faultCounts.addressInfoCount; ++i) {
        const auto &a = addressInfos[i];
        auto addressTypeString = [](const VkDeviceFaultAddressTypeEXT type) {
            switch (type) {
            case VK_DEVICE_FAULT_ADDRESS_TYPE_NONE_EXT: return "NONE";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_READ_INVALID_EXT: return "READ_INVALID";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_WRITE_INVALID_EXT: return "WRITE_INVALID";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_EXECUTE_INVALID_EXT: return "EXECUTE_INVALID";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_INSTRUCTION_POINTER_UNKNOWN_EXT: return "INSTRUCTION_POINTER_UNKNOWN";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_INSTRUCTION_POINTER_INVALID_EXT: return "INSTRUCTION_POINTER_INVALID";
            case VK_DEVICE_FAULT_ADDRESS_TYPE_INSTRUCTION_POINTER_FAULT_EXT: return "INSTRUCTION_POINTER_FAULT";
            default: return "UNKNOWN";
            };
        };
        qWarning("  AddressInfo[%02u]: type=%s addr=0x%llx precision=%llu",
                 i,
                 addressTypeString(a.addressType),
                 (unsigned long long)a.reportedAddress,
                 (unsigned long long)a.addressPrecision);
    }

    for (uint32_t i = 0; i < faultCounts.vendorInfoCount; ++i) {
        const auto &v = vendorInfos[i];
        qWarning("  VendorInfo[%02u]: code=%llu data=%llu desc=%s",
                 i,
                 (unsigned long long)v.vendorFaultCode,
                 (unsigned long long)v.vendorFaultData,
                 v.description);
    }
#endif // VK_EXT_device_fault
}
//  -----------------------------------------------------------------------

//  A QRhiVulkan that Python can take functions over in. Every QRhiVulkan
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRhiVulkanCall0)(const void *, int, int *);
typedef void (*CuteQRhiVulkanCall1)(const void *, int *);
typedef void * (*CuteQRhiVulkanCall2)(const void *, int *);
typedef void * (*CuteQRhiVulkanCall3)(const void *, int *);
typedef void * (*CuteQRhiVulkanCall4)(const void *, int *);
typedef void * (*CuteQRhiVulkanCall5)(const void *, int, int, quint32, int *);
typedef void * (*CuteQRhiVulkanCall6)(const void *, int, const QSize *, int, int, int, int *);
typedef void * (*CuteQRhiVulkanCall7)(const void *, int, const QSize *, int, int, int, int, int *);
typedef void * (*CuteQRhiVulkanCall8)(const void *, int, int, int, int, int, int, int *);
typedef void * (*CuteQRhiVulkanCall9)(const void *, const QRhiTextureRenderTargetDescription *, int, int *);
typedef void * (*CuteQRhiVulkanCall10)(const void *, int *);
typedef void * (*CuteQRhiVulkanCall11)(const void *, int *);
typedef int (*CuteQRhiVulkanCall12)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiVulkanCall13)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiVulkanCall14)(const void *, int, int *);
typedef int (*CuteQRhiVulkanCall15)(const void *, int *);
typedef void (*CuteQRhiVulkanCall16)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiVulkanCall17)(const void *, QRhiCommandBuffer *, QRhiRenderTarget *, const QColor *, const QRhiDepthStencilClearValue *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiVulkanCall18)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiVulkanCall19)(const void *, QRhiCommandBuffer *, QRhiGraphicsPipeline *, int *);
typedef void (*CuteQRhiVulkanCall20)(const void *, QRhiCommandBuffer *, const QRhiViewport *, int *);
typedef void (*CuteQRhiVulkanCall21)(const void *, QRhiCommandBuffer *, const QRhiScissor *, int *);
typedef void (*CuteQRhiVulkanCall22)(const void *, QRhiCommandBuffer *, const QColor *, int *);
typedef void (*CuteQRhiVulkanCall23)(const void *, QRhiCommandBuffer *, quint32, int *);
typedef void (*CuteQRhiVulkanCall24)(const void *, QRhiCommandBuffer *, const QSize *, int *);
typedef void (*CuteQRhiVulkanCall25)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiVulkanCall26)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, qint32, quint32, int *);
typedef void (*CuteQRhiVulkanCall27)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiVulkanCall28)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiVulkanCall29)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiVulkanCall30)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiVulkanCall31)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiVulkanCall32)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiVulkanCall33)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiVulkanCall34)(const void *, QRhiCommandBuffer *, QRhiComputePipeline *, int *);
typedef void (*CuteQRhiVulkanCall35)(const void *, QRhiCommandBuffer *, int, int, int, int *);
typedef void * (*CuteQRhiVulkanCall36)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiVulkanCall37)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiVulkanCall38)(const void *, QRhiCommandBuffer *, int *);
typedef double (*CuteQRhiVulkanCall39)(const void *, QRhiCommandBuffer *, int *);
typedef int (*CuteQRhiVulkanCall40)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall41)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall42)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall43)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQRhiVulkanCall44)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall45)(const void *, int, int, int *);
typedef bool (*CuteQRhiVulkanCall46)(const void *, int, int *);
typedef int (*CuteQRhiVulkanCall47)(const void *, int, int *);
typedef void * (*CuteQRhiVulkanCall48)(const void *, int *);
typedef const QRhiDriverInfo * (*CuteQRhiVulkanCall49)(const void *, int *);
typedef const QRhiStats * (*CuteQRhiVulkanCall50)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall51)(const void *, int *);
typedef void (*CuteQRhiVulkanCall52)(const void *, QRhiNativeHandles *, int *);
typedef void (*CuteQRhiVulkanCall53)(const void *, int *);
typedef bool (*CuteQRhiVulkanCall54)(const void *, int *);
typedef const QByteArray * (*CuteQRhiVulkanCall55)(const void *, int *);
typedef void (*CuteQRhiVulkanCall56)(const void *, const QByteArray *, int *);
class CuteQRhiVulkan : public QRhiVulkan {
public:
  using QRhiVulkan::QRhiVulkan;
  CuteQRhiVulkan(const QRhiVulkan &other) : QRhiVulkan(other) {}
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

  //  bool QRhiVulkan::create(QRhi::Flags flags)
  bool create(QRhi::Flags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiVulkanCall0 call = reinterpret_cast<CuteQRhiVulkanCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiVulkan::create(flags);
  }

  //  void QRhiVulkan::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiVulkanCall1 call = reinterpret_cast<CuteQRhiVulkanCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiVulkan::destroy();
  }

  //  QRhiGraphicsPipeline *QRhiVulkan::createGraphicsPipeline()
  QRhiGraphicsPipeline *createGraphicsPipeline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiVulkanCall2 call = reinterpret_cast<CuteQRhiVulkanCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiGraphicsPipeline *>(given);
    }
    return QRhiVulkan::createGraphicsPipeline();
  }

  //  QRhiComputePipeline *QRhiVulkan::createComputePipeline()
  QRhiComputePipeline *createComputePipeline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiVulkanCall3 call = reinterpret_cast<CuteQRhiVulkanCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiComputePipeline *>(given);
    }
    return QRhiVulkan::createComputePipeline();
  }

  //  QRhiShaderResourceBindings
  //      *QRhiVulkan::createShaderResourceBindings()
  QRhiShaderResourceBindings *createShaderResourceBindings() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiVulkanCall4 call = reinterpret_cast<CuteQRhiVulkanCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShaderResourceBindings *>(given);
    }
    return QRhiVulkan::createShaderResourceBindings();
  }

  //  QRhiBuffer *QRhiVulkan::createBuffer(QRhiBuffer::Type type,
  //      QRhiBuffer::UsageFlags usage, quint32 size)
  QRhiBuffer *createBuffer(
      QRhiBuffer::Type type,
      QRhiBuffer::UsageFlags usage,
      quint32 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiVulkanCall5 call = reinterpret_cast<CuteQRhiVulkanCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), static_cast<int>(usage.toInt()), size, &handled);
      if (handled) return static_cast<QRhiBuffer *>(given);
    }
    return QRhiVulkan::createBuffer(type, usage, size);
  }

  //  QRhiRenderBuffer
  //      *QRhiVulkan::createRenderBuffer(QRhiRenderBuffer::Type type,
  //      const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags
  //      flags, QRhiTexture::Format backingFormatHint)
  QRhiRenderBuffer *createRenderBuffer(
      QRhiRenderBuffer::Type type,
      const QSize &pixelSize,
      int sampleCount,
      QRhiRenderBuffer::Flags flags,
      QRhiTexture::Format backingFormatHint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiVulkanCall6 call = reinterpret_cast<CuteQRhiVulkanCall6>(taken[6]);
      void * given = call(this, static_cast<int>(type), &pixelSize, sampleCount, static_cast<int>(flags.toInt()), static_cast<int>(backingFormatHint), &handled);
      if (handled) return static_cast<QRhiRenderBuffer *>(given);
    }
    return QRhiVulkan::createRenderBuffer(type, pixelSize, sampleCount, flags, backingFormatHint);
  }

  //  QRhiTexture *QRhiVulkan::createTexture(QRhiTexture::Format format,
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
      CuteQRhiVulkanCall7 call = reinterpret_cast<CuteQRhiVulkanCall7>(taken[7]);
      void * given = call(this, static_cast<int>(format), &pixelSize, depth, arraySize, sampleCount, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QRhiVulkan::createTexture(format, pixelSize, depth, arraySize, sampleCount, flags);
  }

  //  QRhiSampler *QRhiVulkan::createSampler(QRhiSampler::Filter magFilter,
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
      CuteQRhiVulkanCall8 call = reinterpret_cast<CuteQRhiVulkanCall8>(taken[8]);
      void * given = call(this, static_cast<int>(magFilter), static_cast<int>(minFilter), static_cast<int>(mipmapMode), static_cast<int>(u), static_cast<int>(v), static_cast<int>(w), &handled);
      if (handled) return static_cast<QRhiSampler *>(given);
    }
    return QRhiVulkan::createSampler(magFilter, minFilter, mipmapMode, u, v, w);
  }

  //  QRhiTextureRenderTarget *QRhiVulkan::createTextureRenderTarget(const
  //      QRhiTextureRenderTargetDescription &desc,
  //      QRhiTextureRenderTarget::Flags flags)
  QRhiTextureRenderTarget *createTextureRenderTarget(
      const QRhiTextureRenderTargetDescription &desc,
      QRhiTextureRenderTarget::Flags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiVulkanCall9 call = reinterpret_cast<CuteQRhiVulkanCall9>(taken[9]);
      void * given = call(this, &desc, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTextureRenderTarget *>(given);
    }
    return QRhiVulkan::createTextureRenderTarget(desc, flags);
  }

  //  QRhiShadingRateMap *QRhiVulkan::createShadingRateMap()
  QRhiShadingRateMap *createShadingRateMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiVulkanCall10 call = reinterpret_cast<CuteQRhiVulkanCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShadingRateMap *>(given);
    }
    return QRhiVulkan::createShadingRateMap();
  }

  //  QRhiSwapChain *QRhiVulkan::createSwapChain()
  QRhiSwapChain *createSwapChain() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiVulkanCall11 call = reinterpret_cast<CuteQRhiVulkanCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiSwapChain *>(given);
    }
    return QRhiVulkan::createSwapChain();
  }

  //  QRhi::FrameOpResult QRhiVulkan::beginFrame(QRhiSwapChain *swapChain,
  //      QRhi::BeginFrameFlags flags)
  QRhi::FrameOpResult beginFrame(
      QRhiSwapChain *swapChain,
      QRhi::BeginFrameFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiVulkanCall12 call = reinterpret_cast<CuteQRhiVulkanCall12>(taken[12]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiVulkan::beginFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiVulkan::endFrame(QRhiSwapChain *swapChain,
  //      QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endFrame(
      QRhiSwapChain *swapChain,
      QRhi::EndFrameFlags flags) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiVulkanCall13 call = reinterpret_cast<CuteQRhiVulkanCall13>(taken[13]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiVulkan::endFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiVulkan::endOffscreenFrame(QRhi::EndFrameFlags
  //      flags)
  QRhi::FrameOpResult endOffscreenFrame(QRhi::EndFrameFlags flags) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiVulkanCall14 call = reinterpret_cast<CuteQRhiVulkanCall14>(taken[14]);
      int given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiVulkan::endOffscreenFrame(flags);
  }

  //  QRhi::FrameOpResult QRhiVulkan::finish()
  QRhi::FrameOpResult finish() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiVulkanCall15 call = reinterpret_cast<CuteQRhiVulkanCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiVulkan::finish();
  }

  //  void QRhiVulkan::resourceUpdate(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void resourceUpdate(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiVulkanCall16 call = reinterpret_cast<CuteQRhiVulkanCall16>(taken[16]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiVulkan::resourceUpdate(cb, resourceUpdates);
  }

  //  void QRhiVulkan::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget
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
      CuteQRhiVulkanCall17 call = reinterpret_cast<CuteQRhiVulkanCall17>(taken[17]);
      call(this, cb, rt, &colorClearValue, &depthStencilClearValue, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiVulkan::beginPass(cb, rt, colorClearValue, depthStencilClearValue, resourceUpdates, flags);
  }

  //  void QRhiVulkan::endPass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endPass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiVulkanCall18 call = reinterpret_cast<CuteQRhiVulkanCall18>(taken[18]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiVulkan::endPass(cb, resourceUpdates);
  }

  //  void QRhiVulkan::setGraphicsPipeline(QRhiCommandBuffer *cb,
  //      QRhiGraphicsPipeline *ps)
  void setGraphicsPipeline(
      QRhiCommandBuffer *cb,
      QRhiGraphicsPipeline *ps) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiVulkanCall19 call = reinterpret_cast<CuteQRhiVulkanCall19>(taken[19]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiVulkan::setGraphicsPipeline(cb, ps);
  }

  //  void QRhiVulkan::setViewport(QRhiCommandBuffer *cb, const
  //      QRhiViewport &viewport)
  void setViewport(
      QRhiCommandBuffer *cb,
      const QRhiViewport &viewport) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiVulkanCall20 call = reinterpret_cast<CuteQRhiVulkanCall20>(taken[20]);
      call(this, cb, &viewport, &handled);
      if (handled) return;
    }
    QRhiVulkan::setViewport(cb, viewport);
  }

  //  void QRhiVulkan::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
  //      &scissor)
  void setScissor(
      QRhiCommandBuffer *cb,
      const QRhiScissor &scissor) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiVulkanCall21 call = reinterpret_cast<CuteQRhiVulkanCall21>(taken[21]);
      call(this, cb, &scissor, &handled);
      if (handled) return;
    }
    QRhiVulkan::setScissor(cb, scissor);
  }

  //  void QRhiVulkan::setBlendConstants(QRhiCommandBuffer *cb, const
  //      QColor &c)
  void setBlendConstants(QRhiCommandBuffer *cb, const QColor &c) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiVulkanCall22 call = reinterpret_cast<CuteQRhiVulkanCall22>(taken[22]);
      call(this, cb, &c, &handled);
      if (handled) return;
    }
    QRhiVulkan::setBlendConstants(cb, c);
  }

  //  void QRhiVulkan::setStencilRef(QRhiCommandBuffer *cb, quint32
  //      refValue)
  void setStencilRef(QRhiCommandBuffer *cb, quint32 refValue) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiVulkanCall23 call = reinterpret_cast<CuteQRhiVulkanCall23>(taken[23]);
      call(this, cb, refValue, &handled);
      if (handled) return;
    }
    QRhiVulkan::setStencilRef(cb, refValue);
  }

  //  void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const QSize
  //      &coarsePixelSize)
  void setShadingRate(
      QRhiCommandBuffer *cb,
      const QSize &coarsePixelSize) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiVulkanCall24 call = reinterpret_cast<CuteQRhiVulkanCall24>(taken[24]);
      call(this, cb, &coarsePixelSize, &handled);
      if (handled) return;
    }
    QRhiVulkan::setShadingRate(cb, coarsePixelSize);
  }

  //  void QRhiVulkan::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
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
      CuteQRhiVulkanCall25 call = reinterpret_cast<CuteQRhiVulkanCall25>(taken[25]);
      call(this, cb, vertexCount, instanceCount, firstVertex, firstInstance, &handled);
      if (handled) return;
    }
    QRhiVulkan::draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
  }

  //  void QRhiVulkan::drawIndexed(QRhiCommandBuffer *cb, quint32
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
      CuteQRhiVulkanCall26 call = reinterpret_cast<CuteQRhiVulkanCall26>(taken[26]);
      call(this, cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance, &handled);
      if (handled) return;
    }
    QRhiVulkan::drawIndexed(cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance);
  }

  //  void QRhiVulkan::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
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
      CuteQRhiVulkanCall27 call = reinterpret_cast<CuteQRhiVulkanCall27>(taken[27]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiVulkan::drawIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiVulkan::drawIndexedIndirect(QRhiCommandBuffer *cb,
  //      QRhiBuffer *indirectBuffer, quint32 indirectBufferOffset, quint32
  //      drawCount, quint32 stride)
  void drawIndexedIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 indirectBufferOffset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRhiVulkanCall28 call = reinterpret_cast<CuteQRhiVulkanCall28>(taken[28]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiVulkan::drawIndexedIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const
  //      QByteArray &name)
  void debugMarkBegin(
      QRhiCommandBuffer *cb,
      const QByteArray &name) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiVulkanCall29 call = reinterpret_cast<CuteQRhiVulkanCall29>(taken[29]);
      call(this, cb, &name, &handled);
      if (handled) return;
    }
    QRhiVulkan::debugMarkBegin(cb, name);
  }

  //  void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)
  void debugMarkEnd(QRhiCommandBuffer *cb) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiVulkanCall30 call = reinterpret_cast<CuteQRhiVulkanCall30>(taken[30]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiVulkan::debugMarkEnd(cb);
  }

  //  void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
  //      &msg)
  void debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiVulkanCall31 call = reinterpret_cast<CuteQRhiVulkanCall31>(taken[31]);
      call(this, cb, &msg, &handled);
      if (handled) return;
    }
    QRhiVulkan::debugMarkMsg(cb, msg);
  }

  //  void QRhiVulkan::beginComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiVulkanCall32 call = reinterpret_cast<CuteQRhiVulkanCall32>(taken[32]);
      call(this, cb, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiVulkan::beginComputePass(cb, resourceUpdates, flags);
  }

  //  void QRhiVulkan::endComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiVulkanCall33 call = reinterpret_cast<CuteQRhiVulkanCall33>(taken[33]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiVulkan::endComputePass(cb, resourceUpdates);
  }

  //  void QRhiVulkan::setComputePipeline(QRhiCommandBuffer *cb,
  //      QRhiComputePipeline *ps)
  void setComputePipeline(
      QRhiCommandBuffer *cb,
      QRhiComputePipeline *ps) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiVulkanCall34 call = reinterpret_cast<CuteQRhiVulkanCall34>(taken[34]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiVulkan::setComputePipeline(cb, ps);
  }

  //  void QRhiVulkan::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
  void dispatch(QRhiCommandBuffer *cb, int x, int y, int z) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiVulkanCall35 call = reinterpret_cast<CuteQRhiVulkanCall35>(taken[35]);
      call(this, cb, x, y, z, &handled);
      if (handled) return;
    }
    QRhiVulkan::dispatch(cb, x, y, z);
  }

  //  const QRhiNativeHandles *QRhiVulkan::nativeHandles(QRhiCommandBuffer
  //      *cb)
  const QRhiNativeHandles *nativeHandles(QRhiCommandBuffer *cb) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiVulkanCall36 call = reinterpret_cast<CuteQRhiVulkanCall36>(taken[36]);
      void * given = call(this, cb, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiVulkan::nativeHandles(cb);
  }

  //  void QRhiVulkan::beginExternal(QRhiCommandBuffer *cb)
  void beginExternal(QRhiCommandBuffer *cb) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiVulkanCall37 call = reinterpret_cast<CuteQRhiVulkanCall37>(taken[37]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiVulkan::beginExternal(cb);
  }

  //  void QRhiVulkan::endExternal(QRhiCommandBuffer *cb)
  void endExternal(QRhiCommandBuffer *cb) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiVulkanCall38 call = reinterpret_cast<CuteQRhiVulkanCall38>(taken[38]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiVulkan::endExternal(cb);
  }

  //  double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer *cb)
  double lastCompletedGpuTime(QRhiCommandBuffer *cb) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiVulkanCall39 call = reinterpret_cast<CuteQRhiVulkanCall39>(taken[39]);
      double given = call(this, cb, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::lastCompletedGpuTime(cb);
  }

  //  int QRhiVulkan::ubufAlignment() const
  int ubufAlignment() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiVulkanCall40 call = reinterpret_cast<CuteQRhiVulkanCall40>(taken[40]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::ubufAlignment();
  }

  //  bool QRhiVulkan::isYUpInFramebuffer() const
  bool isYUpInFramebuffer() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiVulkanCall41 call = reinterpret_cast<CuteQRhiVulkanCall41>(taken[41]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isYUpInFramebuffer();
  }

  //  bool QRhiVulkan::isYUpInNDC() const
  bool isYUpInNDC() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiVulkanCall42 call = reinterpret_cast<CuteQRhiVulkanCall42>(taken[42]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isYUpInNDC();
  }

  //  bool QRhiVulkan::isClipDepthZeroToOne() const
  bool isClipDepthZeroToOne() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRhiVulkanCall43 call = reinterpret_cast<CuteQRhiVulkanCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isClipDepthZeroToOne();
  }

  //  QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const
  QMatrix4x4 clipSpaceCorrMatrix() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQRhiVulkanCall44 call = reinterpret_cast<CuteQRhiVulkanCall44>(taken[44]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiVulkan::clipSpaceCorrMatrix();
  }

  //  bool QRhiVulkan::isTextureFormatSupported(QRhiTexture::Format format,
  //      QRhiTexture::Flags flags) const
  bool isTextureFormatSupported(
      QRhiTexture::Format format,
      QRhiTexture::Flags flags) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQRhiVulkanCall45 call = reinterpret_cast<CuteQRhiVulkanCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isTextureFormatSupported(format, flags);
  }

  //  bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature) const
  bool isFeatureSupported(QRhi::Feature feature) const override {
    if (taken[46]) {
      int handled = 0;
      CuteQRhiVulkanCall46 call = reinterpret_cast<CuteQRhiVulkanCall46>(taken[46]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isFeatureSupported(feature);
  }

  //  int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit) const
  int resourceLimit(QRhi::ResourceLimit limit) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQRhiVulkanCall47 call = reinterpret_cast<CuteQRhiVulkanCall47>(taken[47]);
      int given = call(this, static_cast<int>(limit), &handled);
      if (handled) return given;
    }
    return QRhiVulkan::resourceLimit(limit);
  }

  //  const QRhiNativeHandles *QRhiVulkan::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[48]) {
      int handled = 0;
      CuteQRhiVulkanCall48 call = reinterpret_cast<CuteQRhiVulkanCall48>(taken[48]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiVulkan::nativeHandles();
  }

  //  QRhiDriverInfo QRhiVulkan::driverInfo() const
  QRhiDriverInfo driverInfo() const override {
    if (taken[49]) {
      int handled = 0;
      CuteQRhiVulkanCall49 call = reinterpret_cast<CuteQRhiVulkanCall49>(taken[49]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiVulkan::driverInfo();
  }

  //  QRhiStats QRhiVulkan::statistics()
  QRhiStats statistics() override {
    if (taken[50]) {
      int handled = 0;
      CuteQRhiVulkanCall50 call = reinterpret_cast<CuteQRhiVulkanCall50>(taken[50]);
      const QRhiStats * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiVulkan::statistics();
  }

  //  bool QRhiVulkan::makeThreadLocalNativeContextCurrent()
  bool makeThreadLocalNativeContextCurrent() override {
    if (taken[51]) {
      int handled = 0;
      CuteQRhiVulkanCall51 call = reinterpret_cast<CuteQRhiVulkanCall51>(taken[51]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::makeThreadLocalNativeContextCurrent();
  }

  //  void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles *params)
  void setQueueSubmitParams(QRhiNativeHandles *params) override {
    if (taken[52]) {
      int handled = 0;
      CuteQRhiVulkanCall52 call = reinterpret_cast<CuteQRhiVulkanCall52>(taken[52]);
      call(this, params, &handled);
      if (handled) return;
    }
    QRhiVulkan::setQueueSubmitParams(params);
  }

  //  void QRhiVulkan::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[53]) {
      int handled = 0;
      CuteQRhiVulkanCall53 call = reinterpret_cast<CuteQRhiVulkanCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiVulkan::releaseCachedResources();
  }

  //  bool QRhiVulkan::isDeviceLost() const
  bool isDeviceLost() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQRhiVulkanCall54 call = reinterpret_cast<CuteQRhiVulkanCall54>(taken[54]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiVulkan::isDeviceLost();
  }

  //  QByteArray QRhiVulkan::pipelineCacheData()
  QByteArray pipelineCacheData() override {
    if (taken[55]) {
      int handled = 0;
      CuteQRhiVulkanCall55 call = reinterpret_cast<CuteQRhiVulkanCall55>(taken[55]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiVulkan::pipelineCacheData();
  }

  //  void QRhiVulkan::setPipelineCacheData(const QByteArray &data)
  void setPipelineCacheData(const QByteArray &data) override {
    if (taken[56]) {
      int handled = 0;
      CuteQRhiVulkanCall56 call = reinterpret_cast<CuteQRhiVulkanCall56>(taken[56]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QRhiVulkan::setPipelineCacheData(data);
  }
};

//  QRhiGraphicsPipeline *QRhiVulkan::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN10QRhiVulkan22createGraphicsPipelineEv(
    QRhiVulkan *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiVulkan::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN10QRhiVulkan21createComputePipelineEv(
    QRhiVulkan *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings *QRhiVulkan::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN10QRhiVulkan28createShaderResourceBindingsEv(
    QRhiVulkan *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiVulkan::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN10QRhiVulkan12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiVulkan *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer *QRhiVulkan::createRenderBuffer(QRhiRenderBuffer::Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN10QRhiVulkan18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiVulkan *self,
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

//  QRhiTexture *QRhiVulkan::createTexture(QRhiTexture::Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN10QRhiVulkan13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiVulkan *self,
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

//  QRhiSampler *QRhiVulkan::createSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN10QRhiVulkan13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiVulkan *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget *QRhiVulkan::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN10QRhiVulkan25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiVulkan *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiVulkan::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN10QRhiVulkan20createShadingRateMapEv(
    QRhiVulkan *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiVulkan::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN10QRhiVulkan15createSwapChainEv(QRhiVulkan *self) {
  return self->createSwapChain();
}

//  void QRhiVulkan::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiVulkan::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiVulkan *self,
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

//  void QRhiVulkan::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan12debugMarkEndEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiVulkan::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiVulkan::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  const QRhiNativeHandles *QRhiVulkan::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN10QRhiVulkan13nativeHandlesEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN10QRhiVulkan20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  int QRhiVulkan::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRhiVulkan13ubufAlignmentEv(const QRhiVulkan *self) {
  return self->ubufAlignment();
}

//  bool QRhiVulkan::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiVulkan18isYUpInFramebufferEv(const QRhiVulkan *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiVulkan::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiVulkan10isYUpInNDCEv(const QRhiVulkan *self) {
  return self->isYUpInNDC();
}

//  bool QRhiVulkan::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiVulkan20isClipDepthZeroToOneEv(const QRhiVulkan *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10QRhiVulkan19clipSpaceCorrMatrixEv(
    const QRhiVulkan *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiVulkan18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiVulkan *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRhiVulkan13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiVulkan *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiVulkan::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN10QRhiVulkan13nativeHandlesEv(
    QRhiVulkan *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiVulkan::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK10QRhiVulkan10driverInfoEv(
    const QRhiVulkan *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  bool QRhiVulkan::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QRhiVulkan35makeThreadLocalNativeContextCurrentEv(
    QRhiVulkan *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiVulkan *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiVulkan::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan22releaseCachedResourcesEv(QRhiVulkan *self) {
  self->releaseCachedResources();
}

//  bool QRhiVulkan::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiVulkan12isDeviceLostEv(const QRhiVulkan *self) {
  return self->isDeviceLost();
}

//  void QRhiVulkan::enqueueTransitionPassResources(QVkCommandBuffer *cbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan30enqueueTransitionPassResourcesEP16QVkCommandBuffer(
    QRhiVulkan *self,
    QVkCommandBuffer *cbD) {
  self->enqueueTransitionPassResources(cbD);
}

//  void QRhiVulkan::depthStencilExplicitBarrier(QVkCommandBuffer *cbD,
//      QVkRenderBuffer *rbD)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkan27depthStencilExplicitBarrierEP16QVkCommandBufferP15QVkRenderBuffer(
    QRhiVulkan *self,
    QVkCommandBuffer *cbD,
    QVkRenderBuffer *rbD) {
  self->depthStencilExplicitBarrier(cbD, rbD);
}

//  double QRhiVulkan::elapsedSecondsFromTimestamp(quint64 *timestamp, bool
//      *ok)
extern "C" Q_DECL_EXPORT
double ritual_ZN10QRhiVulkan27elapsedSecondsFromTimestampEPyPb(
    QRhiVulkan *self,
    quint64 *timestamp,
    bool *ok) {
  return self->elapsedSecondsFromTimestamp(timestamp, ok);
}

//  void QRhiVulkan::printDeviceLossErrorInfo() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QRhiVulkan24printDeviceLossErrorInfoEv(
    const QRhiVulkan *self) {
  self->printDeviceLossErrorInfo();
}

//  QRhiVulkan::~QRhiVulkan()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiVulkanD1Ev(QRhiVulkan *self) {
  delete self;
}

//  a Python function taken by a CuteQRhiVulkan, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiVulkan(QRhiVulkan *self, const char *key, void *call) {
  return static_cast<CuteQRhiVulkan *>(self)->take(key, call);
}

//  void QRhiVulkan::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->QRhiVulkan::setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiVulkan::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->QRhiVulkan::debugMarkBegin(cb, *name);
}

//  void QRhiVulkan::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan12debugMarkEndEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  self->QRhiVulkan::debugMarkEnd(cb);
}

//  void QRhiVulkan::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->QRhiVulkan::debugMarkMsg(cb, *msg);
}

//  const QRhiNativeHandles *QRhiVulkan::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN10QRhiVulkan13nativeHandlesEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiVulkan::nativeHandles(cb);
}

//  double QRhiVulkan::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_own_ZN10QRhiVulkan20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiVulkan *self,
    QRhiCommandBuffer *cb) {
  return self->QRhiVulkan::lastCompletedGpuTime(cb);
}

//  int QRhiVulkan::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QRhiVulkan13ubufAlignmentEv(const QRhiVulkan *self) {
  return self->QRhiVulkan::ubufAlignment();
}

//  bool QRhiVulkan::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QRhiVulkan18isYUpInFramebufferEv(
    const QRhiVulkan *self) {
  return self->QRhiVulkan::isYUpInFramebuffer();
}

//  bool QRhiVulkan::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QRhiVulkan10isYUpInNDCEv(const QRhiVulkan *self) {
  return self->QRhiVulkan::isYUpInNDC();
}

//  bool QRhiVulkan::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QRhiVulkan20isClipDepthZeroToOneEv(
    const QRhiVulkan *self) {
  return self->QRhiVulkan::isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiVulkan::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_own_ZNK10QRhiVulkan19clipSpaceCorrMatrixEv(
    const QRhiVulkan *self) {
  return new QMatrix4x4(self->QRhiVulkan::clipSpaceCorrMatrix());
}

//  bool QRhiVulkan::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QRhiVulkan18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiVulkan *self,
    QRhi::Feature feature) {
  return self->QRhiVulkan::isFeatureSupported(feature);
}

//  int QRhiVulkan::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QRhiVulkan13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiVulkan *self,
    QRhi::ResourceLimit limit) {
  return self->QRhiVulkan::resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiVulkan::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN10QRhiVulkan13nativeHandlesEv(
    QRhiVulkan *self) {
  return self->QRhiVulkan::nativeHandles();
}

//  QRhiDriverInfo QRhiVulkan::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_own_ZNK10QRhiVulkan10driverInfoEv(
    const QRhiVulkan *self) {
  return new QRhiDriverInfo(self->QRhiVulkan::driverInfo());
}

//  bool QRhiVulkan::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QRhiVulkan35makeThreadLocalNativeContextCurrentEv(
    QRhiVulkan *self) {
  return self->QRhiVulkan::makeThreadLocalNativeContextCurrent();
}

//  void QRhiVulkan::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiVulkan *self,
    QRhiNativeHandles *params) {
  self->QRhiVulkan::setQueueSubmitParams(params);
}

//  void QRhiVulkan::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QRhiVulkan22releaseCachedResourcesEv(QRhiVulkan *self) {
  self->QRhiVulkan::releaseCachedResources();
}

//  bool QRhiVulkan::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QRhiVulkan12isDeviceLostEv(const QRhiVulkan *self) {
  return self->QRhiVulkan::isDeviceLost();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
