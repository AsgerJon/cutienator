//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qtransform.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qtransform.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QTransform that Python can take functions over in. Every Qt3DCore::QTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QTransformCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QTransformCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QTransformCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QTransformCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QTransformCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QTransformCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QTransformCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QTransform : public Qt3DCore::QTransform {
public:
  using Qt3DCore::QTransform::QTransform;
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
      CuteQt3DCore_QTransformCall0 call = reinterpret_cast<CuteQt3DCore_QTransformCall0>(taken[0]);
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
      CuteQt3DCore_QTransformCall1 call = reinterpret_cast<CuteQt3DCore_QTransformCall1>(taken[1]);
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
      CuteQt3DCore_QTransformCall2 call = reinterpret_cast<CuteQt3DCore_QTransformCall2>(taken[2]);
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
      CuteQt3DCore_QTransformCall3 call = reinterpret_cast<CuteQt3DCore_QTransformCall3>(taken[3]);
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
      CuteQt3DCore_QTransformCall4 call = reinterpret_cast<CuteQt3DCore_QTransformCall4>(taken[4]);
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
      CuteQt3DCore_QTransformCall5 call = reinterpret_cast<CuteQt3DCore_QTransformCall5>(taken[5]);
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
      CuteQt3DCore_QTransformCall6 call = reinterpret_cast<CuteQt3DCore_QTransformCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QTransform::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore10QTransform10metaObjectEv(
    const Qt3DCore::QTransform *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QTransform::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore10QTransform11qt_metacastEPKc(
    Qt3DCore::QTransform *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QTransform::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore10QTransform11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QTransform *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QTransform::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore10QTransform2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QTransform::tr(s, c, n));
}

//  Qt3DCore::QTransform::QTransform(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransform *ritual_ZN8Qt3DCore10QTransformC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QTransform(parent);
}

//  Qt3DCore::QTransform::~QTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransformD1Ev(Qt3DCore::QTransform *self) {
  delete self;
}

//  float Qt3DCore::QTransform::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore10QTransform5scaleEv(
    const Qt3DCore::QTransform *self) {
  return self->scale();
}

//  QVector3D Qt3DCore::QTransform::scale3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore10QTransform7scale3DEv(
    const Qt3DCore::QTransform *self) {
  return new QVector3D(self->scale3D());
}

//  QQuaternion Qt3DCore::QTransform::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK8Qt3DCore10QTransform8rotationEv(
    const Qt3DCore::QTransform *self) {
  return new QQuaternion(self->rotation());
}

//  QVector3D Qt3DCore::QTransform::translation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore10QTransform11translationEv(
    const Qt3DCore::QTransform *self) {
  return new QVector3D(self->translation());
}

//  QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(const QVector3D &axis,
//      float angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform16fromAxisAndAngleERK9QVector3Df(
    const QVector3D *axis,
    float angle) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromAxisAndAngle(
          *axis,
          angle));
}

//  QQuaternion Qt3DCore::QTransform::fromAxisAndAngle(float x, float y,
//      float z, float angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform16fromAxisAndAngleEffff(
    float x,
    float y,
    float z,
    float angle) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromAxisAndAngle(
          x,
          y,
          z,
          angle));
}

//  QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const QVector3D
//      &axis1, float angle1, const QVector3D &axis2, float angle2)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform17fromAxesAndAnglesERK9QVector3DfS3_f(
    const QVector3D *axis1,
    float angle1,
    const QVector3D *axis2,
    float angle2) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromAxesAndAngles(
          *axis1,
          angle1,
          *axis2,
          angle2));
}

//  QQuaternion Qt3DCore::QTransform::fromAxesAndAngles(const QVector3D
//      &axis1, float angle1, const QVector3D &axis2, float angle2, const
//      QVector3D &axis3, float angle3)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform17fromAxesAndAnglesERK9QVector3DfS3_fS3_f(
    const QVector3D *axis1,
    float angle1,
    const QVector3D *axis2,
    float angle2,
    const QVector3D *axis3,
    float angle3) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromAxesAndAngles(
          *axis1,
          angle1,
          *axis2,
          angle2,
          *axis3,
          angle3));
}

