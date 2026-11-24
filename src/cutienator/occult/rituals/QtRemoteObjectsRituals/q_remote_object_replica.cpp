//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectreplica.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectreplica.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QRemoteObjectReplica may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectReplica : QRemoteObjectReplica {
  using QRemoteObjectReplica::initialize;
};

//  A QRemoteObjectReplica that Python can take functions over in. Every QRemoteObjectReplica
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectReplicaCall0)(const void *, QRemoteObjectNode *, int *);
typedef void (*CuteQRemoteObjectReplicaCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectReplicaCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectReplicaCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectReplicaCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectReplica : public QRemoteObjectReplica {
public:
  using QRemoteObjectReplica::QRemoteObjectReplica;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica10initializeEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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

  //  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
  void setNode(QRemoteObjectNode *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall0 call = reinterpret_cast<CuteQRemoteObjectReplicaCall0>(taken[0]);
      call(this, node, &handled);
      if (handled) return;
    }
    QRemoteObjectReplica::setNode(node);
  }

  //  void QRemoteObjectReplica::initialize()
  void initialize() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall1 call = reinterpret_cast<CuteQRemoteObjectReplicaCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QRemoteObjectReplica::initialize();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall2 call = reinterpret_cast<CuteQRemoteObjectReplicaCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall3 call = reinterpret_cast<CuteQRemoteObjectReplicaCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall4 call = reinterpret_cast<CuteQRemoteObjectReplicaCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRemoteObjectReplicaCall5 call = reinterpret_cast<CuteQRemoteObjectReplicaCall5>(taken[5]);
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
      CuteQRemoteObjectReplicaCall6 call = reinterpret_cast<CuteQRemoteObjectReplicaCall6>(taken[6]);
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
      CuteQRemoteObjectReplicaCall7 call = reinterpret_cast<CuteQRemoteObjectReplicaCall7>(taken[7]);
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
      CuteQRemoteObjectReplicaCall8 call = reinterpret_cast<CuteQRemoteObjectReplicaCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectReplica::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QRemoteObjectReplica10metaObjectEv(
    const QRemoteObjectReplica *self) {
  return self->metaObject();
}

//  QString QRemoteObjectReplica::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QRemoteObjectReplica2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectReplica::tr(s, c, n));
}

//  QRemoteObjectReplica::~QRemoteObjectReplica()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplicaD1Ev(QRemoteObjectReplica *self) {
  delete self;
}

//  bool QRemoteObjectReplica::isReplicaValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRemoteObjectReplica14isReplicaValidEv(
    const QRemoteObjectReplica *self) {
  return self->isReplicaValid();
}

//  bool QRemoteObjectReplica::waitForSource(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QRemoteObjectReplica13waitForSourceEi(
    QRemoteObjectReplica *self,
    int timeout) {
  return self->waitForSource(timeout);
}

//  bool QRemoteObjectReplica::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRemoteObjectReplica13isInitializedEv(
    const QRemoteObjectReplica *self) {
  return self->isInitialized();
}

//  State QRemoteObjectReplica::state() const
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica::State ritual_ZNK20QRemoteObjectReplica5stateEv(
    const QRemoteObjectReplica *self) {
  return self->state();
}

//  QRemoteObjectNode *QRemoteObjectReplica::node() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZNK20QRemoteObjectReplica4nodeEv(
    const QRemoteObjectReplica *self) {
  return self->node();
}

//  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode(
    QRemoteObjectReplica *self,
    QRemoteObjectNode *node) {
  self->setNode(node);
}

//  QRemoteObjectReplica::QRemoteObjectReplica(ConstructorType t)
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica *ritual_ZN20QRemoteObjectReplicaC1ENS_15ConstructorTypeE(
    QRemoteObjectReplica::ConstructorType t) {
  return new CuteQRemoteObjectReplica(t);
}

//  void QRemoteObjectReplica::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplica10initializeEv(
    QRemoteObjectReplica *self) {
  self->initialize();
}

//  void QRemoteObjectReplica::send(QMetaObject::Call call, int index, const
//      QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplica4sendEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QRemoteObjectReplica *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  self->send(call, index, *args);
}

//  QRemoteObjectPendingCall
//      QRemoteObjectReplica::sendWithReply(QMetaObject::Call call, int
//      index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN20QRemoteObjectReplica13sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QRemoteObjectReplica *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  return new QRemoteObjectPendingCall(
      self->sendWithReply(
          call,
          index,
          *args));
}

//  void QRemoteObjectReplica::setChild(int i, const QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplica8setChildEiRK8QVariant(
    QRemoteObjectReplica *self,
    int i,
    const QVariant *a1) {
  self->setChild(i, *a1);
}

//  const QVariant QRemoteObjectReplica::propAsVariant(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QRemoteObjectReplica13propAsVariantEi(
    const QRemoteObjectReplica *self,
    int i) {
  return new QVariant(self->propAsVariant(i));
}

//  void QRemoteObjectReplica::persistProperties(const QString &repName,
//      const QByteArray &repSig, const QVariantList &props) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QRemoteObjectReplica17persistPropertiesERK7QStringRK10QByteArrayRK5QListI8QVariantE(
    const QRemoteObjectReplica *self,
    const QString *repName,
    const QByteArray *repSig,
    const QList<QVariant> *props) {
  self->persistProperties(*repName, *repSig, *props);
}

//  QVariantList QRemoteObjectReplica::retrieveProperties(const QString
//      &repName, const QByteArray &repSig) const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK20QRemoteObjectReplica18retrievePropertiesERK7QStringRK10QByteArray(
    const QRemoteObjectReplica *self,
    const QString *repName,
    const QByteArray *repSig) {
  return new QList<QVariant>(self->retrieveProperties(*repName, *repSig));
}

//  void QRemoteObjectReplica::initializeNode(QRemoteObjectNode *node, const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectReplica14initializeNodeEP17QRemoteObjectNodeRK7QString(
    QRemoteObjectReplica *self,
    QRemoteObjectNode *node,
    const QString *name) {
  self->initializeNode(node, *name);
}

//  a Python function taken by a CuteQRemoteObjectReplica, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectReplica(
    QRemoteObjectReplica *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectReplica *>(self)->take(key, call);
}

//  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode(
    QRemoteObjectReplica *self,
    QRemoteObjectNode *node) {
  self->QRemoteObjectReplica::setNode(node);
}

//  void QRemoteObjectReplica::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectReplica10initializeEv(
    QRemoteObjectReplica *self) {
  static_cast<OwnQRemoteObjectReplica *>(self)->OwnQRemoteObjectReplica::initialize();
}
