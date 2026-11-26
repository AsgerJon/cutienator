//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qorbitcameracontroller.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DExtras/qorbitcameracontroller.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <Qt3DExtras/qabstractcameracontroller.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QOrbitCameraController that Python can take functions over in. Every Qt3DExtras::QOrbitCameraController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall0)(const void *, const Qt3DExtras::QAbstractCameraController::InputState *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QOrbitCameraControllerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QOrbitCameraControllerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QOrbitCameraControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QOrbitCameraController : public Qt3DExtras::QOrbitCameraController {
public:
  using Qt3DExtras::QOrbitCameraController::QOrbitCameraController;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DExtras25QAbstractCameraController10moveCameraERKNS0_10InputStateEf")) {
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

  //  void Qt3DExtras::QOrbitCameraController::moveCamera(const
  //      QAbstractCameraController::InputState &state, float dt)
  void moveCamera(
      const Qt3DExtras::QAbstractCameraController::InputState &state,
      float dt) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QOrbitCameraControllerCall0 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall0>(taken[0]);
      call(this, &state, dt, &handled);
      if (handled) return;
    }
    Qt3DExtras::QOrbitCameraController::moveCamera(state, dt);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QOrbitCameraControllerCall1 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall1>(taken[1]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall2 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall2>(taken[2]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall3 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall3>(taken[3]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall4 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall4>(taken[4]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall5 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall5>(taken[5]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall6 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall6>(taken[6]);
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
      CuteQt3DExtras_QOrbitCameraControllerCall7 call = reinterpret_cast<CuteQt3DExtras_QOrbitCameraControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QOrbitCameraController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras22QOrbitCameraController10metaObjectEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QOrbitCameraController::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras22QOrbitCameraController11qt_metacastEPKc(
    Qt3DExtras::QOrbitCameraController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QOrbitCameraController::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras22QOrbitCameraController11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QOrbitCameraController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QOrbitCameraController::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras22QOrbitCameraController2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QOrbitCameraController::tr(s, c, n));
}

//  Qt3DExtras::QOrbitCameraController::QOrbitCameraController(Qt3DCore::QNod
//      e *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QOrbitCameraController *ritual_ZN10Qt3DExtras22QOrbitCameraControllerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QOrbitCameraController(parent);
}

//  Qt3DExtras::QOrbitCameraController::~QOrbitCameraController()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraControllerD1Ev(
    Qt3DExtras::QOrbitCameraController *self) {
  delete self;
}

//  float Qt3DExtras::QOrbitCameraController::zoomInLimit() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras22QOrbitCameraController11zoomInLimitEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->zoomInLimit();
}

//  QVector3D Qt3DExtras::QOrbitCameraController::upVector() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DExtras22QOrbitCameraController8upVectorEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return new QVector3D(self->upVector());
}

//  bool Qt3DExtras::QOrbitCameraController::inverseXTranslate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QOrbitCameraController17inverseXTranslateEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->inverseXTranslate();
}

//  bool Qt3DExtras::QOrbitCameraController::inverseYTranslate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QOrbitCameraController17inverseYTranslateEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->inverseYTranslate();
}

//  bool Qt3DExtras::QOrbitCameraController::inversePan() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QOrbitCameraController10inversePanEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->inversePan();
}

//  bool Qt3DExtras::QOrbitCameraController::inverseTilt() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QOrbitCameraController11inverseTiltEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->inverseTilt();
}

//  bool Qt3DExtras::QOrbitCameraController::zoomTranslateViewCenter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras22QOrbitCameraController23zoomTranslateViewCenterEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->zoomTranslateViewCenter();
}

//  void Qt3DExtras::QOrbitCameraController::setZoomInLimit(float
//      zoomInLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController14setZoomInLimitEf(
    Qt3DExtras::QOrbitCameraController *self,
    float zoomInLimit) {
  self->setZoomInLimit(zoomInLimit);
}

//  void Qt3DExtras::QOrbitCameraController::setUpVector(const QVector3D
//      &upVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController11setUpVectorERK9QVector3D(
    Qt3DExtras::QOrbitCameraController *self,
    const QVector3D *upVector) {
  self->setUpVector(*upVector);
}

