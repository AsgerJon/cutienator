//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qaxissetting.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qaxissetting.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DInput::QAxisSetting that Python can take functions over in. Every Qt3DInput::QAxisSetting
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisSettingCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QAxisSettingCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisSettingCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisSettingCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisSettingCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisSettingCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QAxisSettingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAxisSetting : public Qt3DInput::QAxisSetting {
public:
  using Qt3DInput::QAxisSetting::QAxisSetting;
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
      CuteQt3DInput_QAxisSettingCall0 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall0>(taken[0]);
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
      CuteQt3DInput_QAxisSettingCall1 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall1>(taken[1]);
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
      CuteQt3DInput_QAxisSettingCall2 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall2>(taken[2]);
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
      CuteQt3DInput_QAxisSettingCall3 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall3>(taken[3]);
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
      CuteQt3DInput_QAxisSettingCall4 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall4>(taken[4]);
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
      CuteQt3DInput_QAxisSettingCall5 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall5>(taken[5]);
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
      CuteQt3DInput_QAxisSettingCall6 call = reinterpret_cast<CuteQt3DInput_QAxisSettingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAxisSetting::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput12QAxisSetting10metaObjectEv(
    const Qt3DInput::QAxisSetting *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAxisSetting::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput12QAxisSetting11qt_metacastEPKc(
    Qt3DInput::QAxisSetting *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAxisSetting::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput12QAxisSetting11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAxisSetting *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAxisSetting::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput12QAxisSetting2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAxisSetting::tr(s, c, n));
}

//  Qt3DInput::QAxisSetting::QAxisSetting(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisSetting *ritual_ZN9Qt3DInput12QAxisSettingC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAxisSetting(parent);
}

//  Qt3DInput::QAxisSetting::~QAxisSetting()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSettingD1Ev(Qt3DInput::QAxisSetting *self) {
  delete self;
}

//  float Qt3DInput::QAxisSetting::deadZoneRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput12QAxisSetting14deadZoneRadiusEv(
    const Qt3DInput::QAxisSetting *self) {
  return self->deadZoneRadius();
}

//  QList<int> Qt3DInput::QAxisSetting::axes() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9Qt3DInput12QAxisSetting4axesEv(
    const Qt3DInput::QAxisSetting *self) {
  return new QList<int>(self->axes());
}

//  bool Qt3DInput::QAxisSetting::isSmoothEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput12QAxisSetting15isSmoothEnabledEv(
    const Qt3DInput::QAxisSetting *self) {
  return self->isSmoothEnabled();
}

//  void Qt3DInput::QAxisSetting::setDeadZoneRadius(float deadZoneRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting17setDeadZoneRadiusEf(
    Qt3DInput::QAxisSetting *self,
    float deadZoneRadius) {
  self->setDeadZoneRadius(deadZoneRadius);
}

//  void Qt3DInput::QAxisSetting::setAxes(const QList<int> &axes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting7setAxesERK5QListIiE(
    Qt3DInput::QAxisSetting *self,
    const QList<int> *axes) {
  self->setAxes(*axes);
}

//  void Qt3DInput::QAxisSetting::setSmoothEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting16setSmoothEnabledEb(
    Qt3DInput::QAxisSetting *self,
    bool enabled) {
  self->setSmoothEnabled(enabled);
}

//  void Qt3DInput::QAxisSetting::deadZoneRadiusChanged(float deadZoneRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting21deadZoneRadiusChangedEf(
    Qt3DInput::QAxisSetting *self,
    float deadZoneRadius) {
  self->deadZoneRadiusChanged(deadZoneRadius);
}

//  void Qt3DInput::QAxisSetting::axesChanged(const QList<int> &axes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting11axesChangedERK5QListIiE(
    Qt3DInput::QAxisSetting *self,
    const QList<int> *axes) {
  self->axesChanged(*axes);
}

//  void Qt3DInput::QAxisSetting::smoothChanged(bool smooth)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisSetting13smoothChangedEb(
    Qt3DInput::QAxisSetting *self,
    bool smooth) {
  self->smoothChanged(smooth);
}

//  QAxisSettingPrivate *Qt3DInput::QAxisSetting::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisSettingPrivate *ritual_ZN9Qt3DInput12QAxisSetting6d_funcEv(
    Qt3DInput::QAxisSetting *self) {
  return self->d_func();
}

//  const QAxisSettingPrivate *Qt3DInput::QAxisSetting::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAxisSettingPrivate *ritual_ZNK9Qt3DInput12QAxisSetting6d_funcEv(
    const Qt3DInput::QAxisSetting *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAxisSetting, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAxisSetting(
    Qt3DInput::QAxisSetting *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAxisSetting *>(self)->take(key, call);
}

//  a QList<int> a ritual of Qt3DInput::QAxisSetting gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QAxisSetting__QList_int(QList<int> *self) {
  delete self;
}
