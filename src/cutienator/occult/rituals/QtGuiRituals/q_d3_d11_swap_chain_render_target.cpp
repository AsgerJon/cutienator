//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, which Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11SwapChainRenderTarget::~QD3D11SwapChainRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QD3D11SwapChainRenderTargetD1Ev(
    QD3D11SwapChainRenderTarget *self) {
  delete self;
}

//  void QD3D11SwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QD3D11SwapChainRenderTarget7destroyEv(
    QD3D11SwapChainRenderTarget *self) {
  self->destroy();
}

//  QSize QD3D11SwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QD3D11SwapChainRenderTarget9pixelSizeEv(
    const QD3D11SwapChainRenderTarget *self) {
  self->pixelSize();
}

//  float QD3D11SwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QD3D11SwapChainRenderTarget16devicePixelRatioEv(
    const QD3D11SwapChainRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QD3D11SwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QD3D11SwapChainRenderTarget11sampleCountEv(
    const QD3D11SwapChainRenderTarget *self) {
  return self->sampleCount();
}

#endif  // defined(Q_OS_WIN)
