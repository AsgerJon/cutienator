//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectnode.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qstringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QRemoteObjectNode may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectNode : QRemoteObjectNode {
  using QRemoteObjectNode::timerEvent;
};

//  A QRemoteObjectNode that Python can take functions over in. Every QRemoteObjectNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectNodeCall0)(const void *, const QString *, int *);
typedef bool (*CuteQRemoteObjectNodeCall1)(const void *, const QUrl *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectNodeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectNodeCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectNodeCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectNodeCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectNodeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectNodeCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectNodeCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectNode : public QRemoteObjectNode {
public:
  using QRemoteObjectNode::QRemoteObjectNode;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode7setNameERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QRemoteObjectNode::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall0 call = reinterpret_cast<CuteQRemoteObjectNodeCall0>(taken[0]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QRemoteObjectNode::setName(name);
  }

  //  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
  bool setRegistryUrl(const QUrl &registryAddress) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall1 call = reinterpret_cast<CuteQRemoteObjectNodeCall1>(taken[1]);
      bool given = call(this, &registryAddress, &handled);
      if (handled) return given;
    }
    return QRemoteObjectNode::setRegistryUrl(registryAddress);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall2 call = reinterpret_cast<CuteQRemoteObjectNodeCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QRemoteObjectNode::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall3 call = reinterpret_cast<CuteQRemoteObjectNodeCall3>(taken[3]);
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
      CuteQRemoteObjectNodeCall4 call = reinterpret_cast<CuteQRemoteObjectNodeCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall5 call = reinterpret_cast<CuteQRemoteObjectNodeCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall6 call = reinterpret_cast<CuteQRemoteObjectNodeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall7 call = reinterpret_cast<CuteQRemoteObjectNodeCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRemoteObjectNodeCall8 call = reinterpret_cast<CuteQRemoteObjectNodeCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QRemoteObjectNode10metaObjectEv(
    const QRemoteObjectNode *self) {
  return self->metaObject();
}

//  QString QRemoteObjectNode::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QRemoteObjectNode2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectNode::tr(s, c, n));
}

//  QRemoteObjectNode::QRemoteObjectNode(QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZN17QRemoteObjectNodeC1EP7QObject(
    QObject *parent) {
  return new CuteQRemoteObjectNode(parent);
}

//  QRemoteObjectNode::QRemoteObjectNode(const QUrl &registryAddress, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZN17QRemoteObjectNodeC1ERK4QUrlP7QObject(
    const QUrl *registryAddress,
    QObject *parent) {
  return new CuteQRemoteObjectNode(*registryAddress, parent);
}

//  QRemoteObjectNode::~QRemoteObjectNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNodeD1Ev(QRemoteObjectNode *self) {
  delete self;
}

//  bool QRemoteObjectNode::connectToNode(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QRemoteObjectNode13connectToNodeERK4QUrl(
    QRemoteObjectNode *self,
    const QUrl *address) {
  return self->connectToNode(*address);
}

//  void QRemoteObjectNode::addClientSideConnection(QIODevice *ioDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode23addClientSideConnectionEP9QIODevice(
    QRemoteObjectNode *self,
    QIODevice *ioDevice) {
  self->addClientSideConnection(ioDevice);
}

//  void QRemoteObjectNode::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode7setNameERK7QString(
    QRemoteObjectNode *self,
    const QString *name) {
  self->setName(*name);
}

//  QStringList QRemoteObjectNode::instances(QStringView typeName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QRemoteObjectNode9instancesE11QStringView(
    const QRemoteObjectNode *self,
    const QString *typeName) {
  return new QList<QString>(self->instances(QStringView(*typeName)));
}

//  QRemoteObjectDynamicReplica *QRemoteObjectNode::acquireDynamic(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QRemoteObjectDynamicReplica *ritual_ZN17QRemoteObjectNode14acquireDynamicERK7QString(
    QRemoteObjectNode *self,
    const QString *name) {
  return self->acquireDynamic(*name);
}

//  QUrl QRemoteObjectNode::registryUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QRemoteObjectNode11registryUrlEv(
    const QRemoteObjectNode *self) {
  return new QUrl(self->registryUrl());
}

//  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl(
    QRemoteObjectNode *self,
    const QUrl *registryAddress) {
  return self->setRegistryUrl(*registryAddress);
}

