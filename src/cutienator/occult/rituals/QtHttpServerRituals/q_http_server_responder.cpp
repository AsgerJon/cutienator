//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverresponder.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qjsondocument.h>

//  QHttpServerResponderPrivate *QHttpServerResponder::d_func()
extern "C" Q_DECL_EXPORT
QHttpServerResponderPrivate *ritual_ZN20QHttpServerResponder6d_funcEv(
    QHttpServerResponder *self) {
  return self->d_func();
}

//  const QHttpServerResponderPrivate *QHttpServerResponder::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpServerResponderPrivate *ritual_ZNK20QHttpServerResponder6d_funcEv(
    const QHttpServerResponder *self) {
  return self->d_func();
}

//  QHttpServerResponder::~QHttpServerResponder()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponderD1Ev(QHttpServerResponder *self) {
  delete self;
}

//  void QHttpServerResponder::write(QIODevice *data, const QHttpHeaders
//      &headers, StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeEP9QIODeviceRK12QHttpHeadersNS_10StatusCodeE(
    QHttpServerResponder *self,
    QIODevice *data,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(data, *headers, status);
}

//  void QHttpServerResponder::write(QIODevice *data, const QByteArray
//      &mimeType, StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeEP9QIODeviceRK10QByteArrayNS_10StatusCodeE(
    QHttpServerResponder *self,
    QIODevice *data,
    const QByteArray *mimeType,
    QHttpServerResponder::StatusCode status) {
  self->write(data, *mimeType, status);
}

//  void QHttpServerResponder::write(const QJsonDocument &document, const
//      QHttpHeaders &headers, StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeERK13QJsonDocumentRK12QHttpHeadersNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QJsonDocument *document,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(*document, *headers, status);
}

//  void QHttpServerResponder::write(const QJsonDocument &document,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeERK13QJsonDocumentNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QJsonDocument *document,
    QHttpServerResponder::StatusCode status) {
  self->write(*document, status);
}

//  void QHttpServerResponder::write(const QByteArray &data, const
//      QHttpHeaders &headers, StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeERK10QByteArrayRK12QHttpHeadersNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QByteArray *data,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(*data, *headers, status);
}

//  void QHttpServerResponder::write(const QByteArray &data, const QByteArray
//      &mimeType, StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeERK10QByteArrayS2_NS_10StatusCodeE(
    QHttpServerResponder *self,
    const QByteArray *data,
    const QByteArray *mimeType,
    QHttpServerResponder::StatusCode status) {
  self->write(*data, *mimeType, status);
}

//  void QHttpServerResponder::write(const QHttpHeaders &headers, StatusCode
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeERK12QHttpHeadersNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(*headers, status);
}

//  void QHttpServerResponder::write(StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder5writeENS_10StatusCodeE(
    QHttpServerResponder *self,
    QHttpServerResponder::StatusCode status) {
  self->write(status);
}

//  void QHttpServerResponder::writeBeginChunked(const QHttpHeaders &headers,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder17writeBeginChunkedERK12QHttpHeadersNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->writeBeginChunked(*headers, status);
}

//  void QHttpServerResponder::writeBeginChunked(const QByteArray &mimeType,
//      StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder17writeBeginChunkedERK10QByteArrayNS_10StatusCodeE(
    QHttpServerResponder *self,
    const QByteArray *mimeType,
    QHttpServerResponder::StatusCode status) {
  self->writeBeginChunked(*mimeType, status);
}

//  void QHttpServerResponder::writeChunk(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder10writeChunkERK10QByteArray(
    QHttpServerResponder *self,
    const QByteArray *data) {
  self->writeChunk(*data);
}

//  void QHttpServerResponder::writeEndChunked(const QByteArray &data, const
//      QHttpHeaders &trailers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder15writeEndChunkedERK10QByteArrayRK12QHttpHeaders(
    QHttpServerResponder *self,
    const QByteArray *data,
    const QHttpHeaders *trailers) {
  self->writeEndChunked(*data, *trailers);
}

//  void QHttpServerResponder::writeEndChunked(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHttpServerResponder15writeEndChunkedERK10QByteArray(
    QHttpServerResponder *self,
    const QByteArray *data) {
  self->writeEndChunked(*data);
}

//  bool QHttpServerResponder::isResponseCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QHttpServerResponder18isResponseCanceledEv(
    const QHttpServerResponder *self) {
  return self->isResponseCanceled();
}

//  QHttpServerResponder::QHttpServerResponder(QHttpServerStream *stream)
extern "C" Q_DECL_EXPORT
QHttpServerResponder *ritual_ZN20QHttpServerResponderC1EP17QHttpServerStream(
    QHttpServerStream *stream) {
  return new QHttpServerResponder(stream);
}
