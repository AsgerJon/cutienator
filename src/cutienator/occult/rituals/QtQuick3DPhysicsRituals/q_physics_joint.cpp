//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qjoint_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qjoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPhysicsJoint that Python can take functions over in. Every QPhysicsJoint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPhysicsJointCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPhysicsJointCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPhysicsJointCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsJointCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsJointCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsJointCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsJointCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsJointCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPhysicsJoint : public QPhysicsJoint {
public:
  using QPhysicsJoint::QPhysicsJoint;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QPhysicsJoint18setJointPropertiesEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPhysicsJoint::setJointProperties()
  void setJointProperties() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPhysicsJointCall0 call = reinterpret_cast<CuteQPhysicsJointCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPhysicsJointCall1 call = reinterpret_cast<CuteQPhysicsJointCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPhysicsJointCall2 call = reinterpret_cast<CuteQPhysicsJointCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPhysicsJointCall3 call = reinterpret_cast<CuteQPhysicsJointCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPhysicsJointCall4 call = reinterpret_cast<CuteQPhysicsJointCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPhysicsJointCall5 call = reinterpret_cast<CuteQPhysicsJointCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPhysicsJointCall6 call = reinterpret_cast<CuteQPhysicsJointCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPhysicsJointCall7 call = reinterpret_cast<CuteQPhysicsJointCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPhysicsJoint::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPhysicsJoint10metaObjectEv(
    const QPhysicsJoint *self) {
  return self->metaObject();
}

//  void *QPhysicsJoint::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QPhysicsJoint11qt_metacastEPKc(
    QPhysicsJoint *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPhysicsJoint::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QPhysicsJoint11qt_metacallEN11QMetaObject4CallEiPPv(
    QPhysicsJoint *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPhysicsJoint::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPhysicsJoint2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPhysicsJoint::tr(s, c, n));
}

//  void QPhysicsJoint::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint24qt_qmlMarker_uncreatableEv(
    QPhysicsJoint *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QPhysicsJoint::~QPhysicsJoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJointD1Ev(QPhysicsJoint *self) {
  delete self;
}

//  QAbstractPhysicsBody *QPhysicsJoint::bodyA() const
extern "C" Q_DECL_EXPORT
QAbstractPhysicsBody *ritual_ZNK13QPhysicsJoint5bodyAEv(
    const QPhysicsJoint *self) {
  return self->bodyA();
}

//  void QPhysicsJoint::setBodyA(QAbstractPhysicsBody *newBodyA)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint8setBodyAEP20QAbstractPhysicsBody(
    QPhysicsJoint *self,
    QAbstractPhysicsBody *newBodyA) {
  self->setBodyA(newBodyA);
}

//  QAbstractPhysicsBody *QPhysicsJoint::bodyB() const
extern "C" Q_DECL_EXPORT
QAbstractPhysicsBody *ritual_ZNK13QPhysicsJoint5bodyBEv(
    const QPhysicsJoint *self) {
  return self->bodyB();
}

//  void QPhysicsJoint::setBodyB(QAbstractPhysicsBody *newBodyB)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint8setBodyBEP20QAbstractPhysicsBody(
    QPhysicsJoint *self,
    QAbstractPhysicsBody *newBodyB) {
  self->setBodyB(newBodyB);
}

//  QVector3D QPhysicsJoint::positionA() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QPhysicsJoint9positionAEv(const QPhysicsJoint *self) {
  return new QVector3D(self->positionA());
}

//  void QPhysicsJoint::setPositionA(const QVector3D &newPositionA)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint12setPositionAERK9QVector3D(
    QPhysicsJoint *self,
    const QVector3D *newPositionA) {
  self->setPositionA(*newPositionA);
}

//  QVector3D QPhysicsJoint::positionB() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QPhysicsJoint9positionBEv(const QPhysicsJoint *self) {
  return new QVector3D(self->positionB());
}

//  void QPhysicsJoint::setPositionB(const QVector3D &newPositionB)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint12setPositionBERK9QVector3D(
    QPhysicsJoint *self,
    const QVector3D *newPositionB) {
  self->setPositionB(*newPositionB);
}

//  QQuaternion QPhysicsJoint::orientationA() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK13QPhysicsJoint12orientationAEv(
    const QPhysicsJoint *self) {
  return new QQuaternion(self->orientationA());
}

//  void QPhysicsJoint::setOrientationA(const QQuaternion &newOrientationA)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint15setOrientationAERK11QQuaternion(
    QPhysicsJoint *self,
    const QQuaternion *newOrientationA) {
  self->setOrientationA(*newOrientationA);
}

//  QQuaternion QPhysicsJoint::orientationB() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK13QPhysicsJoint12orientationBEv(
    const QPhysicsJoint *self) {
  return new QQuaternion(self->orientationB());
}

//  void QPhysicsJoint::setOrientationB(const QQuaternion &newOrientationB)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint15setOrientationBERK11QQuaternion(
    QPhysicsJoint *self,
    const QQuaternion *newOrientationB) {
  self->setOrientationB(*newOrientationB);
}

//  void QPhysicsJoint::updatePhysXBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint18updatePhysXBackendEv(QPhysicsJoint *self) {
  self->updatePhysXBackend();
}

//  physx::PxJoint *QPhysicsJoint::getPhysXBackend() const
extern "C" Q_DECL_EXPORT
physx::PxJoint *ritual_ZNK13QPhysicsJoint15getPhysXBackendEv(
    const QPhysicsJoint *self) {
  return self->getPhysXBackend();
}

//  void QPhysicsJoint::bodyAChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint12bodyAChangedEv(QPhysicsJoint *self) {
  self->bodyAChanged();
}

//  void QPhysicsJoint::bodyBChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint12bodyBChangedEv(QPhysicsJoint *self) {
  self->bodyBChanged();
}

//  void QPhysicsJoint::positionAChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint16positionAChangedEv(QPhysicsJoint *self) {
  self->positionAChanged();
}

//  void QPhysicsJoint::positionBChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint16positionBChangedEv(QPhysicsJoint *self) {
  self->positionBChanged();
}

//  void QPhysicsJoint::orientationAChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint19orientationAChangedEv(QPhysicsJoint *self) {
  self->orientationAChanged();
}

//  void QPhysicsJoint::orientationBChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint19orientationBChangedEv(QPhysicsJoint *self) {
  self->orientationBChanged();
}

//  physx::PxJoint *QPhysicsJoint::createPhysxJoint(physx::PxRigidActor
//      *actorA, physx::PxRigidActor *actorB, const physx::PxTransform &trfA,
//      const physx::PxTransform &trfB)
extern "C" Q_DECL_EXPORT
physx::PxJoint *ritual_ZN13QPhysicsJoint16createPhysxJointEPN5physx12PxRigidActorES2_RKNS0_11PxTransformES5_(
    QPhysicsJoint *self,
    physx::PxRigidActor *actorA,
    physx::PxRigidActor *actorB,
    const physx::PxTransform *trfA,
    const physx::PxTransform *trfB) {
  return self->createPhysxJoint(actorA, actorB, *trfA, *trfB);
}

//  void QPhysicsJoint::setJointProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint18setJointPropertiesEv(QPhysicsJoint *self) {
  self->setJointProperties();
}

//  void QPhysicsJoint::onBodyDestroyed(QObject *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsJoint15onBodyDestroyedEP7QObject(
    QPhysicsJoint *self,
    QObject *body) {
  self->onBodyDestroyed(body);
}

//  a Python function taken by a CuteQPhysicsJoint, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPhysicsJoint(
    QPhysicsJoint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPhysicsJoint *>(self)->take(key, call);
}
