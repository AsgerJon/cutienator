//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/qquick3drenderoutputprovider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qquick3drenderoutputprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuick3DRenderOutputProvider may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DRenderOutputProvider : QQuick3DRenderOutputProvider {
  using QQuick3DRenderOutputProvider::updateSpatialNode;
  using QQuick3DRenderOutputProvider::markAllDirty;
};

//  const QMetaObject *QQuick3DRenderOutputProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DRenderOutputProvider10metaObjectEv(
    const QQuick3DRenderOutputProvider *self) {
  return self->metaObject();
}

//  QString QQuick3DRenderOutputProvider::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DRenderOutputProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRenderOutputProvider::tr(s, c, n));
}

//  QQuick3DRenderOutputProvider::QQuick3DRenderOutputProvider(QQuick3DObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRenderOutputProvider *ritual_ZN28QQuick3DRenderOutputProviderC1EP14QQuick3DObject(
    QQuick3DObject *parent) {
  return new QQuick3DRenderOutputProvider(parent);
}

//  TextureSource QQuick3DRenderOutputProvider::textureSource() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderOutputProvider::TextureSource ritual_ZNK28QQuick3DRenderOutputProvider13textureSourceEv(
    const QQuick3DRenderOutputProvider *self) {
  return self->textureSource();
}

//  void QQuick3DRenderOutputProvider::setTextureSource(TextureSource
//      newTextureSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DRenderOutputProvider16setTextureSourceENS_13TextureSourceE(
    QQuick3DRenderOutputProvider *self,
    QQuick3DRenderOutputProvider::TextureSource newTextureSource) {
  self->setTextureSource(newTextureSource);
}

//  QQuick3DRenderPass *QQuick3DRenderOutputProvider::renderPass() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderPass *ritual_ZNK28QQuick3DRenderOutputProvider10renderPassEv(
    const QQuick3DRenderOutputProvider *self) {
  return self->renderPass();
}

//  void QQuick3DRenderOutputProvider::setRenderPass(QQuick3DRenderPass
//      *newRenderPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DRenderOutputProvider13setRenderPassEP18QQuick3DRenderPass(
    QQuick3DRenderOutputProvider *self,
    QQuick3DRenderPass *newRenderPass) {
  self->setRenderPass(newRenderPass);
}

//  AttachmentSelector QQuick3DRenderOutputProvider::attachmentSelector()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DRenderOutputProvider::AttachmentSelector ritual_ZNK28QQuick3DRenderOutputProvider18attachmentSelectorEv(
    const QQuick3DRenderOutputProvider *self) {
  return self->attachmentSelector();
}

//  void
//      QQuick3DRenderOutputProvider::setAttachmentSelector(AttachmentSelecto
//      r newAttachmentSelector)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DRenderOutputProvider21setAttachmentSelectorENS_18AttachmentSelectorE(
    QQuick3DRenderOutputProvider *self,
    QQuick3DRenderOutputProvider::AttachmentSelector newAttachmentSelector) {
  self->setAttachmentSelector(newAttachmentSelector);
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderOutputProvider::updateSpatialNode(QSSGRenderGraphObjec
//      t *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZN28QQuick3DRenderOutputProvider17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderOutputProvider *self,
    QSSGRenderGraphObject *node) {
  return self->updateSpatialNode(node);
}

//  void QQuick3DRenderOutputProvider::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DRenderOutputProvider12markAllDirtyEv(
    QQuick3DRenderOutputProvider *self) {
  self->markAllDirty();
}

//  void QQuick3DRenderOutputProvider::markDirty(DirtyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DRenderOutputProvider9markDirtyENS_9DirtyTypeE(
    QQuick3DRenderOutputProvider *self,
    QQuick3DRenderOutputProvider::DirtyType type) {
  self->markDirty(type);
}

//  QSSGRenderGraphObject
//      *QQuick3DRenderOutputProvider::updateSpatialNode(QSSGRenderGraphObjec
//      t *node)
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_own_ZN28QQuick3DRenderOutputProvider17updateSpatialNodeEP21QSSGRenderGraphObject(
    QQuick3DRenderOutputProvider *self,
    QSSGRenderGraphObject *node) {
  return static_cast<OwnQQuick3DRenderOutputProvider *>(self)->OwnQQuick3DRenderOutputProvider::updateSpatialNode(
      node);
}

//  void QQuick3DRenderOutputProvider::markAllDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DRenderOutputProvider12markAllDirtyEv(
    QQuick3DRenderOutputProvider *self) {
  static_cast<OwnQQuick3DRenderOutputProvider *>(self)->OwnQQuick3DRenderOutputProvider::markAllDirty();
}
