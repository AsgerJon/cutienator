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

//  QD3D11GraphicsPipeline::~QD3D11GraphicsPipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11GraphicsPipelineD1Ev(QD3D11GraphicsPipeline *self) {
  delete self;
}

//  void QD3D11GraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QD3D11GraphicsPipeline7destroyEv(
    QD3D11GraphicsPipeline *self) {
  self->destroy();
}

//  bool QD3D11GraphicsPipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QD3D11GraphicsPipeline6createEv(
    QD3D11GraphicsPipeline *self) {
  return self->create();
}

#endif  // defined(Q_OS_WIN)
