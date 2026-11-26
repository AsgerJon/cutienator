//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qactioninput.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qactioninput.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DInput::QActionInput that Python can take functions over in. Every Qt3DInput::QActionInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QActionInputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QActionInputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionInputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionInputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionInputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionInputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionInputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QActionInput : public Qt3DInput::QActionInput {
public:
  using Qt3DInput::QActionInput::QActionInput;
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
      CuteQt3DInput_QActionInputCall0 call = reinterpret_cast<CuteQt3DInput_QActionInputCall0>(taken[0]);
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
      CuteQt3DInput_QActionInputCall1 call = reinterpret_cast<CuteQt3DInput_QActionInputCall1>(taken[1]);
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
      CuteQt3DInput_QActionInputCall2 call = reinterpret_cast<CuteQt3DInput_QActionInputCall2>(taken[2]);
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
      CuteQt3DInput_QActionInputCall3 call = reinterpret_cast<CuteQt3DInput_QActionInputCall3>(taken[3]);
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
      CuteQt3DInput_QActionInputCall4 call = reinterpret_cast<CuteQt3DInput_QActionInputCall4>(taken[4]);
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
      CuteQt3DInput_QActionInputCall5 call = reinterpret_cast<CuteQt3DInput_QActionInputCall5>(taken[5]);
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
      CuteQt3DInput_QActionInputCall6 call = reinterpret_cast<CuteQt3DInput_QActionInputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QActionInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput12QActionInput10metaObjectEv(
    const Qt3DInput::QActionInput *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QActionInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput12QActionInput11qt_metacastEPKc(
    Qt3DInput::QActionInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QActionInput::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput12QActionInput11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QActionInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QActionInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput12QActionInput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QActionInput::tr(s, c, n));
}

//  Qt3DInput::QActionInput::QActionInput(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QActionInput *ritual_ZN9Qt3DInput12QActionInputC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QActionInput(parent);
}

//  Qt3DInput::QActionInput::~QActionInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QActionInputD1Ev(Qt3DInput::QActionInput *self) {
  delete self;
}

//  QAbstractPhysicalDevice *Qt3DInput::QActionInput::sourceDevice() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZNK9Qt3DInput12QActionInput12sourceDeviceEv(
    const Qt3DInput::QActionInput *self) {
  return self->sourceDevice();
}

//  QList<int> Qt3DInput::QActionInput::buttons() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput12QActionInput7buttonsEv(
    const Qt3DInput::QActionInput *self) {
  return new QList<int>(self->buttons());
}

//  void Qt3DInput::QActionInput::setSourceDevice(QAbstractPhysicalDevice
//      *sourceDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QActionInput15setSourceDeviceEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QActionInput *self,
    Qt3DInput::QAbstractPhysicalDevice *sourceDevice) {
  self->setSourceDevice(sourceDevice);
}

//  void Qt3DInput::QActionInput::setButtons(const QList<int> &buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QActionInput10setButtonsERK5QListIiE(
    Qt3DInput::QActionInput *self,
    const QList<int> *buttons) {
  self->setButtons(*buttons);
}

//  void Qt3DInput::QActionInput::sourceDeviceChanged(QAbstractPhysicalDevice
//      *sourceDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QActionInput19sourceDeviceChangedEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QActionInput *self,
    Qt3DInput::QAbstractPhysicalDevice *sourceDevice) {
  self->sourceDeviceChanged(sourceDevice);
}

//  void Qt3DInput::QActionInput::buttonsChanged(const QList<int> &buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QActionInput14buttonsChangedERK5QListIiE(
    Qt3DInput::QActionInput *self,
    const QList<int> *buttons) {
  self->buttonsChanged(*buttons);
}

//  QActionInputPrivate *Qt3DInput::QActionInput::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QActionInputPrivate *ritual_ZN9Qt3DInput12QActionInput6d_funcEv(
    Qt3DInput::QActionInput *self) {
  return self->d_func();
}

//  const QActionInputPrivate *Qt3DInput::QActionInput::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QActionInputPrivate *ritual_ZNK9Qt3DInput12QActionInput6d_funcEv(
    const Qt3DInput::QActionInput *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QActionInput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QActionInput(
    Qt3DInput::QActionInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QActionInput *>(self)->take(key, call);
}

//  a QList<int> a ritual of Qt3DInput::QActionInput gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QActionInput__QList_int(QList<int> *self) {
  delete self;
}
