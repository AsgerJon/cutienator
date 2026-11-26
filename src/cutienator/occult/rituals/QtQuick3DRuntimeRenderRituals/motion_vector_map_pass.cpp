//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderhelpers_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qbitarray.h>
#include <cmath>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskeleton_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderjoint_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermorphtarget_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgruntimerenderlogging_p.h>
#include <QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtCore/qspan.h>
#include <array>
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderhelpers_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 563, as local:qssgrenderhelpers.cpp:setupInstancing
static int setupInstancing(QSSGSubsetRenderable *renderable, QSSGRhiGraphicsPipelineState *ps, QSSGRhiContext *rhiCtx, const QVector3D &cameraDirection, const QVector3D &cameraPosition)
{
    // TODO: non-static so it can be used from QSSGCustomMaterialSystem::rhiPrepareRenderable()?
    const bool instancing = QSSGLayerRenderData::prepareInstancing(rhiCtx, renderable, cameraDirection, cameraPosition, renderable->instancingLodMin, renderable->instancingLodMax);
    int instanceBufferBinding = 0;
    if (instancing) {
        auto &ia = QSSGRhiInputAssemblerStatePrivate::get(*ps);
        // set up new bindings for instanced buffers
        const quint32 stride = renderable->modelContext.model.instanceTable->stride();
        QVarLengthArray<QRhiVertexInputBinding, 8> bindings;
        std::copy(ia.inputLayout.cbeginBindings(), ia.inputLayout.cendBindings(), std::back_inserter(bindings));
        bindings.append({ stride, QRhiVertexInputBinding::PerInstance });
        instanceBufferBinding = bindings.size() - 1;
        ia.inputLayout.setBindings(bindings.cbegin(), bindings.cend());
    }
    return instanceBufferBinding;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 3893, as _ZN13RenderHelpers29rhiPrepareMotionVectorTextureEP14QSSGRhiContextRK5QSizeP24QSSGRhiRenderableTexture
inline bool RenderHelpers::rhiPrepareMotionVectorTexture(QSSGRhiContext *rhiCtx,
                                   const QSize &size,
                                   QSSGRhiRenderableTexture *renderableTex){
    QRhi *rhi = rhiCtx->rhi();
    bool needsBuild = false;
    QRhiTexture::Flags flags = QRhiTexture::RenderTarget;
    if (!renderableTex->texture) {
        renderableTex->texture = rhi->newTexture(QRhiTexture::RGBA16F, size, 1, flags);
        needsBuild = true;
    } else if (renderableTex->texture->pixelSize() != size) {
        renderableTex->texture->setPixelSize(size);
        needsBuild = true;
    }

    if (!renderableTex->depthStencil && !renderableTex->depthTexture) {
        renderableTex->depthStencil = rhi->newRenderBuffer(QRhiRenderBuffer::DepthStencil, size);
        needsBuild = true;
    } else {
        if (renderableTex->depthStencil && renderableTex->depthStencil->pixelSize() != size) {
            renderableTex->depthStencil->setPixelSize(size);
            needsBuild = true;
        }
    }

    if (needsBuild) {
        if (!renderableTex->texture->create()) {
            qWarning("Failed to build motionvector texture (size %dx%d)", size.width(), size.height());
            renderableTex->reset();
            return false;
        }
        if (renderableTex->depthStencil && !renderableTex->depthStencil->create()) {
            qWarning("Failed to build depth-stencil buffer for motionvector texture (size %dx%d)",
                     size.width(), size.height());
            renderableTex->reset();
            return false;
        }
        renderableTex->resetRenderTarget();
        QRhiTextureRenderTargetDescription desc;
        QRhiColorAttachment colorAttachment(renderableTex->texture);
        desc.setColorAttachments({ colorAttachment });
        if (renderableTex->depthStencil)
            desc.setDepthStencilBuffer(renderableTex->depthStencil);
        renderableTex->rt = rhi->newTextureRenderTarget(desc);
        renderableTex->rt->setName(QByteArrayLiteral("Motionvector texture"));
        renderableTex->rpDesc = renderableTex->rt->newCompatibleRenderPassDescriptor();
        renderableTex->rt->setRenderPassDescriptor(renderableTex->rpDesc);
        if (!renderableTex->rt->create()) {
            qWarning("Failed to build render target for motionvector texture");
            renderableTex->reset();
            return false;
        }
    }

    return true;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 3949, as _ZN13RenderHelpers32rhiPrepareMotionVectorRenderableEP14QSSGRhiContextPvRK19QSSGLayerRenderDataRK10QMatrix4x4R20QSSGRenderableObjectP24QRhiRenderPassDescriptorP28QSSGRhiGraphicsPipelineStateR25QSSGRenderMotionVectorMap
inline void RenderHelpers::rhiPrepareMotionVectorRenderable(QSSGRhiContext *rhiCtx,
                                                     QSSGPassKey passKey,
                                                     const QSSGLayerRenderData &inData,
                                                     const QMatrix4x4 &viewProjection,
                                                     QSSGRenderableObject &inObject,
                                                     QRhiRenderPassDescriptor *renderPassDescriptor,
                                                     QSSGRhiGraphicsPipelineState *ps,
                                                     QSSGRenderMotionVectorMap &motionVectorMapManager)
{
    if (inObject.type != QSSGRenderableObject::Type::DefaultMaterialMeshSubset &&
        inObject.type != QSSGRenderableObject::Type::CustomMaterialMeshSubset)
        return;

    QSSGSubsetRenderable &subsetRenderable = static_cast<QSSGSubsetRenderable &>(inObject);
    auto &modelNode = subsetRenderable.modelContext.model;

    bool skin = modelNode.usesBoneTexture();
    bool instance = modelNode.instanceCount() > 0;
    bool morph = modelNode.morphTargets.size() > 0;

    QSSGRhiShaderPipelinePtr shaderPipeline = inData.contextInterface()->shaderCache()->
                                              getBuiltInRhiShaders().getRhiMotionVectorShader(skin, instance, morph);

    if (!shaderPipeline)
        return;

    QSSGRhiShaderResourceBindingList bindings;

    QSSGRhiContextPrivate *rhiCtxD = QSSGRhiContextPrivate::get(rhiCtx);
    QSSGRhiDrawCallData &dcd = rhiCtxD->drawCallData({ passKey, &modelNode, nullptr, 0 });


    QSSGRenderTextureData *boneTextureData = nullptr;
    if (modelNode.skin)
        boneTextureData = modelNode.skin;
    else if (modelNode.skeleton)
        boneTextureData = &modelNode.skeleton->boneTexData;

    QMatrix4x4 modelViewProjection = subsetRenderable.modelContext.modelViewProjections[0];
    QMatrix4x4 instanceLocal;
    QMatrix4x4 instanceGlobal;

    if (instance) {
        instanceLocal = inData.getInstanceTransforms(modelNode).local;
        instanceGlobal = inData.getInstanceTransforms(modelNode).global;
        if (!skin)
            modelViewProjection = viewProjection;
    }
    auto motionData = motionVectorMapManager.trackMotionData(&modelNode,
                                                             modelViewProjection,
                                                             instanceLocal,
                                                             instanceGlobal,
                                                             boneTextureData,
                                                             modelNode.instanceTable,
                                                             modelNode.morphWeights);
    float velocityAmount = subsetRenderable.modelContext.model.motionVectorScale;
    int morphTargetCount = modelNode.morphWeights.count();

    // mat4 mvp;                    // 64
    // mat4 prevMVP;                // 64
    // mat4 instanceLocal;          // 64
    // mat4 instanceGlobal;         // 64
    // mat4 prevInstanceLocal;      // 64
    // mat4 prevInstanceGlobal;     // 64
    // vec4 currentAndLastJitter;   // 16
    // float velocityAmount;        // 4
    // int morphTargetCount;        // 4
    // vec2 padding;                // 8
    const int ubufSize = 416;

    if (!dcd.ubuf) {
        dcd.ubuf = rhiCtx->rhi()->newBuffer(QRhiBuffer::Dynamic,
                                            QRhiBuffer::UniformBuffer,
                                            ubufSize);
        dcd.ubuf->create();
    }

    char *ubufData = dcd.ubuf->beginFullDynamicBufferUpdateForCurrentFrame();
    int ubufOffset = 0;
    memcpy(ubufData, modelViewProjection.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, motionData.prevModelViewProjection.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, instanceLocal.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, instanceGlobal.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, motionData.prevInstanceLocal.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, motionData.prevInstanceGlobal.constData(), 64);
    ubufOffset += 64;
    memcpy(ubufData + ubufOffset, &inData.layer.currentAndLastJitter, 16);
    ubufOffset += 16;
    memcpy(ubufData + ubufOffset, &velocityAmount, 4);
    ubufOffset += 4;
    memcpy(ubufData + ubufOffset, &morphTargetCount, 4);
    dcd.ubuf->endFullDynamicBufferUpdateForCurrentFrame();

    bindings.addUniformBuffer(0, QRhiShaderResourceBinding::VertexStage |
                                      QRhiShaderResourceBinding::FragmentStage, dcd.ubuf);

    QRhiSampler *nearestSampler = nullptr;

    if (skin || instance) {
        nearestSampler = rhiCtx->sampler({ QRhiSampler::Nearest,
                QRhiSampler::Nearest,
                QRhiSampler::None,
                QRhiSampler::ClampToEdge,
                QRhiSampler::ClampToEdge,
                QRhiSampler::Repeat
        });
    }

    if (skin) {
        int binding = shaderPipeline->bindingForTexture("qt_boneTexture");
        if (binding >= 0) {

            bindings.addTexture(binding,
                                QRhiShaderResourceBinding::VertexStage,
                                inData.getBonemapTexture(subsetRenderable.modelContext),
                                nearestSampler);
            binding = shaderPipeline->bindingForTexture("lastBoneTexture");
            if (binding >= 0) {
                bindings.addTexture(binding,
                                    QRhiShaderResourceBinding::VertexStage,
                                    motionData.prevBoneTexture.m_texture,
                                    nearestSampler);
            }
        }
    }

    if (instance) {
        int binding = shaderPipeline->bindingForTexture("lastInstanceTexture");
        if (binding >= 0) {
            bindings.addTexture(binding,
                                QRhiShaderResourceBinding::VertexStage,
                                motionData.prevInstanceTexture.m_texture,
                                nearestSampler);
        }
    }

    auto *targetsTexture = subsetRenderable.subset.rhi.targetsTexture;
    if (targetsTexture) {
        int binding = shaderPipeline->bindingForTexture("qt_morphTargetTexture");
        if (binding >= 0) {
            QRhiSampler *targetsSampler = rhiCtx->sampler({ QRhiSampler::Nearest,
                    QRhiSampler::Nearest,
                    QRhiSampler::None,
                    QRhiSampler::ClampToEdge,
                    QRhiSampler::ClampToEdge,
                    QRhiSampler::ClampToEdge
            });
            bindings.addTexture(binding, QRhiShaderResourceBinding::VertexStage, subsetRenderable.subset.rhi.targetsTexture, targetsSampler);

            if ((binding = shaderPipeline->bindingForTexture("morphWeightTexture")) >= 0)
                bindings.addTexture(binding, QRhiShaderResourceBinding::VertexStage, motionData.currentMorphWeightTexture.m_texture, targetsSampler);

            if ((binding = shaderPipeline->bindingForTexture("lastMorphWeightTexture")) >= 0)
                bindings.addTexture(binding, QRhiShaderResourceBinding::VertexStage, motionData.prevMorphWeightTexture.m_texture, targetsSampler);
        }
    }

    auto &ia = QSSGRhiInputAssemblerStatePrivate::get(*ps);
    ia = subsetRenderable.subset.rhi.ia;
    const QSSGRenderCameraDataList &cameraDatas(*inData.renderedCameraData);
    QVector3D cameraDirection = cameraDatas[0].direction;
    QVector3D cameraPosition = cameraDatas[0].position;
    int instanceBufferBinding = setupInstancing(&subsetRenderable, ps, rhiCtx, cameraDirection, cameraPosition);
    QSSGRhiHelpers::bakeVertexInputLocations(&ia, *shaderPipeline, instanceBufferBinding);
    QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(*ps, shaderPipeline.get());

    QRhiShaderResourceBindings *&srb = dcd.srb;
    bool srbChanged = false;
    if (!srb || bindings != dcd.bindings) {
        srb = rhiCtxD->srb(bindings);
        rhiCtxD->releaseCachedSrb(dcd.bindings);
        dcd.bindings = bindings;
        srbChanged = true;
    }

    subsetRenderable.rhiRenderData.motionVectorPass.srb = srb;

    const auto pipelineKey = QSSGGraphicsPipelineStateKey::create(*ps, renderPassDescriptor, srb);
    if (dcd.pipeline
        && !srbChanged
        && dcd.renderTargetDescriptionHash == pipelineKey.extra.renderTargetDescriptionHash
        && dcd.renderTargetDescription == pipelineKey.renderTargetDescription
        && dcd.ps == *ps)
    {
        subsetRenderable.rhiRenderData.motionVectorPass.pipeline = dcd.pipeline;
    } else {

        subsetRenderable.rhiRenderData.motionVectorPass.pipeline = rhiCtxD->pipeline(pipelineKey,
                                                                                     renderPassDescriptor,
                                                                                     srb);
        dcd.pipeline = subsetRenderable.rhiRenderData.motionVectorPass.pipeline;
        dcd.renderTargetDescriptionHash = pipelineKey.extra.renderTargetDescriptionHash;
        dcd.renderTargetDescription = pipelineKey.renderTargetDescription;
        dcd.ps = *ps;
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 3133, as _ZNK32QSSGLayerRenderPreparationResult17textureDimensionsEv
inline QSize QSSGLayerRenderPreparationResult::textureDimensions() const
{
    const auto size = viewport.size().toSize();
    return QSize(QSSGRendererUtil::nextMultipleOf4(size.width()), QSSGRendererUtil::nextMultipleOf4(size.height()));
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 156, as _ZN19MotionVectorMapPass13resetForFrameEv
inline void MotionVectorMapPass::resetForFrame()
{
    QSSG_CHECK(motionVectorMapManager);
    motionVectorMapManager->endFrame();
    camera = nullptr;
    ps = {};
    rhiMotionVectorTexture = nullptr;
    for (int i = 0; i < MaxBuckets; ++i)
        motionVectorPassObjects[i].clear();
}
//  -----------------------------------------------------------------------

//  Type MotionVectorMapPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK19MotionVectorMapPass8passTypeEv(
    const MotionVectorMapPass *self) {
  return self->passType();
}

//  void MotionVectorMapPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19MotionVectorMapPass13resetForFrameEv(
    MotionVectorMapPass *self) {
  self->resetForFrame();
}

//  MotionVectorMapPass::~MotionVectorMapPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN19MotionVectorMapPassD1Ev(MotionVectorMapPass *self) {
  delete self;
}
