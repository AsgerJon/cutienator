//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qmousedevice.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qmousedevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DInput::QMouseDevice that Python can take functions over in. Every Qt3DInput::QMouseDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QMouseDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QMouseDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QMouseDevice : public Qt3DInput::QMouseDevice {
public:
  using Qt3DInput::QMouseDevice::QMouseDevice;
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
      CuteQt3DInput_QMouseDeviceCall0 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall0>(taken[0]);
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
      CuteQt3DInput_QMouseDeviceCall1 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall1>(taken[1]);
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
      CuteQt3DInput_QMouseDeviceCall2 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall2>(taken[2]);
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
      CuteQt3DInput_QMouseDeviceCall3 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall3>(taken[3]);
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
      CuteQt3DInput_QMouseDeviceCall4 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall4>(taken[4]);
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
      CuteQt3DInput_QMouseDeviceCall5 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall5>(taken[5]);
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
      CuteQt3DInput_QMouseDeviceCall6 call = reinterpret_cast<CuteQt3DInput_QMouseDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QMouseDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput12QMouseDevice10metaObjectEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QMouseDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput12QMouseDevice11qt_metacastEPKc(
    Qt3DInput::QMouseDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QMouseDevice::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput12QMouseDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QMouseDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QMouseDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput12QMouseDevice2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QMouseDevice::tr(s, c, n));
}

//  Qt3DInput::QMouseDevice::QMouseDevice(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseDevice *ritual_ZN9Qt3DInput12QMouseDeviceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QMouseDevice(parent);
}

//  Qt3DInput::QMouseDevice::~QMouseDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QMouseDeviceD1Ev(Qt3DInput::QMouseDevice *self) {
  delete self;
}

//  int Qt3DInput::QMouseDevice::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput12QMouseDevice9axisCountEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->axisCount();
}

//  int Qt3DInput::QMouseDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput12QMouseDevice11buttonCountEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->buttonCount();
}

//  QStringList Qt3DInput::QMouseDevice::axisNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput12QMouseDevice9axisNamesEv(
    const Qt3DInput::QMouseDevice *self) {
  return new QList<QString>(self->axisNames());
}

//  QStringList Qt3DInput::QMouseDevice::buttonNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput12QMouseDevice11buttonNamesEv(
    const Qt3DInput::QMouseDevice *self) {
  return new QList<QString>(self->buttonNames());
}

//  int Qt3DInput::QMouseDevice::axisIdentifier(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput12QMouseDevice14axisIdentifierERK7QString(
    const Qt3DInput::QMouseDevice *self,
    const QString *name) {
  return self->axisIdentifier(*name);
}

//  int Qt3DInput::QMouseDevice::buttonIdentifier(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput12QMouseDevice16buttonIdentifierERK7QString(
    const Qt3DInput::QMouseDevice *self,
    const QString *name) {
  return self->buttonIdentifier(*name);
}

//  float Qt3DInput::QMouseDevice::sensitivity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput12QMouseDevice11sensitivityEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->sensitivity();
}

//  bool Qt3DInput::QMouseDevice::updateAxesContinuously() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput12QMouseDevice22updateAxesContinuouslyEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->updateAxesContinuously();
}

//  void Qt3DInput::QMouseDevice::setSensitivity(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QMouseDevice14setSensitivityEf(
    Qt3DInput::QMouseDevice *self,
    float value) {
  self->setSensitivity(value);
}

//  void Qt3DInput::QMouseDevice::setUpdateAxesContinuously(bool
//      updateAxesContinuously)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QMouseDevice25setUpdateAxesContinuouslyEb(
    Qt3DInput::QMouseDevice *self,
    bool updateAxesContinuously) {
  self->setUpdateAxesContinuously(updateAxesContinuously);
}

//  void Qt3DInput::QMouseDevice::sensitivityChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QMouseDevice18sensitivityChangedEf(
    Qt3DInput::QMouseDevice *self,
    float value) {
  self->sensitivityChanged(value);
}

//  void Qt3DInput::QMouseDevice::updateAxesContinuouslyChanged(bool
//      updateAxesContinuously)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QMouseDevice29updateAxesContinuouslyChangedEb(
    Qt3DInput::QMouseDevice *self,
    bool updateAxesContinuously) {
  self->updateAxesContinuouslyChanged(updateAxesContinuously);
}

//  QMouseDevicePrivate *Qt3DInput::QMouseDevice::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseDevicePrivate *ritual_ZN9Qt3DInput12QMouseDevice6d_funcEv(
    Qt3DInput::QMouseDevice *self) {
  return self->d_func();
}

//  const QMouseDevicePrivate *Qt3DInput::QMouseDevice::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QMouseDevicePrivate *ritual_ZNK9Qt3DInput12QMouseDevice6d_funcEv(
    const Qt3DInput::QMouseDevice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QMouseDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QMouseDevice(
    Qt3DInput::QMouseDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QMouseDevice *>(self)->take(key, call);
}
