//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRemoteObjectHostBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectHostBase : QRemoteObjectHostBase {
  using QRemoteObjectHostBase::hostUrl;
  using QRemoteObjectHostBase::setHostUrl;
};

//  A QRemoteObjectHostBase that Python can take functions over in. Every QRemoteObjectHostBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectHostBaseCall0)(const void *, const QString *, int *);
typedef const QUrl * (*CuteQRemoteObjectHostBaseCall1)(const void *, int *);
typedef bool (*CuteQRemoteObjectHostBaseCall2)(const void *, const QUrl *, int, int *);
typedef bool (*CuteQRemoteObjectHostBaseCall3)(const void *, const QUrl *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostBaseCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectHostBaseCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectHostBaseCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostBaseCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostBaseCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostBaseCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectHostBaseCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectHostBase : public QRemoteObjectHostBase {
public:
  using QRemoteObjectHostBase::QRemoteObjectHostBase;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode7setNameERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QRemoteObjectHostBase7hostUrlEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchemasE")) {
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

  //  void QRemoteObjectHostBase::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectHostBaseCall0 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall0>(taken[0]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QRemoteObjectHostBase::setName(name);
  }

  //  QUrl QRemoteObjectHostBase::hostUrl() const
  QUrl hostUrl() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectHostBaseCall1 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectHostBaseCall2 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall2>(taken[2]);
      bool given = call(this, &hostAddress, static_cast<int>(allowedSchemas), &handled);
      if (handled) return given;
    }
    return QRemoteObjectHostBase::setHostUrl(hostAddress, allowedSchemas);
  }

  //  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
  bool setRegistryUrl(const QUrl &registryAddress) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectHostBaseCall3 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall3>(taken[3]);
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
      CuteQRemoteObjectHostBaseCall4 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall4>(taken[4]);
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
      CuteQRemoteObjectHostBaseCall5 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall5>(taken[5]);
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
      CuteQRemoteObjectHostBaseCall6 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall6>(taken[6]);
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
      CuteQRemoteObjectHostBaseCall7 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall7>(taken[7]);
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
      CuteQRemoteObjectHostBaseCall8 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall8>(taken[8]);
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
      CuteQRemoteObjectHostBaseCall9 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall9>(taken[9]);
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
      CuteQRemoteObjectHostBaseCall10 call = reinterpret_cast<CuteQRemoteObjectHostBaseCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectHostBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QRemoteObjectHostBase10metaObjectEv(
    const QRemoteObjectHostBase *self) {
  return self->metaObject();
}

//  QString QRemoteObjectHostBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QRemoteObjectHostBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectHostBase::tr(s, c, n));
}

//  QRemoteObjectHostBase::~QRemoteObjectHostBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectHostBaseD1Ev(QRemoteObjectHostBase *self) {
  delete self;
}

//  void QRemoteObjectHostBase::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectHostBase7setNameERK7QString(
    QRemoteObjectHostBase *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QRemoteObjectHostBase::enableRemoting(QObject *object, const QString
//      &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRemoteObjectHostBase14enableRemotingEP7QObjectRK7QString(
    QRemoteObjectHostBase *self,
    QObject *object,
    const QString *name) {
  return self->enableRemoting(object, *name);
}

//  bool QRemoteObjectHostBase::disableRemoting(QObject *remoteObject)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRemoteObjectHostBase15disableRemotingEP7QObject(
    QRemoteObjectHostBase *self,
    QObject *remoteObject) {
  return self->disableRemoting(remoteObject);
}

//  void QRemoteObjectHostBase::addHostSideConnection(QIODevice *ioDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectHostBase21addHostSideConnectionEP9QIODevice(
    QRemoteObjectHostBase *self,
    QIODevice *ioDevice) {
  self->addHostSideConnection(ioDevice);
}

//  QUrl QRemoteObjectHostBase::hostUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QRemoteObjectHostBase7hostUrlEv(
    const QRemoteObjectHostBase *self) {
  return new QUrl(self->hostUrl());
}

//  bool QRemoteObjectHostBase::setHostUrl(const QUrl &hostAddress,
//      AllowedSchemas allowedSchemas)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchemasE(
    QRemoteObjectHostBase *self,
    const QUrl *hostAddress,
    QRemoteObjectHostBase::AllowedSchemas allowedSchemas) {
  return self->setHostUrl(*hostAddress, allowedSchemas);
}

//  bool QRemoteObjectHostBase::enableRemoting(QObject *object, const
//      SourceApiMap *a1, QObject *adapter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QRemoteObjectHostBase14enableRemotingEP7QObjectPK12SourceApiMapS1_(
    QRemoteObjectHostBase *self,
    QObject *object,
    const SourceApiMap *a1,
    QObject *adapter) {
  return self->enableRemoting(object, a1, adapter);
}

//  QRemoteObjectHostBasePrivate *QRemoteObjectHostBase::d_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHostBasePrivate *ritual_ZN21QRemoteObjectHostBase6d_funcEv(
    QRemoteObjectHostBase *self) {
  return self->d_func();
}

//  const QRemoteObjectHostBasePrivate *QRemoteObjectHostBase::d_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHostBasePrivate *ritual_ZNK21QRemoteObjectHostBase6d_funcEv(
    const QRemoteObjectHostBase *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRemoteObjectHostBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHostBase(
    QRemoteObjectHostBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHostBase *>(self)->take(key, call);
}

//  void QRemoteObjectHostBase::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRemoteObjectHostBase7setNameERK7QString(
    QRemoteObjectHostBase *self,
    const QString *name) {
  self->QRemoteObjectHostBase::setName(*name);
}

//  QUrl QRemoteObjectHostBase::hostUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK21QRemoteObjectHostBase7hostUrlEv(
    const QRemoteObjectHostBase *self) {
  return new QUrl(
      static_cast<const OwnQRemoteObjectHostBase *>(self)->OwnQRemoteObjectHostBase::hostUrl());
}

//  bool QRemoteObjectHostBase::setHostUrl(const QUrl &hostAddress,
//      AllowedSchemas allowedSchemas)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QRemoteObjectHostBase10setHostUrlERK4QUrlNS_14AllowedSchemasE(
    QRemoteObjectHostBase *self,
    const QUrl *hostAddress,
    QRemoteObjectHostBase::AllowedSchemas allowedSchemas) {
  return static_cast<OwnQRemoteObjectHostBase *>(self)->OwnQRemoteObjectHostBase::setHostUrl(
      *hostAddress,
      allowedSchemas);
}
