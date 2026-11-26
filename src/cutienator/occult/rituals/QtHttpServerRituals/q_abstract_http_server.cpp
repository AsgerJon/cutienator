//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qabstracthttpserver.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qtcpserver.h>
#include <QtNetwork/qlocalserver.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtHttpServer/qhttpserverconfiguration.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QAbstractHttpServer that Python can take functions over in. Every QAbstractHttpServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractHttpServerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractHttpServerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractHttpServerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractHttpServerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractHttpServerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractHttpServerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractHttpServerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractHttpServer : public QAbstractHttpServer {
public:
  using QAbstractHttpServer::QAbstractHttpServer;
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
      CuteQAbstractHttpServerCall0 call = reinterpret_cast<CuteQAbstractHttpServerCall0>(taken[0]);
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
      CuteQAbstractHttpServerCall1 call = reinterpret_cast<CuteQAbstractHttpServerCall1>(taken[1]);
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
      CuteQAbstractHttpServerCall2 call = reinterpret_cast<CuteQAbstractHttpServerCall2>(taken[2]);
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
      CuteQAbstractHttpServerCall3 call = reinterpret_cast<CuteQAbstractHttpServerCall3>(taken[3]);
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
      CuteQAbstractHttpServerCall4 call = reinterpret_cast<CuteQAbstractHttpServerCall4>(taken[4]);
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
      CuteQAbstractHttpServerCall5 call = reinterpret_cast<CuteQAbstractHttpServerCall5>(taken[5]);
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
      CuteQAbstractHttpServerCall6 call = reinterpret_cast<CuteQAbstractHttpServerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractHttpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractHttpServer10metaObjectEv(
    const QAbstractHttpServer *self) {
  return self->metaObject();
}

//  void *QAbstractHttpServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QAbstractHttpServer11qt_metacastEPKc(
    QAbstractHttpServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractHttpServer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QAbstractHttpServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractHttpServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractHttpServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractHttpServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractHttpServer::tr(s, c, n));
}

//  QAbstractHttpServer::~QAbstractHttpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractHttpServerD1Ev(QAbstractHttpServer *self) {
  delete self;
}

//  QList<quint16> QAbstractHttpServer::serverPorts() const
extern "C" Q_DECL_EXPORT
QList<quint16> *ritual_ZNK19QAbstractHttpServer11serverPortsEv(
    const QAbstractHttpServer *self) {
  return new QList<quint16>(self->serverPorts());
}

//  bool QAbstractHttpServer::bind(QTcpServer *server)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractHttpServer4bindEP10QTcpServer(
    QAbstractHttpServer *self,
    QTcpServer *server) {
  return self->bind(server);
}

//  QList<QTcpServer *> QAbstractHttpServer::servers() const
extern "C" Q_DECL_EXPORT
QList<QTcpServer *> *ritual_ZNK19QAbstractHttpServer7serversEv(
    const QAbstractHttpServer *self) {
  return new QList<QTcpServer *>(self->servers());
}

#if QT_CONFIG(localserver)
//  bool QAbstractHttpServer::bind(QLocalServer *server)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractHttpServer4bindEP12QLocalServer(
    QAbstractHttpServer *self,
    QLocalServer *server) {
  return self->bind(server);
}
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
//  QList<QLocalServer *> QAbstractHttpServer::localServers() const
extern "C" Q_DECL_EXPORT
QList<QLocalServer *> *ritual_ZNK19QAbstractHttpServer12localServersEv(
    const QAbstractHttpServer *self) {
  return new QList<QLocalServer *>(self->localServers());
}
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(ssl)
//  QHttp2Configuration QAbstractHttpServer::http2Configuration() const
extern "C" Q_DECL_EXPORT
QHttp2Configuration *ritual_ZNK19QAbstractHttpServer18http2ConfigurationEv(
    const QAbstractHttpServer *self) {
  return new QHttp2Configuration(self->http2Configuration());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QAbstractHttpServer::setHttp2Configuration(const QHttp2Configuration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractHttpServer21setHttp2ConfigurationERK19QHttp2Configuration(
    QAbstractHttpServer *self,
    const QHttp2Configuration *configuration) {
  self->setHttp2Configuration(*configuration);
}
#endif  // QT_CONFIG(ssl)

//  void QAbstractHttpServer::setConfiguration(const QHttpServerConfiguration
//      &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractHttpServer16setConfigurationERK24QHttpServerConfiguration(
    QAbstractHttpServer *self,
    const QHttpServerConfiguration *config) {
  self->setConfiguration(*config);
}

//  QHttpServerConfiguration QAbstractHttpServer::configuration() const
extern "C" Q_DECL_EXPORT
QHttpServerConfiguration *ritual_ZNK19QAbstractHttpServer13configurationEv(
    const QAbstractHttpServer *self) {
  return new QHttpServerConfiguration(self->configuration());
}

//  bool QAbstractHttpServer::handleRequest(const QHttpServerRequest
//      &request, QHttpServerResponder &responder)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractHttpServer13handleRequestERK18QHttpServerRequestR20QHttpServerResponder(
    QAbstractHttpServer *self,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  return self->handleRequest(*request, *responder);
}

//  void QAbstractHttpServer::missingHandler(const QHttpServerRequest
//      &request, QHttpServerResponder &responder)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractHttpServer14missingHandlerERK18QHttpServerRequestR20QHttpServerResponder(
    QAbstractHttpServer *self,
    const QHttpServerRequest *request,
    QHttpServerResponder *responder) {
  self->missingHandler(*request, *responder);
}

//  QAbstractHttpServerPrivate *QAbstractHttpServer::d_func()
extern "C" Q_DECL_EXPORT
QAbstractHttpServerPrivate *ritual_ZN19QAbstractHttpServer6d_funcEv(
    QAbstractHttpServer *self) {
  return self->d_func();
}

//  const QAbstractHttpServerPrivate *QAbstractHttpServer::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractHttpServerPrivate *ritual_ZNK19QAbstractHttpServer6d_funcEv(
    const QAbstractHttpServer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractHttpServer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractHttpServer(
    QAbstractHttpServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractHttpServer *>(self)->take(key, call);
}

//  a QList<quint16> a ritual of QAbstractHttpServer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractHttpServer__QList_quint16(QList<quint16> *self) {
  delete self;
}
