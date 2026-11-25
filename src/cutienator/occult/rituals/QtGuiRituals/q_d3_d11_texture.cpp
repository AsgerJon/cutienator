//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor, 'prepareCreate', 'finishCreate' and
//  'unorderedAccessViewForLevel', which Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11Texture::~QD3D11Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QD3D11TextureD1Ev(QD3D11Texture *self) {
  delete self;
}

//  void QD3D11Texture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QD3D11Texture7destroyEv(QD3D11Texture *self) {
  self->destroy();
}

//  bool QD3D11Texture::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QD3D11Texture6createEv(QD3D11Texture *self) {
  return self->create();
}

//  bool QD3D11Texture::createFrom(NativeTexture src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QD3D11Texture10createFromEN11QRhiTexture13NativeTextureE(
    QD3D11Texture *self,
    const QRhiTexture::NativeTexture *src) {
  return self->createFrom(*src);
}

//  QRhiTexture::NativeTexture QD3D11Texture::nativeTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture::NativeTexture *ritual_ZN13QD3D11Texture13nativeTextureEv(
    QD3D11Texture *self) {
  self->nativeTexture();
}

//  ID3D11Resource *QD3D11Texture::textureResource() const
extern "C" Q_DECL_EXPORT
ID3D11Resource *ritual_ZNK13QD3D11Texture15textureResourceEv(
    const QD3D11Texture *self) {
  return self->textureResource();
}

#endif  // defined(Q_OS_WIN)
