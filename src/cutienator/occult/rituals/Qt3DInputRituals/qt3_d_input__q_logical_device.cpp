//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qlogicaldevice.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qlogicaldevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::QLogicalDevice that Python can take functions over in. Every Qt3DInput::QLogicalDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QLogicalDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QLogicalDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QLogicalDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QLogicalDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QLogicalDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QLogicalDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QLogicalDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QLogicalDevice : public Qt3DInput::QLogicalDevice {
public:
  using Qt3DInput::QLogicalDevice::QLogicalDevice;
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
      CuteQt3DInput_QLogicalDeviceCall0 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall0>(taken[0]);
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
      CuteQt3DInput_QLogicalDeviceCall1 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall1>(taken[1]);
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
      CuteQt3DInput_QLogicalDeviceCall2 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall2>(taken[2]);
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
      CuteQt3DInput_QLogicalDeviceCall3 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall3>(taken[3]);
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
      CuteQt3DInput_QLogicalDeviceCall4 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall4>(taken[4]);
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
      CuteQt3DInput_QLogicalDeviceCall5 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall5>(taken[5]);
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
      CuteQt3DInput_QLogicalDeviceCall6 call = reinterpret_cast<CuteQt3DInput_QLogicalDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QLogicalDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput14QLogicalDevice10metaObjectEv(
    const Qt3DInput::QLogicalDevice *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QLogicalDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput14QLogicalDevice11qt_metacastEPKc(
    Qt3DInput::QLogicalDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QLogicalDevice::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput14QLogicalDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QLogicalDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QLogicalDevice::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput14QLogicalDevice2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QLogicalDevice::tr(s, c, n));
}

//  Qt3DInput::QLogicalDevice::QLogicalDevice(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QLogicalDevice *ritual_ZN9Qt3DInput14QLogicalDeviceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QLogicalDevice(parent);
}

//  Qt3DInput::QLogicalDevice::~QLogicalDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QLogicalDeviceD1Ev(
    Qt3DInput::QLogicalDevice *self) {
  delete self;
}

//  void Qt3DInput::QLogicalDevice::addAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QLogicalDevice9addActionEPNS_7QActionE(
    Qt3DInput::QLogicalDevice *self,
    Qt3DInput::QAction *action) {
  self->addAction(action);
}

//  void Qt3DInput::QLogicalDevice::removeAction(QAction *action)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QLogicalDevice12removeActionEPNS_7QActionE(
    Qt3DInput::QLogicalDevice *self,
    Qt3DInput::QAction *action) {
  self->removeAction(action);
}

//  QList<QAction *> Qt3DInput::QLogicalDevice::actions() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAction *> *ritual_ZNK9Qt3DInput14QLogicalDevice7actionsEv(
    const Qt3DInput::QLogicalDevice *self) {
  return new QList<Qt3DInput::QAction *>(self->actions());
}

//  void Qt3DInput::QLogicalDevice::addAxis(QAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QLogicalDevice7addAxisEPNS_5QAxisE(
    Qt3DInput::QLogicalDevice *self,
    Qt3DInput::QAxis *axis) {
  self->addAxis(axis);
}

//  void Qt3DInput::QLogicalDevice::removeAxis(QAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QLogicalDevice10removeAxisEPNS_5QAxisE(
    Qt3DInput::QLogicalDevice *self,
    Qt3DInput::QAxis *axis) {
  self->removeAxis(axis);
}

//  QList<QAxis *> Qt3DInput::QLogicalDevice::axes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAxis *> *ritual_ZNK9Qt3DInput14QLogicalDevice4axesEv(
    const Qt3DInput::QLogicalDevice *self) {
  return new QList<Qt3DInput::QAxis *>(self->axes());
}

//  QLogicalDevicePrivate *Qt3DInput::QLogicalDevice::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QLogicalDevicePrivate *ritual_ZN9Qt3DInput14QLogicalDevice6d_funcEv(
    Qt3DInput::QLogicalDevice *self) {
  return self->d_func();
}

//  const QLogicalDevicePrivate *Qt3DInput::QLogicalDevice::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QLogicalDevicePrivate *ritual_ZNK9Qt3DInput14QLogicalDevice6d_funcEv(
    const Qt3DInput::QLogicalDevice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QLogicalDevice, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QLogicalDevice(
    Qt3DInput::QLogicalDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QLogicalDevice *>(self)->take(key, call);
}

//  a QList<Qt3DInput::QAction *> a ritual of Qt3DInput::QLogicalDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QLogicalDevice__QList_Qt3DInput_QAction(
    QList<Qt3DInput::QAction *> *self) {
  delete self;
}

//  a QList<Qt3DInput::QAxis *> a ritual of Qt3DInput::QLogicalDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QLogicalDevice__QList_Qt3DInput_QAxis(
    QList<Qt3DInput::QAxis *> *self) {
  delete self;
}
