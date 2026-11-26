//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauth1.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauth1.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <utility>
#include <QtCore/QString>

//  const QMetaObject *QOAuth1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QOAuth110metaObjectEv(const QOAuth1 *self) {
  return self->metaObject();
}

//  void *QOAuth1::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN7QOAuth111qt_metacastEPKc(QOAuth1 *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOAuth1::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QOAuth111qt_metacallEN11QMetaObject4CallEiPPv(
    QOAuth1 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOAuth1::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QOAuth12trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QOAuth1::tr(s, c, n));
}

//  QOAuth1::QOAuth1(QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth1 *ritual_ZN7QOAuth1C1EP7QObject(QObject *parent) {
  return new QOAuth1(parent);
}

//  QOAuth1::QOAuth1(QNetworkAccessManager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth1 *ritual_ZN7QOAuth1C1EP21QNetworkAccessManagerP7QObject(
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new QOAuth1(manager, parent);
}

//  QOAuth1::QOAuth1(const QString &clientIdentifier, const QString
//      &clientSharedSecret, QNetworkAccessManager *manager, QObject *parent)
extern "C" Q_DECL_EXPORT
QOAuth1 *ritual_ZN7QOAuth1C1ERK7QStringS2_P21QNetworkAccessManagerP7QObject(
    const QString *clientIdentifier,
    const QString *clientSharedSecret,
    QNetworkAccessManager *manager,
    QObject *parent) {
  return new QOAuth1(
      *clientIdentifier,
      *clientSharedSecret,
      manager,
      parent);
}

//  QString QOAuth1::clientSharedSecret() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QOAuth118clientSharedSecretEv(const QOAuth1 *self) {
  return new QString(self->clientSharedSecret());
}

//  void QOAuth1::setClientSharedSecret(const QString &clientSharedSecret)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth121setClientSharedSecretERK7QString(
    QOAuth1 *self,
    const QString *clientSharedSecret) {
  self->setClientSharedSecret(*clientSharedSecret);
}

//  std::pair<QString, QString> QOAuth1::clientCredentials() const
extern "C" Q_DECL_EXPORT
std::pair<QString, QString> *ritual_ZNK7QOAuth117clientCredentialsEv(
    const QOAuth1 *self) {
  return new std::pair<QString, QString>(self->clientCredentials());
}

//  void QOAuth1::setClientCredentials(const std::pair<QString, QString>
//      &clientCredentials)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth120setClientCredentialsERKSt4pairI7QStringS1_E(
    QOAuth1 *self,
    const std::pair<QString, QString> *clientCredentials) {
  self->setClientCredentials(*clientCredentials);
}

//  void QOAuth1::setClientCredentials(const QString &clientIdentifier, const
//      QString &clientSharedSecret)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth120setClientCredentialsERK7QStringS2_(
    QOAuth1 *self,
    const QString *clientIdentifier,
    const QString *clientSharedSecret) {
  self->setClientCredentials(*clientIdentifier, *clientSharedSecret);
}

//  QString QOAuth1::tokenSecret() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QOAuth111tokenSecretEv(const QOAuth1 *self) {
  return new QString(self->tokenSecret());
}

//  void QOAuth1::setTokenSecret(const QString &tokenSecret)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth114setTokenSecretERK7QString(
    QOAuth1 *self,
    const QString *tokenSecret) {
  self->setTokenSecret(*tokenSecret);
}

//  std::pair<QString, QString> QOAuth1::tokenCredentials() const
extern "C" Q_DECL_EXPORT
std::pair<QString, QString> *ritual_ZNK7QOAuth116tokenCredentialsEv(
    const QOAuth1 *self) {
  return new std::pair<QString, QString>(self->tokenCredentials());
}

//  void QOAuth1::setTokenCredentials(const std::pair<QString, QString>
//      &tokenCredentials)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth119setTokenCredentialsERKSt4pairI7QStringS1_E(
    QOAuth1 *self,
    const std::pair<QString, QString> *tokenCredentials) {
  self->setTokenCredentials(*tokenCredentials);
}

