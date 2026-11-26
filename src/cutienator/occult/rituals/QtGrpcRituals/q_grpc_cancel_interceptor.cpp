//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcCancelInterceptor::~QGrpcCancelInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcCancelInterceptorD1Ev(QGrpcCancelInterceptor *self) {
  delete self;
}

//  void QGrpcCancelInterceptor::onCancel(QGrpcInterceptionContext &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGrpcCancelInterceptor8onCancelER24QGrpcInterceptionContext(
    QGrpcCancelInterceptor *self,
    QGrpcInterceptionContext *context) {
  self->onCancel(*context);
}
