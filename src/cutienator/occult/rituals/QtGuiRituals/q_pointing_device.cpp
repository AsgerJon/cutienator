//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpointingdevice.h>
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPointingDevice that Python can take functions over in. Every QPointingDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPointingDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPointingDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPointingDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPointingDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPointingDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPointingDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPointingDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPointingDevice : public QPointingDevice {
public:
  using QPointingDevice::QPointingDevice;
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
      CuteQPointingDeviceCall0 call = reinterpret_cast<CuteQPointingDeviceCall0>(taken[0]);
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
      CuteQPointingDeviceCall1 call = reinterpret_cast<CuteQPointingDeviceCall1>(taken[1]);
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
      CuteQPointingDeviceCall2 call = reinterpret_cast<CuteQPointingDeviceCall2>(taken[2]);
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
      CuteQPointingDeviceCall3 call = reinterpret_cast<CuteQPointingDeviceCall3>(taken[3]);
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
      CuteQPointingDeviceCall4 call = reinterpret_cast<CuteQPointingDeviceCall4>(taken[4]);
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
      CuteQPointingDeviceCall5 call = reinterpret_cast<CuteQPointingDeviceCall5>(taken[5]);
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
      CuteQPointingDeviceCall6 call = reinterpret_cast<CuteQPointingDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPointingDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QPointingDevice10metaObjectEv(
    const QPointingDevice *self) {
  return self->metaObject();
}

//  void *QPointingDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QPointingDevice11qt_metacastEPKc(
    QPointingDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPointingDevice::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QPointingDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QPointingDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPointingDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPointingDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPointingDevice::tr(s, c, n));
}

//  QPointingDevicePrivate *QPointingDevice::d_func()
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate *ritual_ZN15QPointingDevice6d_funcEv(
    QPointingDevice *self) {
  return self->d_func();
}

//  const QPointingDevicePrivate *QPointingDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QPointingDevicePrivate *ritual_ZNK15QPointingDevice6d_funcEv(
    const QPointingDevice *self) {
  return self->d_func();
}

//  QPointingDevice::QPointingDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN15QPointingDeviceC1EP7QObject(QObject *parent) {
  return new CuteQPointingDevice(parent);
}

//  QPointingDevice::~QPointingDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDeviceD1Ev(QPointingDevice *self) {
  delete self;
}

//  QPointingDevice::QPointingDevice(const QString &name, qint64 systemId,
//      QInputDevice::DeviceType devType, PointerType pType, Capabilities
//      caps, int maxPoints, int buttonCount, const QString &seatName,
//      QPointingDeviceUniqueId uniqueId, QObject *parent)
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN15QPointingDeviceC1ERK7QStringxN12QInputDevice10DeviceTypeENS_11PointerTypeE6QFlagsINS3_10CapabilityEEiiS2_23QPointingDeviceUniqueIdP7QObject(
    const QString *name,
    qint64 systemId,
    QInputDevice::DeviceType devType,
    QPointingDevice::PointerType pType,
    int caps,
    int maxPoints,
    int buttonCount,
    const QString *seatName,
    const QPointingDeviceUniqueId *uniqueId,
    QObject *parent) {
  return new CuteQPointingDevice(
      *name,
      systemId,
      devType,
      pType,
      QFlags<QInputDevice::Capability>::fromInt(caps),
      maxPoints,
      buttonCount,
      *seatName,
      *uniqueId,
      parent);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPointingDevice::setType(DeviceType devType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice7setTypeEN12QInputDevice10DeviceTypeE(
    QPointingDevice *self,
    QInputDevice::DeviceType devType) {
  self->setType(devType);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPointingDevice::setCapabilities(QInputDevice::Capabilities caps)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice15setCapabilitiesE6QFlagsIN12QInputDevice10CapabilityEE(
    QPointingDevice *self,
    int caps) {
  self->setCapabilities(QFlags<QInputDevice::Capability>::fromInt(caps));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QPointingDevice::setMaximumTouchPoints(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice21setMaximumTouchPointsEi(
    QPointingDevice *self,
    int c) {
  self->setMaximumTouchPoints(c);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  PointerType QPointingDevice::pointerType() const
extern "C" Q_DECL_EXPORT
QPointingDevice::PointerType ritual_ZNK15QPointingDevice11pointerTypeEv(
    const QPointingDevice *self) {
  return self->pointerType();
}

//  int QPointingDevice::maximumPoints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPointingDevice13maximumPointsEv(
    const QPointingDevice *self) {
  return self->maximumPoints();
}

//  int QPointingDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPointingDevice11buttonCountEv(const QPointingDevice *self) {
  return self->buttonCount();
}

//  QPointingDeviceUniqueId QPointingDevice::uniqueId() const
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZNK15QPointingDevice8uniqueIdEv(
    const QPointingDevice *self) {
  return new QPointingDeviceUniqueId(self->uniqueId());
}

//  const QPointingDevice *QPointingDevice::primaryPointingDevice(const
//      QString &seatName)
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZN15QPointingDevice21primaryPointingDeviceERK7QString(
    const QString *seatName) {
  return QPointingDevice::primaryPointingDevice(*seatName);
}

//  bool QPointingDevice::operator==(const QPointingDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QPointingDeviceeqERKS_(
    const QPointingDevice *self,
    const QPointingDevice *other) {
  return self->operator==(*other);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QPointingDevice::grabChanged(QObject *grabber, GrabTransition
//      transition, const QPointerEvent *event, const QEventPoint &point)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QPointingDevice11grabChangedEP7QObjectNS_14GrabTransitionEPK13QPointerEventRK11QEventPoint(
    const QPointingDevice *self,
    QObject *grabber,
    QPointingDevice::GrabTransition transition,
    const QPointerEvent *event,
    const QEventPoint *point) {
  self->grabChanged(grabber, transition, event, *point);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  QPointingDevice::QPointingDevice(QPointingDevicePrivate &d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN15QPointingDeviceC1ER22QPointingDevicePrivateP7QObject(
    QPointingDevicePrivate *d,
    QObject *parent) {
  return new CuteQPointingDevice(*d, parent);
}

//  a Python function taken by a CuteQPointingDevice, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPointingDevice(
    QPointingDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPointingDevice *>(self)->take(key, call);
}
