//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qabstractgrpcchannel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qabstractgrpcchannel.h>
#include <QtGrpc/qgrpcchanneloptions.h>

//  QAbstractGrpcChannel::~QAbstractGrpcChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannelD1Ev(QAbstractGrpcChannel *self) {
  delete self;
}

//  const QGrpcChannelOptions &QAbstractGrpcChannel::channelOptions() const
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZNKR20QAbstractGrpcChannel14channelOptionsEv(
    const QAbstractGrpcChannel *self) {
  return new QGrpcChannelOptions(self->channelOptions());
}

//  void QAbstractGrpcChannel::setChannelOptions(const QGrpcChannelOptions
//      &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractGrpcChannel17setChannelOptionsERK19QGrpcChannelOptions(
    QAbstractGrpcChannel *self,
    const QGrpcChannelOptions *options) {
  self->setChannelOptions(*options);
}

//  QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func()
extern "C" Q_DECL_EXPORT
QAbstractGrpcChannelPrivate *ritual_ZN20QAbstractGrpcChannel6d_funcEv(
    QAbstractGrpcChannel *self) {
  return self->d_func();
}

//  const QAbstractGrpcChannelPrivate *QAbstractGrpcChannel::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractGrpcChannelPrivate *ritual_ZNK20QAbstractGrpcChannel6d_funcEv(
    const QAbstractGrpcChannel *self) {
  return self->d_func();
}
