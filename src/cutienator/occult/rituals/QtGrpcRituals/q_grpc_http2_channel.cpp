//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpchttp2channel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpchttp2channel.h>
#include <QtCore/qurl.h>
#include <QtGrpc/qgrpcchanneloptions.h>
#include <memory>
#include <QtProtobuf/QAbstractProtobufSerializer>

//  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri)
extern "C" Q_DECL_EXPORT
QGrpcHttp2Channel *ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrl(
    const QUrl *hostUri) {
  return new QGrpcHttp2Channel(*hostUri);
}

//  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri, const
//      QGrpcChannelOptions &options)
extern "C" Q_DECL_EXPORT
QGrpcHttp2Channel *ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrlRK19QGrpcChannelOptions(
    const QUrl *hostUri,
    const QGrpcChannelOptions *options) {
  return new QGrpcHttp2Channel(*hostUri, *options);
}

//  QGrpcHttp2Channel::~QGrpcHttp2Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2ChannelD1Ev(QGrpcHttp2Channel *self) {
  delete self;
}

//  QUrl QGrpcHttp2Channel::hostUri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QGrpcHttp2Channel7hostUriEv(
    const QGrpcHttp2Channel *self) {
  return new QUrl(self->hostUri());
}

//  void QGrpcHttp2Channel::call(QGrpcOperationContext *operationContext,
//      QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2Channel4callEP21QGrpcOperationContextO10QByteArray(
    QGrpcHttp2Channel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->call(operationContext, std::move(*messageData));
}

//  void QGrpcHttp2Channel::serverStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2Channel12serverStreamEP21QGrpcOperationContextO10QByteArray(
    QGrpcHttp2Channel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->serverStream(operationContext, std::move(*messageData));
}

//  void QGrpcHttp2Channel::clientStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2Channel12clientStreamEP21QGrpcOperationContextO10QByteArray(
    QGrpcHttp2Channel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->clientStream(operationContext, std::move(*messageData));
}

//  void QGrpcHttp2Channel::bidiStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2Channel10bidiStreamEP21QGrpcOperationContextO10QByteArray(
    QGrpcHttp2Channel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->bidiStream(operationContext, std::move(*messageData));
}

//  std::shared_ptr<QAbstractProtobufSerializer>
//      QGrpcHttp2Channel::serializer() const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QAbstractProtobufSerializer> *ritual_ZNK17QGrpcHttp2Channel10serializerEv(
    const QGrpcHttp2Channel *self) {
  return new std::shared_ptr<QAbstractProtobufSerializer>(
      self->serializer());
}

//  a std::shared_ptr<QAbstractProtobufSerializer> a ritual of
//      QGrpcHttp2Channel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcHttp2Channel__std_shared_ptr_QAbstractProtobufSerializer(
    std::shared_ptr<QAbstractProtobufSerializer> *self) {
  delete self;
}
