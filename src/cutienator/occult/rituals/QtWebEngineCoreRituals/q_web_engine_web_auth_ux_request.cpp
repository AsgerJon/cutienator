//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginewebauthuxrequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginewebauthuxrequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWebEngineWebAuthUxRequest that Python can take functions over in. Every QWebEngineWebAuthUxRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineWebAuthUxRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineWebAuthUxRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineWebAuthUxRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineWebAuthUxRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineWebAuthUxRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineWebAuthUxRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineWebAuthUxRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineWebAuthUxRequest : public QWebEngineWebAuthUxRequest {
public:
  using QWebEngineWebAuthUxRequest::QWebEngineWebAuthUxRequest;
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
      CuteQWebEngineWebAuthUxRequestCall0 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall0>(taken[0]);
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
      CuteQWebEngineWebAuthUxRequestCall1 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall1>(taken[1]);
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
      CuteQWebEngineWebAuthUxRequestCall2 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall2>(taken[2]);
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
      CuteQWebEngineWebAuthUxRequestCall3 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall3>(taken[3]);
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
      CuteQWebEngineWebAuthUxRequestCall4 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall4>(taken[4]);
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
      CuteQWebEngineWebAuthUxRequestCall5 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall5>(taken[5]);
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
      CuteQWebEngineWebAuthUxRequestCall6 call = reinterpret_cast<CuteQWebEngineWebAuthUxRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineWebAuthUxRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWebEngineWebAuthUxRequest10metaObjectEv(
    const QWebEngineWebAuthUxRequest *self) {
  return self->metaObject();
}

//  void *QWebEngineWebAuthUxRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWebEngineWebAuthUxRequest11qt_metacastEPKc(
    QWebEngineWebAuthUxRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineWebAuthUxRequest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWebEngineWebAuthUxRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineWebAuthUxRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineWebAuthUxRequest::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWebEngineWebAuthUxRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineWebAuthUxRequest::tr(s, c, n));
}

//  QWebEngineWebAuthUxRequest::~QWebEngineWebAuthUxRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequestD1Ev(
    QWebEngineWebAuthUxRequest *self) {
  delete self;
}

//  QStringList QWebEngineWebAuthUxRequest::userNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK26QWebEngineWebAuthUxRequest9userNamesEv(
    const QWebEngineWebAuthUxRequest *self) {
  return new QList<QString>(self->userNames());
}

//  QString QWebEngineWebAuthUxRequest::relyingPartyId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QWebEngineWebAuthUxRequest14relyingPartyIdEv(
    const QWebEngineWebAuthUxRequest *self) {
  return new QString(self->relyingPartyId());
}

//  QWebEngineWebAuthPinRequest QWebEngineWebAuthUxRequest::pinRequest()
//      const
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthPinRequest *ritual_ZNK26QWebEngineWebAuthUxRequest10pinRequestEv(
    const QWebEngineWebAuthUxRequest *self) {
  return new QWebEngineWebAuthPinRequest(self->pinRequest());
}

//  WebAuthUxState QWebEngineWebAuthUxRequest::state() const
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthUxRequest::WebAuthUxState ritual_ZNK26QWebEngineWebAuthUxRequest5stateEv(
    const QWebEngineWebAuthUxRequest *self) {
  return self->state();
}

//  RequestFailureReason QWebEngineWebAuthUxRequest::requestFailureReason()
//      const
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthUxRequest::RequestFailureReason ritual_ZNK26QWebEngineWebAuthUxRequest20requestFailureReasonEv(
    const QWebEngineWebAuthUxRequest *self) {
  return self->requestFailureReason();
}

//  void QWebEngineWebAuthUxRequest::stateChanged(QWebEngineWebAuthUxRequest:
//      :WebAuthUxState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequest12stateChangedENS_14WebAuthUxStateE(
    QWebEngineWebAuthUxRequest *self,
    QWebEngineWebAuthUxRequest::WebAuthUxState state) {
  self->stateChanged(state);
}

//  void QWebEngineWebAuthUxRequest::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequest6cancelEv(
    QWebEngineWebAuthUxRequest *self) {
  self->cancel();
}

//  void QWebEngineWebAuthUxRequest::retry()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequest5retryEv(
    QWebEngineWebAuthUxRequest *self) {
  self->retry();
}

//  void QWebEngineWebAuthUxRequest::setSelectedAccount(const QString
//      &selectedAccount)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequest18setSelectedAccountERK7QString(
    QWebEngineWebAuthUxRequest *self,
    const QString *selectedAccount) {
  self->setSelectedAccount(*selectedAccount);
}

//  void QWebEngineWebAuthUxRequest::setPin(const QString &pin)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineWebAuthUxRequest6setPinERK7QString(
    QWebEngineWebAuthUxRequest *self,
    const QString *pin) {
  self->setPin(*pin);
}

//  QWebEngineWebAuthUxRequest::QWebEngineWebAuthUxRequest(QWebEngineWebAuthU
//      xRequestPrivate *a0)
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthUxRequest *ritual_ZN26QWebEngineWebAuthUxRequestC1EP33QWebEngineWebAuthUxRequestPrivate(
    QWebEngineWebAuthUxRequestPrivate *a0) {
  return new CuteQWebEngineWebAuthUxRequest(a0);
}

//  QWebEngineWebAuthUxRequestPrivate *QWebEngineWebAuthUxRequest::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthUxRequestPrivate *ritual_ZN26QWebEngineWebAuthUxRequest6d_funcEv(
    QWebEngineWebAuthUxRequest *self) {
  return self->d_func();
}

//  const QWebEngineWebAuthUxRequestPrivate
//      *QWebEngineWebAuthUxRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineWebAuthUxRequestPrivate *ritual_ZNK26QWebEngineWebAuthUxRequest6d_funcEv(
    const QWebEngineWebAuthUxRequest *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWebEngineWebAuthUxRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineWebAuthUxRequest(
    QWebEngineWebAuthUxRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineWebAuthUxRequest *>(self)->take(key, call);
}
