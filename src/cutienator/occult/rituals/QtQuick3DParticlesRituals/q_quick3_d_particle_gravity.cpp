//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlegravity_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlegravity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleGravity may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleGravity : QQuick3DParticleGravity {
  using QQuick3DParticleGravity::affectParticle;
};

//  const QMetaObject *QQuick3DParticleGravity::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DParticleGravity10metaObjectEv(
    const QQuick3DParticleGravity *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleGravity::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuick3DParticleGravity11qt_metacastEPKc(
    QQuick3DParticleGravity *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleGravity::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuick3DParticleGravity11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleGravity *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleGravity::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DParticleGravity2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleGravity::tr(s, c, n));
}

//  QQuick3DParticleGravity::QQuick3DParticleGravity(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleGravity *ritual_ZN23QQuick3DParticleGravityC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleGravity(parent);
}

//  float QQuick3DParticleGravity::magnitude() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK23QQuick3DParticleGravity9magnitudeEv(
    const QQuick3DParticleGravity *self) {
  return self->magnitude();
}

//  const QVector3D &QQuick3DParticleGravity::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuick3DParticleGravity9directionEv(
    const QQuick3DParticleGravity *self) {
  return new QVector3D(self->direction());
}

//  void QQuick3DParticleGravity::setDirection(const QVector3D &direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleGravity12setDirectionERK9QVector3D(
    QQuick3DParticleGravity *self,
    const QVector3D *direction) {
  self->setDirection(*direction);
}

//  void QQuick3DParticleGravity::setMagnitude(float magnitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleGravity12setMagnitudeEf(
    QQuick3DParticleGravity *self,
    float magnitude) {
  self->setMagnitude(magnitude);
}

//  void QQuick3DParticleGravity::magnitudeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleGravity16magnitudeChangedEv(
    QQuick3DParticleGravity *self) {
  self->magnitudeChanged();
}

//  void QQuick3DParticleGravity::directionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleGravity16directionChangedEv(
    QQuick3DParticleGravity *self) {
  self->directionChanged();
}

//  void QQuick3DParticleGravity::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DParticleGravity14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleGravity *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticleGravity::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQuick3DParticleGravity14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleGravity *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticleGravity *>(self)->OwnQQuick3DParticleGravity::affectParticle(
      *sd,
      d,
      time);
}
