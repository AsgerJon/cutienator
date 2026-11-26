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
#include <QtCore/qbytearrayview.h>
#include <QtCore/qdatetime.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtCore/qlist.h>
#include <optional>
#include <QtCore/QByteArrayView>
#include <QtCore/QList>
#include <QtCore/QByteArray>
#include <QtNetwork/QHttpHeaders>
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

using namespace Qt::StringLiterals;

//  from src/network/access/qnetworkrequest.cpp, line 1214, as local:qnetworkrequest.cpp:HeaderPair
namespace {
struct HeaderPair {
    QHttpHeaders::WellKnownHeader wellKnownHeader;
    QNetworkRequest::KnownHeaders knownHeader;
};
}  // namespace

//  from src/network/access/qnetworkrequest.cpp, line 1236, as local:qnetworkrequest.cpp:knownHeadersArr
static constexpr HeaderPair knownHeadersArr[] = {
    { QHttpHeaders::WellKnownHeader::ContentDisposition, QNetworkRequest::KnownHeaders::ContentDispositionHeader },
    { QHttpHeaders::WellKnownHeader::ContentLength,      QNetworkRequest::KnownHeaders::ContentLengthHeader },
    { QHttpHeaders::WellKnownHeader::ContentType,        QNetworkRequest::KnownHeaders::ContentTypeHeader },
    { QHttpHeaders::WellKnownHeader::Cookie,             QNetworkRequest::KnownHeaders::CookieHeader },
    { QHttpHeaders::WellKnownHeader::ETag,               QNetworkRequest::KnownHeaders::ETagHeader },
    { QHttpHeaders::WellKnownHeader::IfMatch ,           QNetworkRequest::KnownHeaders::IfMatchHeader },
    { QHttpHeaders::WellKnownHeader::IfModifiedSince,    QNetworkRequest::KnownHeaders::IfModifiedSinceHeader },
    { QHttpHeaders::WellKnownHeader::IfNoneMatch,        QNetworkRequest::KnownHeaders::IfNoneMatchHeader },
    { QHttpHeaders::WellKnownHeader::LastModified,       QNetworkRequest::KnownHeaders::LastModifiedHeader},
    { QHttpHeaders::WellKnownHeader::Location,           QNetworkRequest::KnownHeaders::LocationHeader},
    { QHttpHeaders::WellKnownHeader::Server,             QNetworkRequest::KnownHeaders::ServerHeader },
    { QHttpHeaders::WellKnownHeader::SetCookie,          QNetworkRequest::KnownHeaders::SetCookieHeader },
    { QHttpHeaders::WellKnownHeader::UserAgent,          QNetworkRequest::KnownHeaders::UserAgentHeader }
};

//  from src/network/access/qnetworkrequest.cpp, line 1272, as local:qnetworkrequest.cpp:makeCookieHeader
static QByteArray makeCookieHeader(const QList<QNetworkCookie> &cookies,
                                   QNetworkCookie::RawForm type,
                                   QByteArrayView separator)
{
    QByteArray result;
    for (const QNetworkCookie &cookie : cookies) {
        result += cookie.toRawForm(type);
        result += separator;
    }
    if (!result.isEmpty())
        result.chop(separator.size());
    return result;
}

//  from src/network/access/qnetworkrequest.cpp, line 1341, as local:qnetworkrequest.cpp:parseHeaderName
static int parseHeaderName(QByteArrayView headerName)
{
    if (headerName.isEmpty())
        return -1;

    auto is = [headerName](QByteArrayView what) {
        return headerName.compare(what, Qt::CaseInsensitive) == 0;
    };

    switch (QtMiscUtils::toAsciiLower(headerName.front())) {
    case 'c':
        if (is("content-type"))
            return QNetworkRequest::ContentTypeHeader;
        else if (is("content-length"))
            return QNetworkRequest::ContentLengthHeader;
        else if (is("cookie"))
            return QNetworkRequest::CookieHeader;
        else if (is("content-disposition"))
            return QNetworkRequest::ContentDispositionHeader;
        break;

    case 'e':
        if (is("etag"))
            return QNetworkRequest::ETagHeader;
        break;

    case 'i':
        if (is("if-modified-since"))
            return QNetworkRequest::IfModifiedSinceHeader;
        if (is("if-match"))
            return QNetworkRequest::IfMatchHeader;
        if (is("if-none-match"))
            return QNetworkRequest::IfNoneMatchHeader;
        break;

    case 'l':
        if (is("location"))
            return QNetworkRequest::LocationHeader;
        else if (is("last-modified"))
            return QNetworkRequest::LastModifiedHeader;
        break;

    case 's':
        if (is("set-cookie"))
            return QNetworkRequest::SetCookieHeader;
        else if (is("server"))
            return QNetworkRequest::ServerHeader;
        break;

    case 'u':
        if (is("user-agent"))
            return QNetworkRequest::UserAgentHeader;
        break;
    }

    return -1; // nothing found
}

