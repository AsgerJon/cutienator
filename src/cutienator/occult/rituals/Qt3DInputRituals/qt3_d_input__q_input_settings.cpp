//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qinputsettings.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qinputsettings.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QInputSettings that Python can take functions over in. Every Qt3DInput::QInputSettings
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputSettingsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QInputSettingsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSettingsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSettingsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSettingsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSettingsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QInputSettingsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QInputSettings : public Qt3DInput::QInputSettings {
public:
  using Qt3DInput::QInputSettings::QInputSettings;
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
      CuteQt3DInput_QInputSettingsCall0 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall0>(taken[0]);
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
      CuteQt3DInput_QInputSettingsCall1 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall1>(taken[1]);
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
      CuteQt3DInput_QInputSettingsCall2 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall2>(taken[2]);
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
      CuteQt3DInput_QInputSettingsCall3 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall3>(taken[3]);
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
      CuteQt3DInput_QInputSettingsCall4 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall4>(taken[4]);
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
      CuteQt3DInput_QInputSettingsCall5 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall5>(taken[5]);
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
      CuteQt3DInput_QInputSettingsCall6 call = reinterpret_cast<CuteQt3DInput_QInputSettingsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QInputSettings::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput14QInputSettings10metaObjectEv(
    const Qt3DInput::QInputSettings *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QInputSettings::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput14QInputSettings11qt_metacastEPKc(
    Qt3DInput::QInputSettings *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QInputSettings::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput14QInputSettings11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QInputSettings *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QInputSettings::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput14QInputSettings2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QInputSettings::tr(s, c, n));
}

//  Qt3DInput::QInputSettings::QInputSettings(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputSettings *ritual_ZN9Qt3DInput14QInputSettingsC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QInputSettings(parent);
}

//  Qt3DInput::QInputSettings::~QInputSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSettingsD1Ev(
    Qt3DInput::QInputSettings *self) {
  delete self;
}

//  QObject *Qt3DInput::QInputSettings::eventSource() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK9Qt3DInput14QInputSettings11eventSourceEv(
    const Qt3DInput::QInputSettings *self) {
  return self->eventSource();
}

//  void Qt3DInput::QInputSettings::setEventSource(QObject *eventSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSettings14setEventSourceEP7QObject(
    Qt3DInput::QInputSettings *self,
    QObject *eventSource) {
  self->setEventSource(eventSource);
}

//  void Qt3DInput::QInputSettings::eventSourceChanged(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSettings18eventSourceChangedEP7QObject(
    Qt3DInput::QInputSettings *self,
    QObject *a0) {
  self->eventSourceChanged(a0);
}

//  QInputSettingsPrivate *Qt3DInput::QInputSettings::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputSettingsPrivate *ritual_ZN9Qt3DInput14QInputSettings6d_funcEv(
    Qt3DInput::QInputSettings *self) {
  return self->d_func();
}

//  const QInputSettingsPrivate *Qt3DInput::QInputSettings::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputSettingsPrivate *ritual_ZNK9Qt3DInput14QInputSettings6d_funcEv(
    const Qt3DInput::QInputSettings *self) {
  return self->d_func();
}

//  void Qt3DInput::QInputSettings::eventSourceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QInputSettings20eventSourceDestroyedEv(
    Qt3DInput::QInputSettings *self) {
  self->eventSourceDestroyed();
}

//  a Python function taken by a CuteQt3DInput_QInputSettings, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputSettings(
    Qt3DInput::QInputSettings *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputSettings *>(self)->take(key, call);
}
