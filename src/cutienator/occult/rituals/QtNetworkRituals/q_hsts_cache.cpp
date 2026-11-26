//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhstsstore_p.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <utility>
#include <QtNetwork/private/qhsts_p.h>
#include <QtNetwork/qhttpheaders.h>
#include "QtCore/private/qipaddress_p.h"
#include "QtCore/qlist.h"
#if QT_CONFIG(settings)
#include <QtNetwork/private/qhstsstore_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhsts.cpp, line 18, as local:qhsts.cpp:is_valid_domain_name
static bool is_valid_domain_name(const QString &host)
{
    if (!host.size())
        return false;

    // RFC6797 8.1.1
    // If the substring matching the host production from the Request-URI
    // (of the message to which the host responded) syntactically matches
    //the IP-literal or IPv4address productions from Section 3.2.2 of
    //[RFC3986], then the UA MUST NOT note this host as a Known HSTS Host.
    using namespace QIPAddressUtils;

    IPv4Address ipv4Addr = {};
    if (parseIp4(ipv4Addr, host.constBegin(), host.constEnd()))
        return false;

    IPv6Address ipv6Addr = {};
    // Unlike parseIp4, parseIp6 returns nullptr if it managed to parse IPv6
    // address successfully.
    if (!parseIp6(ipv6Addr, host.constBegin(), host.constEnd()))
        return false;

    // TODO: for now we do not test IPvFuture address, it must be addressed
    // by introducing parseIpFuture (actually, there is an implementation
    // in QUrl that can be adopted/modified/moved to QIPAddressUtils).
    return true;
}

//  from src/network/access/qhstsstore.cpp, line 72, as _ZN10QHstsStore13addToObservedERK11QHstsPolicy
inline void QHstsStore::addToObserved(const QHstsPolicy &policy)
{
    observedPolicies.push_back(policy);
}

//  from src/network/access/qhsts.cpp, line 135, as _ZNK10QHstsCache11isKnownHostERK4QUrl
inline bool QHstsCache::isKnownHost(const QUrl &url) const
{
    if (!url.isValid() || !is_valid_domain_name(url.host()))
        return false;

    /*
        RFC6797, 8.2.  Known HSTS Host Domain Name Matching

        * Superdomain Match
          If a label-for-label match between an entire Known HSTS Host's
          domain name and a right-hand portion of the given domain name
          is found, then this Known HSTS Host's domain name is a
          superdomain match for the given domain name.  There could be
          multiple superdomain matches for a given domain name.
        * Congruent Match
          If a label-for-label match between a Known HSTS Host's domain
          name and the given domain name is found -- i.e., there are no
          further labels to compare -- then the given domain name
          congruently matches this Known HSTS Host.

        We start from the congruent match, and then chop labels and dots and
        proceed with superdomain match. While RFC6797 recommends to start from
        superdomain, the result is the same - some valid policy will make a host
        known.
    */

    bool superDomainMatch = false;
    const QString hostNameAsString(url.host());
    HostName nameToTest(QStringView{hostNameAsString});
    while (nameToTest.fragment.size()) {
        auto const pos = knownHosts.find(nameToTest);
        if (pos != knownHosts.end()) {
            if (pos->second.isExpired()) {
                knownHosts.erase(pos);
#if QT_CONFIG(settings)
                if (hstsStore) {
                    // Inform our store that this policy has expired.
                    hstsStore->addToObserved(pos->second);
                }
#endif // QT_CONFIG(settings)
            } else if (!superDomainMatch || pos->second.includesSubDomains()) {
                return true;
            }
        }

        const qsizetype dot = nameToTest.fragment.indexOf(u'.');
        if (dot == -1)
            break;

        nameToTest.fragment = nameToTest.fragment.mid(dot + 1);
        superDomainMatch = true;
    }

    return false;
}

//  from src/network/access/qhsts.cpp, line 191, as _ZN10QHstsCache5clearEv
inline void QHstsCache::clear()
{
    knownHosts.clear();
}

//  from src/network/access/qhsts.cpp, line 196, as _ZNK10QHstsCache8policiesEv
inline QList<QHstsPolicy> QHstsCache::policies() const
{
    QList<QHstsPolicy> values;
    values.reserve(int(knownHosts.size()));
    for (const auto &host : knownHosts)
        values << host.second;
    return values;
}
//  -----------------------------------------------------------------------

//  bool QHstsCache::isKnownHost(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QHstsCache11isKnownHostERK4QUrl(
    const QHstsCache *self,
    const QUrl *url) {
  return self->isKnownHost(*url);
}

//  void QHstsCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsCache5clearEv(QHstsCache *self) {
  self->clear();
}

//  QList<QHstsPolicy> QHstsCache::policies() const
extern "C" Q_DECL_EXPORT
QList<QHstsPolicy> *ritual_ZNK10QHstsCache8policiesEv(
    const QHstsCache *self) {
  return new QList<QHstsPolicy>(self->policies());
}

//  QHstsCache::~QHstsCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHstsCacheD1Ev(QHstsCache *self) {
  delete self;
}
