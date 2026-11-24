//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsctpserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if !defined(QT_NO_SCTP)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qsctpserver.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsctpserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsctpserver.h"
#include "qsctpserver_p.h"
#include "qsctpsocket.h"
#include "qabstractsocketengine_p.h"
#ifdef QSCTPSERVER_DEBUG
#include <qdebug.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qsctpserver.cpp, line 76, as _ZN18QSctpServerPrivateD2Ev
inline QSctpServerPrivate::~QSctpServerPrivate()
{
}

//  from src/network/socket/qsctpserver.cpp, line 82, as _ZN18QSctpServerPrivate22configureCreatedSocketEv
inline void QSctpServerPrivate::configureCreatedSocket()
{
    QTcpServerPrivate::configureCreatedSocket();
    if (socketEngine)
        socketEngine->setOption(QAbstractSocketEngine::MaxStreamsSocketOption,
                                maximumChannelCount == -1 ? 1 : maximumChannelCount);
}
//  -----------------------------------------------------------------------

//  A QSctpServerPrivate that Python can take functions over in. Every QSctpServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SCTP)
typedef void (*CuteQSctpServerPrivateCall0)(const void *, int *);
#endif  // !defined(QT_NO_SCTP)
typedef int (*CuteQSctpServerPrivateCall1)(const void *, int *);
typedef void (*CuteQSctpServerPrivateCall2)(const void *, int *);
typedef void (*CuteQSctpServerPrivateCall3)(const void *, int *);
typedef void (*CuteQSctpServerPrivateCall4)(const void *, int *);
typedef void (*CuteQSctpServerPrivateCall5)(const void *, int *);
typedef void (*CuteQSctpServerPrivateCall6)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQSctpServerPrivateCall7)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
class CuteQSctpServerPrivate : public QSctpServerPrivate {
public:
  using QSctpServerPrivate::QSctpServerPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZN17QTcpServerPrivate22configureCreatedSocketEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP)
    if (!std::strcmp(key, "_ZNK17QTcpServerPrivate23totalPendingConnectionsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
    return false;
  }

#if !defined(QT_NO_SCTP)
  //  void QSctpServerPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSctpServerPrivateCall0 call = reinterpret_cast<CuteQSctpServerPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSctpServerPrivate::configureCreatedSocket();
  }
#endif  // !defined(QT_NO_SCTP)

  //  int QTcpServerPrivate::totalPendingConnections() const
  int totalPendingConnections() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSctpServerPrivateCall1 call = reinterpret_cast<CuteQSctpServerPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTcpServerPrivate::totalPendingConnections();
  }

  //  void QTcpServerPrivate::readNotification()
  void readNotification() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSctpServerPrivateCall2 call = reinterpret_cast<CuteQSctpServerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::readNotification();
  }

  //  void QTcpServerPrivate::closeNotification()
  void closeNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSctpServerPrivateCall3 call = reinterpret_cast<CuteQSctpServerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::closeNotification();
  }

  //  void QTcpServerPrivate::writeNotification()
  void writeNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSctpServerPrivateCall4 call = reinterpret_cast<CuteQSctpServerPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::writeNotification();
  }

  //  void QTcpServerPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSctpServerPrivateCall5 call = reinterpret_cast<CuteQSctpServerPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::exceptionNotification();
  }

  //  void QTcpServerPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSctpServerPrivateCall6 call = reinterpret_cast<CuteQSctpServerPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::connectionNotification();
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QTcpServerPrivate::proxyAuthenticationRequired(const
  //      QNetworkProxy &a0, QAuthenticator *a1)
  void proxyAuthenticationRequired(
      const QNetworkProxy &a0,
      QAuthenticator *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSctpServerPrivateCall7 call = reinterpret_cast<CuteQSctpServerPrivateCall7>(taken[7]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::proxyAuthenticationRequired(a0, a1);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
};

//  QSctpServer *QSctpServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSctpServer *ritual_ZN18QSctpServerPrivate6q_funcEv(
    QSctpServerPrivate *self) {
  return self->q_func();
}

//  const QSctpServer *QSctpServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSctpServer *ritual_ZNK18QSctpServerPrivate6q_funcEv(
    const QSctpServerPrivate *self) {
  return self->q_func();
}

//  QSctpServerPrivate::~QSctpServerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSctpServerPrivateD1Ev(QSctpServerPrivate *self) {
  delete self;
}

//  void QSctpServerPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSctpServerPrivate22configureCreatedSocketEv(
    QSctpServerPrivate *self) {
  self->configureCreatedSocket();
}

//  a Python function taken by a CuteQSctpServerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSctpServerPrivate(
    QSctpServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSctpServerPrivate *>(self)->take(key, call);
}

//  void QSctpServerPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSctpServerPrivate22configureCreatedSocketEv(
    QSctpServerPrivate *self) {
  self->QSctpServerPrivate::configureCreatedSocket();
}

#endif  // !defined(QT_NO_SCTP)
