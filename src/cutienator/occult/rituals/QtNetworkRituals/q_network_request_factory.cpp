//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkrequestfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtNetwork/qnetworkrequestfactory.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>

//  QNetworkRequestFactory::QNetworkRequestFactory()
extern "C" Q_DECL_EXPORT
QNetworkRequestFactory *ritual_ZN22QNetworkRequestFactoryC1Ev() {
  return new QNetworkRequestFactory();
}

//  QNetworkRequestFactory::QNetworkRequestFactory(const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
QNetworkRequestFactory *ritual_ZN22QNetworkRequestFactoryC1ERK4QUrl(
    const QUrl *baseUrl) {
  return new QNetworkRequestFactory(*baseUrl);
}

//  QNetworkRequestFactory::~QNetworkRequestFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactoryD1Ev(QNetworkRequestFactory *self) {
  delete self;
}

//  QNetworkRequestFactory::QNetworkRequestFactory(const
//      QNetworkRequestFactory &other)
extern "C" Q_DECL_EXPORT
QNetworkRequestFactory *ritual_ZN22QNetworkRequestFactoryC1ERKS_(
    const QNetworkRequestFactory *other) {
  return new QNetworkRequestFactory(*other);
}

//  QUrl QNetworkRequestFactory::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK22QNetworkRequestFactory7baseUrlEv(
    const QNetworkRequestFactory *self) {
  return new QUrl(self->baseUrl());
}

//  void QNetworkRequestFactory::setBaseUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory10setBaseUrlERK4QUrl(
    QNetworkRequestFactory *self,
    const QUrl *url) {
  self->setBaseUrl(*url);
}

#if QT_CONFIG(ssl)
//  QSslConfiguration QNetworkRequestFactory::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK22QNetworkRequestFactory16sslConfigurationEv(
    const QNetworkRequestFactory *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QNetworkRequestFactory::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory19setSslConfigurationERK17QSslConfiguration(
    QNetworkRequestFactory *self,
    const QSslConfiguration *configuration) {
  self->setSslConfiguration(*configuration);
}
#endif  // QT_CONFIG(ssl)

//  QNetworkRequest QNetworkRequestFactory::createRequest() const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK22QNetworkRequestFactory13createRequestEv(
    const QNetworkRequestFactory *self) {
  return new QNetworkRequest(self->createRequest());
}

//  QNetworkRequest QNetworkRequestFactory::createRequest(const QUrlQuery
//      &query) const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK22QNetworkRequestFactory13createRequestERK9QUrlQuery(
    const QNetworkRequestFactory *self,
    const QUrlQuery *query) {
  return new QNetworkRequest(self->createRequest(*query));
}

//  QNetworkRequest QNetworkRequestFactory::createRequest(const QString
//      &path) const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK22QNetworkRequestFactory13createRequestERK7QString(
    const QNetworkRequestFactory *self,
    const QString *path) {
  return new QNetworkRequest(self->createRequest(*path));
}

//  QNetworkRequest QNetworkRequestFactory::createRequest(const QString
//      &path, const QUrlQuery &query) const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK22QNetworkRequestFactory13createRequestERK7QStringRK9QUrlQuery(
    const QNetworkRequestFactory *self,
    const QString *path,
    const QUrlQuery *query) {
  return new QNetworkRequest(self->createRequest(*path, *query));
}

//  void QNetworkRequestFactory::setCommonHeaders(const QHttpHeaders
//      &headers)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory16setCommonHeadersERK12QHttpHeaders(
    QNetworkRequestFactory *self,
    const QHttpHeaders *headers) {
  self->setCommonHeaders(*headers);
}

//  QHttpHeaders QNetworkRequestFactory::commonHeaders() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK22QNetworkRequestFactory13commonHeadersEv(
    const QNetworkRequestFactory *self) {
  return new QHttpHeaders(self->commonHeaders());
}

//  void QNetworkRequestFactory::clearCommonHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory18clearCommonHeadersEv(
    QNetworkRequestFactory *self) {
  self->clearCommonHeaders();
}

//  QByteArray QNetworkRequestFactory::bearerToken() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QNetworkRequestFactory11bearerTokenEv(
    const QNetworkRequestFactory *self) {
  return new QByteArray(self->bearerToken());
}

//  void QNetworkRequestFactory::setBearerToken(const QByteArray &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory14setBearerTokenERK10QByteArray(
    QNetworkRequestFactory *self,
    const QByteArray *token) {
  self->setBearerToken(*token);
}

