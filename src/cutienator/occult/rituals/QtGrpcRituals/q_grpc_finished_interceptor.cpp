//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcFinishedInterceptor::~QGrpcFinishedInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGrpcFinishedInterceptorD1Ev(
    QGrpcFinishedInterceptor *self) {
  delete self;
}

//  void QGrpcFinishedInterceptor::onFinished(QGrpcInterceptionContext
//      &context, QGrpcStatus &status)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGrpcFinishedInterceptor10onFinishedER24QGrpcInterceptionContextR11QGrpcStatus(
    QGrpcFinishedInterceptor *self,
    QGrpcInterceptionContext *context,
    QGrpcStatus *status) {
  self->onFinished(*context, *status);
}
