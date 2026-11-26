//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcInitialMetadataInterceptor::~QGrpcInitialMetadataInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QGrpcInitialMetadataInterceptorD1Ev(
    QGrpcInitialMetadataInterceptor *self) {
  delete self;
}

//  void QGrpcInitialMetadataInterceptor::onInitialMetadata(QGrpcInterception
//      Context &context, QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QGrpcInitialMetadataInterceptor17onInitialMetadataER24QGrpcInterceptionContextR10QMultiHashI10QByteArrayS3_E(
    QGrpcInitialMetadataInterceptor *self,
    QGrpcInterceptionContext *context,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->onInitialMetadata(*context, *metadata);
}
