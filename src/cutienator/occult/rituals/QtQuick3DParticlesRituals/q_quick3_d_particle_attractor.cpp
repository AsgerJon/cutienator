//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleattractor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleattractor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleAttractor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleAttractor : QQuick3DParticleAttractor {
  using QQuick3DParticleAttractor::prepareToAffect;
  using QQuick3DParticleAttractor::affectParticle;
};

//  const QMetaObject *QQuick3DParticleAttractor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuick3DParticleAttractor10metaObjectEv(
    const QQuick3DParticleAttractor *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleAttractor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuick3DParticleAttractor11qt_metacastEPKc(
    QQuick3DParticleAttractor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleAttractor::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuick3DParticleAttractor11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleAttractor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleAttractor::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuick3DParticleAttractor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleAttractor::tr(s, c, n));
}

//  QQuick3DParticleAttractor::QQuick3DParticleAttractor(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleAttractor *ritual_ZN25QQuick3DParticleAttractorC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleAttractor(parent);
}

//  QVector3D QQuick3DParticleAttractor::positionVariation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuick3DParticleAttractor17positionVariationEv(
    const QQuick3DParticleAttractor *self) {
  return new QVector3D(self->positionVariation());
}

//  QQuick3DParticleAbstractShape *QQuick3DParticleAttractor::shape() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleAbstractShape *ritual_ZNK25QQuick3DParticleAttractor5shapeEv(
    const QQuick3DParticleAttractor *self) {
  return self->shape();
}

//  int QQuick3DParticleAttractor::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleAttractor8durationEv(
    const QQuick3DParticleAttractor *self) {
  return self->duration();
}

//  int QQuick3DParticleAttractor::durationVariation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleAttractor17durationVariationEv(
    const QQuick3DParticleAttractor *self) {
  return self->durationVariation();
}

//  bool QQuick3DParticleAttractor::hideAtEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuick3DParticleAttractor9hideAtEndEv(
    const QQuick3DParticleAttractor *self) {
  return self->hideAtEnd();
}

//  bool QQuick3DParticleAttractor::useCachedPositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuick3DParticleAttractor18useCachedPositionsEv(
    const QQuick3DParticleAttractor *self) {
  return self->useCachedPositions();
}

//  int QQuick3DParticleAttractor::positionsAmount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuick3DParticleAttractor15positionsAmountEv(
    const QQuick3DParticleAttractor *self) {
  return self->positionsAmount();
}

//  void QQuick3DParticleAttractor::setPositionVariation(const QVector3D
//      &positionVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor20setPositionVariationERK9QVector3D(
    QQuick3DParticleAttractor *self,
    const QVector3D *positionVariation) {
  self->setPositionVariation(*positionVariation);
}

//  void QQuick3DParticleAttractor::setShape(QQuick3DParticleAbstractShape
//      *shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor8setShapeEP29QQuick3DParticleAbstractShape(
    QQuick3DParticleAttractor *self,
    QQuick3DParticleAbstractShape *shape) {
  self->setShape(shape);
}

//  void QQuick3DParticleAttractor::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor11setDurationEi(
    QQuick3DParticleAttractor *self,
    int duration) {
  self->setDuration(duration);
}

//  void QQuick3DParticleAttractor::setDurationVariation(int
//      durationVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor20setDurationVariationEi(
    QQuick3DParticleAttractor *self,
    int durationVariation) {
  self->setDurationVariation(durationVariation);
}

//  void QQuick3DParticleAttractor::setHideAtEnd(bool hideAtEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor12setHideAtEndEb(
    QQuick3DParticleAttractor *self,
    bool hideAtEnd) {
  self->setHideAtEnd(hideAtEnd);
}

//  void QQuick3DParticleAttractor::setUseCachedPositions(bool
//      useCachedPositions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor21setUseCachedPositionsEb(
    QQuick3DParticleAttractor *self,
    bool useCachedPositions) {
  self->setUseCachedPositions(useCachedPositions);
}

//  void QQuick3DParticleAttractor::setPositionsAmount(int positionsAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor18setPositionsAmountEi(
    QQuick3DParticleAttractor *self,
    int positionsAmount) {
  self->setPositionsAmount(positionsAmount);
}

//  void QQuick3DParticleAttractor::positionVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor24positionVariationChangedEv(
    QQuick3DParticleAttractor *self) {
  self->positionVariationChanged();
}

//  void QQuick3DParticleAttractor::shapeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor12shapeChangedEv(
    QQuick3DParticleAttractor *self) {
  self->shapeChanged();
}

//  void QQuick3DParticleAttractor::durationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor15durationChangedEv(
    QQuick3DParticleAttractor *self) {
  self->durationChanged();
}

//  void QQuick3DParticleAttractor::durationVariationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor24durationVariationChangedEv(
    QQuick3DParticleAttractor *self) {
  self->durationVariationChanged();
}

//  void QQuick3DParticleAttractor::hideAtEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor16hideAtEndChangedEv(
    QQuick3DParticleAttractor *self) {
  self->hideAtEndChanged();
}

//  void QQuick3DParticleAttractor::useCachedPositionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor25useCachedPositionsChangedEv(
    QQuick3DParticleAttractor *self) {
  self->useCachedPositionsChanged();
}

//  void QQuick3DParticleAttractor::positionsAmountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor22positionsAmountChangedEv(
    QQuick3DParticleAttractor *self) {
  self->positionsAmountChanged();
}

//  void QQuick3DParticleAttractor::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor15prepareToAffectEv(
    QQuick3DParticleAttractor *self) {
  self->prepareToAffect();
}

//  void QQuick3DParticleAttractor::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleAttractor *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticleAttractor::updateShapePositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuick3DParticleAttractor20updateShapePositionsEv(
    QQuick3DParticleAttractor *self) {
  self->updateShapePositions();
}

//  void QQuick3DParticleAttractor::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DParticleAttractor15prepareToAffectEv(
    QQuick3DParticleAttractor *self) {
  static_cast<OwnQQuick3DParticleAttractor *>(self)->OwnQQuick3DParticleAttractor::prepareToAffect();
}

//  void QQuick3DParticleAttractor::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuick3DParticleAttractor14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleAttractor *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticleAttractor *>(self)->OwnQQuick3DParticleAttractor::affectParticle(
      *sd,
      d,
      time);
}
