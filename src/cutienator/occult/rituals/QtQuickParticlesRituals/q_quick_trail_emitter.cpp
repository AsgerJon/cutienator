//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquicktrailemitter_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquicktrailemitter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickv4particledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  const QMetaObject *QQuickTrailEmitter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickTrailEmitter10metaObjectEv(
    const QQuickTrailEmitter *self) {
  return self->metaObject();
}

//  void *QQuickTrailEmitter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickTrailEmitter11qt_metacastEPKc(
    QQuickTrailEmitter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTrailEmitter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickTrailEmitter11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTrailEmitter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTrailEmitter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickTrailEmitter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTrailEmitter::tr(s, c, n));
}

//  QQuickTrailEmitter::QQuickTrailEmitter(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTrailEmitter *ritual_ZN18QQuickTrailEmitterC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTrailEmitter(parent);
}

//  void QQuickTrailEmitter::emitWindow(int timeStamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter10emitWindowEi(
    QQuickTrailEmitter *self,
    int timeStamp) {
  self->emitWindow(timeStamp);
}

//  void QQuickTrailEmitter::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter5resetEv(QQuickTrailEmitter *self) {
  self->reset();
}

//  int QQuickTrailEmitter::particlesPerParticlePerSecond() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickTrailEmitter29particlesPerParticlePerSecondEv(
    const QQuickTrailEmitter *self) {
  return self->particlesPerParticlePerSecond();
}

//  qreal QQuickTrailEmitter::emitterXVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickTrailEmitter17emitterXVariationEv(
    const QQuickTrailEmitter *self) {
  return self->emitterXVariation();
}

//  qreal QQuickTrailEmitter::emitterYVariation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickTrailEmitter17emitterYVariationEv(
    const QQuickTrailEmitter *self) {
  return self->emitterYVariation();
}

//  QString QQuickTrailEmitter::follow() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickTrailEmitter6followEv(
    const QQuickTrailEmitter *self) {
  return new QString(self->follow());
}

//  QQuickParticleExtruder *QQuickTrailEmitter::emissonShape() const
extern "C" Q_DECL_EXPORT
QQuickParticleExtruder *ritual_ZNK18QQuickTrailEmitter12emissonShapeEv(
    const QQuickTrailEmitter *self) {
  return self->emissonShape();
}

//  void QQuickTrailEmitter::emitFollowParticles(const
//      QList<QQuickV4ParticleData> &particles, const QQuickV4ParticleData
//      &followed)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter19emitFollowParticlesERK5QListI20QQuickV4ParticleDataERKS1_(
    QQuickTrailEmitter *self,
    const QList<QQuickV4ParticleData> *particles,
    const QQuickV4ParticleData *followed) {
  self->emitFollowParticles(*particles, *followed);
}

//  void QQuickTrailEmitter::particlesPerParticlePerSecondChanged(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter36particlesPerParticlePerSecondChangedEi(
    QQuickTrailEmitter *self,
    int arg) {
  self->particlesPerParticlePerSecondChanged(arg);
}

//  void QQuickTrailEmitter::emitterXVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter24emitterXVariationChangedEd(
    QQuickTrailEmitter *self,
    qreal arg) {
  self->emitterXVariationChanged(arg);
}

//  void QQuickTrailEmitter::emitterYVariationChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter24emitterYVariationChangedEd(
    QQuickTrailEmitter *self,
    qreal arg) {
  self->emitterYVariationChanged(arg);
}

//  void QQuickTrailEmitter::followChanged(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter13followChangedERK7QString(
    QQuickTrailEmitter *self,
    const QString *arg) {
  self->followChanged(*arg);
}

//  void QQuickTrailEmitter::emissionShapeChanged(QQuickParticleExtruder
//      *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter20emissionShapeChangedEP22QQuickParticleExtruder(
    QQuickTrailEmitter *self,
    QQuickParticleExtruder *arg) {
  self->emissionShapeChanged(arg);
}

//  void QQuickTrailEmitter::setParticlesPerParticlePerSecond(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter32setParticlesPerParticlePerSecondEi(
    QQuickTrailEmitter *self,
    int arg) {
  self->setParticlesPerParticlePerSecond(arg);
}

//  void QQuickTrailEmitter::setEmitterXVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter20setEmitterXVariationEd(
    QQuickTrailEmitter *self,
    qreal arg) {
  self->setEmitterXVariation(arg);
}

//  void QQuickTrailEmitter::setEmitterYVariation(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter20setEmitterYVariationEd(
    QQuickTrailEmitter *self,
    qreal arg) {
  self->setEmitterYVariation(arg);
}

//  void QQuickTrailEmitter::setFollow(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter9setFollowERK7QString(
    QQuickTrailEmitter *self,
    const QString *arg) {
  self->setFollow(*arg);
}

//  void QQuickTrailEmitter::setEmissionShape(QQuickParticleExtruder *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter16setEmissionShapeEP22QQuickParticleExtruder(
    QQuickTrailEmitter *self,
    QQuickParticleExtruder *arg) {
  self->setEmissionShape(arg);
}

//  void QQuickTrailEmitter::recalcParticlesPerSecond()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTrailEmitter24recalcParticlesPerSecondEv(
    QQuickTrailEmitter *self) {
  self->recalcParticlesPerSecond();
}

//  bool QQuickTrailEmitter::isEmitFollowConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickTrailEmitter21isEmitFollowConnectedEv(
    QQuickTrailEmitter *self) {
  return self->isEmitFollowConnected();
}

//  void QQuickTrailEmitter::emitWindow(int timeStamp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickTrailEmitter10emitWindowEi(
    QQuickTrailEmitter *self,
    int timeStamp) {
  self->QQuickTrailEmitter::emitWindow(timeStamp);
}

//  void QQuickTrailEmitter::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickTrailEmitter5resetEv(QQuickTrailEmitter *self) {
  self->QQuickTrailEmitter::reset();
}
