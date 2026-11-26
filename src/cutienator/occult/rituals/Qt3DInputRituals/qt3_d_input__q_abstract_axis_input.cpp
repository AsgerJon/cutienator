//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qabstractaxisinput.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qabstractaxisinput.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QAbstractAxisInput that Python can take functions over in. Every Qt3DInput::QAbstractAxisInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAbstractAxisInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAbstractAxisInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractAxisInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractAxisInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractAxisInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractAxisInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractAxisInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAbstractAxisInput : public Qt3DInput::QAbstractAxisInput {
public:
  using Qt3DInput::QAbstractAxisInput::QAbstractAxisInput;
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
      CuteQt3DInput_QAbstractAxisInputCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall0>(taken[0]);
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
      CuteQt3DInput_QAbstractAxisInputCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall1>(taken[1]);
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
      CuteQt3DInput_QAbstractAxisInputCall2 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall2>(taken[2]);
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
      CuteQt3DInput_QAbstractAxisInputCall3 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall3>(taken[3]);
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
      CuteQt3DInput_QAbstractAxisInputCall4 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall4>(taken[4]);
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
      CuteQt3DInput_QAbstractAxisInputCall5 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall5>(taken[5]);
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
      CuteQt3DInput_QAbstractAxisInputCall6 call = reinterpret_cast<CuteQt3DInput_QAbstractAxisInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAbstractAxisInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput18QAbstractAxisInput10metaObjectEv(
    const Qt3DInput::QAbstractAxisInput *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAbstractAxisInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput18QAbstractAxisInput11qt_metacastEPKc(
    Qt3DInput::QAbstractAxisInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAbstractAxisInput::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput18QAbstractAxisInput11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAbstractAxisInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAbstractAxisInput::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput18QAbstractAxisInput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAbstractAxisInput::tr(s, c, n));
}

//  Qt3DInput::QAbstractAxisInput::~QAbstractAxisInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput18QAbstractAxisInputD1Ev(
    Qt3DInput::QAbstractAxisInput *self) {
  delete self;
}

//  QAbstractPhysicalDevice *Qt3DInput::QAbstractAxisInput::sourceDevice()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZNK9Qt3DInput18QAbstractAxisInput12sourceDeviceEv(
    const Qt3DInput::QAbstractAxisInput *self) {
  return self->sourceDevice();
}

//  void
//      Qt3DInput::QAbstractAxisInput::setSourceDevice(QAbstractPhysicalDevic
//      e *sourceDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput18QAbstractAxisInput15setSourceDeviceEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QAbstractAxisInput *self,
    Qt3DInput::QAbstractPhysicalDevice *sourceDevice) {
  self->setSourceDevice(sourceDevice);
}

//  void Qt3DInput::QAbstractAxisInput::sourceDeviceChanged(QAbstractPhysical
//      Device *sourceDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput18QAbstractAxisInput19sourceDeviceChangedEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QAbstractAxisInput *self,
    Qt3DInput::QAbstractPhysicalDevice *sourceDevice) {
  self->sourceDeviceChanged(sourceDevice);
}

//  Qt3DInput::QAbstractAxisInput::QAbstractAxisInput(QAbstractAxisInputPriva
//      te &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractAxisInput *ritual_ZN9Qt3DInput18QAbstractAxisInputC1ERNS_25QAbstractAxisInputPrivateEPN8Qt3DCore5QNodeE(
    Qt3DInput::QAbstractAxisInputPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAbstractAxisInput(*dd, parent);
}

//  QAbstractAxisInputPrivate *Qt3DInput::QAbstractAxisInput::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractAxisInputPrivate *ritual_ZN9Qt3DInput18QAbstractAxisInput6d_funcEv(
    Qt3DInput::QAbstractAxisInput *self) {
  return self->d_func();
}

//  const QAbstractAxisInputPrivate *Qt3DInput::QAbstractAxisInput::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractAxisInputPrivate *ritual_ZNK9Qt3DInput18QAbstractAxisInput6d_funcEv(
    const Qt3DInput::QAbstractAxisInput *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAbstractAxisInput, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractAxisInput(
    Qt3DInput::QAbstractAxisInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractAxisInput *>(self)->take(key, call);
}
