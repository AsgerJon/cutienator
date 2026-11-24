//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlegroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlegroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickParticleGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticleGroup : QQuickParticleGroup {
  using QQuickParticleGroup::componentComplete;
  using QQuickParticleGroup::classBegin;
};

//  const QMetaObject *QQuickParticleGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickParticleGroup10metaObjectEv(
    const QQuickParticleGroup *self) {
  return self->metaObject();
}

//  QString QQuickParticleGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickParticleGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleGroup::tr(s, c, n));
}

//  QQuickParticleGroup::QQuickParticleGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickParticleGroup *ritual_ZN19QQuickParticleGroupC1EP7QObject(
    QObject *parent) {
  return new QQuickParticleGroup(parent);
}

//  QQuickParticleSystem *QQuickParticleGroup::system() const
extern "C" Q_DECL_EXPORT
QQuickParticleSystem *ritual_ZNK19QQuickParticleGroup6systemEv(
    const QQuickParticleGroup *self) {
  return self->system();
}

//  void QQuickParticleGroup::setSystem(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup9setSystemEP20QQuickParticleSystem(
    QQuickParticleGroup *self,
    QQuickParticleSystem *arg) {
  self->setSystem(arg);
}

//  void QQuickParticleGroup::delayRedirect(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup13delayRedirectEP7QObject(
    QQuickParticleGroup *self,
    QObject *obj) {
  self->delayRedirect(obj);
}

//  void QQuickParticleGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup17componentCompleteEv(
    QQuickParticleGroup *self) {
  self->componentComplete();
}

//  void QQuickParticleGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup10classBeginEv(
    QQuickParticleGroup *self) {
  self->classBegin();
}

//  void QQuickParticleGroup::performDelayedRedirects()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup23performDelayedRedirectsEv(
    QQuickParticleGroup *self) {
  self->performDelayedRedirects();
}

//  QQuickParticleGroup as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickParticleGroup_QQmlParserStatus(
    QQuickParticleGroup *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQuickParticleGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickParticleGroup17componentCompleteEv(
    QQuickParticleGroup *self) {
  static_cast<OwnQQuickParticleGroup *>(self)->OwnQQuickParticleGroup::componentComplete();
}

//  void QQuickParticleGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickParticleGroup10classBeginEv(
    QQuickParticleGroup *self) {
  static_cast<OwnQQuickParticleGroup *>(self)->OwnQQuickParticleGroup::classBegin();
}
