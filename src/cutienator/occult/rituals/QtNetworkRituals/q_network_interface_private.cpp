//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if !defined(QT_NO_NETWORKINTERFACE)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/private/qhostaddress_p.h>
#include <QtCore/private/qipaddress_p.h>
#include <QtCore/qdebug.h>
#if defined(Q_OS_WIN)
# include <winsock2.h>
# include <ws2tcpip.h>
#else
# include <netinet/in.h>
#endif
#include "qplatformdefs.h"
#include <QtCore/qstringlist.h>
#include <QtCore/qendian.h>
#ifndef QT_NO_DATASTREAM
#include <QtCore/qdatastream.h>
#endif
#ifdef __SSE2__
#  include <QtCore/private/qsimd_p.h>
#endif
#ifdef QT_LINUXBASE
#  include <arpa/inet.h>
#endif
#include <QtNetwork/qnetworkinterface.h>
#include <QtNetwork/private/qnetworkinterface_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qhostaddress.cpp, line 143, as _ZNK19QHostAddressPrivate8classifyEv
inline AddressClassification QHostAddressPrivate::classify() const
{
    if (a) {
        // This is an IPv4 address or an IPv6 v4-mapped address includes all
        // IPv6 v4-compat addresses, except for ::ffff:0.0.0.0 (because `a' is
        // zero). See setAddress(quint8*) below, which calls convertToIpv4(),
        // for details.
        // Source: RFC 5735
        if ((a & 0xff000000U) == 0x7f000000U)   // 127.0.0.0/8
            return LoopbackAddress;
        if ((a & 0xf0000000U) == 0xe0000000U)   // 224.0.0.0/4
            return MulticastAddress;
        if ((a & 0xffff0000U) == 0xa9fe0000U)   // 169.254.0.0/16
            return LinkLocalAddress;
        if ((a & 0xff000000U) == 0)             // 0.0.0.0/8 except 0.0.0.0 (handled below)
            return LocalNetAddress;
        if ((a & 0xf0000000U) == 0xf0000000U) { // 240.0.0.0/4
            if (a == 0xffffffffU)               // 255.255.255.255
                return BroadcastAddress;
            return UnknownAddress;
        }
        if (((a & 0xff000000U) == 0x0a000000U)      // 10.0.0.0/8
            || ((a & 0xfff00000U) == 0xac100000U)   // 172.16.0.0/12
            || ((a & 0xffff0000U) == 0xc0a80000U))  // 192.168.0.0/16
            return PrivateNetworkAddress;

        // Not testing for TestNetworkAddress
        // since we don't need them yet.
        return GlobalAddress;
    }

    // As `a' is zero, this address is either ::ffff:0.0.0.0 or a non-v4-mapped IPv6 address.
    // Source: https://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xhtml
    if (a6_64.c[0]) {
        quint32 high16 = qFromBigEndian(a6_32.c[0]) >> 16;
        switch (high16 >> 8) {
        case 0xff:                          // ff00::/8
            return MulticastAddress;
        case 0xfe:
            switch (high16 & 0xffc0) {
            case 0xfec0:                    // fec0::/10
                return SiteLocalAddress;

            case 0xfe80:                    // fe80::/10
                return LinkLocalAddress;

            default:                        // fe00::/9
                return UnknownAddress;
            }
        case 0xfd:                          // fc00::/7
        case 0xfc:
            return UniqueLocalAddress;
        default:
            return GlobalAddress;
        }
    }

    quint64 low64 = qFromBigEndian(a6_64.c[1]);
    if (low64 == 1)                             // ::1
        return LoopbackAddress;
    if (low64 >> 32 == 0xffff) {                // ::ffff:0.0.0.0/96
        Q_ASSERT(quint32(low64) == 0);
        return LocalNetAddress;
    }
    if (low64)                                  // not ::
        return GlobalAddress;

    if (protocol == QHostAddress::UnknownNetworkLayerProtocol)
        return UnknownAddress;

    // only :: and 0.0.0.0 remain now
    return LocalNetAddress;
}

//  from src/network/kernel/qnetworkinterface.cpp, line 103, as _ZN24QNetworkInterfacePrivate13makeHwAddressEiPh
#if !defined(QT_NO_NETWORKINTERFACE)
inline QString QNetworkInterfacePrivate::makeHwAddress(int len, uchar *data)
{
    const int outLen = qMax(len * 2 + (len - 1) * 1, 0);
    QString result(outLen, Qt::Uninitialized);
    QChar *out = result.data();
    for (int i = 0; i < len; ++i) {
        if (i)
            *out++ = u':';
        *out++ = QLatin1Char(QtMiscUtils::toHexUpper(data[i] / 16));
        *out++ = QLatin1Char(QtMiscUtils::toHexUpper(data[i] % 16));
    }
    return result;
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
//  -----------------------------------------------------------------------

//  QNetworkInterfacePrivate::QNetworkInterfacePrivate()
extern "C" Q_DECL_EXPORT
QNetworkInterfacePrivate *ritual_ZN24QNetworkInterfacePrivateC1Ev() {
  return new QNetworkInterfacePrivate();
}

//  QNetworkInterfacePrivate::~QNetworkInterfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkInterfacePrivateD1Ev(
    QNetworkInterfacePrivate *self) {
  delete self;
}

#if !defined(QT_NO_NETWORKINTERFACE)
//  QString QNetworkInterfacePrivate::makeHwAddress(int len, uchar *data)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QNetworkInterfacePrivate13makeHwAddressEiPh(
    int len,
    uchar *data) {
  return new QString(QNetworkInterfacePrivate::makeHwAddress(len, data));
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)

//  void
//      QNetworkInterfacePrivate::calculateDnsEligibility(QNetworkAddressEntr
//      y *entry, bool isTemporary, bool isDeprecated)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkInterfacePrivate23calculateDnsEligibilityEP20QNetworkAddressEntrybb(
    QNetworkAddressEntry *entry,
    bool isTemporary,
    bool isDeprecated) {
  QNetworkInterfacePrivate::calculateDnsEligibility(
      entry,
      isTemporary,
      isDeprecated);
}

//  QList<QNetworkInterfacePrivate *>::QList()
extern "C" Q_DECL_EXPORT
QList<QNetworkInterfacePrivate *> *ritual_list_make_QNetworkInterfacePrivate_ptr() {
  return new QList<QNetworkInterfacePrivate *>();
}

//  void QList<QNetworkInterfacePrivate *>::append(const
//      QNetworkInterfacePrivate * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNetworkInterfacePrivate_ptr(
    QList<QNetworkInterfacePrivate *> *self,
    QNetworkInterfacePrivate *element) {
  self->append(element);
}

//  qsizetype QList<QNetworkInterfacePrivate *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNetworkInterfacePrivate_ptr(
    const QList<QNetworkInterfacePrivate *> *self) {
  return self->size();
}

//  const QNetworkInterfacePrivate * &QList<QNetworkInterfacePrivate
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNetworkInterfacePrivate *ritual_list_at_QNetworkInterfacePrivate_ptr(
    const QList<QNetworkInterfacePrivate *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QNetworkInterfacePrivate *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNetworkInterfacePrivate_ptr(
    QList<QNetworkInterfacePrivate *> *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKINTERFACE)
