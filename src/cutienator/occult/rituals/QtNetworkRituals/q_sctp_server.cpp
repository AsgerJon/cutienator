//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsctpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
#include <QtNetwork/qsctpserver.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSctpServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSctpServer : QSctpServer {
  using QSctpServer::incomingConnection;
};

//  A QSctpServer that Python can take functions over in. Every QSctpServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
typedef void (*CuteQSctpServerCall0)(const void *, qintptr, int *);
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
typedef bool (*CuteQSctpServerCall1)(const void *, int *);
typedef void * (*CuteQSctpServerCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSctpServerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSctpServerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpServerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpServerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpServerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpServerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSctpServer : public QSctpServer {
public:
  using QSctpServer::QSctpServer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN10QTcpServer18incomingConnectionEx")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK10QTcpServer21hasPendingConnectionsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTcpServer21nextPendingConnectionEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
  //  void QSctpServer::incomingConnection(qintptr handle)
  void incomingConnection(qintptr handle) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSctpServerCall0 call = reinterpret_cast<CuteQSctpServerCall0>(taken[0]);
      call(this, handle, &handled);
      if (handled) return;
    }
    QSctpServer::incomingConnection(handle);
  }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)

  //  bool QTcpServer::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSctpServerCall1 call = reinterpret_cast<CuteQSctpServerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTcpServer::hasPendingConnections();
  }

  //  QTcpSocket *QTcpServer::nextPendingConnection()
  QTcpSocket *nextPendingConnection() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSctpServerCall2 call = reinterpret_cast<CuteQSctpServerCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTcpSocket *>(given);
    }
    return QTcpServer::nextPendingConnection();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSctpServerCall3 call = reinterpret_cast<CuteQSctpServerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSctpServerCall4 call = reinterpret_cast<CuteQSctpServerCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSctpServerCall5 call = reinterpret_cast<CuteQSctpServerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSctpServerCall6 call = reinterpret_cast<CuteQSctpServerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSctpServerCall7 call = reinterpret_cast<CuteQSctpServerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSctpServerCall8 call = reinterpret_cast<CuteQSctpServerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSctpServerCall9 call = reinterpret_cast<CuteQSctpServerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSctpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QSctpServer10metaObjectEv(
    const QSctpServer *self) {
  return self->metaObject();
}

//  QString QSctpServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QSctpServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSctpServer::tr(s, c, n));
}

//  QSctpServer::QSctpServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QSctpServer *ritual_ZN11QSctpServerC1EP7QObject(QObject *parent) {
  return new CuteQSctpServer(parent);
}

//  QSctpServer::~QSctpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpServerD1Ev(QSctpServer *self) {
  delete self;
}

//  void QSctpServer::setMaximumChannelCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpServer22setMaximumChannelCountEi(
    QSctpServer *self,
    int count) {
  self->setMaximumChannelCount(count);
}

//  int QSctpServer::maximumChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSctpServer19maximumChannelCountEv(const QSctpServer *self) {
  return self->maximumChannelCount();
}

//  QSctpSocket *QSctpServer::nextPendingDatagramConnection()
extern "C" Q_DECL_EXPORT
QSctpSocket *ritual_ZN11QSctpServer29nextPendingDatagramConnectionEv(
    QSctpServer *self) {
  return self->nextPendingDatagramConnection();
}

//  void QSctpServer::incomingConnection(qintptr handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpServer18incomingConnectionEx(
    QSctpServer *self,
    qintptr handle) {
  self->incomingConnection(handle);
}

//  QSctpServerPrivate *QSctpServer::d_func()
extern "C" Q_DECL_EXPORT
QSctpServerPrivate *ritual_ZN11QSctpServer6d_funcEv(QSctpServer *self) {
  return self->d_func();
}

//  const QSctpServerPrivate *QSctpServer::d_func() const
extern "C" Q_DECL_EXPORT
const QSctpServerPrivate *ritual_ZNK11QSctpServer6d_funcEv(
    const QSctpServer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSctpServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSctpServer(
    QSctpServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSctpServer *>(self)->take(key, call);
}

//  void QSctpServer::incomingConnection(qintptr handle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSctpServer18incomingConnectionEx(
    QSctpServer *self,
    qintptr handle) {
  static_cast<OwnQSctpServer *>(self)->OwnQSctpServer::incomingConnection(
      handle);
}

#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
