//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickInput/6.12.0/Qt3DQuickInput/private/quick3dlogicaldevice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickInput/6.12.0/Qt3DQuickInput/private/qt3dquickinput_global_p.h>
#include <Qt3DQuickInput/Qt3DQuickInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickInput/6.12.0/Qt3DQuickInput/private/quick3dlogicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::Input::Quick::Quick3DLogicalDevice that Python can take functions over in. Every Qt3DInput::Input::Quick::Quick3DLogicalDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_Input_Quick_Quick3DLogicalDevice : public Qt3DInput::Input::Quick::Quick3DLogicalDevice {
public:
  using Qt3DInput::Input::Quick::Quick3DLogicalDevice::Quick3DLogicalDevice;
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall0 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall0>(taken[0]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall1 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall1>(taken[1]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall2 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall2>(taken[2]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall3 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall3>(taken[3]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall4 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall4>(taken[4]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall5 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall5>(taken[5]);
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
      CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall6 call = reinterpret_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DInput::Input::Quick::Quick3DLogicalDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput5Input5Quick20Quick3DLogicalDevice10metaObjectEv(
    const Qt3DInput::Input::Quick::Quick3DLogicalDevice *self) {
  return self->metaObject();
}

//  void *Qt3DInput::Input::Quick::Quick3DLogicalDevice::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDevice11qt_metacastEPKc(
    Qt3DInput::Input::Quick::Quick3DLogicalDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::Input::Quick::Quick3DLogicalDevice::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::Input::Quick::Quick3DLogicalDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::Input::Quick::Quick3DLogicalDevice::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDevice2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DInput::Input::Quick::Quick3DLogicalDevice::tr(
          s,
          c,
          n));
}

//  Qt3DInput::Input::Quick::Quick3DLogicalDevice::Quick3DLogicalDevice(QObje
//      ct *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::Quick::Quick3DLogicalDevice *ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDeviceC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DInput_Input_Quick_Quick3DLogicalDevice(parent);
}

//  QLogicalDevice
//      *Qt3DInput::Input::Quick::Quick3DLogicalDevice::parentLogicalDevice()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::QLogicalDevice *ritual_ZNK9Qt3DInput5Input5Quick20Quick3DLogicalDevice19parentLogicalDeviceEv(
    const Qt3DInput::Input::Quick::Quick3DLogicalDevice *self) {
  return self->parentLogicalDevice();
}

//  QQmlListProperty<QAxis>
//      Qt3DInput::Input::Quick::Quick3DLogicalDevice::qmlAxes()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DInput::QAxis> *ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDevice7qmlAxesEv(
    Qt3DInput::Input::Quick::Quick3DLogicalDevice *self) {
  return new QQmlListProperty<Qt3DInput::QAxis>(self->qmlAxes());
}

//  QQmlListProperty<QAction>
//      Qt3DInput::Input::Quick::Quick3DLogicalDevice::qmlActions()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DInput::QAction> *ritual_ZN9Qt3DInput5Input5Quick20Quick3DLogicalDevice10qmlActionsEv(
    Qt3DInput::Input::Quick::Quick3DLogicalDevice *self) {
  return new QQmlListProperty<Qt3DInput::QAction>(self->qmlActions());
}

//  a Python function taken by a
//      CuteQt3DInput_Input_Quick_Quick3DLogicalDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_Quick_Quick3DLogicalDevice(
    Qt3DInput::Input::Quick::Quick3DLogicalDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_Quick_Quick3DLogicalDevice *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DInput::QAxis> a ritual of
//      Qt3DInput::Input::Quick::Quick3DLogicalDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_Quick_Quick3DLogicalDevice__QQmlListProperty_Qt3DInput_QAxis(
    QQmlListProperty<Qt3DInput::QAxis> *self) {
  delete self;
}

//  a QQmlListProperty<Qt3DInput::QAction> a ritual of
//      Qt3DInput::Input::Quick::Quick3DLogicalDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_Quick_Quick3DLogicalDevice__QQmlListProperty_Qt3DInput_QAction(
    QQmlListProperty<Qt3DInput::QAction> *self) {
  delete self;
}
