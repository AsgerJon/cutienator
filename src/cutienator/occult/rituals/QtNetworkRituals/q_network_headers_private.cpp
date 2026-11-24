//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkrequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include "qplatformdefs.h"
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qhttpheadershelper_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttp1configuration.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtNetwork/private/http2protocol_p.h>
#endif
#include "QtCore/qdatetime.h"
#include "QtCore/qlocale.h"
#include "QtCore/qshareddata.h"
#include "QtCore/qtimezone.h"
#include "QtCore/private/qduplicatetracker_p.h"
#include "QtCore/private/qtools_p.h"
#if QT_CONFIG(datestring)
# include <stdio.h>
#endif
#include <algorithm>
#include <QtCore/q20algorithm.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkrequest.cpp, line 1588, as _ZNK22QNetworkHeadersPrivate14rawHeadersKeysEv
inline QList<QByteArray> QNetworkHeadersPrivate::rawHeadersKeys() const
{
    if (httpHeaders.isEmpty())
        return {};

    QList<QByteArray> result;
    result.reserve(httpHeaders.size());
    QDuplicateTracker<QByteArray> seen(httpHeaders.size());

    for (qsizetype i = 0; i < httpHeaders.size(); i++) {
        const auto nameL1 = httpHeaders.nameAt(i);
        const auto name = QByteArray(nameL1.data(), nameL1.size());
        if (seen.hasSeen(name))
            continue;

        result << name;
    }

    return result;
}

//  from src/network/access/qnetworkrequest.cpp, line 1609, as _ZNK22QNetworkHeadersPrivate9rawHeaderE14QAnyStringView
inline QByteArray QNetworkHeadersPrivate::rawHeader(QAnyStringView headerName) const
{
    QByteArrayView setCookieStr = QHttpHeaders::wellKnownHeaderName(
            QHttpHeaders::WellKnownHeader::SetCookie);
    if (QAnyStringView::compare(headerName, setCookieStr, Qt::CaseInsensitive) != 0)
        return httpHeaders.combinedValue(headerName);

    QByteArray result;
    const char* separator = "";
    for (qsizetype i = 0; i < httpHeaders.size(); ++i) {
        if (QAnyStringView::compare(httpHeaders.nameAt(i), headerName, Qt::CaseInsensitive) == 0) {
            result.append(separator);
            result.append(httpHeaders.valueAt(i));
            separator = "\n";
        }
    }
    return result;
}

//  from src/network/access/qnetworkrequest.cpp, line 1669, as _ZNK22QNetworkHeadersPrivate7headersEv
inline QHttpHeaders QNetworkHeadersPrivate::headers() const
{
    return httpHeaders;
}

//  from src/network/access/qnetworkrequest.cpp, line 1700, as _ZN22QNetworkHeadersPrivate12clearHeadersEv
inline void QNetworkHeadersPrivate::clearHeaders()
{
    httpHeaders.clear();
    cookedHeaders.clear();
    invalidateHeaderCache();
}

//  from src/network/access/qnetworkrequest.cpp, line 1826, as _ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime
inline QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
{
    return QLocale::c().toString(dt.toUTC(), u"ddd, dd MMM yyyy hh:mm:ss 'GMT'").toLatin1();
}

//  from src/network/access/qnetworkrequest.cpp, line 1932, as _ZN22QNetworkHeadersPrivate21invalidateHeaderCacheEv
inline void QNetworkHeadersPrivate::invalidateHeaderCache()
{
    rawHeaderCache.headersList.clear();
    rawHeaderCache.isCached = false;
}
//  -----------------------------------------------------------------------

//  QList<QByteArray> QNetworkHeadersPrivate::rawHeadersKeys() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK22QNetworkHeadersPrivate14rawHeadersKeysEv(
    const QNetworkHeadersPrivate *self) {
  return new QList<QByteArray>(self->rawHeadersKeys());
}

//  QByteArray QNetworkHeadersPrivate::rawHeader(QAnyStringView headerName)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QNetworkHeadersPrivate9rawHeaderE14QAnyStringView(
    const QNetworkHeadersPrivate *self,
    const QString *headerName) {
  return new QByteArray(self->rawHeader(QAnyStringView(*headerName)));
}

//  QHttpHeaders QNetworkHeadersPrivate::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK22QNetworkHeadersPrivate7headersEv(
    const QNetworkHeadersPrivate *self) {
  return new QHttpHeaders(self->headers());
}

//  void QNetworkHeadersPrivate::clearHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkHeadersPrivate12clearHeadersEv(
    QNetworkHeadersPrivate *self) {
  self->clearHeaders();
}

//  QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime(
    const QDateTime *dt) {
  return new QByteArray(QNetworkHeadersPrivate::toHttpDate(*dt));
}

//  void QNetworkHeadersPrivate::invalidateHeaderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkHeadersPrivate21invalidateHeaderCacheEv(
    QNetworkHeadersPrivate *self) {
  self->invalidateHeaderCache();
}

//  QNetworkHeadersPrivate::~QNetworkHeadersPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QNetworkHeadersPrivateD1Ev(QNetworkHeadersPrivate *self) {
  delete self;
}
