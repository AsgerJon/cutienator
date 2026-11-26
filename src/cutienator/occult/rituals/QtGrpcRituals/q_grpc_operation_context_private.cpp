//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcoperationcontext_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/qgrpcoperationcontext.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcoperationcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/qgrpccalloptions.h>

//  QGrpcOperationContext *QGrpcOperationContextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGrpcOperationContext *ritual_ZN28QGrpcOperationContextPrivate6q_funcEv(
    QGrpcOperationContextPrivate *self) {
  return self->q_func();
}

//  const QGrpcOperationContext *QGrpcOperationContextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGrpcOperationContext *ritual_ZNK28QGrpcOperationContextPrivate6q_funcEv(
    const QGrpcOperationContextPrivate *self) {
  return self->q_func();
}

//  QGrpcOperationContextPrivate::QGrpcOperationContextPrivate(QtGrpc::RpcDes
//      criptor &&descriptor_, QGrpcCallOptions options_,
//      std::shared_ptr<QAbstractProtobufSerializer> &&serializer_, quint64
//      operationId_)
extern "C" Q_DECL_EXPORT
QGrpcOperationContextPrivate *ritual_ZN28QGrpcOperationContextPrivateC1EON6QtGrpc13RpcDescriptorE16QGrpcCallOptionsOSt10shared_ptrI27QAbstractProtobufSerializerEy(
    QtGrpc::RpcDescriptor *descriptor_,
    const QGrpcCallOptions *options_,
    std::shared_ptr<QAbstractProtobufSerializer> *serializer_,
    quint64 operationId_) {
  return new QGrpcOperationContextPrivate(
      std::move(*descriptor_),
      *options_,
      std::move(*serializer_),
      operationId_);
}
