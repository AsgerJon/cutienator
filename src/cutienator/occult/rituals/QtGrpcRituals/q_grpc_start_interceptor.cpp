//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcStartInterceptor::~QGrpcStartInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcStartInterceptorD1Ev(QGrpcStartInterceptor *self) {
  delete self;
}

//  Continuation QGrpcStartInterceptor::onStart(QGrpcInterceptionContext
//      &context, QProtobufMessage &message, QGrpcCallOptions &callOptions)
extern "C" Q_DECL_EXPORT
QGrpcStartInterceptor::Continuation ritual_ZN21QGrpcStartInterceptor7onStartER24QGrpcInterceptionContextR16QProtobufMessageR16QGrpcCallOptions(
    QGrpcStartInterceptor *self,
    QGrpcInterceptionContext *context,
    QProtobufMessage *message,
    QGrpcCallOptions *callOptions) {
  return self->onStart(*context, *message, *callOptions);
}
