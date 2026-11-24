//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qgrpchttp2channel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qgrpchttp2channel.h>
#include <QtCore/qurl.h>
#include <QtGrpc/qgrpcchanneloptions.h>

//  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri)
extern "C" Q_DECL_EXPORT
QGrpcHttp2Channel *ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrl(
    const QUrl *hostUri) {
  return new QGrpcHttp2Channel(*hostUri);
}

//  QGrpcHttp2Channel::QGrpcHttp2Channel(const QUrl &hostUri, const
//      QGrpcChannelOptions &options)
extern "C" Q_DECL_EXPORT
QGrpcHttp2Channel *ritual_ZN17QGrpcHttp2ChannelC1ERK4QUrlRK19QGrpcChannelOptions(
    const QUrl *hostUri,
    const QGrpcChannelOptions *options) {
  return new QGrpcHttp2Channel(*hostUri, *options);
}

//  QGrpcHttp2Channel::~QGrpcHttp2Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGrpcHttp2ChannelD1Ev(QGrpcHttp2Channel *self) {
  delete self;
}

//  QUrl QGrpcHttp2Channel::hostUri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QGrpcHttp2Channel7hostUriEv(
    const QGrpcHttp2Channel *self) {
  return new QUrl(self->hostUri());
}
