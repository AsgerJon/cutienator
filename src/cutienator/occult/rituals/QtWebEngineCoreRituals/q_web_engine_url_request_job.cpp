//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineurlrequestjob.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebengineurlrequestjob.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QMap>
#include <QtCore/QByteArray>

//  A QWebEngineUrlRequestJob that Python can take functions over in. Every QWebEngineUrlRequestJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlRequestJobCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineUrlRequestJobCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestJobCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestJobCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestJobCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestJobCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineUrlRequestJobCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineUrlRequestJob : public QWebEngineUrlRequestJob {
public:
  using QWebEngineUrlRequestJob::QWebEngineUrlRequestJob;
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
      CuteQWebEngineUrlRequestJobCall0 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall0>(taken[0]);
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
      CuteQWebEngineUrlRequestJobCall1 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall1>(taken[1]);
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
      CuteQWebEngineUrlRequestJobCall2 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall2>(taken[2]);
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
      CuteQWebEngineUrlRequestJobCall3 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall3>(taken[3]);
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
      CuteQWebEngineUrlRequestJobCall4 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall4>(taken[4]);
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
      CuteQWebEngineUrlRequestJobCall5 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall5>(taken[5]);
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
      CuteQWebEngineUrlRequestJobCall6 call = reinterpret_cast<CuteQWebEngineUrlRequestJobCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineUrlRequestJob::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWebEngineUrlRequestJob10metaObjectEv(
    const QWebEngineUrlRequestJob *self) {
  return self->metaObject();
}

//  void *QWebEngineUrlRequestJob::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QWebEngineUrlRequestJob11qt_metacastEPKc(
    QWebEngineUrlRequestJob *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineUrlRequestJob::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QWebEngineUrlRequestJob11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineUrlRequestJob *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineUrlRequestJob::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QWebEngineUrlRequestJob2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineUrlRequestJob::tr(s, c, n));
}

//  QWebEngineUrlRequestJob::~QWebEngineUrlRequestJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineUrlRequestJobD1Ev(QWebEngineUrlRequestJob *self) {
  delete self;
}

//  QUrl QWebEngineUrlRequestJob::requestUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK23QWebEngineUrlRequestJob10requestUrlEv(
    const QWebEngineUrlRequestJob *self) {
  return new QUrl(self->requestUrl());
}

//  QByteArray QWebEngineUrlRequestJob::requestMethod() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QWebEngineUrlRequestJob13requestMethodEv(
    const QWebEngineUrlRequestJob *self) {
  return new QByteArray(self->requestMethod());
}

//  QUrl QWebEngineUrlRequestJob::initiator() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK23QWebEngineUrlRequestJob9initiatorEv(
    const QWebEngineUrlRequestJob *self) {
  return new QUrl(self->initiator());
}

//  QMap<QByteArray, QByteArray> QWebEngineUrlRequestJob::requestHeaders()
//      const
extern "C" Q_DECL_EXPORT
QMap<QByteArray, QByteArray> *ritual_ZNK23QWebEngineUrlRequestJob14requestHeadersEv(
    const QWebEngineUrlRequestJob *self) {
  return new QMap<QByteArray, QByteArray>(self->requestHeaders());
}

//  QIODevice *QWebEngineUrlRequestJob::requestBody() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK23QWebEngineUrlRequestJob11requestBodyEv(
    const QWebEngineUrlRequestJob *self) {
  return self->requestBody();
}

//  void QWebEngineUrlRequestJob::reply(const QByteArray &contentType,
//      QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineUrlRequestJob5replyERK10QByteArrayP9QIODevice(
    QWebEngineUrlRequestJob *self,
    const QByteArray *contentType,
    QIODevice *device) {
  self->reply(*contentType, device);
}

//  void QWebEngineUrlRequestJob::fail(Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineUrlRequestJob4failENS_5ErrorE(
    QWebEngineUrlRequestJob *self,
    QWebEngineUrlRequestJob::Error error) {
  self->fail(error);
}

//  void QWebEngineUrlRequestJob::redirect(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineUrlRequestJob8redirectERK4QUrl(
    QWebEngineUrlRequestJob *self,
    const QUrl *url) {
  self->redirect(*url);
}

//  void QWebEngineUrlRequestJob::setAdditionalResponseHeaders(const
//      QMultiMap<QByteArray, QByteArray> &additionalResponseHeaders) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QWebEngineUrlRequestJob28setAdditionalResponseHeadersERK9QMultiMapI10QByteArrayS1_E(
    const QWebEngineUrlRequestJob *self,
    const QMultiMap<QByteArray, QByteArray> *additionalResponseHeaders) {
  self->setAdditionalResponseHeaders(*additionalResponseHeaders);
}

//  QWebEngineUrlRequestJob::QWebEngineUrlRequestJob(QtWebEngineCore::URLRequ
//      estCustomJobDelegate *a0)
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestJob *ritual_ZN23QWebEngineUrlRequestJobC1EPN15QtWebEngineCore27URLRequestCustomJobDelegateE(
    QtWebEngineCore::URLRequestCustomJobDelegate *a0) {
  return new CuteQWebEngineUrlRequestJob(a0);
}

//  a Python function taken by a CuteQWebEngineUrlRequestJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineUrlRequestJob(
    QWebEngineUrlRequestJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineUrlRequestJob *>(self)->take(key, call);
}

//  a QMap<QByteArray, QByteArray> a ritual of QWebEngineUrlRequestJob gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEngineUrlRequestJob__QMap_QByteArray_QByteArray(
    QMap<QByteArray, QByteArray> *self) {
  delete self;
}
