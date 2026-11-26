//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslpresharedkeyauthenticator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslpresharedkeyauthenticator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslpresharedkeyauthenticator.h>
#include <QtNetwork/private/qsslpresharedkeyauthenticator_p.h>
#include <QtCore/QSharedData>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qsslpresharedkeyauthenticator.cpp, line 18, as _ZN36QSslPreSharedKeyAuthenticatorPrivateC1Ev
inline QSslPreSharedKeyAuthenticatorPrivate::QSslPreSharedKeyAuthenticatorPrivate()
    : maximumIdentityLength(0),
      maximumPreSharedKeyLength(0)
{
}
//  -----------------------------------------------------------------------

//  QSslPreSharedKeyAuthenticatorPrivate::QSslPreSharedKeyAuthenticatorPrivat
//      e()
extern "C" Q_DECL_EXPORT
QSslPreSharedKeyAuthenticatorPrivate *ritual_ZN36QSslPreSharedKeyAuthenticatorPrivateC1Ev() {
  return new QSslPreSharedKeyAuthenticatorPrivate();
}

//  QSslPreSharedKeyAuthenticatorPrivate::~QSslPreSharedKeyAuthenticatorPriva
//      te()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QSslPreSharedKeyAuthenticatorPrivateD1Ev(
    QSslPreSharedKeyAuthenticatorPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
