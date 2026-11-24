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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qsocks5socketengine.cpp, line 389, as _ZN20QSocks5AuthenticatorC2Ev
inline QSocks5Authenticator::QSocks5Authenticator()
{
}

//  from src/network/socket/qsocks5socketengine.cpp, line 393, as _ZN20QSocks5AuthenticatorD2Ev
inline QSocks5Authenticator::~QSocks5Authenticator()
{
}

//  from src/network/socket/qsocks5socketengine.cpp, line 439, as _ZN28QSocks5PasswordAuthenticator8methodIdEv
inline char QSocks5PasswordAuthenticator::methodId()
{
    return 0x02;
}
//  -----------------------------------------------------------------------

//  char QSocks5PasswordAuthenticator::methodId()
extern "C" Q_DECL_EXPORT
char ritual_ZN28QSocks5PasswordAuthenticator8methodIdEv(
    QSocks5PasswordAuthenticator *self) {
  return self->methodId();
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

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