//  void Qt3DExtras::QOrbitCameraController::setInverseXTranslate(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController20setInverseXTranslateEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->setInverseXTranslate(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::setInverseYTranslate(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController20setInverseYTranslateEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->setInverseYTranslate(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::setInversePan(bool isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController13setInversePanEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->setInversePan(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::setInverseTilt(bool isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController14setInverseTiltEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->setInverseTilt(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::setZoomTranslateViewCenter(bool
//      isTranslate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController26setZoomTranslateViewCenterEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isTranslate) {
  self->setZoomTranslateViewCenter(isTranslate);
}

//  void Qt3DExtras::QOrbitCameraController::zoomInLimitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController18zoomInLimitChangedEv(
    Qt3DExtras::QOrbitCameraController *self) {
  self->zoomInLimitChanged();
}

//  void Qt3DExtras::QOrbitCameraController::upVectorChanged(const QVector3D
//      &upVector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController15upVectorChangedERK9QVector3D(
    Qt3DExtras::QOrbitCameraController *self,
    const QVector3D *upVector) {
  self->upVectorChanged(*upVector);
}

//  void Qt3DExtras::QOrbitCameraController::inverseXTranslateChanged(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController24inverseXTranslateChangedEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->inverseXTranslateChanged(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::inverseYTranslateChanged(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController24inverseYTranslateChangedEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->inverseYTranslateChanged(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::inversePanChanged(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController17inversePanChangedEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->inversePanChanged(isInverse);
}

//  void Qt3DExtras::QOrbitCameraController::inverseTiltChanged(bool
//      isInverse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController18inverseTiltChangedEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isInverse) {
  self->inverseTiltChanged(isInverse);
}

//  void
//      Qt3DExtras::QOrbitCameraController::zoomTranslateViewCenterChanged(bo
//      ol isTranslate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController30zoomTranslateViewCenterChangedEb(
    Qt3DExtras::QOrbitCameraController *self,
    bool isTranslate) {
  self->zoomTranslateViewCenterChanged(isTranslate);
}

//  Qt3DExtras::QOrbitCameraController::QOrbitCameraController(QOrbitCameraCo
//      ntrollerPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QOrbitCameraController *ritual_ZN10Qt3DExtras22QOrbitCameraControllerC1ERNS_29QOrbitCameraControllerPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QOrbitCameraControllerPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QOrbitCameraController(*dd, parent);
}

//  void Qt3DExtras::QOrbitCameraController::moveCamera(const
//      QAbstractCameraController::InputState &state, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras22QOrbitCameraController10moveCameraERKNS_25QAbstractCameraController10InputStateEf(
    Qt3DExtras::QOrbitCameraController *self,
    const Qt3DExtras::QAbstractCameraController::InputState *state,
    float dt) {
  self->moveCamera(*state, dt);
}

//  QOrbitCameraControllerPrivate
//      *Qt3DExtras::QOrbitCameraController::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QOrbitCameraControllerPrivate *ritual_ZN10Qt3DExtras22QOrbitCameraController6d_funcEv(
    Qt3DExtras::QOrbitCameraController *self) {
  return self->d_func();
}

//  const QOrbitCameraControllerPrivate
//      *Qt3DExtras::QOrbitCameraController::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QOrbitCameraControllerPrivate *ritual_ZNK10Qt3DExtras22QOrbitCameraController6d_funcEv(
    const Qt3DExtras::QOrbitCameraController *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QOrbitCameraController, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QOrbitCameraController(
    Qt3DExtras::QOrbitCameraController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QOrbitCameraController *>(self)->take(key, call);
}

//  void Qt3DExtras::QOrbitCameraController::moveCamera(const
//      QAbstractCameraController::InputState &state, float dt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras22QOrbitCameraController10moveCameraERKNS_25QAbstractCameraController10InputStateEf(
    Qt3DExtras::QOrbitCameraController *self,
    const Qt3DExtras::QAbstractCameraController::InputState *state,
    float dt) {
  self->Qt3DExtras::QOrbitCameraController::moveCamera(*state, dt);
}
