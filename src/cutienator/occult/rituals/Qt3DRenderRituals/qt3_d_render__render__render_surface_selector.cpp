//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendersurfaceselector_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendersurfaceselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  Qt3DRender::Render::RenderSurfaceSelector::RenderSurfaceSelector()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderSurfaceSelector *ritual_ZN10Qt3DRender6Render21RenderSurfaceSelectorC1Ev() {
  return new Qt3DRender::Render::RenderSurfaceSelector();
}

//  QSize Qt3DRender::Render::RenderSurfaceSelector::renderTargetSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector16renderTargetSizeEv(
    const Qt3DRender::Render::RenderSurfaceSelector *self) {
  return new QSize(self->renderTargetSize());
}

//  void Qt3DRender::Render::RenderSurfaceSelector::setRenderTargetSize(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21RenderSurfaceSelector19setRenderTargetSizeERK5QSize(
    Qt3DRender::Render::RenderSurfaceSelector *self,
    const QSize *size) {
  self->setRenderTargetSize(*size);
}

//  void Qt3DRender::Render::RenderSurfaceSelector::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21RenderSurfaceSelector16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderSurfaceSelector *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QSurface *Qt3DRender::Render::RenderSurfaceSelector::surface() const
extern "C" Q_DECL_EXPORT
QSurface *ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector7surfaceEv(
    const Qt3DRender::Render::RenderSurfaceSelector *self) {
  return self->surface();
}

//  int Qt3DRender::Render::RenderSurfaceSelector::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector5widthEv(
    const Qt3DRender::Render::RenderSurfaceSelector *self) {
  return self->width();
}

//  int Qt3DRender::Render::RenderSurfaceSelector::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector6heightEv(
    const Qt3DRender::Render::RenderSurfaceSelector *self) {
  return self->height();
}

//  float Qt3DRender::Render::RenderSurfaceSelector::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render21RenderSurfaceSelector16devicePixelRatioEv(
    const Qt3DRender::Render::RenderSurfaceSelector *self) {
  return self->devicePixelRatio();
}

//  void Qt3DRender::Render::RenderSurfaceSelector::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render21RenderSurfaceSelector16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderSurfaceSelector *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderSurfaceSelector::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
