//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiSwapChain that Python can take functions over in. Every QRhiSwapChain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiSwapChainCall0)(const void *, int *);
typedef void * (*CuteQRhiSwapChainCall1)(const void *, int *);
typedef void * (*CuteQRhiSwapChainCall2)(const void *, int *);
typedef void * (*CuteQRhiSwapChainCall3)(const void *, int, int *);
typedef const QSize * (*CuteQRhiSwapChainCall4)(const void *, int *);
typedef bool (*CuteQRhiSwapChainCall5)(const void *, int, int *);
typedef void * (*CuteQRhiSwapChainCall6)(const void *, int *);
typedef bool (*CuteQRhiSwapChainCall7)(const void *, int *);
typedef const QRhiSwapChainHdrInfo * (*CuteQRhiSwapChainCall8)(const void *, int *);
typedef void (*CuteQRhiSwapChainCall9)(const void *, int *);
class CuteQRhiSwapChain : public QRhiSwapChain {
public:
  using QRhiSwapChain::QRhiSwapChain;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
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
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain16surfacePixelSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain14createOrResizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain7hdrInfoEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiSwapChain::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiSwapChainCall0 call = reinterpret_cast<CuteQRhiSwapChainCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChain::resourceType();
  }

  //  QRhiCommandBuffer *QRhiSwapChain::currentFrameCommandBuffer()
  QRhiCommandBuffer *currentFrameCommandBuffer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiSwapChainCall1 call = reinterpret_cast<CuteQRhiSwapChainCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiCommandBuffer *>(given);
    }
    return {};
  }

  //  QRhiRenderTarget *QRhiSwapChain::currentFrameRenderTarget()
  QRhiRenderTarget *currentFrameRenderTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiSwapChainCall2 call = reinterpret_cast<CuteQRhiSwapChainCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return {};
  }

  //  QRhiRenderTarget
  //      *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
  //      targetBuffer)
  QRhiRenderTarget *currentFrameRenderTarget(
      QRhiSwapChain::StereoTargetBuffer targetBuffer) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiSwapChainCall3 call = reinterpret_cast<CuteQRhiSwapChainCall3>(taken[3]);
      void * given = call(this, static_cast<int>(targetBuffer), &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QRhiSwapChain::currentFrameRenderTarget(targetBuffer);
  }

  //  QSize QRhiSwapChain::surfacePixelSize()
  QSize surfacePixelSize() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiSwapChainCall4 call = reinterpret_cast<CuteQRhiSwapChainCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QRhiSwapChain::isFormatSupported(Format f)
  bool isFormatSupported(QRhiSwapChain::Format f) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiSwapChainCall5 call = reinterpret_cast<CuteQRhiSwapChainCall5>(taken[5]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhiRenderPassDescriptor
  //      *QRhiSwapChain::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiSwapChainCall6 call = reinterpret_cast<CuteQRhiSwapChainCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return {};
  }

  //  bool QRhiSwapChain::createOrResize()
  bool createOrResize() override {
    if (taken[7]) {
      int handled = 0;
      CuteQRhiSwapChainCall7 call = reinterpret_cast<CuteQRhiSwapChainCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
  QRhiSwapChainHdrInfo hdrInfo() override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiSwapChainCall8 call = reinterpret_cast<CuteQRhiSwapChainCall8>(taken[8]);
      const QRhiSwapChainHdrInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiSwapChain::hdrInfo();
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiSwapChainCall9 call = reinterpret_cast<CuteQRhiSwapChainCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiSwapChain::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK13QRhiSwapChain12resourceTypeEv(
    const QRhiSwapChain *self) {
  return self->resourceType();
}

//  QWindow *QRhiSwapChain::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK13QRhiSwapChain6windowEv(const QRhiSwapChain *self) {
  return self->window();
}

//  void QRhiSwapChain::setWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain9setWindowEP7QWindow(
    QRhiSwapChain *self,
    QWindow *window) {
  self->setWindow(window);
}

//  QRhiSwapChainProxyData QRhiSwapChain::proxyData() const
extern "C" Q_DECL_EXPORT
QRhiSwapChainProxyData *ritual_ZNK13QRhiSwapChain9proxyDataEv(
    const QRhiSwapChain *self) {
  return new QRhiSwapChainProxyData(self->proxyData());
}

//  void QRhiSwapChain::setProxyData(const QRhiSwapChainProxyData &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain12setProxyDataERK22QRhiSwapChainProxyData(
    QRhiSwapChain *self,
    const QRhiSwapChainProxyData *d) {
  self->setProxyData(*d);
}

