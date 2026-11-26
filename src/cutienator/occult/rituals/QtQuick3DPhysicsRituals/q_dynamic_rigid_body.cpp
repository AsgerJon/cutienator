//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qdynamicrigidbody_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qdynamicrigidbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  A QDynamicRigidBody that Python can take functions over in. Every QDynamicRigidBody
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDynamicRigidBodyCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall3)(const void *, int *);
typedef void * (*CuteQDynamicRigidBodyCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQDynamicRigidBodyCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQDynamicRigidBodyCall6)(const void *, int *);
typedef void (*CuteQDynamicRigidBodyCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDynamicRigidBodyCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDynamicRigidBodyCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDynamicRigidBodyCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDynamicRigidBody : public QDynamicRigidBody {
public:
  using QDynamicRigidBody::QDynamicRigidBody;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall0 call = reinterpret_cast<CuteQDynamicRigidBodyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall1 call = reinterpret_cast<CuteQDynamicRigidBodyCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall2 call = reinterpret_cast<CuteQDynamicRigidBodyCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DNode::componentComplete()
  void componentComplete() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall3 call = reinterpret_cast<CuteQDynamicRigidBodyCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::componentComplete();
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall4 call = reinterpret_cast<CuteQDynamicRigidBodyCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall5 call = reinterpret_cast<CuteQDynamicRigidBodyCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall6 call = reinterpret_cast<CuteQDynamicRigidBodyCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall7 call = reinterpret_cast<CuteQDynamicRigidBodyCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall8 call = reinterpret_cast<CuteQDynamicRigidBodyCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall9 call = reinterpret_cast<CuteQDynamicRigidBodyCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall10 call = reinterpret_cast<CuteQDynamicRigidBodyCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall11 call = reinterpret_cast<CuteQDynamicRigidBodyCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDynamicRigidBodyCall12 call = reinterpret_cast<CuteQDynamicRigidBodyCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDynamicRigidBody::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDynamicRigidBody10metaObjectEv(
    const QDynamicRigidBody *self) {
  return self->metaObject();
}

//  void *QDynamicRigidBody::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QDynamicRigidBody11qt_metacastEPKc(
    QDynamicRigidBody *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDynamicRigidBody::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QDynamicRigidBody11qt_metacallEN11QMetaObject4CallEiPPv(
    QDynamicRigidBody *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDynamicRigidBody::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDynamicRigidBody2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDynamicRigidBody::tr(s, c, n));
}

//  QDynamicRigidBody::QDynamicRigidBody()
extern "C" Q_DECL_EXPORT
QDynamicRigidBody *ritual_ZN17QDynamicRigidBodyC1Ev() {
  return new CuteQDynamicRigidBody();
}

//  QDynamicRigidBody::~QDynamicRigidBody()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBodyD1Ev(QDynamicRigidBody *self) {
  delete self;
}

//  float QDynamicRigidBody::mass() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QDynamicRigidBody4massEv(const QDynamicRigidBody *self) {
  return self->mass();
}

//  void QDynamicRigidBody::setMass(float mass)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody7setMassEf(
    QDynamicRigidBody *self,
    float mass) {
  self->setMass(mass);
}

//  float QDynamicRigidBody::density() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QDynamicRigidBody7densityEv(
    const QDynamicRigidBody *self) {
  return self->density();
}

//  void QDynamicRigidBody::setDensity(float density)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody10setDensityEf(
    QDynamicRigidBody *self,
    float density) {
  self->setDensity(density);
}

//  bool QDynamicRigidBody::isKinematic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDynamicRigidBody11isKinematicEv(
    const QDynamicRigidBody *self) {
  return self->isKinematic();
}

//  void QDynamicRigidBody::setIsKinematic(bool isKinematic)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody14setIsKinematicEb(
    QDynamicRigidBody *self,
    bool isKinematic) {
  self->setIsKinematic(isKinematic);
}

//  AxisLock QDynamicRigidBody::linearAxisLock() const
extern "C" Q_DECL_EXPORT
QDynamicRigidBody::AxisLock ritual_ZNK17QDynamicRigidBody14linearAxisLockEv(
    const QDynamicRigidBody *self) {
  return self->linearAxisLock();
}

