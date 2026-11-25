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

//  QD3D11ShaderResourceBindings::~QD3D11ShaderResourceBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QD3D11ShaderResourceBindingsD1Ev(
    QD3D11ShaderResourceBindings *self) {
  delete self;
}

//  void QD3D11ShaderResourceBindings::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QD3D11ShaderResourceBindings7destroyEv(
    QD3D11ShaderResourceBindings *self) {
  self->destroy();
}

//  bool QD3D11ShaderResourceBindings::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QD3D11ShaderResourceBindings6createEv(
    QD3D11ShaderResourceBindings *self) {
  return self->create();
}

//  void QD3D11ShaderResourceBindings::updateResources(UpdateFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QD3D11ShaderResourceBindings15updateResourcesE6QFlagsIN26QRhiShaderResourceBindings10UpdateFlagEE(
    QD3D11ShaderResourceBindings *self,
    int flags) {
  self->updateResources(QFlags<QRhiShaderResourceBindings::UpdateFlag>::fromInt(flags));
}

#endif  // defined(Q_OS_WIN)
