//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qcameralens.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qcameralens.h>
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QCameraLens that Python can take functions over in. Every Qt3DRender::QCameraLens
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCameraLensCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCameraLensCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraLensCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraLensCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraLensCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraLensCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCameraLensCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QCameraLens : public Qt3DRender::QCameraLens {
public:
  using Qt3DRender::QCameraLens::QCameraLens;
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
      CuteQt3DRender_QCameraLensCall0 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall0>(taken[0]);
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
      CuteQt3DRender_QCameraLensCall1 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall1>(taken[1]);
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
      CuteQt3DRender_QCameraLensCall2 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall2>(taken[2]);
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
      CuteQt3DRender_QCameraLensCall3 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall3>(taken[3]);
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
      CuteQt3DRender_QCameraLensCall4 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall4>(taken[4]);
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
      CuteQt3DRender_QCameraLensCall5 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall5>(taken[5]);
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
      CuteQt3DRender_QCameraLensCall6 call = reinterpret_cast<CuteQt3DRender_QCameraLensCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QCameraLens::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11QCameraLens10metaObjectEv(
    const Qt3DRender::QCameraLens *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QCameraLens::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11QCameraLens11qt_metacastEPKc(
    Qt3DRender::QCameraLens *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QCameraLens::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11QCameraLens11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QCameraLens *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QCameraLens::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender11QCameraLens2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QCameraLens::tr(s, c, n));
}

//  Qt3DRender::QCameraLens::QCameraLens(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLens *ritual_ZN10Qt3DRender11QCameraLensC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QCameraLens(parent);
}

//  Qt3DRender::QCameraLens::~QCameraLens()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLensD1Ev(Qt3DRender::QCameraLens *self) {
  delete self;
}

//  ProjectionType Qt3DRender::QCameraLens::projectionType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLens::ProjectionType ritual_ZNK10Qt3DRender11QCameraLens14projectionTypeEv(
    const Qt3DRender::QCameraLens *self) {
  return self->projectionType();
}

//  float Qt3DRender::QCameraLens::nearPlane() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens9nearPlaneEv(
    const Qt3DRender::QCameraLens *self) {
  return self->nearPlane();
}

//  float Qt3DRender::QCameraLens::farPlane() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens8farPlaneEv(
    const Qt3DRender::QCameraLens *self) {
  return self->farPlane();
}

//  float Qt3DRender::QCameraLens::fieldOfView() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens11fieldOfViewEv(
    const Qt3DRender::QCameraLens *self) {
  return self->fieldOfView();
}

//  float Qt3DRender::QCameraLens::aspectRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens11aspectRatioEv(
    const Qt3DRender::QCameraLens *self) {
  return self->aspectRatio();
}

//  float Qt3DRender::QCameraLens::left() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens4leftEv(
    const Qt3DRender::QCameraLens *self) {
  return self->left();
}

//  float Qt3DRender::QCameraLens::right() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens5rightEv(
    const Qt3DRender::QCameraLens *self) {
  return self->right();
}

//  float Qt3DRender::QCameraLens::bottom() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens6bottomEv(
    const Qt3DRender::QCameraLens *self) {
  return self->bottom();
}

//  float Qt3DRender::QCameraLens::top() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens3topEv(
    const Qt3DRender::QCameraLens *self) {
  return self->top();
}

//  QMatrix4x4 Qt3DRender::QCameraLens::projectionMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender11QCameraLens16projectionMatrixEv(
    const Qt3DRender::QCameraLens *self) {
  return new QMatrix4x4(self->projectionMatrix());
}

//  void Qt3DRender::QCameraLens::setOrthographicProjection(float left, float
//      right, float bottom, float top, float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens25setOrthographicProjectionEffffff(
    Qt3DRender::QCameraLens *self,
    float left,
    float right,
    float bottom,
    float top,
    float nearPlane,
    float farPlane) {
  self->setOrthographicProjection(
      left,
      right,
      bottom,
      top,
      nearPlane,
      farPlane);
}

