//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qsocks5socketengine_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtNetwork/qudpsocket.h>
#include <QtNetwork/qtcpserver.h>
#include <QtCore/qdebug.h>
#include <QtCore/qhash.h>
#include <QtCore/qqueue.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmutex.h>
#include <QtCore/qthread.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qauthenticator.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/private/qringbuffer_p.h>
#include <QtCore/qendian.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qbasictimer.h>
#include <QtCore/qpointer.h>
#include <memory>
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

//  from src/network/socket/qsocks5socketengine.cpp, line 68, as local:qsocks5socketengine.cpp:S5_PASSWORDAUTH_VERSION
#define S5_PASSWORDAUTH_VERSION 0x01

//  from src/network/socket/qsocks5socketengine.cpp, line 389, as _ZN20QSocks5AuthenticatorC2Ev
inline QSocks5Authenticator::QSocks5Authenticator()
{
}

//  from src/network/socket/qsocks5socketengine.cpp, line 439, as _ZN28QSocks5PasswordAuthenticator8methodIdEv
inline char QSocks5PasswordAuthenticator::methodId()
{
    return 0x02;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 444, as _ZN28QSocks5PasswordAuthenticator17beginAuthenticateEP10QTcpSocketPb
inline bool QSocks5PasswordAuthenticator::beginAuthenticate(QTcpSocket *socket, bool *completed)
{
    *completed = false;
    QByteArray uname = userName.toLatin1();
    QByteArray passwd = password.toLatin1();
    QByteArray dataBuf(3 + uname.size() + passwd.size(), 0);
    char *buf = dataBuf.data();
    int pos = 0;
    buf[pos++] = S5_PASSWORDAUTH_VERSION;
    buf[pos++] = uname.size();
    memcpy(&buf[pos], uname.data(), uname.size());
    pos += uname.size();
    buf[pos++] = passwd.size();
    memcpy(&buf[pos], passwd.data(), passwd.size());
    return socket->write(dataBuf) == dataBuf.size();
}

//  from src/network/socket/qsocks5socketengine.cpp, line 479, as _ZN28QSocks5PasswordAuthenticator11errorStringEv
inline QString QSocks5PasswordAuthenticator::errorString()
{
    return "Socks5 user name or password incorrect"_L1;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 393, as _ZN20QSocks5AuthenticatorD2Ev
inline QSocks5Authenticator::~QSocks5Authenticator()
{
}
//  -----------------------------------------------------------------------

//  char QSocks5PasswordAuthenticator::methodId()
extern "C" Q_DECL_EXPORT
char ritual_ZN28QSocks5PasswordAuthenticator8methodIdEv(
    QSocks5PasswordAuthenticator *self) {
  return self->methodId();
}

//  bool QSocks5PasswordAuthenticator::beginAuthenticate(QTcpSocket *socket,
//      bool *completed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSocks5PasswordAuthenticator17beginAuthenticateEP10QTcpSocketPb(
    QSocks5PasswordAuthenticator *self,
    QTcpSocket *socket,
    bool *completed) {
  return self->beginAuthenticate(socket, completed);
}

//  bool QSocks5PasswordAuthenticator::continueAuthenticate(QTcpSocket
//      *socket, bool *completed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSocks5PasswordAuthenticator20continueAuthenticateEP10QTcpSocketPb(
    QSocks5PasswordAuthenticator *self,
    QTcpSocket *socket,
    bool *completed) {
  return self->continueAuthenticate(socket, completed);
}

//  QString QSocks5PasswordAuthenticator::errorString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QSocks5PasswordAuthenticator11errorStringEv(
    QSocks5PasswordAuthenticator *self) {
  return new QString(self->errorString());
}

//  QSocks5PasswordAuthenticator::~QSocks5PasswordAuthenticator()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSocks5PasswordAuthenticatorD1Ev(
    QSocks5PasswordAuthenticator *self) {
  delete self;
}

//  char QSocks5PasswordAuthenticator::methodId()
extern "C" Q_DECL_EXPORT
char ritual_own_ZN28QSocks5PasswordAuthenticator8methodIdEv(
    QSocks5PasswordAuthenticator *self) {
  return self->QSocks5PasswordAuthenticator::methodId();
}

//  QString QSocks5PasswordAuthenticator::errorString()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN28QSocks5PasswordAuthenticator11errorStringEv(
    QSocks5PasswordAuthenticator *self) {
  return new QString(self->QSocks5PasswordAuthenticator::errorString());
}

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
