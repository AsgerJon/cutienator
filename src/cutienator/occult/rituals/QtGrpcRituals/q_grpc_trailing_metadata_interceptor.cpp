//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpcinterceptor.h>

//  QGrpcTrailingMetadataInterceptor::~QGrpcTrailingMetadataInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGrpcTrailingMetadataInterceptorD1Ev(
    QGrpcTrailingMetadataInterceptor *self) {
  delete self;
}

//  void QGrpcTrailingMetadataInterceptor::onTrailingMetadata(QGrpcIntercepti
//      onContext &context, QMultiHash<QByteArray, QByteArray> &metadata)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QGrpcTrailingMetadataInterceptor18onTrailingMetadataER24QGrpcInterceptionContextR10QMultiHashI10QByteArrayS3_E(
    QGrpcTrailingMetadataInterceptor *self,
    QGrpcInterceptionContext *context,
    QMultiHash<QByteArray, QByteArray> *metadata) {
  self->onTrailingMetadata(*context, *metadata);
}
