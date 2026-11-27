//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  what names Vulkan's types stands under '__has_include(<vulkan/vulkan.h>)'
//  as well, as in every other ritual file naming them, since Qt's
//  'qvulkaninstance.h' stands in for those types with others of its own
//  ('quint64' for 'VkImage') when Vulkan's headers are missing, which no
//  function of Qt's library takes. Kept as it is when the generator runs
//  again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>
#include <QtCore/qsize.h>
#include <QtCore/QSize>
#include <QtCore/QFlags>
#include <QtQuick/QQuickWindow>

//  QNativeInterface::QSGVulkanTexture::~QSGVulkanTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface16QSGVulkanTextureD1Ev(
    QNativeInterface::QSGVulkanTexture *self) {
  delete self;
}

//  VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const
extern "C" Q_DECL_EXPORT
VkImage *ritual_ZNK16QNativeInterface16QSGVulkanTexture11nativeImageEv(
    const QNativeInterface::QSGVulkanTexture *self) {
  return new VkImage(self->nativeImage());
}

//  VkImageLayout QNativeInterface::QSGVulkanTexture::nativeImageLayout()
//      const
extern "C" Q_DECL_EXPORT
VkImageLayout *ritual_ZNK16QNativeInterface16QSGVulkanTexture17nativeImageLayoutEv(
    const QNativeInterface::QSGVulkanTexture *self) {
  return new VkImageLayout(self->nativeImageLayout());
}

//  QSGTexture *QNativeInterface::QSGVulkanTexture::fromNative(VkImage image,
//      VkImageLayout layout, QQuickWindow *window, const QSize &size,
//      QQuickWindow::CreateTextureOptions options)
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZN16QNativeInterface16QSGVulkanTexture10fromNativeEP9VkImage_T13VkImageLayoutP12QQuickWindowRK5QSize6QFlagsINS4_19CreateTextureOptionEE(
    VkImage image,
    const VkImageLayout *layout,
    QQuickWindow *window,
    const QSize *size,
    int options) {
  return QNativeInterface::QSGVulkanTexture::fromNative(
      image,
      *layout,
      window,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options));
}

//  a VkImage a ritual of QNativeInterface::QSGVulkanTexture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNativeInterface_QSGVulkanTexture__VkImage(VkImage *self) {
  delete self;
}

//  a VkImageLayout a ritual of QNativeInterface::QSGVulkanTexture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNativeInterface_QSGVulkanTexture__VkImageLayout(
    VkImageLayout *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
