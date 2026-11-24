//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentity_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DCore::Quick::Quick3DEntity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick13Quick3DEntity10metaObjectEv(
    const Qt3DCore::Quick::Quick3DEntity *self) {
  return self->metaObject();
}

//  QString Qt3DCore::Quick::Quick3DEntity::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick13Quick3DEntity2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DEntity::tr(s, c, n));
}

//  QEntity *Qt3DCore::Quick::Quick3DEntity::parentEntity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK8Qt3DCore5Quick13Quick3DEntity12parentEntityEv(
    const Qt3DCore::Quick::Quick3DEntity *self) {
  return self->parentEntity();
}
