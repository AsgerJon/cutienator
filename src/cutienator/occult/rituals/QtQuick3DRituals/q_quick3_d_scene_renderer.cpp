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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquick3dcubemaptexture_p.h"
#include "qquick3dscenerenderer_p.h"
#include "qquick3dsceneenvironment_p.h"
#include "qquick3dobject_p.h"
#include "qquick3dnode_p.h"
#include "qquick3dscenemanager_p.h"
#include "qquick3dtexture_p.h"
#include "qquick3dcamera_p.h"
#include "qquick3dpickresult_p.h"
#include "qquick3dmodel_p.h"
#include "qquick3drenderstats_p.h"
#include "qquick3ddebugsettings_p.h"
#include "qquick3dskymaterial_p.h"
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  QQuick3DSceneRenderer::~QQuick3DSceneRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DSceneRendererD1Ev(QQuick3DSceneRenderer *self) {
  delete self;
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
