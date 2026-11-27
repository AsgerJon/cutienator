//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickrendertarget.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  what names Vulkan's types stands under '__has_include(<vulkan/vulkan.h>)'
//  as well, as in every other ritual file naming them, since Qt's
//  'qvulkaninstance.h' stands in for those types with others of its own
//  ('quint64' for 'VkImage') when Vulkan's headers are missing, which no
//  function of Qt's library takes. Kept as it is when the generator runs
//  again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickrendertarget.h>
#include <QtCore/qsize.h>
#include <QtQuick/QQuickRenderTarget>
#include <QtCore/QSize>
#include <QtCore/QFlags>

//  QQuickRenderTarget::QQuickRenderTarget()
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTargetC1Ev() {
  return new QQuickRenderTarget();
}

//  QQuickRenderTarget::~QQuickRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRenderTargetD1Ev(QQuickRenderTarget *self) {
  delete self;
}

//  QQuickRenderTarget::QQuickRenderTarget(const QQuickRenderTarget &other)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTargetC1ERKS_(
    const QQuickRenderTarget *other) {
  return new QQuickRenderTarget(*other);
}

//  QQuickRenderTarget &QQuickRenderTarget::operator=(const
//      QQuickRenderTarget &other)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTargetaSERKS_(
    QQuickRenderTarget *self,
    const QQuickRenderTarget *other) {
  return &(self->operator=(*other));
}

//  bool QQuickRenderTarget::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickRenderTarget6isNullEv(
    const QQuickRenderTarget *self) {
  return self->isNull();
}

//  qreal QQuickRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickRenderTarget16devicePixelRatioEv(
    const QQuickRenderTarget *self) {
  return self->devicePixelRatio();
}

//  void QQuickRenderTarget::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRenderTarget19setDevicePixelRatioEd(
    QQuickRenderTarget *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  bool QQuickRenderTarget::mirrorVertically() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickRenderTarget16mirrorVerticallyEv(
    const QQuickRenderTarget *self) {
  return self->mirrorVertically();
}

//  void QQuickRenderTarget::setMirrorVertically(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRenderTarget19setMirrorVerticallyEb(
    QQuickRenderTarget *self,
    bool enable) {
  self->setMirrorVertically(enable);
}

//  QRhiTexture *QQuickRenderTarget::depthTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK18QQuickRenderTarget12depthTextureEv(
    const QQuickRenderTarget *self) {
  return self->depthTexture();
}

//  void QQuickRenderTarget::setDepthTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRenderTarget15setDepthTextureEP11QRhiTexture(
    QQuickRenderTarget *self,
    QRhiTexture *texture) {
  self->setDepthTexture(texture);
}

#if QT_CONFIG(opengl) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint textureId,
//      const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjRK5QSizei(
    uint textureId,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromOpenGLTexture(
          textureId,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)

#if QT_CONFIG(opengl) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint textureId,
//      uint format, const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjjRK5QSizei(
    uint textureId,
    uint format,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromOpenGLTexture(
          textureId,
          format,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)

#if QT_CONFIG(opengl) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromOpenGLTexture(uint textureId,
//      uint format, QSize pixelSize, int sampleCount, int arraySize, Flags
//      flags)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget17fromOpenGLTextureEjj5QSizeii6QFlagsINS_4FlagEE(
    uint textureId,
    uint format,
    const QSize *pixelSize,
    int sampleCount,
    int arraySize,
    int flags) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromOpenGLTexture(
          textureId,
          format,
          *pixelSize,
          sampleCount,
          arraySize,
          QFlags<QQuickRenderTarget::Flag>::fromInt(flags)));
}
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)

#if QT_CONFIG(opengl) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromOpenGLRenderBuffer(uint
//      renderbufferId, const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget22fromOpenGLRenderBufferEjRK5QSizei(
    uint renderbufferId,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromOpenGLRenderBuffer(
          renderbufferId,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)

#if QT_CONFIG(metal) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
//      *texture, const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget16fromMetalTextureEP10MTLTextureRK5QSizei(
    MTLTexture *texture,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromMetalTexture(
          texture,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)

