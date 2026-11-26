//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgfrustum_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendergraphobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <optional>
#include <QtCore/QPointF>
#include <QtCore/QVarLengthArray>
#include <QtGui/QVector3D>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/private/qquick3dlightmapbaker_p.h>
#include <QtQuick3D/private/qquick3dviewport_p.h>
#include <QtQuick3D/private/qquick3dcubemaptexture_p.h>
#include <QtQuick3D/private/qquick3dscenerenderer_p.h>
#include <QtQuick3D/private/qquick3dsceneenvironment_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3D/private/qquick3dnode_p.h>
#include <QtQuick3D/private/qquick3dscenemanager_p.h>
#include <QtQuick3D/private/qquick3dtexture_p.h>
#include <QtQuick3D/private/qquick3dcamera_p.h>
#include <QtQuick3D/private/qquick3dpickresult_p.h>
#include <QtQuick3D/private/qquick3dmodel_p.h>
#include <QtQuick3D/private/qquick3drenderstats_p.h>
#include <QtQuick3D/private/qquick3ddebugsettings_p.h>
#include <QtQuick3D/private/qquick3dskymaterial_p.h>
#include <QtQuick3DUtils/private/qquick3dprofiler_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendererutil_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qsgrendernode_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtQuick3DRuntimeRender/private/qssgcputonemapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderroot_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtCore/QObject>
#include <QtCore/qqueue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dlightmapbaker.cpp, line 238, as _ZNK21QQuick3DLightmapBaker13BakingControl11isCancelledEv
inline bool QQuick3DLightmapBaker::BakingControl::isCancelled() const {
    return cancelFlag;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 201, as _ZN21QQuick3DSceneRendererC1ERKSt10shared_ptrI26QSSGRenderContextInterfaceE
inline QQuick3DSceneRenderer::QQuick3DSceneRenderer(const std::shared_ptr<QSSGRenderContextInterface> &rci)
    : m_sgContext(rci)
{
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 206, as _ZN21QQuick3DSceneRendererD1Ev
inline QQuick3DSceneRenderer::~QQuick3DSceneRenderer()
{
    const auto &rhiCtx = m_sgContext->rhiContext();
    auto *rhi = rhiCtx->rhi();
    rhi->finish(); // finish active readbacks
    QSSGRhiContextStats::get(*rhiCtx).cleanupLayerInfo(m_layer);
    m_sgContext->bufferManager()->releaseResourcesForLayer(m_layer);

    if (m_layer) {
        // The scene root is created by the scene manager and released by the normal cleanup of
        // scene nodes. Since we delete the layer at a later point, detach the scene root from the
        // layer now. QSSGRenderNode::removeChild() ignores a node that is no longer a child of
        // the layer, so this is safe even if the scene manager has already cleaned up (and
        // unlinked) the scene root.
        if (m_sceneRootNode)
            removeNodeFromLayer(m_sceneRootNode);
        m_sceneRootNode = nullptr;

        // There might be nodes queued for cleanup that still reference the layer,
        // so we schedule the layer for cleanup so that it is deleted after the nodes
        // have been cleaned up.
        if (winAttacment)
            winAttacment->queueForCleanup(m_layer);
        else
            delete m_layer;
        m_layer = nullptr;
    }

    delete m_texture;

    releaseAaDependentRhiResources();
    delete m_effectSystem;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 571, as _ZN21QQuick3DSceneRenderer10beginFrameEv
inline void QQuick3DSceneRenderer::beginFrame()
{
    m_sgContext->renderer()->beginFrame(*m_layer);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 576, as _ZN21QQuick3DSceneRenderer8endFrameEv
inline void QQuick3DSceneRenderer::endFrame()
{
    m_sgContext->renderer()->endFrame(*m_layer);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 581, as _ZN21QQuick3DSceneRenderer10rhiPrepareERK5QRectd
inline void QQuick3DSceneRenderer::rhiPrepare(const QRect &viewport, qreal displayPixelRatio)
{
    if (!m_layer)
        return;

    const auto &renderer = m_sgContext->renderer();

    renderer->setDpr(displayPixelRatio);

    renderer->setViewport(viewport);

    renderer->prepareLayerForRender(*m_layer);
    // If sync was called the assumption is that the scene is dirty regardless of what
    // the scene prep function says, we still should verify that we have a camera before
    // we call render prep and render.
    const bool renderReady = !m_layer->renderData->renderedCameras.isEmpty();
    if (renderReady) {
        renderer->rhiPrepare(*m_layer);
        m_prepared = true;
    }
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 603, as _ZN21QQuick3DSceneRenderer9rhiRenderEv
inline void QQuick3DSceneRenderer::rhiRender()
{
    if (m_prepared) {
        // There is no clearFirst flag - the rendering here does not record a
        // beginPass() so it never clears on its own.

        m_sgContext->renderer()->rhiRender(*m_layer);
    }

    m_prepared = false;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1273, as _ZN21QQuick3DSceneRenderer27invalidateFramebufferObjectEv
inline void QQuick3DSceneRenderer::invalidateFramebufferObject()
{
    if (fboNode)
        fboNode->invalidatePending = true;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1279, as _ZN21QQuick3DSceneRenderer22releaseCachedResourcesEv
inline void QQuick3DSceneRenderer::releaseCachedResources()
{
    if (m_layer && m_layer->renderData) {
        if (const auto &mgr = m_layer->renderData->getShadowMapManager())
            mgr->releaseCachedResources();
        if (const auto &mgr = m_layer->renderData->getReflectionMapManager())
            mgr->releaseCachedResources();
    }
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1289, as _ZN21QQuick3DSceneRenderer21getRayFromViewportPosERK7QPointF
inline std::optional<QSSGRenderRay> QQuick3DSceneRenderer::getRayFromViewportPos(const QPointF &pos)
{
    if (!m_layer || !m_layer->renderData)
        return std::nullopt;

    QMutexLocker locker(&m_layer->renderedCamerasMutex);

    if (m_layer->renderedCameras.isEmpty())
        return std::nullopt;

    QMatrix4x4 globalTransform = m_layer->renderData->getGlobalTransform(*m_layer->renderedCameras[0]);

    const QVector2D viewportSize(m_surfaceSize.width(), m_surfaceSize.height());
    const QVector2D position(float(pos.x()), float(pos.y()));
    const QRectF viewportRect(QPointF{}, QSizeF(m_surfaceSize));

    // First invert the y so we are dealing with numbers in a normal coordinate space.
    // Second, move into our layer's coordinate space
    QVector2D correctCoords(position.x(), viewportSize.y() - position.y());
    QVector2D theLocalMouse = QSSGUtils::rect::toRectRelative(viewportRect, correctCoords);
    if ((theLocalMouse.x() < 0.0f || theLocalMouse.x() >= viewportSize.x() || theLocalMouse.y() < 0.0f
         || theLocalMouse.y() >= viewportSize.y()))
        return std::nullopt;

    return m_layer->renderedCameras[0]->unproject(globalTransform, theLocalMouse, viewportRect);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1327, as _ZN21QQuick3DSceneRenderer8syncPickERK13QSSGRenderRay
inline QQuick3DSceneRenderer::PickResultList QQuick3DSceneRenderer::syncPick(const QSSGRenderRay &ray)
{
    if (!m_layer)
        return QQuick3DSceneRenderer::PickResultList();

    return QSSGRendererPrivate::syncPick(*m_sgContext,
                                         *m_layer,
                                         ray);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1337, as _ZN21QQuick3DSceneRenderer11syncPickOneERK13QSSGRenderRayP14QSSGRenderNode
inline QQuick3DSceneRenderer::PickResultList QQuick3DSceneRenderer::syncPickOne(const QSSGRenderRay &ray, QSSGRenderNode *node)
{
    if (!m_layer)
        return QQuick3DSceneRenderer::PickResultList();

    return QSSGRendererPrivate::syncPick(*m_sgContext,
                                         *m_layer,
                                         ray,
                                         node);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1348, as _ZN21QQuick3DSceneRenderer14syncPickSubsetERK13QSSGRenderRay15QVarLengthArrayIP14QSSGRenderNodeLx256EE
inline QQuick3DSceneRenderer::PickResultList QQuick3DSceneRenderer::syncPickSubset(const QSSGRenderRay &ray,
                                                                            QVarLengthArray<QSSGRenderNode *> subset)
{
    if (!m_layer)
        return QQuick3DSceneRenderer::PickResultList();

    return QSSGRendererPrivate::syncPickSubset(*m_layer,
                                               *m_sgContext->bufferManager(),
                                               ray,
                                               subset);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1360, as _ZN21QQuick3DSceneRenderer11syncPickAllERK13QSSGRenderRay
inline QQuick3DSceneRenderer::PickResultList QQuick3DSceneRenderer::syncPickAll(const QSSGRenderRay &ray)
{
    if (!m_layer)
        return QQuick3DSceneRenderer::PickResultList();

    return QSSGRendererPrivate::syncPickAll(*m_sgContext,
                                            *m_layer,
                                            ray);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1316, as _ZN21QQuick3DSceneRenderer20syncPickClosestPointERK9QVector3DfP14QSSGRenderNode
inline std::optional<QSSGRenderPickResult> QQuick3DSceneRenderer::syncPickClosestPoint(const QVector3D &center, float radiusSquared, QSSGRenderNode *node)
{
    if (!m_layer)
        return std::nullopt;

    return QSSGRendererPrivate::syncPickClosestPoint(*m_sgContext,
                                                     *m_layer,
                                                     center, radiusSquared,
                                                     node);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1370, as _ZN21QQuick3DSceneRenderer17syncPickInFrustumERK11QSSGFrustum
inline QList<const QSSGRenderNode *> QQuick3DSceneRenderer::syncPickInFrustum(const QSSGFrustum &frustum)
{
    if (!m_layer)
        return {};

    return QSSGRendererPrivate::syncPickInFrustum(*m_sgContext, *m_layer, frustum);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1378, as _ZN21QQuick3DSceneRenderer23setGlobalPickingEnabledEb
inline void QQuick3DSceneRenderer::setGlobalPickingEnabled(bool isEnabled)
{
    QSSGRendererPrivate::setGlobalPickingEnabled(*m_sgContext->renderer(), isEnabled);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1383, as _ZN21QQuick3DSceneRenderer11renderStatsEv
inline QQuick3DRenderStats *QQuick3DSceneRenderer::renderStats()
{
    return m_renderStats;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 240, as _ZN21QQuick3DSceneRenderer30releaseAaDependentRhiResourcesEv
inline void QQuick3DSceneRenderer::releaseAaDependentRhiResources()
{
    const auto &rhiCtx = m_sgContext->rhiContext();
    if (!rhiCtx->isValid())
        return;

    delete m_textureRenderTarget;
    m_textureRenderTarget = nullptr;

    delete m_textureRenderPassDescriptor;
    m_textureRenderPassDescriptor = nullptr;

    delete m_depthStencilBuffer;
    m_depthStencilBuffer = nullptr;

    delete m_multiViewDepthStencilBuffer;
    m_multiViewDepthStencilBuffer = nullptr;

    delete m_msaaRenderBufferLegacy;
    m_msaaRenderBufferLegacy = nullptr;

    delete m_msaaRenderTexture;
    m_msaaRenderTexture = nullptr;

    delete m_msaaMultiViewRenderBuffer;
    m_msaaMultiViewRenderBuffer = nullptr;

    delete m_ssaaTexture;
    m_ssaaTexture = nullptr;

    delete m_ssaaTextureToTextureRenderTarget;
    m_ssaaTextureToTextureRenderTarget = nullptr;

    delete m_ssaaTextureToTextureRenderPassDescriptor;
    m_ssaaTextureToTextureRenderPassDescriptor = nullptr;

    delete m_temporalAATexture;
    m_temporalAATexture = nullptr;
    delete m_temporalAARenderTarget;
    m_temporalAARenderTarget = nullptr;
    delete m_temporalAARenderPassDescriptor;
    m_temporalAARenderPassDescriptor = nullptr;

    delete m_prevTempAATexture;
    m_prevTempAATexture = nullptr;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1405, as _ZN21QQuick3DSceneRenderer15updateLayerNodeER15QSSGRenderLayerRK16QQuick3DViewportRK5QListIP21QSSGRenderGraphObjectE
inline void QQuick3DSceneRenderer::updateLayerNode(QSSGRenderLayer &layerNode,
                                            const QQuick3DViewport &view3D,
                                            const QList<QSSGRenderGraphObject *> &resourceLoaders)
{
    QQuick3DSceneEnvironment *environment = view3D.environment();
    const auto &effects = environment->effectList();

    QSSGRenderLayer::AAMode aaMode = QSSGRenderLayer::AAMode(environment->antialiasingMode());
    if (aaMode != layerNode.antialiasingMode) {
        layerNode.antialiasingMode = aaMode;
        layerNode.progAAPassIndex = 0;
        m_aaIsDirty = true;
    }
    QSSGRenderLayer::AAQuality aaQuality = QSSGRenderLayer::AAQuality(environment->antialiasingQuality());
    if (aaQuality != layerNode.antialiasingQuality) {
        layerNode.antialiasingQuality = aaQuality;
        layerNode.ssaaMultiplier = QSSGRenderLayer::ssaaMultiplierForQuality(aaQuality);
        m_aaIsDirty = true;
    }

    // NOTE: Temporal AA is disabled when MSAA is enabled.
    const bool temporalAARequested = environment->temporalAAEnabled();
    const bool wasTaaEnabled = layerNode.isTemporalAAEnabled();
    layerNode.temporalAAMode = temporalAARequested ? QSSGRenderLayer::TAAMode(environment->m_temporalAAMode + 1) // map the environment mode to the layer mode
                                                   : QSSGRenderLayer::TAAMode::Off;

    // If the state changed we need to reset the temporal AA pass index etc.
    if (wasTaaEnabled != layerNode.isTemporalAAEnabled()) {
        layerNode.tempAAPassIndex = 0;
        m_aaIsDirty = true;
        m_temporalIsDirty = true;
    }

    layerNode.temporalAAStrength = environment->temporalAAStrength();

    layerNode.specularAAEnabled = environment->specularAAEnabled();

    layerNode.background = QSSGRenderLayer::Background(environment->backgroundMode());
    layerNode.clearColor = QVector3D(float(environment->clearColor().redF()),
                                      float(environment->clearColor().greenF()),
                                      float(environment->clearColor().blueF()));

    layerNode.gridEnabled = environment->gridEnabled();
    layerNode.gridScale = environment->gridScale();
    layerNode.gridFlags = environment->gridFlags();

    layerNode.aoStrength = environment->aoStrength();
    layerNode.aoDistance = environment->aoDistance();
    layerNode.aoSoftness = environment->aoSoftness();
    layerNode.aoEnabled = environment->aoEnabled();
    layerNode.aoBias = environment->aoBias();
    layerNode.aoSamplerate = environment->aoSampleRate();
    layerNode.aoDither = environment->aoDither();

    // ### These images will not be registered anywhere
    if (environment->lightProbe()) {
        layerNode.lightProbe = environment->lightProbe()->getRenderImage();
        // FIXME: Band-aid. Need a proper solution where textureData is setting the format of the render node.
        if (auto texData = environment->lightProbe()->textureData();
            texData && texData->format() == QQuick3DTextureData::Format::RGBE8) {
            layerNode.lightProbe->m_format = QSSGRenderTextureFormat::Format::RGBE8;
        }
    } else
        layerNode.lightProbe = nullptr;
    if (view3D.environment()->skyBoxCubeMap())
        layerNode.skyBoxCubeMap = view3D.environment()->skyBoxCubeMap()->getRenderImage();
    else
        layerNode.skyBoxCubeMap = nullptr;

    layerNode.skyMaterial = nullptr;
    if (auto skyMaterial = environment->skyMaterial())
        layerNode.skyMaterial = static_cast<QSSGRenderSkyMaterial *>(QQuick3DObjectPrivate::get(skyMaterial)->spatialNode);

    layerNode.lightProbeSettings.probeExposure = environment->probeExposure();
    // Remap the probeHorizon to the expected Range
    layerNode.lightProbeSettings.probeHorizon = qMin(environment->probeHorizon() - 1.0f, -0.001f);
    layerNode.setProbeOrientation(environment->probeOrientation());

    QQuick3DViewport::updateCameraForLayer(view3D, layerNode);

    layerNode.layerFlags.setFlag(QSSGRenderLayer::LayerFlag::EnableDepthTest, environment->depthTestEnabled());
    layerNode.layerFlags.setFlag(QSSGRenderLayer::LayerFlag::EnableDepthPrePass, environment->depthPrePassEnabled());

    layerNode.tonemapMode = QQuick3DSceneRenderer::getTonemapMode(*environment);
    layerNode.skyboxBlurAmount = environment->skyboxBlurAmount();
    if (auto debugSettings = view3D.environment()->debugSettings()) {
        layerNode.debugMode = QSSGRenderLayer::MaterialDebugMode(debugSettings->materialOverride());
        layerNode.wireframeMode = debugSettings->wireframeEnabled();
        layerNode.drawDirectionalLightShadowBoxes = debugSettings->drawDirectionalLightShadowBoxes();
        layerNode.drawPointLightShadowBoxes = debugSettings->drawPointLightShadowBoxes();
        layerNode.drawShadowCastingBounds = debugSettings->drawShadowCastingBounds();
        layerNode.drawShadowReceivingBounds = debugSettings->drawShadowReceivingBounds();
        layerNode.drawCascades = debugSettings->drawCascades();
        layerNode.drawSceneCascadeIntersection = debugSettings->drawSceneCascadeIntersection();
        layerNode.disableShadowCameraUpdate = debugSettings->disableShadowCameraUpdate();
        layerNode.drawCulledObjects = debugSettings->drawCulledObjects();
    } else {
        layerNode.debugMode = QSSGRenderLayer::MaterialDebugMode::None;
        layerNode.wireframeMode = false;
    }

    if (environment->fog() && environment->fog()->isEnabled()) {
        layerNode.fog.enabled = true;
        const QQuick3DFog *fog = environment->fog();
        layerNode.fog.color = QSSGUtils::color::sRGBToLinear(fog->color()).toVector3D();
        layerNode.fog.density = fog->density();
        layerNode.fog.depthEnabled = fog->isDepthEnabled();
        layerNode.fog.depthBegin = fog->depthNear();
        layerNode.fog.depthEnd = fog->depthFar();
        layerNode.fog.depthCurve = fog->depthCurve();
        layerNode.fog.heightEnabled = fog->isHeightEnabled();
        layerNode.fog.heightMin = fog->leastIntenseY();
        layerNode.fog.heightMax = fog->mostIntenseY();
        layerNode.fog.heightCurve = fog->heightCurve();
        layerNode.fog.transmitEnabled = fog->isTransmitEnabled();
        layerNode.fog.transmitCurve = fog->transmitCurve();
    } else {
        layerNode.fog.enabled = false;
    }
    const auto method = static_cast<QSSGRenderLayer::OITMethod>(environment->oitMethod());
    layerNode.oitMethodDirty = method != layerNode.oitMethod;
    layerNode.oitMethod = method;

    // Effects need to be rendered in reverse order as described in the file.
    // NOTE: We only build up the list here, don't do anything that depends
    //       on the collected layer state yet. See sync() for that.
    layerNode.firstEffect = nullptr; // We reset the linked list
    auto rit = effects.crbegin();
    const auto rend = effects.crend();
    for (; rit != rend; ++rit) {
        QQuick3DObjectPrivate *p = QQuick3DObjectPrivate::get(*rit);
        QSSGRenderEffect *effectNode = static_cast<QSSGRenderEffect *>(p->spatialNode);
        if (effectNode) {
            if (layerNode.hasEffect(effectNode)) {
                qWarning() << "Duplicate effect found, skipping!";
            } else {
                effectNode->className = (*rit)->metaObject()->className(); //### persistent, but still icky to store a const char* returned from a function
                layerNode.addEffect(*effectNode);
            }
        }
    }

    const bool hasEffects = (layerNode.firstEffect != nullptr);

    const auto renderMode = view3D.renderMode();

    const bool progressiveAA = layerNode.isProgressiveAAEnabled();
    const bool temporalAA = layerNode.isTemporalAAEnabled();
    const bool superSamplingAA = layerNode.isSsaaEnabled();
    m_timeBasedAA = progressiveAA || temporalAA;
    m_postProcessingStack = hasEffects || m_timeBasedAA  || superSamplingAA;
    m_useFBO = renderMode == QQuick3DViewport::RenderMode::Offscreen ||
            ((renderMode == QQuick3DViewport::RenderMode::Underlay || renderMode == QQuick3DViewport::RenderMode::Overlay)
             && m_postProcessingStack);

    // Update the view count

    // NOTE: If we're rendering to an FBO, the view count is more than 1, and the View3D is not an XR view instance,
    // we need to force the view count to 1 (The only time this should be the case is when embedding View3D(s)
    // in XR with multiview enabled).
    // Also, note that embedding View3D(s) in XR with multiview enabled only works if those View3D(s) are
    // being rendered through a FBO.
    if (m_useFBO && (layerNode.viewCount > 1) && !view3D.isXrViewInstance())
        layerNode.viewCount = 1;

    // ResourceLoaders
    layerNode.resourceLoaders.clear();
    layerNode.resourceLoaders = resourceLoaders;

    layerNode.renderOverrides = QSSGRenderLayer::RenderOverridesT(view3D.renderOverrides().toInt());
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1668, as _ZN21QQuick3DSceneRenderer14addNodeToLayerEP14QSSGRenderNode
inline void QQuick3DSceneRenderer::addNodeToLayer(QSSGRenderNode *node)
{
    if (!m_layer)
        return;

    m_layer->addChild(*node);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1577, as _ZN21QQuick3DSceneRenderer19removeNodeFromLayerEP14QSSGRenderNode
inline void QQuick3DSceneRenderer::removeNodeFromLayer(QSSGRenderNode *node)
{
    if (!m_layer)
        return;

    m_layer->removeChild(*node);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1585, as _ZN21QQuick3DSceneRenderer24maybeSetupLightmapBakingEP16QQuick3DViewport
inline void QQuick3DSceneRenderer::maybeSetupLightmapBaking(QQuick3DViewport *view3D)
{
    if (m_layer->renderData && m_layer->renderData->lightmapBaker)
        return;

    // Check if we have interactive bake requested or if we are coming in here the second
    // time from cmd line request (needs to wait a frame before starting to bake).
    bool bakeRequested = false;
    bool denoiseRequested = false;
    bool fromCmd = false;
    QQuick3DLightmapBaker *lightmapBaker = view3D->maybeLightmapBaker();
    if (lightmapBaker && (lightmapBaker->m_bakingRequested || lightmapBaker->m_denoisingRequested)) {
        bakeRequested = std::exchange(lightmapBaker->m_bakingRequested, false);
        denoiseRequested = std::exchange(lightmapBaker->m_denoisingRequested, false);
    } else {
        bakeRequested = m_lightmapBakingFromCmdRequested;
        denoiseRequested = m_lightmapDenoisingFromCmdRequested;
        fromCmd = bakeRequested;
    }

    // Start the bake (we should have a valid layer render data at this point).
    if (bakeRequested || denoiseRequested) {
        QSSGLightmapBaker::Context ctx;
        ctx.settings.bakeRequested = bakeRequested;
        ctx.settings.denoiseRequested = denoiseRequested;
        ctx.settings.quitWhenFinished = fromCmd;

        // We want the frontend callback in the case that a QQuick3DLightmapBaker is present
        if (lightmapBaker) {
            QQuick3DLightmapBaker::Callback qq3dCallback = lightmapBaker->m_callback;
            QQuick3DLightmapBaker::BakingControl *qq3dBakingControl = lightmapBaker->m_bakingControl;
            QSSGLightmapper::Callback callback =
                [qq3dCallback,
                 qq3dBakingControl](const QVariantMap &payload,
                                    QSSGLightmapper::BakingControl *qssgBakingControl) {
                    qq3dCallback(payload, qq3dBakingControl);

                    if (qq3dBakingControl->isCancelled() && !qssgBakingControl->cancelled)
                        qssgBakingControl->cancelled = true;
                };
            ctx.callbacks.lightmapBakingOutput = callback;
        }

        // Both the QQuick3DLightmapBaker and cmd / env variant needs this
        ctx.callbacks.triggerNewFrame = [view3D](bool releaseResources) {
            if (releaseResources) {
                QMetaObject::invokeMethod(view3D->window(),
                                            &QQuickWindow::releaseResources,
                                            Qt::QueuedConnection);
            }
            QMetaObject::invokeMethod(view3D, &QQuick3DViewport::update, Qt::QueuedConnection);
        };
        ctx.callbacks.setCurrentlyBaking = [this](bool value) {
            m_sgContext->bufferManager()->setCurrentlyLightmapBaking(value);
        };

        ctx.env.rhiCtx = m_sgContext->rhiContext().get();
        ctx.env.renderer = m_sgContext->renderer().get();
        ctx.env.lmOptions = lmOptions;
        m_layer->renderData->initializeLightmapBaking(ctx);

    } else {
        // Check cmd line and env flags for request
        static bool flagsChecked = false;
        if (flagsChecked)
            return;
        flagsChecked = true;

        auto isLightmapFlagSet = [](const QString &flag, const char *envVar) {
            return QCoreApplication::arguments().contains(flag)
            || qEnvironmentVariableIntValue(envVar);
        };

        m_lightmapBakingFromCmdRequested = isLightmapFlagSet(QStringLiteral("--bake-lightmaps"), "QT_QUICK3D_BAKE_LIGHTMAPS");
        m_lightmapDenoisingFromCmdRequested = isLightmapFlagSet(QStringLiteral("--denoise-lightmaps"), "QT_QUICK3D_DENOISE_LIGHTMAPS");

        if (m_lightmapBakingFromCmdRequested || m_lightmapDenoisingFromCmdRequested) {
            // Delay one frame so the render data is initialized
            QMetaObject::invokeMethod(view3D, &QQuick3DViewport::update, Qt::QueuedConnection);
        }
    }
}
//  -----------------------------------------------------------------------

//  QQuick3DSceneRenderer::QQuick3DSceneRenderer(const
//      std::shared_ptr<QSSGRenderContextInterface> &rci)
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer *ritual_ZN21QQuick3DSceneRendererC1ERKSt10shared_ptrI26QSSGRenderContextInterfaceE(
    const std::shared_ptr<QSSGRenderContextInterface> *rci) {
  return new QQuick3DSceneRenderer(*rci);
}

//  QQuick3DSceneRenderer::~QQuick3DSceneRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRendererD1Ev(QQuick3DSceneRenderer *self) {
  delete self;
}

//  QSSGRenderLayer::TonemapMode QQuick3DSceneRenderer::getTonemapMode(const
//      QQuick3DSceneEnvironment &environment)
extern "C" Q_DECL_EXPORT
QSSGRenderLayer::TonemapMode ritual_ZN21QQuick3DSceneRenderer14getTonemapModeERK24QQuick3DSceneEnvironment(
    const QQuick3DSceneEnvironment *environment) {
  return QQuick3DSceneRenderer::getTonemapMode(*environment);
}

//  void QQuick3DSceneRenderer::beginFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer10beginFrameEv(
    QQuick3DSceneRenderer *self) {
  self->beginFrame();
}

//  void QQuick3DSceneRenderer::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer8endFrameEv(
    QQuick3DSceneRenderer *self) {
  self->endFrame();
}

//  void QQuick3DSceneRenderer::rhiPrepare(const QRect &viewport, qreal
//      displayPixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer10rhiPrepareERK5QRectd(
    QQuick3DSceneRenderer *self,
    const QRect *viewport,
    qreal displayPixelRatio) {
  self->rhiPrepare(*viewport, displayPixelRatio);
}

//  void QQuick3DSceneRenderer::rhiRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer9rhiRenderEv(
    QQuick3DSceneRenderer *self) {
  self->rhiRender();
}

//  void QQuick3DSceneRenderer::invalidateFramebufferObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer27invalidateFramebufferObjectEv(
    QQuick3DSceneRenderer *self) {
  self->invalidateFramebufferObject();
}

//  QSize QQuick3DSceneRenderer::surfaceSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QQuick3DSceneRenderer11surfaceSizeEv(
    const QQuick3DSceneRenderer *self) {
  return new QSize(self->surfaceSize());
}

//  void QQuick3DSceneRenderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer22releaseCachedResourcesEv(
    QQuick3DSceneRenderer *self) {
  self->releaseCachedResources();
}

//  std::optional<QSSGRenderRay>
//      QQuick3DSceneRenderer::getRayFromViewportPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
std::optional<QSSGRenderRay> *ritual_ZN21QQuick3DSceneRenderer21getRayFromViewportPosERK7QPointF(
    QQuick3DSceneRenderer *self,
    const QPointF *pos) {
  return new std::optional<QSSGRenderRay>(self->getRayFromViewportPos(*pos));
}

//  PickResultList QQuick3DSceneRenderer::syncPick(const QSSGRenderRay &ray)
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer::PickResultList *ritual_ZN21QQuick3DSceneRenderer8syncPickERK13QSSGRenderRay(
    QQuick3DSceneRenderer *self,
    const QSSGRenderRay *ray) {
  return new QQuick3DSceneRenderer::PickResultList(self->syncPick(*ray));
}

//  PickResultList QQuick3DSceneRenderer::syncPickOne(const QSSGRenderRay
//      &ray, QSSGRenderNode *node)
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer::PickResultList *ritual_ZN21QQuick3DSceneRenderer11syncPickOneERK13QSSGRenderRayP14QSSGRenderNode(
    QQuick3DSceneRenderer *self,
    const QSSGRenderRay *ray,
    QSSGRenderNode *node) {
  return new QQuick3DSceneRenderer::PickResultList(
      self->syncPickOne(
          *ray,
          node));
}

//  PickResultList QQuick3DSceneRenderer::syncPickSubset(const QSSGRenderRay
//      &ray, QVarLengthArray<QSSGRenderNode *> subset)
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer::PickResultList *ritual_ZN21QQuick3DSceneRenderer14syncPickSubsetERK13QSSGRenderRay15QVarLengthArrayIP14QSSGRenderNodeLx256EE(
    QQuick3DSceneRenderer *self,
    const QSSGRenderRay *ray,
    const QVarLengthArray<QSSGRenderNode *> *subset) {
  return new QQuick3DSceneRenderer::PickResultList(
      self->syncPickSubset(
          *ray,
          *subset));
}

//  PickResultList QQuick3DSceneRenderer::syncPickAll(const QSSGRenderRay
//      &ray)
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer::PickResultList *ritual_ZN21QQuick3DSceneRenderer11syncPickAllERK13QSSGRenderRay(
    QQuick3DSceneRenderer *self,
    const QSSGRenderRay *ray) {
  return new QQuick3DSceneRenderer::PickResultList(self->syncPickAll(*ray));
}

//  std::optional<QSSGRenderPickResult>
//      QQuick3DSceneRenderer::syncPickClosestPoint(const QVector3D &center,
//      float radiusSquared, QSSGRenderNode *node)
extern "C" Q_DECL_EXPORT
std::optional<QSSGRenderPickResult> *ritual_ZN21QQuick3DSceneRenderer20syncPickClosestPointERK9QVector3DfP14QSSGRenderNode(
    QQuick3DSceneRenderer *self,
    const QVector3D *center,
    float radiusSquared,
    QSSGRenderNode *node) {
  return new std::optional<QSSGRenderPickResult>(
      self->syncPickClosestPoint(
          *center,
          radiusSquared,
          node));
}

//  QList<const QSSGRenderNode *>
//      QQuick3DSceneRenderer::syncPickInFrustum(const QSSGFrustum &frustum)
extern "C" Q_DECL_EXPORT
QList<const QSSGRenderNode *> *ritual_ZN21QQuick3DSceneRenderer17syncPickInFrustumERK11QSSGFrustum(
    QQuick3DSceneRenderer *self,
    const QSSGFrustum *frustum) {
  return new QList<const QSSGRenderNode *>(
      self->syncPickInFrustum(
          *frustum));
}

//  void QQuick3DSceneRenderer::setGlobalPickingEnabled(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer23setGlobalPickingEnabledEb(
    QQuick3DSceneRenderer *self,
    bool isEnabled) {
  self->setGlobalPickingEnabled(isEnabled);
}

//  QQuick3DRenderStats *QQuick3DSceneRenderer::renderStats()
extern "C" Q_DECL_EXPORT
QQuick3DRenderStats *ritual_ZN21QQuick3DSceneRenderer11renderStatsEv(
    QQuick3DSceneRenderer *self) {
  return self->renderStats();
}

//  void QQuick3DSceneRenderer::releaseAaDependentRhiResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer30releaseAaDependentRhiResourcesEv(
    QQuick3DSceneRenderer *self) {
  self->releaseAaDependentRhiResources();
}

//  void QQuick3DSceneRenderer::updateLayerNode(QSSGRenderLayer &layerNode,
//      const QQuick3DViewport &view3D, const QList<QSSGRenderGraphObject *>
//      &resourceLoaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer15updateLayerNodeER15QSSGRenderLayerRK16QQuick3DViewportRK5QListIP21QSSGRenderGraphObjectE(
    QQuick3DSceneRenderer *self,
    QSSGRenderLayer *layerNode,
    const QQuick3DViewport *view3D,
    const QList<QSSGRenderGraphObject *> *resourceLoaders) {
  self->updateLayerNode(*layerNode, *view3D, *resourceLoaders);
}

//  void QQuick3DSceneRenderer::addNodeToLayer(QSSGRenderNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer14addNodeToLayerEP14QSSGRenderNode(
    QQuick3DSceneRenderer *self,
    QSSGRenderNode *node) {
  self->addNodeToLayer(node);
}

//  void QQuick3DSceneRenderer::removeNodeFromLayer(QSSGRenderNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer19removeNodeFromLayerEP14QSSGRenderNode(
    QQuick3DSceneRenderer *self,
    QSSGRenderNode *node) {
  self->removeNodeFromLayer(node);
}

//  void QQuick3DSceneRenderer::maybeSetupLightmapBaking(QQuick3DViewport
//      *view3D)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRenderer24maybeSetupLightmapBakingEP16QQuick3DViewport(
    QQuick3DSceneRenderer *self,
    QQuick3DViewport *view3D) {
  self->maybeSetupLightmapBaking(view3D);
}

//  a std::optional<QSSGRenderRay> a ritual of QQuick3DSceneRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSceneRenderer__std_optional_QSSGRenderRay(
    std::optional<QSSGRenderRay> *self) {
  delete self;
}

//  a QQuick3DSceneRenderer::PickResultList a ritual of QQuick3DSceneRenderer
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSceneRenderer__QQuick3DSceneRenderer_PickResultList(
    QQuick3DSceneRenderer::PickResultList *self) {
  delete self;
}

//  a std::optional<QSSGRenderPickResult> a ritual of QQuick3DSceneRenderer
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSceneRenderer__std_optional_QSSGRenderPickResult(
    std::optional<QSSGRenderPickResult> *self) {
  delete self;
}

//  a QList<const QSSGRenderNode *> a ritual of QQuick3DSceneRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DSceneRenderer__QList_const_QSSGRenderNode(
    QList<const QSSGRenderNode *> *self) {
  delete self;
}
