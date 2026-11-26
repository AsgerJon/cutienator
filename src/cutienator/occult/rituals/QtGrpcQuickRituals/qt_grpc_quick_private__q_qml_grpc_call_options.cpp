//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/qqmlgrpccalloptions.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: wrote QQmlGrpcCallOptionsPrivate in full,
//  as QtGrpcQuickPrivate::QQmlGrpcCallOptionsPrivate, in the two d_func
//  rituals. Kept as it is when the generator runs again.
#include <QtGrpcQuick/QtGrpcQuick>
#include <QtGrpcQuick/qqmlgrpccalloptions.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtGrpcQuickPrivate::QQmlGrpcCallOptions that Python can take functions over in. Every QtGrpcQuickPrivate::QQmlGrpcCallOptions
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtGrpcQuickPrivate_QQmlGrpcCallOptions : public QtGrpcQuickPrivate::QQmlGrpcCallOptions {
public:
  using QtGrpcQuickPrivate::QQmlGrpcCallOptions::QQmlGrpcCallOptions;
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall0 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall0>(taken[0]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall1 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall1>(taken[1]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall2 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall2>(taken[2]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall3 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall3>(taken[3]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall4 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall4>(taken[4]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall5 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall5>(taken[5]);
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
      CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall6 call = reinterpret_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptionsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtGrpcQuickPrivate::QQmlGrpcCallOptions::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtGrpcQuickPrivate19QQmlGrpcCallOptions10metaObjectEv(
    const QtGrpcQuickPrivate::QQmlGrpcCallOptions *self) {
  return self->metaObject();
}

//  void *QtGrpcQuickPrivate::QQmlGrpcCallOptions::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions11qt_metacastEPKc(
    QtGrpcQuickPrivate::QQmlGrpcCallOptions *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QtGrpcQuickPrivate::QQmlGrpcCallOptions::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtGrpcQuickPrivate::QQmlGrpcCallOptions::tr(s, c, n));
}

//  QQmlGrpcCallOptionsPrivate
//      *QtGrpcQuickPrivate::QQmlGrpcCallOptions::d_func()
extern "C" Q_DECL_EXPORT
QtGrpcQuickPrivate::QQmlGrpcCallOptionsPrivate *ritual_ZN18QtGrpcQuickPrivate19QQmlGrpcCallOptions6d_funcEv(
    QtGrpcQuickPrivate::QQmlGrpcCallOptions *self) {
  return self->d_func();
}

//  const QQmlGrpcCallOptionsPrivate
//      *QtGrpcQuickPrivate::QQmlGrpcCallOptions::d_func() const
extern "C" Q_DECL_EXPORT
const QtGrpcQuickPrivate::QQmlGrpcCallOptionsPrivate *ritual_ZNK18QtGrpcQuickPrivate19QQmlGrpcCallOptions6d_funcEv(
    const QtGrpcQuickPrivate::QQmlGrpcCallOptions *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtGrpcQuickPrivate_QQmlGrpcCallOptions,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtGrpcQuickPrivate_QQmlGrpcCallOptions(
    QtGrpcQuickPrivate::QQmlGrpcCallOptions *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtGrpcQuickPrivate_QQmlGrpcCallOptions *>(self)->take(key, call);
}