//  bool QRemoteObjectNode::waitForRegistry(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QRemoteObjectNode15waitForRegistryEi(
    QRemoteObjectNode *self,
    int timeout) {
  return self->waitForRegistry(timeout);
}

//  const QRemoteObjectRegistry *QRemoteObjectNode::registry() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectRegistry *ritual_ZNK17QRemoteObjectNode8registryEv(
    const QRemoteObjectNode *self) {
  return self->registry();
}

//  QRemoteObjectAbstractPersistedStore *QRemoteObjectNode::persistedStore()
//      const
extern "C" Q_DECL_EXPORT
QRemoteObjectAbstractPersistedStore *ritual_ZNK17QRemoteObjectNode14persistedStoreEv(
    const QRemoteObjectNode *self) {
  return self->persistedStore();
}

//  void
//      QRemoteObjectNode::setPersistedStore(QRemoteObjectAbstractPersistedSt
//      ore *persistedStore)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode17setPersistedStoreEP35QRemoteObjectAbstractPersistedStore(
    QRemoteObjectNode *self,
    QRemoteObjectAbstractPersistedStore *persistedStore) {
  self->setPersistedStore(persistedStore);
}

//  ErrorCode QRemoteObjectNode::lastError() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode::ErrorCode ritual_ZNK17QRemoteObjectNode9lastErrorEv(
    const QRemoteObjectNode *self) {
  return self->lastError();
}

//  int QRemoteObjectNode::heartbeatInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QRemoteObjectNode17heartbeatIntervalEv(
    const QRemoteObjectNode *self) {
  return self->heartbeatInterval();
}

//  void QRemoteObjectNode::setHeartbeatInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode20setHeartbeatIntervalEi(
    QRemoteObjectNode *self,
    int interval) {
  self->setHeartbeatInterval(interval);
}

//  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode10timerEventEP11QTimerEvent(
    QRemoteObjectNode *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QRemoteObjectNode::initializeReplica(QRemoteObjectReplica *instance,
//      const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode17initializeReplicaEP20QRemoteObjectReplicaRK7QString(
    QRemoteObjectNode *self,
    QRemoteObjectReplica *instance,
    const QString *name) {
  self->initializeReplica(instance, *name);
}

//  void QRemoteObjectNode::persistProperties(const QString &repName, const
//      QByteArray &repSig, const QVariantList &props)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QRemoteObjectNode17persistPropertiesERK7QStringRK10QByteArrayRK5QListI8QVariantE(
    QRemoteObjectNode *self,
    const QString *repName,
    const QByteArray *repSig,
    const QList<QVariant> *props) {
  self->persistProperties(*repName, *repSig, *props);
}

//  QVariantList QRemoteObjectNode::retrieveProperties(const QString
//      &repName, const QByteArray &repSig)
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZN17QRemoteObjectNode18retrievePropertiesERK7QStringRK10QByteArray(
    QRemoteObjectNode *self,
    const QString *repName,
    const QByteArray *repSig) {
  return new QList<QVariant>(self->retrieveProperties(*repName, *repSig));
}

//  QRemoteObjectNodePrivate *QRemoteObjectNode::d_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectNodePrivate *ritual_ZN17QRemoteObjectNode6d_funcEv(
    QRemoteObjectNode *self) {
  return self->d_func();
}

//  const QRemoteObjectNodePrivate *QRemoteObjectNode::d_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectNodePrivate *ritual_ZNK17QRemoteObjectNode6d_funcEv(
    const QRemoteObjectNode *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRemoteObjectNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectNode(
    QRemoteObjectNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectNode *>(self)->take(key, call);
}

//  void QRemoteObjectNode::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QRemoteObjectNode7setNameERK7QString(
    QRemoteObjectNode *self,
    const QString *name) {
  self->QRemoteObjectNode::setName(*name);
}

//  bool QRemoteObjectNode::setRegistryUrl(const QUrl &registryAddress)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QRemoteObjectNode14setRegistryUrlERK4QUrl(
    QRemoteObjectNode *self,
    const QUrl *registryAddress) {
  return self->QRemoteObjectNode::setRegistryUrl(*registryAddress);
}

//  void QRemoteObjectNode::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QRemoteObjectNode10timerEventEP11QTimerEvent(
    QRemoteObjectNode *self,
    QTimerEvent *a0) {
  static_cast<OwnQRemoteObjectNode *>(self)->OwnQRemoteObjectNode::timerEvent(
      a0);
}
