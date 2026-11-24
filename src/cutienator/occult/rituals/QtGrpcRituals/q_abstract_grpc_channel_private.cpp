//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qabstractgrpcchannel_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qabstractgrpcchannel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/qgrpcchanneloptions.h>

//  QAbstractGrpcChannelPrivate::QAbstractGrpcChannelPrivate(const
//      QGrpcChannelOptions &options, QAbstractGrpcChannel *parent)
extern "C" Q_DECL_EXPORT
QAbstractGrpcChannelPrivate *ritual_ZN27QAbstractGrpcChannelPrivateC1ERK19QGrpcChannelOptionsP20QAbstractGrpcChannel(
    const QGrpcChannelOptions *options,
    QAbstractGrpcChannel *parent) {
  return new QAbstractGrpcChannelPrivate(*options, parent);
}

//  const QAbstractGrpcChannelPrivate *QAbstractGrpcChannelPrivate::get(const
//      QAbstractGrpcChannel *ch)
extern "C" Q_DECL_EXPORT
const QAbstractGrpcChannelPrivate *ritual_ZN27QAbstractGrpcChannelPrivate3getEPK20QAbstractGrpcChannel(
    const QAbstractGrpcChannel *ch) {
  return QAbstractGrpcChannelPrivate::get(ch);
}

//  QAbstractGrpcChannelPrivate
//      *QAbstractGrpcChannelPrivate::get(QAbstractGrpcChannel *ch)
extern "C" Q_DECL_EXPORT
QAbstractGrpcChannelPrivate *ritual_ZN27QAbstractGrpcChannelPrivate3getEP20QAbstractGrpcChannel(
    QAbstractGrpcChannel *ch) {
  return QAbstractGrpcChannelPrivate::get(ch);
}
