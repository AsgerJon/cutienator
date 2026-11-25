//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  void QD3D11RenderTargetData::Views::setFrom(int colorAttCount,
//      ID3D11RenderTargetView *const *rtv, ID3D11DepthStencilView *dsv)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11RenderTargetData5Views7setFromEiPKP22ID3D11RenderTargetViewP22ID3D11DepthStencilView(
    QD3D11RenderTargetData::Views *self,
    int colorAttCount,
    ID3D11RenderTargetView *const *rtv,
    ID3D11DepthStencilView *dsv) {
  self->setFrom(colorAttCount, rtv, dsv);
}

//  void QD3D11RenderTargetData::Views::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11RenderTargetData5Views5resetEv(
    QD3D11RenderTargetData::Views *self) {
  self->reset();
}

//  QD3D11RenderTargetData::Views::~Views()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11RenderTargetData5ViewsD1Ev(
    QD3D11RenderTargetData::Views *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
