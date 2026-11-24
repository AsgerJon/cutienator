//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 1027, as _ZN18QNullCommandBufferC1EP18QRhiImplementation
inline QNullCommandBuffer::QNullCommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 1032, as _ZN18QNullCommandBufferD1Ev
inline QNullCommandBuffer::~QNullCommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 811, as _ZN25QNullRenderPassDescriptorC1EP18QRhiImplementation
inline QNullRenderPassDescriptor::QNullRenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 847, as _ZN26QNullSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 853, as _ZN26QNullSwapChainRenderTargetD1Ev
inline QNullSwapChainRenderTarget::~QNullSwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 1037, as _ZN18QNullCommandBuffer7destroyEv
inline void QNullCommandBuffer::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhinull.cpp, line 858, as _ZN26QNullSwapChainRenderTarget7destroyEv
inline void QNullSwapChainRenderTarget::destroy()
{
}

//  from src/gui/rhi/qrhinull.cpp, line 872, as _ZNK26QNullSwapChainRenderTarget11sampleCountEv
inline int QNullSwapChainRenderTarget::sampleCount() const
{
    return 1;
}

//  from src/gui/rhi/qrhinull.cpp, line 867, as _ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv
inline float QNullSwapChainRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhinull.cpp, line 862, as _ZNK26QNullSwapChainRenderTarget9pixelSizeEv
inline QSize QNullSwapChainRenderTarget::pixelSize() const
{
    return d.pixelSize;
}

//  from src/gui/rhi/qrhinull.cpp, line 1049, as _ZN14QNullSwapChainD1Ev
inline QNullSwapChain::~QNullSwapChain()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 1054, as _ZN14QNullSwapChain7destroyEv
inline void QNullSwapChain::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 1061, as _ZN14QNullSwapChain25currentFrameCommandBufferEv
inline QRhiCommandBuffer *QNullSwapChain::currentFrameCommandBuffer()
{
    return &cb;
}

//  from src/gui/rhi/qrhinull.cpp, line 1066, as _ZN14QNullSwapChain24currentFrameRenderTargetEv
inline QRhiRenderTarget *QNullSwapChain::currentFrameRenderTarget()
{
    return &rt;
}

//  from src/gui/rhi/qrhinull.cpp, line 1071, as _ZN14QNullSwapChain16surfacePixelSizeEv
inline QSize QNullSwapChain::surfacePixelSize()
{
    return QSize(1280, 720);
}

//  from src/gui/rhi/qrhinull.cpp, line 1076, as _ZN14QNullSwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE
inline bool QNullSwapChain::isFormatSupported(Format f)
{
    return f == SDR;
}