//  void QOAuth1::setTokenCredentials(const QString &token, const QString
//      &tokenSecret)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth119setTokenCredentialsERK7QStringS2_(
    QOAuth1 *self,
    const QString *token,
    const QString *tokenSecret) {
  self->setTokenCredentials(*token, *tokenSecret);
}

//  QUrl QOAuth1::temporaryCredentialsUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK7QOAuth123temporaryCredentialsUrlEv(const QOAuth1 *self) {
  return new QUrl(self->temporaryCredentialsUrl());
}

//  void QOAuth1::setTemporaryCredentialsUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth126setTemporaryCredentialsUrlERK4QUrl(
    QOAuth1 *self,
    const QUrl *url) {
  self->setTemporaryCredentialsUrl(*url);
}

//  QUrl QOAuth1::tokenCredentialsUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK7QOAuth119tokenCredentialsUrlEv(const QOAuth1 *self) {
  return new QUrl(self->tokenCredentialsUrl());
}

//  void QOAuth1::setTokenCredentialsUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth122setTokenCredentialsUrlERK4QUrl(
    QOAuth1 *self,
    const QUrl *url) {
  self->setTokenCredentialsUrl(*url);
}

//  SignatureMethod QOAuth1::signatureMethod() const
extern "C" Q_DECL_EXPORT
QOAuth1::SignatureMethod ritual_ZNK7QOAuth115signatureMethodEv(
    const QOAuth1 *self) {
  return self->signatureMethod();
}

//  void QOAuth1::setSignatureMethod(SignatureMethod value)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth118setSignatureMethodENS_15SignatureMethodE(
    QOAuth1 *self,
    QOAuth1::SignatureMethod value) {
  self->setSignatureMethod(value);
}

//  void QOAuth1::prepareRequest(QNetworkRequest *request, const QByteArray
//      &verb, const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth114prepareRequestEP15QNetworkRequestRK10QByteArrayS4_(
    QOAuth1 *self,
    QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *body) {
  self->prepareRequest(request, *verb, *body);
}

//  QNetworkReply *QOAuth1::head(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth14headERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->head(*url, *parameters);
}

//  QNetworkReply *QOAuth1::get(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth13getERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->get(*url, *parameters);
}

//  QNetworkReply *QOAuth1::post(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth14postERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->post(*url, *parameters);
}

//  QNetworkReply *QOAuth1::put(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth13putERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->put(*url, *parameters);
}

//  QNetworkReply *QOAuth1::deleteResource(const QUrl &url, const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth114deleteResourceERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->deleteResource(*url, *parameters);
}

//  void QOAuth1::grant()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth15grantEv(QOAuth1 *self) {
  self->grant();
}

//  void QOAuth1::continueGrantWithVerifier(const QString &verifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth125continueGrantWithVerifierERK7QString(
    QOAuth1 *self,
    const QString *verifier) {
  self->continueGrantWithVerifier(*verifier);
}

//  void QOAuth1::signatureMethodChanged(QOAuth1::SignatureMethod method)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth122signatureMethodChangedENS_15SignatureMethodE(
    QOAuth1 *self,
    QOAuth1::SignatureMethod method) {
  self->signatureMethodChanged(method);
}

//  void QOAuth1::clientSharedSecretChanged(const QString &credential)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth125clientSharedSecretChangedERK7QString(
    QOAuth1 *self,
    const QString *credential) {
  self->clientSharedSecretChanged(*credential);
}

//  void QOAuth1::tokenSecretChanged(const QString &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth118tokenSecretChangedERK7QString(
    QOAuth1 *self,
    const QString *token) {
  self->tokenSecretChanged(*token);
}

//  void QOAuth1::temporaryCredentialsUrlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth130temporaryCredentialsUrlChangedERK4QUrl(
    QOAuth1 *self,
    const QUrl *url) {
  self->temporaryCredentialsUrlChanged(*url);
}

