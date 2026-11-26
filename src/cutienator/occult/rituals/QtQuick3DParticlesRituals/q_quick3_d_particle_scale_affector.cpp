//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlescaleaffector_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlescaleaffector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(easingcurve)
#include <QtCore/qeasingcurve.h>
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleScaleAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleScaleAffector : QQuick3DParticleScaleAffector {
  using QQuick3DParticleScaleAffector::prepareToAffect;
  using QQuick3DParticleScaleAffector::affectParticle;
};

//  const QMetaObject *QQuick3DParticleScaleAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DParticleScaleAffector10metaObjectEv(
    const QQuick3DParticleScaleAffector *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleScaleAffector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuick3DParticleScaleAffector11qt_metacastEPKc(
    QQuick3DParticleScaleAffector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleScaleAffector::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuick3DParticleScaleAffector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleScaleAffector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleScaleAffector::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuick3DParticleScaleAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleScaleAffector::tr(s, c, n));
}

//  QQuick3DParticleScaleAffector::QQuick3DParticleScaleAffector(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleScaleAffector *ritual_ZN29QQuick3DParticleScaleAffectorC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleScaleAffector(parent);
}

//  float QQuick3DParticleScaleAffector::minSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QQuick3DParticleScaleAffector7minSizeEv(
    const QQuick3DParticleScaleAffector *self) {
  return self->minSize();
}

//  float QQuick3DParticleScaleAffector::maxSize() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK29QQuick3DParticleScaleAffector7maxSizeEv(
    const QQuick3DParticleScaleAffector *self) {
  return self->maxSize();
}

//  int QQuick3DParticleScaleAffector::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuick3DParticleScaleAffector8durationEv(
    const QQuick3DParticleScaleAffector *self) {
  return self->duration();
}

//  ScalingType QQuick3DParticleScaleAffector::type() const
extern "C" Q_DECL_EXPORT
QQuick3DParticleScaleAffector::ScalingType ritual_ZNK29QQuick3DParticleScaleAffector4typeEv(
    const QQuick3DParticleScaleAffector *self) {
  return self->type();
}

//  QEasingCurve QQuick3DParticleScaleAffector::easingCurve() const
extern "C" Q_DECL_EXPORT
QEasingCurve *ritual_ZNK29QQuick3DParticleScaleAffector11easingCurveEv(
    const QQuick3DParticleScaleAffector *self) {
  return new QEasingCurve(self->easingCurve());
}

//  void QQuick3DParticleScaleAffector::setMinSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector10setMinSizeEf(
    QQuick3DParticleScaleAffector *self,
    float size) {
  self->setMinSize(size);
}

//  void QQuick3DParticleScaleAffector::setMaxSize(float size)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector10setMaxSizeEf(
    QQuick3DParticleScaleAffector *self,
    float size) {
  self->setMaxSize(size);
}

//  void QQuick3DParticleScaleAffector::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector11setDurationEi(
    QQuick3DParticleScaleAffector *self,
    int duration) {
  self->setDuration(duration);
}

//  void QQuick3DParticleScaleAffector::setType(ScalingType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector7setTypeENS_11ScalingTypeE(
    QQuick3DParticleScaleAffector *self,
    QQuick3DParticleScaleAffector::ScalingType type) {
  self->setType(type);
}

//  void QQuick3DParticleScaleAffector::setEasingCurve(const QEasingCurve
//      &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector14setEasingCurveERK12QEasingCurve(
    QQuick3DParticleScaleAffector *self,
    const QEasingCurve *curve) {
  self->setEasingCurve(*curve);
}

//  void QQuick3DParticleScaleAffector::minSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector14minSizeChangedEv(
    QQuick3DParticleScaleAffector *self) {
  self->minSizeChanged();
}

//  void QQuick3DParticleScaleAffector::maxSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector14maxSizeChangedEv(
    QQuick3DParticleScaleAffector *self) {
  self->maxSizeChanged();
}

//  void QQuick3DParticleScaleAffector::durationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector15durationChangedEv(
    QQuick3DParticleScaleAffector *self) {
  self->durationChanged();
}

//  void QQuick3DParticleScaleAffector::typeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector11typeChangedEv(
    QQuick3DParticleScaleAffector *self) {
  self->typeChanged();
}

//  void QQuick3DParticleScaleAffector::easingCurveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector18easingCurveChangedEv(
    QQuick3DParticleScaleAffector *self) {
  self->easingCurveChanged();
}

//  void QQuick3DParticleScaleAffector::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector15prepareToAffectEv(
    QQuick3DParticleScaleAffector *self) {
  self->prepareToAffect();
}

//  void QQuick3DParticleScaleAffector::affectParticle(const
//      QQuick3DParticleData &a0, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleScaleAffector14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleScaleAffector *self,
    const QQuick3DParticleData *a0,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*a0, d, time);
}

//  void QQuick3DParticleScaleAffector::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleScaleAffector15prepareToAffectEv(
    QQuick3DParticleScaleAffector *self) {
  static_cast<OwnQQuick3DParticleScaleAffector *>(self)->OwnQQuick3DParticleScaleAffector::prepareToAffect();
}

//  void QQuick3DParticleScaleAffector::affectParticle(const
//      QQuick3DParticleData &a0, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleScaleAffector14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleScaleAffector *self,
    const QQuick3DParticleData *a0,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticleScaleAffector *>(self)->OwnQQuick3DParticleScaleAffector::affectParticle(
      *a0,
      d,
      time);
}
