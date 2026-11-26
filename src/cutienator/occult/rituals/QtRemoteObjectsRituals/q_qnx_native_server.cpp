//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnection_qnx_server.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#if defined(Q_OS_QNX)
#include <QtRemoteObjects/QtRemoteObjects>
#include <QtRemoteObjects/qconnection_qnx_server.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtRemoteObjects/QIOQnxSource>

//  A QQnxNativeServer that Python can take functions over in. Every QQnxNativeServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxNativeServerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxNativeServerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeServerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeServerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeServerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeServerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeServerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQnxNativeServer : public QQnxNativeServer {
public:
  using QQnxNativeServer::QQnxNativeServer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQnxNativeServerCall0 call = reinterpret_cast<CuteQQnxNativeServerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQnxNativeServerCall1 call = reinterpret_cast<CuteQQnxNativeServerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQnxNativeServerCall2 call = reinterpret_cast<CuteQQnxNativeServerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQnxNativeServerCall3 call = reinterpret_cast<CuteQQnxNativeServerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQnxNativeServerCall4 call = reinterpret_cast<CuteQQnxNativeServerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQnxNativeServerCall5 call = reinterpret_cast<CuteQQnxNativeServerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQnxNativeServerCall6 call = reinterpret_cast<CuteQQnxNativeServerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQnxNativeServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQnxNativeServer10metaObjectEv(
    const QQnxNativeServer *self) {
  return self->metaObject();
}

//  void *QQnxNativeServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQnxNativeServer11qt_metacastEPKc(
    QQnxNativeServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQnxNativeServer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQnxNativeServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQnxNativeServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQnxNativeServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQnxNativeServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQnxNativeServer::tr(s, c, n));
}

//  QQnxNativeServerPrivate *QQnxNativeServer::d_func()
extern "C" Q_DECL_EXPORT
QQnxNativeServerPrivate *ritual_ZN16QQnxNativeServer6d_funcEv(
    QQnxNativeServer *self) {
  return self->d_func();
}

//  const QQnxNativeServerPrivate *QQnxNativeServer::d_func() const
extern "C" Q_DECL_EXPORT
const QQnxNativeServerPrivate *ritual_ZNK16QQnxNativeServer6d_funcEv(
    const QQnxNativeServer *self) {
  return self->d_func();
}

//  void QQnxNativeServer::newConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQnxNativeServer13newConnectionEv(QQnxNativeServer *self) {
  self->newConnection();
}

//  QQnxNativeServer::QQnxNativeServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QQnxNativeServer *ritual_ZN16QQnxNativeServerC1EP7QObject(QObject *parent) {
  return new CuteQQnxNativeServer(parent);
}

//  QQnxNativeServer::~QQnxNativeServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQnxNativeServerD1Ev(QQnxNativeServer *self) {
  delete self;
}

//  void QQnxNativeServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQnxNativeServer5closeEv(QQnxNativeServer *self) {
  self->close();
}

//  bool QQnxNativeServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQnxNativeServer21hasPendingConnectionsEv(
    const QQnxNativeServer *self) {
  return self->hasPendingConnections();
}

//  bool QQnxNativeServer::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQnxNativeServer11isListeningEv(
    const QQnxNativeServer *self) {
  return self->isListening();
}

//  bool QQnxNativeServer::listen(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQnxNativeServer6listenERK7QString(
    QQnxNativeServer *self,
    const QString *name) {
  return self->listen(*name);
}

//  QSharedPointer<QIOQnxSource> QQnxNativeServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QSharedPointer<QIOQnxSource> *ritual_ZN16QQnxNativeServer21nextPendingConnectionEv(
    QQnxNativeServer *self) {
  return new QSharedPointer<QIOQnxSource>(self->nextPendingConnection());
}

//  QString QQnxNativeServer::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQnxNativeServer10serverNameEv(
    const QQnxNativeServer *self) {
  return new QString(self->serverName());
}

//  bool QQnxNativeServer::waitForNewConnection(int msec, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQnxNativeServer20waitForNewConnectionEiPb(
    QQnxNativeServer *self,
    int msec,
    bool *timedOut) {
  return self->waitForNewConnection(msec, timedOut);
}

//  void QQnxNativeServer::onSourceClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQnxNativeServer14onSourceClosedEv(QQnxNativeServer *self) {
  self->onSourceClosed();
}

//  a Python function taken by a CuteQQnxNativeServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQnxNativeServer(
    QQnxNativeServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQnxNativeServer *>(self)->take(key, call);
}

//  a QSharedPointer<QIOQnxSource> a ritual of QQnxNativeServer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQnxNativeServer__QSharedPointer_QIOQnxSource(
    QSharedPointer<QIOQnxSource> *self) {
  delete self;
}

#endif  // defined(Q_OS_QNX)
