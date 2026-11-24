//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlevectordirection_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlevectordirection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QQuick3DParticleVectorDirection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuick3DParticleVectorDirection10metaObjectEv(
    const QQuick3DParticleVectorDirection *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleVectorDirection::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuick3DParticleVectorDirection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleVectorDirection::tr(s, c, n));
}

//  QQuick3DParticleVectorDirection::QQuick3DParticleVectorDirection(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleVectorDirection *ritual_ZN31QQuick3DParticleVectorDirectionC1EP7QObject(
    QObject *parent) {
  return new QQuick3DParticleVectorDirection(parent);
}

//  QVector3D QQuick3DParticleVectorDirection::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK31QQuick3DParticleVectorDirection9directionEv(
    const QQuick3DParticleVectorDirection *self) {
  return new QVector3D(self->direction());
}

//  QVector3D QQuick3DParticleVectorDirection::directionVariation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK31QQuick3DParticleVectorDirection18directionVariationEv(
    const QQuick3DParticleVectorDirection *self) {
  return new QVector3D(self->directionVariation());
}

//  bool QQuick3DParticleVectorDirection::normalized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuick3DParticleVectorDirection10normalizedEv(
    const QQuick3DParticleVectorDirection *self) {
  return self->normalized();
}

//  void QQuick3DParticleVectorDirection::setDirection(const QVector3D
//      &direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleVectorDirection12setDirectionERK9QVector3D(
    QQuick3DParticleVectorDirection *self,
    const QVector3D *direction) {
  self->setDirection(*direction);
}

//  void QQuick3DParticleVectorDirection::setDirectionVariation(const
//      QVector3D &directionVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleVectorDirection21setDirectionVariationERK9QVector3D(
    QQuick3DParticleVectorDirection *self,
    const QVector3D *directionVariation) {
  self->setDirectionVariation(*directionVariation);
}

//  void QQuick3DParticleVectorDirection::setNormalized(bool normalized)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleVectorDirection13setNormalizedEb(
    QQuick3DParticleVectorDirection *self,
    bool normalized) {
  self->setNormalized(normalized);
}

//  QVector3D QQuick3DParticleVectorDirection::sample(const
//      QQuick3DParticleData &d)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN31QQuick3DParticleVectorDirection6sampleERK20QQuick3DParticleData(
    QQuick3DParticleVectorDirection *self,
    const QQuick3DParticleData *d) {
  return new QVector3D(self->sample(*d));
}

//  QVector3D QQuick3DParticleVectorDirection::sample(const
//      QQuick3DParticleData &d)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN31QQuick3DParticleVectorDirection6sampleERK20QQuick3DParticleData(
    QQuick3DParticleVectorDirection *self,
    const QQuick3DParticleData *d) {
  return new QVector3D(self->QQuick3DParticleVectorDirection::sample(*d));
}
