//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qabstractoauth.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qabstractoauth.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtNetworkAuth/QAbstractOAuth>

//  A QAbstractOAuth that Python can take functions over in. Every QAbstractOAuth
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_HTTP)
typedef void (*CuteQAbstractOAuthCall0)(const void *, QNetworkRequest *, const QByteArray *, const QByteArray *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
typedef void (*CuteQAbstractOAuthCall1)(const void *, int *);
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuthCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractOAuthCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractOAuthCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractOAuth : public QAbstractOAuth {
public:
  using QAbstractOAuth::QAbstractOAuth;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByteArrayS4_")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_HTTP)
    if (!std::strcmp(key, "_ZN14QAbstractOAuth5grantEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_HTTP)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_HTTP)
  //  void QAbstractOAuth::prepareRequest(QNetworkRequest *request, const
  //      QByteArray &verb, const QByteArray &body)
  void prepareRequest(
      QNetworkRequest *request,
      const QByteArray &verb,
      const QByteArray &body) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractOAuthCall0 call = reinterpret_cast<CuteQAbstractOAuthCall0>(taken[0]);
      call(this, request, &verb, &body, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_HTTP)
  //  void QAbstractOAuth::grant()
  void grant() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractOAuthCall1 call = reinterpret_cast<CuteQAbstractOAuthCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_HTTP)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractOAuthCall2 call = reinterpret_cast<CuteQAbstractOAuthCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractOAuthCall3 call = reinterpret_cast<CuteQAbstractOAuthCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractOAuthCall4 call = reinterpret_cast<CuteQAbstractOAuthCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractOAuthCall5 call = reinterpret_cast<CuteQAbstractOAuthCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractOAuthCall6 call = reinterpret_cast<CuteQAbstractOAuthCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractOAuthCall7 call = reinterpret_cast<CuteQAbstractOAuthCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractOAuthCall8 call = reinterpret_cast<CuteQAbstractOAuthCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractOAuth::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAbstractOAuth10metaObjectEv(
    const QAbstractOAuth *self) {
  return self->metaObject();
}

//  void *QAbstractOAuth::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QAbstractOAuth11qt_metacastEPKc(
    QAbstractOAuth *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractOAuth::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAbstractOAuth11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractOAuth *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractOAuth::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QAbstractOAuth2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractOAuth::tr(s, c, n));
}

//  QAbstractOAuth::~QAbstractOAuth()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuthD1Ev(QAbstractOAuth *self) {
  delete self;
}

//  QString QAbstractOAuth::clientIdentifier() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAbstractOAuth16clientIdentifierEv(
    const QAbstractOAuth *self) {
  return new QString(self->clientIdentifier());
}

//  void QAbstractOAuth::setClientIdentifier(const QString &clientIdentifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth19setClientIdentifierERK7QString(
    QAbstractOAuth *self,
    const QString *clientIdentifier) {
  self->setClientIdentifier(*clientIdentifier);
}

//  QString QAbstractOAuth::token() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAbstractOAuth5tokenEv(const QAbstractOAuth *self) {
  return new QString(self->token());
}

//  void QAbstractOAuth::setToken(const QString &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth8setTokenERK7QString(
    QAbstractOAuth *self,
    const QString *token) {
  self->setToken(*token);
}

//  QNetworkAccessManager *QAbstractOAuth::networkAccessManager() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZNK14QAbstractOAuth20networkAccessManagerEv(
    const QAbstractOAuth *self) {
  return self->networkAccessManager();
}

//  void QAbstractOAuth::setNetworkAccessManager(QNetworkAccessManager
//      *networkAccessManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth23setNetworkAccessManagerEP21QNetworkAccessManager(
    QAbstractOAuth *self,
    QNetworkAccessManager *networkAccessManager) {
  self->setNetworkAccessManager(networkAccessManager);
}

//  Status QAbstractOAuth::status() const
extern "C" Q_DECL_EXPORT
QAbstractOAuth::Status ritual_ZNK14QAbstractOAuth6statusEv(
    const QAbstractOAuth *self) {
  return self->status();
}