//  void QOAuth1::tokenCredentialsUrlChanged(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth126tokenCredentialsUrlChangedERK4QUrl(
    QOAuth1 *self,
    const QUrl *url) {
  self->tokenCredentialsUrlChanged(*url);
}

//  QNetworkReply
//      *QOAuth1::requestTemporaryCredentials(QNetworkAccessManager::Operatio
//      n operation, const QUrl &url, const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth127requestTemporaryCredentialsEN21QNetworkAccessManager9OperationERK4QUrlRK4QMapI7QString8QVariantE(
    QOAuth1 *self,
    QNetworkAccessManager::Operation operation,
    const QUrl *url,
    const QMap<QString, QVariant> *parameters) {
  return self->requestTemporaryCredentials(operation, *url, *parameters);
}

//  QNetworkReply
//      *QOAuth1::requestTokenCredentials(QNetworkAccessManager::Operation
//      operation, const QUrl &url, const std::pair<QString, QString>
//      &temporaryToken, const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN7QOAuth123requestTokenCredentialsEN21QNetworkAccessManager9OperationERK4QUrlRKSt4pairI7QStringS6_ERK4QMapIS6_8QVariantE(
    QOAuth1 *self,
    QNetworkAccessManager::Operation operation,
    const QUrl *url,
    const std::pair<QString, QString> *temporaryToken,
    const QMap<QString, QVariant> *parameters) {
  return self->requestTokenCredentials(
      operation,
      *url,
      *temporaryToken,
      *parameters);
}

//  void QOAuth1::setup(QNetworkRequest *request, const QVariantMap
//      &signingParameters, QNetworkAccessManager::Operation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth15setupEP15QNetworkRequestRK4QMapI7QString8QVariantEN21QNetworkAccessManager9OperationE(
    QOAuth1 *self,
    QNetworkRequest *request,
    const QMap<QString, QVariant> *signingParameters,
    QNetworkAccessManager::Operation operation) {
  self->setup(request, *signingParameters, operation);
}

//  void QOAuth1::setup(QNetworkRequest *request, const QVariantMap
//      &signingParameters, const QByteArray &operationVerb)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QOAuth15setupEP15QNetworkRequestRK4QMapI7QString8QVariantERK10QByteArray(
    QOAuth1 *self,
    QNetworkRequest *request,
    const QMap<QString, QVariant> *signingParameters,
    const QByteArray *operationVerb) {
  self->setup(request, *signingParameters, *operationVerb);
}

//  QByteArray QOAuth1::nonce()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QOAuth15nonceEv() {
  return new QByteArray(QOAuth1::nonce());
}

//  QByteArray QOAuth1::generateAuthorizationHeader(const QVariantMap
//      &oauthParams)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QOAuth127generateAuthorizationHeaderERK4QMapI7QString8QVariantE(
    const QMap<QString, QVariant> *oauthParams) {
  return new QByteArray(QOAuth1::generateAuthorizationHeader(*oauthParams));
}

//  QOAuth1Private *QOAuth1::d_func()
extern "C" Q_DECL_EXPORT
QOAuth1Private *ritual_ZN7QOAuth16d_funcEv(QOAuth1 *self) {
  return self->d_func();
}

//  const QOAuth1Private *QOAuth1::d_func() const
extern "C" Q_DECL_EXPORT
const QOAuth1Private *ritual_ZNK7QOAuth16d_funcEv(const QOAuth1 *self) {
  return self->d_func();
}

//  void QOAuth1::prepareRequest(QNetworkRequest *request, const QByteArray
//      &verb, const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QOAuth114prepareRequestEP15QNetworkRequestRK10QByteArrayS4_(
    QOAuth1 *self,
    QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *body) {
  self->QOAuth1::prepareRequest(request, *verb, *body);
}

//  void QOAuth1::grant()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QOAuth15grantEv(QOAuth1 *self) {
  self->QOAuth1::grant();
}

//  a std::pair<QString, QString> a ritual of QOAuth1 gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOAuth1__std_pair_QString_QString(
    std::pair<QString, QString> *self) {
  delete self;
}

#endif  // !defined(QT_NO_HTTP)
