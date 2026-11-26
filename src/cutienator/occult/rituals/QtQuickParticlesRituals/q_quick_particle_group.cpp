//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlegroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlegroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

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

//  void *QQuickParticleGroup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickParticleGroup11qt_metacastEPKc(
    QQuickParticleGroup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParticleGroup::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickParticleGroup11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParticleGroup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QObject> QQuickParticleGroup::particleChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN19QQuickParticleGroup16particleChildrenEv(
    QQuickParticleGroup *self) {
  return new QQmlListProperty<QObject>(self->particleChildren());
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

//  void QQuickParticleGroup::systemChanged(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickParticleGroup13systemChangedEP20QQuickParticleSystem(
    QQuickParticleGroup *self,
    QQuickParticleSystem *arg) {
  self->systemChanged(arg);
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

//  a QQmlListProperty<QObject> a ritual of QQuickParticleGroup gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickParticleGroup__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
