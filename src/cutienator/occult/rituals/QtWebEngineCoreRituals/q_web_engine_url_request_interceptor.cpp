//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineurlrequestinterceptor.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWebEngineCore/qwebengineurlrequestinterceptor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineUrlRequestInterceptor that Python can take functions over in. Every QWebEngineUrlRequestInterceptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlRequestInterceptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlRequestInterceptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestInterceptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestInterceptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestInterceptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestInterceptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestInterceptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineUrlRequestInterceptor : public QWebEngineUrlRequestInterceptor {
public:
  using QWebEngineUrlRequestInterceptor::QWebEngineUrlRequestInterceptor;
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
      CuteQWebEngineUrlRequestInterceptorCall0 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall0>(taken[0]);
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
      CuteQWebEngineUrlRequestInterceptorCall1 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall1>(taken[1]);
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
      CuteQWebEngineUrlRequestInterceptorCall2 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall2>(taken[2]);
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
      CuteQWebEngineUrlRequestInterceptorCall3 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall3>(taken[3]);
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
      CuteQWebEngineUrlRequestInterceptorCall4 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall4>(taken[4]);
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
      CuteQWebEngineUrlRequestInterceptorCall5 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall5>(taken[5]);
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
      CuteQWebEngineUrlRequestInterceptorCall6 call = reinterpret_cast<CuteQWebEngineUrlRequestInterceptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineUrlRequestInterceptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QWebEngineUrlRequestInterceptor10metaObjectEv(
    const QWebEngineUrlRequestInterceptor *self) {
  return self->metaObject();
}

//  void *QWebEngineUrlRequestInterceptor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QWebEngineUrlRequestInterceptor11qt_metacastEPKc(
    QWebEngineUrlRequestInterceptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineUrlRequestInterceptor::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QWebEngineUrlRequestInterceptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineUrlRequestInterceptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineUrlRequestInterceptor::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QWebEngineUrlRequestInterceptor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineUrlRequestInterceptor::tr(s, c, n));
}

//  QWebEngineUrlRequestInterceptor::~QWebEngineUrlRequestInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWebEngineUrlRequestInterceptorD1Ev(
    QWebEngineUrlRequestInterceptor *self) {
  delete self;
}

//  void QWebEngineUrlRequestInterceptor::interceptRequest(QWebEngineUrlReque
//      stInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWebEngineUrlRequestInterceptor16interceptRequestER24QWebEngineUrlRequestInfo(
    QWebEngineUrlRequestInterceptor *self,
    QWebEngineUrlRequestInfo *info) {
  self->interceptRequest(*info);
}

//  a Python function taken by a CuteQWebEngineUrlRequestInterceptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineUrlRequestInterceptor(
    QWebEngineUrlRequestInterceptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineUrlRequestInterceptor *>(self)->take(key, call);
}
