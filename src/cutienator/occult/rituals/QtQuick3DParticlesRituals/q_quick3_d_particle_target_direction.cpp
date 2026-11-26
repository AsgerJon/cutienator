//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticletargetdirection_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticletargetdirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuick3DParticleTargetDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuick3DParticleTargetDirection10metaObjectEv(
    const QQuick3DParticleTargetDirection *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleTargetDirection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuick3DParticleTargetDirection11qt_metacastEPKc(
    QQuick3DParticleTargetDirection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleTargetDirection::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuick3DParticleTargetDirection11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleTargetDirection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleTargetDirection::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuick3DParticleTargetDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleTargetDirection::tr(s, c, n));
}

//  QQuick3DParticleTargetDirection::QQuick3DParticleTargetDirection(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleTargetDirection *ritual_ZN31QQuick3DParticleTargetDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleTargetDirection(parent);
}

//  QVector3D QQuick3DParticleTargetDirection::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK31QQuick3DParticleTargetDirection8positionEv(
    const QQuick3DParticleTargetDirection *self) {
  return new QVector3D(self->position());
}

//  void QQuick3DParticleTargetDirection::setPosition(const QVector3D
//      &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection11setPositionERK9QVector3D(
    QQuick3DParticleTargetDirection *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  bool QQuick3DParticleTargetDirection::normalized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuick3DParticleTargetDirection10normalizedEv(
    const QQuick3DParticleTargetDirection *self) {
  return self->normalized();
}

//  float QQuick3DParticleTargetDirection::magnitude() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK31QQuick3DParticleTargetDirection9magnitudeEv(
    const QQuick3DParticleTargetDirection *self) {
  return self->magnitude();
}

//  float QQuick3DParticleTargetDirection::magnitudeVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK31QQuick3DParticleTargetDirection18magnitudeVariationEv(
    const QQuick3DParticleTargetDirection *self) {
  return self->magnitudeVariation();
}

//  QVector3D QQuick3DParticleTargetDirection::positionVariation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK31QQuick3DParticleTargetDirection17positionVariationEv(
    const QQuick3DParticleTargetDirection *self) {
  return new QVector3D(self->positionVariation());
}

//  void QQuick3DParticleTargetDirection::setPositionVariation(const
//      QVector3D &positionVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection20setPositionVariationERK9QVector3D(
    QQuick3DParticleTargetDirection *self,
    const QVector3D *positionVariation) {
  self->setPositionVariation(*positionVariation);
}

//  void QQuick3DParticleTargetDirection::setNormalized(bool normalized)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection13setNormalizedEb(
    QQuick3DParticleTargetDirection *self,
    bool normalized) {
  self->setNormalized(normalized);
}

//  void QQuick3DParticleTargetDirection::setMagnitude(float magnitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection12setMagnitudeEf(
    QQuick3DParticleTargetDirection *self,
    float magnitude) {
  self->setMagnitude(magnitude);
}

//  void QQuick3DParticleTargetDirection::setMagnitudeVariation(float
//      magnitudeVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection21setMagnitudeVariationEf(
    QQuick3DParticleTargetDirection *self,
    float magnitudeVariation) {
  self->setMagnitudeVariation(magnitudeVariation);
}

//  void QQuick3DParticleTargetDirection::positionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection15positionChangedEv(
    QQuick3DParticleTargetDirection *self) {
  self->positionChanged();
}

//  void QQuick3DParticleTargetDirection::positionVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection24positionVariationChangedEv(
    QQuick3DParticleTargetDirection *self) {
  self->positionVariationChanged();
}

//  void QQuick3DParticleTargetDirection::normalizedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection17normalizedChangedEv(
    QQuick3DParticleTargetDirection *self) {
  self->normalizedChanged();
}

//  void QQuick3DParticleTargetDirection::magnitudeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection16magnitudeChangedEv(
    QQuick3DParticleTargetDirection *self) {
  self->magnitudeChanged();
}

//  void QQuick3DParticleTargetDirection::magnitudeChangedVariation()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleTargetDirection25magnitudeChangedVariationEv(
    QQuick3DParticleTargetDirection *self) {
  self->magnitudeChangedVariation();
}

//  QVector3D QQuick3DParticleTargetDirection::sample(const
//      QQuick3DParticleData &d)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN31QQuick3DParticleTargetDirection6sampleERK20QQuick3DParticleData(
    QQuick3DParticleTargetDirection *self,
    const QQuick3DParticleData *d) {
  return new QVector3D(self->sample(*d));
}

//  QVector3D QQuick3DParticleTargetDirection::sample(const
//      QQuick3DParticleData &d)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN31QQuick3DParticleTargetDirection6sampleERK20QQuick3DParticleData(
    QQuick3DParticleTargetDirection *self,
    const QQuick3DParticleData *d) {
  return new QVector3D(self->QQuick3DParticleTargetDirection::sample(*d));
}
