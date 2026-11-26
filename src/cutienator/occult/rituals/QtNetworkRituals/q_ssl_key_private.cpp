//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslkey_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslkey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qssl_p.h>
#include <QtNetwork/qsslkey.h>
#include <QtNetwork/private/qsslkey_p.h>
#include <QtNetwork/qsslsocket.h>
#include <QtNetwork/private/qsslsocket_p.h>
#include <QtNetwork/private/qtlsbackend_p.h>
#include <QtCore/qatomic.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qiodevice.h>
#ifndef QT_NO_DEBUG_STREAM
#include <QtCore/qdebug.h>
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

//  from src/network/ssl/qsslkey_p.cpp, line 72, as _ZN14QSslKeyPrivateD1Ev
inline QSslKeyPrivate::~QSslKeyPrivate()
{
    if (backend.get())
        backend->clear(true /*deep clear*/);
}
//  -----------------------------------------------------------------------

//  QSslKeyPrivate::~QSslKeyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSslKeyPrivateD1Ev(QSslKeyPrivate *self) {
  delete self;
}

//  QByteArray QSslKeyPrivate::decrypt(Cipher cipher, const QByteArray &data,
//      const QByteArray &key, const QByteArray &iv)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QSslKeyPrivate7decryptEN11QTlsPrivate6CipherERK10QByteArrayS4_S4_(
    QSslKeyPrivate::Cipher cipher,
    const QByteArray *data,
    const QByteArray *key,
    const QByteArray *iv) {
  return new QByteArray(QSslKeyPrivate::decrypt(cipher, *data, *key, *iv));
}

//  QByteArray QSslKeyPrivate::encrypt(Cipher cipher, const QByteArray &data,
//      const QByteArray &key, const QByteArray &iv)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QSslKeyPrivate7encryptEN11QTlsPrivate6CipherERK10QByteArrayS4_S4_(
    QSslKeyPrivate::Cipher cipher,
    const QByteArray *data,
    const QByteArray *key,
    const QByteArray *iv) {
  return new QByteArray(QSslKeyPrivate::encrypt(cipher, *data, *key, *iv));
}

#endif  // QT_CONFIG(ssl)