#if QT_CONFIG(metal) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
//      *texture, uint format, const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget16fromMetalTextureEP10MTLTexturejRK5QSizei(
    MTLTexture *texture,
    uint format,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromMetalTexture(
          texture,
          format,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)

#if QT_CONFIG(metal) || defined(Q_QDOC)
//  QQuickRenderTarget QQuickRenderTarget::fromMetalTexture(MTLTexture
//      *texture, uint format, uint viewFormat, QSize pixelSize, int
//      sampleCount, int arraySize, Flags flags)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget16fromMetalTextureEP10MTLTexturejj5QSizeii6QFlagsINS_4FlagEE(
    MTLTexture *texture,
    uint format,
    uint viewFormat,
    const QSize *pixelSize,
    int sampleCount,
    int arraySize,
    int flags) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromMetalTexture(
          texture,
          format,
          viewFormat,
          *pixelSize,
          sampleCount,
          arraySize,
          QFlags<QQuickRenderTarget::Flag>::fromInt(flags)));
}
#endif  // QT_CONFIG(metal) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
//  QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage image,
//      VkImageLayout layout, const QSize &pixelSize, int sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget15fromVulkanImageEP9VkImage_T13VkImageLayoutRK5QSizei(
    VkImage image,
    const VkImageLayout *layout,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromVulkanImage(
          image,
          *layout,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
//  QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage image,
//      VkImageLayout layout, VkFormat format, const QSize &pixelSize, int
//      sampleCount)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget15fromVulkanImageEP9VkImage_T13VkImageLayout8VkFormatRK5QSizei(
    VkImage image,
    const VkImageLayout *layout,
    const VkFormat *format,
    const QSize *pixelSize,
    int sampleCount) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromVulkanImage(
          image,
          *layout,
          *format,
          *pixelSize,
          sampleCount));
}
#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)

#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
//  QQuickRenderTarget QQuickRenderTarget::fromVulkanImage(VkImage image,
//      VkImageLayout layout, VkFormat format, VkFormat viewFormat, QSize
//      pixelSize, int sampleCount, int arraySize, Flags flags)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget15fromVulkanImageEP9VkImage_T13VkImageLayout8VkFormatS3_5QSizeii6QFlagsINS_4FlagEE(
    VkImage image,
    const VkImageLayout *layout,
    const VkFormat *format,
    const VkFormat *viewFormat,
    const QSize *pixelSize,
    int sampleCount,
    int arraySize,
    int flags) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromVulkanImage(
          image,
          *layout,
          *format,
          *viewFormat,
          *pixelSize,
          sampleCount,
          arraySize,
          QFlags<QQuickRenderTarget::Flag>::fromInt(flags)));
}
#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)

//  QQuickRenderTarget
//      QQuickRenderTarget::fromRhiRenderTarget(QRhiRenderTarget
//      *renderTarget)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget19fromRhiRenderTargetEP16QRhiRenderTarget(
    QRhiRenderTarget *renderTarget) {
  return new QQuickRenderTarget(
      QQuickRenderTarget::fromRhiRenderTarget(
          renderTarget));
}

//  QQuickRenderTarget QQuickRenderTarget::fromPaintDevice(QPaintDevice
//      *device)
extern "C" Q_DECL_EXPORT
QQuickRenderTarget *ritual_ZN18QQuickRenderTarget15fromPaintDeviceEP12QPaintDevice(
    QPaintDevice *device) {
  return new QQuickRenderTarget(QQuickRenderTarget::fromPaintDevice(device));
}

//  void QQuickRenderTarget::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRenderTarget6detachEv(QQuickRenderTarget *self) {
  self->detach();
}

//  bool QQuickRenderTarget::isEqual(const QQuickRenderTarget &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickRenderTarget7isEqualERKS_(
    const QQuickRenderTarget *self,
    const QQuickRenderTarget *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QQuickRenderTarget &lhs, const QQuickRenderTarget
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QQuickRenderTargetS1_(
    const QQuickRenderTarget *lhs,
    const QQuickRenderTarget *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QQuickRenderTarget &lhs, const QQuickRenderTarget
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QQuickRenderTargetS1_(
    const QQuickRenderTarget *lhs,
    const QQuickRenderTarget *rhs) {
  return operator!=(*lhs, *rhs);
}
