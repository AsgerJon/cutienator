//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequestfilter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequestfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qhttpserverconfiguration.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/QHash>
#include <QtNetwork/QHostAddress>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverrequestfilter_p.h>
#include <QtCore/qdatetime.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverrequestfilter.cpp, line 16, as local:qhttpserverrequestfilter.cpp:cCleanupThreshold
static constexpr int cCleanupThreshold = 10;

//  from ../qthttpserver/src/httpserver/qhttpserverrequestfilter.cpp, line 146, as _ZNK24QHttpServerRequestFilter6IpInfo9isGarbageEx
inline bool QHttpServerRequestFilter::IpInfo::isGarbage(qint64 currTime) const
{
    // ip info is garbage if we got no requests during next period
    return (currTime >= m_thisPeriodEnd + QHttpServerRequestFilterPrivate::cPeriodDurationMSec);
}

//  from ../qthttpserver/src/httpserver/qhttpserverrequestfilter.cpp, line 124, as _ZN24QHttpServerRequestFilter18cleanIpInfoGarbageEN5QHashI12QHostAddressNS_6IpInfoEE8iteratorEx
inline void QHttpServerRequestFilter::cleanIpInfoGarbage(QHash<QHostAddress, IpInfo>::iterator it,
                                                  qint64 currTime)
{
    Q_ASSERT(ipInfo.begin() != ipInfo.end());

    const auto myIp = it.key();
    ++it;
    // check the range after the current ip
    for (int i = 0; i < cCleanupThreshold; ++i) {
        if (it == ipInfo.end())
            it = ipInfo.begin();

        if (it.key() == myIp)
            break;

        if (it->isGarbage(currTime))
            it = ipInfo.erase(it);
        else
            ++it;
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverrequestfilter.cpp, line 18, as _ZNK24QHttpServerRequestFilter19maxRequestPerPeriodEv
inline unsigned int QHttpServerRequestFilter::maxRequestPerPeriod() const
{
    return m_config.rateLimitPerSecond();
}
//  -----------------------------------------------------------------------

//  void QHttpServerRequestFilter::setConfiguration(const
//      QHttpServerConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerRequestFilter16setConfigurationERK24QHttpServerConfiguration(
    QHttpServerRequestFilter *self,
    const QHttpServerConfiguration *config) {
  self->setConfiguration(*config);
}

//  bool QHttpServerRequestFilter::isRequestAllowed(const QHostAddress
//      &peerAddress) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter16isRequestAllowedERK12QHostAddress(
    const QHttpServerRequestFilter *self,
    const QHostAddress *peerAddress) {
  return self->isRequestAllowed(*peerAddress);
}

//  bool QHttpServerRequestFilter::isRequestWithinRate(const QHostAddress
//      &peerAddress)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpServerRequestFilter19isRequestWithinRateERK12QHostAddress(
    QHttpServerRequestFilter *self,
    const QHostAddress *peerAddress) {
  return self->isRequestWithinRate(*peerAddress);
}

//  bool QHttpServerRequestFilter::isRequestWithinRate(const QHostAddress
//      &peerAddress, qint64 currTimeMSec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QHttpServerRequestFilter19isRequestWithinRateERK12QHostAddressx(
    QHttpServerRequestFilter *self,
    const QHostAddress *peerAddress,
    qint64 currTimeMSec) {
  return self->isRequestWithinRate(*peerAddress, currTimeMSec);
}

//  bool QHttpServerRequestFilter::isUrlSizeAllowed(qsizetype urlSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter16isUrlSizeAllowedEx(
    const QHttpServerRequestFilter *self,
    qsizetype urlSize) {
  return self->isUrlSizeAllowed(urlSize);
}

//  bool QHttpServerRequestFilter::isTotalHeaderSizeAllowed(qsizetype
//      headerSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter24isTotalHeaderSizeAllowedEx(
    const QHttpServerRequestFilter *self,
    qsizetype headerSize) {
  return self->isTotalHeaderSizeAllowed(headerSize);
}

//  bool QHttpServerRequestFilter::isHeaderFieldSizeAllowed(qsizetype
//      headerSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter24isHeaderFieldSizeAllowedEx(
    const QHttpServerRequestFilter *self,
    qsizetype headerSize) {
  return self->isHeaderFieldSizeAllowed(headerSize);
}

//  bool QHttpServerRequestFilter::isNumberOfHeaderFieldsAllowed(qsizetype
//      headerSize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter29isNumberOfHeaderFieldsAllowedEx(
    const QHttpServerRequestFilter *self,
    qsizetype headerSize) {
  return self->isNumberOfHeaderFieldsAllowed(headerSize);
}

//  bool QHttpServerRequestFilter::isBodySizeAllowed(qint64 bodySize) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QHttpServerRequestFilter17isBodySizeAllowedEx(
    const QHttpServerRequestFilter *self,
    qint64 bodySize) {
  return self->isBodySizeAllowed(bodySize);
}

//  void QHttpServerRequestFilter::cleanIpInfoGarbage(QHash<QHostAddress,
//      IpInfo>::iterator it, qint64 currTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerRequestFilter18cleanIpInfoGarbageEN5QHashI12QHostAddressNS_6IpInfoEE8iteratorEx(
    QHttpServerRequestFilter *self,
    const QHash<QHostAddress, QHttpServerRequestFilter::IpInfo>::iterator *it,
    qint64 currTime) {
  self->cleanIpInfoGarbage(*it, currTime);
}

//  unsigned int QHttpServerRequestFilter::maxRequestPerPeriod() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK24QHttpServerRequestFilter19maxRequestPerPeriodEv(
    const QHttpServerRequestFilter *self) {
  return self->maxRequestPerPeriod();
}

//  QHttpServerRequestFilter::~QHttpServerRequestFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerRequestFilterD1Ev(
    QHttpServerRequestFilter *self) {
  delete self;
}
