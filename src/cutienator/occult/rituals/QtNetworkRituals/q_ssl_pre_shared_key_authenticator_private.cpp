//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslpresharedkeyauthenticator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslpresharedkeyauthenticator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsslpresharedkeyauthenticator.h"
#include "qsslpresharedkeyauthenticator_p.h"
#include <QSharedData>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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
