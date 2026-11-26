//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpsocketengine_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qurl.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtNetwork/qnetworkinterface.h>
#if !defined(QT_NO_NETWORKPROXY)
#include <QtCore/qdebug.h>
#endif
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/socket/qhttpsocketengine.cpp, line 817, as _ZN24QHttpSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject
#if !defined(QT_NO_NETWORKPROXY)
inline QAbstractSocketEngine *QHttpSocketEngineHandler::createSocketEngine(QAbstractSocket::SocketType socketType,
                                                                    const QNetworkProxy &proxy,
                                                                    QObject *parent)
{
    if (socketType != QAbstractSocket::TcpSocket)
        return nullptr;

    // proxy type must have been resolved by now
    if (proxy.type() != QNetworkProxy::HttpProxy)
        return nullptr;

    // we only accept active sockets
    if (!qobject_cast<QAbstractSocket *>(parent))
        return nullptr;

    QHttpSocketEngine *engine = new QHttpSocketEngine(parent);
    engine->setProxy(proxy);
    return engine;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 837, as _ZN24QHttpSocketEngineHandler18createSocketEngineExP7QObject
#if !defined(QT_NO_NETWORKPROXY)
inline QAbstractSocketEngine *QHttpSocketEngineHandler::createSocketEngine(qintptr, QObject *)
{
    return nullptr;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 75, as _ZN17QHttpSocketEngine8setProxyERK13QNetworkProxy
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpSocketEngine::setProxy(const QNetworkProxy &proxy)
{
    Q_D(QHttpSocketEngine);
    d->proxy = proxy;
    QString user = proxy.user();
    if (!user.isEmpty())
        d->authenticator.setUser(user);
    QString password = proxy.password();
    if (!password.isEmpty())
        d->authenticator.setPassword(password);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 23, as _ZN17QHttpSocketEngineC1EP7QObject
#if !defined(QT_NO_NETWORKPROXY)
inline QHttpSocketEngine::QHttpSocketEngine(QObject *parent)
    : QAbstractSocketEngine(*new QHttpSocketEnginePrivate, parent)
{
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qabstractsocketengine.cpp, line 60, as _ZN21QAbstractSocketEngineC2ER28QAbstractSocketEnginePrivateP7QObject
inline QAbstractSocketEngine::QAbstractSocketEngine(QAbstractSocketEnginePrivate &dd, QObject* parent)
    : QObject(dd, parent)
{
}

//  from src/network/socket/qhttpsocketengine.cpp, line 798, as _ZN24QHttpSocketEnginePrivateC1Ev
#if !defined(QT_NO_NETWORKPROXY)
inline QHttpSocketEnginePrivate::QHttpSocketEnginePrivate()
    : readNotificationEnabled(false)
    , writeNotificationEnabled(false)
    , exceptNotificationEnabled(false)
    , readNotificationPending(false)
    , writeNotificationPending(false)
    , connectionNotificationPending(false)
    , credentialsSent(false)
    , pendingResponseData(0)
{
    socket = nullptr;
    reply = nullptr;
    state = QHttpSocketEngine::None;
}
#endif  // !defined(QT_NO_NETWORKPROXY)
//  -----------------------------------------------------------------------

//  A QHttpSocketEngineHandler that Python can take functions over in. Every QHttpSocketEngineHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void * (*CuteQHttpSocketEngineHandlerCall0)(const void *, int, const QNetworkProxy *, QObject *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
typedef void * (*CuteQHttpSocketEngineHandlerCall1)(const void *, qintptr, QObject *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
class CuteQHttpSocketEngineHandler : public QHttpSocketEngineHandler {
public:
  using QHttpSocketEngineHandler::QHttpSocketEngineHandler;
  CuteQHttpSocketEngineHandler(const QHttpSocketEngineHandler & other) : QHttpSocketEngineHandler(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineExP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
    return false;
  }

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  QAbstractSocketEngine *QHttpSocketEngineHandler::createSocketEngine(Q
  //      AbstractSocket::SocketType socketType, const QNetworkProxy &a1,
  //      QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      QAbstractSocket::SocketType socketType,
      const QNetworkProxy &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpSocketEngineHandlerCall0 call = reinterpret_cast<CuteQHttpSocketEngineHandlerCall0>(taken[0]);
      void * given = call(this, static_cast<int>(socketType), &a1, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return QHttpSocketEngineHandler::createSocketEngine(socketType, a1, parent);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
  //  QAbstractSocketEngine
  //      *QHttpSocketEngineHandler::createSocketEngine(qintptr
  //      socketDescripter, QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      qintptr socketDescripter,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpSocketEngineHandlerCall1 call = reinterpret_cast<CuteQHttpSocketEngineHandlerCall1>(taken[1]);
      void * given = call(this, socketDescripter, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return QHttpSocketEngineHandler::createSocketEngine(socketDescripter, parent);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
};

//  QAbstractSocketEngine
//      *QHttpSocketEngineHandler::createSocketEngine(QAbstractSocket::Socket
//      Type socketType, const QNetworkProxy &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN24QHttpSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject(
    QHttpSocketEngineHandler *self,
    QAbstractSocket::SocketType socketType,
    const QNetworkProxy *a1,
    QObject *parent) {
  return self->createSocketEngine(socketType, *a1, parent);
}

//  QAbstractSocketEngine
//      *QHttpSocketEngineHandler::createSocketEngine(qintptr
//      socketDescripter, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN24QHttpSocketEngineHandler18createSocketEngineExP7QObject(
    QHttpSocketEngineHandler *self,
    qintptr socketDescripter,
    QObject *parent) {
  return self->createSocketEngine(socketDescripter, parent);
}

//  QHttpSocketEngineHandler::~QHttpSocketEngineHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpSocketEngineHandlerD1Ev(
    QHttpSocketEngineHandler *self) {
  delete self;
}

//  a Python function taken by a CuteQHttpSocketEngineHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpSocketEngineHandler(
    QHttpSocketEngineHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpSocketEngineHandler *>(self)->take(key, call);
}

#if !defined(QT_NO_NETWORKPROXY)
//  QAbstractSocketEngine
//      *QHttpSocketEngineHandler::createSocketEngine(qintptr
//      socketDescripter, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_own_ZN24QHttpSocketEngineHandler18createSocketEngineExP7QObject(
    QHttpSocketEngineHandler *self,
    qintptr socketDescripter,
    QObject *parent) {
  return self->QHttpSocketEngineHandler::createSocketEngine(
      socketDescripter,
      parent);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