//  QQuaternion Qt3DCore::QTransform::fromAxes(const QVector3D &xAxis, const
//      QVector3D &yAxis, const QVector3D &zAxis)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform8fromAxesERK9QVector3DS3_S3_(
    const QVector3D *xAxis,
    const QVector3D *yAxis,
    const QVector3D *zAxis) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromAxes(
          *xAxis,
          *yAxis,
          *zAxis));
}

//  QQuaternion Qt3DCore::QTransform::fromEulerAngles(const QVector3D
//      &eulerAngles)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform15fromEulerAnglesERK9QVector3D(
    const QVector3D *eulerAngles) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromEulerAngles(
          *eulerAngles));
}

//  QQuaternion Qt3DCore::QTransform::fromEulerAngles(float pitch, float yaw,
//      float roll)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN8Qt3DCore10QTransform15fromEulerAnglesEfff(
    float pitch,
    float yaw,
    float roll) {
  return new QQuaternion(
      Qt3DCore::QTransform::fromEulerAngles(
          pitch,
          yaw,
          roll));
}

//  QMatrix4x4 Qt3DCore::QTransform::rotateAround(const QVector3D &point,
//      float angle, const QVector3D &axis)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN8Qt3DCore10QTransform12rotateAroundERK9QVector3DfS3_(
    const QVector3D *point,
    float angle,
    const QVector3D *axis) {
  return new QMatrix4x4(
      Qt3DCore::QTransform::rotateAround(
          *point,
          angle,
          *axis));
}

//  QMatrix4x4 Qt3DCore::QTransform::rotateFromAxes(const QVector3D &xAxis,
//      const QVector3D &yAxis, const QVector3D &zAxis)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN8Qt3DCore10QTransform14rotateFromAxesERK9QVector3DS3_S3_(
    const QVector3D *xAxis,
    const QVector3D *yAxis,
    const QVector3D *zAxis) {
  return new QMatrix4x4(
      Qt3DCore::QTransform::rotateFromAxes(
          *xAxis,
          *yAxis,
          *zAxis));
}

//  QMatrix4x4 Qt3DCore::QTransform::matrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK8Qt3DCore10QTransform6matrixEv(
    const Qt3DCore::QTransform *self) {
  return new QMatrix4x4(self->matrix());
}

//  QMatrix4x4 Qt3DCore::QTransform::worldMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK8Qt3DCore10QTransform11worldMatrixEv(
    const Qt3DCore::QTransform *self) {
  return new QMatrix4x4(self->worldMatrix());
}

//  float Qt3DCore::QTransform::rotationX() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore10QTransform9rotationXEv(
    const Qt3DCore::QTransform *self) {
  return self->rotationX();
}

//  float Qt3DCore::QTransform::rotationY() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore10QTransform9rotationYEv(
    const Qt3DCore::QTransform *self) {
  return self->rotationY();
}

//  float Qt3DCore::QTransform::rotationZ() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK8Qt3DCore10QTransform9rotationZEv(
    const Qt3DCore::QTransform *self) {
  return self->rotationZ();
}

//  void Qt3DCore::QTransform::setScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform8setScaleEf(
    Qt3DCore::QTransform *self,
    float scale) {
  self->setScale(scale);
}

//  void Qt3DCore::QTransform::setScale3D(const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform10setScale3DERK9QVector3D(
    Qt3DCore::QTransform *self,
    const QVector3D *scale) {
  self->setScale3D(*scale);
}

//  void Qt3DCore::QTransform::setRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform11setRotationERK11QQuaternion(
    Qt3DCore::QTransform *self,
    const QQuaternion *rotation) {
  self->setRotation(*rotation);
}

