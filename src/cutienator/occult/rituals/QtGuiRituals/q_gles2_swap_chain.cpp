//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhigles2_p.h"
#include <QOffscreenSurface>
#include <QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <qpa/qplatformopenglcontext.h>
#include <qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 7195, as _ZN19QGles2CommandBufferC1EP18QRhiImplementation
inline QGles2CommandBuffer::QGles2CommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7201, as _ZN19QGles2CommandBufferD1Ev
inline QGles2CommandBuffer::~QGles2CommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7326, as _ZN25QGles2SwapChainTimestamps7prepareEP9QRhiGles2
inline void QGles2SwapChainTimestamps::prepare(QRhiGles2 *rhiD)
{
    if (!query[0])
        rhiD->f->glGenQueries(TIMESTAMP_PAIRS * 2, query);
}

//  from src/gui/rhi/qrhigles2.cpp, line 6462, as _ZN26QGles2RenderPassDescriptorC1EP18QRhiImplementation
inline QGles2RenderPassDescriptor::QGles2RenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6498, as _ZN27QGles2SwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QGles2SwapChainRenderTarget::QGles2SwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6504, as _ZN27QGles2SwapChainRenderTargetD1Ev
inline QGles2SwapChainRenderTarget::~QGles2SwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7206, as _ZN19QGles2CommandBuffer7destroyEv
inline void QGles2CommandBuffer::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhigles2.cpp, line 6509, as _ZN27QGles2SwapChainRenderTarget7destroyEv
inline void QGles2SwapChainRenderTarget::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhigles2.cpp, line 6524, as _ZNK27QGles2SwapChainRenderTarget11sampleCountEv
inline int QGles2SwapChainRenderTarget::sampleCount() const
{
    return d.sampleCount;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6519, as _ZNK27QGles2SwapChainRenderTarget16devicePixelRatioEv
inline float QGles2SwapChainRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6514, as _ZNK27QGles2SwapChainRenderTarget9pixelSizeEv
inline QSize QGles2SwapChainRenderTarget::pixelSize() const
{
    return d.pixelSize;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7220, as _ZN15QGles2SwapChainD1Ev
inline QGles2SwapChain::~QGles2SwapChain()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7225, as _ZN15QGles2SwapChain7destroyEv
inline void QGles2SwapChain::destroy()
{
    QRHI_RES_RHI(QRhiGles2);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhigles2.cpp, line 7232, as _ZN15QGles2SwapChain25currentFrameCommandBufferEv
inline QRhiCommandBuffer *QGles2SwapChain::currentFrameCommandBuffer()
{
    return &cb;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7237, as _ZN15QGles2SwapChain24currentFrameRenderTargetEv
inline QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget()
{
    return &rt;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7242, as _ZN15QGles2SwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE
inline QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer targetBuffer)
{
    if (targetBuffer == LeftBuffer)
        return rtLeft.d.isValid() ? &rtLeft : &rt;
    else if (targetBuffer == RightBuffer)
        return rtRight.d.isValid() ? &rtRight : &rt;
    else
        Q_UNREACHABLE_RETURN(nullptr);
}

//  from src/gui/rhi/qrhigles2.cpp, line 7252, as _ZN15QGles2SwapChain16surfacePixelSizeEv
inline QSize QGles2SwapChain::surfacePixelSize()
{
    Q_ASSERT(m_window);
    if (QPlatformWindow *platformWindow = m_window->handle())
        // Prefer using QPlatformWindow geometry and DPR in order to avoid
        // errors due to rounded QWindow geometry.
        return platformWindow->geometry().size() * platformWindow->devicePixelRatio();
    else
        return m_window->size() * m_window->devicePixelRatio();
}

//  from src/gui/rhi/qrhigles2.cpp, line 7263, as _ZN15QGles2SwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE
inline bool QGles2SwapChain::isFormatSupported(Format f)
{
    return f == SDR;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7268, as _ZN15QGles2SwapChain33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QGles2SwapChain::newCompatibleRenderPassDescriptor()
{
    QGles2RenderPassDescriptor *rpD = new QGles2RenderPassDescriptor(m_rhi);
    QRHI_RES_RHI(QRhiGles2);
    rhiD->registerResource(rpD, false);
    return rpD;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7288, as _ZN15QGles2SwapChain14createOrResizeEv
inline bool QGles2SwapChain::createOrResize()
{
    // can be called multiple times due to window resizes
    if (surface && surface != m_window)
        destroy();

    surface = m_window;
    m_currentPixelSize = surfacePixelSize();
    pixelSize = m_currentPixelSize;

    if (m_depthStencil && m_depthStencil->flags().testFlag(QRhiRenderBuffer::UsedWithSwapChainOnly)
            && m_depthStencil->pixelSize() != pixelSize)
    {
        m_depthStencil->setPixelSize(pixelSize);
        m_depthStencil->create();
    }

    initSwapChainRenderTarget(&rt);

    if (m_window->format().stereo()) {
        initSwapChainRenderTarget(&rtLeft);
        rtLeft.d.stereoTarget = QRhiSwapChain::LeftBuffer;
        initSwapChainRenderTarget(&rtRight);
        rtRight.d.stereoTarget = QRhiSwapChain::RightBuffer;
    }

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD->rhiFlags.testFlag(QRhi::EnableTimestamps) && rhiD->caps.timestamps)
        timestamps.prepare(rhiD);

    // The only reason to register this fairly fake gl swapchain
    // object with no native resources underneath is to be able to
    // implement a safe destroy().
    rhiD->registerResource(this, false);

    return true;
}

//  from src/gui/rhi/qrhigles2.cpp, line 7276, as _ZN15QGles2SwapChain25initSwapChainRenderTargetEP27QGles2SwapChainRenderTarget
inline void QGles2SwapChain::initSwapChainRenderTarget(QGles2SwapChainRenderTarget *rt)
{
    rt->setRenderPassDescriptor(m_renderPassDesc); // for the public getter in QRhiRenderTarget
    rt->d.rp = QRHI_RES(QGles2RenderPassDescriptor, m_renderPassDesc);
    rt->d.pixelSize = pixelSize;
    rt->d.dpr = float(m_window->devicePixelRatio());
    rt->d.sampleCount = qBound(1, m_sampleCount, 64);
    rt->d.colorAttCount = 1;
    rt->d.dsAttCount = m_depthStencil ? 1 : 0;
    rt->d.srgbUpdateAndBlend = m_flags.testFlag(QRhiSwapChain::sRGB);
}
//  -----------------------------------------------------------------------

//  A QGles2SwapChain that Python can take functions over in. Every QGles2SwapChain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2SwapChainCall0)(const void *, int *);
typedef void * (*CuteQGles2SwapChainCall1)(const void *, int *);
typedef void * (*CuteQGles2SwapChainCall2)(const void *, int *);
typedef void * (*CuteQGles2SwapChainCall3)(const void *, int, int *);
typedef const QSize * (*CuteQGles2SwapChainCall4)(const void *, int *);
typedef bool (*CuteQGles2SwapChainCall5)(const void *, int, int *);
typedef void * (*CuteQGles2SwapChainCall6)(const void *, int *);
typedef bool (*CuteQGles2SwapChainCall7)(const void *, int *);
typedef int (*CuteQGles2SwapChainCall8)(const void *, int *);
typedef const QRhiSwapChainHdrInfo * (*CuteQGles2SwapChainCall9)(const void *, int *);
class CuteQGles2SwapChain : public QGles2SwapChain {
public:
  using QGles2SwapChain::QGles2SwapChain;
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
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain7hdrInfoEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QGles2SwapChain::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2SwapChainCall0 call = reinterpret_cast<CuteQGles2SwapChainCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2SwapChain::destroy();
  }

  //  QRhiCommandBuffer *QGles2SwapChain::currentFrameCommandBuffer()
  QRhiCommandBuffer *currentFrameCommandBuffer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2SwapChainCall1 call = reinterpret_cast<CuteQGles2SwapChainCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiCommandBuffer *>(given);
    }
    return QGles2SwapChain::currentFrameCommandBuffer();
  }

  //  QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget()
  QRhiRenderTarget *currentFrameRenderTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2SwapChainCall2 call = reinterpret_cast<CuteQGles2SwapChainCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QGles2SwapChain::currentFrameRenderTarget();
  }

  //  QRhiRenderTarget
  //      *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer
  //      targetBuffer)
  QRhiRenderTarget *currentFrameRenderTarget(
      QRhiSwapChain::StereoTargetBuffer targetBuffer) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2SwapChainCall3 call = reinterpret_cast<CuteQGles2SwapChainCall3>(taken[3]);
      void * given = call(this, static_cast<int>(targetBuffer), &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QGles2SwapChain::currentFrameRenderTarget(targetBuffer);
  }

  //  QSize QGles2SwapChain::surfacePixelSize()
  QSize surfacePixelSize() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2SwapChainCall4 call = reinterpret_cast<CuteQGles2SwapChainCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGles2SwapChain::surfacePixelSize();
  }

  //  bool QGles2SwapChain::isFormatSupported(Format f)
  bool isFormatSupported(QRhiSwapChain::Format f) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGles2SwapChainCall5 call = reinterpret_cast<CuteQGles2SwapChainCall5>(taken[5]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return QGles2SwapChain::isFormatSupported(f);
  }

  //  QRhiRenderPassDescriptor
  //      *QGles2SwapChain::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[6]) {
      int handled = 0;
      CuteQGles2SwapChainCall6 call = reinterpret_cast<CuteQGles2SwapChainCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QGles2SwapChain::newCompatibleRenderPassDescriptor();
  }

  //  bool QGles2SwapChain::createOrResize()
  bool createOrResize() override {
    if (taken[7]) {
      int handled = 0;
      CuteQGles2SwapChainCall7 call = reinterpret_cast<CuteQGles2SwapChainCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2SwapChain::createOrResize();
  }

  //  QRhiResource::Type QRhiSwapChain::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGles2SwapChainCall8 call = reinterpret_cast<CuteQGles2SwapChainCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChain::resourceType();
  }

  //  QRhiSwapChainHdrInfo QRhiSwapChain::hdrInfo()
  QRhiSwapChainHdrInfo hdrInfo() override {
    if (taken[9]) {
      int handled = 0;
      CuteQGles2SwapChainCall9 call = reinterpret_cast<CuteQGles2SwapChainCall9>(taken[9]);
      const QRhiSwapChainHdrInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiSwapChain::hdrInfo();
  }
};

