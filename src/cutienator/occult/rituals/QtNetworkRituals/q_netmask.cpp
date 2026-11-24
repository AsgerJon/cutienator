//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostaddress_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostaddress_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhostaddress.h"
#include "qhostaddress_p.h"
#include "private/qipaddress_p.h"
#include "qdebug.h"
#if defined(Q_OS_WIN)
# include <winsock2.h>
# include <ws2tcpip.h>
#else
# include <netinet/in.h>
#endif
#include "qplatformdefs.h"
#include "qstringlist.h"
#include "qendian.h"
#ifndef QT_NO_DATASTREAM
#include <qdatastream.h>
#endif
#ifdef __SSE2__
#  include <private/qsimd_p.h>
#endif
#ifdef QT_LINUXBASE
#  include <arpa/inet.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qhostaddress.cpp, line 217, as _ZN8QNetmask10setAddressERK12QHostAddress
inline bool QNetmask::setAddress(const QHostAddress &address)
{
    static const quint8 zeroes[16] = { 0 };
    union {
        quint32 v4;
        quint8 v6[16];
    } ip;

    int netmask = 0;
    quint8 *ptr = ip.v6;
    quint8 *end;
    length = 255;

    if (address.protocol() == QHostAddress::IPv4Protocol) {
        ip.v4 = qToBigEndian(address.toIPv4Address());
        end = ptr + 4;
    } else if (address.protocol() == QHostAddress::IPv6Protocol) {
        memcpy(ip.v6, address.toIPv6Address().c, 16);
        end = ptr + 16;
    } else {
        return false;
    }

    while (ptr < end) {
        switch (*ptr) {
        case 255:
            netmask += 8;
            ++ptr;
            continue;

        default:
            return false;       // invalid IP-style netmask

        case 254:
            ++netmask;
            Q_FALLTHROUGH();
        case 252:
            ++netmask;
            Q_FALLTHROUGH();
        case 248:
            ++netmask;
            Q_FALLTHROUGH();
        case 240:
            ++netmask;
            Q_FALLTHROUGH();
        case 224:
            ++netmask;
            Q_FALLTHROUGH();
        case 192:
            ++netmask;
            Q_FALLTHROUGH();
        case 128:
            ++netmask;
            Q_FALLTHROUGH();
        case 0:
            break;
        }
        break;
    }

    // confirm that the rest is only zeroes
    if (ptr < end && memcmp(ptr + 1, zeroes, end - ptr - 1) != 0)
        return false;

    length = netmask;
    return true;
}
//  -----------------------------------------------------------------------

//  QNetmask::QNetmask()
extern "C" Q_DECL_EXPORT
QNetmask *ritual_ZN8QNetmaskC1Ev() {
  return new QNetmask();
}

//  bool QNetmask::setAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QNetmask10setAddressERK12QHostAddress(
    QNetmask *self,
    const QHostAddress *address) {
  return self->setAddress(*address);
}

//  int QNetmask::prefixLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QNetmask12prefixLengthEv(const QNetmask *self) {
  return self->prefixLength();
}

//  void QNetmask::setPrefixLength(QAbstractSocket::NetworkLayerProtocol
//      proto, int len)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QNetmask15setPrefixLengthEN15QAbstractSocket20NetworkLayerProtocolEi(
    QNetmask *self,
    QAbstractSocket::NetworkLayerProtocol proto,
    int len) {
  self->setPrefixLength(proto, len);
}

//  bool operator==(QNetmask n1, QNetmask n2)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq8QNetmaskS_(const QNetmask *n1, const QNetmask *n2) {
  return operator==(*n1, *n2);
}

//  QNetmask::~QNetmask()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QNetmaskD1Ev(QNetmask *self) {
  delete self;
}
