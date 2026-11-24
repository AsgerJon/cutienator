//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiShaderResourceBinding::QRhiShaderResourceBinding()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBindingC1Ev() {
  return new QRhiShaderResourceBinding();
}

//  bool QRhiShaderResourceBinding::isLayoutCompatible(const
//      QRhiShaderResourceBinding &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QRhiShaderResourceBinding18isLayoutCompatibleERKS_(
    const QRhiShaderResourceBinding *self,
    const QRhiShaderResourceBinding *other) {
  return self->isLayoutCompatible(*other);
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::uniformBuffer(int
//      binding, StageFlags stage, QRhiBuffer *buf)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding13uniformBufferEi6QFlagsINS_9StageFlagEEP10QRhiBuffer(
    int binding,
    int stage,
    QRhiBuffer *buf) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::uniformBuffer(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::uniformBuffer(int
//      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset, quint32
//      size)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding13uniformBufferEi6QFlagsINS_9StageFlagEEP10QRhiBufferjj(
    int binding,
    int stage,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::uniformBuffer(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf,
          offset,
          size));
}

//  QRhiShaderResourceBinding
//      QRhiShaderResourceBinding::uniformBufferWithDynamicOffset(int
//      binding, StageFlags stage, QRhiBuffer *buf, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding30uniformBufferWithDynamicOffsetEi6QFlagsINS_9StageFlagEEP10QRhiBufferj(
    int binding,
    int stage,
    QRhiBuffer *buf,
    quint32 size) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::uniformBufferWithDynamicOffset(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf,
          size));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::sampledTexture(int
//      binding, StageFlags stage, QRhiTexture *tex, QRhiSampler *sampler)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding14sampledTextureEi6QFlagsINS_9StageFlagEEP11QRhiTextureP11QRhiSampler(
    int binding,
    int stage,
    QRhiTexture *tex,
    QRhiSampler *sampler) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::sampledTexture(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          tex,
          sampler));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::sampledTextures(int
//      binding, StageFlags stage, int count, const TextureAndSampler
//      *texSamplers)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding15sampledTexturesEi6QFlagsINS_9StageFlagEEiPKNS_17TextureAndSamplerE(
    int binding,
    int stage,
    int count,
    const QRhiShaderResourceBinding::TextureAndSampler *texSamplers) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::sampledTextures(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          count,
          texSamplers));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::texture(int binding,
//      StageFlags stage, QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding7textureEi6QFlagsINS_9StageFlagEEP11QRhiTexture(
    int binding,
    int stage,
    QRhiTexture *tex) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::texture(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          tex));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::sampler(int binding,
//      StageFlags stage, QRhiSampler *sampler)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding7samplerEi6QFlagsINS_9StageFlagEEP11QRhiSampler(
    int binding,
    int stage,
    QRhiSampler *sampler) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::sampler(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          sampler));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::imageLoad(int
//      binding, StageFlags stage, QRhiTexture *tex, int level)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding9imageLoadEi6QFlagsINS_9StageFlagEEP11QRhiTexturei(
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::imageLoad(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          tex,
          level));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::imageStore(int
//      binding, StageFlags stage, QRhiTexture *tex, int level)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding10imageStoreEi6QFlagsINS_9StageFlagEEP11QRhiTexturei(
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::imageStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          tex,
          level));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::imageLoadStore(int
//      binding, StageFlags stage, QRhiTexture *tex, int level)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding14imageLoadStoreEi6QFlagsINS_9StageFlagEEP11QRhiTexturei(
    int binding,
    int stage,
    QRhiTexture *tex,
    int level) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::imageLoadStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          tex,
          level));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoad(int
//      binding, StageFlags stage, QRhiBuffer *buf)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding10bufferLoadEi6QFlagsINS_9StageFlagEEP10QRhiBuffer(
    int binding,
    int stage,
    QRhiBuffer *buf) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferLoad(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoad(int
//      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset, quint32
//      size)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding10bufferLoadEi6QFlagsINS_9StageFlagEEP10QRhiBufferjj(
    int binding,
    int stage,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferLoad(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf,
          offset,
          size));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferStore(int
//      binding, StageFlags stage, QRhiBuffer *buf)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding11bufferStoreEi6QFlagsINS_9StageFlagEEP10QRhiBuffer(
    int binding,
    int stage,
    QRhiBuffer *buf) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferStore(int
//      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset, quint32
//      size)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding11bufferStoreEi6QFlagsINS_9StageFlagEEP10QRhiBufferjj(
    int binding,
    int stage,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf,
          offset,
          size));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoadStore(int
//      binding, StageFlags stage, QRhiBuffer *buf)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding15bufferLoadStoreEi6QFlagsINS_9StageFlagEEP10QRhiBuffer(
    int binding,
    int stage,
    QRhiBuffer *buf) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferLoadStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf));
}

//  QRhiShaderResourceBinding QRhiShaderResourceBinding::bufferLoadStore(int
//      binding, StageFlags stage, QRhiBuffer *buf, quint32 offset, quint32
//      size)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBinding *ritual_ZN25QRhiShaderResourceBinding15bufferLoadStoreEi6QFlagsINS_9StageFlagEEP10QRhiBufferjj(
    int binding,
    int stage,
    QRhiBuffer *buf,
    quint32 offset,
    quint32 size) {
  return new QRhiShaderResourceBinding(
      QRhiShaderResourceBinding::bufferLoadStore(
          binding,
          QFlags<QRhiShaderResourceBinding::StageFlag>::fromInt(stage),
          buf,
          offset,
          size));
}

//  QRhiShaderResourceBinding::~QRhiShaderResourceBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRhiShaderResourceBindingD1Ev(
    QRhiShaderResourceBinding *self) {
  delete self;
}