//  QGles2SwapChain::~QGles2SwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGles2SwapChainD1Ev(QGles2SwapChain *self) {
  delete self;
}

//  void QGles2SwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGles2SwapChain7destroyEv(QGles2SwapChain *self) {
  self->destroy();
}

//  QRhiCommandBuffer *QGles2SwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN15QGles2SwapChain25currentFrameCommandBufferEv(
    QGles2SwapChain *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN15QGles2SwapChain24currentFrameRenderTargetEv(
    QGles2SwapChain *self) {
  return self->currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN15QGles2SwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE(
    QGles2SwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->currentFrameRenderTarget(targetBuffer);
}

//  QSize QGles2SwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN15QGles2SwapChain16surfacePixelSizeEv(
    QGles2SwapChain *self) {
  return new QSize(self->surfacePixelSize());
}

//  bool QGles2SwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGles2SwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE(
    QGles2SwapChain *self,
    QRhiSwapChain::Format f) {
  return self->isFormatSupported(f);
}

//  QRhiRenderPassDescriptor
//      *QGles2SwapChain::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN15QGles2SwapChain33newCompatibleRenderPassDescriptorEv(
    QGles2SwapChain *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QGles2SwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QGles2SwapChain14createOrResizeEv(QGles2SwapChain *self) {
  return self->createOrResize();
}

