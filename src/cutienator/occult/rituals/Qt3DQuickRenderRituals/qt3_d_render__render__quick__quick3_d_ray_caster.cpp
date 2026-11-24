//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick16Quick3DRayCaster10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->metaObject();
}

//  QString Qt3DRender::Render::Quick::Quick3DRayCaster::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DRayCaster::tr(
          s,
          c,
          n));
}

//  Quick3DRayCasterPrivate
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *ritual_ZN10Qt3DRender6Render5Quick16Quick3DRayCaster6d_funcEv(
    Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->d_func();
}

//  const Quick3DRayCasterPrivate
//      *Qt3DRender::Render::Quick::Quick3DRayCaster::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *ritual_ZNK10Qt3DRender6Render5Quick16Quick3DRayCaster6d_funcEv(
    const Qt3DRender::Render::Quick::Quick3DRayCaster *self) {
  return self->d_func();
}
