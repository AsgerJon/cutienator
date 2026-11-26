//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibilityhints.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibilityhints.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAccessibilityHints may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAccessibilityHints : QAccessibilityHints {
  using QAccessibilityHints::event;
};

//  A QAccessibilityHints that Python can take functions over in. Every QAccessibilityHints
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibilityHintsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibilityHintsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibilityHintsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibilityHintsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibilityHintsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibilityHintsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibilityHintsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccessibilityHints : public QAccessibilityHints {
public:
  using QAccessibilityHints::QAccessibilityHints;
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
  //  bool QAccessibilityHints::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibilityHintsCall0 call = reinterpret_cast<CuteQAccessibilityHintsCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAccessibilityHints::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibilityHintsCall1 call = reinterpret_cast<CuteQAccessibilityHintsCall1>(taken[1]);
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
      CuteQAccessibilityHintsCall2 call = reinterpret_cast<CuteQAccessibilityHintsCall2>(taken[2]);
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
      CuteQAccessibilityHintsCall3 call = reinterpret_cast<CuteQAccessibilityHintsCall3>(taken[3]);
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
      CuteQAccessibilityHintsCall4 call = reinterpret_cast<CuteQAccessibilityHintsCall4>(taken[4]);
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
      CuteQAccessibilityHintsCall5 call = reinterpret_cast<CuteQAccessibilityHintsCall5>(taken[5]);
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
      CuteQAccessibilityHintsCall6 call = reinterpret_cast<CuteQAccessibilityHintsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccessibilityHints::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAccessibilityHints10metaObjectEv(
    const QAccessibilityHints *self) {
  return self->metaObject();
}

//  void *QAccessibilityHints::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QAccessibilityHints11qt_metacastEPKc(
    QAccessibilityHints *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAccessibilityHints::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QAccessibilityHints11qt_metacallEN11QMetaObject4CallEiPPv(
    QAccessibilityHints *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAccessibilityHints::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAccessibilityHints2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessibilityHints::tr(s, c, n));
}

//  QAccessibilityHintsPrivate *QAccessibilityHints::d_func()
extern "C" Q_DECL_EXPORT
QAccessibilityHintsPrivate *ritual_ZN19QAccessibilityHints6d_funcEv(
    QAccessibilityHints *self) {
  return self->d_func();
}

//  const QAccessibilityHintsPrivate *QAccessibilityHints::d_func() const
extern "C" Q_DECL_EXPORT
const QAccessibilityHintsPrivate *ritual_ZNK19QAccessibilityHints6d_funcEv(
    const QAccessibilityHints *self) {
  return self->d_func();
}

//  QAccessibilityHints::QAccessibilityHints(QObject *parent)
extern "C" Q_DECL_EXPORT
QAccessibilityHints *ritual_ZN19QAccessibilityHintsC1EP7QObject(
    QObject *parent) {
  return new CuteQAccessibilityHints(parent);
}

//  QAccessibilityHints::~QAccessibilityHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibilityHintsD1Ev(QAccessibilityHints *self) {
  delete self;
}

//  Qt::ContrastPreference QAccessibilityHints::contrastPreference() const
extern "C" Q_DECL_EXPORT
Qt::ContrastPreference ritual_ZNK19QAccessibilityHints18contrastPreferenceEv(
    const QAccessibilityHints *self) {
  return self->contrastPreference();
}

//  Qt::MotionPreference QAccessibilityHints::motionPreference() const
extern "C" Q_DECL_EXPORT
Qt::MotionPreference ritual_ZNK19QAccessibilityHints16motionPreferenceEv(
    const QAccessibilityHints *self) {
  return self->motionPreference();
}

//  void
//      QAccessibilityHints::contrastPreferenceChanged(Qt::ContrastPreference
//      contrastPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibilityHints25contrastPreferenceChangedEN2Qt18ContrastPreferenceE(
    QAccessibilityHints *self,
    Qt::ContrastPreference contrastPreference) {
  self->contrastPreferenceChanged(contrastPreference);
}

//  void QAccessibilityHints::motionPreferenceChanged(Qt::MotionPreference
//      motionPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibilityHints23motionPreferenceChangedEN2Qt16MotionPreferenceE(
    QAccessibilityHints *self,
    Qt::MotionPreference motionPreference) {
  self->motionPreferenceChanged(motionPreference);
}

//  bool QAccessibilityHints::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAccessibilityHints5eventEP6QEvent(
    QAccessibilityHints *self,
    QEvent *event) {
  return self->event(event);
}

//  a Python function taken by a CuteQAccessibilityHints, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibilityHints(
    QAccessibilityHints *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibilityHints *>(self)->take(key, call);
}

//  bool QAccessibilityHints::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAccessibilityHints5eventEP6QEvent(
    QAccessibilityHints *self,
    QEvent *event) {
  return static_cast<OwnQAccessibilityHints *>(self)->OwnQAccessibilityHints::event(
      event);
}
