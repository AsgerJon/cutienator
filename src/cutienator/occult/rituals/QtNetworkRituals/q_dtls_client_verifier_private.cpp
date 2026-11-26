//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qdtls_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dtls) && QT_CONFIG(ssl)
#if QT_CONFIG(dtls)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qdtls_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qsslsocket_p.h>
#include <QtNetwork/qudpsocket.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/private/qdtls_p.h>
#include <QtNetwork/private/qssl_p.h>
#include <QtNetwork/qdtls.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qdtls.cpp, line 347, as _ZN26QDtlsClientVerifierPrivateD1Ev
inline QDtlsClientVerifierPrivate::~QDtlsClientVerifierPrivate() = default;
//  -----------------------------------------------------------------------

//  QDtlsClientVerifierPrivate::~QDtlsClientVerifierPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDtlsClientVerifierPrivateD1Ev(
    QDtlsClientVerifierPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(dtls)
#endif  // QT_CONFIG(dtls) && QT_CONFIG(ssl)
