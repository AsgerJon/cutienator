//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauth2authorizationcodeflow.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauth2authorizationcodeflow.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOAuth2AuthorizationCodeFlow that Python can take functions over in. Every QOAuth2AuthorizationCodeFlow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall0)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2AuthorizationCodeFlowCall1)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2AuthorizationCodeFlowCall2)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2AuthorizationCodeFlowCall3)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQOAuth2AuthorizationCodeFlowCall4)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall5)(const void *, QNetworkRequest *, const QByteArray *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuth2AuthorizationCodeFlowCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOAuth2AuthorizationCodeFlowCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOAuth2AuthorizationCodeFlowCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOAuth2AuthorizationCodeFlow : public QOAuth2AuthorizationCodeFlow {
public:
  using QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth5grantEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByteArrayS4_")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
  //  void QOAuth2AuthorizationCodeFlow::grant()
  void grant() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall0 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QOAuth2AuthorizationCodeFlow::grant();
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
  //      QByteArray &data)
  QNetworkReply *post(const QUrl &url, const QByteArray &data) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall1 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall2 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall3 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall4 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall5 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall5>(taken[5]);
      call(this, request, &verb, &body, &handled);
      if (handled) return;
    }
    QAbstractOAuth2::prepareRequest(request, verb, body);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall6 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOAuth2AuthorizationCodeFlowCall7 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall7>(taken[7]);
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
      CuteQOAuth2AuthorizationCodeFlowCall8 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall8>(taken[8]);
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
      CuteQOAuth2AuthorizationCodeFlowCall9 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall9>(taken[9]);
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
      CuteQOAuth2AuthorizationCodeFlowCall10 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall10>(taken[10]);
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
      CuteQOAuth2AuthorizationCodeFlowCall11 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall11>(taken[11]);
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
      CuteQOAuth2AuthorizationCodeFlowCall12 call = reinterpret_cast<CuteQOAuth2AuthorizationCodeFlowCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOAuth2AuthorizationCodeFlow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QOAuth2AuthorizationCodeFlow10metaObjectEv(
    const QOAuth2AuthorizationCodeFlow *self) {
  return self->metaObject();
}

//  QString QOAuth2AuthorizationCodeFlow::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QOAuth2AuthorizationCodeFlow2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOAuth2AuthorizationCodeFlow::tr(s, c, n));
}

//  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN28QOAuth2AuthorizationCodeFlowC1EP7QObject(
    QObject *parent) {
  return new CuteQOAuth2AuthorizationCodeFlow(parent);
}

//  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(QNetworkAccess
//      Manager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN28QOAuth2AuthorizationCodeFlowC1EP21QNetworkAccessManagerP7QObject(
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQOAuth2AuthorizationCodeFlow(manager, parent);
}

//  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QString
//      &clientIdentifier, QNetworkAccessManager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK7QStringP21QNetworkAccessManagerP7QObject(
    const QString *clientIdentifier,
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQOAuth2AuthorizationCodeFlow(
      *clientIdentifier,
      manager,
      parent);
}

//  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QUrl
//      &authorizationUrl, const QUrl &accessTokenUrl, QNetworkAccessManager
//      *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK4QUrlS2_P21QNetworkAccessManagerP7QObject(
    const QUrl *authorizationUrl,
    const QUrl *accessTokenUrl,
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQOAuth2AuthorizationCodeFlow(
      *authorizationUrl,
      *accessTokenUrl,
      manager,
      parent);
}

//  QOAuth2AuthorizationCodeFlow::QOAuth2AuthorizationCodeFlow(const QString
//      &clientIdentifier, const QUrl &authorizationUrl, const QUrl
//      &accessTokenUrl, QNetworkAccessManager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN28QOAuth2AuthorizationCodeFlowC1ERK7QStringRK4QUrlS5_P21QNetworkAccessManagerP7QObject(
    const QString *clientIdentifier,
    const QUrl *authorizationUrl,
    const QUrl *accessTokenUrl,
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new CuteQOAuth2AuthorizationCodeFlow(
      *clientIdentifier,
      *authorizationUrl,
      *accessTokenUrl,
      manager,
      parent);
}

