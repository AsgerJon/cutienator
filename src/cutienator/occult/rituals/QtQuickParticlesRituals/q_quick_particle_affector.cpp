//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticleaffector_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticleaffector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  Only a class built on QQuickParticleAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticleAffector : QQuickParticleAffector {
  using QQuickParticleAffector::affectParticle;
  using QQuickParticleAffector::componentComplete;
};

//  const QMetaObject *QQuickParticleAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickParticleAffector10metaObjectEv(
    const QQuickParticleAffector *self) {
  return self->metaObject();
}

//  QString QQuickParticleAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickParticleAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleAffector::tr(s, c, n));
}

//  void QQuickParticleAffector::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector24qt_qmlMarker_uncreatableEv(
    QQuickParticleAffector *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickParticleAffector::QQuickParticleAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickParticleAffector *ritual_ZN22QQuickParticleAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickParticleAffector(parent);
}

//  void QQuickParticleAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector12affectSystemEd(
    QQuickParticleAffector *self,
    qreal dt) {
  self->affectSystem(dt);
}

//  void QQuickParticleAffector::reset(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector5resetEP18QQuickParticleData(
    QQuickParticleAffector *self,
    QQuickParticleData *a0) {
  self->reset(a0);
}

//  QQuickParticleSystem *QQuickParticleAffector::system() const
extern "C" Q_DECL_EXPORT
QQuickParticleSystem *ritual_ZNK22QQuickParticleAffector6systemEv(
    const QQuickParticleAffector *self) {
  return self->system();
}

//  QStringList QQuickParticleAffector::groups() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QQuickParticleAffector6groupsEv(
    const QQuickParticleAffector *self) {
  return new QList<QString>(self->groups());
}

//  bool QQuickParticleAffector::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickParticleAffector7enabledEv(
    const QQuickParticleAffector *self) {
  return self->enabled();
}

//  bool QQuickParticleAffector::onceOff() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickParticleAffector7onceOffEv(
    const QQuickParticleAffector *self) {
  return self->onceOff();
}

//  QQuickParticleExtruder *QQuickParticleAffector::shape() const
extern "C" Q_DECL_EXPORT
QQuickParticleExtruder *ritual_ZNK22QQuickParticleAffector5shapeEv(
    const QQuickParticleAffector *self) {
  return self->shape();
}

//  QStringList QQuickParticleAffector::whenCollidingWith() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QQuickParticleAffector17whenCollidingWithEv(
    const QQuickParticleAffector *self) {
  return new QList<QString>(self->whenCollidingWith());
}

//  void QQuickParticleAffector::setSystem(QQuickParticleSystem *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector9setSystemEP20QQuickParticleSystem(
    QQuickParticleAffector *self,
    QQuickParticleSystem *arg) {
  self->setSystem(arg);
}

//  void QQuickParticleAffector::setGroups(const QStringList &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector9setGroupsERK5QListI7QStringE(
    QQuickParticleAffector *self,
    const QList<QString> *arg) {
  self->setGroups(*arg);
}

//  void QQuickParticleAffector::setEnabled(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector10setEnabledEb(
    QQuickParticleAffector *self,
    bool arg) {
  self->setEnabled(arg);
}

//  void QQuickParticleAffector::setOnceOff(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector10setOnceOffEb(
    QQuickParticleAffector *self,
    bool arg) {
  self->setOnceOff(arg);
}

//  void QQuickParticleAffector::setShape(QQuickParticleExtruder *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector8setShapeEP22QQuickParticleExtruder(
    QQuickParticleAffector *self,
    QQuickParticleExtruder *arg) {
  self->setShape(arg);
}

//  void QQuickParticleAffector::setWhenCollidingWith(const QStringList &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector20setWhenCollidingWithERK5QListI7QStringE(
    QQuickParticleAffector *self,
    const QList<QString> *arg) {
  self->setWhenCollidingWith(*arg);
}

//  void QQuickParticleAffector::updateOffsets()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector13updateOffsetsEv(
    QQuickParticleAffector *self) {
  self->updateOffsets();
}

//  bool QQuickParticleAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticleDatad(
    QQuickParticleAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  bool QQuickParticleAffector::activeGroup(int g)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleAffector11activeGroupEi(
    QQuickParticleAffector *self,
    int g) {
  return self->activeGroup(g);
}

//  bool QQuickParticleAffector::shouldAffect(QQuickParticleData *datum)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleAffector12shouldAffectEP18QQuickParticleData(
    QQuickParticleAffector *self,
    QQuickParticleData *datum) {
  return self->shouldAffect(datum);
}

//  void QQuickParticleAffector::postAffect(QQuickParticleData *datum)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector10postAffectEP18QQuickParticleData(
    QQuickParticleAffector *self,
    QQuickParticleData *datum) {
  self->postAffect(datum);
}

//  void QQuickParticleAffector::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleAffector17componentCompleteEv(
    QQuickParticleAffector *self) {
  self->componentComplete();
}

//  bool QQuickParticleAffector::isAffectedConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleAffector19isAffectedConnectedEv(
    QQuickParticleAffector *self) {
  return self->isAffectedConnected();
}

//  bool QQuickParticleAffector::isColliding(QQuickParticleData *d) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickParticleAffector11isCollidingEP18QQuickParticleData(
    const QQuickParticleAffector *self,
    QQuickParticleData *d) {
  return self->isColliding(d);
}

//  void QQuickParticleAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickParticleAffector12affectSystemEd(
    QQuickParticleAffector *self,
    qreal dt) {
  self->QQuickParticleAffector::affectSystem(dt);
}

//  void QQuickParticleAffector::reset(QQuickParticleData *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickParticleAffector5resetEP18QQuickParticleData(
    QQuickParticleAffector *self,
    QQuickParticleData *a0) {
  self->QQuickParticleAffector::reset(a0);
}

//  bool QQuickParticleAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickParticleAffector14affectParticleEP18QQuickParticleDatad(
    QQuickParticleAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickParticleAffector *>(self)->OwnQQuickParticleAffector::affectParticle(
      d,
      dt);
}

//  void QQuickParticleAffector::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickParticleAffector17componentCompleteEv(
    QQuickParticleAffector *self) {
  static_cast<OwnQQuickParticleAffector *>(self)->OwnQQuickParticleAffector::componentComplete();
}
