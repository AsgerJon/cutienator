//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverresponse.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtHttpServer/QHttpServerResponse>
#include <QtCore/QString>

//  QHttpServerResponsePrivate *QHttpServerResponse::d_func()
extern "C" Q_DECL_EXPORT
QHttpServerResponsePrivate *ritual_ZN19QHttpServerResponse6d_funcEv(
    QHttpServerResponse *self) {
  return self->d_func();
}

//  const QHttpServerResponsePrivate *QHttpServerResponse::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpServerResponsePrivate *ritual_ZNK19QHttpServerResponse6d_funcEv(
    const QHttpServerResponse *self) {
  return self->d_func();
}

//  QHttpServerResponse::QHttpServerResponse(QHttpServerResponse &&other)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1EOS_(
    QHttpServerResponse *other) {
  return new QHttpServerResponse(std::move(*other));
}

//  QHttpServerResponse &QHttpServerResponse::operator=(QHttpServerResponse
//      &&other)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseaSEOS_(
    QHttpServerResponse *self,
    QHttpServerResponse *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QHttpServerResponse::swap(QHttpServerResponse &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpServerResponse4swapERS_(
    QHttpServerResponse *self,
    QHttpServerResponse *other) {
  self->swap(*other);
}

//  QHttpServerResponse::QHttpServerResponse(StatusCode statusCode)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1EN20QHttpServerResponder10StatusCodeE(
    QHttpServerResponse::StatusCode statusCode) {
  return new QHttpServerResponse(statusCode);
}

//  QHttpServerResponse::QHttpServerResponse(const char *data, StatusCode
//      status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1EPKcN20QHttpServerResponder10StatusCodeE(
    const char *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(data, status);
}

//  QHttpServerResponse::QHttpServerResponse(const QString &data, StatusCode
//      status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK7QStringN20QHttpServerResponder10StatusCodeE(
    const QString *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*data, status);
}

//  QHttpServerResponse::QHttpServerResponse(const QByteArray &data,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK10QByteArrayN20QHttpServerResponder10StatusCodeE(
    const QByteArray *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*data, status);
}

//  QHttpServerResponse::QHttpServerResponse(QByteArray &&data, StatusCode
//      status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1EO10QByteArrayN20QHttpServerResponder10StatusCodeE(
    QByteArray *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(std::move(*data), status);
}

//  QHttpServerResponse::QHttpServerResponse(const QJsonObject &data,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK11QJsonObjectN20QHttpServerResponder10StatusCodeE(
    const QJsonObject *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*data, status);
}

//  QHttpServerResponse::QHttpServerResponse(const QJsonArray &data,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK10QJsonArrayN20QHttpServerResponder10StatusCodeE(
    const QJsonArray *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*data, status);
}

//  QHttpServerResponse::QHttpServerResponse(const QByteArray &mimeType,
//      const QByteArray &data, StatusCode status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK10QByteArrayS2_N20QHttpServerResponder10StatusCodeE(
    const QByteArray *mimeType,
    const QByteArray *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*mimeType, *data, status);
}

//  QHttpServerResponse::QHttpServerResponse(const QByteArray &mimeType,
//      QByteArray &&data, StatusCode status)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponseC1ERK10QByteArrayOS0_N20QHttpServerResponder10StatusCodeE(
    const QByteArray *mimeType,
    QByteArray *data,
    QHttpServerResponse::StatusCode status) {
  return new QHttpServerResponse(*mimeType, std::move(*data), status);
}

//  QHttpServerResponse::~QHttpServerResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpServerResponseD1Ev(QHttpServerResponse *self) {
  delete self;
}

//  QHttpServerResponse QHttpServerResponse::fromFile(const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
QHttpServerResponse *ritual_ZN19QHttpServerResponse8fromFileERK7QString(
    const QString *fileName) {
  return new QHttpServerResponse(QHttpServerResponse::fromFile(*fileName));
}

//  QByteArray QHttpServerResponse::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpServerResponse4dataEv(
    const QHttpServerResponse *self) {
  return new QByteArray(self->data());
}

//  QByteArray QHttpServerResponse::mimeType() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpServerResponse8mimeTypeEv(
    const QHttpServerResponse *self) {
  return new QByteArray(self->mimeType());
}

//  StatusCode QHttpServerResponse::statusCode() const
extern "C" Q_DECL_EXPORT
QHttpServerResponse::StatusCode ritual_ZNK19QHttpServerResponse10statusCodeEv(
    const QHttpServerResponse *self) {
  return self->statusCode();
}

//  QHttpHeaders QHttpServerResponse::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK19QHttpServerResponse7headersEv(
    const QHttpServerResponse *self) {
  return new QHttpHeaders(self->headers());
}

//  void QHttpServerResponse::setHeaders(const QHttpHeaders &newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpServerResponse10setHeadersERK12QHttpHeaders(
    QHttpServerResponse *self,
    const QHttpHeaders *newHeaders) {
  self->setHeaders(*newHeaders);
}

//  void QHttpServerResponse::setHeaders(QHttpHeaders &&newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpServerResponse10setHeadersEO12QHttpHeaders(
    QHttpServerResponse *self,
    QHttpHeaders *newHeaders) {
  self->setHeaders(std::move(*newHeaders));
}

//  a QHttpServerResponse a ritual of QHttpServerResponse gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHttpServerResponse__QHttpServerResponse(
    QHttpServerResponse *self) {
  delete self;
}
