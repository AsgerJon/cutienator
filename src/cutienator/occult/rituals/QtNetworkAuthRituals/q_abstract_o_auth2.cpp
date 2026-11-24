//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qabstractoauth2.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qabstractoauth2.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QAbstractOAuth2 that Python can take functions over in. Every QAbstractOAuth2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQAbstractOAuth2Call0)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQAbstractOAuth2Call1)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQAbstractOAuth2Call2)(const void *, const QUrl *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void * (*CuteQAbstractOAuth2Call3)(const void *, const QUrl *, QHttpMultiPart *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQAbstractOAuth2Call4)(const void *, QNetworkRequest *, const QByteArray *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQAbstractOAuth2Call5)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuth2Call6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuth2Call7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuth2Call8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuth2Call9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuth2Call10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuth2Call11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuth2Call12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractOAuth2 : public QAbstractOAuth2 {
public:
  using QAbstractOAuth2::QAbstractOAuth2;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByteArrayS4_")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth5grantEv")) {
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
  //  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const
  //      QByteArray &data)
  QNetworkReply *post(const QUrl &url, const QByteArray &data) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractOAuth2Call0 call = reinterpret_cast<CuteQAbstractOAuth2Call0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractOAuth2Call1 call = reinterpret_cast<CuteQAbstractOAuth2Call1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractOAuth2Call2 call = reinterpret_cast<CuteQAbstractOAuth2Call2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractOAuth2Call3 call = reinterpret_cast<CuteQAbstractOAuth2Call3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractOAuth2Call4 call = reinterpret_cast<CuteQAbstractOAuth2Call4>(taken[4]);
      call(this, request, &verb, &body, &handled);
      if (handled) return;
    }
    QAbstractOAuth2::prepareRequest(request, verb, body);
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QAbstractOAuth::grant()
  void grant() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractOAuth2Call5 call = reinterpret_cast<CuteQAbstractOAuth2Call5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractOAuth2Call6 call = reinterpret_cast<CuteQAbstractOAuth2Call6>(taken[6]);
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
      CuteQAbstractOAuth2Call7 call = reinterpret_cast<CuteQAbstractOAuth2Call7>(taken[7]);
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
      CuteQAbstractOAuth2Call8 call = reinterpret_cast<CuteQAbstractOAuth2Call8>(taken[8]);
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
      CuteQAbstractOAuth2Call9 call = reinterpret_cast<CuteQAbstractOAuth2Call9>(taken[9]);
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
      CuteQAbstractOAuth2Call10 call = reinterpret_cast<CuteQAbstractOAuth2Call10>(taken[10]);
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
      CuteQAbstractOAuth2Call11 call = reinterpret_cast<CuteQAbstractOAuth2Call11>(taken[11]);
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
      CuteQAbstractOAuth2Call12 call = reinterpret_cast<CuteQAbstractOAuth2Call12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractOAuth2::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractOAuth210metaObjectEv(
    const QAbstractOAuth2 *self) {
  return self->metaObject();
}

//  QString QAbstractOAuth2::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractOAuth22trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractOAuth2::tr(s, c, n));
}

//  QAbstractOAuth2::~QAbstractOAuth2()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth2D1Ev(QAbstractOAuth2 *self) {
  delete self;
}

//  QUrl QAbstractOAuth2::createAuthenticatedUrl(const QUrl &url, const
//      QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN15QAbstractOAuth222createAuthenticatedUrlERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return new QUrl(self->createAuthenticatedUrl(*url, *parameters));
}

//  QNetworkReply *QAbstractOAuth2::head(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth24headERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->head(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth2::get(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth23getERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->get(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth24postERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->post(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->post(*url, *data);
}

//  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, QHttpMultiPart
//      *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart(
    QAbstractOAuth2 *self,
    const QUrl *url,
    QHttpMultiPart *multiPart) {
  return self->post(*url, multiPart);
}

//  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth23putERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->put(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->put(*url, *data);
}

//  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, QHttpMultiPart
//      *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart(
    QAbstractOAuth2 *self,
    const QUrl *url,
    QHttpMultiPart *multiPart) {
  return self->put(*url, multiPart);
}

//  QNetworkReply *QAbstractOAuth2::deleteResource(const QUrl &url, const
//      QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN15QAbstractOAuth214deleteResourceERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->deleteResource(*url, *parameters);
}

