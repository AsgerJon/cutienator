//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalimagenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  QSGDefaultInternalImageNode::QSGDefaultInternalImageNode(QSGDefaultRender
//      Context *rc)
extern "C" Q_DECL_EXPORT
QSGDefaultInternalImageNode *ritual_ZN27QSGDefaultInternalImageNodeC1EP23QSGDefaultRenderContext(
    QSGDefaultRenderContext *rc) {
  return new QSGDefaultInternalImageNode(rc);
}

//  void
//      QSGDefaultInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setMipmapFiltering(filtering);
}

//  void QSGDefaultInternalImageNode::setFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void
//      QSGDefaultInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMo
//      de wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setHorizontalWrapMode(wrapMode);
}

//  void
//      QSGDefaultInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
//      wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setVerticalWrapMode(wrapMode);
}

//  void QSGDefaultInternalImageNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode26updateMaterialAntialiasingEv(
    QSGDefaultInternalImageNode *self) {
  self->updateMaterialAntialiasing();
}

//  void QSGDefaultInternalImageNode::setMaterialTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGDefaultInternalImageNode18setMaterialTextureEP10QSGTexture(
    QSGDefaultInternalImageNode *self,
    QSGTexture *texture) {
  self->setMaterialTexture(texture);
}

//  QSGTexture *QSGDefaultInternalImageNode::materialTexture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK27QSGDefaultInternalImageNode15materialTextureEv(
    const QSGDefaultInternalImageNode *self) {
  return self->materialTexture();
}

//  bool QSGDefaultInternalImageNode::updateMaterialBlending()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QSGDefaultInternalImageNode22updateMaterialBlendingEv(
    QSGDefaultInternalImageNode *self) {
  return self->updateMaterialBlending();
}

//  bool QSGDefaultInternalImageNode::supportsWrap(const QSize &size) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSGDefaultInternalImageNode12supportsWrapERK5QSize(
    const QSGDefaultInternalImageNode *self,
    const QSize *size) {
  return self->supportsWrap(*size);
}

//  void
//      QSGDefaultInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGDefaultInternalImageNode::setMipmapFiltering(filtering);
}

//  void QSGDefaultInternalImageNode::setFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGDefaultInternalImageNode::setFiltering(filtering);
}

//  void
//      QSGDefaultInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMo
//      de wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->QSGDefaultInternalImageNode::setHorizontalWrapMode(wrapMode);
}

//  void
//      QSGDefaultInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
//      wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGDefaultInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->QSGDefaultInternalImageNode::setVerticalWrapMode(wrapMode);
}

//  void QSGDefaultInternalImageNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode26updateMaterialAntialiasingEv(
    QSGDefaultInternalImageNode *self) {
  self->QSGDefaultInternalImageNode::updateMaterialAntialiasing();
}

//  void QSGDefaultInternalImageNode::setMaterialTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGDefaultInternalImageNode18setMaterialTextureEP10QSGTexture(
    QSGDefaultInternalImageNode *self,
    QSGTexture *texture) {
  self->QSGDefaultInternalImageNode::setMaterialTexture(texture);
}

//  QSGTexture *QSGDefaultInternalImageNode::materialTexture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK27QSGDefaultInternalImageNode15materialTextureEv(
    const QSGDefaultInternalImageNode *self) {
  return self->QSGDefaultInternalImageNode::materialTexture();
}

//  bool QSGDefaultInternalImageNode::updateMaterialBlending()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN27QSGDefaultInternalImageNode22updateMaterialBlendingEv(
    QSGDefaultInternalImageNode *self) {
  return self->QSGDefaultInternalImageNode::updateMaterialBlending();
}

//  bool QSGDefaultInternalImageNode::supportsWrap(const QSize &size) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSGDefaultInternalImageNode12supportsWrapERK5QSize(
    const QSGDefaultInternalImageNode *self,
    const QSize *size) {
  return self->QSGDefaultInternalImageNode::supportsWrap(*size);
}
