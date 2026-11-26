//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qrestreply_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qrestreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qrestreply.h>
#include <QtNetwork/private/qrestreply_p.h>
#include <QtNetwork/private/qnetworkreply_p.h>
#include <QtNetwork/private/qrestaccessmanager_p.h>
#include <QtNetwork/private/qtcontenttypeparser_p.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qlatin1stringmatcher.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qstringconverter.h>
#include <QtCore/qxpfunctional.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qrestreply.cpp, line 285, as _ZN17QRestReplyPrivateC1Ev
inline QRestReplyPrivate::QRestReplyPrivate()
    = default;

//  from src/network/access/qrestreply.cpp, line 288, as _ZN17QRestReplyPrivateD1Ev
inline QRestReplyPrivate::~QRestReplyPrivate()
    = default;

//  from src/network/access/qrestreply.cpp, line 344, as _ZN17QRestReplyPrivate14contentCharsetEPK13QNetworkReply
inline QByteArray QRestReplyPrivate::contentCharset(const QNetworkReply* reply)
{
    // Content-type consists of mimetype and optional parameters, of which one may be 'charset'
    // Example values and their combinations below are all valid, see RFC 7231 section 3.1.1.5
    // and RFC 2045 section 5.1
    //
    // text/plain; charset=utf-8
    // text/plain; charset=utf-8;version=1.7
    // text/plain; charset = utf-8
    // text/plain; charset ="utf-8"

    const QByteArray contentTypeValue =
            reply->headers().value(QHttpHeaders::WellKnownHeader::ContentType).toByteArray();

    const auto r = QtContentTypeParser::parse_content_type(contentTypeValue);
    if (r && !r.charset.empty())
        return QByteArrayView(r.charset).toByteArray();
    else
        return "UTF-8"_ba; // Default to the most commonly used UTF-8.
}
//  -----------------------------------------------------------------------

//  QRestReplyPrivate::QRestReplyPrivate()
extern "C" Q_DECL_EXPORT
QRestReplyPrivate *ritual_ZN17QRestReplyPrivateC1Ev() {
  return new QRestReplyPrivate();
}

//  QRestReplyPrivate::~QRestReplyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRestReplyPrivateD1Ev(QRestReplyPrivate *self) {
  delete self;
}

//  QByteArray QRestReplyPrivate::contentCharset(const QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QRestReplyPrivate14contentCharsetEPK13QNetworkReply(
    const QNetworkReply *reply) {
  return new QByteArray(QRestReplyPrivate::contentCharset(reply));
}

#endif  // QT_CONFIG(http)
