//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhsts.cpp, line 245, as local:qhsts.cpp:isCHAR
static bool isCHAR(int c)
{
    // CHAR           = <any US-ASCII character (octets 0 - 127)>
    return c >= 0 && c <= 127;
}

//  from src/network/access/qhsts.cpp, line 251, as local:qhsts.cpp:isCTL
static bool isCTL(int c)
{
    // CTL            = <any US-ASCII control character
    //                  (octets 0 - 31) and DEL (127)>
    return (c >= 0 && c <= 31) || c == 127;
}

//  from src/network/access/qhsts.cpp, line 259, as local:qhsts.cpp:isLWS
static bool isLWS(int c)
{
    // LWS            = [CRLF] 1*( SP | HT )
    //
    // CRLF           = CR LF
    // CR             = <US-ASCII CR, carriage return (13)>
    // LF             = <US-ASCII LF, linefeed (10)>
    // SP             = <US-ASCII SP, space (32)>
    // HT             = <US-ASCII HT, horizontal-tab (9)>
    //
    // CRLF is handled by the time we parse a header (they were replaced with
    // spaces). We only have to deal with remaining SP|HT
    return c == ' '  || c == '\t';
}

//  from src/network/access/qhsts.cpp, line 274, as local:qhsts.cpp:isTEXT
static bool isTEXT(char c)
{
    // TEXT           = <any OCTET except CTLs,
    //                  but including LWS>
    return !isCTL(c) || isLWS(c);
}

//  from src/network/access/qhsts.cpp, line 292, as local:qhsts.cpp:unescapeMaxAge
static QByteArrayView unescapeMaxAge(QByteArrayView value)
{
    if (value.size() < 2 || value[0] != '"')
        return value;

    Q_ASSERT(value[value.size() - 1] == '"');
    return value.mid(1, value.size() - 2);
}

//  from src/network/access/qhsts.cpp, line 433, as _ZN17QHstsHeaderParser16processDirectiveERK10QByteArrayS2_
inline bool QHstsHeaderParser::processDirective(const QByteArray &name, const QByteArray &value)
{
    Q_ASSERT(name.size());
    // RFC6797 6.1/3 Directive names are case-insensitive
    if (name.compare("max-age", Qt::CaseInsensitive) == 0) {
        // RFC 6797, 6.1.1
        // The syntax of the max-age directive's REQUIRED value (after
        // quoted-string unescaping, if necessary) is defined as:
        //
        // max-age-value = delta-seconds
        if (maxAgeFound) {
            // RFC 6797, 6.1/2:
            // All directives MUST appear only once in an STS header field.
            return false;
        }

        const QByteArrayView unescapedValue = unescapeMaxAge(value);
        if (!unescapedValue.size())
            return false;

        bool ok = false;
        const qint64 age = unescapedValue.toLongLong(&ok);
        if (!ok || age < 0)
            return false;

        maxAge = age;
        maxAgeFound = true;
    } else if (name.compare("includesubdomains", Qt::CaseInsensitive) == 0) {
        // RFC 6797, 6.1.2.  The includeSubDomains Directive.
        // The OPTIONAL "includeSubDomains" directive is a valueless directive.

        if (subDomainsFound) {
            // RFC 6797, 6.1/2:
            // All directives MUST appear only once in an STS header field.
            return false;
        }

        subDomainsFound = true;
    } // else we do nothing, skip unknown directives (RFC 6797, 6.1/5)

    return true;
}
//  -----------------------------------------------------------------------

//  QDateTime QHstsHeaderParser::expirationDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK17QHstsHeaderParser14expirationDateEv(
    const QHstsHeaderParser *self) {
  return new QDateTime(self->expirationDate());
}

//  bool QHstsHeaderParser::includeSubDomains() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHstsHeaderParser17includeSubDomainsEv(
    const QHstsHeaderParser *self) {
  return self->includeSubDomains();
}

//  bool QHstsHeaderParser::processDirective(const QByteArray &name, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHstsHeaderParser16processDirectiveERK10QByteArrayS2_(
    QHstsHeaderParser *self,
    const QByteArray *name,
    const QByteArray *value) {
  return self->processDirective(*name, *value);
}

//  QHstsHeaderParser::~QHstsHeaderParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHstsHeaderParserD1Ev(QHstsHeaderParser *self) {
  delete self;
}
