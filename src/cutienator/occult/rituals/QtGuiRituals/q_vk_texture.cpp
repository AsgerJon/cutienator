//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 7482, as _ZN10QVkTextureD1Ev
inline QVkTexture::~QVkTexture()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7487, as _ZN10QVkTexture7destroyEv
inline void QVkTexture::destroy()
{
    if (!image)
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::Texture;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.texture.image = owns ? image : VK_NULL_HANDLE;
    e.texture.imageView = imageView;
    e.texture.allocation = owns ? imageAlloc : nullptr;

    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        e.texture.stagingBuffers[i] = stagingBuffers[i];
        e.texture.stagingAllocations[i] = stagingAllocations[i];

        stagingBuffers[i] = VK_NULL_HANDLE;
        stagingAllocations[i] = nullptr;
    }

    for (int i = 0; i < QRhi::MAX_MIP_LEVELS; ++i) {
        e.texture.extraImageViews[i] = perLevelImageViews[i];
        perLevelImageViews[i] = VK_NULL_HANDLE;
    }

    image = VK_NULL_HANDLE;
    imageView = VK_NULL_HANDLE;
    imageAlloc = nullptr;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7760, as _ZN10QVkTexture10createFromEN11QRhiTexture13NativeTextureE
inline bool QVkTexture::createFrom(QRhiTexture::NativeTexture src)
{
    VkImage img = VkImage(src.object);
    if (img == 0)
        return false;

    if (!prepareCreate())
        return false;

    image = img;

    if (!finishCreate())
        return false;

    usageState.layout = VkImageLayout(src.layout);

    owns = false;
    QRHI_RES_RHI(QRhiVulkan);
    rhiD->registerResource(this);
    return true;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7782, as _ZN10QVkTexture13nativeTextureEv
inline QRhiTexture::NativeTexture QVkTexture::nativeTexture()
{
    return {quint64(image), usageState.layout};
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7787, as _ZN10QVkTexture15setNativeLayoutEi
inline void QVkTexture::setNativeLayout(int layout)
{
    usageState.layout = VkImageLayout(layout);
}
//  -----------------------------------------------------------------------

//  A QVkTexture that Python can take functions over in. Every QVkTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkTextureCall0)(const void *, int *);
typedef bool (*CuteQVkTextureCall1)(const void *, int *);
typedef bool (*CuteQVkTextureCall2)(const void *, const QRhiTexture::NativeTexture *, int *);
typedef const QRhiTexture::NativeTexture * (*CuteQVkTextureCall3)(const void *, int *);
typedef void (*CuteQVkTextureCall4)(const void *, int, int *);
typedef int (*CuteQVkTextureCall5)(const void *, int *);
class CuteQVkTexture : public QVkTexture {
public:
  using QVkTexture::QVkTexture;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture10createFromENS_13NativeTextureE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture13nativeTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiTexture15setNativeLayoutEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void QVkTexture::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkTextureCall0 call = reinterpret_cast<CuteQVkTextureCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkTexture::destroy();
  }

  //  bool QVkTexture::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkTextureCall1 call = reinterpret_cast<CuteQVkTextureCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkTexture::create();
  }

  //  bool QVkTexture::createFrom(NativeTexture src)
  bool createFrom(QRhiTexture::NativeTexture src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkTextureCall2 call = reinterpret_cast<CuteQVkTextureCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QVkTexture::createFrom(src);
  }

  //  NativeTexture QVkTexture::nativeTexture()
  QRhiTexture::NativeTexture nativeTexture() override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkTextureCall3 call = reinterpret_cast<CuteQVkTextureCall3>(taken[3]);
      const QRhiTexture::NativeTexture * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkTexture::nativeTexture();
  }

  //  void QVkTexture::setNativeLayout(int layout)
  void setNativeLayout(int layout) override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkTextureCall4 call = reinterpret_cast<CuteQVkTextureCall4>(taken[4]);
      call(this, layout, &handled);
      if (handled) return;
    }
    QVkTexture::setNativeLayout(layout);
  }

  //  QRhiResource::Type QRhiTexture::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVkTextureCall5 call = reinterpret_cast<CuteQVkTextureCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTexture::resourceType();
  }
};

//  QVkTexture::~QVkTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVkTextureD1Ev(QVkTexture *self) {
  delete self;
}

//  void QVkTexture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVkTexture7destroyEv(QVkTexture *self) {
  self->destroy();
}

//  bool QVkTexture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QVkTexture10createFromEN11QRhiTexture13NativeTextureE(
    QVkTexture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->createFrom(*src);
}

//  NativeTexture QVkTexture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_ZN10QVkTexture13nativeTextureEv(
    QVkTexture *self) {
  return new QRhiTexture::NativeTexture(self->nativeTexture());
}

//  void QVkTexture::setNativeLayout(int layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVkTexture15setNativeLayoutEi(QVkTexture *self, int layout) {
  self->setNativeLayout(layout);
}

//  a Python function taken by a CuteQVkTexture, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkTexture(QVkTexture *self, const char *key, void *call) {
  return static_cast<CuteQVkTexture *>(self)->take(key, call);
}

//  void QVkTexture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QVkTexture7destroyEv(QVkTexture *self) {
  self->QVkTexture::destroy();
}

//  NativeTexture QVkTexture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_own_ZN10QVkTexture13nativeTextureEv(
    QVkTexture *self) {
  return new QRhiTexture::NativeTexture(self->QVkTexture::nativeTexture());
}

//  void QVkTexture::setNativeLayout(int layout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QVkTexture15setNativeLayoutEi(
    QVkTexture *self,
    int layout) {
  self->QVkTexture::setNativeLayout(layout);
}

#endif  // QT_CONFIG(vulkan)
