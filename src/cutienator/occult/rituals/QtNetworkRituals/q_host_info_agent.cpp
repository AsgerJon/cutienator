//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostinfo.h>
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostinfo.h>
#include <QtNetwork/private/qhostinfo_p.h>
#include <qplatformdefs.h>
#include "QtCore/qapplicationstatic.h"
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/qurl.h>
#include <QtCore/private/qobject_p.h>
#include <algorithm>
#ifdef Q_OS_UNIX
#  include <unistd.h>
#  include <netdb.h>
#  include <netinet/in.h>
#elif defined Q_OS_WIN
#  include <ws2tcpip.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qhostinfo.cpp, line 395, as _ZN14QHostInfoAgent6lookupERK7QString
#if defined(Q_OS_LINUX)
inline QHostInfo QHostInfoAgent::lookup(const QString &hostName)
{
    QHostInfo results;

    // IDN support
    QByteArray aceHostname = QUrl::toAce(hostName);
    results.setHostName(hostName);
    if (aceHostname.isEmpty()) {
        results.setError(QHostInfo::HostNotFound);
        results.setErrorString(hostName.isEmpty() ?
                               QCoreApplication::translate("QHostInfoAgent", "No host name given") :
                               QCoreApplication::translate("QHostInfoAgent", "Invalid hostname"));
        return results;
    }

    addrinfo *res = nullptr;
    struct addrinfo hints;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = PF_UNSPEC;
#ifdef Q_ADDRCONFIG
    hints.ai_flags = Q_ADDRCONFIG;
#endif

    int result = getaddrinfo(aceHostname.constData(), nullptr, &hints, &res);
# ifdef Q_ADDRCONFIG
    if (result == EAI_BADFLAGS) {
        // if the lookup failed with AI_ADDRCONFIG set, try again without it
        hints.ai_flags = 0;
        result = getaddrinfo(aceHostname.constData(), nullptr, &hints, &res);
    }
# endif

    if (result == 0) {
        addrinfo *node = res;
        QList<QHostAddress> addresses;
        while (node) {
#ifdef QHOSTINFO_DEBUG
            qDebug() << "getaddrinfo node: flags:" << node->ai_flags << "family:" << node->ai_family
                     << "ai_socktype:" << node->ai_socktype << "ai_protocol:" << node->ai_protocol
                     << "ai_addrlen:" << node->ai_addrlen;
#endif
            switch (node->ai_family) {
            case AF_INET: {
                QHostAddress addr;
                addr.setAddress(ntohl(((sockaddr_in *) node->ai_addr)->sin_addr.s_addr));
                if (!addresses.contains(addr))
                    addresses.append(addr);
                break;
            }
            case AF_INET6: {
                QHostAddress addr;
                sockaddr_in6 *sa6 = (sockaddr_in6 *) node->ai_addr;
                addr.setAddress(sa6->sin6_addr.s6_addr);
                if (sa6->sin6_scope_id)
                    addr.setScopeId(QString::number(sa6->sin6_scope_id));
                if (!addresses.contains(addr))
                    addresses.append(addr);
                break;
            }
            default:
                results.setError(QHostInfo::UnknownError);
                results.setErrorString(QCoreApplication::translate("QHostInfoAgent", "Unknown address type"));
            }
            node = node->ai_next;
        }
        if (addresses.isEmpty()) {
            // Reached the end of the list, but no addresses were found; this
            // means the list contains one or more unknown address types.
            results.setError(QHostInfo::UnknownError);
            results.setErrorString(QCoreApplication::translate("QHostInfoAgent", "Unknown address type"));
        }

        results.setAddresses(addresses);
        freeaddrinfo(res);
    } else {
        switch (result) {
#ifdef Q_OS_WIN
        case WSAHOST_NOT_FOUND: //authoritative not found
        case WSATRY_AGAIN: //non authoritative not found
        case WSANO_DATA: //valid name, no associated address
#else
        case EAI_NONAME:
        case EAI_FAIL:
#  ifdef EAI_NODATA // EAI_NODATA is deprecated in RFC 3493
        case EAI_NODATA:
#  endif
#endif
            results.setError(QHostInfo::HostNotFound);
            results.setErrorString(QCoreApplication::translate("QHostInfoAgent", "Host not found"));
            break;
        default:
            results.setError(QHostInfo::UnknownError);
#ifdef Q_OS_WIN
            results.setErrorString(QString::fromWCharArray(gai_strerror(result)));
#else
            results.setErrorString(QString::fromLocal8Bit(gai_strerror(result)));
#endif
            break;
        }
    }

#if defined(QHOSTINFO_DEBUG)
    if (results.error() != QHostInfo::NoError) {
        qDebug("QHostInfoAgent::fromName(): error #%d %s",
               h_errno, results.errorString().toLatin1().constData());
    } else {
        QString tmp;
        QList<QHostAddress> addresses = results.addresses();
        for (int i = 0; i < addresses.count(); ++i) {
            if (i != 0) tmp += ", "_L1;
            tmp += addresses.at(i).toString();
        }
        qDebug("QHostInfoAgent::fromName(): found %i entries for \"%s\": {%s}",
               addresses.count(), aceHostname.constData(),
               tmp.toLatin1().constData());
    }
#endif

    return results;
}
#endif  // defined(Q_OS_LINUX)

//  from src/network/kernel/qhostinfo.cpp, line 359, as _ZN14QHostInfoAgent13reverseLookupERK12QHostAddress
inline QHostInfo QHostInfoAgent::reverseLookup(const QHostAddress &address)
{
    QHostInfo results;
    // Reverse lookup
    sockaddr_in sa4;
    sockaddr_in6 sa6;
    sockaddr *sa = nullptr;
    QT_SOCKLEN_T saSize;
    if (address.protocol() == QHostAddress::IPv4Protocol) {
        sa = reinterpret_cast<sockaddr *>(&sa4);
        saSize = sizeof(sa4);
        memset(&sa4, 0, sizeof(sa4));
        sa4.sin_family = AF_INET;
        sa4.sin_addr.s_addr = htonl(address.toIPv4Address());
    } else {
        sa = reinterpret_cast<sockaddr *>(&sa6);
        saSize = sizeof(sa6);
        memset(&sa6, 0, sizeof(sa6));
        sa6.sin6_family = AF_INET6;
        memcpy(&sa6.sin6_addr, address.toIPv6Address().c, sizeof(sa6.sin6_addr));
    }

    char hbuf[NI_MAXHOST];
    if (sa && getnameinfo(sa, saSize, hbuf, sizeof(hbuf), nullptr, 0, 0) == 0)
        results.setHostName(QString::fromLatin1(hbuf));

    if (results.hostName().isEmpty())
        results.setHostName(address.toString());
    results.setAddresses(QList<QHostAddress>() << address);

    return results;
}
//  -----------------------------------------------------------------------

#if defined(Q_OS_LINUX)
//  QHostInfo QHostInfoAgent::lookup(const QString &hostName)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN14QHostInfoAgent6lookupERK7QString(
    const QString *hostName) {
  return new QHostInfo(QHostInfoAgent::lookup(*hostName));
}
#endif  // defined(Q_OS_LINUX)

//  QHostInfo QHostInfoAgent::reverseLookup(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
QHostInfo *ritual_ZN14QHostInfoAgent13reverseLookupERK12QHostAddress(
    const QHostAddress *address) {
  return new QHostInfo(QHostInfoAgent::reverseLookup(*address));
}

//  QHostInfoAgent::~QHostInfoAgent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHostInfoAgentD1Ev(QHostInfoAgent *self) {
  delete self;
}
