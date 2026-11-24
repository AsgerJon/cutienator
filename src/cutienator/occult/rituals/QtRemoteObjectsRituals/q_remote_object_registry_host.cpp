//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRemoteObjectRegistryHost that Python can take functions over in. Every QRemoteObjectRegistryHost
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRemoteObjectRegistryHostCall0)(const void *, const QUrl *, int *);
typedef void (*CuteQRemoteObjectRegistryHostCall1)(const void *, const QString *, int *);
typedef const QUrl * (*CuteQRemoteObjectRegistryHostCall2)(const void *, int *);
typedef bool (*CuteQRemoteObjectRegistryHostCall3)(const void *, const QUrl *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryHostCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRegistryHostCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRegistryHostCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryHostCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryHostCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryHostCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryHostCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectRegistryHost : public QRemoteObjectRegistryHost {
public:
  using QRemoteObjectRegistryHost::QRemoteObjectRegistryHost;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode7setNameERK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QRemoteObjectHostBase7hostUrlEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchemasE")) {
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

  //  bool QRemoteObjectRegistryHost::setRegistryUrl(const QUrl
  //      &registryUrl)
  bool setRegistryUrl(const QUrl &registryUrl) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectRegistryHostCall0 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall0>(taken[0]);
      bool given = call(this, &registryUrl, &handled);
      if (handled) return given;
    }
    return QRemoteObjectRegistryHost::setRegistryUrl(registryUrl);
  }

  //  void QRemoteObjectHostBase::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectRegistryHostCall1 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall1>(taken[1]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QRemoteObjectHostBase::setName(name);
  }

  //  QUrl QRemoteObjectHostBase::hostUrl() const
  QUrl hostUrl() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectRegistryHostCall2 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall2>(taken[2]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRemoteObjectHostBase::hostUrl();
  }

  //  bool QRemoteObjectHostBase::setHostUrl(const QUrl &hostAddress,
  //      AllowedSchemas allowedSchemas)
  bool setHostUrl(
      const QUrl &hostAddress,
      QRemoteObjectHostBase::AllowedSchemas allowedSchemas) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectRegistryHostCall3 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall3>(taken[3]);
      bool given = call(this, &hostAddress, static_cast<int>(allowedSchemas), &handled);
      if (handled) return given;
    }
    return QRemoteObjectHostBase::setHostUrl(hostAddress, allowedSchemas);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectRegistryHostCall4 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall4>(taken[4]);
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
      CuteQRemoteObjectRegistryHostCall5 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall5>(taken[5]);
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
      CuteQRemoteObjectRegistryHostCall6 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall6>(taken[6]);
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
      CuteQRemoteObjectRegistryHostCall7 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall7>(taken[7]);
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
      CuteQRemoteObjectRegistryHostCall8 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall8>(taken[8]);
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
      CuteQRemoteObjectRegistryHostCall9 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall9>(taken[9]);
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
      CuteQRemoteObjectRegistryHostCall10 call = reinterpret_cast<CuteQRemoteObjectRegistryHostCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectRegistryHost::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QRemoteObjectRegistryHost10metaObjectEv(
    const QRemoteObjectRegistryHost *self) {
  return self->metaObject();
}

//  QString QRemoteObjectRegistryHost::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QRemoteObjectRegistryHost2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectRegistryHost::tr(s, c, n));
}

//  QRemoteObjectRegistryHost::QRemoteObjectRegistryHost(const QUrl
//      &registryAddress, QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectRegistryHost *ritual_ZN25QRemoteObjectRegistryHostC1ERK4QUrlP7QObject(
    const QUrl *registryAddress,
    QObject *parent) {
  return new CuteQRemoteObjectRegistryHost(*registryAddress, parent);
}

//  QRemoteObjectRegistryHost::~QRemoteObjectRegistryHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRemoteObjectRegistryHostD1Ev(
    QRemoteObjectRegistryHost *self) {
  delete self;
}

//  bool QRemoteObjectRegistryHost::setRegistryUrl(const QUrl &registryUrl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QRemoteObjectRegistryHost14setRegistryUrlERK4QUrl(
    QRemoteObjectRegistryHost *self,
    const QUrl *registryUrl) {
  return self->setRegistryUrl(*registryUrl);
}

//  QRemoteObjectRegistryHostPrivate *QRemoteObjectRegistryHost::d_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectRegistryHostPrivate *ritual_ZN25QRemoteObjectRegistryHost6d_funcEv(
    QRemoteObjectRegistryHost *self) {
  return self->d_func();
}

//  const QRemoteObjectRegistryHostPrivate
//      *QRemoteObjectRegistryHost::d_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectRegistryHostPrivate *ritual_ZNK25QRemoteObjectRegistryHost6d_funcEv(
    const QRemoteObjectRegistryHost *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRemoteObjectRegistryHost, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectRegistryHost(
    QRemoteObjectRegistryHost *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectRegistryHost *>(self)->take(key, call);
}

//  bool QRemoteObjectRegistryHost::setRegistryUrl(const QUrl &registryUrl)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QRemoteObjectRegistryHost14setRegistryUrlERK4QUrl(
    QRemoteObjectRegistryHost *self,
    const QUrl *registryUrl) {
  return self->QRemoteObjectRegistryHost::setRegistryUrl(*registryUrl);
}
