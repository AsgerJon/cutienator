//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelparticle_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelparticle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuick3DParticleModelParticle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleModelParticle : QQuick3DParticleModelParticle {
  using QQuick3DParticleModelParticle::componentComplete;
  using QQuick3DParticleModelParticle::itemChange;
  using QQuick3DParticleModelParticle::setDepthBias;
};

//  const QMetaObject *QQuick3DParticleModelParticle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DParticleModelParticle10metaObjectEv(
    const QQuick3DParticleModelParticle *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleModelParticle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuick3DParticleModelParticle11qt_metacastEPKc(
    QQuick3DParticleModelParticle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleModelParticle::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuick3DParticleModelParticle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleModelParticle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleModelParticle::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuick3DParticleModelParticle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleModelParticle::tr(s, c, n));
}

//  QQuick3DParticleModelParticle::QQuick3DParticleModelParticle(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelParticle *ritual_ZN29QQuick3DParticleModelParticleC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleModelParticle(parent);
}

//  QQmlComponent *QQuick3DParticleModelParticle::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK29QQuick3DParticleModelParticle8delegateEv(
    const QQuick3DParticleModelParticle *self) {
  return self->delegate();
}

//  QQuick3DInstancing *QQuick3DParticleModelParticle::instanceTable() const
extern "C" Q_DECL_EXPORT
QQuick3DInstancing *ritual_ZNK29QQuick3DParticleModelParticle13instanceTableEv(
    const QQuick3DParticleModelParticle *self) {
  return self->instanceTable();
}

//  void QQuick3DParticleModelParticle::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle11setDelegateEP13QQmlComponent(
    QQuick3DParticleModelParticle *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  void QQuick3DParticleModelParticle::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle15delegateChangedEv(
    QQuick3DParticleModelParticle *self) {
  self->delegateChanged();
}

//  void QQuick3DParticleModelParticle::instanceTableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle20instanceTableChangedEv(
    QQuick3DParticleModelParticle *self) {
  self->instanceTableChanged();
}

//  void QQuick3DParticleModelParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle17componentCompleteEv(
    QQuick3DParticleModelParticle *self) {
  self->componentComplete();
}

//  void QQuick3DParticleModelParticle::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleModelParticle *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuick3DParticleModelParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle12setDepthBiasEf(
    QQuick3DParticleModelParticle *self,
    float bias) {
  self->setDepthBias(bias);
}

//  void QQuick3DParticleModelParticle::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle10regenerateEv(
    QQuick3DParticleModelParticle *self) {
  self->regenerate();
}

//  void QQuick3DParticleModelParticle::handleMaxAmountChanged(int amount)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle22handleMaxAmountChangedEi(
    QQuick3DParticleModelParticle *self,
    int amount) {
  self->handleMaxAmountChanged(amount);
}

//  void QQuick3DParticleModelParticle::handleSortModeChanged(QQuick3DParticl
//      e::SortMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle21handleSortModeChangedEN16QQuick3DParticle8SortModeE(
    QQuick3DParticleModelParticle *self,
    QQuick3DParticle::SortMode mode) {
  self->handleSortModeChanged(mode);
}

//  void QQuick3DParticleModelParticle::clearInstanceTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle18clearInstanceTableEv(
    QQuick3DParticleModelParticle *self) {
  self->clearInstanceTable();
}

//  void QQuick3DParticleModelParticle::addInstance(const QVector3D
//      &position, const QVector3D &scale, const QVector3D &eulerRotation,
//      const QColor &color, float age)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle11addInstanceERK9QVector3DS2_S2_RK6QColorf(
    QQuick3DParticleModelParticle *self,
    const QVector3D *position,
    const QVector3D *scale,
    const QVector3D *eulerRotation,
    const QColor *color,
    float age) {
  self->addInstance(*position, *scale, *eulerRotation, *color, age);
}

//  void QQuick3DParticleModelParticle::commitInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle14commitInstanceEv(
    QQuick3DParticleModelParticle *self) {
  self->commitInstance();
}

//  void QQuick3DParticleModelParticle::updateDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleModelParticle15updateDepthBiasEf(
    QQuick3DParticleModelParticle *self,
    float bias) {
  self->updateDepthBias(bias);
}

//  void QQuick3DParticleModelParticle::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleModelParticle17componentCompleteEv(
    QQuick3DParticleModelParticle *self) {
  static_cast<OwnQQuick3DParticleModelParticle *>(self)->OwnQQuick3DParticleModelParticle::componentComplete();
}

//  void QQuick3DParticleModelParticle::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleModelParticle10itemChangeEN14QQuick3DObject10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DParticleModelParticle *self,
    QQuick3DObject::ItemChange change,
    const QQuick3DObject::ItemChangeData *value) {
  static_cast<OwnQQuick3DParticleModelParticle *>(self)->OwnQQuick3DParticleModelParticle::itemChange(
      change,
      *value);
}

//  void QQuick3DParticleModelParticle::setDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleModelParticle12setDepthBiasEf(
    QQuick3DParticleModelParticle *self,
    float bias) {
  static_cast<OwnQQuick3DParticleModelParticle *>(self)->OwnQQuick3DParticleModelParticle::setDepthBias(
      bias);
}
