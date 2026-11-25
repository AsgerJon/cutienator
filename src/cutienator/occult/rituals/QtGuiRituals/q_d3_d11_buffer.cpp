//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, and 'unorderedAccessView', which
//  Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11Buffer::~QD3D11Buffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QD3D11BufferD1Ev(QD3D11Buffer *self) {
  delete self;
}

//  void QD3D11Buffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QD3D11Buffer7destroyEv(QD3D11Buffer *self) {
  self->destroy();
}

//  bool QD3D11Buffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QD3D11Buffer6createEv(QD3D11Buffer *self) {
  return self->create();
}

//  QRhiBuffer::NativeBuffer QD3D11Buffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_ZN12QD3D11Buffer12nativeBufferEv(
    QD3D11Buffer *self) {
  self->nativeBuffer();
}

//  char *QD3D11Buffer::beginFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
char *ritual_ZN12QD3D11Buffer43beginFullDynamicBufferUpdateForCurrentFrameEv(
    QD3D11Buffer *self) {
  return self->beginFullDynamicBufferUpdateForCurrentFrame();
}

//  void QD3D11Buffer::endFullDynamicBufferUpdateForCurrentFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QD3D11Buffer41endFullDynamicBufferUpdateForCurrentFrameEv(
    QD3D11Buffer *self) {
  self->endFullDynamicBufferUpdateForCurrentFrame();
}

#endif  // defined(Q_OS_WIN)