//  from src/network/access/qnetworkrequest.cpp, line 1399, as local:qnetworkrequest.cpp:parseHttpDate
static QVariant parseHttpDate(QByteArrayView raw)
{
    QDateTime dt = QNetworkHeadersPrivate::fromHttpDate(raw);
    if (dt.isValid())
        return dt;
    return QVariant();          // transform an invalid QDateTime into a null QVariant
}

//  from src/network/access/qnetworkrequest.cpp, line 1407, as local:qnetworkrequest.cpp:parseCookieHeader
static QList<QNetworkCookie> parseCookieHeader(QByteArrayView raw)
{
    QList<QNetworkCookie> result;
    for (auto cookie : QLatin1StringView(raw).tokenize(';'_L1)) {
        QList<QNetworkCookie> parsed = QNetworkCookie::parseCookies(cookie.trimmed());
        if (parsed.size() != 1)
            return {};  // invalid Cookie: header

        result += parsed;
    }

    return result;
}

//  from src/network/access/qnetworkrequest.cpp, line 1421, as local:qnetworkrequest.cpp:parseETag
static QVariant parseETag(QByteArrayView raw)
{
    const QByteArrayView trimmed = raw.trimmed();
    if (!trimmed.startsWith('"') && !trimmed.startsWith(R"(W/")"))
        return QVariant();

    if (!trimmed.endsWith('"'))
        return QVariant();

    return QString::fromLatin1(trimmed);
}

//  from src/network/access/qnetworkrequest.cpp, line 1433, as local:qnetworkrequest.cpp:parseMatchImpl
template<typename T>
static QStringList parseMatchImpl(QByteArrayView raw, T op)
{
    const QByteArrayView trimmedRaw = raw.trimmed();
    if (trimmedRaw == "*")
        return QStringList(QStringLiteral("*"));

    QStringList tags;
    for (auto &element : QLatin1StringView(trimmedRaw).tokenize(','_L1)) {
        if (const auto trimmed = element.trimmed(); op(trimmed))
            tags += QString::fromLatin1(trimmed);
    }
    return tags;
}

//  from src/network/access/qnetworkrequest.cpp, line 1449, as local:qnetworkrequest.cpp:parseIfMatch
static QStringList parseIfMatch(QByteArrayView raw)
{
    return parseMatchImpl(raw, [](QByteArrayView element) {
        return element.startsWith('"') && element.endsWith('"');
    });
}

//  from src/network/access/qnetworkrequest.cpp, line 1549, as local:qnetworkrequest.cpp:isSetCookie
static bool isSetCookie(QByteArrayView name)
{
    return name.compare(QHttpHeaders::wellKnownHeaderName(QHttpHeaders::WellKnownHeader::SetCookie),
                        Qt::CaseInsensitive) == 0;
}

//  from src/network/access/qnetworkrequest.cpp, line 1560, as local:qnetworkrequest.cpp:setFromRawHeader
template<class HeaderName>
static void setFromRawHeader(QHttpHeaders &headers, HeaderName header,
                             QByteArrayView value)
{
    headers.removeAll(header);

    if (value.isNull())
        // only wanted to erase key
        return;

    if (isSetCookie(header)) {
        for (auto cookie : QLatin1StringView(value).tokenize('\n'_L1))
            headers.append(QHttpHeaders::WellKnownHeader::SetCookie, cookie);
    } else {
        headers.append(header, value);
    }
}

//  from src/network/access/qnetworkrequest.cpp, line 1735, as local:qnetworkrequest.cpp:name_to_month
static int name_to_month(const char* month_str)
{
    switch (month_str[0]) {
    case 'J':
        switch (month_str[1]) {
        case 'a':
            return 1;
        case 'u':
            switch (month_str[2] ) {
            case 'n':
                return 6;
            case 'l':
                return 7;
            }
        }
        break;
    case 'F':
        return 2;
    case 'M':
        switch (month_str[2] ) {
        case 'r':
            return 3;
        case 'y':
            return 5;
        }
        break;
    case 'A':
        switch (month_str[1]) {
        case 'p':
            return 4;
        case 'u':
            return 8;
        }
        break;
    case 'O':
        return 10;
    case 'S':
        return 9;
    case 'N':
        return 11;
    case 'D':
        return 12;
    }

    return 0;
}

//  from src/network/access/qnetworkrequest.cpp, line 1578, as _ZNK22QNetworkHeadersPrivate13allRawHeadersEv
inline const QNetworkHeadersPrivate::RawHeadersList &QNetworkHeadersPrivate::allRawHeaders() const
{
    if (rawHeaderCache.isCached)
        return rawHeaderCache.headersList;

    rawHeaderCache.headersList = fromHttpToRaw(httpHeaders);
    rawHeaderCache.isCached = true;
    return rawHeaderCache.headersList;
}

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

//  from src/network/access/qnetworkrequest.cpp, line 1782, as _ZN22QNetworkHeadersPrivate12fromHttpDateE14QByteArrayView
#if defined(Q_OS_LINUX)
inline QDateTime QNetworkHeadersPrivate::fromHttpDate(QByteArrayView value)
{
    // HTTP dates have three possible formats:
    //  RFC 1123/822      -   ddd, dd MMM yyyy hh:mm:ss "GMT"
    //  RFC 850           -   dddd, dd-MMM-yy hh:mm:ss "GMT"
    //  ANSI C's asctime  -   ddd MMM d hh:mm:ss yyyy
    // We only handle them exactly. If they deviate, we bail out.

    int pos = value.indexOf(',');
    QDateTime dt;
#if QT_CONFIG(datestring)
    if (pos == -1) {
        // no comma -> asctime(3) format
        dt = QDateTime::fromString(QString::fromLatin1(value), Qt::TextDate);
    } else {
        // Use sscanf over QLocal/QDateTimeParser for speed reasons. See the
        // Qt WebKit performance benchmarks to get an idea.
        if (pos == 3) {
            char month_name[4];
            int day, year, hour, minute, second;
#ifdef Q_CC_MSVC
            // Use secure version to avoid compiler warning
            if (sscanf_s(value.constData(), "%*3s, %d %3s %d %d:%d:%d 'GMT'", &day, month_name, 4, &year, &hour, &minute, &second) == 6)
#else
            // The POSIX secure mode is %ms (which allocates memory), too bleeding edge for now
            // In any case this is already safe as field width is specified.
            if (sscanf(value.constData(), "%*3s, %d %3s %d %d:%d:%d 'GMT'", &day, month_name, &year, &hour, &minute, &second) == 6)
#endif
                dt = QDateTime(QDate(year, name_to_month(month_name), day), QTime(hour, minute, second));
        } else {
            QLocale c = QLocale::c();
            // eat the weekday, the comma and the space following it
            QString sansWeekday = QString::fromLatin1(value.constData() + pos + 2);
            // must be RFC 850 date
            dt = c.toDateTime(sansWeekday, "dd-MMM-yy hh:mm:ss 'GMT'"_L1);
        }
    }
#endif // datestring

    if (dt.isValid())
        dt.setTimeZone(QTimeZone::UTC);
    return dt;
}
#endif  // defined(Q_OS_LINUX)

//  from src/network/access/qnetworkrequest.cpp, line 1826, as _ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime
inline QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
{
    return QLocale::c().toString(dt.toUTC(), u"ddd, dd MMM yyyy hh:mm:ss 'GMT'").toLatin1();
}

//  from src/network/access/qnetworkrequest.cpp, line 1885, as _ZN22QNetworkHeadersPrivate5toIntE14QByteArrayView
inline std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView value)
{
    if (value.empty())
        return std::nullopt;

    bool ok;
    qint64 res = value.toLongLong(&ok);
    if (ok)
        return res;
    return std::nullopt;
}

