//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-27: what names Vulkan's types stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as in every other ritual file
//  naming them, since Qt's 'qvulkaninstance.h' stands in for those types
//  with others of its own ('quint64' for 'VkImage') when Vulkan's headers
//  are missing, which no function of Qt's library takes. Kept as it is when
//  the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGTexturePlatformVulkan::QSGTexturePlatformVulkan(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformVulkan *ritual_ZN24QSGTexturePlatformVulkanC1EP10QSGTexture(
    QSGTexture *t) {
  return new QSGTexturePlatformVulkan(t);
}

//  VkImage QSGTexturePlatformVulkan::nativeImage() const
extern "C" Q_DECL_EXPORT
VkImage *ritual_ZNK24QSGTexturePlatformVulkan11nativeImageEv(
    const QSGTexturePlatformVulkan *self) {
  return new VkImage(self->nativeImage());
}

//  VkImageLayout QSGTexturePlatformVulkan::nativeImageLayout() const
extern "C" Q_DECL_EXPORT
VkImageLayout *ritual_ZNK24QSGTexturePlatformVulkan17nativeImageLayoutEv(
    const QSGTexturePlatformVulkan *self) {
  return new VkImageLayout(self->nativeImageLayout());
}

//  a VkImage a ritual of QSGTexturePlatformVulkan gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGTexturePlatformVulkan__VkImage(VkImage *self) {
  delete self;
}

//  a VkImageLayout a ritual of QSGTexturePlatformVulkan gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSGTexturePlatformVulkan__VkImageLayout(
    VkImageLayout *self) {
  delete self;
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