//  void QNetworkRequestFactory::clearBearerToken()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory16clearBearerTokenEv(
    QNetworkRequestFactory *self) {
  self->clearBearerToken();
}

//  QString QNetworkRequestFactory::userName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QNetworkRequestFactory8userNameEv(
    const QNetworkRequestFactory *self) {
  return new QString(self->userName());
}

//  void QNetworkRequestFactory::setUserName(const QString &userName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory11setUserNameERK7QString(
    QNetworkRequestFactory *self,
    const QString *userName) {
  self->setUserName(*userName);
}

//  void QNetworkRequestFactory::clearUserName()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory13clearUserNameEv(
    QNetworkRequestFactory *self) {
  self->clearUserName();
}

//  QString QNetworkRequestFactory::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QNetworkRequestFactory8passwordEv(
    const QNetworkRequestFactory *self) {
  return new QString(self->password());
}

//  void QNetworkRequestFactory::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory11setPasswordERK7QString(
    QNetworkRequestFactory *self,
    const QString *password) {
  self->setPassword(*password);
}

//  void QNetworkRequestFactory::clearPassword()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory13clearPasswordEv(
    QNetworkRequestFactory *self) {
  self->clearPassword();
}

//  QUrlQuery QNetworkRequestFactory::queryParameters() const
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZNK22QNetworkRequestFactory15queryParametersEv(
    const QNetworkRequestFactory *self) {
  return new QUrlQuery(self->queryParameters());
}

//  void QNetworkRequestFactory::setQueryParameters(const QUrlQuery &query)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory18setQueryParametersERK9QUrlQuery(
    QNetworkRequestFactory *self,
    const QUrlQuery *query) {
  self->setQueryParameters(*query);
}

//  void QNetworkRequestFactory::clearQueryParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory20clearQueryParametersEv(
    QNetworkRequestFactory *self) {
  self->clearQueryParameters();
}

//  void QNetworkRequestFactory::setPriority(QNetworkRequest::Priority
//      priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory11setPriorityEN15QNetworkRequest8PriorityE(
    QNetworkRequestFactory *self,
    QNetworkRequest::Priority priority) {
  self->setPriority(priority);
}

//  QNetworkRequest::Priority QNetworkRequestFactory::priority() const
extern "C" Q_DECL_EXPORT
QNetworkRequest::Priority ritual_ZNK22QNetworkRequestFactory8priorityEv(
    const QNetworkRequestFactory *self) {
  return self->priority();
}

//  QVariant QNetworkRequestFactory::attribute(QNetworkRequest::Attribute
//      attribute) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QNetworkRequestFactory9attributeEN15QNetworkRequest9AttributeE(
    const QNetworkRequestFactory *self,
    QNetworkRequest::Attribute attribute) {
  return new QVariant(self->attribute(attribute));
}

//  QVariant QNetworkRequestFactory::attribute(QNetworkRequest::Attribute
//      attribute, const QVariant &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QNetworkRequestFactory9attributeEN15QNetworkRequest9AttributeERK8QVariant(
    const QNetworkRequestFactory *self,
    QNetworkRequest::Attribute attribute,
    const QVariant *defaultValue) {
  return new QVariant(self->attribute(attribute, *defaultValue));
}

//  void QNetworkRequestFactory::setAttribute(QNetworkRequest::Attribute
//      attribute, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory12setAttributeEN15QNetworkRequest9AttributeERK8QVariant(
    QNetworkRequestFactory *self,
    QNetworkRequest::Attribute attribute,
    const QVariant *value) {
  self->setAttribute(attribute, *value);
}

//  void QNetworkRequestFactory::clearAttribute(QNetworkRequest::Attribute
//      attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory14clearAttributeEN15QNetworkRequest9AttributeE(
    QNetworkRequestFactory *self,
    QNetworkRequest::Attribute attribute) {
  self->clearAttribute(attribute);
}

//  void QNetworkRequestFactory::clearAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkRequestFactory15clearAttributesEv(
    QNetworkRequestFactory *self) {
  self->clearAttributes();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QNetworkRequestFactory &reply)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK22QNetworkRequestFactory(
    const QDebug *debug,
    const QNetworkRequestFactory *reply) {
  return new QDebug(operator<<(*debug, *reply));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
