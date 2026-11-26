//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dfog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QQuick3DFog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuick3DFog10metaObjectEv(
    const QQuick3DFog *self) {
  return self->metaObject();
}

//  void *QQuick3DFog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QQuick3DFog11qt_metacastEPKc(
    QQuick3DFog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DFog::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QQuick3DFog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DFog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DFog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuick3DFog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DFog::tr(s, c, n));
}

//  bool QQuick3DFog::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuick3DFog9isEnabledEv(const QQuick3DFog *self) {
  return self->isEnabled();
}

//  QColor QQuick3DFog::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuick3DFog5colorEv(const QQuick3DFog *self) {
  return new QColor(self->color());
}

//  float QQuick3DFog::density() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog7densityEv(const QQuick3DFog *self) {
  return self->density();
}

//  bool QQuick3DFog::isDepthEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuick3DFog14isDepthEnabledEv(const QQuick3DFog *self) {
  return self->isDepthEnabled();
}

//  float QQuick3DFog::depthNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog9depthNearEv(const QQuick3DFog *self) {
  return self->depthNear();
}

//  float QQuick3DFog::depthFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog8depthFarEv(const QQuick3DFog *self) {
  return self->depthFar();
}

//  float QQuick3DFog::depthCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog10depthCurveEv(const QQuick3DFog *self) {
  return self->depthCurve();
}

//  bool QQuick3DFog::isHeightEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuick3DFog15isHeightEnabledEv(const QQuick3DFog *self) {
  return self->isHeightEnabled();
}

//  float QQuick3DFog::leastIntenseY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog13leastIntenseYEv(const QQuick3DFog *self) {
  return self->leastIntenseY();
}

//  float QQuick3DFog::mostIntenseY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog12mostIntenseYEv(const QQuick3DFog *self) {
  return self->mostIntenseY();
}

//  float QQuick3DFog::heightCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog11heightCurveEv(const QQuick3DFog *self) {
  return self->heightCurve();
}

//  bool QQuick3DFog::isTransmitEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuick3DFog17isTransmitEnabledEv(const QQuick3DFog *self) {
  return self->isTransmitEnabled();
}

//  float QQuick3DFog::transmitCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuick3DFog13transmitCurveEv(const QQuick3DFog *self) {
  return self->transmitCurve();
}

//  void QQuick3DFog::setEnabled(bool newEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog10setEnabledEb(
    QQuick3DFog *self,
    bool newEnabled) {
  self->setEnabled(newEnabled);
}

//  void QQuick3DFog::setColor(const QColor &newColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog8setColorERK6QColor(
    QQuick3DFog *self,
    const QColor *newColor) {
  self->setColor(*newColor);
}

//  void QQuick3DFog::setDensity(float newDensity)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog10setDensityEf(
    QQuick3DFog *self,
    float newDensity) {
  self->setDensity(newDensity);
}

//  void QQuick3DFog::setDepthEnabled(bool newDepthEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog15setDepthEnabledEb(
    QQuick3DFog *self,
    bool newDepthEnabled) {
  self->setDepthEnabled(newDepthEnabled);
}

//  void QQuick3DFog::setDepthNear(float newDepthNear)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog12setDepthNearEf(
    QQuick3DFog *self,
    float newDepthNear) {
  self->setDepthNear(newDepthNear);
}

//  void QQuick3DFog::setDepthFar(float newDepthFar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog11setDepthFarEf(
    QQuick3DFog *self,
    float newDepthFar) {
  self->setDepthFar(newDepthFar);
}

//  void QQuick3DFog::setDepthCurve(float newDepthCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog13setDepthCurveEf(
    QQuick3DFog *self,
    float newDepthCurve) {
  self->setDepthCurve(newDepthCurve);
}

//  void QQuick3DFog::setHeightEnabled(bool newHeightEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog16setHeightEnabledEb(
    QQuick3DFog *self,
    bool newHeightEnabled) {
  self->setHeightEnabled(newHeightEnabled);
}

//  void QQuick3DFog::setLeastIntenseY(float newleastIntenseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog16setLeastIntenseYEf(
    QQuick3DFog *self,
    float newleastIntenseY) {
  self->setLeastIntenseY(newleastIntenseY);
}

//  void QQuick3DFog::setMostIntenseY(float newmostIntenseY)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog15setMostIntenseYEf(
    QQuick3DFog *self,
    float newmostIntenseY) {
  self->setMostIntenseY(newmostIntenseY);
}

//  void QQuick3DFog::setHeightCurve(float newHeightCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog14setHeightCurveEf(
    QQuick3DFog *self,
    float newHeightCurve) {
  self->setHeightCurve(newHeightCurve);
}

//  void QQuick3DFog::setTransmitEnabled(bool newTransmitEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog18setTransmitEnabledEb(
    QQuick3DFog *self,
    bool newTransmitEnabled) {
  self->setTransmitEnabled(newTransmitEnabled);
}

//  void QQuick3DFog::setTransmitCurve(float newTransmitCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog16setTransmitCurveEf(
    QQuick3DFog *self,
    float newTransmitCurve) {
  self->setTransmitCurve(newTransmitCurve);
}

//  void QQuick3DFog::changed()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog7changedEv(QQuick3DFog *self) {
  self->changed();
}

//  void QQuick3DFog::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog14enabledChangedEv(QQuick3DFog *self) {
  self->enabledChanged();
}

//  void QQuick3DFog::colorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog12colorChangedEv(QQuick3DFog *self) {
  self->colorChanged();
}

//  void QQuick3DFog::densityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog14densityChangedEv(QQuick3DFog *self) {
  self->densityChanged();
}

//  void QQuick3DFog::depthEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog19depthEnabledChangedEv(QQuick3DFog *self) {
  self->depthEnabledChanged();
}

//  void QQuick3DFog::depthNearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog16depthNearChangedEv(QQuick3DFog *self) {
  self->depthNearChanged();
}

//  void QQuick3DFog::depthFarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog15depthFarChangedEv(QQuick3DFog *self) {
  self->depthFarChanged();
}

//  void QQuick3DFog::depthCurveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog17depthCurveChangedEv(QQuick3DFog *self) {
  self->depthCurveChanged();
}

//  void QQuick3DFog::heightEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog20heightEnabledChangedEv(QQuick3DFog *self) {
  self->heightEnabledChanged();
}

//  void QQuick3DFog::leastIntenseYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog20leastIntenseYChangedEv(QQuick3DFog *self) {
  self->leastIntenseYChanged();
}

//  void QQuick3DFog::mostIntenseYChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog19mostIntenseYChangedEv(QQuick3DFog *self) {
  self->mostIntenseYChanged();
}

//  void QQuick3DFog::heightCurveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog18heightCurveChangedEv(QQuick3DFog *self) {
  self->heightCurveChanged();
}

//  void QQuick3DFog::transmitEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog22transmitEnabledChangedEv(QQuick3DFog *self) {
  self->transmitEnabledChanged();
}

//  void QQuick3DFog::transmitCurveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuick3DFog20transmitCurveChangedEv(QQuick3DFog *self) {
  self->transmitCurveChanged();
}
