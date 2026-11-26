//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qkeyboarddevice.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qkeyboarddevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A Qt3DInput::QKeyboardDevice that Python can take functions over in. Every Qt3DInput::QKeyboardDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyboardDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QKeyboardDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QKeyboardDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QKeyboardDevice : public Qt3DInput::QKeyboardDevice {
public:
  using Qt3DInput::QKeyboardDevice::QKeyboardDevice;
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
      CuteQt3DInput_QKeyboardDeviceCall0 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall0>(taken[0]);
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
      CuteQt3DInput_QKeyboardDeviceCall1 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall1>(taken[1]);
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
      CuteQt3DInput_QKeyboardDeviceCall2 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall2>(taken[2]);
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
      CuteQt3DInput_QKeyboardDeviceCall3 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall3>(taken[3]);
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
      CuteQt3DInput_QKeyboardDeviceCall4 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall4>(taken[4]);
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
      CuteQt3DInput_QKeyboardDeviceCall5 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall5>(taken[5]);
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
      CuteQt3DInput_QKeyboardDeviceCall6 call = reinterpret_cast<CuteQt3DInput_QKeyboardDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QKeyboardDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput15QKeyboardDevice10metaObjectEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QKeyboardDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput15QKeyboardDevice11qt_metacastEPKc(
    Qt3DInput::QKeyboardDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QKeyboardDevice::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput15QKeyboardDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QKeyboardDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QKeyboardDevice::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput15QKeyboardDevice2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QKeyboardDevice::tr(s, c, n));
}

//  Qt3DInput::QKeyboardDevice::QKeyboardDevice(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevice *ritual_ZN9Qt3DInput15QKeyboardDeviceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QKeyboardDevice(parent);
}

//  Qt3DInput::QKeyboardDevice::~QKeyboardDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput15QKeyboardDeviceD1Ev(
    Qt3DInput::QKeyboardDevice *self) {
  delete self;
}

//  QKeyboardHandler *Qt3DInput::QKeyboardDevice::activeInput() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardHandler *ritual_ZNK9Qt3DInput15QKeyboardDevice11activeInputEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return self->activeInput();
}

//  int Qt3DInput::QKeyboardDevice::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput15QKeyboardDevice9axisCountEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return self->axisCount();
}

//  int Qt3DInput::QKeyboardDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput15QKeyboardDevice11buttonCountEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return self->buttonCount();
}

//  QStringList Qt3DInput::QKeyboardDevice::axisNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput15QKeyboardDevice9axisNamesEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return new QList<QString>(self->axisNames());
}

//  QStringList Qt3DInput::QKeyboardDevice::buttonNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput15QKeyboardDevice11buttonNamesEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return new QList<QString>(self->buttonNames());
}

//  int Qt3DInput::QKeyboardDevice::axisIdentifier(const QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput15QKeyboardDevice14axisIdentifierERK7QString(
    const Qt3DInput::QKeyboardDevice *self,
    const QString *name) {
  return self->axisIdentifier(*name);
}

//  int Qt3DInput::QKeyboardDevice::buttonIdentifier(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput15QKeyboardDevice16buttonIdentifierERK7QString(
    const Qt3DInput::QKeyboardDevice *self,
    const QString *name) {
  return self->buttonIdentifier(*name);
}

//  Qt3DInput::QKeyboardDevice::QKeyboardDevice(QKeyboardDevicePrivate &dd,
//      QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevice *ritual_ZN9Qt3DInput15QKeyboardDeviceC1ERNS_22QKeyboardDevicePrivateEPN8Qt3DCore5QNodeE(
    Qt3DInput::QKeyboardDevicePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QKeyboardDevice(*dd, parent);
}

//  void Qt3DInput::QKeyboardDevice::activeInputChanged(QKeyboardHandler
//      *activeInput)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput15QKeyboardDevice18activeInputChangedEPNS_16QKeyboardHandlerE(
    Qt3DInput::QKeyboardDevice *self,
    Qt3DInput::QKeyboardHandler *activeInput) {
  self->activeInputChanged(activeInput);
}

//  QKeyboardDevicePrivate *Qt3DInput::QKeyboardDevice::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QKeyboardDevicePrivate *ritual_ZN9Qt3DInput15QKeyboardDevice6d_funcEv(
    Qt3DInput::QKeyboardDevice *self) {
  return self->d_func();
}

//  const QKeyboardDevicePrivate *Qt3DInput::QKeyboardDevice::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QKeyboardDevicePrivate *ritual_ZNK9Qt3DInput15QKeyboardDevice6d_funcEv(
    const Qt3DInput::QKeyboardDevice *self) {
  return self->d_func();
}

//  void Qt3DInput::QKeyboardDevice::setActiveInput(QKeyboardHandler
//      *activeInput)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput15QKeyboardDevice14setActiveInputEPNS_16QKeyboardHandlerE(
    Qt3DInput::QKeyboardDevice *self,
    Qt3DInput::QKeyboardHandler *activeInput) {
  self->setActiveInput(activeInput);
}

//  a Python function taken by a CuteQt3DInput_QKeyboardDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QKeyboardDevice(
    Qt3DInput::QKeyboardDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QKeyboardDevice *>(self)->take(key, call);
}