//  void Qt3DCore::QTransform::setTranslation(const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform14setTranslationERK9QVector3D(
    Qt3DCore::QTransform *self,
    const QVector3D *translation) {
  self->setTranslation(*translation);
}

//  void Qt3DCore::QTransform::setMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform9setMatrixERK10QMatrix4x4(
    Qt3DCore::QTransform *self,
    const QMatrix4x4 *matrix) {
  self->setMatrix(*matrix);
}

//  void Qt3DCore::QTransform::setRotationX(float rotationX)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform12setRotationXEf(
    Qt3DCore::QTransform *self,
    float rotationX) {
  self->setRotationX(rotationX);
}

//  void Qt3DCore::QTransform::setRotationY(float rotationY)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform12setRotationYEf(
    Qt3DCore::QTransform *self,
    float rotationY) {
  self->setRotationY(rotationY);
}

//  void Qt3DCore::QTransform::setRotationZ(float rotationZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform12setRotationZEf(
    Qt3DCore::QTransform *self,
    float rotationZ) {
  self->setRotationZ(rotationZ);
}

//  void Qt3DCore::QTransform::scaleChanged(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform12scaleChangedEf(
    Qt3DCore::QTransform *self,
    float scale) {
  self->scaleChanged(scale);
}

//  void Qt3DCore::QTransform::scale3DChanged(const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform14scale3DChangedERK9QVector3D(
    Qt3DCore::QTransform *self,
    const QVector3D *scale) {
  self->scale3DChanged(*scale);
}

//  void Qt3DCore::QTransform::rotationChanged(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform15rotationChangedERK11QQuaternion(
    Qt3DCore::QTransform *self,
    const QQuaternion *rotation) {
  self->rotationChanged(*rotation);
}

//  void Qt3DCore::QTransform::translationChanged(const QVector3D
//      &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform18translationChangedERK9QVector3D(
    Qt3DCore::QTransform *self,
    const QVector3D *translation) {
  self->translationChanged(*translation);
}

//  void Qt3DCore::QTransform::matrixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform13matrixChangedEv(
    Qt3DCore::QTransform *self) {
  self->matrixChanged();
}

//  void Qt3DCore::QTransform::rotationXChanged(float rotationX)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform16rotationXChangedEf(
    Qt3DCore::QTransform *self,
    float rotationX) {
  self->rotationXChanged(rotationX);
}

//  void Qt3DCore::QTransform::rotationYChanged(float rotationY)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform16rotationYChangedEf(
    Qt3DCore::QTransform *self,
    float rotationY) {
  self->rotationYChanged(rotationY);
}

//  void Qt3DCore::QTransform::rotationZChanged(float rotationZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform16rotationZChangedEf(
    Qt3DCore::QTransform *self,
    float rotationZ) {
  self->rotationZChanged(rotationZ);
}

//  void Qt3DCore::QTransform::worldMatrixChanged(const QMatrix4x4
//      &worldMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QTransform18worldMatrixChangedERK10QMatrix4x4(
    Qt3DCore::QTransform *self,
    const QMatrix4x4 *worldMatrix) {
  self->worldMatrixChanged(*worldMatrix);
}

//  Qt3DCore::QTransform::QTransform(QTransformPrivate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransform *ritual_ZN8Qt3DCore10QTransformC1ERNS_17QTransformPrivateEPNS_5QNodeE(
    Qt3DCore::QTransformPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DCore_QTransform(*dd, parent);
}

//  QTransformPrivate *Qt3DCore::QTransform::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransformPrivate *ritual_ZN8Qt3DCore10QTransform6d_funcEv(
    Qt3DCore::QTransform *self) {
  return self->d_func();
}

//  const QTransformPrivate *Qt3DCore::QTransform::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QTransformPrivate *ritual_ZNK8Qt3DCore10QTransform6d_funcEv(
    const Qt3DCore::QTransform *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QTransform, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QTransform(
    Qt3DCore::QTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QTransform *>(self)->take(key, call);
}
