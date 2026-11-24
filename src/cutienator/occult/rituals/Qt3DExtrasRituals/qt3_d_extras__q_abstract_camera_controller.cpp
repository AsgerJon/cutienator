//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qabstractcameracontroller.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DExtras/qabstractcameracontroller.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QAbstractCameraController that Python can take functions over in. Every Qt3DExtras::QAbstractCameraController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall0)(const void *, const Qt3DExtras::QAbstractCameraController::InputState *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QAbstractCameraControllerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QAbstractCameraControllerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QAbstractCameraControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QAbstractCameraController : public Qt3DExtras::QAbstractCameraController {
public:
  using Qt3DExtras::QAbstractCameraController::QAbstractCameraController;
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

  //  void Qt3DExtras::QAbstractCameraController::moveCamera(const
  //      InputState &state, float dt)
  void moveCamera(
      const Qt3DExtras::QAbstractCameraController::InputState &state,
      float dt) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractCameraControllerCall0 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall0>(taken[0]);
      call(this, &state, dt, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractCameraControllerCall1 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall1>(taken[1]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall2 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall2>(taken[2]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall3 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall3>(taken[3]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall4 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall4>(taken[4]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall5 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall5>(taken[5]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall6 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall6>(taken[6]);
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
      CuteQt3DExtras_QAbstractCameraControllerCall7 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QAbstractCameraController::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras25QAbstractCameraController10metaObjectEv(
    const Qt3DExtras::QAbstractCameraController *self) {
  return self->metaObject();
}

//  QString Qt3DExtras::QAbstractCameraController::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras25QAbstractCameraController2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QAbstractCameraController::tr(s, c, n));
}

//  void Qt3DExtras::QAbstractCameraController::moveCamera(const InputState
//      &state, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras25QAbstractCameraController10moveCameraERKNS0_10InputStateEf(
    Qt3DExtras::QAbstractCameraController *self,
    const Qt3DExtras::QAbstractCameraController::InputState *state,
    float dt) {
  self->moveCamera(*state, dt);
}

//  QAbstractCameraControllerPrivate
//      *Qt3DExtras::QAbstractCameraController::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QAbstractCameraControllerPrivate *ritual_ZN10Qt3DExtras25QAbstractCameraController6d_funcEv(
    Qt3DExtras::QAbstractCameraController *self) {
  return self->d_func();
}

//  const QAbstractCameraControllerPrivate
//      *Qt3DExtras::QAbstractCameraController::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QAbstractCameraControllerPrivate *ritual_ZNK10Qt3DExtras25QAbstractCameraController6d_funcEv(
    const Qt3DExtras::QAbstractCameraController *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QAbstractCameraController,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QAbstractCameraController(
    Qt3DExtras::QAbstractCameraController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QAbstractCameraController *>(self)->take(key, call);
}
