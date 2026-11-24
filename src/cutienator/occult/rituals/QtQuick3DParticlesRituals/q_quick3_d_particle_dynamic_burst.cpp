//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticledynamicburst_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledynamicburst_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuick3DParticleDynamicBurst::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DParticleDynamicBurst10metaObjectEv(
    const QQuick3DParticleDynamicBurst *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleDynamicBurst::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DParticleDynamicBurst2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleDynamicBurst::tr(s, c, n));
}

//  QQuick3DParticleDynamicBurst::QQuick3DParticleDynamicBurst(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleDynamicBurst *ritual_ZN28QQuick3DParticleDynamicBurstC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleDynamicBurst(parent);
}

//  bool QQuick3DParticleDynamicBurst::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuick3DParticleDynamicBurst7enabledEv(
    const QQuick3DParticleDynamicBurst *self) {
  return self->enabled();
}

//  int QQuick3DParticleDynamicBurst::amountVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuick3DParticleDynamicBurst15amountVariationEv(
    const QQuick3DParticleDynamicBurst *self) {
  return self->amountVariation();
}

//  TriggerMode QQuick3DParticleDynamicBurst::triggerMode() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleDynamicBurst::TriggerMode ritual_ZNK28QQuick3DParticleDynamicBurst11triggerModeEv(
    const QQuick3DParticleDynamicBurst *self) {
  return self->triggerMode();
}

//  void QQuick3DParticleDynamicBurst::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleDynamicBurst10setEnabledEb(
    QQuick3DParticleDynamicBurst *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QQuick3DParticleDynamicBurst::setAmountVariation(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleDynamicBurst18setAmountVariationEi(
    QQuick3DParticleDynamicBurst *self,
    int value) {
  self->setAmountVariation(value);
}

//  void QQuick3DParticleDynamicBurst::setTriggerMode(TriggerMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleDynamicBurst14setTriggerModeENS_11TriggerModeE(
    QQuick3DParticleDynamicBurst *self,
    QQuick3DParticleDynamicBurst::TriggerMode mode) {
  self->setTriggerMode(mode);
}
