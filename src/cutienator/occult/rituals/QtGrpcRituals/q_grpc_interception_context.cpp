//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtGrpc/qgrpccalloptions.h>

//  QGrpcInterceptionContext::~QGrpcInterceptionContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGrpcInterceptionContextD1Ev(
    QGrpcInterceptionContext *self) {
  delete self;
}

//  quint32 QGrpcInterceptionContext::version() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QGrpcInterceptionContext7versionEv(
    const QGrpcInterceptionContext *self) {
  return self->version();
}

//  const QAbstractGrpcChannel &QGrpcInterceptionContext::channel() const
extern "C" Q_DECL_EXPORT
const QAbstractGrpcChannel *ritual_ZNKR24QGrpcInterceptionContext7channelEv(
    const QGrpcInterceptionContext *self) {
  return &(self->channel());
}

//  QtGrpc::RpcDescriptor QGrpcInterceptionContext::descriptor() const
extern "C" Q_DECL_EXPORT
QtGrpc::RpcDescriptor *ritual_ZNK24QGrpcInterceptionContext10descriptorEv(
    const QGrpcInterceptionContext *self) {
  return new QtGrpc::RpcDescriptor(self->descriptor());
}

//  const QGrpcCallOptions &QGrpcInterceptionContext::callOptions() const
extern "C" Q_DECL_EXPORT
QGrpcCallOptions *ritual_ZNKR24QGrpcInterceptionContext11callOptionsEv(
    const QGrpcInterceptionContext *self) {
  return new QGrpcCallOptions(self->callOptions());
}

//  quint64 QGrpcInterceptionContext::operationId() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK24QGrpcInterceptionContext11operationIdEv(
    const QGrpcInterceptionContext *self) {
  return self->operationId();
}

//  QGrpcInterceptionContext::QGrpcInterceptionContext(const
//      QAbstractGrpcChannel &channel, QGrpcOperationContext &context)
extern "C" Q_DECL_EXPORT
QGrpcInterceptionContext *ritual_ZN24QGrpcInterceptionContextC1ERK20QAbstractGrpcChannelR21QGrpcOperationContext(
    const QAbstractGrpcChannel *channel,
    QGrpcOperationContext *context) {
  return new QGrpcInterceptionContext(*channel, *context);
}
