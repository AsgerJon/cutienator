//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlewander_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlewander_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleWander may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleWander : QQuick3DParticleWander {
  using QQuick3DParticleWander::affectParticle;
};

//  const QMetaObject *QQuick3DParticleWander::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DParticleWander10metaObjectEv(
    const QQuick3DParticleWander *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleWander::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DParticleWander2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleWander::tr(s, c, n));
}

//  QQuick3DParticleWander::QQuick3DParticleWander(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleWander *ritual_ZN22QQuick3DParticleWanderC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleWander(parent);
}

//  const QVector3D &QQuick3DParticleWander::globalAmount() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK22QQuick3DParticleWander12globalAmountEv(
    const QQuick3DParticleWander *self) {
  return new QVector3D(self->globalAmount());
}

//  const QVector3D &QQuick3DParticleWander::globalPace() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK22QQuick3DParticleWander10globalPaceEv(
    const QQuick3DParticleWander *self) {
  return new QVector3D(self->globalPace());
}

//  const QVector3D &QQuick3DParticleWander::globalPaceStart() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK22QQuick3DParticleWander15globalPaceStartEv(
    const QQuick3DParticleWander *self) {
  return new QVector3D(self->globalPaceStart());
}

//  const QVector3D &QQuick3DParticleWander::uniqueAmount() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK22QQuick3DParticleWander12uniqueAmountEv(
    const QQuick3DParticleWander *self) {
  return new QVector3D(self->uniqueAmount());
}

//  const QVector3D &QQuick3DParticleWander::uniquePace() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK22QQuick3DParticleWander10uniquePaceEv(
    const QQuick3DParticleWander *self) {
  return new QVector3D(self->uniquePace());
}

//  float QQuick3DParticleWander::uniqueAmountVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QQuick3DParticleWander21uniqueAmountVariationEv(
    const QQuick3DParticleWander *self) {
  return self->uniqueAmountVariation();
}

//  float QQuick3DParticleWander::uniquePaceVariation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QQuick3DParticleWander19uniquePaceVariationEv(
    const QQuick3DParticleWander *self) {
  return self->uniquePaceVariation();
}

//  int QQuick3DParticleWander::fadeInDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleWander14fadeInDurationEv(
    const QQuick3DParticleWander *self) {
  return self->fadeInDuration();
}

//  int QQuick3DParticleWander::fadeOutDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleWander15fadeOutDurationEv(
    const QQuick3DParticleWander *self) {
  return self->fadeOutDuration();
}

//  void QQuick3DParticleWander::setGlobalAmount(const QVector3D
//      &globalAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander15setGlobalAmountERK9QVector3D(
    QQuick3DParticleWander *self,
    const QVector3D *globalAmount) {
  self->setGlobalAmount(*globalAmount);
}

//  void QQuick3DParticleWander::setGlobalPace(const QVector3D &globalPace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander13setGlobalPaceERK9QVector3D(
    QQuick3DParticleWander *self,
    const QVector3D *globalPace) {
  self->setGlobalPace(*globalPace);
}

//  void QQuick3DParticleWander::setGlobalPaceStart(const QVector3D
//      &globalPaceStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander18setGlobalPaceStartERK9QVector3D(
    QQuick3DParticleWander *self,
    const QVector3D *globalPaceStart) {
  self->setGlobalPaceStart(*globalPaceStart);
}

//  void QQuick3DParticleWander::setUniqueAmount(const QVector3D
//      &uniqueAmount)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander15setUniqueAmountERK9QVector3D(
    QQuick3DParticleWander *self,
    const QVector3D *uniqueAmount) {
  self->setUniqueAmount(*uniqueAmount);
}

//  void QQuick3DParticleWander::setUniquePace(const QVector3D &uniquePace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander13setUniquePaceERK9QVector3D(
    QQuick3DParticleWander *self,
    const QVector3D *uniquePace) {
  self->setUniquePace(*uniquePace);
}

//  void QQuick3DParticleWander::setUniqueAmountVariation(float
//      uniqueAmountVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander24setUniqueAmountVariationEf(
    QQuick3DParticleWander *self,
    float uniqueAmountVariation) {
  self->setUniqueAmountVariation(uniqueAmountVariation);
}

//  void QQuick3DParticleWander::setUniquePaceVariation(float
//      uniquePaceVariation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander22setUniquePaceVariationEf(
    QQuick3DParticleWander *self,
    float uniquePaceVariation) {
  self->setUniquePaceVariation(uniquePaceVariation);
}

//  void QQuick3DParticleWander::setFadeInDuration(int fadeInDuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander17setFadeInDurationEi(
    QQuick3DParticleWander *self,
    int fadeInDuration) {
  self->setFadeInDuration(fadeInDuration);
}

//  void QQuick3DParticleWander::setFadeOutDuration(int fadeOutDuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander18setFadeOutDurationEi(
    QQuick3DParticleWander *self,
    int fadeOutDuration) {
  self->setFadeOutDuration(fadeOutDuration);
}

//  void QQuick3DParticleWander::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleWander14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleWander *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticleWander::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DParticleWander14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleWander *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticleWander *>(self)->OwnQQuick3DParticleWander::affectParticle(
      *sd,
      d,
      time);
}
