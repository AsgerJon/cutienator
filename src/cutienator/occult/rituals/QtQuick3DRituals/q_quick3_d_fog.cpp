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
