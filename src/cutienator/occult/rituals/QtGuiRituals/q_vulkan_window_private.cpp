//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qvulkanwindow_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#if (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/QtGui>
#include <QtGui/qvulkanwindow.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qvulkanwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QVulkanWindowPrivate that Python can take functions over in. Every QVulkanWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQVulkanWindowPrivateCall0)(const void *, int *);
typedef const QPalette * (*CuteQVulkanWindowPrivateCall1)(const void *, int *);
typedef void (*CuteQVulkanWindowPrivateCall2)(const void *, bool, int *);
typedef void (*CuteQVulkanWindowPrivateCall3)(const void *, int *);
typedef void (*CuteQVulkanWindowPrivateCall4)(const void *, int, int, int *);
typedef const QRectF * (*CuteQVulkanWindowPrivateCall5)(const void *, const QRectF *, int *);
typedef bool (*CuteQVulkanWindowPrivateCall6)(const void *, int *);
typedef bool (*CuteQVulkanWindowPrivateCall7)(const void *, int *);
typedef void (*CuteQVulkanWindowPrivateCall8)(const void *, QMouseEvent *, int *);
class CuteQVulkanWindowPrivate : public QVulkanWindowPrivate {
public:
  using QVulkanWindowPrivate::QVulkanWindowPrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall0 call = reinterpret_cast<CuteQVulkanWindowPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall1 call = reinterpret_cast<CuteQVulkanWindowPrivateCall1>(taken[1]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall2 call = reinterpret_cast<CuteQVulkanWindowPrivateCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  void QWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[3]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall3 call = reinterpret_cast<CuteQVulkanWindowPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowPrivate::clearFocusObject();
  }

  //  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason
  //      a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall4 call = reinterpret_cast<CuteQVulkanWindowPrivateCall4>(taken[4]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall5 call = reinterpret_cast<CuteQVulkanWindowPrivateCall5>(taken[5]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall6 call = reinterpret_cast<CuteQVulkanWindowPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall7 call = reinterpret_cast<CuteQVulkanWindowPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }

  //  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQVulkanWindowPrivateCall8 call = reinterpret_cast<CuteQVulkanWindowPrivateCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }
};

//  QVulkanWindow *QVulkanWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QVulkanWindow *ritual_ZN20QVulkanWindowPrivate6q_funcEv(
    QVulkanWindowPrivate *self) {
  return self->q_func();
}

//  const QVulkanWindow *QVulkanWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QVulkanWindow *ritual_ZNK20QVulkanWindowPrivate6q_funcEv(
    const QVulkanWindowPrivate *self) {
  return self->q_func();
}

//  QVulkanWindowPrivate::~QVulkanWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivateD1Ev(QVulkanWindowPrivate *self) {
  delete self;
}

//  void QVulkanWindowPrivate::ensureStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate13ensureStartedEv(
    QVulkanWindowPrivate *self) {
  self->ensureStarted();
}

//  void QVulkanWindowPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate4initEv(QVulkanWindowPrivate *self) {
  self->init();
}

//  void QVulkanWindowPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate5resetEv(QVulkanWindowPrivate *self) {
  self->reset();
}

//  bool QVulkanWindowPrivate::createDefaultRenderPass()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QVulkanWindowPrivate23createDefaultRenderPassEv(
    QVulkanWindowPrivate *self) {
  return self->createDefaultRenderPass();
}

//  QSize QVulkanWindowPrivate::surfacePixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QVulkanWindowPrivate16surfacePixelSizeEv(
    const QVulkanWindowPrivate *self) {
  return new QSize(self->surfacePixelSize());
}

//  void QVulkanWindowPrivate::recreateSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate17recreateSwapChainEv(
    QVulkanWindowPrivate *self) {
  self->recreateSwapChain();
}

//  uint32_t QVulkanWindowPrivate::chooseTransientImageMemType(VkImage img,
//      uint32_t startIndex)
extern "C" Q_DECL_EXPORT
uint32_t ritual_ZN20QVulkanWindowPrivate27chooseTransientImageMemTypeEP9VkImage_Tj(
    QVulkanWindowPrivate *self,
    VkImage img,
    uint32_t startIndex) {
  return self->chooseTransientImageMemType(img, startIndex);
}

//  bool QVulkanWindowPrivate::createTransientImage(VkFormat format,
//      VkImageUsageFlags usage, VkImageAspectFlags aspectMask, VkImage
//      *images, VkDeviceMemory *mem, VkImageView *views, int count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QVulkanWindowPrivate20createTransientImageE8VkFormatjjPP9VkImage_TPP16VkDeviceMemory_TPP13VkImageView_Ti(
    QVulkanWindowPrivate *self,
    const VkFormat *format,
    VkImageUsageFlags usage,
    VkImageAspectFlags aspectMask,
    VkImage *images,
    VkDeviceMemory *mem,
    VkImageView *views,
    int count) {
  return self->createTransientImage(
      *format,
      usage,
      aspectMask,
      images,
      mem,
      views,
      count);
}

//  bool QVulkanWindowPrivate::createSwapChainResources()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QVulkanWindowPrivate24createSwapChainResourcesEv(
    QVulkanWindowPrivate *self) {
  return self->createSwapChainResources();
}

//  void QVulkanWindowPrivate::destroySwapChainResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate25destroySwapChainResourcesEv(
    QVulkanWindowPrivate *self) {
  self->destroySwapChainResources();
}

//  void QVulkanWindowPrivate::releaseSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate16releaseSwapChainEv(
    QVulkanWindowPrivate *self) {
  self->releaseSwapChain();
}

//  void QVulkanWindowPrivate::beginFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate10beginFrameEv(
    QVulkanWindowPrivate *self) {
  self->beginFrame();
}

//  void QVulkanWindowPrivate::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate8endFrameEv(QVulkanWindowPrivate *self) {
  self->endFrame();
}

//  bool QVulkanWindowPrivate::checkDeviceLost(VkResult err)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QVulkanWindowPrivate15checkDeviceLostE8VkResult(
    QVulkanWindowPrivate *self,
    const VkResult *err) {
  return self->checkDeviceLost(*err);
}

//  bool QVulkanWindowPrivate::addReadback()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QVulkanWindowPrivate11addReadbackEv(
    QVulkanWindowPrivate *self) {
  return self->addReadback();
}

//  void QVulkanWindowPrivate::releaseReadbackResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate24releaseReadbackResourcesEv(
    QVulkanWindowPrivate *self) {
  self->releaseReadbackResources();
}

//  void QVulkanWindowPrivate::finishBlockingReadback()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVulkanWindowPrivate22finishBlockingReadbackEv(
    QVulkanWindowPrivate *self) {
  self->finishBlockingReadback();
}

//  a Python function taken by a CuteQVulkanWindowPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVulkanWindowPrivate(
    QVulkanWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVulkanWindowPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