//  from src/gui/rhi/qrhinull.cpp, line 1081, as _ZN14QNullSwapChain33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QNullSwapChain::newCompatibleRenderPassDescriptor()
{
    QNullRenderPassDescriptor *rpD = new QNullRenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from src/gui/rhi/qrhinull.cpp, line 1089, as _ZN14QNullSwapChain14createOrResizeEv
inline bool QNullSwapChain::createOrResize()
{
    const bool needsRegistration = !window || window != m_window;
    if (window && window != m_window)
        destroy();

    window = m_window;
    m_currentPixelSize = surfacePixelSize();
    rt.setRenderPassDescriptor(m_renderPassDesc); // for the public getter in QRhiRenderTarget
    rt.d.rp = QRHI_RES(QNullRenderPassDescriptor, m_renderPassDesc);
    rt.d.pixelSize = m_currentPixelSize;
    frameCount = 0;

    if (needsRegistration) {
        QRHI_RES_RHI(QRhiNull);
        rhiD->registerResource(this);
    }

    return true;
}
//  -----------------------------------------------------------------------

//  A QNullSwapChain that Python can take functions over in. Every QNullSwapChain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullSwapChainCall0)(const void *, int *);
typedef void * (*CuteQNullSwapChainCall1)(const void *, int *);
typedef void * (*CuteQNullSwapChainCall2)(const void *, int *);
typedef const QSize * (*CuteQNullSwapChainCall3)(const void *, int *);
typedef bool (*CuteQNullSwapChainCall4)(const void *, int, int *);
typedef void * (*CuteQNullSwapChainCall5)(const void *, int *);
typedef bool (*CuteQNullSwapChainCall6)(const void *, int *);
typedef int (*CuteQNullSwapChainCall7)(const void *, int *);
typedef void * (*CuteQNullSwapChainCall8)(const void *, int, int *);
typedef const QRhiSwapChainHdrInfo * (*CuteQNullSwapChainCall9)(const void *, int *);
class CuteQNullSwapChain : public QNullSwapChain {
public:
  using QNullSwapChain::QNullSwapChain;
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
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain7hdrInfoEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QNullSwapChain::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullSwapChainCall0 call = reinterpret_cast<CuteQNullSwapChainCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullSwapChain::destroy();
  }

  //  QRhiCommandBuffer *QNullSwapChain::currentFrameCommandBuffer()
  QRhiCommandBuffer *currentFrameCommandBuffer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullSwapChainCall1 call = reinterpret_cast<CuteQNullSwapChainCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiCommandBuffer *>(given);
    }
    return QNullSwapChain::currentFrameCommandBuffer();
  }

  //  QRhiRenderTarget *QNullSwapChain::currentFrameRenderTarget()
  QRhiRenderTarget *currentFrameRenderTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullSwapChainCall2 call = reinterpret_cast<CuteQNullSwapChainCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QNullSwapChain::currentFrameRenderTarget();
  }

  //  QSize QNullSwapChain::surfacePixelSize()
  QSize surfacePixelSize() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullSwapChainCall3 call = reinterpret_cast<CuteQNullSwapChainCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNullSwapChain::surfacePixelSize();
  }

  //  bool QNullSwapChain::isFormatSupported(Format f)
  bool isFormatSupported(QRhiSwapChain::Format f) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullSwapChainCall4 call = reinterpret_cast<CuteQNullSwapChainCall4>(taken[4]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return QNullSwapChain::isFormatSupported(f);
  }

  //  QRhiRenderPassDescriptor
  //      *QNullSwapChain::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNullSwapChainCall5 call = reinterpret_cast<CuteQNullSwapChainCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QNullSwapChain::newCompatibleRenderPassDescriptor();
  }

  //  bool QNullSwapChain::createOrResize()
  bool createOrResize() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNullSwapChainCall6 call = reinterpret_cast<CuteQNullSwapChainCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullSwapChain::createOrResize();
  }

  //  QRhiResource::Type QRhiSwapChain::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQNullSwapChainCall7 call = reinterpret_cast<CuteQNullSwapChainCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQNullSwapChainCall8 call = reinterpret_cast<CuteQNullSwapChainCall8>(taken[8]);
      void * given = call(this, static_cast<int>(targetBuffer), &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QRhiSwapChain::currentFrameRenderTarget(targetBuffer);
  }

  //  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
  QRhiSwapChainHdrInfo hdrInfo() override {
    if (taken[9]) {
      int handled = 0;
      CuteQNullSwapChainCall9 call = reinterpret_cast<CuteQNullSwapChainCall9>(taken[9]);
      const QRhiSwapChainHdrInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiSwapChain::hdrInfo();
  }
};

//  QNullSwapChain::~QNullSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNullSwapChainD1Ev(QNullSwapChain *self) {
  delete self;
}

//  void QNullSwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QNullSwapChain7destroyEv(QNullSwapChain *self) {
  self->destroy();
}

//  QRhiCommandBuffer *QNullSwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN14QNullSwapChain25currentFrameCommandBufferEv(
    QNullSwapChain *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QNullSwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN14QNullSwapChain24currentFrameRenderTargetEv(
    QNullSwapChain *self) {
  return self->currentFrameRenderTarget();
}

//  QSize QNullSwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN14QNullSwapChain16surfacePixelSizeEv(QNullSwapChain *self) {
  return new QSize(self->surfacePixelSize());
}

//  bool QNullSwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QNullSwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE(
    QNullSwapChain *self,
    QRhiSwapChain::Format f) {
  return self->isFormatSupported(f);
}

//  QRhiRenderPassDescriptor
//      *QNullSwapChain::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN14QNullSwapChain33newCompatibleRenderPassDescriptorEv(
    QNullSwapChain *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QNullSwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QNullSwapChain14createOrResizeEv(QNullSwapChain *self) {
  return self->createOrResize();
}

//  a Python function taken by a CuteQNullSwapChain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullSwapChain(
    QNullSwapChain *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullSwapChain *>(self)->take(key, call);
}

//  void QNullSwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QNullSwapChain7destroyEv(QNullSwapChain *self) {
  self->QNullSwapChain::destroy();
}

//  QRhiCommandBuffer *QNullSwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_own_ZN14QNullSwapChain25currentFrameCommandBufferEv(
    QNullSwapChain *self) {
  return self->QNullSwapChain::currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QNullSwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN14QNullSwapChain24currentFrameRenderTargetEv(
    QNullSwapChain *self) {
  return self->QNullSwapChain::currentFrameRenderTarget();
}

//  QSize QNullSwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN14QNullSwapChain16surfacePixelSizeEv(
    QNullSwapChain *self) {
  return new QSize(self->QNullSwapChain::surfacePixelSize());
}

//  bool QNullSwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QNullSwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE(
    QNullSwapChain *self,
    QRhiSwapChain::Format f) {
  return self->QNullSwapChain::isFormatSupported(f);
}

//  bool QNullSwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QNullSwapChain14createOrResizeEv(QNullSwapChain *self) {
  return self->QNullSwapChain::createOrResize();
}
