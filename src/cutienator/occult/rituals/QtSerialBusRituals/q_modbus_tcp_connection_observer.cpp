//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbustcpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbustcpserver.h>
#include <cstring>

//  A QModbusTcpConnectionObserver that Python can take functions over in. Every QModbusTcpConnectionObserver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQModbusTcpConnectionObserverCall0)(const void *, QTcpSocket *, int *);
class CuteQModbusTcpConnectionObserver : public QModbusTcpConnectionObserver {
public:
  using QModbusTcpConnectionObserver::QModbusTcpConnectionObserver;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QModbusTcpConnectionObserver19acceptNewConnectionEP10QTcpSocket")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QModbusTcpConnectionObserver::acceptNewConnection(QTcpSocket
  //      *newClient)
  bool acceptNewConnection(QTcpSocket *newClient) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusTcpConnectionObserverCall0 call = reinterpret_cast<CuteQModbusTcpConnectionObserverCall0>(taken[0]);
      bool given = call(this, newClient, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QModbusTcpConnectionObserver::~QModbusTcpConnectionObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QModbusTcpConnectionObserverD1Ev(
    QModbusTcpConnectionObserver *self) {
  delete self;
}

//  bool QModbusTcpConnectionObserver::acceptNewConnection(QTcpSocket
//      *newClient)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QModbusTcpConnectionObserver19acceptNewConnectionEP10QTcpSocket(
    QModbusTcpConnectionObserver *self,
    QTcpSocket *newClient) {
  return self->acceptNewConnection(newClient);
}

//  a Python function taken by a CuteQModbusTcpConnectionObserver, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusTcpConnectionObserver(
    QModbusTcpConnectionObserver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusTcpConnectionObserver *>(self)->take(key, call);
}
