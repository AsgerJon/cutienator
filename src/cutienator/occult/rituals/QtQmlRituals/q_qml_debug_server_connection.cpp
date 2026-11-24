//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugserverconnection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugserverconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlDebugServerConnection that Python can take functions over in. Every QQmlDebugServerConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlDebugServerConnectionCall0)(const void *, QQmlDebugServer *, int *);
typedef bool (*CuteQQmlDebugServerConnectionCall1)(const void *, int, int, bool, const QString *, int *);
typedef bool (*CuteQQmlDebugServerConnectionCall2)(const void *, const QString *, bool, int *);
typedef bool (*CuteQQmlDebugServerConnectionCall3)(const void *, int *);
typedef void (*CuteQQmlDebugServerConnectionCall4)(const void *, int *);
typedef void (*CuteQQmlDebugServerConnectionCall5)(const void *, int *);
typedef void (*CuteQQmlDebugServerConnectionCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServerConnectionCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServerConnectionCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerConnectionCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerConnectionCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerConnectionCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerConnectionCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServerConnectionCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDebugServerConnection : public QQmlDebugServerConnection {
public:
  using QQmlDebugServerConnection::QQmlDebugServerConnection;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection9setServerEP15QQmlDebugServer")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection12setPortRangeEiibRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection11setFileNameERK7QStringb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QQmlDebugServerConnection11isConnectedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection10disconnectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection17waitForConnectionEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQmlDebugServerConnection5flushEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQmlDebugServerConnection::setServer(QQmlDebugServer *server)
  void setServer(QQmlDebugServer *server) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall0 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall0>(taken[0]);
      call(this, server, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlDebugServerConnection::setPortRange(int portFrom, int
  //      portTo, bool block, const QString &hostaddress)
  bool setPortRange(
      int portFrom,
      int portTo,
      bool block,
      const QString &hostaddress) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall1 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall1>(taken[1]);
      bool given = call(this, portFrom, portTo, block, &hostaddress, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QQmlDebugServerConnection::setFileName(const QString &fileName,
  //      bool block)
  bool setFileName(const QString &fileName, bool block) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall2 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall2>(taken[2]);
      bool given = call(this, &fileName, block, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QQmlDebugServerConnection::isConnected() const
  bool isConnected() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall3 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlDebugServerConnection::disconnect()
  void disconnect() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall4 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDebugServerConnection::waitForConnection()
  void waitForConnection() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall5 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QQmlDebugServerConnection::flush()
  void flush() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall6 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall7 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall8 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall9 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall10 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall11 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall12 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlDebugServerConnectionCall13 call = reinterpret_cast<CuteQQmlDebugServerConnectionCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDebugServerConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQmlDebugServerConnection10metaObjectEv(
    const QQmlDebugServerConnection *self) {
  return self->metaObject();
}

//  QString QQmlDebugServerConnection::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQmlDebugServerConnection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDebugServerConnection::tr(s, c, n));
}

//  QQmlDebugServerConnection::~QQmlDebugServerConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugServerConnectionD1Ev(
    QQmlDebugServerConnection *self) {
  delete self;
}

//  void QQmlDebugServerConnection::setServer(QQmlDebugServer *server)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugServerConnection9setServerEP15QQmlDebugServer(
    QQmlDebugServerConnection *self,
    QQmlDebugServer *server) {
  self->setServer(server);
}

//  bool QQmlDebugServerConnection::setPortRange(int portFrom, int portTo,
//      bool block, const QString &hostaddress)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlDebugServerConnection12setPortRangeEiibRK7QString(
    QQmlDebugServerConnection *self,
    int portFrom,
    int portTo,
    bool block,
    const QString *hostaddress) {
  return self->setPortRange(portFrom, portTo, block, *hostaddress);
}

//  bool QQmlDebugServerConnection::setFileName(const QString &fileName, bool
//      block)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlDebugServerConnection11setFileNameERK7QStringb(
    QQmlDebugServerConnection *self,
    const QString *fileName,
    bool block) {
  return self->setFileName(*fileName, block);
}

//  bool QQmlDebugServerConnection::isConnected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlDebugServerConnection11isConnectedEv(
    const QQmlDebugServerConnection *self) {
  return self->isConnected();
}

//  void QQmlDebugServerConnection::disconnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugServerConnection10disconnectEv(
    QQmlDebugServerConnection *self) {
  self->disconnect();
}

//  void QQmlDebugServerConnection::waitForConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugServerConnection17waitForConnectionEv(
    QQmlDebugServerConnection *self) {
  self->waitForConnection();
}

//  void QQmlDebugServerConnection::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlDebugServerConnection5flushEv(
    QQmlDebugServerConnection *self) {
  self->flush();
}

//  a Python function taken by a CuteQQmlDebugServerConnection, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugServerConnection(
    QQmlDebugServerConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugServerConnection *>(self)->take(key, call);
}
