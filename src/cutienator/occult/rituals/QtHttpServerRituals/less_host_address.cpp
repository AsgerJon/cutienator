//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qabstracthttpserver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qabstracthttpserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/private/qabstracthttpserver_p.h>
#include <QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qtcpserver.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl) && QT_CONFIG(http)
#include <QtNetwork/private/qhttp2connection_p.h>
#endif
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalserver.h>
#include <QtNetwork/qlocalsocket.h>
#endif
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslserver.h>
#endif
#if QT_CONFIG(http) && QT_CONFIG(ssl)
#include <QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h>
#endif
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qabstracthttpserver.cpp, line 40, as _ZNK15LessHostAddressclERK12QHostAddressS2_
inline bool LessHostAddress::operator()(const QHostAddress &lhs, const QHostAddress &rhs) const
{
    bool lhsIsIPv4 = false;
    bool rhsIsIPv4 = false;
    quint32 lhsIpAddressV4 = lhs.toIPv4Address(&lhsIsIPv4);
    quint32 rhsIpAddressV4 = rhs.toIPv4Address(&rhsIsIPv4);
    if (lhsIsIPv4 != rhsIsIPv4)
        return lhsIsIPv4;
    if (lhsIsIPv4)
        return lhsIpAddressV4 < rhsIpAddressV4;

    Q_IPV6ADDR lhsIpAddressV6 = lhs.toIPv6Address();
    Q_IPV6ADDR rhsIpAddressV6 = rhs.toIPv6Address();
    for (int i = 0; i < 16; ++i) {
        if (lhsIpAddressV6[i] != rhsIpAddressV6[i])
            return lhsIpAddressV6[i] < rhsIpAddressV6[i];
    }

    return false;
}
//  -----------------------------------------------------------------------

//  bool LessHostAddress::operator()(const QHostAddress &lhs, const
//      QHostAddress &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15LessHostAddressclERK12QHostAddressS2_(
    const LessHostAddress *self,
    const QHostAddress *lhs,
    const QHostAddress *rhs) {
  return self->operator()(*lhs, *rhs);
}

//  LessHostAddress::~LessHostAddress()
extern "C" Q_DECL_EXPORT
void ritual_ZN15LessHostAddressD1Ev(LessHostAddress *self) {
  delete self;
}
