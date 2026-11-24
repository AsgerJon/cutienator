//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1273, as _ZN21QQuick3DSceneRenderer27invalidateFramebufferObjectEv
inline void QQuick3DSceneRenderer::invalidateFramebufferObject()
{
    if (fboNode)
        fboNode->invalidatePending = true;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1577, as _ZN21QQuick3DSceneRenderer19removeNodeFromLayerEP14QSSGRenderNode
inline void QQuick3DSceneRenderer::removeNodeFromLayer(QSSGRenderNode *node)
{
    if (!m_layer)
        return;

    m_layer->removeChild(*node);
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

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 118, as _ZN23SGFramebufferObjectNodeD1Ev
inline SGFramebufferObjectNode::~SGFramebufferObjectNode()
{
    delete renderer;
    delete texture();
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 124, as _ZN23SGFramebufferObjectNode14scheduleRenderEv
inline void SGFramebufferObjectNode::scheduleRender()
{
    renderPending = true;
    markDirty(DirtyMaterial);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 130, as _ZNK23SGFramebufferObjectNode7textureEv
inline QSGTexture *SGFramebufferObjectNode::texture() const
{
    return QSGSimpleTextureNode::texture();
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 192, as _ZN23SGFramebufferObjectNode18handleScreenChangeEv
inline void SGFramebufferObjectNode::handleScreenChange()
{
    if (!qFuzzyCompare(window->effectiveDevicePixelRatio(), devicePixelRatio)) {
        renderer->invalidateFramebufferObject();
        quickFbo->update();
    }
}
//  -----------------------------------------------------------------------

//  SGFramebufferObjectNode::~SGFramebufferObjectNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SGFramebufferObjectNodeD1Ev(SGFramebufferObjectNode *self) {
  delete self;
}

//  void SGFramebufferObjectNode::scheduleRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SGFramebufferObjectNode14scheduleRenderEv(
    SGFramebufferObjectNode *self) {
  self->scheduleRender();
}

//  QSGTexture *SGFramebufferObjectNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK23SGFramebufferObjectNode7textureEv(
    const SGFramebufferObjectNode *self) {
  return self->texture();
}

//  void SGFramebufferObjectNode::handleScreenChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN23SGFramebufferObjectNode18handleScreenChangeEv(
    SGFramebufferObjectNode *self) {
  self->handleScreenChange();
}

//  SGFramebufferObjectNode as the QSGSimpleTextureNode it is built on
extern "C" Q_DECL_EXPORT
QSGSimpleTextureNode *ritual_cast_SGFramebufferObjectNode_QSGSimpleTextureNode(
    SGFramebufferObjectNode *self) {
  return static_cast<QSGSimpleTextureNode *>(self);
}
