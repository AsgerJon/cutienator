//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbusdevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QModbusDevice that Python can take functions over in. Every QModbusDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusDeviceCall0)(const void *, int *);
typedef void (*CuteQModbusDeviceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusDeviceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusDeviceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusDeviceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusDeviceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusDeviceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusDeviceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusDeviceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusDevice : public QModbusDevice {
public:
  using QModbusDevice::QModbusDevice;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QModbusDevice4openEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QModbusDevice5closeEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QModbusDevice::open()
  bool open() override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusDeviceCall0 call = reinterpret_cast<CuteQModbusDeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QModbusDevice::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusDeviceCall1 call = reinterpret_cast<CuteQModbusDeviceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusDeviceCall2 call = reinterpret_cast<CuteQModbusDeviceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQModbusDeviceCall3 call = reinterpret_cast<CuteQModbusDeviceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQModbusDeviceCall4 call = reinterpret_cast<CuteQModbusDeviceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQModbusDeviceCall5 call = reinterpret_cast<CuteQModbusDeviceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQModbusDeviceCall6 call = reinterpret_cast<CuteQModbusDeviceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQModbusDeviceCall7 call = reinterpret_cast<CuteQModbusDeviceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQModbusDeviceCall8 call = reinterpret_cast<CuteQModbusDeviceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QModbusDevice10metaObjectEv(
    const QModbusDevice *self) {
  return self->metaObject();
}

//  QString QModbusDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QModbusDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusDevice::tr(s, c, n));
}

//  QModbusDevicePrivate *QModbusDevice::d_func()
extern "C" Q_DECL_EXPORT
QModbusDevicePrivate *ritual_ZN13QModbusDevice6d_funcEv(
    QModbusDevice *self) {
  return self->d_func();
}

//  const QModbusDevicePrivate *QModbusDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QModbusDevicePrivate *ritual_ZNK13QModbusDevice6d_funcEv(
    const QModbusDevice *self) {
  return self->d_func();
}

//  QModbusDevice::~QModbusDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDeviceD1Ev(QModbusDevice *self) {
  delete self;
}

//  QVariant QModbusDevice::connectionParameter(ConnectionParameter
//      parameter) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QModbusDevice19connectionParameterENS_19ConnectionParameterE(
    const QModbusDevice *self,
    QModbusDevice::ConnectionParameter parameter) {
  return new QVariant(self->connectionParameter(parameter));
}

//  void QModbusDevice::setConnectionParameter(ConnectionParameter parameter,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDevice22setConnectionParameterENS_19ConnectionParameterERK8QVariant(
    QModbusDevice *self,
    QModbusDevice::ConnectionParameter parameter,
    const QVariant *value) {
  self->setConnectionParameter(parameter, *value);
}

//  bool QModbusDevice::connectDevice()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusDevice13connectDeviceEv(QModbusDevice *self) {
  return self->connectDevice();
}

//  void QModbusDevice::disconnectDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDevice16disconnectDeviceEv(QModbusDevice *self) {
  self->disconnectDevice();
}

//  State QModbusDevice::state() const
extern "C" Q_DECL_EXPORT
QModbusDevice::State ritual_ZNK13QModbusDevice5stateEv(
    const QModbusDevice *self) {
  return self->state();
}

//  Error QModbusDevice::error() const
extern "C" Q_DECL_EXPORT
QModbusDevice::Error ritual_ZNK13QModbusDevice5errorEv(
    const QModbusDevice *self) {
  return self->error();
}

//  QString QModbusDevice::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QModbusDevice11errorStringEv(
    const QModbusDevice *self) {
  return new QString(self->errorString());
}

//  QIODevice *QModbusDevice::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13QModbusDevice6deviceEv(const QModbusDevice *self) {
  return self->device();
}

//  void QModbusDevice::setState(QModbusDevice::State newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDevice8setStateENS_5StateE(
    QModbusDevice *self,
    QModbusDevice::State newState) {
  self->setState(newState);
}

//  void QModbusDevice::setError(const QString &errorText,
//      QModbusDevice::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDevice8setErrorERK7QStringNS_5ErrorE(
    QModbusDevice *self,
    const QString *errorText,
    QModbusDevice::Error error) {
  self->setError(*errorText, error);
}

//  bool QModbusDevice::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QModbusDevice4openEv(QModbusDevice *self) {
  return self->open();
}

//  void QModbusDevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QModbusDevice5closeEv(QModbusDevice *self) {
  self->close();
}

//  a Python function taken by a CuteQModbusDevice, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusDevice(
    QModbusDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusDevice *>(self)->take(key, call);
}
