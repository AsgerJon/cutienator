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

//  QD3D11Adapter::~QD3D11Adapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QD3D11AdapterD1Ev(QD3D11Adapter *self) {
  delete self;
}

//  QRhiDriverInfo QD3D11Adapter::info() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK13QD3D11Adapter4infoEv(const QD3D11Adapter *self) {
  self->info();
}

#endif  // defined(Q_OS_WIN)