#if !defined(QOAUTH2_NO_LEGACY_SCOPE)
//  QString QAbstractOAuth2::scope() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth25scopeEv(const QAbstractOAuth2 *self) {
  return new QString(self->scope());
}
#endif  // !defined(QOAUTH2_NO_LEGACY_SCOPE)

#if !defined(QOAUTH2_NO_LEGACY_SCOPE)
//  void QAbstractOAuth2::setScope(const QString &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth28setScopeERK7QString(
    QAbstractOAuth2 *self,
    const QString *scope) {
  self->setScope(*scope);
}
#endif  // !defined(QOAUTH2_NO_LEGACY_SCOPE)

//  QString QAbstractOAuth2::userAgent() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth29userAgentEv(
    const QAbstractOAuth2 *self) {
  return new QString(self->userAgent());
}

//  void QAbstractOAuth2::setUserAgent(const QString &userAgent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth212setUserAgentERK7QString(
    QAbstractOAuth2 *self,
    const QString *userAgent) {
  self->setUserAgent(*userAgent);
}

//  QString QAbstractOAuth2::responseType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth212responseTypeEv(
    const QAbstractOAuth2 *self) {
  return new QString(self->responseType());
}

//  QString QAbstractOAuth2::clientIdentifierSharedKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth225clientIdentifierSharedKeyEv(
    const QAbstractOAuth2 *self) {
  return new QString(self->clientIdentifierSharedKey());
}

//  void QAbstractOAuth2::setClientIdentifierSharedKey(const QString
//      &clientIdentifierSharedKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth228setClientIdentifierSharedKeyERK7QString(
    QAbstractOAuth2 *self,
    const QString *clientIdentifierSharedKey) {
  self->setClientIdentifierSharedKey(*clientIdentifierSharedKey);
}

//  QString QAbstractOAuth2::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth25stateEv(const QAbstractOAuth2 *self) {
  return new QString(self->state());
}

//  void QAbstractOAuth2::setState(const QString &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth28setStateERK7QString(
    QAbstractOAuth2 *self,
    const QString *state) {
  self->setState(*state);
}

//  QDateTime QAbstractOAuth2::expirationAt() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QAbstractOAuth212expirationAtEv(
    const QAbstractOAuth2 *self) {
  return new QDateTime(self->expirationAt());
}

//  QString QAbstractOAuth2::refreshToken() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth212refreshTokenEv(
    const QAbstractOAuth2 *self) {
  return new QString(self->refreshToken());
}

//  void QAbstractOAuth2::setRefreshToken(const QString &refreshToken)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth215setRefreshTokenERK7QString(
    QAbstractOAuth2 *self,
    const QString *refreshToken) {
  self->setRefreshToken(*refreshToken);
}

//  bool QAbstractOAuth2::autoRefresh() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractOAuth211autoRefreshEv(
    const QAbstractOAuth2 *self) {
  return self->autoRefresh();
}

//  void QAbstractOAuth2::setAutoRefresh(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth214setAutoRefreshEb(
    QAbstractOAuth2 *self,
    bool enable) {
  self->setAutoRefresh(enable);
}

//  NonceMode QAbstractOAuth2::nonceMode() const
extern "C" Q_DECL_EXPORT
QAbstractOAuth2::NonceMode ritual_ZNK15QAbstractOAuth29nonceModeEv(
    const QAbstractOAuth2 *self) {
  return self->nonceMode();
}

//  void QAbstractOAuth2::setNonceMode(NonceMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth212setNonceModeENS_9NonceModeE(
    QAbstractOAuth2 *self,
    QAbstractOAuth2::NonceMode mode) {
  self->setNonceMode(mode);
}

//  QString QAbstractOAuth2::nonce() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth25nonceEv(const QAbstractOAuth2 *self) {
  return new QString(self->nonce());
}

//  void QAbstractOAuth2::setNonce(const QString &nonce)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth28setNonceERK7QString(
    QAbstractOAuth2 *self,
    const QString *nonce) {
  self->setNonce(*nonce);
}

//  QString QAbstractOAuth2::idToken() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractOAuth27idTokenEv(const QAbstractOAuth2 *self) {
  return new QString(self->idToken());
}

//  QUrl QAbstractOAuth2::tokenUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QAbstractOAuth28tokenUrlEv(const QAbstractOAuth2 *self) {
  return new QUrl(self->tokenUrl());
}

