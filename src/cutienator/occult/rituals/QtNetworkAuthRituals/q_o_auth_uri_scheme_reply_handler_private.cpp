//  Written by hand on 2026-11-25 from
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthurischemereplyhandler_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds the class only with its feature 'urischeme_replyhandler',
//  as the CMakeLists.txt of its oauth directory says, so the whole file
//  stands under it. The feature is private to the part, its line is in
//  the private config header, which comes first.
#include <QtNetworkAuth/qoauthglobal.h>
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qtnetworkauth-config_p.h>
#if QT_CONFIG(urischeme_replyhandler)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauthurischemereplyhandler.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthurischemereplyhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractoauthreplyhandler_p.h" // for lcReplyHandler()
#include "qoauthurischemereplyhandler.h"
#include "qoauthurischemereplyhandler_p.h"
#include <QtGui/qdesktopservices.h>
#include <private/qobject_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qurlquery.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qoauthurischemereplyhandler.cpp, line 153, as _ZNK34QOAuthUriSchemeReplyHandlerPrivate19hasValidRedirectUrlEv
inline bool QOAuthUriSchemeReplyHandlerPrivate::hasValidRedirectUrl() const
{
    // RFC 6749 Section 3.1.2
    return redirectUrl.isValid()
           && !redirectUrl.scheme().isEmpty()
           && redirectUrl.fragment().isEmpty();
}
//  -----------------------------------------------------------------------

//  QOAuthUriSchemeReplyHandler *QOAuthUriSchemeReplyHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOAuthUriSchemeReplyHandler *ritual_ZN34QOAuthUriSchemeReplyHandlerPrivate6q_funcEv(
    QOAuthUriSchemeReplyHandlerPrivate *self) {
  return self->q_func();
}

//  const QOAuthUriSchemeReplyHandler
//      *QOAuthUriSchemeReplyHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuthUriSchemeReplyHandler *ritual_ZNK34QOAuthUriSchemeReplyHandlerPrivate6q_funcEv(
    const QOAuthUriSchemeReplyHandlerPrivate *self) {
  return self->q_func();
}

//  bool QOAuthUriSchemeReplyHandlerPrivate::hasValidRedirectUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QOAuthUriSchemeReplyHandlerPrivate19hasValidRedirectUrlEv(
    const QOAuthUriSchemeReplyHandlerPrivate *self) {
  return self->hasValidRedirectUrl();
}

#endif  // QT_CONFIG(urischeme_replyhandler)
