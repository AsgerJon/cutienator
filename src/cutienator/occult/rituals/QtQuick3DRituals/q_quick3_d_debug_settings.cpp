//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddebugsettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3ddebugsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuick3DDebugSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DDebugSettings10metaObjectEv(
    const QQuick3DDebugSettings *self) {
  return self->metaObject();
}

//  QString QQuick3DDebugSettings::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DDebugSettings2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DDebugSettings::tr(s, c, n));
}

//  QQuick3DDebugSettings::QQuick3DDebugSettings(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DDebugSettings *ritual_ZN21QQuick3DDebugSettingsC1EP7QObject(
    QObject *parent) {
  return new QQuick3DDebugSettings(parent);
}

//  QQuick3DMaterialOverrides QQuick3DDebugSettings::materialOverride() const
extern "C" Q_DECL_EXPORT
QQuick3DDebugSettings::QQuick3DMaterialOverrides ritual_ZNK21QQuick3DDebugSettings16materialOverrideEv(
    const QQuick3DDebugSettings *self) {
  return self->materialOverride();
}

//  void QQuick3DDebugSettings::setMaterialOverride(QQuick3DMaterialOverrides
//      newMaterialOverride)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings19setMaterialOverrideENS_25QQuick3DMaterialOverridesE(
    QQuick3DDebugSettings *self,
    QQuick3DDebugSettings::QQuick3DMaterialOverrides newMaterialOverride) {
  self->setMaterialOverride(newMaterialOverride);
}

//  bool QQuick3DDebugSettings::wireframeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings16wireframeEnabledEv(
    const QQuick3DDebugSettings *self) {
  return self->wireframeEnabled();
}

//  void QQuick3DDebugSettings::setWireframeEnabled(bool newWireframeEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings19setWireframeEnabledEb(
    QQuick3DDebugSettings *self,
    bool newWireframeEnabled) {
  self->setWireframeEnabled(newWireframeEnabled);
}

//  bool QQuick3DDebugSettings::drawDirectionalLightShadowBoxes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings31drawDirectionalLightShadowBoxesEv(
    const QQuick3DDebugSettings *self) {
  return self->drawDirectionalLightShadowBoxes();
}

//  void QQuick3DDebugSettings::setDrawDirectionalLightShadowBoxes(bool
//      newDrawDirectionalLightShadowBoxes)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings34setDrawDirectionalLightShadowBoxesEb(
    QQuick3DDebugSettings *self,
    bool newDrawDirectionalLightShadowBoxes) {
  self->setDrawDirectionalLightShadowBoxes(
      newDrawDirectionalLightShadowBoxes);
}

//  bool QQuick3DDebugSettings::drawPointLightShadowBoxes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings25drawPointLightShadowBoxesEv(
    const QQuick3DDebugSettings *self) {
  return self->drawPointLightShadowBoxes();
}

//  void QQuick3DDebugSettings::setDrawPointLightShadowBoxes(bool
//      newDrawPointLightShadowBoxes)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings28setDrawPointLightShadowBoxesEb(
    QQuick3DDebugSettings *self,
    bool newDrawPointLightShadowBoxes) {
  self->setDrawPointLightShadowBoxes(newDrawPointLightShadowBoxes);
}

//  bool QQuick3DDebugSettings::drawShadowCastingBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings23drawShadowCastingBoundsEv(
    const QQuick3DDebugSettings *self) {
  return self->drawShadowCastingBounds();
}

//  void QQuick3DDebugSettings::setDrawShadowCastingBounds(bool
//      newDrawShadowCastingBounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings26setDrawShadowCastingBoundsEb(
    QQuick3DDebugSettings *self,
    bool newDrawShadowCastingBounds) {
  self->setDrawShadowCastingBounds(newDrawShadowCastingBounds);
}

//  bool QQuick3DDebugSettings::drawShadowReceivingBounds() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings25drawShadowReceivingBoundsEv(
    const QQuick3DDebugSettings *self) {
  return self->drawShadowReceivingBounds();
}

//  void QQuick3DDebugSettings::setDrawShadowReceivingBounds(bool
//      newDrawShadowReceivingBounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings28setDrawShadowReceivingBoundsEb(
    QQuick3DDebugSettings *self,
    bool newDrawShadowReceivingBounds) {
  self->setDrawShadowReceivingBounds(newDrawShadowReceivingBounds);
}

//  bool QQuick3DDebugSettings::drawCascades() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings12drawCascadesEv(
    const QQuick3DDebugSettings *self) {
  return self->drawCascades();
}

//  void QQuick3DDebugSettings::setDrawCascades(bool newDrawCascades)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings15setDrawCascadesEb(
    QQuick3DDebugSettings *self,
    bool newDrawCascades) {
  self->setDrawCascades(newDrawCascades);
}

//  bool QQuick3DDebugSettings::drawSceneCascadeIntersection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings28drawSceneCascadeIntersectionEv(
    const QQuick3DDebugSettings *self) {
  return self->drawSceneCascadeIntersection();
}

//  void QQuick3DDebugSettings::setDrawSceneCascadeIntersection(bool
//      newDrawSceneCascadeIntersection)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings31setDrawSceneCascadeIntersectionEb(
    QQuick3DDebugSettings *self,
    bool newDrawSceneCascadeIntersection) {
  self->setDrawSceneCascadeIntersection(newDrawSceneCascadeIntersection);
}

//  bool QQuick3DDebugSettings::disableShadowCameraUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings25disableShadowCameraUpdateEv(
    const QQuick3DDebugSettings *self) {
  return self->disableShadowCameraUpdate();
}

//  void QQuick3DDebugSettings::setDisableShadowCameraUpdate(bool
//      newDisableShadowCameraUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings28setDisableShadowCameraUpdateEb(
    QQuick3DDebugSettings *self,
    bool newDisableShadowCameraUpdate) {
  self->setDisableShadowCameraUpdate(newDisableShadowCameraUpdate);
}

//  bool QQuick3DDebugSettings::drawCulledObjects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuick3DDebugSettings17drawCulledObjectsEv(
    const QQuick3DDebugSettings *self) {
  return self->drawCulledObjects();
}

//  void QQuick3DDebugSettings::setDrawCulledObjects(bool
//      newDrawCulledObjects)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings20setDrawCulledObjectsEb(
    QQuick3DDebugSettings *self,
    bool newDrawCulledObjects) {
  self->setDrawCulledObjects(newDrawCulledObjects);
}

//  void QQuick3DDebugSettings::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DDebugSettings6updateEv(QQuick3DDebugSettings *self) {
  self->update();
}
