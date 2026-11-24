//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/qoauth1signature.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetworkAuth/qoauthglobal.h>
#if !defined(QT_NO_HTTP)
#include <QtNetworkAuth/qoauth1signature.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QOAuth1Signature::QOAuth1Signature(const QOAuth1Signature &other)
extern "C" Q_DECL_EXPORT
QOAuth1Signature *ritual_ZN16QOAuth1SignatureC1ERKS_(
    const QOAuth1Signature *other) {
  return new QOAuth1Signature(*other);
}

//  QOAuth1Signature::~QOAuth1Signature()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1SignatureD1Ev(QOAuth1Signature *self) {
  delete self;
}

//  HttpRequestMethod QOAuth1Signature::httpRequestMethod() const
extern "C" Q_DECL_EXPORT
QOAuth1Signature::HttpRequestMethod ritual_ZNK16QOAuth1Signature17httpRequestMethodEv(
    const QOAuth1Signature *self) {
  return self->httpRequestMethod();
}

//  void QOAuth1Signature::setHttpRequestMethod(HttpRequestMethod method)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature20setHttpRequestMethodENS_17HttpRequestMethodE(
    QOAuth1Signature *self,
    QOAuth1Signature::HttpRequestMethod method) {
  self->setHttpRequestMethod(method);
}

//  QByteArray QOAuth1Signature::customMethodString() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QOAuth1Signature18customMethodStringEv(
    const QOAuth1Signature *self) {
  return new QByteArray(self->customMethodString());
}

//  void QOAuth1Signature::setCustomMethodString(const QByteArray &verb)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature21setCustomMethodStringERK10QByteArray(
    QOAuth1Signature *self,
    const QByteArray *verb) {
  self->setCustomMethodString(*verb);
}

//  QUrl QOAuth1Signature::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QOAuth1Signature3urlEv(const QOAuth1Signature *self) {
  return new QUrl(self->url());
}

//  void QOAuth1Signature::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature6setUrlERK4QUrl(
    QOAuth1Signature *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  void QOAuth1Signature::addRequestBody(const QUrlQuery &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature14addRequestBodyERK9QUrlQuery(
    QOAuth1Signature *self,
    const QUrlQuery *body) {
  self->addRequestBody(*body);
}

//  void QOAuth1Signature::insert(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature6insertERK7QStringRK8QVariant(
    QOAuth1Signature *self,
    const QString *key,
    const QVariant *value) {
  self->insert(*key, *value);
}

//  QList<QString> QOAuth1Signature::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QOAuth1Signature4keysEv(
    const QOAuth1Signature *self) {
  return new QList<QString>(self->keys());
}

//  QVariant QOAuth1Signature::take(const QString &key)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN16QOAuth1Signature4takeERK7QString(
    QOAuth1Signature *self,
    const QString *key) {
  return new QVariant(self->take(*key));
}

//  QVariant QOAuth1Signature::value(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QOAuth1Signature5valueERK7QStringRK8QVariant(
    const QOAuth1Signature *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->value(*key, *defaultValue));
}

//  QString QOAuth1Signature::clientSharedKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QOAuth1Signature15clientSharedKeyEv(
    const QOAuth1Signature *self) {
  return new QString(self->clientSharedKey());
}

//  void QOAuth1Signature::setClientSharedKey(const QString &secret)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature18setClientSharedKeyERK7QString(
    QOAuth1Signature *self,
    const QString *secret) {
  self->setClientSharedKey(*secret);
}

//  QString QOAuth1Signature::tokenSecret() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QOAuth1Signature11tokenSecretEv(
    const QOAuth1Signature *self) {
  return new QString(self->tokenSecret());
}

//  void QOAuth1Signature::setTokenSecret(const QString &secret)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOAuth1Signature14setTokenSecretERK7QString(
    QOAuth1Signature *self,
    const QString *secret) {
  self->setTokenSecret(*secret);
}

//  QByteArray QOAuth1Signature::hmacSha1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QOAuth1Signature8hmacSha1Ev(
    const QOAuth1Signature *self) {
  return new QByteArray(self->hmacSha1());
}

//  QByteArray QOAuth1Signature::rsaSha1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QOAuth1Signature7rsaSha1Ev(
    const QOAuth1Signature *self) {
  return new QByteArray(self->rsaSha1());
}

//  QByteArray QOAuth1Signature::plainText() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QOAuth1Signature9plainTextEv(
    const QOAuth1Signature *self) {
  return new QByteArray(self->plainText());
}

//  QByteArray QOAuth1Signature::plainText(const QString &clientSharedSecret,
//      const QString &tokenSecret)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QOAuth1Signature9plainTextERK7QStringS2_(
    const QString *clientSharedSecret,
    const QString *tokenSecret) {
  return new QByteArray(
      QOAuth1Signature::plainText(
          *clientSharedSecret,
          *tokenSecret));
}

#endif  // !defined(QT_NO_HTTP)