//  Flags QRhiSwapChain::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRhiSwapChain5flagsEv(const QRhiSwapChain *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiSwapChain::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain8setFlagsE6QFlagsINS_4FlagEE(
    QRhiSwapChain *self,
    int f) {
  self->setFlags(QFlags<QRhiSwapChain::Flag>::fromInt(f));
}

//  Format QRhiSwapChain::format() const
extern "C" Q_DECL_EXPORT
QRhiSwapChain::Format ritual_ZNK13QRhiSwapChain6formatEv(
    const QRhiSwapChain *self) {
  return self->format();
}

//  void QRhiSwapChain::setFormat(Format f)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain9setFormatENS_6FormatE(
    QRhiSwapChain *self,
    QRhiSwapChain::Format f) {
  self->setFormat(f);
}

//  QRhiRenderBuffer *QRhiSwapChain::depthStencil() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK13QRhiSwapChain12depthStencilEv(
    const QRhiSwapChain *self) {
  return self->depthStencil();
}

//  void QRhiSwapChain::setDepthStencil(QRhiRenderBuffer *ds)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain15setDepthStencilEP16QRhiRenderBuffer(
    QRhiSwapChain *self,
    QRhiRenderBuffer *ds) {
  self->setDepthStencil(ds);
}

//  int QRhiSwapChain::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QRhiSwapChain11sampleCountEv(const QRhiSwapChain *self) {
  return self->sampleCount();
}

//  void QRhiSwapChain::setSampleCount(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain14setSampleCountEi(
    QRhiSwapChain *self,
    int samples) {
  self->setSampleCount(samples);
}

//  QRhiRenderPassDescriptor *QRhiSwapChain::renderPassDescriptor() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK13QRhiSwapChain20renderPassDescriptorEv(
    const QRhiSwapChain *self) {
  return self->renderPassDescriptor();
}

//  void QRhiSwapChain::setRenderPassDescriptor(QRhiRenderPassDescriptor
//      *desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain23setRenderPassDescriptorEP24QRhiRenderPassDescriptor(
    QRhiSwapChain *self,
    QRhiRenderPassDescriptor *desc) {
  self->setRenderPassDescriptor(desc);
}

//  QRhiShadingRateMap *QRhiSwapChain::shadingRateMap() const
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZNK13QRhiSwapChain14shadingRateMapEv(
    const QRhiSwapChain *self) {
  return self->shadingRateMap();
}

//  void QRhiSwapChain::setShadingRateMap(QRhiShadingRateMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QRhiSwapChain17setShadingRateMapEP18QRhiShadingRateMap(
    QRhiSwapChain *self,
    QRhiShadingRateMap *map) {
  self->setShadingRateMap(map);
}

//  QSize QRhiSwapChain::currentPixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QRhiSwapChain16currentPixelSizeEv(
    const QRhiSwapChain *self) {
  return new QSize(self->currentPixelSize());
}

//  QRhiCommandBuffer *QRhiSwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN13QRhiSwapChain25currentFrameCommandBufferEv(
    QRhiSwapChain *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QRhiSwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN13QRhiSwapChain24currentFrameRenderTargetEv(
    QRhiSwapChain *self) {
  return self->currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE(
    QRhiSwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->currentFrameRenderTarget(targetBuffer);
}

//  QSize QRhiSwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN13QRhiSwapChain16surfacePixelSizeEv(QRhiSwapChain *self) {
  return new QSize(self->surfacePixelSize());
}

//  bool QRhiSwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE(
    QRhiSwapChain *self,
    QRhiSwapChain::Format f) {
  return self->isFormatSupported(f);
}

//  QRhiRenderPassDescriptor
//      *QRhiSwapChain::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv(
    QRhiSwapChain *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QRhiSwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QRhiSwapChain14createOrResizeEv(QRhiSwapChain *self) {
  return self->createOrResize();
}

//  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_ZN13QRhiSwapChain7hdrInfoEv(
    QRhiSwapChain *self) {
  return new QRhiSwapChainHdrInfo(self->hdrInfo());
}

//  QRhiSwapChain::QRhiSwapChain(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN13QRhiSwapChainC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQRhiSwapChain(rhi);
}

//  a Python function taken by a CuteQRhiSwapChain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiSwapChain(
    QRhiSwapChain *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiSwapChain *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiSwapChain::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK13QRhiSwapChain12resourceTypeEv(
    const QRhiSwapChain *self) {
  return self->QRhiSwapChain::resourceType();
}

//  QRhiRenderTarget
//      *QRhiSwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE(
    QRhiSwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->QRhiSwapChain::currentFrameRenderTarget(targetBuffer);
}

//  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_own_ZN13QRhiSwapChain7hdrInfoEv(
    QRhiSwapChain *self) {
  return new QRhiSwapChainHdrInfo(self->QRhiSwapChain::hdrInfo());
}
