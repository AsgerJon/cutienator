//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvulkanwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(vulkan)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#include <QtGui/QtGui>
#include <QtGui/qvulkanwindow.h>
#include <cstring>

//  A QVulkanWindowRenderer that Python can take functions over in. Every QVulkanWindowRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall0)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall1)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall2)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall3)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall4)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall5)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall6)(const void *, int *);
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
typedef void (*CuteQVulkanWindowRendererCall7)(const void *, int *);
#endif
class CuteQVulkanWindowRenderer : public QVulkanWindowRenderer {
public:
  using QVulkanWindowRenderer::QVulkanWindowRenderer;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer16preInitResourcesEv")) {
      taken[0] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer13initResourcesEv")) {
      taken[1] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv")) {
      taken[2] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesEv")) {
      taken[3] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer16releaseResourcesEv")) {
      taken[4] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer14startNextFrameEv")) {
      taken[5] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer18physicalDeviceLostEv")) {
      taken[6] = call;
      return true;
    }
#endif
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN21QVulkanWindowRenderer17logicalDeviceLostEv")) {
      taken[7] = call;
      return true;
    }
#endif
    return false;
  }

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::preInitResources()
  void preInitResources() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall0 call = reinterpret_cast<CuteQVulkanWindowRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::preInitResources();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::initResources()
  void initResources() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall1 call = reinterpret_cast<CuteQVulkanWindowRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::initResources();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::initSwapChainResources()
  void initSwapChainResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall2 call = reinterpret_cast<CuteQVulkanWindowRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::initSwapChainResources();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::releaseSwapChainResources()
  void releaseSwapChainResources() override {
    if (taken[3]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall3 call = reinterpret_cast<CuteQVulkanWindowRendererCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::releaseSwapChainResources();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::releaseResources()
  void releaseResources() override {
    if (taken[4]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall4 call = reinterpret_cast<CuteQVulkanWindowRendererCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::releaseResources();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::startNextFrame()
  void startNextFrame() override {
    if (taken[5]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall5 call = reinterpret_cast<CuteQVulkanWindowRendererCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::physicalDeviceLost()
  void physicalDeviceLost() override {
    if (taken[6]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall6 call = reinterpret_cast<CuteQVulkanWindowRendererCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::physicalDeviceLost();
  }
#endif

#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || \
    defined(Q_QDOC)
  //  void QVulkanWindowRenderer::logicalDeviceLost()
  void logicalDeviceLost() override {
    if (taken[7]) {
      int handled = 0;
      CuteQVulkanWindowRendererCall7 call = reinterpret_cast<CuteQVulkanWindowRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QVulkanWindowRenderer::logicalDeviceLost();
  }
#endif
};

//  QVulkanWindowRenderer::~QVulkanWindowRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRendererD1Ev(QVulkanWindowRenderer *self) {
  delete self;
}

//  void QVulkanWindowRenderer::preInitResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer16preInitResourcesEv(
    QVulkanWindowRenderer *self) {
  self->preInitResources();
}

//  void QVulkanWindowRenderer::initResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer13initResourcesEv(
    QVulkanWindowRenderer *self) {
  self->initResources();
}

//  void QVulkanWindowRenderer::initSwapChainResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv(
    QVulkanWindowRenderer *self) {
  self->initSwapChainResources();
}

//  void QVulkanWindowRenderer::releaseSwapChainResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesEv(
    QVulkanWindowRenderer *self) {
  self->releaseSwapChainResources();
}

//  void QVulkanWindowRenderer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer16releaseResourcesEv(
    QVulkanWindowRenderer *self) {
  self->releaseResources();
}

//  void QVulkanWindowRenderer::startNextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer14startNextFrameEv(
    QVulkanWindowRenderer *self) {
  self->startNextFrame();
}

//  void QVulkanWindowRenderer::physicalDeviceLost()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer18physicalDeviceLostEv(
    QVulkanWindowRenderer *self) {
  self->physicalDeviceLost();
}

//  void QVulkanWindowRenderer::logicalDeviceLost()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QVulkanWindowRenderer17logicalDeviceLostEv(
    QVulkanWindowRenderer *self) {
  self->logicalDeviceLost();
}

//  a Python function taken by a CuteQVulkanWindowRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVulkanWindowRenderer(
    QVulkanWindowRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVulkanWindowRenderer *>(self)->take(key, call);
}

//  void QVulkanWindowRenderer::preInitResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer16preInitResourcesEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::preInitResources();
}

//  void QVulkanWindowRenderer::initResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer13initResourcesEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::initResources();
}

//  void QVulkanWindowRenderer::initSwapChainResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::initSwapChainResources();
}

//  void QVulkanWindowRenderer::releaseSwapChainResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::releaseSwapChainResources();
}

//  void QVulkanWindowRenderer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer16releaseResourcesEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::releaseResources();
}

//  void QVulkanWindowRenderer::physicalDeviceLost()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer18physicalDeviceLostEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::physicalDeviceLost();
}

//  void QVulkanWindowRenderer::logicalDeviceLost()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QVulkanWindowRenderer17logicalDeviceLostEv(
    QVulkanWindowRenderer *self) {
  self->QVulkanWindowRenderer::logicalDeviceLost();
}

#endif  // (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
