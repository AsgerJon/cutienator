//  Written by dev_tooling.RitualGenerator from the records of QtWebViewQuick
//  /6.12.0/QtWebViewQuick/private/qquickwebviewloadrequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qtwebviewquickglobal_p.h>
#include <QtWebViewQuick/QtWebViewQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebViewQuick/6.12.0/QtWebViewQuick/private/qquickwebviewloadrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtWebView/qwebviewloadinginfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebViewLoadRequest that Python can take functions over in. Every QQuickWebViewLoadRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewLoadRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebViewLoadRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewLoadRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewLoadRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewLoadRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewLoadRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebViewLoadRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebViewLoadRequest : public QQuickWebViewLoadRequest {
public:
  using QQuickWebViewLoadRequest::QQuickWebViewLoadRequest;
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
      CuteQQuickWebViewLoadRequestCall0 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall0>(taken[0]);
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
      CuteQQuickWebViewLoadRequestCall1 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall1>(taken[1]);
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
      CuteQQuickWebViewLoadRequestCall2 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall2>(taken[2]);
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
      CuteQQuickWebViewLoadRequestCall3 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall3>(taken[3]);
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
      CuteQQuickWebViewLoadRequestCall4 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall4>(taken[4]);
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
      CuteQQuickWebViewLoadRequestCall5 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall5>(taken[5]);
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
      CuteQQuickWebViewLoadRequestCall6 call = reinterpret_cast<CuteQQuickWebViewLoadRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebViewLoadRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickWebViewLoadRequest10metaObjectEv(
    const QQuickWebViewLoadRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebViewLoadRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickWebViewLoadRequest11qt_metacastEPKc(
    QQuickWebViewLoadRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebViewLoadRequest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickWebViewLoadRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebViewLoadRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebViewLoadRequest::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickWebViewLoadRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebViewLoadRequest::tr(s, c, n));
}

//  void QQuickWebViewLoadRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickWebViewLoadRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebViewLoadRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebViewLoadRequest::~QQuickWebViewLoadRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickWebViewLoadRequestD1Ev(
    QQuickWebViewLoadRequest *self) {
  delete self;
}

//  QUrl QQuickWebViewLoadRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QQuickWebViewLoadRequest3urlEv(
    const QQuickWebViewLoadRequest *self) {
  return new QUrl(self->url());
}

//  QQuickWebView::LoadStatus QQuickWebViewLoadRequest::status() const
extern "C" Q_DECL_EXPORT
QQuickWebView::LoadStatus ritual_ZNK24QQuickWebViewLoadRequest6statusEv(
    const QQuickWebViewLoadRequest *self) {
  return self->status();
}

//  QString QQuickWebViewLoadRequest::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickWebViewLoadRequest11errorStringEv(
    const QQuickWebViewLoadRequest *self) {
  return new QString(self->errorString());
}

//  QQuickWebViewLoadRequest::QQuickWebViewLoadRequest(const
//      QWebViewLoadingInfo &d)
extern "C" Q_DECL_EXPORT
QQuickWebViewLoadRequest *ritual_ZN24QQuickWebViewLoadRequestC1ERK19QWebViewLoadingInfo(
    const QWebViewLoadingInfo *d) {
  return new CuteQQuickWebViewLoadRequest(*d);
}

//  a Python function taken by a CuteQQuickWebViewLoadRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebViewLoadRequest(
    QQuickWebViewLoadRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebViewLoadRequest *>(self)->take(key, call);
}