//  void Qt3DRender::QCameraLens::setFrustumProjection(float left, float
//      right, float bottom, float top, float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens20setFrustumProjectionEffffff(
    Qt3DRender::QCameraLens *self,
    float left,
    float right,
    float bottom,
    float top,
    float nearPlane,
    float farPlane) {
  self->setFrustumProjection(left, right, bottom, top, nearPlane, farPlane);
}

//  void Qt3DRender::QCameraLens::setPerspectiveProjection(float fieldOfView,
//      float aspect, float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens24setPerspectiveProjectionEffff(
    Qt3DRender::QCameraLens *self,
    float fieldOfView,
    float aspect,
    float nearPlane,
    float farPlane) {
  self->setPerspectiveProjection(fieldOfView, aspect, nearPlane, farPlane);
}

//  float Qt3DRender::QCameraLens::exposure() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender11QCameraLens8exposureEv(
    const Qt3DRender::QCameraLens *self) {
  return self->exposure();
}

//  void Qt3DRender::QCameraLens::viewAll(Qt3DCore::QNodeId cameraId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens7viewAllEN8Qt3DCore7QNodeIdE(
    Qt3DRender::QCameraLens *self,
    const Qt3DCore::QNodeId *cameraId) {
  self->viewAll(*cameraId);
}

//  void Qt3DRender::QCameraLens::viewEntity(Qt3DCore::QNodeId entityId,
//      Qt3DCore::QNodeId cameraId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens10viewEntityEN8Qt3DCore7QNodeIdES2_(
    Qt3DRender::QCameraLens *self,
    const Qt3DCore::QNodeId *entityId,
    const Qt3DCore::QNodeId *cameraId) {
  self->viewEntity(*entityId, *cameraId);
}

//  void Qt3DRender::QCameraLens::setProjectionType(ProjectionType
//      projectionType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens17setProjectionTypeENS0_14ProjectionTypeE(
    Qt3DRender::QCameraLens *self,
    Qt3DRender::QCameraLens::ProjectionType projectionType) {
  self->setProjectionType(projectionType);
}

//  void Qt3DRender::QCameraLens::setNearPlane(float nearPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens12setNearPlaneEf(
    Qt3DRender::QCameraLens *self,
    float nearPlane) {
  self->setNearPlane(nearPlane);
}

//  void Qt3DRender::QCameraLens::setFarPlane(float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens11setFarPlaneEf(
    Qt3DRender::QCameraLens *self,
    float farPlane) {
  self->setFarPlane(farPlane);
}

//  void Qt3DRender::QCameraLens::setFieldOfView(float fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens14setFieldOfViewEf(
    Qt3DRender::QCameraLens *self,
    float fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  void Qt3DRender::QCameraLens::setAspectRatio(float aspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens14setAspectRatioEf(
    Qt3DRender::QCameraLens *self,
    float aspectRatio) {
  self->setAspectRatio(aspectRatio);
}

//  void Qt3DRender::QCameraLens::setLeft(float left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens7setLeftEf(
    Qt3DRender::QCameraLens *self,
    float left) {
  self->setLeft(left);
}

//  void Qt3DRender::QCameraLens::setRight(float right)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens8setRightEf(
    Qt3DRender::QCameraLens *self,
    float right) {
  self->setRight(right);
}

//  void Qt3DRender::QCameraLens::setBottom(float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens9setBottomEf(
    Qt3DRender::QCameraLens *self,
    float bottom) {
  self->setBottom(bottom);
}

//  void Qt3DRender::QCameraLens::setTop(float top)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens6setTopEf(
    Qt3DRender::QCameraLens *self,
    float top) {
  self->setTop(top);
}

//  void Qt3DRender::QCameraLens::setProjectionMatrix(const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens19setProjectionMatrixERK10QMatrix4x4(
    Qt3DRender::QCameraLens *self,
    const QMatrix4x4 *projectionMatrix) {
  self->setProjectionMatrix(*projectionMatrix);
}

