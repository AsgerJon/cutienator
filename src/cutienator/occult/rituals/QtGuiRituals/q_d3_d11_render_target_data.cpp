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

//  QD3D11RenderTargetData::QD3D11RenderTargetData(QRhiImplementation *a0)
extern "C" Q_DECL_EXPORT
QD3D11RenderTargetData *ritual_ZN22QD3D11RenderTargetDataC1EP18QRhiImplementation(
    QRhiImplementation *a0) {
  return new QD3D11RenderTargetData(a0);
}

//  QD3D11RenderTargetData::~QD3D11RenderTargetData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11RenderTargetDataD1Ev(QD3D11RenderTargetData *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
