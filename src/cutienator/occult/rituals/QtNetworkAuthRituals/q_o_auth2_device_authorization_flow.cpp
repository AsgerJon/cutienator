//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauth2deviceauthorizationflow.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauth2deviceauthorizationflow.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QOAuth2DeviceAuthorizationFlow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQOAuth2DeviceAuthorizationFlow : QOAuth2DeviceAuthorizationFlow {
  using QOAuth2DeviceAuthorizationFlow::event;
};

//  A QOAuth2DeviceAuthorizationFlow that Python can take functions over in. Every QOAuth2DeviceAuthorizationFlow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_HTTP)
typedef bool (*CuteQOAuth2DeviceAuthorizationFlowCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_HTTP)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2DeviceAuthorizationFlowCall2)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2DeviceAuthorizationFlowCall3)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2DeviceAuthorizationFlowCall4)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2DeviceAuthorizationFlowCall5)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall6)(const void *, QNetworkRequest *, const QByteArray *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuth2DeviceAuthorizationFlowCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2DeviceAuthorizationFlowCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOAuth2DeviceAuthorizationFlow : public QOAuth2DeviceAuthorizationFlow {
public:
  using QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth5grantEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByteArrayS4_")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_HTTP)
  //  void QOAuth2DeviceAuthorizationFlow::grant()
  void grant() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall0 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOAuth2DeviceAuthorizationFlow::grant();
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_HTTP)
  //  bool QOAuth2DeviceAuthorizationFlow::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall1 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QOAuth2DeviceAuthorizationFlow::event(event);
  }
#endif  // !defined(QT_NO_HTTP)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_HTTP)
  //  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
  //      QByteArray &data)
  QNetworkReply *post(const QUrl &url, const QByteArray &data) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall2 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall2>(taken[2]);
      void * given = call(this, &url, &data, &handled);
      if (handled) return static_cast<QNetworkReply *>(given);
    }
    return QAbstractOAuth2::post(url, data);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, QHttpMultiPart
  //      *multiPart)
  QNetworkReply *post(const QUrl &url, QHttpMultiPart *multiPart) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall3 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall3>(taken[3]);
      void * given = call(this, &url, multiPart, &handled);
      if (handled) return static_cast<QNetworkReply *>(given);
    }
    return QAbstractOAuth2::post(url, multiPart);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QByteArray
  //      &data)
  QNetworkReply *put(const QUrl &url, const QByteArray &data) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall4 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall4>(taken[4]);
      void * given = call(this, &url, &data, &handled);
      if (handled) return static_cast<QNetworkReply *>(given);
    }
    return QAbstractOAuth2::put(url, data);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, QHttpMultiPart
  //      *multiPart)
  QNetworkReply *put(const QUrl &url, QHttpMultiPart *multiPart) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall5 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall5>(taken[5]);
      void * given = call(this, &url, multiPart, &handled);
      if (handled) return static_cast<QNetworkReply *>(given);
    }
    return QAbstractOAuth2::put(url, multiPart);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QAbstractOAuth2::prepareRequest(QNetworkRequest *request, const
  //      QByteArray &verb, const QByteArray &body)
  void prepareRequest(
      QNetworkRequest *request,
      const QByteArray &verb,
      const QByteArray &body) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall6 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall6>(taken[6]);
      call(this, request, &verb, &body, &handled);
      if (handled) return;
    }
    QAbstractOAuth2::prepareRequest(request, verb, body);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall7 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall8 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall9 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall10 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall11 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQOAuth2DeviceAuthorizationFlowCall12 call = reinterpret_cast<CuteQOAuth2DeviceAuthorizationFlowCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOAuth2DeviceAuthorizationFlow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QOAuth2DeviceAuthorizationFlow10metaObjectEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return self->metaObject();
}

//  void *QOAuth2DeviceAuthorizationFlow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QOAuth2DeviceAuthorizationFlow11qt_metacastEPKc(
    QOAuth2DeviceAuthorizationFlow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOAuth2DeviceAuthorizationFlow::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QOAuth2DeviceAuthorizationFlow11qt_metacallEN11QMetaObject4CallEiPPv(
    QOAuth2DeviceAuthorizationFlow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOAuth2DeviceAuthorizationFlow::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QOAuth2DeviceAuthorizationFlow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOAuth2DeviceAuthorizationFlow::tr(s, c, n));
}

//  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow()
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlow *ritual_ZN30QOAuth2DeviceAuthorizationFlowC1Ev() {
  return new CuteQOAuth2DeviceAuthorizationFlow();
}

//  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlow *ritual_ZN30QOAuth2DeviceAuthorizationFlowC1EP7QObject(
    QObject *parent) {
  return new CuteQOAuth2DeviceAuthorizationFlow(parent);
}

//  QOAuth2DeviceAuthorizationFlow::QOAuth2DeviceAuthorizationFlow(QNetworkAc
//      cessManager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlow *ritual_ZN30QOAuth2DeviceAuthorizationFlowC1EP21QNetworkAccessManagerP7QObject(
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQOAuth2DeviceAuthorizationFlow(manager, parent);
}

//  QOAuth2DeviceAuthorizationFlow::~QOAuth2DeviceAuthorizationFlow()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlowD1Ev(
    QOAuth2DeviceAuthorizationFlow *self) {
  delete self;
}

//  QString QOAuth2DeviceAuthorizationFlow::userCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QOAuth2DeviceAuthorizationFlow8userCodeEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return new QString(self->userCode());
}

