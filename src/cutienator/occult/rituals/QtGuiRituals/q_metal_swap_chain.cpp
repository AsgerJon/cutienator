//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QMetalSwapChain that Python can take functions over in. Every QMetalSwapChain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalSwapChainCall0)(const void *, int *);
typedef void * (*CuteQMetalSwapChainCall1)(const void *, int *);
typedef void * (*CuteQMetalSwapChainCall2)(const void *, int *);
typedef const QSize * (*CuteQMetalSwapChainCall3)(const void *, int *);
typedef bool (*CuteQMetalSwapChainCall4)(const void *, int, int *);
typedef void * (*CuteQMetalSwapChainCall5)(const void *, int *);
typedef bool (*CuteQMetalSwapChainCall6)(const void *, int *);
typedef const QRhiSwapChainHdrInfo * (*CuteQMetalSwapChainCall7)(const void *, int *);
typedef int (*CuteQMetalSwapChainCall8)(const void *, int *);
typedef void * (*CuteQMetalSwapChainCall9)(const void *, int, int *);
class CuteQMetalSwapChain : public QMetalSwapChain {
public:
  using QMetalSwapChain::QMetalSwapChain;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain25currentFrameCommandBufferEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain16surfacePixelSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain14createOrResizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain7hdrInfoEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QMetalSwapChain::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalSwapChainCall0 call = reinterpret_cast<CuteQMetalSwapChainCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalSwapChain::destroy();
  }

  //  QRhiCommandBuffer *QMetalSwapChain::currentFrameCommandBuffer()
  QRhiCommandBuffer *currentFrameCommandBuffer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalSwapChainCall1 call = reinterpret_cast<CuteQMetalSwapChainCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiCommandBuffer *>(given);
    }
    return QMetalSwapChain::currentFrameCommandBuffer();
  }

  //  QRhiRenderTarget *QMetalSwapChain::currentFrameRenderTarget()
  QRhiRenderTarget *currentFrameRenderTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalSwapChainCall2 call = reinterpret_cast<CuteQMetalSwapChainCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QMetalSwapChain::currentFrameRenderTarget();
  }

  //  QSize QMetalSwapChain::surfacePixelSize()
  QSize surfacePixelSize() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalSwapChainCall3 call = reinterpret_cast<CuteQMetalSwapChainCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalSwapChain::surfacePixelSize();
  }

  //  bool QMetalSwapChain::isFormatSupported(Format f)
  bool isFormatSupported(QRhiSwapChain::Format f) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalSwapChainCall4 call = reinterpret_cast<CuteQMetalSwapChainCall4>(taken[4]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return QMetalSwapChain::isFormatSupported(f);
  }

  //  QRhiRenderPassDescriptor
  //      *QMetalSwapChain::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[5]) {
      int handled = 0;
      CuteQMetalSwapChainCall5 call = reinterpret_cast<CuteQMetalSwapChainCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QMetalSwapChain::newCompatibleRenderPassDescriptor();
  }

  //  bool QMetalSwapChain::createOrResize()
  bool createOrResize() override {
    if (taken[6]) {
      int handled = 0;
      CuteQMetalSwapChainCall6 call = reinterpret_cast<CuteQMetalSwapChainCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalSwapChain::createOrResize();
  }

  //  QRhiSwapChainHdrInfo QMetalSwapChain::hdrInfo()
  QRhiSwapChainHdrInfo hdrInfo() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMetalSwapChainCall7 call = reinterpret_cast<CuteQMetalSwapChainCall7>(taken[7]);
      const QRhiSwapChainHdrInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalSwapChain::hdrInfo();
  }

  //  QRhiResource::Type QRhiSwapChain::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQMetalSwapChainCall8 call = reinterpret_cast<CuteQMetalSwapChainCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChain::resourceType();
  }

  //  QRhiRenderTarget
  //      *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
  //      targetBuffer)
  QRhiRenderTarget *currentFrameRenderTarget(
      QRhiSwapChain::StereoTargetBuffer targetBuffer) override {
    if (taken[9]) {
      int handled = 0;
      CuteQMetalSwapChainCall9 call = reinterpret_cast<CuteQMetalSwapChainCall9>(taken[9]);
      void * given = call(this, static_cast<int>(targetBuffer), &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QRhiSwapChain::currentFrameRenderTarget(targetBuffer);
  }
};

//  QRhiSwapChainHdrInfo QMetalSwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_ZN15QMetalSwapChain7hdrInfoEv(
    QMetalSwapChain *self) {
  return new QRhiSwapChainHdrInfo(self->hdrInfo());
}

//  a Python function taken by a CuteQMetalSwapChain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalSwapChain(
    QMetalSwapChain *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalSwapChain *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
