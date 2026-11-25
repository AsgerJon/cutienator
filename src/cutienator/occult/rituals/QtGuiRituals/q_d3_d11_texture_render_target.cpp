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

//  QD3D11TextureRenderTarget::~QD3D11TextureRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QD3D11TextureRenderTargetD1Ev(
    QD3D11TextureRenderTarget *self) {
  delete self;
}

//  void QD3D11TextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QD3D11TextureRenderTarget7destroyEv(
    QD3D11TextureRenderTarget *self) {
  self->destroy();
}

//  QSize QD3D11TextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QD3D11TextureRenderTarget9pixelSizeEv(
    const QD3D11TextureRenderTarget *self) {
  self->pixelSize();
}

//  float QD3D11TextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QD3D11TextureRenderTarget16devicePixelRatioEv(
    const QD3D11TextureRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QD3D11TextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QD3D11TextureRenderTarget11sampleCountEv(
    const QD3D11TextureRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor
//      *QD3D11TextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN25QD3D11TextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QD3D11TextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QD3D11TextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QD3D11TextureRenderTarget6createEv(
    QD3D11TextureRenderTarget *self) {
  return self->create();
}

#endif  // defined(Q_OS_WIN)
