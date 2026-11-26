//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qjoint.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qjoint.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DCore::QJoint that Python can take functions over in. Every Qt3DCore::QJoint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QJointCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QJointCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QJointCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QJointCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QJointCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QJointCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QJointCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QJoint : public Qt3DCore::QJoint {
public:
  using Qt3DCore::QJoint::QJoint;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QJointCall0 call = reinterpret_cast<CuteQt3DCore_QJointCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QJointCall1 call = reinterpret_cast<CuteQt3DCore_QJointCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QJointCall2 call = reinterpret_cast<CuteQt3DCore_QJointCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QJointCall3 call = reinterpret_cast<CuteQt3DCore_QJointCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QJointCall4 call = reinterpret_cast<CuteQt3DCore_QJointCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QJointCall5 call = reinterpret_cast<CuteQt3DCore_QJointCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QJointCall6 call = reinterpret_cast<CuteQt3DCore_QJointCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QJoint::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore6QJoint10metaObjectEv(
    const Qt3DCore::QJoint *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QJoint::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore6QJoint11qt_metacastEPKc(
    Qt3DCore::QJoint *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QJoint::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore6QJoint11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QJoint *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QJoint::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore6QJoint2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QJoint::tr(s, c, n));
}

//  Qt3DCore::QJoint::QJoint(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QJoint *ritual_ZN8Qt3DCore6QJointC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QJoint(parent);
}

//  Qt3DCore::QJoint::~QJoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJointD1Ev(Qt3DCore::QJoint *self) {
  delete self;
}

//  QVector3D Qt3DCore::QJoint::scale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore6QJoint5scaleEv(const Qt3DCore::QJoint *self) {
  return new QVector3D(self->scale());
}

//  QQuaternion Qt3DCore::QJoint::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK8Qt3DCore6QJoint8rotationEv(
    const Qt3DCore::QJoint *self) {
  return new QQuaternion(self->rotation());
}

//  QVector3D Qt3DCore::QJoint::translation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore6QJoint11translationEv(
    const Qt3DCore::QJoint *self) {
  return new QVector3D(self->translation());
}

//  QMatrix4x4 Qt3DCore::QJoint::inverseBindMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK8Qt3DCore6QJoint17inverseBindMatrixEv(
    const Qt3DCore::QJoint *self) {
  return new QMatrix4x4(self->inverseBindMatrix());
}

//  float Qt3DCore::QJoint::rotationX() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore6QJoint9rotationXEv(const Qt3DCore::QJoint *self) {
  return self->rotationX();
}

//  float Qt3DCore::QJoint::rotationY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore6QJoint9rotationYEv(const Qt3DCore::QJoint *self) {
  return self->rotationY();
}

//  float Qt3DCore::QJoint::rotationZ() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore6QJoint9rotationZEv(const Qt3DCore::QJoint *self) {
  return self->rotationZ();
}

//  QString Qt3DCore::QJoint::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore6QJoint4nameEv(const Qt3DCore::QJoint *self) {
  return new QString(self->name());
}

//  void Qt3DCore::QJoint::addChildJoint(QJoint *joint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint13addChildJointEPS0_(
    Qt3DCore::QJoint *self,
    Qt3DCore::QJoint *joint) {
  self->addChildJoint(joint);
}

//  void Qt3DCore::QJoint::removeChildJoint(QJoint *joint)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint16removeChildJointEPS0_(
    Qt3DCore::QJoint *self,
    Qt3DCore::QJoint *joint) {
  self->removeChildJoint(joint);
}

//  QList<QJoint *> Qt3DCore::QJoint::childJoints() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QJoint *> *ritual_ZNK8Qt3DCore6QJoint11childJointsEv(
    const Qt3DCore::QJoint *self) {
  return new QList<Qt3DCore::QJoint *>(self->childJoints());
}

//  void Qt3DCore::QJoint::setScale(const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint8setScaleERK9QVector3D(
    Qt3DCore::QJoint *self,
    const QVector3D *scale) {
  self->setScale(*scale);
}

