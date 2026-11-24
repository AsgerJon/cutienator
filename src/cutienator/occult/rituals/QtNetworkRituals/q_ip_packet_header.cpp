//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>

//  QIpPacketHeader::QIpPacketHeader(const QHostAddress &dstAddr, quint16
//      port)
extern "C" Q_DECL_EXPORT
QIpPacketHeader *ritual_ZN15QIpPacketHeaderC1ERK12QHostAddresst(
    const QHostAddress *dstAddr,
    quint16 port) {
  return new QIpPacketHeader(*dstAddr, port);
}

//  void QIpPacketHeader::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QIpPacketHeader5clearEv(QIpPacketHeader *self) {
  self->clear();
}

//  QIpPacketHeader::~QIpPacketHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QIpPacketHeaderD1Ev(QIpPacketHeader *self) {
  delete self;
}
