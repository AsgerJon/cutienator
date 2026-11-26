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

//  void *Qt3DRender::Render::OffscreenSurfaceHelper::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper11qt_metacastEPKc(
    Qt3DRender::Render::OffscreenSurfaceHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DRender::Render::OffscreenSurfaceHelper::qt_metacall(QMetaObject::
//      Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::OffscreenSurfaceHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  Qt3DRender::Render::OffscreenSurfaceHelper::OffscreenSurfaceHelper(Abstra
//      ctRenderer *renderer, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::OffscreenSurfaceHelper *ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelperC1EPNS0_16AbstractRendererEP7QObject(
    Qt3DRender::Render::AbstractRenderer *renderer,
    QObject *parent) {
  return new Qt3DRender::Render::OffscreenSurfaceHelper(renderer, parent);
}

//  QOffscreenSurface
//      *Qt3DRender::Render::OffscreenSurfaceHelper::offscreenSurface() const
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZNK10Qt3DRender6Render22OffscreenSurfaceHelper16offscreenSurfaceEv(
    const Qt3DRender::Render::OffscreenSurfaceHelper *self) {
  return self->offscreenSurface();
}

//  void Qt3DRender::Render::OffscreenSurfaceHelper::createOffscreenSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render22OffscreenSurfaceHelper22createOffscreenSurfaceEv(
    Qt3DRender::Render::OffscreenSurfaceHelper *self) {
  self->createOffscreenSurface();
}