//  void QDynamicRigidBody::setLinearAxisLock(AxisLock newAxisLockLinear)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17setLinearAxisLockENS_8AxisLockE(
    QDynamicRigidBody *self,
    QDynamicRigidBody::AxisLock newAxisLockLinear) {
  self->setLinearAxisLock(newAxisLockLinear);
}

//  AxisLock QDynamicRigidBody::angularAxisLock() const
extern "C" Q_DECL_EXPORT
QDynamicRigidBody::AxisLock ritual_ZNK17QDynamicRigidBody15angularAxisLockEv(
    const QDynamicRigidBody *self) {
  return self->angularAxisLock();
}

//  void QDynamicRigidBody::setAngularAxisLock(AxisLock newAxisLockAngular)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody18setAngularAxisLockENS_8AxisLockE(
    QDynamicRigidBody *self,
    QDynamicRigidBody::AxisLock newAxisLockAngular) {
  self->setAngularAxisLock(newAxisLockAngular);
}

//  bool QDynamicRigidBody::gravityEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDynamicRigidBody14gravityEnabledEv(
    const QDynamicRigidBody *self) {
  return self->gravityEnabled();
}

//  void QDynamicRigidBody::setGravityEnabled(bool gravityEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17setGravityEnabledEb(
    QDynamicRigidBody *self,
    bool gravityEnabled) {
  self->setGravityEnabled(gravityEnabled);
}

//  void QDynamicRigidBody::applyCentralForce(const QVector3D &force)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17applyCentralForceERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *force) {
  self->applyCentralForce(*force);
}

//  void QDynamicRigidBody::applyForce(const QVector3D &force, const
//      QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody10applyForceERK9QVector3DS2_(
    QDynamicRigidBody *self,
    const QVector3D *force,
    const QVector3D *position) {
  self->applyForce(*force, *position);
}

//  void QDynamicRigidBody::applyTorque(const QVector3D &torque)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody11applyTorqueERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *torque) {
  self->applyTorque(*torque);
}

//  void QDynamicRigidBody::applyCentralImpulse(const QVector3D &impulse)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody19applyCentralImpulseERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *impulse) {
  self->applyCentralImpulse(*impulse);
}

//  void QDynamicRigidBody::applyImpulse(const QVector3D &impulse, const
//      QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody12applyImpulseERK9QVector3DS2_(
    QDynamicRigidBody *self,
    const QVector3D *impulse,
    const QVector3D *position) {
  self->applyImpulse(*impulse, *position);
}

//  void QDynamicRigidBody::applyTorqueImpulse(const QVector3D &impulse)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody18applyTorqueImpulseERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *impulse) {
  self->applyTorqueImpulse(*impulse);
}

//  void QDynamicRigidBody::setAngularVelocity(const QVector3D
//      &angularVelocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody18setAngularVelocityERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *angularVelocity) {
  self->setAngularVelocity(*angularVelocity);
}

//  void QDynamicRigidBody::setLinearVelocity(const QVector3D
//      &linearVelocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17setLinearVelocityERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *linearVelocity) {
  self->setLinearVelocity(*linearVelocity);
}

//  void QDynamicRigidBody::reset(const QVector3D &position, const QVector3D
//      &eulerRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody5resetERK9QVector3DS2_(
    QDynamicRigidBody *self,
    const QVector3D *position,
    const QVector3D *eulerRotation) {
  self->reset(*position, *eulerRotation);
}

//  QQueue<QPhysicsCommand *> &QDynamicRigidBody::commandQueue()
extern "C" Q_DECL_EXPORT
QQueue<QPhysicsCommand *> *ritual_ZN17QDynamicRigidBody12commandQueueEv(
    QDynamicRigidBody *self) {
  return &(self->commandQueue());
}

//  void QDynamicRigidBody::updateDefaultDensity(float defaultDensity)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody20updateDefaultDensityEf(
    QDynamicRigidBody *self,
    float defaultDensity) {
  self->updateDefaultDensity(defaultDensity);
}

//  MassMode QDynamicRigidBody::massMode() const
extern "C" Q_DECL_EXPORT
QDynamicRigidBody::MassMode ritual_ZNK17QDynamicRigidBody8massModeEv(
    const QDynamicRigidBody *self) {
  return self->massMode();
}

//  void QDynamicRigidBody::setMassMode(const MassMode newMassMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody11setMassModeENS_8MassModeE(
    QDynamicRigidBody *self,
    const QDynamicRigidBody::MassMode *newMassMode) {
  self->setMassMode(*newMassMode);
}

