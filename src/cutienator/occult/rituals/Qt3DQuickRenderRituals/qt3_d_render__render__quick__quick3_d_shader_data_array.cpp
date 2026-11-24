//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickRende
//  r/6.12.0/Qt3DQuickRender/private/quick3dshaderdataarray_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dshaderdataarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DShaderDataArray::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick22Quick3DShaderDataArray10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DShaderDataArray *self) {
  return self->metaObject();
}

//  QString Qt3DRender::Render::Quick::Quick3DShaderDataArray::tr(const char
//      *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick22Quick3DShaderDataArray2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DShaderDataArray::tr(
          s,
          c,
          n));
}
