//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/offscreensurfacehelper_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/offscreensurfacehelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *Qt3DRender::Render::OffscreenSurfaceHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render22OffscreenSurfaceHelper10metaObjectEv(
    const Qt3DRender::Render::OffscreenSurfaceHelper *self) {
  return self->metaObject();
}

//  QString Qt3DRender::Render::OffscreenSurfaceHelper::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::OffscreenSurfaceHelper::tr(
          s,
          c,
          n));
}

//  QOffscreenSurface
//      *Qt3DRender::Render::OffscreenSurfaceHelper::offscreenSurface() const
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZNK10Qt3DRender6Render22OffscreenSurfaceHelper16offscreenSurfaceEv(
    const Qt3DRender::Render::OffscreenSurfaceHelper *self) {
  return self->offscreenSurface();
}