//  QUrl QAbstractOAuth::authorizationUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QAbstractOAuth16authorizationUrlEv(
    const QAbstractOAuth *self) {
  return new QUrl(self->authorizationUrl());
}

//  void QAbstractOAuth::setAuthorizationUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth19setAuthorizationUrlERK4QUrl(
    QAbstractOAuth *self,
    const QUrl *url) {
  self->setAuthorizationUrl(*url);
}

//  QVariantMap QAbstractOAuth::extraTokens() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK14QAbstractOAuth11extraTokensEv(
    const QAbstractOAuth *self) {
  return new QMap<QString, QVariant>(self->extraTokens());
}

//  QAbstractOAuthReplyHandler *QAbstractOAuth::replyHandler() const
extern "C" Q_DECL_EXPORT
QAbstractOAuthReplyHandler *ritual_ZNK14QAbstractOAuth12replyHandlerEv(
    const QAbstractOAuth *self) {
  return self->replyHandler();
}

//  void QAbstractOAuth::setReplyHandler(QAbstractOAuthReplyHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth15setReplyHandlerEP26QAbstractOAuthReplyHandler(
    QAbstractOAuth *self,
    QAbstractOAuthReplyHandler *handler) {
  self->setReplyHandler(handler);
}

//  QNetworkReply *QAbstractOAuth::head(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN14QAbstractOAuth4headERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->head(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth::get(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN14QAbstractOAuth3getERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->get(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth::post(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN14QAbstractOAuth4postERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->post(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth::put(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN14QAbstractOAuth3putERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->put(*url, *parameters);
}

//  QNetworkReply *QAbstractOAuth::deleteResource(const QUrl &url, const
//      QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN14QAbstractOAuth14deleteResourceERK4QUrlRK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->deleteResource(*url, *parameters);
}

//  void QAbstractOAuth::prepareRequest(QNetworkRequest *request, const
//      QByteArray &verb, const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth14prepareRequestEP15QNetworkRequestRK10QByteArrayS4_(
    QAbstractOAuth *self,
    QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *body) {
  self->prepareRequest(request, *verb, *body);
}

//  ModifyParametersFunction QAbstractOAuth::modifyParametersFunction() const
extern "C" Q_DECL_EXPORT
QAbstractOAuth::ModifyParametersFunction *ritual_ZNK14QAbstractOAuth24modifyParametersFunctionEv(
    const QAbstractOAuth *self) {
  return new QAbstractOAuth::ModifyParametersFunction(
      self->modifyParametersFunction());
}

//  void QAbstractOAuth::setModifyParametersFunction(const
//      ModifyParametersFunction &modifyParametersFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth27setModifyParametersFunctionERKSt8functionIFvNS_5StageEP9QMultiMapI7QString8QVariantEEE(
    QAbstractOAuth *self,
    const QAbstractOAuth::ModifyParametersFunction *modifyParametersFunction) {
  self->setModifyParametersFunction(*modifyParametersFunction);
}

//  ContentType QAbstractOAuth::contentType() const
extern "C" Q_DECL_EXPORT
QAbstractOAuth::ContentType ritual_ZNK14QAbstractOAuth11contentTypeEv(
    const QAbstractOAuth *self) {
  return self->contentType();
}

//  void QAbstractOAuth::setContentType(ContentType contentType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth14setContentTypeENS_11ContentTypeE(
    QAbstractOAuth *self,
    QAbstractOAuth::ContentType contentType) {
  self->setContentType(contentType);
}

//  void QAbstractOAuth::grant()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth5grantEv(QAbstractOAuth *self) {
  self->grant();
}

//  void QAbstractOAuth::clientIdentifierChanged(const QString
//      &clientIdentifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth23clientIdentifierChangedERK7QString(
    QAbstractOAuth *self,
    const QString *clientIdentifier) {
  self->clientIdentifierChanged(*clientIdentifier);
}