//  from src/network/access/qnetworkrequest.cpp, line 1912, as _ZN22QNetworkHeadersPrivate14fromCookieListERK5QListI14QNetworkCookieE
inline QByteArray QNetworkHeadersPrivate::fromCookieList(const QList<QNetworkCookie> &cookies)
{
    return makeCookieHeader(cookies, QNetworkCookie::NameAndValueOnly, "; ");
}

//  from src/network/access/qnetworkrequest.cpp, line 1897, as _ZN22QNetworkHeadersPrivate15toSetCookieListERK5QListI10QByteArrayE
inline std::optional<QNetworkHeadersPrivate::NetworkCookieList> QNetworkHeadersPrivate::toSetCookieList(
        const QList<QByteArray> &values)
{
    if (values.empty())
        return std::nullopt;

    QList<QNetworkCookie> cookies;
    for (const auto &s : values)
        cookies += QNetworkCookie::parseCookies(s);

    if (cookies.empty())
        return std::nullopt;
    return cookies;
}

//  from src/network/access/qnetworkrequest.cpp, line 1917, as _ZN22QNetworkHeadersPrivate12toCookieListERK5QListI10QByteArrayE
inline std::optional<QNetworkHeadersPrivate::NetworkCookieList> QNetworkHeadersPrivate::toCookieList(
        const QList<QByteArray> &values)
{
    if (values.empty())
        return std::nullopt;

    QList<QNetworkCookie> cookies;
    for (const auto &s : values)
        cookies += parseCookieHeader(s);

    if (cookies.empty())
        return std::nullopt;
    return cookies;
}

