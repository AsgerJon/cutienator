//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, which Qt's library offers not, and
//  'serializedFormat', giving a list of numbers.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11RenderPassDescriptor::~QD3D11RenderPassDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QD3D11RenderPassDescriptorD1Ev(
    QD3D11RenderPassDescriptor *self) {
  delete self;
}

//  void QD3D11RenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QD3D11RenderPassDescriptor7destroyEv(
    QD3D11RenderPassDescriptor *self) {
  self->destroy();
}

//  bool QD3D11RenderPassDescriptor::isCompatible(const
//      QRhiRenderPassDescriptor *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QD3D11RenderPassDescriptor12isCompatibleEPK24QRhiRenderPassDescriptor(
    const QD3D11RenderPassDescriptor *self,
    const QRhiRenderPassDescriptor *other) {
  return self->isCompatible(other);
}

//  QRhiRenderPassDescriptor
//      *QD3D11RenderPassDescriptor::newCompatibleRenderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK26QD3D11RenderPassDescriptor33newCompatibleRenderPassDescriptorEv(
    const QD3D11RenderPassDescriptor *self) {
  return self->newCompatibleRenderPassDescriptor();
}

#endif  // defined(Q_OS_WIN)
