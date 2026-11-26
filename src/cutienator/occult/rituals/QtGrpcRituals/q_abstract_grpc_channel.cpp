//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qabstractgrpcchannel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qabstractgrpcchannel.h>
#include <QtGrpc/qgrpcchanneloptions.h>
#include <memory>
#include <QtProtobuf/QAbstractProtobufSerializer>

//  QAbstractGrpcChannel::~QAbstractGrpcChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannelD1Ev(QAbstractGrpcChannel *self) {
  delete self;
}

//  std::shared_ptr<QAbstractProtobufSerializer>
//      QAbstractGrpcChannel::serializer() const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QAbstractProtobufSerializer> *ritual_ZNK20QAbstractGrpcChannel10serializerEv(
    const QAbstractGrpcChannel *self) {
  return new std::shared_ptr<QAbstractProtobufSerializer>(
      self->serializer());
}

//  const QGrpcChannelOptions &QAbstractGrpcChannel::channelOptions() const
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZNKR20QAbstractGrpcChannel14channelOptionsEv(
    const QAbstractGrpcChannel *self) {
  return new QGrpcChannelOptions(self->channelOptions());
}

//  void QAbstractGrpcChannel::setChannelOptions(const QGrpcChannelOptions
//      &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel17setChannelOptionsERK19QGrpcChannelOptions(
    QAbstractGrpcChannel *self,
    const QGrpcChannelOptions *options) {
  self->setChannelOptions(*options);
}

//  void QAbstractGrpcChannel::setChannelOptions(QGrpcChannelOptions
//      &&options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel17setChannelOptionsEO19QGrpcChannelOptions(
    QAbstractGrpcChannel *self,
    QGrpcChannelOptions *options) {
  self->setChannelOptions(std::move(*options));
}

//  const QGrpcInterceptorChain &QAbstractGrpcChannel::interceptorChain()
//      const
extern "C" Q_DECL_EXPORT
const QGrpcInterceptorChain *ritual_ZNKR20QAbstractGrpcChannel16interceptorChainEv(
    const QAbstractGrpcChannel *self) {
  return &(self->interceptorChain());
}

//  void QAbstractGrpcChannel::call(QGrpcOperationContext *operationContext,
//      QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel4callEP21QGrpcOperationContextO10QByteArray(
    QAbstractGrpcChannel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->call(operationContext, std::move(*messageData));
}

//  void QAbstractGrpcChannel::serverStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel12serverStreamEP21QGrpcOperationContextO10QByteArray(
    QAbstractGrpcChannel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->serverStream(operationContext, std::move(*messageData));
}

//  void QAbstractGrpcChannel::clientStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel12clientStreamEP21QGrpcOperationContextO10QByteArray(
    QAbstractGrpcChannel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->clientStream(operationContext, std::move(*messageData));
}

//  void QAbstractGrpcChannel::bidiStream(QGrpcOperationContext
//      *operationContext, QByteArray &&messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel10bidiStreamEP21QGrpcOperationContextO10QByteArray(
    QAbstractGrpcChannel *self,
    QGrpcOperationContext *operationContext,
    QByteArray *messageData) {
  self->bidiStream(operationContext, std::move(*messageData));
}

//  QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func()
extern "C" Q_DECL_EXPORT
QAbstractGrpcChannelPrivate *ritual_ZN20QAbstractGrpcChannel6d_funcEv(
    QAbstractGrpcChannel *self) {
  return self->d_func();
}

//  const QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractGrpcChannelPrivate *ritual_ZNK20QAbstractGrpcChannel6d_funcEv(
    const QAbstractGrpcChannel *self) {
  return self->d_func();
}

//  a std::shared_ptr<QAbstractProtobufSerializer> a ritual of
//      QAbstractGrpcChannel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractGrpcChannel__std_shared_ptr_QAbstractProtobufSerializer(
    std::shared_ptr<QAbstractProtobufSerializer> *self) {
  delete self;
}
