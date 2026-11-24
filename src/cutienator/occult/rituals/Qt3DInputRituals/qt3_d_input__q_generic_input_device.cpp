//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qgenericinputdevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qgenericinputdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QGenericInputDevice that Python can take functions over in. Every Qt3DInput::QGenericInputDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DInput_QGenericInputDeviceCall0)(const void *, int *);
typedef int (*CuteQt3DInput_QGenericInputDeviceCall1)(const void *, int *);
typedef int (*CuteQt3DInput_QGenericInputDeviceCall2)(const void *, const QString *, int *);
typedef int (*CuteQt3DInput_QGenericInputDeviceCall3)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QGenericInputDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QGenericInputDeviceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QGenericInputDeviceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QGenericInputDeviceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QGenericInputDeviceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QGenericInputDeviceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QGenericInputDeviceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QGenericInputDevice : public Qt3DInput::QGenericInputDevice {
public:
  using Qt3DInput::QGenericInputDevice::QGenericInputDevice;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifierERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentifierERK7QString")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int Qt3DInput::QAbstractPhysicalDevice::axisCount() const
  int axisCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall0 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DInput::QAbstractPhysicalDevice::axisCount();
  }

  //  int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const
  int buttonCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall1 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DInput::QAbstractPhysicalDevice::buttonCount();
  }

  //  int Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(const QString
  //      &name) const
  int axisIdentifier(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall2 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall2>(taken[2]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(name);
  }

  //  int Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(const
  //      QString &name) const
  int buttonIdentifier(const QString &name) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall3 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall3>(taken[3]);
      int given = call(this, &name, &handled);
      if (handled) return given;
    }
    return Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(name);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall4 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall5 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall6 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall7 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall8 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall9 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DInput_QGenericInputDeviceCall10 call = reinterpret_cast<CuteQt3DInput_QGenericInputDeviceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QGenericInputDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput19QGenericInputDevice10metaObjectEv(
    const Qt3DInput::QGenericInputDevice *self) {
  return self->metaObject();
}

//  QString Qt3DInput::QGenericInputDevice::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput19QGenericInputDevice2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QGenericInputDevice::tr(s, c, n));
}

//  a Python function taken by a CuteQt3DInput_QGenericInputDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QGenericInputDevice(
    Qt3DInput::QGenericInputDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QGenericInputDevice *>(self)->take(key, call);
}
