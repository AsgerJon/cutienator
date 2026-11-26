//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qcamera.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qcamera.h>
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QCamera that Python can take functions over in. Every Qt3DRender::QCamera
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCameraCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCameraCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QCamera : public Qt3DRender::QCamera {
public:
  using Qt3DRender::QCamera::QCamera;
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
      CuteQt3DRender_QCameraCall0 call = reinterpret_cast<CuteQt3DRender_QCameraCall0>(taken[0]);
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
      CuteQt3DRender_QCameraCall1 call = reinterpret_cast<CuteQt3DRender_QCameraCall1>(taken[1]);
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
      CuteQt3DRender_QCameraCall2 call = reinterpret_cast<CuteQt3DRender_QCameraCall2>(taken[2]);
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
      CuteQt3DRender_QCameraCall3 call = reinterpret_cast<CuteQt3DRender_QCameraCall3>(taken[3]);
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
      CuteQt3DRender_QCameraCall4 call = reinterpret_cast<CuteQt3DRender_QCameraCall4>(taken[4]);
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
      CuteQt3DRender_QCameraCall5 call = reinterpret_cast<CuteQt3DRender_QCameraCall5>(taken[5]);
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
      CuteQt3DRender_QCameraCall6 call = reinterpret_cast<CuteQt3DRender_QCameraCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QCamera::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender7QCamera10metaObjectEv(
    const Qt3DRender::QCamera *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QCamera::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender7QCamera11qt_metacastEPKc(
    Qt3DRender::QCamera *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QCamera::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender7QCamera11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QCamera *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QCamera::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender7QCamera2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QCamera::tr(s, c, n));
}

//  Qt3DRender::QCamera::QCamera(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QCamera *ritual_ZN10Qt3DRender7QCameraC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QCamera(parent);
}

//  Qt3DRender::QCamera::~QCamera()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCameraD1Ev(Qt3DRender::QCamera *self) {
  delete self;
}

//  QCameraLens *Qt3DRender::QCamera::lens() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLens *ritual_ZNK10Qt3DRender7QCamera4lensEv(
    const Qt3DRender::QCamera *self) {
  return self->lens();
}

//  Qt3DCore::QTransform *Qt3DRender::QCamera::transform() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransform *ritual_ZNK10Qt3DRender7QCamera9transformEv(
    const Qt3DRender::QCamera *self) {
  return self->transform();
}

//  QQuaternion Qt3DRender::QCamera::tiltRotation(float angle) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10Qt3DRender7QCamera12tiltRotationEf(
    const Qt3DRender::QCamera *self,
    float angle) {
  return new QQuaternion(self->tiltRotation(angle));
}

//  QQuaternion Qt3DRender::QCamera::panRotation(float angle) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10Qt3DRender7QCamera11panRotationEf(
    const Qt3DRender::QCamera *self,
    float angle) {
  return new QQuaternion(self->panRotation(angle));
}

//  QQuaternion Qt3DRender::QCamera::rollRotation(float angle) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10Qt3DRender7QCamera12rollRotationEf(
    const Qt3DRender::QCamera *self,
    float angle) {
  return new QQuaternion(self->rollRotation(angle));
}

//  QQuaternion Qt3DRender::QCamera::rotation(float angle, const QVector3D
//      &axis) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10Qt3DRender7QCamera8rotationEfRK9QVector3D(
    const Qt3DRender::QCamera *self,
    float angle,
    const QVector3D *axis) {
  return new QQuaternion(self->rotation(angle, *axis));
}

//  void Qt3DRender::QCamera::translate(const QVector3D &vLocal,
//      CameraTranslationOption option)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera9translateERK9QVector3DNS0_23CameraTranslationOptionE(
    Qt3DRender::QCamera *self,
    const QVector3D *vLocal,
    Qt3DRender::QCamera::CameraTranslationOption option) {
  self->translate(*vLocal, option);
}

//  void Qt3DRender::QCamera::translateWorld(const QVector3D &vWorld,
//      CameraTranslationOption option)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera14translateWorldERK9QVector3DNS0_23CameraTranslationOptionE(
    Qt3DRender::QCamera *self,
    const QVector3D *vWorld,
    Qt3DRender::QCamera::CameraTranslationOption option) {
  self->translateWorld(*vWorld, option);
}

