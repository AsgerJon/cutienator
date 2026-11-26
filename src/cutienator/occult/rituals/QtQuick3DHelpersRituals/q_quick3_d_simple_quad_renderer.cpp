//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/qquick3dsimplequadrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3dsimplequadrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/private/qquick3dsimplequadrenderpass_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <ssg/qssgrendercontextcore.h>
#include <ssg/qssgrenderextensions.h>
#include <QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/helpers/qquick3dsimplequadrenderpass.cpp, line 88, as local:qquick3dsimplequadrenderpass.cpp:QSSGRenderSimpleQuadRenderer
class QSSGRenderSimpleQuadRenderer : public QSSGRenderExtension
{
    static constexpr FlagT flags = FlagT(Flags::HasGraphicsResources) | FlagT(QSSGRenderGraphObjectUtils::InternalFlags::AutoRegisterExtension);
public:
    QSSGRenderSimpleQuadRenderer()
        : QSSGRenderExtension(QSSGRenderGraphObject::Type::RenderExtension, flags)
    {
    }

    virtual bool prepareData(QSSGFrameData &data) final
    {
        bool wasDirty = true;

        if (image)
            renderImage = data.contextInterface()->bufferManager()->loadRenderImage(image);
        else
            renderImage = QSSGRenderImageTexture();

        wasDirty = (renderImage.m_texture != nullptr);

        return wasDirty;
    }

    virtual void prepareRender(QSSGFrameData &data) final
    {
        if (renderImage.m_texture) {
            const auto &rhiCtx = data.contextInterface()->rhiContext();
            const auto &renderer = data.contextInterface()->renderer();
            QRhiResourceUpdateBatch *rub = rhiCtx->rhi()->nextResourceUpdateBatch();
            renderer->rhiQuadRenderer()->prepareQuad(rhiCtx.get(), rub);
        }
    }

    virtual void render(QSSGFrameData &data) final
    {
        if (renderImage.m_texture) {
            const auto &rhiCtx = data.contextInterface()->rhiContext();
            const auto &renderer = data.contextInterface()->renderer();
            const auto &shaderCache = data.contextInterface()->shaderCache();

            QSSGRhiGraphicsPipelineState ps = data.getPipelineState();
            QRhiCommandBuffer *cb = rhiCtx->commandBuffer();
            cb->debugMarkBegin(QByteArrayLiteral("QtQuick3D Blit Pass"));

            const auto tonemapMode = QSSGLayerRenderData::getCurrent(data)->layer.tonemapMode;
            const auto &shaderPipeline = shaderCache->getBuiltInRhiShaders().getRhiSimpleQuadShader(ps.viewCount, tonemapMode);

            QRhiSampler *sampler = rhiCtx->sampler({ QRhiSampler::Linear, QRhiSampler::Linear, QRhiSampler::None,
                                                     QRhiSampler::ClampToEdge, QRhiSampler::ClampToEdge, QRhiSampler::ClampToEdge });
            QSSGRhiShaderResourceBindingList bindings;
            bindings.addTexture(0, QRhiShaderResourceBinding::FragmentStage, renderImage.m_texture, sampler);
            QSSGRhiContextPrivate *rhiCtxD = QSSGRhiContextPrivate::get(rhiCtx.get());
            QRhiShaderResourceBindings *srb = rhiCtxD->srb(bindings);

            QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(ps, shaderPipeline.get());
            renderer->rhiQuadRenderer()->recordRenderQuad(rhiCtx.get(), &ps, srb, rhiCtx->mainRenderPassDescriptor(), QSSGRhiQuadRenderer::UvCoords | QSSGRhiQuadRenderer::PremulBlend);
            cb->debugMarkEnd();
        }
    }
    virtual void resetForFrame() final {}
    virtual RenderMode mode() const final { return RenderMode::Main; }
    virtual RenderStage stage() const final { return RenderStage::PostColor; }

    QSSGRenderImage *image = nullptr;
    QSSGRenderImageTexture renderImage;
    QRhiShaderResourceBindings *srb = nullptr;
    QSSGRhiShaderPipelinePtr quadShaderPipeline;
};

//  from ../qtquick3d/src/helpers/qquick3dsimplequadrenderpass.cpp, line 180, as _ZNK26QQuick3DSimpleQuadRenderer7textureEv
inline QQuick3DTexture *QQuick3DSimpleQuadRenderer::texture() const
{
    return m_source;
}

//  from ../qtquick3d/src/helpers/qquick3dsimplequadrenderpass.cpp, line 174, as _ZN26QQuick3DSimpleQuadRenderer10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuick3DSimpleQuadRenderer::itemChange(QQuick3DObject::ItemChange change, const QQuick3DObject::ItemChangeData &value)
{
    if (change == QQuick3DObject::ItemSceneChange)
        updateSceneManager(value.sceneManager);
}

//  from ../qtquick3d/src/helpers/qquick3dsimplequadrenderpass.cpp, line 198, as _ZN26QQuick3DSimpleQuadRenderer18updateSceneManagerEP20QQuick3DSceneManager
inline void QQuick3DSimpleQuadRenderer::updateSceneManager(QQuick3DSceneManager *sceneManager)
{
    if (sceneManager)
        QQuick3DObjectPrivate::refSceneManager(m_source, *sceneManager);
    else
        QQuick3DObjectPrivate::derefSceneManager(m_source);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuick3DSimpleQuadRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuick3DSimpleQuadRenderer10metaObjectEv(
    const QQuick3DSimpleQuadRenderer *self) {
  return self->metaObject();
}

//  void *QQuick3DSimpleQuadRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuick3DSimpleQuadRenderer11qt_metacastEPKc(
    QQuick3DSimpleQuadRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSimpleQuadRenderer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuick3DSimpleQuadRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSimpleQuadRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DTexture *QQuick3DSimpleQuadRenderer::texture() const
extern "C" Q_DECL_EXPORT
QQuick3DTexture *ritual_ZNK26QQuick3DSimpleQuadRenderer7textureEv(
    const QQuick3DSimpleQuadRenderer *self) {
  return self->texture();
}

//  void QQuick3DSimpleQuadRenderer::textureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DSimpleQuadRenderer14textureChangedEv(
    QQuick3DSimpleQuadRenderer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSimpleQuadRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textureChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textureChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSimpleQuadRenderer::itemChange(ItemChange a0, const
//      ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DSimpleQuadRenderer10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DSimpleQuadRenderer *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DSimpleQuadRenderer::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DSimpleQuadRenderer18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DSimpleQuadRenderer *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}