//  void QAbstractOAuth::tokenChanged(const QString &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth12tokenChangedERK7QString(
    QAbstractOAuth *self,
    const QString *token) {
  self->tokenChanged(*token);
}

//  void QAbstractOAuth::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth13statusChangedENS_6StatusE(
    QAbstractOAuth *self,
    QAbstractOAuth::Status status) {
  self->statusChanged(status);
}

//  void QAbstractOAuth::authorizationUrlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth23authorizationUrlChangedERK4QUrl(
    QAbstractOAuth *self,
    const QUrl *url) {
  self->authorizationUrlChanged(*url);
}

//  void QAbstractOAuth::extraTokensChanged(const QVariantMap &tokens)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth18extraTokensChangedERK4QMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QMap<QString, QVariant> *tokens) {
  self->extraTokensChanged(*tokens);
}

//  void QAbstractOAuth::contentTypeChanged(ContentType contentType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth18contentTypeChangedENS_11ContentTypeE(
    QAbstractOAuth *self,
    QAbstractOAuth::ContentType contentType) {
  self->contentTypeChanged(contentType);
}

//  void QAbstractOAuth::requestFailed(const Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth13requestFailedENS_5ErrorE(
    QAbstractOAuth *self,
    const QAbstractOAuth::Error *error) {
  self->requestFailed(*error);
}

//  void QAbstractOAuth::authorizeWithBrowser(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth20authorizeWithBrowserERK4QUrl(
    QAbstractOAuth *self,
    const QUrl *url) {
  self->authorizeWithBrowser(*url);
}

//  void QAbstractOAuth::granted()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth7grantedEv(QAbstractOAuth *self) {
  self->granted();
}

//  void QAbstractOAuth::finished(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth8finishedEP13QNetworkReply(
    QAbstractOAuth *self,
    QNetworkReply *reply) {
  self->finished(reply);
}

//  void QAbstractOAuth::replyDataReceived(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth17replyDataReceivedERK10QByteArray(
    QAbstractOAuth *self,
    const QByteArray *data) {
  self->replyDataReceived(*data);
}

//  void QAbstractOAuth::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth9setStatusENS_6StatusE(
    QAbstractOAuth *self,
    QAbstractOAuth::Status status) {
  self->setStatus(status);
}

//  QString QAbstractOAuth::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QAbstractOAuth8callbackEv(const QAbstractOAuth *self) {
  return new QString(self->callback());
}

//  void QAbstractOAuth::resourceOwnerAuthorization(const QUrl &url, const
//      QMultiMap<QString, QVariant> &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractOAuth26resourceOwnerAuthorizationERK4QUrlRK9QMultiMapI7QString8QVariantE(
    QAbstractOAuth *self,
    const QUrl *url,
    const QMultiMap<QString, QVariant> *parameters) {
  self->resourceOwnerAuthorization(*url, *parameters);
}

//  QByteArray QAbstractOAuth::generateRandomString(quint8 length)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QAbstractOAuth20generateRandomStringEh(
    quint8 length) {
  return new QByteArray(QAbstractOAuth::generateRandomString(length));
}

//  QAbstractOAuthPrivate *QAbstractOAuth::d_func()
extern "C" Q_DECL_EXPORT
QAbstractOAuthPrivate *ritual_ZN14QAbstractOAuth6d_funcEv(
    QAbstractOAuth *self) {
  return self->d_func();
}

//  const QAbstractOAuthPrivate *QAbstractOAuth::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractOAuthPrivate *ritual_ZNK14QAbstractOAuth6d_funcEv(
    const QAbstractOAuth *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractOAuth, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractOAuth(
    QAbstractOAuth *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractOAuth *>(self)->take(key, call);
}

//  a QAbstractOAuth::ModifyParametersFunction a ritual of QAbstractOAuth
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractOAuth__QAbstractOAuth_ModifyParametersFunction(
    QAbstractOAuth::ModifyParametersFunction *self) {
  delete self;
}

#endif  // !defined(QT_NO_HTTP)