//  QOAuth2AuthorizationCodeFlow::~QOAuth2AuthorizationCodeFlow()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlowD1Ev(
    QOAuth2AuthorizationCodeFlow *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 13)
//  QUrl QOAuth2AuthorizationCodeFlow::accessTokenUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QOAuth2AuthorizationCodeFlow14accessTokenUrlEv(
    const QOAuth2AuthorizationCodeFlow *self) {
  return new QUrl(self->accessTokenUrl());
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QOAuth2AuthorizationCodeFlow::setAccessTokenUrl(const QUrl
//      &accessTokenUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow17setAccessTokenUrlERK4QUrl(
    QOAuth2AuthorizationCodeFlow *self,
    const QUrl *accessTokenUrl) {
  self->setAccessTokenUrl(*accessTokenUrl);
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  void QOAuth2AuthorizationCodeFlow::setPkceMethod(PkceMethod method,
//      qsizetype length)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow13setPkceMethodENS_10PkceMethodEx(
    QOAuth2AuthorizationCodeFlow *self,
    QOAuth2AuthorizationCodeFlow::PkceMethod method,
    qsizetype length) {
  self->setPkceMethod(method, length);
}

//  PkceMethod QOAuth2AuthorizationCodeFlow::pkceMethod() const
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow::PkceMethod ritual_ZNK28QOAuth2AuthorizationCodeFlow10pkceMethodEv(
    const QOAuth2AuthorizationCodeFlow *self) {
  return self->pkceMethod();
}

//  void QOAuth2AuthorizationCodeFlow::grant()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow5grantEv(
    QOAuth2AuthorizationCodeFlow *self) {
  self->grant();
}

#if QT_DEPRECATED_SINCE(6, 13)
//  void QOAuth2AuthorizationCodeFlow::refreshAccessToken()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow18refreshAccessTokenEv(
    QOAuth2AuthorizationCodeFlow *self) {
  self->refreshAccessToken();
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  void QOAuth2AuthorizationCodeFlow::refreshTokensImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow27refreshTokensImplementationEv(
    QOAuth2AuthorizationCodeFlow *self) {
  self->refreshTokensImplementation();
}

//  void QOAuth2AuthorizationCodeFlow::requestAccessToken(const QString
//      &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOAuth2AuthorizationCodeFlow18requestAccessTokenERK7QString(
    QOAuth2AuthorizationCodeFlow *self,
    const QString *code) {
  self->requestAccessToken(*code);
}

//  QOAuth2AuthorizationCodeFlowPrivate
//      *QOAuth2AuthorizationCodeFlow::d_func()
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlowPrivate *ritual_ZN28QOAuth2AuthorizationCodeFlow6d_funcEv(
    QOAuth2AuthorizationCodeFlow *self) {
  return self->d_func();
}

//  const QOAuth2AuthorizationCodeFlowPrivate
//      *QOAuth2AuthorizationCodeFlow::d_func() const
extern "C" Q_DECL_EXPORT
const QOAuth2AuthorizationCodeFlowPrivate *ritual_ZNK28QOAuth2AuthorizationCodeFlow6d_funcEv(
    const QOAuth2AuthorizationCodeFlow *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOAuth2AuthorizationCodeFlow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOAuth2AuthorizationCodeFlow(
    QOAuth2AuthorizationCodeFlow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOAuth2AuthorizationCodeFlow *>(self)->take(key, call);
}

//  void QOAuth2AuthorizationCodeFlow::grant()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QOAuth2AuthorizationCodeFlow5grantEv(
    QOAuth2AuthorizationCodeFlow *self) {
  self->QOAuth2AuthorizationCodeFlow::grant();
}

#endif  // !defined(QT_NO_HTTP)
