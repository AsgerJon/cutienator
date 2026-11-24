//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  const QMetaObject *QQuick3DLightmapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DLightmapper10metaObjectEv(
    const QQuick3DLightmapper *self) {
  return self->metaObject();
}

//  QString QQuick3DLightmapper::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DLightmapper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DLightmapper::tr(s, c, n));
}

//  float QQuick3DLightmapper::opacityThreshold() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DLightmapper16opacityThresholdEv(
    const QQuick3DLightmapper *self) {
  return self->opacityThreshold();
}

//  float QQuick3DLightmapper::bias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DLightmapper4biasEv(
    const QQuick3DLightmapper *self) {
  return self->bias();
}

//  bool QQuick3DLightmapper::isAdaptiveBiasEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DLightmapper21isAdaptiveBiasEnabledEv(
    const QQuick3DLightmapper *self) {
  return self->isAdaptiveBiasEnabled();
}

//  bool QQuick3DLightmapper::isIndirectLightEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DLightmapper22isIndirectLightEnabledEv(
    const QQuick3DLightmapper *self) {
  return self->isIndirectLightEnabled();
}

//  int QQuick3DLightmapper::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DLightmapper7samplesEv(
    const QQuick3DLightmapper *self) {
  return self->samples();
}

//  int QQuick3DLightmapper::indirectLightWorkgroupSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DLightmapper26indirectLightWorkgroupSizeEv(
    const QQuick3DLightmapper *self) {
  return self->indirectLightWorkgroupSize();
}

//  int QQuick3DLightmapper::bounces() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DLightmapper7bouncesEv(
    const QQuick3DLightmapper *self) {
  return self->bounces();
}

//  float QQuick3DLightmapper::indirectLightFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DLightmapper19indirectLightFactorEv(
    const QQuick3DLightmapper *self) {
  return self->indirectLightFactor();
}

//  QUrl QQuick3DLightmapper::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQuick3DLightmapper6sourceEv(
    const QQuick3DLightmapper *self) {
  return new QUrl(self->source());
}

//  float QQuick3DLightmapper::denoiseSigma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DLightmapper12denoiseSigmaEv(
    const QQuick3DLightmapper *self) {
  return self->denoiseSigma();
}

//  float QQuick3DLightmapper::texelsPerUnit() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DLightmapper13texelsPerUnitEv(
    const QQuick3DLightmapper *self) {
  return self->texelsPerUnit();
}

//  void QQuick3DLightmapper::setOpacityThreshold(float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper19setOpacityThresholdEf(
    QQuick3DLightmapper *self,
    float opacity) {
  self->setOpacityThreshold(opacity);
}

//  void QQuick3DLightmapper::setBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper7setBiasEf(
    QQuick3DLightmapper *self,
    float bias) {
  self->setBias(bias);
}

//  void QQuick3DLightmapper::setAdaptiveBiasEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper22setAdaptiveBiasEnabledEb(
    QQuick3DLightmapper *self,
    bool enabled) {
  self->setAdaptiveBiasEnabled(enabled);
}

//  void QQuick3DLightmapper::setIndirectLightEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper23setIndirectLightEnabledEb(
    QQuick3DLightmapper *self,
    bool enabled) {
  self->setIndirectLightEnabled(enabled);
}

//  void QQuick3DLightmapper::setSamples(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper10setSamplesEi(
    QQuick3DLightmapper *self,
    int count) {
  self->setSamples(count);
}

//  void QQuick3DLightmapper::setIndirectLightWorkgroupSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper29setIndirectLightWorkgroupSizeEi(
    QQuick3DLightmapper *self,
    int size) {
  self->setIndirectLightWorkgroupSize(size);
}

//  void QQuick3DLightmapper::setBounces(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper10setBouncesEi(
    QQuick3DLightmapper *self,
    int count) {
  self->setBounces(count);
}

//  void QQuick3DLightmapper::setIndirectLightFactor(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper22setIndirectLightFactorEf(
    QQuick3DLightmapper *self,
    float factor) {
  self->setIndirectLightFactor(factor);
}

//  void QQuick3DLightmapper::setSource(const QUrl &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper9setSourceERK4QUrl(
    QQuick3DLightmapper *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  void QQuick3DLightmapper::setDenoiseSigma(float newDenoiseSigma)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper15setDenoiseSigmaEf(
    QQuick3DLightmapper *self,
    float newDenoiseSigma) {
  self->setDenoiseSigma(newDenoiseSigma);
}

//  void QQuick3DLightmapper::setTexelsPerUnit(float newTexelsPerUnit)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DLightmapper16setTexelsPerUnitEf(
    QQuick3DLightmapper *self,
    float newTexelsPerUnit) {
  self->setTexelsPerUnit(newTexelsPerUnit);
}
