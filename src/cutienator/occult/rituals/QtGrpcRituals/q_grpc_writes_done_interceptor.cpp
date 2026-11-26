//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcWritesDoneInterceptor::~QGrpcWritesDoneInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGrpcWritesDoneInterceptorD1Ev(
    QGrpcWritesDoneInterceptor *self) {
  delete self;
}

//  void QGrpcWritesDoneInterceptor::onWritesDone(QGrpcInterceptionContext
//      &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGrpcWritesDoneInterceptor12onWritesDoneER24QGrpcInterceptionContext(
    QGrpcWritesDoneInterceptor *self,
    QGrpcInterceptionContext *context) {
  self->onWritesDone(*context);
}