//  void
//      QGles2SwapChain::initSwapChainRenderTarget(QGles2SwapChainRenderTarge
//      t *rt)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGles2SwapChain25initSwapChainRenderTargetEP27QGles2SwapChainRenderTarget(
    QGles2SwapChain *self,
    QGles2SwapChainRenderTarget *rt) {
  self->initSwapChainRenderTarget(rt);
}

//  a Python function taken by a CuteQGles2SwapChain, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2SwapChain(
    QGles2SwapChain *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2SwapChain *>(self)->take(key, call);
}

//  void QGles2SwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGles2SwapChain7destroyEv(QGles2SwapChain *self) {
  self->QGles2SwapChain::destroy();
}

//  QRhiCommandBuffer *QGles2SwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_own_ZN15QGles2SwapChain25currentFrameCommandBufferEv(
    QGles2SwapChain *self) {
  return self->QGles2SwapChain::currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QGles2SwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN15QGles2SwapChain24currentFrameRenderTargetEv(
    QGles2SwapChain *self) {
  return self->QGles2SwapChain::currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QGles2SwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN15QGles2SwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE(
    QGles2SwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->QGles2SwapChain::currentFrameRenderTarget(targetBuffer);
}

//  QSize QGles2SwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZN15QGles2SwapChain16surfacePixelSizeEv(
    QGles2SwapChain *self) {
  return new QSize(self->QGles2SwapChain::surfacePixelSize());
}

//  bool QGles2SwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGles2SwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE(
    QGles2SwapChain *self,
    QRhiSwapChain::Format f) {
  return self->QGles2SwapChain::isFormatSupported(f);
}

//  bool QGles2SwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QGles2SwapChain14createOrResizeEv(
    QGles2SwapChain *self) {
  return self->QGles2SwapChain::createOrResize();
}