//  QUrl QOAuth2DeviceAuthorizationFlow::verificationUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK30QOAuth2DeviceAuthorizationFlow15verificationUrlEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return new QUrl(self->verificationUrl());
}

//  QUrl QOAuth2DeviceAuthorizationFlow::completeVerificationUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK30QOAuth2DeviceAuthorizationFlow23completeVerificationUrlEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return new QUrl(self->completeVerificationUrl());
}

//  bool QOAuth2DeviceAuthorizationFlow::isPolling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QOAuth2DeviceAuthorizationFlow9isPollingEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return self->isPolling();
}

//  QDateTime QOAuth2DeviceAuthorizationFlow::userCodeExpirationAt() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK30QOAuth2DeviceAuthorizationFlow20userCodeExpirationAtEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return new QDateTime(self->userCodeExpirationAt());
}

//  void QOAuth2DeviceAuthorizationFlow::grant()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow5grantEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  self->grant();
}

//  bool QOAuth2DeviceAuthorizationFlow::startTokenPolling()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QOAuth2DeviceAuthorizationFlow17startTokenPollingEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  return self->startTokenPolling();
}

//  void QOAuth2DeviceAuthorizationFlow::stopTokenPolling()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow16stopTokenPollingEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  self->stopTokenPolling();
}

//  void QOAuth2DeviceAuthorizationFlow::authorizeWithUserCode(const QUrl
//      &verificationUrl, const QString &userCode, const QUrl
//      &completeVerificationUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow21authorizeWithUserCodeERK4QUrlRK7QStringS2_(
    QOAuth2DeviceAuthorizationFlow *self,
    const QUrl *verificationUrl,
    const QString *userCode,
    const QUrl *completeVerificationUrl) {
  self->authorizeWithUserCode(
      *verificationUrl,
      *userCode,
      *completeVerificationUrl);
}

//  void QOAuth2DeviceAuthorizationFlow::userCodeChanged(const QString
//      &userCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow15userCodeChangedERK7QString(
    QOAuth2DeviceAuthorizationFlow *self,
    const QString *userCode) {
  self->userCodeChanged(*userCode);
}

//  void QOAuth2DeviceAuthorizationFlow::verificationUrlChanged(const QUrl
//      &verificationUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow22verificationUrlChangedERK4QUrl(
    QOAuth2DeviceAuthorizationFlow *self,
    const QUrl *verificationUrl) {
  self->verificationUrlChanged(*verificationUrl);
}

//  void QOAuth2DeviceAuthorizationFlow::completeVerificationUrlChanged(const
//      QUrl &completeVerificationUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow30completeVerificationUrlChangedERK4QUrl(
    QOAuth2DeviceAuthorizationFlow *self,
    const QUrl *completeVerificationUrl) {
  self->completeVerificationUrlChanged(*completeVerificationUrl);
}

//  void QOAuth2DeviceAuthorizationFlow::pollingChanged(bool polling)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow14pollingChangedEb(
    QOAuth2DeviceAuthorizationFlow *self,
    bool polling) {
  self->pollingChanged(polling);
}

//  void QOAuth2DeviceAuthorizationFlow::userCodeExpirationAtChanged(const
//      QDateTime &expiration)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow27userCodeExpirationAtChangedERK9QDateTime(
    QOAuth2DeviceAuthorizationFlow *self,
    const QDateTime *expiration) {
  self->userCodeExpirationAtChanged(*expiration);
}

//  bool QOAuth2DeviceAuthorizationFlow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QOAuth2DeviceAuthorizationFlow5eventEP6QEvent(
    QOAuth2DeviceAuthorizationFlow *self,
    QEvent *event) {
  return self->event(event);
}

//  void QOAuth2DeviceAuthorizationFlow::refreshTokensImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QOAuth2DeviceAuthorizationFlow27refreshTokensImplementationEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  self->refreshTokensImplementation();
}

//  QOAuth2DeviceAuthorizationFlowPrivate
//      *QOAuth2DeviceAuthorizationFlow::d_func()
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlowPrivate *ritual_ZN30QOAuth2DeviceAuthorizationFlow6d_funcEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  return self->d_func();
}

//  const QOAuth2DeviceAuthorizationFlowPrivate
//      *QOAuth2DeviceAuthorizationFlow::d_func() const
extern "C" Q_DECL_EXPORT
const QOAuth2DeviceAuthorizationFlowPrivate *ritual_ZNK30QOAuth2DeviceAuthorizationFlow6d_funcEv(
    const QOAuth2DeviceAuthorizationFlow *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOAuth2DeviceAuthorizationFlow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOAuth2DeviceAuthorizationFlow(
    QOAuth2DeviceAuthorizationFlow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOAuth2DeviceAuthorizationFlow *>(self)->take(key, call);
}

//  void QOAuth2DeviceAuthorizationFlow::grant()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QOAuth2DeviceAuthorizationFlow5grantEv(
    QOAuth2DeviceAuthorizationFlow *self) {
  self->QOAuth2DeviceAuthorizationFlow::grant();
}

//  bool QOAuth2DeviceAuthorizationFlow::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QOAuth2DeviceAuthorizationFlow5eventEP6QEvent(
    QOAuth2DeviceAuthorizationFlow *self,
    QEvent *event) {
  return static_cast<OwnQOAuth2DeviceAuthorizationFlow *>(self)->OwnQOAuth2DeviceAuthorizationFlow::event(
      event);
}

#endif  // !defined(QT_NO_HTTP)
