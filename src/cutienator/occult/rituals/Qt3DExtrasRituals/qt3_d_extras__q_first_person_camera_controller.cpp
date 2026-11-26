//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qfirstpersoncameracontroller.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DExtras/qfirstpersoncameracontroller.h>
#include <QtCore/qstring.h>
#include <Qt3DExtras/qabstractcameracontroller.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QFirstPersonCameraController that Python can take functions over in. Every Qt3DExtras::QFirstPersonCameraController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall0)(const void *, const Qt3DExtras::QAbstractCameraController::InputState *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QFirstPersonCameraControllerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QFirstPersonCameraControllerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QFirstPersonCameraControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QFirstPersonCameraController : public Qt3DExtras::QFirstPersonCameraController {
public:
  using Qt3DExtras::QFirstPersonCameraController::QFirstPersonCameraController;
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

  //  void Qt3DExtras::QFirstPersonCameraController::moveCamera(const
  //      QAbstractCameraController::InputState &state, float dt)
  void moveCamera(
      const Qt3DExtras::QAbstractCameraController::InputState &state,
      float dt) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QFirstPersonCameraControllerCall0 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall0>(taken[0]);
      call(this, &state, dt, &handled);
      if (handled) return;
    }
    Qt3DExtras::QFirstPersonCameraController::moveCamera(state, dt);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QFirstPersonCameraControllerCall1 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall1>(taken[1]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall2 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall2>(taken[2]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall3 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall3>(taken[3]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall4 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall4>(taken[4]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall5 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall5>(taken[5]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall6 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall6>(taken[6]);
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
      CuteQt3DExtras_QFirstPersonCameraControllerCall7 call = reinterpret_cast<CuteQt3DExtras_QFirstPersonCameraControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QFirstPersonCameraController::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras28QFirstPersonCameraController10metaObjectEv(
    const Qt3DExtras::QFirstPersonCameraController *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QFirstPersonCameraController::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras28QFirstPersonCameraController11qt_metacastEPKc(
    Qt3DExtras::QFirstPersonCameraController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DExtras::QFirstPersonCameraController::qt_metacall(QMetaObject::Ca
//      ll a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras28QFirstPersonCameraController11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QFirstPersonCameraController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QFirstPersonCameraController::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras28QFirstPersonCameraController2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QFirstPersonCameraController::tr(s, c, n));
}

//  Qt3DExtras::QFirstPersonCameraController::QFirstPersonCameraController(Qt
//      3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QFirstPersonCameraController *ritual_ZN10Qt3DExtras28QFirstPersonCameraControllerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QFirstPersonCameraController(parent);
}

//  Qt3DExtras::QFirstPersonCameraController::~QFirstPersonCameraController()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras28QFirstPersonCameraControllerD1Ev(
    Qt3DExtras::QFirstPersonCameraController *self) {
  delete self;
}

//  void Qt3DExtras::QFirstPersonCameraController::moveCamera(const
//      QAbstractCameraController::InputState &state, float dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras28QFirstPersonCameraController10moveCameraERKNS_25QAbstractCameraController10InputStateEf(
    Qt3DExtras::QFirstPersonCameraController *self,
    const Qt3DExtras::QAbstractCameraController::InputState *state,
    float dt) {
  self->moveCamera(*state, dt);
}

//  a Python function taken by a CuteQt3DExtras_QFirstPersonCameraController,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QFirstPersonCameraController(
    Qt3DExtras::QFirstPersonCameraController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QFirstPersonCameraController *>(self)->take(key, call);
}

//  void Qt3DExtras::QFirstPersonCameraController::moveCamera(const
//      QAbstractCameraController::InputState &state, float dt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DExtras28QFirstPersonCameraController10moveCameraERKNS_25QAbstractCameraController10InputStateEf(
    Qt3DExtras::QFirstPersonCameraController *self,
    const Qt3DExtras::QAbstractCameraController::InputState *state,
    float dt) {
  self->Qt3DExtras::QFirstPersonCameraController::moveCamera(*state, dt);
}