//  const QVector3D &QDynamicRigidBody::inertiaTensor() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QDynamicRigidBody13inertiaTensorEv(
    const QDynamicRigidBody *self) {
  return new QVector3D(self->inertiaTensor());
}

//  void QDynamicRigidBody::setInertiaTensor(const QVector3D
//      &newInertiaTensor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody16setInertiaTensorERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *newInertiaTensor) {
  self->setInertiaTensor(*newInertiaTensor);
}

//  const QVector3D &QDynamicRigidBody::centerOfMassPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QDynamicRigidBody20centerOfMassPositionEv(
    const QDynamicRigidBody *self) {
  return new QVector3D(self->centerOfMassPosition());
}

//  void QDynamicRigidBody::setCenterOfMassPosition(const QVector3D
//      &newCenterOfMassPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody23setCenterOfMassPositionERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *newCenterOfMassPosition) {
  self->setCenterOfMassPosition(*newCenterOfMassPosition);
}

//  const QQuaternion &QDynamicRigidBody::centerOfMassRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK17QDynamicRigidBody20centerOfMassRotationEv(
    const QDynamicRigidBody *self) {
  return new QQuaternion(self->centerOfMassRotation());
}

//  void QDynamicRigidBody::setCenterOfMassRotation(const QQuaternion
//      &newCenterOfMassRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody23setCenterOfMassRotationERK11QQuaternion(
    QDynamicRigidBody *self,
    const QQuaternion *newCenterOfMassRotation) {
  self->setCenterOfMassRotation(*newCenterOfMassRotation);
}

//  const QList<float> &QDynamicRigidBody::readInertiaMatrix() const
extern "C" Q_DECL_EXPORT
const QList<float> *ritual_ZNK17QDynamicRigidBody17readInertiaMatrixEv(
    const QDynamicRigidBody *self) {
  return &(self->readInertiaMatrix());
}

//  void QDynamicRigidBody::setInertiaMatrix(const QList<float>
//      &newInertiaMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody16setInertiaMatrixERK5QListIfE(
    QDynamicRigidBody *self,
    const QList<float> *newInertiaMatrix) {
  self->setInertiaMatrix(*newInertiaMatrix);
}

//  const QMatrix3x3 &QDynamicRigidBody::inertiaMatrix() const
extern "C" Q_DECL_EXPORT
const QMatrix3x3 *ritual_ZNK17QDynamicRigidBody13inertiaMatrixEv(
    const QDynamicRigidBody *self) {
  return &(self->inertiaMatrix());
}

//  void QDynamicRigidBody::setKinematicPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody20setKinematicPositionERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *position) {
  self->setKinematicPosition(*position);
}

//  QVector3D QDynamicRigidBody::kinematicPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QDynamicRigidBody17kinematicPositionEv(
    const QDynamicRigidBody *self) {
  return new QVector3D(self->kinematicPosition());
}

//  void QDynamicRigidBody::setKinematicRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody20setKinematicRotationERK11QQuaternion(
    QDynamicRigidBody *self,
    const QQuaternion *rotation) {
  self->setKinematicRotation(*rotation);
}

//  QQuaternion QDynamicRigidBody::kinematicRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK17QDynamicRigidBody17kinematicRotationEv(
    const QDynamicRigidBody *self) {
  return new QQuaternion(self->kinematicRotation());
}

//  void QDynamicRigidBody::setKinematicEulerRotation(const QVector3D
//      &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody25setKinematicEulerRotationERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *rotation) {
  self->setKinematicEulerRotation(*rotation);
}

//  QVector3D QDynamicRigidBody::kinematicEulerRotation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QDynamicRigidBody22kinematicEulerRotationEv(
    const QDynamicRigidBody *self) {
  return new QVector3D(self->kinematicEulerRotation());
}

//  void QDynamicRigidBody::setKinematicPivot(const QVector3D &pivot)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17setKinematicPivotERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *pivot) {
  self->setKinematicPivot(*pivot);
}

//  QVector3D QDynamicRigidBody::kinematicPivot() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QDynamicRigidBody14kinematicPivotEv(
    const QDynamicRigidBody *self) {
  return new QVector3D(self->kinematicPivot());
}

