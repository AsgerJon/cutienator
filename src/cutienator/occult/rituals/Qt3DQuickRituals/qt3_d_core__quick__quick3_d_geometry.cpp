//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dgeometry_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DCore::Quick::Quick3DGeometry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry10metaObjectEv(
    const Qt3DCore::Quick::Quick3DGeometry *self) {
  return self->metaObject();
}

//  QString Qt3DCore::Quick::Quick3DGeometry::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick15Quick3DGeometry2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DGeometry::tr(s, c, n));
}

//  QGeometry *Qt3DCore::Quick::Quick3DGeometry::parentGeometry() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZNK8Qt3DCore5Quick15Quick3DGeometry14parentGeometryEv(
    const Qt3DCore::Quick::Quick3DGeometry *self) {
  return self->parentGeometry();
}
