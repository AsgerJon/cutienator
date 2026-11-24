//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGTexturePlatformVulkan that Python can take functions over in. Every QSGTexturePlatformVulkan
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
typedef VkImage (*CuteQSGTexturePlatformVulkanCall0)(const void *, int *);
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
typedef VkImageLayout (*CuteQSGTexturePlatformVulkanCall1)(const void *, int *);
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
class CuteQSGTexturePlatformVulkan : public QSGTexturePlatformVulkan {
public:
  using QSGTexturePlatformVulkan::QSGTexturePlatformVulkan;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGVulkanTexture11nativeImageEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGVulkanTexture17nativeImageLayoutEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
  //  VkImage QSGTexturePlatformVulkan::nativeImage() const
  VkImage nativeImage() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTexturePlatformVulkanCall0 call = reinterpret_cast<CuteQSGTexturePlatformVulkanCall0>(taken[0]);
      VkImage given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexturePlatformVulkan::nativeImage();
  }
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan)
  //  VkImageLayout QSGTexturePlatformVulkan::nativeImageLayout() const
  VkImageLayout nativeImageLayout() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTexturePlatformVulkanCall1 call = reinterpret_cast<CuteQSGTexturePlatformVulkanCall1>(taken[1]);
      VkImageLayout given = call(this, &handled);
      if (handled) return given;
    }
    return QSGTexturePlatformVulkan::nativeImageLayout();
  }
#endif  // QT_CONFIG(vulkan)
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
};

//  QSGTexturePlatformVulkan::QSGTexturePlatformVulkan(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformVulkan *ritual_ZN24QSGTexturePlatformVulkanC1EP10QSGTexture(
    QSGTexture *t) {
  return new CuteQSGTexturePlatformVulkan(t);
}

//  VkImage QSGTexturePlatformVulkan::nativeImage() const
extern "C" Q_DECL_EXPORT
VkImage ritual_ZNK24QSGTexturePlatformVulkan11nativeImageEv(
    const QSGTexturePlatformVulkan *self) {
  return self->nativeImage();
}

//  VkImageLayout QSGTexturePlatformVulkan::nativeImageLayout() const
extern "C" Q_DECL_EXPORT
VkImageLayout ritual_ZNK24QSGTexturePlatformVulkan17nativeImageLayoutEv(
    const QSGTexturePlatformVulkan *self) {
  return self->nativeImageLayout();
}

//  a Python function taken by a CuteQSGTexturePlatformVulkan, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTexturePlatformVulkan(
    QSGTexturePlatformVulkan *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTexturePlatformVulkan *>(self)->take(key, call);
}

//  VkImage QSGTexturePlatformVulkan::nativeImage() const
extern "C" Q_DECL_EXPORT
VkImage ritual_own_ZNK24QSGTexturePlatformVulkan11nativeImageEv(
    const QSGTexturePlatformVulkan *self) {
  return self->QSGTexturePlatformVulkan::nativeImage();
}

//  VkImageLayout QSGTexturePlatformVulkan::nativeImageLayout() const
extern "C" Q_DECL_EXPORT
VkImageLayout ritual_own_ZNK24QSGTexturePlatformVulkan17nativeImageLayoutEv(
    const QSGTexturePlatformVulkan *self) {
  return self->QSGTexturePlatformVulkan::nativeImageLayout();
}

#endif  // QT_CONFIG(vulkan)
