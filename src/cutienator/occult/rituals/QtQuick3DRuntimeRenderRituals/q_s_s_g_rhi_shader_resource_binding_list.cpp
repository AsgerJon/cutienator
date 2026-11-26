//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGRhiShaderResourceBindingList::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList5clearEv(
    QSSGRhiShaderResourceBindingList *self) {
  self->clear();
}

//  QSSGRhiShaderResourceBindingList::QSSGRhiShaderResourceBindingList()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderResourceBindingList *ritual_ZN32QSSGRhiShaderResourceBindingListC1Ev() {
  return new QSSGRhiShaderResourceBindingList();
}

//  QSSGRhiShaderResourceBindingList::QSSGRhiShaderResourceBindingList(const
//      QSSGRhiShaderResourceBindingList &other)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderResourceBindingList *ritual_ZN32QSSGRhiShaderResourceBindingListC1ERKS_(
    const QSSGRhiShaderResourceBindingList *other) {
  return new QSSGRhiShaderResourceBindingList(*other);
}

//  QSSGRhiShaderResourceBindingList
//      &QSSGRhiShaderResourceBindingList::operator=(const
//      QSSGRhiShaderResourceBindingList &other)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderResourceBindingList *ritual_ZN32QSSGRhiShaderResourceBindingListaSERKS_(
    QSSGRhiShaderResourceBindingList *self,
    const QSSGRhiShaderResourceBindingList *other) {
  return &(self->operator=(*other));
}

//  void QSSGRhiShaderResourceBindingList::addUniformBuffer(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf, int
//      offset, int size, bool hasDynamicOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList16addUniformBufferEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP10QRhiBufferiib(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiBuffer *buf,
    int offset,
    int size,
    bool hasDynamicOffset) {
  self->addUniformBuffer(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      buf,
      offset,
      size,
      hasDynamicOffset);
}

//  void QSSGRhiShaderResourceBindingList::addTexture(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex,
//      QRhiSampler *sampler)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList10addTextureEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTextureP11QRhiSampler(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiTexture *tex,
    QRhiSampler *sampler) {
  self->addTexture(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      tex,
      sampler);
}

//  void QSSGRhiShaderResourceBindingList::addImageLoad(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList12addImageLoadEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  self->addImageLoad(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      tex,
      level);
}

//  void QSSGRhiShaderResourceBindingList::addImageStore(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList13addImageStoreEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  self->addImageStore(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      tex,
      level);
}

//  void QSSGRhiShaderResourceBindingList::addImageLoadStore(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiTexture *tex, int
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList17addImageLoadStoreEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP11QRhiTexturei(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  self->addImageLoadStore(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      tex,
      level);
}

//  void QSSGRhiShaderResourceBindingList::addStorageBuffer(int binding,
//      QRhiShaderResourceBinding::StageFlags stage, QRhiBuffer *buf, int
//      offset, int size, bool hasDynamicOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingList16addStorageBufferEi6QFlagsIN25QRhiShaderResourceBinding9StageFlagEEP10QRhiBufferiib(
    QSSGRhiShaderResourceBindingList *self,
    int binding,
    int stage,
    QRhiBuffer *buf,
    int offset,
    int size,
    bool hasDynamicOffset) {
  self->addStorageBuffer(
      binding,
      QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
      buf,
      offset,
      size,
      hasDynamicOffset);
}

//  QSSGRhiShaderResourceBindingList::~QSSGRhiShaderResourceBindingList()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGRhiShaderResourceBindingListD1Ev(
    QSSGRhiShaderResourceBindingList *self) {
  delete self;
}
