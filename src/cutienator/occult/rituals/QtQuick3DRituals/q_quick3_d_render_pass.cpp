//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderpass_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qurl.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>

//  Only a class built on QQuick3DRenderPass may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DRenderPass : QQuick3DRenderPass {
  using QQuick3DRenderPass::updateSpatialNode;
  using QQuick3DRenderPass::itemChange;
  using QQuick3DRenderPass::markTrackedPropertyDirty;
};

//  const QMetaObject *QQuick3DRenderPass::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuick3DRenderPass10metaObjectEv(
    const QQuick3DRenderPass *self) {
  return self->metaObject();
}

//  QString QQuick3DRenderPass::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuick3DRenderPass2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRenderPass::tr(s, c, n));
}

//  QQuick3DRenderPass::QQuick3DRenderPass(QQuick3DObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRenderPass *ritual_ZN18QQuick3DRenderPassC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new QQuick3DRenderPass(parent);
}

//  QColor QQuick3DRenderPass::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QQuick3DRenderPass10clearColorEv(
    const QQuick3DRenderPass *self) {
  return new QColor(self->clearColor());
}

//  void QQuick3DRenderPass::setClearColor(const QColor &newClearColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass13setClearColorERK6QColor(
    QQuick3DRenderPass *self,
    const QColor *newClearColor) {
  self->setClearColor(*newClearColor);
}

//  MaterialModes QQuick3DRenderPass::materialMode() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPass::MaterialModes ritual_ZNK18QQuick3DRenderPass12materialModeEv(
    const QQuick3DRenderPass *self) {
  return self->materialMode();
}

//  void QQuick3DRenderPass::setMaterialMode(MaterialModes newMaterialMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass15setMaterialModeENS_13MaterialModesE(
    QQuick3DRenderPass *self,
    QQuick3DRenderPass::MaterialModes newMaterialMode) {
  self->setMaterialMode(newMaterialMode);
}

//  QQuick3DMaterial *QQuick3DRenderPass::overrideMaterial() const
extern "C" Q_DECL_EXPORT
QQuick3DMaterial *ritual_ZNK18QQuick3DRenderPass16overrideMaterialEv(
    const QQuick3DRenderPass *self) {
  return self->overrideMaterial();
}

//  void QQuick3DRenderPass::setOverrideMaterial(QQuick3DMaterial
//      *newOverrideMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass19setOverrideMaterialEP16QQuick3DMaterial(
    QQuick3DRenderPass *self,
    QQuick3DMaterial *newOverrideMaterial) {
  self->setOverrideMaterial(newOverrideMaterial);
}

//  QUrl QQuick3DRenderPass::augmentShader() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuick3DRenderPass13augmentShaderEv(
    const QQuick3DRenderPass *self) {
  return new QUrl(self->augmentShader());
}

//  void QQuick3DRenderPass::setAugmentShader(const QUrl &newAugmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass16setAugmentShaderERK4QUrl(
    QQuick3DRenderPass *self,
    const QUrl *newAugmentShader) {
  self->setAugmentShader(*newAugmentShader);
}

//  PassMode QQuick3DRenderPass::passMode() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPass::PassMode ritual_ZNK18QQuick3DRenderPass8passModeEv(
    const QQuick3DRenderPass *self) {
  return self->passMode();
}

//  void QQuick3DRenderPass::setPassMode(PassMode newPassMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass11setPassModeENS_8PassModeE(
    QQuick3DRenderPass *self,
    QQuick3DRenderPass::PassMode newPassMode) {
  self->setPassMode(newPassMode);
}

//  float QQuick3DRenderPass::depthClearValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK18QQuick3DRenderPass15depthClearValueEv(
    const QQuick3DRenderPass *self) {
  return self->depthClearValue();
}

//  void QQuick3DRenderPass::setDepthClearValue(float newDepthClearValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass18setDepthClearValueEf(
    QQuick3DRenderPass *self,
    float newDepthClearValue) {
  self->setDepthClearValue(newDepthClearValue);
}

//  quint32 QQuick3DRenderPass::stencilClearValue() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK18QQuick3DRenderPass17stencilClearValueEv(
    const QQuick3DRenderPass *self) {
  return self->stencilClearValue();
}

//  void QQuick3DRenderPass::setStencilClearValue(quint32
//      newStencilClearValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass20setStencilClearValueEj(
    QQuick3DRenderPass *self,
    quint32 newStencilClearValue) {
  self->setStencilClearValue(newStencilClearValue);
}

