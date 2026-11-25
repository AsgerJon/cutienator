//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: 'prepare', 'destroy' and 'tryQueryTimestamps', which
//  Qt's library offers not.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QD3D11SwapChainTimestamps::~QD3D11SwapChainTimestamps()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QD3D11SwapChainTimestampsD1Ev(
    QD3D11SwapChainTimestamps *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
