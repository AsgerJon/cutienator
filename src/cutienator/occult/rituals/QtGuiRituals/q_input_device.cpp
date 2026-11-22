//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qinputdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qinputdevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QInputDevice that Python can take functions over in. Every QInputDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQInputDeviceCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQInputDeviceCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQInputDeviceCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQInputDeviceCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQInputDeviceCall4)(const void *, QEvent *, int *);
typedef void (*CuteQInputDeviceCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQInputDeviceCall6)(const void *, const QMetaMethod *, int *);
class CuteQInputDevice : public QInputDevice {
public:
  using QInputDevice::QInputDevice;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQInputDeviceCall0 call = reinterpret_cast<CuteQInputDeviceCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQInputDeviceCall1 call = reinterpret_cast<CuteQInputDeviceCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQInputDeviceCall2 call = reinterpret_cast<CuteQInputDeviceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQInputDeviceCall3 call = reinterpret_cast<CuteQInputDeviceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQInputDeviceCall4 call = reinterpret_cast<CuteQInputDeviceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQInputDeviceCall5 call = reinterpret_cast<CuteQInputDeviceCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQInputDeviceCall6 call = reinterpret_cast<CuteQInputDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QInputDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QInputDevice10metaObjectEv(
    const QInputDevice *self) {
  return self->metaObject();
}

//  QString QInputDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputDevice::tr(s, c, n));
}

//  QInputDevice::QInputDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QInputDevice *ritual_ZN12QInputDeviceC1EP7QObject(QObject *parent) {
  return new CuteQInputDevice(parent);
}

//  QInputDevice::~QInputDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDeviceD1Ev(QInputDevice *self) {
  delete self;
}

//  QInputDevice::QInputDevice(const QString &name, qint64 systemId,
//      DeviceType type, const QString &seatName, QObject *parent)
extern "C" Q_DECL_EXPORT
QInputDevice *ritual_ZN12QInputDeviceC1ERK7QStringxNS_10DeviceTypeES2_P7QObject(
    const QString *name,
    qint64 systemId,
    QInputDevice::DeviceType type,
    const QString *seatName,
    QObject *parent) {
  return new CuteQInputDevice(*name, systemId, type, *seatName, parent);
}

//  QString QInputDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDevice4nameEv(const QInputDevice *self) {
  return new QString(self->name());
}

//  DeviceType QInputDevice::type() const
extern "C" Q_DECL_EXPORT
QInputDevice::DeviceType ritual_ZNK12QInputDevice4typeEv(
    const QInputDevice *self) {
  return self->type();
}

//  Capabilities QInputDevice::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDevice12capabilitiesEv(const QInputDevice *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  bool QInputDevice::hasCapability(Capability cap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDevice13hasCapabilityENS_10CapabilityE(
    const QInputDevice *self,
    QInputDevice::Capability cap) {
  return self->hasCapability(cap);
}

//  qint64 QInputDevice::systemId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QInputDevice8systemIdEv(const QInputDevice *self) {
  return self->systemId();
}

//  QString QInputDevice::seatName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDevice8seatNameEv(const QInputDevice *self) {
  return new QString(self->seatName());
}

//  QRect QInputDevice::availableVirtualGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QInputDevice24availableVirtualGeometryEv(
    const QInputDevice *self) {
  return new QRect(self->availableVirtualGeometry());
}

//  const QInputDevice *QInputDevice::primaryKeyboard(const QString
//      &seatName)
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZN12QInputDevice15primaryKeyboardERK7QString(
    const QString *seatName) {
  return QInputDevice::primaryKeyboard(*seatName);
}

//  a Python function taken by a CuteQInputDevice, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QInputDevice(
    QInputDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQInputDevice *>(self)->take(key, call);
}