//  void QQuick3DRenderPass::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass12markAllDirtyEv(
    QQuick3DRenderPass *self) {
  self->markAllDirty();
}

//  RenderTargetFlags QQuick3DRenderPass::renderTargetFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuick3DRenderPass17renderTargetFlagsEv(
    const QQuick3DRenderPass *self) {
  return static_cast<int>(self->renderTargetFlags().toInt());
}

//  void QQuick3DRenderPass::setRenderTargetFlags(RenderTargetFlags
//      newRenderTargetFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass20setRenderTargetFlagsE6QFlagsINS_16RenderTargetFlagEE(
    QQuick3DRenderPass *self,
    int newRenderTargetFlags) {
  self->setRenderTargetFlags(
      QFlags<QQuick3DRenderPass::RenderTargetFlag>::fromInt(newRenderTargetFlags));
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderPass::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN18QQuick3DRenderPass17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderPass *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DRenderPass::itemChange(QQuick3DObject::ItemChange a0, const
//      QQuick3DObject::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DRenderPass *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void QQuick3DRenderPass::markTrackedPropertyDirty(QMetaProperty property,
//      QQuick3DPropertyChangedTracker::DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DRenderPass *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  self->markTrackedPropertyDirty(*property, hint);
}

//  void QQuick3DRenderPass::onMaterialDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass19onMaterialDestroyedEP7QObject(
    QQuick3DRenderPass *self,
    QObject *object) {
  self->onMaterialDestroyed(object);
}

//  void QQuick3DRenderPass::onCommandChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass16onCommandChangedEv(
    QQuick3DRenderPass *self) {
  self->onCommandChanged();
}

//  void QQuick3DRenderPass::updateSceneManager(QQuick3DSceneManager
//      *sceneManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass18updateSceneManagerEP20QQuick3DSceneManager(
    QQuick3DRenderPass *self,
    QQuick3DSceneManager *sceneManager) {
  self->updateSceneManager(sceneManager);
}

//  void QQuick3DRenderPass::markDirty(QQuick3DRenderPass::Dirty type, bool
//      requestSecondaryUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass9markDirtyENS_5DirtyEb(
    QQuick3DRenderPass *self,
    QQuick3DRenderPass::Dirty type,
    bool requestSecondaryUpdate) {
  self->markDirty(type, requestSecondaryUpdate);
}

//  void QQuick3DRenderPass::clearDirty(QQuick3DRenderPass::Dirty type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuick3DRenderPass10clearDirtyENS_5DirtyE(
    QQuick3DRenderPass *self,
    QQuick3DRenderPass::Dirty type) {
  self->clearDirty(type);
}

//  QQuick3DRenderPass as the QQuick3DPropertyChangedTracker it is built on
extern "C" Q_DECL_EXPORT
QQuick3DPropertyChangedTracker *ritual_cast_QQuick3DRenderPass_QQuick3DPropertyChangedTracker(
    QQuick3DRenderPass *self) {
  return static_cast<QQuick3DPropertyChangedTracker *>(self);
}

//  void QQuick3DRenderPass::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuick3DRenderPass12markAllDirtyEv(
    QQuick3DRenderPass *self) {
  self->QQuick3DRenderPass::markAllDirty();
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderPass::updateSpatialNode(QSSGRenderGraphObject *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN18QQuick3DRenderPass17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderPass *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DRenderPass *>(self)->OwnQQuick3DRenderPass::updateSpatialNode(
      node);
}

//  void QQuick3DRenderPass::itemChange(QQuick3DObject::ItemChange a0, const
//      QQuick3DObject::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuick3DRenderPass10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DRenderPass *self,
    QQuick3DObject::ItemChange a0,
    const QQuick3DObject::ItemChangeData *a1) {
  static_cast<OwnQQuick3DRenderPass *>(self)->OwnQQuick3DRenderPass::itemChange(
      a0,
      *a1);
}

//  void QQuick3DRenderPass::markTrackedPropertyDirty(QMetaProperty property,
//      QQuick3DPropertyChangedTracker::DirtyPropertyHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuick3DRenderPass24markTrackedPropertyDirtyE13QMetaPropertyN30QQuick3DPropertyChangedTracker17DirtyPropertyHintE(
    QQuick3DRenderPass *self,
    const QMetaProperty *property,
    QQuick3DPropertyChangedTracker::DirtyPropertyHint hint) {
  static_cast<OwnQQuick3DRenderPass *>(self)->OwnQQuick3DRenderPass::markTrackedPropertyDirty(
      *property,
      hint);
}
