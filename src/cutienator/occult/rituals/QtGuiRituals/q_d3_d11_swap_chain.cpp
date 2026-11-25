//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, 'releaseBuffers' and 'newColorBuffer',
//  which Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11SwapChain::~QD3D11SwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QD3D11SwapChainD1Ev(QD3D11SwapChain *self) {
  delete self;
}

//  void QD3D11SwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QD3D11SwapChain7destroyEv(QD3D11SwapChain *self) {
  self->destroy();
}

//  QRhiCommandBuffer *QD3D11SwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN15QD3D11SwapChain25currentFrameCommandBufferEv(
    QD3D11SwapChain *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QD3D11SwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN15QD3D11SwapChain24currentFrameRenderTargetEv(
    QD3D11SwapChain *self) {
  return self->currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QD3D11SwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN15QD3D11SwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE(
    QD3D11SwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->currentFrameRenderTarget(targetBuffer);
}

//  QSize QD3D11SwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN15QD3D11SwapChain16surfacePixelSizeEv(
    QD3D11SwapChain *self) {
  self->surfacePixelSize();
}

//  bool QD3D11SwapChain::isFormatSupported(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QD3D11SwapChain17isFormatSupportedEN13QRhiSwapChain6FormatE(
    QD3D11SwapChain *self,
    QRhiSwapChain::Format f) {
  return self->isFormatSupported(f);
}

//  QRhiSwapChainHdrInfo QD3D11SwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_ZN15QD3D11SwapChain7hdrInfoEv(
    QD3D11SwapChain *self) {
  self->hdrInfo();
}

//  QRhiRenderPassDescriptor
//      *QD3D11SwapChain::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN15QD3D11SwapChain33newCompatibleRenderPassDescriptorEv(
    QD3D11SwapChain *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QD3D11SwapChain::createOrResize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QD3D11SwapChain14createOrResizeEv(QD3D11SwapChain *self) {
  return self->createOrResize();
}

#endif  // defined(Q_OS_WIN)
