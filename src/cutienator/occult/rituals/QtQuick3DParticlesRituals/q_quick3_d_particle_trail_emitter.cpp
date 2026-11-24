//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticletrailemitter_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticletrailemitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QQuick3DParticleTrailEmitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DParticleTrailEmitter10metaObjectEv(
    const QQuick3DParticleTrailEmitter *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleTrailEmitter::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DParticleTrailEmitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleTrailEmitter::tr(s, c, n));
}

//  QQuick3DParticleTrailEmitter::QQuick3DParticleTrailEmitter(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleTrailEmitter *ritual_ZN28QQuick3DParticleTrailEmitterC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleTrailEmitter(parent);
}

//  QQuick3DParticle *QQuick3DParticleTrailEmitter::follow() const
extern "C" Q_DECL_EXPORT
QQuick3DParticle *ritual_ZNK28QQuick3DParticleTrailEmitter6followEv(
    const QQuick3DParticleTrailEmitter *self) {
  return self->follow();
}

//  void QQuick3DParticleTrailEmitter::burst(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleTrailEmitter5burstEi(
    QQuick3DParticleTrailEmitter *self,
    int count) {
  self->burst(count);
}

//  void QQuick3DParticleTrailEmitter::setFollow(QQuick3DParticle *follow)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleTrailEmitter9setFollowEP16QQuick3DParticle(
    QQuick3DParticleTrailEmitter *self,
    QQuick3DParticle *follow) {
  self->setFollow(follow);
}

//  void QQuick3DParticleTrailEmitter::emitTrailParticles(const QVector3D
//      &centerPos, int emitAmount, int triggerType, const QVector3D &normal,
//      const QVector3D &velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleTrailEmitter18emitTrailParticlesERK9QVector3DiiS2_S2_(
    QQuick3DParticleTrailEmitter *self,
    const QVector3D *centerPos,
    int emitAmount,
    int triggerType,
    const QVector3D *normal,
    const QVector3D *velocity) {
  self->emitTrailParticles(
      *centerPos,
      emitAmount,
      triggerType,
      *normal,
      *velocity);
}

//  bool QQuick3DParticleTrailEmitter::hasBursts() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuick3DParticleTrailEmitter9hasBurstsEv(
    const QQuick3DParticleTrailEmitter *self) {
  return self->hasBursts();
}

//  void QQuick3DParticleTrailEmitter::clearBursts()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleTrailEmitter11clearBurstsEv(
    QQuick3DParticleTrailEmitter *self) {
  self->clearBursts();
}

//  void QQuick3DParticleTrailEmitter::burst(int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleTrailEmitter5burstEi(
    QQuick3DParticleTrailEmitter *self,
    int count) {
  self->QQuick3DParticleTrailEmitter::burst(count);
}
