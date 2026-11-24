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
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>

//  A QSocks5SocketEngineHandler that Python can take functions over in. Every QSocks5SocketEngineHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(socks5)
typedef void * (*CuteQSocks5SocketEngineHandlerCall0)(const void *, int, const QNetworkProxy *, QObject *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void * (*CuteQSocks5SocketEngineHandlerCall1)(const void *, qintptr, QObject *, int *);
#endif  // QT_CONFIG(socks5)
class CuteQSocks5SocketEngineHandler : public QSocks5SocketEngineHandler {
public:
  using QSocks5SocketEngineHandler::QSocks5SocketEngineHandler;
  CuteQSocks5SocketEngineHandler(const QSocks5SocketEngineHandler &other) : QSocks5SocketEngineHandler(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineExP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
    return false;
  }

#if QT_CONFIG(socks5)
  //  QAbstractSocketEngine *QSocks5SocketEngineHandler::createSocketEngine
  //      (QAbstractSocket::SocketType socketType, const QNetworkProxy &a1,
  //      QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      QAbstractSocket::SocketType socketType,
      const QNetworkProxy &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSocks5SocketEngineHandlerCall0 call = reinterpret_cast<CuteQSocks5SocketEngineHandlerCall0>(taken[0]);
      void * given = call(this, static_cast<int>(socketType), &a1, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return QSocks5SocketEngineHandler::createSocketEngine(socketType, a1, parent);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  QAbstractSocketEngine
  //      *QSocks5SocketEngineHandler::createSocketEngine(qintptr
  //      socketDescriptor, QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      qintptr socketDescriptor,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSocks5SocketEngineHandlerCall1 call = reinterpret_cast<CuteQSocks5SocketEngineHandlerCall1>(taken[1]);
      void * given = call(this, socketDescriptor, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return QSocks5SocketEngineHandler::createSocketEngine(socketDescriptor, parent);
  }
#endif  // QT_CONFIG(socks5)
};

//  QAbstractSocketEngine *QSocks5SocketEngineHandler::createSocketEngine(QAb
//      stractSocket::SocketType socketType, const QNetworkProxy &a1, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN26QSocks5SocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject(
    QSocks5SocketEngineHandler *self,
    QAbstractSocket::SocketType socketType,
    const QNetworkProxy *a1,
    QObject *parent) {
  return self->createSocketEngine(socketType, *a1, parent);
}

//  QAbstractSocketEngine
//      *QSocks5SocketEngineHandler::createSocketEngine(qintptr
//      socketDescriptor, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN26QSocks5SocketEngineHandler18createSocketEngineExP7QObject(
    QSocks5SocketEngineHandler *self,
    qintptr socketDescriptor,
    QObject *parent) {
  return self->createSocketEngine(socketDescriptor, parent);
}

//  QSocks5SocketEngineHandler::~QSocks5SocketEngineHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSocks5SocketEngineHandlerD1Ev(
    QSocks5SocketEngineHandler *self) {
  delete self;
}

//  a Python function taken by a CuteQSocks5SocketEngineHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSocks5SocketEngineHandler(
    QSocks5SocketEngineHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSocks5SocketEngineHandler *>(self)->take(key, call);
}

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
