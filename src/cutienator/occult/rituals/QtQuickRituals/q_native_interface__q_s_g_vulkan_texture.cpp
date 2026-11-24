//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>
#include <cstring>

//  A QNativeInterface::QSGVulkanTexture that Python can take functions over in. Every QNativeInterface::QSGVulkanTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef VkImage (*CuteQNativeInterface_QSGVulkanTextureCall0)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef VkImageLayout (*CuteQNativeInterface_QSGVulkanTextureCall1)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
class CuteQNativeInterface_QSGVulkanTexture : public QNativeInterface::QSGVulkanTexture {
public:
  using QNativeInterface::QSGVulkanTexture::QSGVulkanTexture;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGVulkanTexture11nativeImageEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK16QNativeInterface16QSGVulkanTexture17nativeImageLayoutEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const
  VkImage nativeImage() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeInterface_QSGVulkanTextureCall0 call = reinterpret_cast<CuteQNativeInterface_QSGVulkanTextureCall0>(taken[0]);
      VkImage given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  VkImageLayout QNativeInterface::QSGVulkanTexture::nativeImageLayout()
  //      const
  VkImageLayout nativeImageLayout() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeInterface_QSGVulkanTextureCall1 call = reinterpret_cast<CuteQNativeInterface_QSGVulkanTextureCall1>(taken[1]);
      VkImageLayout given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
};

//  QNativeInterface::QSGVulkanTexture::~QSGVulkanTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface16QSGVulkanTextureD1Ev(
    QNativeInterface::QSGVulkanTexture *self) {
  delete self;
}

//  VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const
extern "C" Q_DECL_EXPORT
VkImage ritual_ZNK16QNativeInterface16QSGVulkanTexture11nativeImageEv(
    const QNativeInterface::QSGVulkanTexture *self) {
  return self->nativeImage();
}

//  VkImageLayout QNativeInterface::QSGVulkanTexture::nativeImageLayout()
//      const
extern "C" Q_DECL_EXPORT
VkImageLayout ritual_ZNK16QNativeInterface16QSGVulkanTexture17nativeImageLayoutEv(
    const QNativeInterface::QSGVulkanTexture *self) {
  return self->nativeImageLayout();
}

//  a Python function taken by a CuteQNativeInterface_QSGVulkanTexture, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeInterface_QSGVulkanTexture(
    QNativeInterface::QSGVulkanTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeInterface_QSGVulkanTexture *>(self)->take(key, call);
}

#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