//  void Qt3DRender::QCamera::tilt(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera4tiltEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->tilt(angle);
}

//  void Qt3DRender::QCamera::pan(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera3panEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->pan(angle);
}

//  void Qt3DRender::QCamera::pan(float angle, const QVector3D &axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera3panEfRK9QVector3D(
    Qt3DRender::QCamera *self,
    float angle,
    const QVector3D *axis) {
  self->pan(angle, *axis);
}

//  void Qt3DRender::QCamera::roll(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera4rollEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->roll(angle);
}

//  void Qt3DRender::QCamera::tiltAboutViewCenter(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera19tiltAboutViewCenterEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->tiltAboutViewCenter(angle);
}

//  void Qt3DRender::QCamera::panAboutViewCenter(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera18panAboutViewCenterEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->panAboutViewCenter(angle);
}

//  void Qt3DRender::QCamera::panAboutViewCenter(float angle, const QVector3D
//      &axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera18panAboutViewCenterEfRK9QVector3D(
    Qt3DRender::QCamera *self,
    float angle,
    const QVector3D *axis) {
  self->panAboutViewCenter(angle, *axis);
}

//  void Qt3DRender::QCamera::rollAboutViewCenter(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera19rollAboutViewCenterEf(
    Qt3DRender::QCamera *self,
    float angle) {
  self->rollAboutViewCenter(angle);
}

//  void Qt3DRender::QCamera::rotate(const QQuaternion &q)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera6rotateERK11QQuaternion(
    Qt3DRender::QCamera *self,
    const QQuaternion *q) {
  self->rotate(*q);
}

//  void Qt3DRender::QCamera::rotateAboutViewCenter(const QQuaternion &q)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera21rotateAboutViewCenterERK11QQuaternion(
    Qt3DRender::QCamera *self,
    const QQuaternion *q) {
  self->rotateAboutViewCenter(*q);
}

//  QCameraLens::ProjectionType Qt3DRender::QCamera::projectionType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLens::ProjectionType ritual_ZNK10Qt3DRender7QCamera14projectionTypeEv(
    const Qt3DRender::QCamera *self) {
  return self->projectionType();
}

//  float Qt3DRender::QCamera::nearPlane() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera9nearPlaneEv(
    const Qt3DRender::QCamera *self) {
  return self->nearPlane();
}

//  float Qt3DRender::QCamera::farPlane() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera8farPlaneEv(
    const Qt3DRender::QCamera *self) {
  return self->farPlane();
}

//  float Qt3DRender::QCamera::fieldOfView() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera11fieldOfViewEv(
    const Qt3DRender::QCamera *self) {
  return self->fieldOfView();
}

//  float Qt3DRender::QCamera::aspectRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera11aspectRatioEv(
    const Qt3DRender::QCamera *self) {
  return self->aspectRatio();
}

//  float Qt3DRender::QCamera::left() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera4leftEv(
    const Qt3DRender::QCamera *self) {
  return self->left();
}

//  float Qt3DRender::QCamera::right() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera5rightEv(
    const Qt3DRender::QCamera *self) {
  return self->right();
}

//  float Qt3DRender::QCamera::bottom() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera6bottomEv(
    const Qt3DRender::QCamera *self) {
  return self->bottom();
}

//  float Qt3DRender::QCamera::top() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera3topEv(const Qt3DRender::QCamera *self) {
  return self->top();
}

//  QMatrix4x4 Qt3DRender::QCamera::projectionMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender7QCamera16projectionMatrixEv(
    const Qt3DRender::QCamera *self) {
  return new QMatrix4x4(self->projectionMatrix());
}

//  float Qt3DRender::QCamera::exposure() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender7QCamera8exposureEv(
    const Qt3DRender::QCamera *self) {
  return self->exposure();
}

//  QVector3D Qt3DRender::QCamera::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender7QCamera8positionEv(
    const Qt3DRender::QCamera *self) {
  return new QVector3D(self->position());
}

//  QVector3D Qt3DRender::QCamera::upVector() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender7QCamera8upVectorEv(
    const Qt3DRender::QCamera *self) {
  return new QVector3D(self->upVector());
}