//  void Qt3DCore::QJoint::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint11setRotationERK11QQuaternion(
    Qt3DCore::QJoint *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  void Qt3DCore::QJoint::setTranslation(const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint14setTranslationERK9QVector3D(
    Qt3DCore::QJoint *self,
    const QVector3D *translation) {
  self->setTranslation(*translation);
}

//  void Qt3DCore::QJoint::setInverseBindMatrix(const QMatrix4x4
//      &inverseBindMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint20setInverseBindMatrixERK10QMatrix4x4(
    Qt3DCore::QJoint *self,
    const QMatrix4x4 *inverseBindMatrix) {
  self->setInverseBindMatrix(*inverseBindMatrix);
}

//  void Qt3DCore::QJoint::setRotationX(float rotationX)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint12setRotationXEf(
    Qt3DCore::QJoint *self,
    float rotationX) {
  self->setRotationX(rotationX);
}

//  void Qt3DCore::QJoint::setRotationY(float rotationY)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint12setRotationYEf(
    Qt3DCore::QJoint *self,
    float rotationY) {
  self->setRotationY(rotationY);
}

//  void Qt3DCore::QJoint::setRotationZ(float rotationZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint12setRotationZEf(
    Qt3DCore::QJoint *self,
    float rotationZ) {
  self->setRotationZ(rotationZ);
}

//  void Qt3DCore::QJoint::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint7setNameERK7QString(
    Qt3DCore::QJoint *self,
    const QString *name) {
  self->setName(*name);
}

//  void Qt3DCore::QJoint::setToIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint13setToIdentityEv(Qt3DCore::QJoint *self) {
  self->setToIdentity();
}

//  void Qt3DCore::QJoint::scaleChanged(const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint12scaleChangedERK9QVector3D(
    Qt3DCore::QJoint *self,
    const QVector3D *scale) {
  self->scaleChanged(*scale);
}

//  void Qt3DCore::QJoint::rotationChanged(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint15rotationChangedERK11QQuaternion(
    Qt3DCore::QJoint *self,
    const QQuaternion *rotation) {
  self->rotationChanged(*rotation);
}

//  void Qt3DCore::QJoint::translationChanged(const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint18translationChangedERK9QVector3D(
    Qt3DCore::QJoint *self,
    const QVector3D *translation) {
  self->translationChanged(*translation);
}

//  void Qt3DCore::QJoint::inverseBindMatrixChanged(const QMatrix4x4
//      &inverseBindMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint24inverseBindMatrixChangedERK10QMatrix4x4(
    Qt3DCore::QJoint *self,
    const QMatrix4x4 *inverseBindMatrix) {
  self->inverseBindMatrixChanged(*inverseBindMatrix);
}

//  void Qt3DCore::QJoint::rotationXChanged(float rotationX)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint16rotationXChangedEf(
    Qt3DCore::QJoint *self,
    float rotationX) {
  self->rotationXChanged(rotationX);
}

//  void Qt3DCore::QJoint::rotationYChanged(float rotationY)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint16rotationYChangedEf(
    Qt3DCore::QJoint *self,
    float rotationY) {
  self->rotationYChanged(rotationY);
}

//  void Qt3DCore::QJoint::rotationZChanged(float rotationZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint16rotationZChangedEf(
    Qt3DCore::QJoint *self,
    float rotationZ) {
  self->rotationZChanged(rotationZ);
}

//  void Qt3DCore::QJoint::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QJoint11nameChangedERK7QString(
    Qt3DCore::QJoint *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  QJointPrivate *Qt3DCore::QJoint::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QJointPrivate *ritual_ZN8Qt3DCore6QJoint6d_funcEv(
    Qt3DCore::QJoint *self) {
  return self->d_func();
}

//  const QJointPrivate *Qt3DCore::QJoint::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QJointPrivate *ritual_ZNK8Qt3DCore6QJoint6d_funcEv(
    const Qt3DCore::QJoint *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QJoint, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QJoint(
    Qt3DCore::QJoint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QJoint *>(self)->take(key, call);
}

//  a QList<Qt3DCore::QJoint *> a ritual of Qt3DCore::QJoint gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QJoint__QList_Qt3DCore_QJoint(
    QList<Qt3DCore::QJoint *> *self) {
  delete self;
}
