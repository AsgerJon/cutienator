//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugserver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlDebugServer that Python can take functions over in. Every QQmlDebugServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlDebugServerCall0)(const void *, QIODevice *, int *);
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugServerCall1)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void * (*CuteQQmlDebugServerCall2)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlDebugServerCall3)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlDebugServerCall4)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugServerCall5)(const void *, QJSEngine *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugServerCall6)(const void *, const QString *, QQmlDebugService *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQQmlDebugServerCall7)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServerCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServerCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDebugServer : public QQmlDebugServer {
public:
  using QQmlDebugServer::QQmlDebugServer;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQmlDebugServer9setDeviceEP9QIODevice")) {
      taken[0] = call;
      return true;
    }
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector12blockingModeEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector7serviceERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector9addEngineEP9QJSEngine")) {
      taken[3] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector12removeEngineEP9QJSEngine")) {
      taken[4] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK18QQmlDebugConnector9hasEngineEP9QJSEngine")) {
      taken[5] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector10addServiceERK7QStringP16QQmlDebugService")) {
      taken[6] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN18QQmlDebugConnector13removeServiceERK7QString")) {
      taken[7] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQmlDebugServer::setDevice(QIODevice *socket)
  void setDevice(QIODevice *socket) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugServerCall0 call = reinterpret_cast<CuteQQmlDebugServerCall0>(taken[0]);
      call(this, socket, &handled);
      if (handled) return;
    }
  }

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::blockingMode() const
  bool blockingMode() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugServerCall1 call = reinterpret_cast<CuteQQmlDebugServerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  QQmlDebugService *QQmlDebugConnector::service(const QString &name)
  //      const
  QQmlDebugService *service(const QString &name) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDebugServerCall2 call = reinterpret_cast<CuteQQmlDebugServerCall2>(taken[2]);
      void * given = call(this, &name, &handled);
      if (handled) return static_cast<QQmlDebugService *>(given);
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlDebugConnector::addEngine(QJSEngine *engine)
  void addEngine(QJSEngine *engine) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDebugServerCall3 call = reinterpret_cast<CuteQQmlDebugServerCall3>(taken[3]);
      call(this, engine, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlDebugConnector::removeEngine(QJSEngine *engine)
  void removeEngine(QJSEngine *engine) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDebugServerCall4 call = reinterpret_cast<CuteQQmlDebugServerCall4>(taken[4]);
      call(this, engine, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::hasEngine(QJSEngine *engine) const
  bool hasEngine(QJSEngine *engine) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDebugServerCall5 call = reinterpret_cast<CuteQQmlDebugServerCall5>(taken[5]);
      bool given = call(this, engine, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::addService(const QString &name,
  //      QQmlDebugService *service)
  bool addService(const QString &name, QQmlDebugService *service) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDebugServerCall6 call = reinterpret_cast<CuteQQmlDebugServerCall6>(taken[6]);
      bool given = call(this, &name, service, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  bool QQmlDebugConnector::removeService(const QString &name)
  bool removeService(const QString &name) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDebugServerCall7 call = reinterpret_cast<CuteQQmlDebugServerCall7>(taken[7]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDebugServerCall8 call = reinterpret_cast<CuteQQmlDebugServerCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDebugServerCall9 call = reinterpret_cast<CuteQQmlDebugServerCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlDebugServerCall10 call = reinterpret_cast<CuteQQmlDebugServerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlDebugServerCall11 call = reinterpret_cast<CuteQQmlDebugServerCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlDebugServerCall12 call = reinterpret_cast<CuteQQmlDebugServerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlDebugServerCall13 call = reinterpret_cast<CuteQQmlDebugServerCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlDebugServerCall14 call = reinterpret_cast<CuteQQmlDebugServerCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDebugServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlDebugServer10metaObjectEv(
    const QQmlDebugServer *self) {
  return self->metaObject();
}

//  QString QQmlDebugServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlDebugServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDebugServer::tr(s, c, n));
}

//  QQmlDebugServer::~QQmlDebugServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlDebugServerD1Ev(QQmlDebugServer *self) {
  delete self;
}

//  void QQmlDebugServer::setDevice(QIODevice *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlDebugServer9setDeviceEP9QIODevice(
    QQmlDebugServer *self,
    QIODevice *socket) {
  self->setDevice(socket);
}

//  a Python function taken by a CuteQQmlDebugServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugServer(
    QQmlDebugServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugServer *>(self)->take(key, call);
}