//  QVector3D Qt3DRender::QCamera::viewCenter() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender7QCamera10viewCenterEv(
    const Qt3DRender::QCamera *self) {
  return new QVector3D(self->viewCenter());
}

//  QVector3D Qt3DRender::QCamera::viewVector() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender7QCamera10viewVectorEv(
    const Qt3DRender::QCamera *self) {
  return new QVector3D(self->viewVector());
}

//  QMatrix4x4 Qt3DRender::QCamera::viewMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender7QCamera10viewMatrixEv(
    const Qt3DRender::QCamera *self) {
  return new QMatrix4x4(self->viewMatrix());
}

//  void Qt3DRender::QCamera::setProjectionType(QCameraLens::ProjectionType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera17setProjectionTypeENS_11QCameraLens14ProjectionTypeE(
    Qt3DRender::QCamera *self,
    Qt3DRender::QCameraLens::ProjectionType type) {
  self->setProjectionType(type);
}

//  void Qt3DRender::QCamera::setNearPlane(float nearPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera12setNearPlaneEf(
    Qt3DRender::QCamera *self,
    float nearPlane) {
  self->setNearPlane(nearPlane);
}

//  void Qt3DRender::QCamera::setFarPlane(float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera11setFarPlaneEf(
    Qt3DRender::QCamera *self,
    float farPlane) {
  self->setFarPlane(farPlane);
}

//  void Qt3DRender::QCamera::setFieldOfView(float fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera14setFieldOfViewEf(
    Qt3DRender::QCamera *self,
    float fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  void Qt3DRender::QCamera::setAspectRatio(float aspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera14setAspectRatioEf(
    Qt3DRender::QCamera *self,
    float aspectRatio) {
  self->setAspectRatio(aspectRatio);
}

//  void Qt3DRender::QCamera::setLeft(float left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera7setLeftEf(
    Qt3DRender::QCamera *self,
    float left) {
  self->setLeft(left);
}

//  void Qt3DRender::QCamera::setRight(float right)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera8setRightEf(
    Qt3DRender::QCamera *self,
    float right) {
  self->setRight(right);
}

//  void Qt3DRender::QCamera::setBottom(float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera9setBottomEf(
    Qt3DRender::QCamera *self,
    float bottom) {
  self->setBottom(bottom);
}

//  void Qt3DRender::QCamera::setTop(float top)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera6setTopEf(
    Qt3DRender::QCamera *self,
    float top) {
  self->setTop(top);
}

//  void Qt3DRender::QCamera::setProjectionMatrix(const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera19setProjectionMatrixERK10QMatrix4x4(
    Qt3DRender::QCamera *self,
    const QMatrix4x4 *projectionMatrix) {
  self->setProjectionMatrix(*projectionMatrix);
}

//  void Qt3DRender::QCamera::setExposure(float exposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera11setExposureEf(
    Qt3DRender::QCamera *self,
    float exposure) {
  self->setExposure(exposure);
}

//  void Qt3DRender::QCamera::setPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera11setPositionERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  void Qt3DRender::QCamera::setUpVector(const QVector3D &upVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera11setUpVectorERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *upVector) {
  self->setUpVector(*upVector);
}

//  void Qt3DRender::QCamera::setViewCenter(const QVector3D &viewCenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera13setViewCenterERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *viewCenter) {
  self->setViewCenter(*viewCenter);
}

//  void Qt3DRender::QCamera::viewAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera7viewAllEv(Qt3DRender::QCamera *self) {
  self->viewAll();
}

//  void Qt3DRender::QCamera::viewSphere(const QVector3D &center, float
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera10viewSphereERK9QVector3Df(
    Qt3DRender::QCamera *self,
    const QVector3D *center,
    float radius) {
  self->viewSphere(*center, radius);
}

//  void Qt3DRender::QCamera::viewEntity(Qt3DCore::QEntity *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera10viewEntityEPN8Qt3DCore7QEntityE(
    Qt3DRender::QCamera *self,
    Qt3DCore::QEntity *entity) {
  self->viewEntity(entity);
}

