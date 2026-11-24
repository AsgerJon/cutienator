//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnodeinstantiator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dnodeinstantiator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DCore::Quick::Quick3DNodeInstantiator::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick23Quick3DNodeInstantiator10metaObjectEv(
    const Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return self->metaObject();
}

//  QString Qt3DCore::Quick::Quick3DNodeInstantiator::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DNodeInstantiator::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DNodeInstantiator as the QQmlParserStatus it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_Qt3DCore_Quick_Quick3DNodeInstantiator_QQmlParserStatus(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator10classBeginEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->Qt3DCore::Quick::Quick3DNodeInstantiator::classBegin();
}

//  void Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore5Quick23Quick3DNodeInstantiator17componentCompleteEv(
    Qt3DCore::Quick::Quick3DNodeInstantiator *self) {
  self->Qt3DCore::Quick::Quick3DNodeInstantiator::componentComplete();
}
