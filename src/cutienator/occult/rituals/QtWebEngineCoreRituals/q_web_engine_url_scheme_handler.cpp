//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineurlschemehandler.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebengineurlschemehandler.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineUrlSchemeHandler that Python can take functions over in. Every QWebEngineUrlSchemeHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWebEngineUrlSchemeHandlerCall0)(const void *, QWebEngineUrlRequestJob *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlSchemeHandlerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlSchemeHandlerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlSchemeHandlerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlSchemeHandlerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlSchemeHandlerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlSchemeHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlSchemeHandlerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineUrlSchemeHandler : public QWebEngineUrlSchemeHandler {
public:
  using QWebEngineUrlSchemeHandler::QWebEngineUrlSchemeHandler;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QWebEngineUrlSchemeHandler14requestStartedEP23QWebEngineUrlRequestJob")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void
  //      QWebEngineUrlSchemeHandler::requestStarted(QWebEngineUrlRequestJo
  //      b *a0)
  void requestStarted(QWebEngineUrlRequestJob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall0 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall1 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall2 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall3 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall4 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall5 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall6 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebEngineUrlSchemeHandlerCall7 call = reinterpret_cast<CuteQWebEngineUrlSchemeHandlerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineUrlSchemeHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWebEngineUrlSchemeHandler10metaObjectEv(
    const QWebEngineUrlSchemeHandler *self) {
  return self->metaObject();
}

//  void *QWebEngineUrlSchemeHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWebEngineUrlSchemeHandler11qt_metacastEPKc(
    QWebEngineUrlSchemeHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineUrlSchemeHandler::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWebEngineUrlSchemeHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineUrlSchemeHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineUrlSchemeHandler::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWebEngineUrlSchemeHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineUrlSchemeHandler::tr(s, c, n));
}

//  QWebEngineUrlSchemeHandler::QWebEngineUrlSchemeHandler(QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineUrlSchemeHandler *ritual_ZN26QWebEngineUrlSchemeHandlerC1EP7QObject(
    QObject *parent) {
  return new CuteQWebEngineUrlSchemeHandler(parent);
}

//  QWebEngineUrlSchemeHandler::~QWebEngineUrlSchemeHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineUrlSchemeHandlerD1Ev(
    QWebEngineUrlSchemeHandler *self) {
  delete self;
}

//  void QWebEngineUrlSchemeHandler::requestStarted(QWebEngineUrlRequestJob
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineUrlSchemeHandler14requestStartedEP23QWebEngineUrlRequestJob(
    QWebEngineUrlSchemeHandler *self,
    QWebEngineUrlRequestJob *a0) {
  self->requestStarted(a0);
}

//  a Python function taken by a CuteQWebEngineUrlSchemeHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineUrlSchemeHandler(
    QWebEngineUrlSchemeHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineUrlSchemeHandler *>(self)->take(key, call);
}