//  void
//      Qt3DRender::QCamera::projectionTypeChanged(QCameraLens::ProjectionTyp
//      e projectionType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera21projectionTypeChangedENS_11QCameraLens14ProjectionTypeE(
    Qt3DRender::QCamera *self,
    Qt3DRender::QCameraLens::ProjectionType projectionType) {
  self->projectionTypeChanged(projectionType);
}

//  void Qt3DRender::QCamera::nearPlaneChanged(float nearPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera16nearPlaneChangedEf(
    Qt3DRender::QCamera *self,
    float nearPlane) {
  self->nearPlaneChanged(nearPlane);
}

//  void Qt3DRender::QCamera::farPlaneChanged(float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera15farPlaneChangedEf(
    Qt3DRender::QCamera *self,
    float farPlane) {
  self->farPlaneChanged(farPlane);
}

//  void Qt3DRender::QCamera::fieldOfViewChanged(float fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera18fieldOfViewChangedEf(
    Qt3DRender::QCamera *self,
    float fieldOfView) {
  self->fieldOfViewChanged(fieldOfView);
}

//  void Qt3DRender::QCamera::aspectRatioChanged(float aspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera18aspectRatioChangedEf(
    Qt3DRender::QCamera *self,
    float aspectRatio) {
  self->aspectRatioChanged(aspectRatio);
}

//  void Qt3DRender::QCamera::leftChanged(float left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera11leftChangedEf(
    Qt3DRender::QCamera *self,
    float left) {
  self->leftChanged(left);
}

//  void Qt3DRender::QCamera::rightChanged(float right)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera12rightChangedEf(
    Qt3DRender::QCamera *self,
    float right) {
  self->rightChanged(right);
}

//  void Qt3DRender::QCamera::bottomChanged(float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera13bottomChangedEf(
    Qt3DRender::QCamera *self,
    float bottom) {
  self->bottomChanged(bottom);
}

//  void Qt3DRender::QCamera::topChanged(float top)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera10topChangedEf(
    Qt3DRender::QCamera *self,
    float top) {
  self->topChanged(top);
}

//  void Qt3DRender::QCamera::projectionMatrixChanged(const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera23projectionMatrixChangedERK10QMatrix4x4(
    Qt3DRender::QCamera *self,
    const QMatrix4x4 *projectionMatrix) {
  self->projectionMatrixChanged(*projectionMatrix);
}

//  void Qt3DRender::QCamera::exposureChanged(float exposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera15exposureChangedEf(
    Qt3DRender::QCamera *self,
    float exposure) {
  self->exposureChanged(exposure);
}

//  void Qt3DRender::QCamera::positionChanged(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera15positionChangedERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *position) {
  self->positionChanged(*position);
}

//  void Qt3DRender::QCamera::upVectorChanged(const QVector3D &upVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera15upVectorChangedERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *upVector) {
  self->upVectorChanged(*upVector);
}

//  void Qt3DRender::QCamera::viewCenterChanged(const QVector3D &viewCenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera17viewCenterChangedERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *viewCenter) {
  self->viewCenterChanged(*viewCenter);
}

//  void Qt3DRender::QCamera::viewVectorChanged(const QVector3D &viewVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera17viewVectorChangedERK9QVector3D(
    Qt3DRender::QCamera *self,
    const QVector3D *viewVector) {
  self->viewVectorChanged(*viewVector);
}

//  void Qt3DRender::QCamera::viewMatrixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender7QCamera17viewMatrixChangedEv(
    Qt3DRender::QCamera *self) {
  self->viewMatrixChanged();
}

//  QCameraPrivate *Qt3DRender::QCamera::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraPrivate *ritual_ZN10Qt3DRender7QCamera6d_funcEv(
    Qt3DRender::QCamera *self) {
  return self->d_func();
}

//  const QCameraPrivate *Qt3DRender::QCamera::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QCameraPrivate *ritual_ZNK10Qt3DRender7QCamera6d_funcEv(
    const Qt3DRender::QCamera *self) {
  return self->d_func();
}

//  Qt3DRender::QCamera::QCamera(QCameraPrivate &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QCamera *ritual_ZN10Qt3DRender7QCameraC1ERNS_14QCameraPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QCameraPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QCamera(*dd, parent);
}

//  a Python function taken by a CuteQt3DRender_QCamera, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QCamera(
    Qt3DRender::QCamera *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QCamera *>(self)->take(key, call);
}