//  void QAbstractOAuth2::setTokenUrl(const QUrl &tokenUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth211setTokenUrlERK4QUrl(
    QAbstractOAuth2 *self,
    const QUrl *tokenUrl) {
  self->setTokenUrl(*tokenUrl);
}

#if !defined(QT_NO_SSL)
//  QSslConfiguration QAbstractOAuth2::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK15QAbstractOAuth216sslConfigurationEv(
    const QAbstractOAuth2 *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QAbstractOAuth2::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth219setSslConfigurationERK17QSslConfiguration(
    QAbstractOAuth2 *self,
    const QSslConfiguration *configuration) {
  self->setSslConfiguration(*configuration);
}
#endif  // !defined(QT_NO_SSL)

//  void QAbstractOAuth2::prepareRequest(QNetworkRequest *request, const
//      QByteArray &verb, const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth214prepareRequestEP15QNetworkRequestRK10QByteArrayS4_(
    QAbstractOAuth2 *self,
    QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *body) {
  self->prepareRequest(request, *verb, *body);
}

//  void QAbstractOAuth2::clearNetworkRequestModifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth227clearNetworkRequestModifierEv(
    QAbstractOAuth2 *self) {
  self->clearNetworkRequestModifier();
}

//  void QAbstractOAuth2::refreshTokensImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth227refreshTokensImplementationEv(
    QAbstractOAuth2 *self) {
  self->refreshTokensImplementation();
}

//  void QAbstractOAuth2::refreshTokens()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth213refreshTokensEv(QAbstractOAuth2 *self) {
  self->refreshTokens();
}

//  void QAbstractOAuth2::setResponseType(const QString &responseType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth215setResponseTypeERK7QString(
    QAbstractOAuth2 *self,
    const QString *responseType) {
  self->setResponseType(*responseType);
}

//  void QAbstractOAuth2::setNetworkRequestModifierImpl(const QObject
//      *context, QtPrivate::QSlotObjectBase *slot)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractOAuth229setNetworkRequestModifierImplEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QAbstractOAuth2 *self,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slot) {
  self->setNetworkRequestModifierImpl(context, slot);
}

//  QAbstractOAuth2Private *QAbstractOAuth2::d_func()
extern "C" Q_DECL_EXPORT
QAbstractOAuth2Private *ritual_ZN15QAbstractOAuth26d_funcEv(
    QAbstractOAuth2 *self) {
  return self->d_func();
}

//  const QAbstractOAuth2Private *QAbstractOAuth2::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractOAuth2Private *ritual_ZNK15QAbstractOAuth26d_funcEv(
    const QAbstractOAuth2 *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractOAuth2, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractOAuth2(
    QAbstractOAuth2 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractOAuth2 *>(self)->take(key, call);
}

//  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_own_ZN15QAbstractOAuth24postERK4QUrlRK10QByteArray(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->QAbstractOAuth2::post(*url, *data);
}

//  QNetworkReply *QAbstractOAuth2::post(const QUrl &url, QHttpMultiPart
//      *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_own_ZN15QAbstractOAuth24postERK4QUrlP14QHttpMultiPart(
    QAbstractOAuth2 *self,
    const QUrl *url,
    QHttpMultiPart *multiPart) {
  return self->QAbstractOAuth2::post(*url, multiPart);
}

//  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_own_ZN15QAbstractOAuth23putERK4QUrlRK10QByteArray(
    QAbstractOAuth2 *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->QAbstractOAuth2::put(*url, *data);
}

//  QNetworkReply *QAbstractOAuth2::put(const QUrl &url, QHttpMultiPart
//      *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_own_ZN15QAbstractOAuth23putERK4QUrlP14QHttpMultiPart(
    QAbstractOAuth2 *self,
    const QUrl *url,
    QHttpMultiPart *multiPart) {
  return self->QAbstractOAuth2::put(*url, multiPart);
}

//  void QAbstractOAuth2::prepareRequest(QNetworkRequest *request, const
//      QByteArray &verb, const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractOAuth214prepareRequestEP15QNetworkRequestRK10QByteArrayS4_(
    QAbstractOAuth2 *self,
    QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *body) {
  self->QAbstractOAuth2::prepareRequest(request, *verb, *body);
}

#endif  // !defined(QT_NO_HTTP)