//  void Qt3DRender::QCameraLens::setExposure(float exposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens11setExposureEf(
    Qt3DRender::QCameraLens *self,
    float exposure) {
  self->setExposure(exposure);
}

//  void Qt3DRender::QCameraLens::projectionTypeChanged(QCameraLens::Projecti
//      onType projectionType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens21projectionTypeChangedENS0_14ProjectionTypeE(
    Qt3DRender::QCameraLens *self,
    Qt3DRender::QCameraLens::ProjectionType projectionType) {
  self->projectionTypeChanged(projectionType);
}

//  void Qt3DRender::QCameraLens::nearPlaneChanged(float nearPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens16nearPlaneChangedEf(
    Qt3DRender::QCameraLens *self,
    float nearPlane) {
  self->nearPlaneChanged(nearPlane);
}

//  void Qt3DRender::QCameraLens::farPlaneChanged(float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens15farPlaneChangedEf(
    Qt3DRender::QCameraLens *self,
    float farPlane) {
  self->farPlaneChanged(farPlane);
}

//  void Qt3DRender::QCameraLens::fieldOfViewChanged(float fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens18fieldOfViewChangedEf(
    Qt3DRender::QCameraLens *self,
    float fieldOfView) {
  self->fieldOfViewChanged(fieldOfView);
}

//  void Qt3DRender::QCameraLens::aspectRatioChanged(float aspectRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens18aspectRatioChangedEf(
    Qt3DRender::QCameraLens *self,
    float aspectRatio) {
  self->aspectRatioChanged(aspectRatio);
}

//  void Qt3DRender::QCameraLens::leftChanged(float left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens11leftChangedEf(
    Qt3DRender::QCameraLens *self,
    float left) {
  self->leftChanged(left);
}

//  void Qt3DRender::QCameraLens::rightChanged(float right)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens12rightChangedEf(
    Qt3DRender::QCameraLens *self,
    float right) {
  self->rightChanged(right);
}

//  void Qt3DRender::QCameraLens::bottomChanged(float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens13bottomChangedEf(
    Qt3DRender::QCameraLens *self,
    float bottom) {
  self->bottomChanged(bottom);
}

//  void Qt3DRender::QCameraLens::topChanged(float top)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens10topChangedEf(
    Qt3DRender::QCameraLens *self,
    float top) {
  self->topChanged(top);
}

//  void Qt3DRender::QCameraLens::projectionMatrixChanged(const QMatrix4x4
//      &projectionMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens23projectionMatrixChangedERK10QMatrix4x4(
    Qt3DRender::QCameraLens *self,
    const QMatrix4x4 *projectionMatrix) {
  self->projectionMatrixChanged(*projectionMatrix);
}

//  void Qt3DRender::QCameraLens::exposureChanged(float exposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens15exposureChangedEf(
    Qt3DRender::QCameraLens *self,
    float exposure) {
  self->exposureChanged(exposure);
}

//  void Qt3DRender::QCameraLens::viewSphere(const QVector3D &center, float
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QCameraLens10viewSphereERK9QVector3Df(
    Qt3DRender::QCameraLens *self,
    const QVector3D *center,
    float radius) {
  self->viewSphere(*center, radius);
}

//  Qt3DRender::QCameraLens::QCameraLens(QCameraLensPrivate &dd, QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLens *ritual_ZN10Qt3DRender11QCameraLensC1ERNS_18QCameraLensPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QCameraLensPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QCameraLens(*dd, parent);
}

//  QCameraLensPrivate *Qt3DRender::QCameraLens::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraLensPrivate *ritual_ZN10Qt3DRender11QCameraLens6d_funcEv(
    Qt3DRender::QCameraLens *self) {
  return self->d_func();
}

//  const QCameraLensPrivate *Qt3DRender::QCameraLens::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QCameraLensPrivate *ritual_ZNK10Qt3DRender11QCameraLens6d_funcEv(
    const Qt3DRender::QCameraLens *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QCameraLens, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QCameraLens(
    Qt3DRender::QCameraLens *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QCameraLens *>(self)->take(key, call);
}
