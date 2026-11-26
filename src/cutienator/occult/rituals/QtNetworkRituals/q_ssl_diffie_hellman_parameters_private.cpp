//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qssldiffiehellmanparameters_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qssldiffiehellmanparameters_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qssldiffiehellmanparameters.h>
#include <QtNetwork/private/qssldiffiehellmanparameters_p.h>
#include <QtNetwork/private/qtlsbackend_p.h>
#include <QtNetwork/qsslsocket.h>
#include <QtNetwork/private/qsslsocket_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qatomic.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearraymatcher.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qssldiffiehellmanparameters.cpp, line 272, as _ZN34QSslDiffieHellmanParametersPrivate11initFromDerERK10QByteArray
inline void QSslDiffieHellmanParametersPrivate::initFromDer(const QByteArray &der)
{
    if (const auto *tlsBackend = QSslSocketPrivate::tlsBackendInUse())
        error = QSslDiffieHellmanParameters::Error(tlsBackend->dhParametersFromDer(der, &derData));
}

//  from src/network/ssl/qssldiffiehellmanparameters.cpp, line 281, as _ZN34QSslDiffieHellmanParametersPrivate11initFromPemERK10QByteArray
inline void QSslDiffieHellmanParametersPrivate::initFromPem(const QByteArray &pem)
{
    if (const auto *tlsBackend = QSslSocketPrivate::tlsBackendInUse())
        error = QSslDiffieHellmanParameters::Error(tlsBackend->dhParametersFromPem(pem, &derData));
}
//  -----------------------------------------------------------------------

//  void QSslDiffieHellmanParametersPrivate::initFromDer(const QByteArray
//      &der)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSslDiffieHellmanParametersPrivate11initFromDerERK10QByteArray(
    QSslDiffieHellmanParametersPrivate *self,
    const QByteArray *der) {
  self->initFromDer(*der);
}

//  void QSslDiffieHellmanParametersPrivate::initFromPem(const QByteArray
//      &pem)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSslDiffieHellmanParametersPrivate11initFromPemERK10QByteArray(
    QSslDiffieHellmanParametersPrivate *self,
    const QByteArray *pem) {
  self->initFromPem(*pem);
}

//  QSslDiffieHellmanParametersPrivate::~QSslDiffieHellmanParametersPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSslDiffieHellmanParametersPrivateD1Ev(
    QSslDiffieHellmanParametersPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
