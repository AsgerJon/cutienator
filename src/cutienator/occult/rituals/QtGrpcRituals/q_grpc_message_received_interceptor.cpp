//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcMessageReceivedInterceptor::~QGrpcMessageReceivedInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QGrpcMessageReceivedInterceptorD1Ev(
    QGrpcMessageReceivedInterceptor *self) {
  delete self;
}

//  void QGrpcMessageReceivedInterceptor::onMessageReceived(QGrpcInterception
//      Context &context, QByteArray &messageData)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QGrpcMessageReceivedInterceptor17onMessageReceivedER24QGrpcInterceptionContextR10QByteArray(
    QGrpcMessageReceivedInterceptor *self,
    QGrpcInterceptionContext *context,
    QByteArray *messageData) {
  self->onMessageReceived(*context, *messageData);
}
