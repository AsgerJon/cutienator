//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/platformsurfacefilter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/platformsurfacefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::SurfaceLocker::SurfaceLocker(QSurface *surface)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SurfaceLocker *ritual_ZN10Qt3DRender6Render13SurfaceLockerC1EP8QSurface(
    QSurface *surface) {
  return new Qt3DRender::Render::SurfaceLocker(surface);
}

//  Qt3DRender::Render::SurfaceLocker::~SurfaceLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13SurfaceLockerD1Ev(
    Qt3DRender::Render::SurfaceLocker *self) {
  delete self;
}

//  bool Qt3DRender::Render::SurfaceLocker::isSurfaceValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13SurfaceLocker14isSurfaceValidEv(
    const Qt3DRender::Render::SurfaceLocker *self) {
  return self->isSurfaceValid();
}
