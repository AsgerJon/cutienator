//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qmultisampleantialiasing.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the 'd_func' rituals name
//  Qt3DRender::QMultiSampleAntiAliasingPrivate in full, as the
//  compiler asked. Kept as it is when the generator runs again.
#include <Qt3DRender/qmultisampleantialiasing.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QMultiSampleAntiAliasing that Python can take functions over in. Every Qt3DRender::QMultiSampleAntiAliasing
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMultiSampleAntiAliasingCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMultiSampleAntiAliasingCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMultiSampleAntiAliasingCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMultiSampleAntiAliasingCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMultiSampleAntiAliasingCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMultiSampleAntiAliasingCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMultiSampleAntiAliasingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QMultiSampleAntiAliasing : public Qt3DRender::QMultiSampleAntiAliasing {
public:
  using Qt3DRender::QMultiSampleAntiAliasing::QMultiSampleAntiAliasing;
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall0 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall0>(taken[0]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall1 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall1>(taken[1]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall2 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall2>(taken[2]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall3 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall3>(taken[3]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall4 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall4>(taken[4]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall5 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall5>(taken[5]);
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
      CuteQt3DRender_QMultiSampleAntiAliasingCall6 call = reinterpret_cast<CuteQt3DRender_QMultiSampleAntiAliasingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QMultiSampleAntiAliasing::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender24QMultiSampleAntiAliasing10metaObjectEv(
    const Qt3DRender::QMultiSampleAntiAliasing *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QMultiSampleAntiAliasing::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender24QMultiSampleAntiAliasing11qt_metacastEPKc(
    Qt3DRender::QMultiSampleAntiAliasing *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString Qt3DRender::QMultiSampleAntiAliasing::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender24QMultiSampleAntiAliasing2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QMultiSampleAntiAliasing::tr(s, c, n));
}

//  Qt3DRender::QMultiSampleAntiAliasingPrivate
//      *Qt3DRender::QMultiSampleAntiAliasing::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMultiSampleAntiAliasingPrivate *ritual_ZN10Qt3DRender24QMultiSampleAntiAliasing6d_funcEv(
    Qt3DRender::QMultiSampleAntiAliasing *self) {
  return self->d_func();
}

//  const Qt3DRender::QMultiSampleAntiAliasingPrivate
//      *Qt3DRender::QMultiSampleAntiAliasing::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QMultiSampleAntiAliasingPrivate *ritual_ZNK10Qt3DRender24QMultiSampleAntiAliasing6d_funcEv(
    const Qt3DRender::QMultiSampleAntiAliasing *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QMultiSampleAntiAliasing, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QMultiSampleAntiAliasing(
    Qt3DRender::QMultiSampleAntiAliasing *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QMultiSampleAntiAliasing *>(self)->take(key, call);
}
