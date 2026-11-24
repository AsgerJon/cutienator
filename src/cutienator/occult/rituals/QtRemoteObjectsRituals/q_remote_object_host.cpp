//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRemoteObjectHost that Python can take functions over in. Every QRemoteObjectHost
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQRemoteObjectHostCall0)(const void *, int *);
typedef bool (*CuteQRemoteObjectHostCall1)(const void *, const QUrl *, int, int *);
typedef void (*CuteQRemoteObjectHostCall2)(const void *, const QString *, int *);
typedef bool (*CuteQRemoteObjectHostCall3)(const void *, const QUrl *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectHostCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectHostCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectHost : public QRemoteObjectHost {
public:
  using QRemoteObjectHost::QRemoteObjectHost;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QRemoteObjectHostBase7hostUrlEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchemasE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode7setNameERK7QString")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QUrl QRemoteObjectHost::hostUrl() const
  QUrl hostUrl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectHostCall0 call = reinterpret_cast<CuteQRemoteObjectHostCall0>(taken[0]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRemoteObjectHost::hostUrl();
  }

  //  bool QRemoteObjectHost::setHostUrl(const QUrl &hostAddress,
  //      AllowedSchemas allowedSchemas)
  bool setHostUrl(
      const QUrl &hostAddress,
      QRemoteObjectHostBase::AllowedSchemas allowedSchemas) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectHostCall1 call = reinterpret_cast<CuteQRemoteObjectHostCall1>(taken[1]);
      bool given = call(this, &hostAddress, static_cast<int>(allowedSchemas), &handled);
      if (handled) return given;
    }
    return QRemoteObjectHost::setHostUrl(hostAddress, allowedSchemas);
  }

  //  void QRemoteObjectHostBase::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectHostCall2 call = reinterpret_cast<CuteQRemoteObjectHostCall2>(taken[2]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QRemoteObjectHostBase::setName(name);
  }

  //  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
  bool setRegistryUrl(const QUrl &registryAddress) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectHostCall3 call = reinterpret_cast<CuteQRemoteObjectHostCall3>(taken[3]);
      bool given = call(this, &registryAddress, &handled);
      if (handled) return given;
    }
    return QRemoteObjectNode::setRegistryUrl(registryAddress);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectHostCall4 call = reinterpret_cast<CuteQRemoteObjectHostCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRemoteObjectNode::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectHostCall5 call = reinterpret_cast<CuteQRemoteObjectHostCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectHostCall6 call = reinterpret_cast<CuteQRemoteObjectHostCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectHostCall7 call = reinterpret_cast<CuteQRemoteObjectHostCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectHostCall8 call = reinterpret_cast<CuteQRemoteObjectHostCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRemoteObjectHostCall9 call = reinterpret_cast<CuteQRemoteObjectHostCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQRemoteObjectHostCall10 call = reinterpret_cast<CuteQRemoteObjectHostCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectHost::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QRemoteObjectHost10metaObjectEv(
    const QRemoteObjectHost *self) {
  return self->metaObject();
}

//  QString QRemoteObjectHost::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QRemoteObjectHost2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectHost::tr(s, c, n));
}

//  QRemoteObjectHost::QRemoteObjectHost(QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectHost *ritual_ZN17QRemoteObjectHostC1EP7QObject(
    QObject *parent) {
  return new CuteQRemoteObjectHost(parent);
}

//  QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, const QUrl
//      &registryAddress, AllowedSchemas allowedSchemas, QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectHost *ritual_ZN17QRemoteObjectHostC1ERK4QUrlS2_N21QRemoteObjectHostBase14AllowedSchemasEP7QObject(
    const QUrl *address,
    const QUrl *registryAddress,
    QRemoteObjectHostBase::AllowedSchemas allowedSchemas,
    QObject *parent) {
  return new CuteQRemoteObjectHost(
      *address,
      *registryAddress,
      allowedSchemas,
      parent);
}

//  QRemoteObjectHost::QRemoteObjectHost(const QUrl &address, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectHost *ritual_ZN17QRemoteObjectHostC1ERK4QUrlP7QObject(
    const QUrl *address,
    QObject *parent) {
  return new CuteQRemoteObjectHost(*address, parent);
}

//  QRemoteObjectHost::~QRemoteObjectHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectHostD1Ev(QRemoteObjectHost *self) {
  delete self;
}

//  QUrl QRemoteObjectHost::hostUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QRemoteObjectHost7hostUrlEv(
    const QRemoteObjectHost *self) {
  return new QUrl(self->hostUrl());
}

//  bool QRemoteObjectHost::setHostUrl(const QUrl &hostAddress,
//      AllowedSchemas allowedSchemas)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QRemoteObjectHost10setHostUrlERK4QUrlN21QRemoteObjectHostBase14AllowedSchemasE(
    QRemoteObjectHost *self,
    const QUrl *hostAddress,
    QRemoteObjectHostBase::AllowedSchemas allowedSchemas) {
  return self->setHostUrl(*hostAddress, allowedSchemas);
}

//  void QRemoteObjectHost::setLocalServerOptions(QLocalServer::SocketOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectHost21setLocalServerOptionsE6QFlagsIN12QLocalServer12SocketOptionEE(
    int options) {
  QRemoteObjectHost::setLocalServerOptions(
      QFlags<QLocalServer::SocketOption>::fromInt(options));
}

//  QRemoteObjectHostPrivate *QRemoteObjectHost::d_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHostPrivate *ritual_ZN17QRemoteObjectHost6d_funcEv(
    QRemoteObjectHost *self) {
  return self->d_func();
}

//  const QRemoteObjectHostPrivate *QRemoteObjectHost::d_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHostPrivate *ritual_ZNK17QRemoteObjectHost6d_funcEv(
    const QRemoteObjectHost *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRemoteObjectHost, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHost(
    QRemoteObjectHost *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHost *>(self)->take(key, call);
}

//  QUrl QRemoteObjectHost::hostUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK17QRemoteObjectHost7hostUrlEv(
    const QRemoteObjectHost *self) {
  return new QUrl(self->QRemoteObjectHost::hostUrl());
}

//  bool QRemoteObjectHost::setHostUrl(const QUrl &hostAddress,
//      AllowedSchemas allowedSchemas)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QRemoteObjectHost10setHostUrlERK4QUrlN21QRemoteObjectHostBase14AllowedSchemasE(
    QRemoteObjectHost *self,
    const QUrl *hostAddress,
    QRemoteObjectHostBase::AllowedSchemas allowedSchemas) {
  return self->QRemoteObjectHost::setHostUrl(*hostAddress, allowedSchemas);
}
