//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QPhysicsMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPhysicsMaterial10metaObjectEv(
    const QPhysicsMaterial *self) {
  return self->metaObject();
}

//  void *QPhysicsMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QPhysicsMaterial11qt_metacastEPKc(
    QPhysicsMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPhysicsMaterial::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QPhysicsMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    QPhysicsMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPhysicsMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPhysicsMaterial2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPhysicsMaterial::tr(s, c, n));
}

//  QPhysicsMaterial::QPhysicsMaterial(QObject *parent)
extern "C" Q_DECL_EXPORT
QPhysicsMaterial *ritual_ZN16QPhysicsMaterialC1EP7QObject(QObject *parent) {
  return new QPhysicsMaterial(parent);
}

//  float QPhysicsMaterial::staticFriction() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QPhysicsMaterial14staticFrictionEv(
    const QPhysicsMaterial *self) {
  return self->staticFriction();
}

//  void QPhysicsMaterial::setStaticFriction(float staticFriction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial17setStaticFrictionEf(
    QPhysicsMaterial *self,
    float staticFriction) {
  self->setStaticFriction(staticFriction);
}

//  float QPhysicsMaterial::dynamicFriction() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QPhysicsMaterial15dynamicFrictionEv(
    const QPhysicsMaterial *self) {
  return self->dynamicFriction();
}

//  void QPhysicsMaterial::setDynamicFriction(float dynamicFriction)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial18setDynamicFrictionEf(
    QPhysicsMaterial *self,
    float dynamicFriction) {
  self->setDynamicFriction(dynamicFriction);
}

//  float QPhysicsMaterial::restitution() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QPhysicsMaterial11restitutionEv(
    const QPhysicsMaterial *self) {
  return self->restitution();
}

//  void QPhysicsMaterial::setRestitution(float restitution)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial14setRestitutionEf(
    QPhysicsMaterial *self,
    float restitution) {
  self->setRestitution(restitution);
}

//  void QPhysicsMaterial::staticFrictionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial21staticFrictionChangedEv(
    QPhysicsMaterial *self) {
  self->staticFrictionChanged();
}

//  void QPhysicsMaterial::dynamicFrictionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial22dynamicFrictionChangedEv(
    QPhysicsMaterial *self) {
  self->dynamicFrictionChanged();
}

//  void QPhysicsMaterial::restitutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPhysicsMaterial18restitutionChangedEv(
    QPhysicsMaterial *self) {
  self->restitutionChanged();
}