//  from src/network/access/qnetworkrequest.cpp, line 1831, as _ZN22QNetworkHeadersPrivate13fromHttpToRawERK12QHttpHeaders
inline QNetworkHeadersPrivate::RawHeadersList QNetworkHeadersPrivate::fromHttpToRaw(
        const QHttpHeaders &headers)
{
    if (headers.isEmpty())
        return {};

    QNetworkHeadersPrivate::RawHeadersList list;
    QHash<QByteArray, qsizetype> nameToIndex;
    list.reserve(headers.size());
    nameToIndex.reserve(headers.size());

    for (qsizetype i = 0; i < headers.size(); ++i) {
        const auto nameL1 = headers.nameAt(i);
        const auto value = headers.valueAt(i);

        const bool isSetCookie = nameL1 == QHttpHeaders::wellKnownHeaderName(
                                         QHttpHeaders::WellKnownHeader::SetCookie);

        const auto name = QByteArray(nameL1.data(), nameL1.size());
        if (auto it = nameToIndex.find(name); it != nameToIndex.end()) {
            list[it.value()].second += isSetCookie ? "\n" : ", ";
            list[it.value()].second += value;
        } else {
            nameToIndex[name] = list.size();
            list.emplaceBack(name, value.toByteArray());
        }
    }

    return list;
}

//  from src/network/access/qnetworkrequest.cpp, line 1862, as _ZN22QNetworkHeadersPrivate13fromRawToHttpERK5QListISt4pairI10QByteArrayS2_EE
inline QHttpHeaders QNetworkHeadersPrivate::fromRawToHttp(const RawHeadersList &raw)
{
    if (raw.empty())
        return {};

    QHttpHeaders headers;
    headers.reserve(raw.size());

    for (const auto &[key, value] : raw) {
        const bool isSetCookie = key.compare(QHttpHeaders::wellKnownHeaderName(
                                             QHttpHeaders::WellKnownHeader::SetCookie),
                                             Qt::CaseInsensitive) == 0;
        if (isSetCookie) {
            for (auto header : QLatin1StringView(value).tokenize('\n'_L1))
                headers.append(key, header);
        } else {
            headers.append(key, value);
        }
    }

    return headers;
}

//  from src/network/access/qnetworkrequest.cpp, line 1932, as _ZN22QNetworkHeadersPrivate21invalidateHeaderCacheEv
inline void QNetworkHeadersPrivate::invalidateHeaderCache()
{
    rawHeaderCache.headersList.clear();
    rawHeaderCache.isCached = false;
}
//  -----------------------------------------------------------------------

//  const RawHeadersList &QNetworkHeadersPrivate::allRawHeaders() const
extern "C" Q_DECL_EXPORT
const QNetworkHeadersPrivate::RawHeadersList *ritual_ZNK22QNetworkHeadersPrivate13allRawHeadersEv(
    const QNetworkHeadersPrivate *self) {
  return &(self->allRawHeaders());
}

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

