//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>

//  A QSocketEngineHandler that Python can take functions over in. Every QSocketEngineHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSocketEngineHandlerCall0)(const void *, int, const QNetworkProxy *, QObject *, int *);
typedef void * (*CuteQSocketEngineHandlerCall1)(const void *, qintptr, QObject *, int *);
class CuteQSocketEngineHandler : public QSocketEngineHandler {
public:
  using QSocketEngineHandler::QSocketEngineHandler;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSocketEngineHandler18createSocketEngineExP7QObject")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QAbstractSocketEngine
  //      *QSocketEngineHandler::createSocketEngine(QAbstractSocket::Socket
  //      Type socketType, const QNetworkProxy &a1, QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      QAbstractSocket::SocketType socketType,
      const QNetworkProxy &a1,
      QObject *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSocketEngineHandlerCall0 call = reinterpret_cast<CuteQSocketEngineHandlerCall0>(taken[0]);
      void * given = call(this, static_cast<int>(socketType), &a1, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return {};
  }

  //  QAbstractSocketEngine
  //      *QSocketEngineHandler::createSocketEngine(qintptr
  //      socketDescriptor, QObject *parent)
  QAbstractSocketEngine *createSocketEngine(
      qintptr socketDescriptor,
      QObject *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSocketEngineHandlerCall1 call = reinterpret_cast<CuteQSocketEngineHandlerCall1>(taken[1]);
      void * given = call(this, socketDescriptor, parent, &handled);
      if (handled) return static_cast<QAbstractSocketEngine *>(given);
    }
    return {};
  }
};

//  QSocketEngineHandler::~QSocketEngineHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSocketEngineHandlerD1Ev(QSocketEngineHandler *self) {
  delete self;
}

//  QAbstractSocketEngine
//      *QSocketEngineHandler::createSocketEngine(QAbstractSocket::SocketType
//      socketType, const QNetworkProxy &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN20QSocketEngineHandler18createSocketEngineEN15QAbstractSocket10SocketTypeERK13QNetworkProxyP7QObject(
    QSocketEngineHandler *self,
    QAbstractSocket::SocketType socketType,
    const QNetworkProxy *a1,
    QObject *parent) {
  return self->createSocketEngine(socketType, *a1, parent);
}

//  QAbstractSocketEngine *QSocketEngineHandler::createSocketEngine(qintptr
//      socketDescriptor, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN20QSocketEngineHandler18createSocketEngineExP7QObject(
    QSocketEngineHandler *self,
    qintptr socketDescriptor,
    QObject *parent) {
  return self->createSocketEngine(socketDescriptor, parent);
}

//  a Python function taken by a CuteQSocketEngineHandler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSocketEngineHandler(
    QSocketEngineHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSocketEngineHandler *>(self)->take(key, call);
}
