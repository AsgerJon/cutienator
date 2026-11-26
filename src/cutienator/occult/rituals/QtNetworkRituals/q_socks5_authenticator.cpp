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
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>
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

using namespace Qt::StringLiterals;

//  from src/network/socket/qsocks5socketengine.cpp, line 402, as _ZN20QSocks5Authenticator17beginAuthenticateEP10QTcpSocketPb
inline bool QSocks5Authenticator::beginAuthenticate(QTcpSocket *socket, bool *completed)
{
    Q_UNUSED(socket);
    *completed = true;
    return true;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 409, as _ZN20QSocks5Authenticator20continueAuthenticateEP10QTcpSocketPb
inline bool QSocks5Authenticator::continueAuthenticate(QTcpSocket *socket, bool *completed)
{
    Q_UNUSED(socket);
    *completed = true;
    return true;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 397, as _ZN20QSocks5Authenticator8methodIdEv
inline char QSocks5Authenticator::methodId()
{
    return 0x00;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 393, as _ZN20QSocks5AuthenticatorD2Ev
inline QSocks5Authenticator::~QSocks5Authenticator()
{
}

//  from src/network/socket/qsocks5socketengine.cpp, line 389, as _ZN20QSocks5AuthenticatorC1Ev
inline QSocks5Authenticator::QSocks5Authenticator()
{
}

//  from src/network/socket/qsocks5socketengine.cpp, line 416, as _ZN20QSocks5Authenticator4sealERK10QByteArrayPS0_
inline bool QSocks5Authenticator::seal(const QByteArray &buf, QByteArray *sealedBuf)
{
    *sealedBuf = buf;
    return true;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 422, as _ZN20QSocks5Authenticator6unSealERK10QByteArrayPS0_
inline bool QSocks5Authenticator::unSeal(const QByteArray &sealedBuf, QByteArray *buf)
{
    *buf = sealedBuf;
    return true;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 428, as _ZN20QSocks5Authenticator6unSealEP10QTcpSocketP10QByteArray
inline bool QSocks5Authenticator::unSeal(QTcpSocket *sealedSocket, QByteArray *buf)
{
    return unSeal(sealedSocket->readAll(), buf);
}
//  -----------------------------------------------------------------------

//  A QSocks5Authenticator that Python can take functions over in. Every QSocks5Authenticator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(socks5)
typedef char (*CuteQSocks5AuthenticatorCall0)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef QString * (*CuteQSocks5AuthenticatorCall1)(const void *, int *);
#endif  // QT_CONFIG(socks5)
class CuteQSocks5Authenticator : public QSocks5Authenticator {
public:
  using QSocks5Authenticator::QSocks5Authenticator;
  CuteQSocks5Authenticator(const QSocks5Authenticator & other) : QSocks5Authenticator(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN20QSocks5Authenticator8methodIdEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN20QSocks5Authenticator11errorStringEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
    return false;
  }

#if QT_CONFIG(socks5)
  //  char QSocks5Authenticator::methodId()
  char methodId() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSocks5AuthenticatorCall0 call = reinterpret_cast<CuteQSocks5AuthenticatorCall0>(taken[0]);
      char given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5Authenticator::methodId();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  QString QSocks5Authenticator::errorString()
  QString errorString() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSocks5AuthenticatorCall1 call = reinterpret_cast<CuteQSocks5AuthenticatorCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSocks5Authenticator::errorString();
  }
#endif  // QT_CONFIG(socks5)
};

//  QSocks5Authenticator::QSocks5Authenticator()
extern "C" Q_DECL_EXPORT
QSocks5Authenticator *ritual_ZN20QSocks5AuthenticatorC1Ev() {
  return new CuteQSocks5Authenticator();
}

//  QSocks5Authenticator::~QSocks5Authenticator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSocks5AuthenticatorD1Ev(QSocks5Authenticator *self) {
  delete self;
}

//  char QSocks5Authenticator::methodId()
extern "C" Q_DECL_EXPORT
char ritual_ZN20QSocks5Authenticator8methodIdEv(QSocks5Authenticator *self) {
  return self->methodId();
}

//  bool QSocks5Authenticator::beginAuthenticate(QTcpSocket *socket, bool
//      *completed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSocks5Authenticator17beginAuthenticateEP10QTcpSocketPb(
    QSocks5Authenticator *self,
    QTcpSocket *socket,
    bool *completed) {
  return self->beginAuthenticate(socket, completed);
}

//  bool QSocks5Authenticator::continueAuthenticate(QTcpSocket *socket, bool
//      *completed)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSocks5Authenticator20continueAuthenticateEP10QTcpSocketPb(
    QSocks5Authenticator *self,
    QTcpSocket *socket,
    bool *completed) {
  return self->continueAuthenticate(socket, completed);
}

//  bool QSocks5Authenticator::seal(const QByteArray &buf, QByteArray
//      *sealedBuf)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSocks5Authenticator4sealERK10QByteArrayPS0_(
    QSocks5Authenticator *self,
    const QByteArray *buf,
    QByteArray *sealedBuf) {
  return self->seal(*buf, sealedBuf);
}

//  bool QSocks5Authenticator::unSeal(const QByteArray &sealedBuf, QByteArray
//      *buf)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSocks5Authenticator6unSealERK10QByteArrayPS0_(
    QSocks5Authenticator *self,
    const QByteArray *sealedBuf,
    QByteArray *buf) {
  return self->unSeal(*sealedBuf, buf);
}

//  bool QSocks5Authenticator::unSeal(QTcpSocket *sealedSocket, QByteArray
//      *buf)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSocks5Authenticator6unSealEP10QTcpSocketP10QByteArray(
    QSocks5Authenticator *self,
    QTcpSocket *sealedSocket,
    QByteArray *buf) {
  return self->unSeal(sealedSocket, buf);
}

//  QString QSocks5Authenticator::errorString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QSocks5Authenticator11errorStringEv(
    QSocks5Authenticator *self) {
  return new QString(self->errorString());
}

//  a Python function taken by a CuteQSocks5Authenticator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSocks5Authenticator(
    QSocks5Authenticator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSocks5Authenticator *>(self)->take(key, call);
}

//  char QSocks5Authenticator::methodId()
extern "C" Q_DECL_EXPORT
char ritual_own_ZN20QSocks5Authenticator8methodIdEv(
    QSocks5Authenticator *self) {
  return self->QSocks5Authenticator::methodId();
}

//  QString QSocks5Authenticator::errorString()
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN20QSocks5Authenticator11errorStringEv(
    QSocks5Authenticator *self) {
  return new QString(self->QSocks5Authenticator::errorString());
}

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
