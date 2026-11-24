//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qauthenticator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qauthenticator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qauthenticator.h>
#include <QtNetwork/qhttpheaders.h>

//  QAuthenticatorPrivate::QAuthenticatorPrivate()
extern "C" Q_DECL_EXPORT
QAuthenticatorPrivate *ritual_ZN21QAuthenticatorPrivateC1Ev() {
  return new QAuthenticatorPrivate();
}

//  QAuthenticatorPrivate::~QAuthenticatorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAuthenticatorPrivateD1Ev(QAuthenticatorPrivate *self) {
  delete self;
}

//  QByteArray QAuthenticatorPrivate::calculateResponse(QByteArrayView
//      method, QByteArrayView path, QStringView host)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QAuthenticatorPrivate17calculateResponseE14QByteArrayViewS0_11QStringView(
    QAuthenticatorPrivate *self,
    const QByteArrayView *method,
    const QByteArrayView *path,
    const QString *host) {
  return new QByteArray(
      self->calculateResponse(
          *method,
          *path,
          QStringView(*host)));
}

//  const QAuthenticatorPrivate *QAuthenticatorPrivate::getPrivate(const
//      QAuthenticator &auth)
extern "C" Q_DECL_EXPORT
const QAuthenticatorPrivate *ritual_ZN21QAuthenticatorPrivate10getPrivateERK14QAuthenticator(
    const QAuthenticator *auth) {
  return QAuthenticatorPrivate::getPrivate(*auth);
}

//  QByteArray QAuthenticatorPrivate::digestMd5Response(QByteArrayView
//      challenge, QByteArrayView method, QByteArrayView path)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QAuthenticatorPrivate17digestMd5ResponseE14QByteArrayViewS0_S0_(
    QAuthenticatorPrivate *self,
    const QByteArrayView *challenge,
    const QByteArrayView *method,
    const QByteArrayView *path) {
  return new QByteArray(self->digestMd5Response(*challenge, *method, *path));
}

//  void QAuthenticatorPrivate::parseHttpResponse(const QHttpHeaders
//      &headers, bool isProxy, QStringView host)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAuthenticatorPrivate17parseHttpResponseERK12QHttpHeadersb11QStringView(
    QAuthenticatorPrivate *self,
    const QHttpHeaders *headers,
    bool isProxy,
    const QString *host) {
  self->parseHttpResponse(*headers, isProxy, QStringView(*host));
}

//  void QAuthenticatorPrivate::updateCredentials()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAuthenticatorPrivate17updateCredentialsEv(
    QAuthenticatorPrivate *self) {
  self->updateCredentials();
}

//  bool QAuthenticatorPrivate::isMethodSupported(QByteArrayView method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAuthenticatorPrivate17isMethodSupportedE14QByteArrayView(
    const QByteArrayView *method) {
  return QAuthenticatorPrivate::isMethodSupported(*method);
}