#if defined(Q_OS_LINUX)
//  QDateTime QNetworkHeadersPrivate::fromHttpDate(QByteArrayView value)
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZN22QNetworkHeadersPrivate12fromHttpDateE14QByteArrayView(
    const QByteArrayView *value) {
  return new QDateTime(QNetworkHeadersPrivate::fromHttpDate(*value));
}
#endif  // defined(Q_OS_LINUX)

//  QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime(
    const QDateTime *dt) {
  return new QByteArray(QNetworkHeadersPrivate::toHttpDate(*dt));
}

//  std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView value)
extern "C" Q_DECL_EXPORT
std::optional<qint64> *ritual_ZN22QNetworkHeadersPrivate5toIntE14QByteArrayView(
    const QByteArrayView *value) {
  return new std::optional<qint64>(QNetworkHeadersPrivate::toInt(*value));
}

//  QByteArray QNetworkHeadersPrivate::fromCookieList(const NetworkCookieList
//      &cookies)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QNetworkHeadersPrivate14fromCookieListERK5QListI14QNetworkCookieE(
    const QList<QNetworkCookie> *cookies) {
  return new QByteArray(QNetworkHeadersPrivate::fromCookieList(*cookies));
}

//  std::optional<NetworkCookieList>
//      QNetworkHeadersPrivate::toSetCookieList(const QList<QByteArray>
//      &values)
extern "C" Q_DECL_EXPORT
std::optional<QNetworkHeadersPrivate::NetworkCookieList> *ritual_ZN22QNetworkHeadersPrivate15toSetCookieListERK5QListI10QByteArrayE(
    const QList<QByteArray> *values) {
  return new std::optional<QNetworkHeadersPrivate::NetworkCookieList>(
      QNetworkHeadersPrivate::toSetCookieList(
          *values));
}

//  std::optional<NetworkCookieList>
//      QNetworkHeadersPrivate::toCookieList(const QList<QByteArray> &values)
extern "C" Q_DECL_EXPORT
std::optional<QNetworkHeadersPrivate::NetworkCookieList> *ritual_ZN22QNetworkHeadersPrivate12toCookieListERK5QListI10QByteArrayE(
    const QList<QByteArray> *values) {
  return new std::optional<QNetworkHeadersPrivate::NetworkCookieList>(
      QNetworkHeadersPrivate::toCookieList(
          *values));
}

//  RawHeadersList QNetworkHeadersPrivate::fromHttpToRaw(const QHttpHeaders
//      &headers)
extern "C" Q_DECL_EXPORT
QNetworkHeadersPrivate::RawHeadersList *ritual_ZN22QNetworkHeadersPrivate13fromHttpToRawERK12QHttpHeaders(
    const QHttpHeaders *headers) {
  return new QNetworkHeadersPrivate::RawHeadersList(
      QNetworkHeadersPrivate::fromHttpToRaw(
          *headers));
}

//  QHttpHeaders QNetworkHeadersPrivate::fromRawToHttp(const RawHeadersList
//      &raw)
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZN22QNetworkHeadersPrivate13fromRawToHttpERK5QListISt4pairI10QByteArrayS2_EE(
    const QNetworkHeadersPrivate::RawHeadersList *raw) {
  return new QHttpHeaders(QNetworkHeadersPrivate::fromRawToHttp(*raw));
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

//  a std::optional<qint64> a ritual of QNetworkHeadersPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkHeadersPrivate__std_optional_qint64(
    std::optional<qint64> *self) {
  delete self;
}

//  a std::optional<QNetworkHeadersPrivate::NetworkCookieList> a ritual of
//      QNetworkHeadersPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkHeadersPrivate__std_optional_QNetworkHeadersPrivate_NetworkCookieList(
    std::optional<QNetworkHeadersPrivate::NetworkCookieList> *self) {
  delete self;
}

//  a QNetworkHeadersPrivate::RawHeadersList a ritual of
//      QNetworkHeadersPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkHeadersPrivate__QNetworkHeadersPrivate_RawHeadersList(
    QNetworkHeadersPrivate::RawHeadersList *self) {
  delete self;
}
