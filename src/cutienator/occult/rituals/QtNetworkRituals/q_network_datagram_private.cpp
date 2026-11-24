//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhostaddress.h>

//  QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray &data,
//      const QHostAddress &dstAddr, quint16 port)
extern "C" Q_DECL_EXPORT
QNetworkDatagramPrivate *ritual_ZN23QNetworkDatagramPrivateC1ERK10QByteArrayRK12QHostAddresst(
    const QByteArray *data,
    const QHostAddress *dstAddr,
    quint16 port) {
  return new QNetworkDatagramPrivate(*data, *dstAddr, port);
}

//  QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray &data,
//      const QIpPacketHeader &header)
extern "C" Q_DECL_EXPORT
QNetworkDatagramPrivate *ritual_ZN23QNetworkDatagramPrivateC1ERK10QByteArrayRK15QIpPacketHeader(
    const QByteArray *data,
    const QIpPacketHeader *header) {
  return new QNetworkDatagramPrivate(*data, *header);
}

//  QNetworkDatagramPrivate::~QNetworkDatagramPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNetworkDatagramPrivateD1Ev(QNetworkDatagramPrivate *self) {
  delete self;
}
