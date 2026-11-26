//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qabstractphysicaldevice.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::QAbstractPhysicalDevice that Python can take functions over in. Every Qt3DInput::QAbstractPhysicalDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DInput_QAbstractPhysicalDeviceCall0)(const void *, int *);
typedef int (*CuteQt3DInput_QAbstractPhysicalDeviceCall1)(const void *, int *);
typedef int (*CuteQt3DInput_QAbstractPhysicalDeviceCall2)(const void *, const QString *, int *);
typedef int (*CuteQt3DInput_QAbstractPhysicalDeviceCall3)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAbstractPhysicalDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAbstractPhysicalDeviceCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAbstractPhysicalDevice : public Qt3DInput::QAbstractPhysicalDevice {
public:
  using Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice;
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DInput::QAbstractPhysicalDevice::axisCount();
  }

  //  int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const
  int buttonCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall1>(taken[1]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall2 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall2>(taken[2]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall3 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall3>(taken[3]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall4 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall4>(taken[4]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall5 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall5>(taken[5]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall6 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall6>(taken[6]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall7 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall7>(taken[7]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall8 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall8>(taken[8]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall9 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall9>(taken[9]);
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
      CuteQt3DInput_QAbstractPhysicalDeviceCall10 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAbstractPhysicalDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice10metaObjectEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAbstractPhysicalDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput23QAbstractPhysicalDevice11qt_metacastEPKc(
    Qt3DInput::QAbstractPhysicalDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAbstractPhysicalDevice::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput23QAbstractPhysicalDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAbstractPhysicalDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAbstractPhysicalDevice::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput23QAbstractPhysicalDevice2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAbstractPhysicalDevice::tr(s, c, n));
}

//  Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice(Qt3DCore::QNo
//      de *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput23QAbstractPhysicalDeviceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAbstractPhysicalDevice(parent);
}

//  Qt3DInput::QAbstractPhysicalDevice::~QAbstractPhysicalDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QAbstractPhysicalDeviceD1Ev(
    Qt3DInput::QAbstractPhysicalDevice *self) {
  delete self;
}

//  int Qt3DInput::QAbstractPhysicalDevice::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->axisCount();
}

//  int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->buttonCount();
}

//  QStringList Qt3DInput::QAbstractPhysicalDevice::axisNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisNamesEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return new QList<QString>(self->axisNames());
}

//  QStringList Qt3DInput::QAbstractPhysicalDevice::buttonNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonNamesEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return new QList<QString>(self->buttonNames());
}

//  int Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDevice *self,
    const QString *name) {
  return self->axisIdentifier(*name);
}

//  int Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDevice *self,
    const QString *name) {
  return self->buttonIdentifier(*name);
}

//  void Qt3DInput::QAbstractPhysicalDevice::addAxisSetting(QAxisSetting
//      *axisSetting)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QAbstractPhysicalDevice14addAxisSettingEPNS_12QAxisSettingE(
    Qt3DInput::QAbstractPhysicalDevice *self,
    Qt3DInput::QAxisSetting *axisSetting) {
  self->addAxisSetting(axisSetting);
}

//  void Qt3DInput::QAbstractPhysicalDevice::removeAxisSetting(QAxisSetting
//      *axisSetting)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QAbstractPhysicalDevice17removeAxisSettingEPNS_12QAxisSettingE(
    Qt3DInput::QAbstractPhysicalDevice *self,
    Qt3DInput::QAxisSetting *axisSetting) {
  self->removeAxisSetting(axisSetting);
}

//  QList<QAxisSetting *> Qt3DInput::QAbstractPhysicalDevice::axisSettings()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAxisSetting *> *ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice12axisSettingsEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return new QList<Qt3DInput::QAxisSetting *>(self->axisSettings());
}

//  Qt3DInput::QAbstractPhysicalDevice::QAbstractPhysicalDevice(QAbstractPhys
//      icalDevicePrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput23QAbstractPhysicalDeviceC1ERNS_30QAbstractPhysicalDevicePrivateEPN8Qt3DCore5QNodeE(
    Qt3DInput::QAbstractPhysicalDevicePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAbstractPhysicalDevice(*dd, parent);
}

//  QAbstractPhysicalDevicePrivate
//      *Qt3DInput::QAbstractPhysicalDevice::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevicePrivate *ritual_ZN9Qt3DInput23QAbstractPhysicalDevice6d_funcEv(
    Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->d_func();
}

//  const QAbstractPhysicalDevicePrivate
//      *Qt3DInput::QAbstractPhysicalDevice::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDevicePrivate *ritual_ZNK9Qt3DInput23QAbstractPhysicalDevice6d_funcEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAbstractPhysicalDevice, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractPhysicalDevice(
    Qt3DInput::QAbstractPhysicalDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractPhysicalDevice *>(self)->take(key, call);
}

//  int Qt3DInput::QAbstractPhysicalDevice::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice9axisCountEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->Qt3DInput::QAbstractPhysicalDevice::axisCount();
}

//  int Qt3DInput::QAbstractPhysicalDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice11buttonCountEv(
    const Qt3DInput::QAbstractPhysicalDevice *self) {
  return self->Qt3DInput::QAbstractPhysicalDevice::buttonCount();
}

//  int Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice14axisIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDevice *self,
    const QString *name) {
  return self->Qt3DInput::QAbstractPhysicalDevice::axisIdentifier(*name);
}

//  int Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput23QAbstractPhysicalDevice16buttonIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDevice *self,
    const QString *name) {
  return self->Qt3DInput::QAbstractPhysicalDevice::buttonIdentifier(*name);
}

//  a QList<Qt3DInput::QAxisSetting *> a ritual of
//      Qt3DInput::QAbstractPhysicalDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QAbstractPhysicalDevice__QList_Qt3DInput_QAxisSetting(
    QList<Qt3DInput::QAxisSetting *> *self) {
  delete self;
}