//  void QDynamicRigidBody::setIsSleeping(bool newIsSleeping)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody13setIsSleepingEb(
    QDynamicRigidBody *self,
    bool newIsSleeping) {
  self->setIsSleeping(newIsSleeping);
}

//  bool QDynamicRigidBody::isSleeping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDynamicRigidBody10isSleepingEv(
    const QDynamicRigidBody *self) {
  return self->isSleeping();
}

//  QAbstractPhysXNode *QDynamicRigidBody::createPhysXBackend()
extern "C" Q_DECL_EXPORT
QAbstractPhysXNode *ritual_ZN17QDynamicRigidBody18createPhysXBackendEv(
    QDynamicRigidBody *self) {
  return self->createPhysXBackend();
}

//  void QDynamicRigidBody::massChanged(float mass)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody11massChangedEf(
    QDynamicRigidBody *self,
    float mass) {
  self->massChanged(mass);
}

//  void QDynamicRigidBody::densityChanged(float density)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody14densityChangedEf(
    QDynamicRigidBody *self,
    float density) {
  self->densityChanged(density);
}

//  void QDynamicRigidBody::isKinematicChanged(bool isKinematic)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody18isKinematicChangedEb(
    QDynamicRigidBody *self,
    bool isKinematic) {
  self->isKinematicChanged(isKinematic);
}

//  void QDynamicRigidBody::linearAxisLockChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody21linearAxisLockChangedEv(
    QDynamicRigidBody *self) {
  self->linearAxisLockChanged();
}

//  void QDynamicRigidBody::angularAxisLockChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody22angularAxisLockChangedEv(
    QDynamicRigidBody *self) {
  self->angularAxisLockChanged();
}

//  void QDynamicRigidBody::gravityEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody21gravityEnabledChangedEv(
    QDynamicRigidBody *self) {
  self->gravityEnabledChanged();
}

//  void QDynamicRigidBody::massModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody15massModeChangedEv(
    QDynamicRigidBody *self) {
  self->massModeChanged();
}

//  void QDynamicRigidBody::inertiaTensorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody20inertiaTensorChangedEv(
    QDynamicRigidBody *self) {
  self->inertiaTensorChanged();
}

//  void QDynamicRigidBody::centerOfMassPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody27centerOfMassPositionChangedEv(
    QDynamicRigidBody *self) {
  self->centerOfMassPositionChanged();
}

//  void QDynamicRigidBody::centerOfMassRotationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody27centerOfMassRotationChangedEv(
    QDynamicRigidBody *self) {
  self->centerOfMassRotationChanged();
}

//  void QDynamicRigidBody::inertiaMatrixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody20inertiaMatrixChangedEv(
    QDynamicRigidBody *self) {
  self->inertiaMatrixChanged();
}

//  void QDynamicRigidBody::kinematicPositionChanged(const QVector3D
//      &kinematicPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody24kinematicPositionChangedERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *kinematicPosition) {
  self->kinematicPositionChanged(*kinematicPosition);
}

//  void QDynamicRigidBody::kinematicRotationChanged(const QQuaternion
//      &kinematicRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody24kinematicRotationChangedERK11QQuaternion(
    QDynamicRigidBody *self,
    const QQuaternion *kinematicRotation) {
  self->kinematicRotationChanged(*kinematicRotation);
}

//  void QDynamicRigidBody::kinematicEulerRotationChanged(const QVector3D
//      &kinematicEulerRotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody29kinematicEulerRotationChangedERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *kinematicEulerRotation) {
  self->kinematicEulerRotationChanged(*kinematicEulerRotation);
}

//  void QDynamicRigidBody::kinematicPivotChanged(const QVector3D
//      &kinematicPivot)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody21kinematicPivotChangedERK9QVector3D(
    QDynamicRigidBody *self,
    const QVector3D *kinematicPivot) {
  self->kinematicPivotChanged(*kinematicPivot);
}

//  void QDynamicRigidBody::isSleepingChanged(bool isSleeping)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDynamicRigidBody17isSleepingChangedEb(
    QDynamicRigidBody *self,
    bool isSleeping) {
  self->isSleepingChanged(isSleeping);
}

//  a Python function taken by a CuteQDynamicRigidBody, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDynamicRigidBody(
    QDynamicRigidBody *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDynamicRigidBody *>(self)->take(key, call);
}
