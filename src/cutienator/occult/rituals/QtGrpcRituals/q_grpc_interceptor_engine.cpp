//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSpan>

//  QGrpcInterceptorEngine::QGrpcInterceptorEngine(const QAbstractGrpcChannel
//      &parentChannel)
extern "C" Q_DECL_EXPORT
QGrpcInterceptorEngine *ritual_ZN22QGrpcInterceptorEngineC1ERK20QAbstractGrpcChannel(
    const QAbstractGrpcChannel *parentChannel) {
  return new QGrpcInterceptorEngine(*parentChannel);
}

//  const QGrpcInterceptorChain &QGrpcInterceptorEngine::interceptorChain()
//      const
extern "C" Q_DECL_EXPORT
const QGrpcInterceptorChain *ritual_ZNK22QGrpcInterceptorEngine16interceptorChainEv(
    const QGrpcInterceptorEngine *self) {
  return &(self->interceptorChain());
}

//  bool QGrpcInterceptorEngine::hasHandlerFor(QtGrpc::InterceptorCapability
//      capability) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGrpcInterceptorEngine13hasHandlerForEN6QtGrpc21InterceptorCapabilityE(
    const QGrpcInterceptorEngine *self,
    QtGrpc::InterceptorCapability capability) {
  return self->hasHandlerFor(capability);
}

//  QGrpcStartInterceptor::Continuation
//      QGrpcInterceptorEngine::onStart(QGrpcOperationContext &context,
//      QProtobufMessage &message, QGrpcCallOptions &callOptions)
extern "C" Q_DECL_EXPORT
QGrpcStartInterceptor::Continuation ritual_ZN22QGrpcInterceptorEngine7onStartER21QGrpcOperationContextR16QProtobufMessageR16QGrpcCallOptions(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QProtobufMessage *message,
    QGrpcCallOptions *callOptions) {
  return self->onStart(*context, *message, *callOptions);
}

//  void QGrpcInterceptorEngine::onInitialMetadata(QGrpcOperationContext
//      &context, QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine17onInitialMetadataER21QGrpcOperationContextR10QMultiHashI10QByteArrayS3_E(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->onInitialMetadata(*context, *metadata);
}

//  void QGrpcInterceptorEngine::onMessageReceived(QGrpcOperationContext
//      &context, QByteArray &messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine17onMessageReceivedER21QGrpcOperationContextR10QByteArray(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QByteArray *messageData) {
  self->onMessageReceived(*context, *messageData);
}

//  void QGrpcInterceptorEngine::onWriteMessage(QGrpcOperationContext
//      &context, QProtobufMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine14onWriteMessageER21QGrpcOperationContextR16QProtobufMessage(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QProtobufMessage *message) {
  self->onWriteMessage(*context, *message);
}

//  void QGrpcInterceptorEngine::onWritesDone(QGrpcOperationContext &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine12onWritesDoneER21QGrpcOperationContext(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context) {
  self->onWritesDone(*context);
}

//  void QGrpcInterceptorEngine::onTrailingMetadata(QGrpcOperationContext
//      &context, QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine18onTrailingMetadataER21QGrpcOperationContextR10QMultiHashI10QByteArrayS3_E(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->onTrailingMetadata(*context, *metadata);
}

//  void QGrpcInterceptorEngine::onFinished(QGrpcOperationContext &context,
//      QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine10onFinishedER21QGrpcOperationContextR11QGrpcStatus(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context,
    QGrpcStatus *status) {
  self->onFinished(*context, *status);
}

//  void QGrpcInterceptorEngine::onCancel(QGrpcOperationContext &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine8onCancelER21QGrpcOperationContext(
    QGrpcInterceptorEngine *self,
    QGrpcOperationContext *context) {
  self->onCancel(*context);
}

//  void QGrpcInterceptorEngine::addInterceptor(QSpan<const
//      QtGrpcPrivate::InterceptorCapabilityBinding> bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcInterceptorEngine14addInterceptorE5QSpanIKN13QtGrpcPrivate28InterceptorCapabilityBindingELm18446744073709551615EE(
    QGrpcInterceptorEngine *self,
    const QSpan<const QtGrpcPrivate::InterceptorCapabilityBinding> *bindings) {
  self->addInterceptor(*bindings);
}
