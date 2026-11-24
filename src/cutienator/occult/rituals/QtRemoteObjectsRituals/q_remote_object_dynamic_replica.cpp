//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectdynamicreplica.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRemoteObjectDynamicReplica that Python can take functions over in. Every QRemoteObjectDynamicReplica
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectDynamicReplicaCall0)(const void *, QRemoteObjectNode *, int *);
typedef void (*CuteQRemoteObjectDynamicReplicaCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectDynamicReplicaCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectDynamicReplicaCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectDynamicReplicaCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectDynamicReplicaCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectDynamicReplicaCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectDynamicReplicaCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectDynamicReplicaCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectDynamicReplica : public QRemoteObjectDynamicReplica {
public:
  using QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica;
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
      CuteQRemoteObjectDynamicReplicaCall0 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall0>(taken[0]);
      call(this, node, &handled);
      if (handled) return;
    }
    QRemoteObjectReplica::setNode(node);
  }

  //  void QRemoteObjectReplica::initialize()
  void initialize() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectDynamicReplicaCall1 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall1>(taken[1]);
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
      CuteQRemoteObjectDynamicReplicaCall2 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall2>(taken[2]);
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
      CuteQRemoteObjectDynamicReplicaCall3 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall3>(taken[3]);
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
      CuteQRemoteObjectDynamicReplicaCall4 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall4>(taken[4]);
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
      CuteQRemoteObjectDynamicReplicaCall5 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall5>(taken[5]);
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
      CuteQRemoteObjectDynamicReplicaCall6 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall6>(taken[6]);
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
      CuteQRemoteObjectDynamicReplicaCall7 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall7>(taken[7]);
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
      CuteQRemoteObjectDynamicReplicaCall8 call = reinterpret_cast<CuteQRemoteObjectDynamicReplicaCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRemoteObjectDynamicReplica::~QRemoteObjectDynamicReplica()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRemoteObjectDynamicReplicaD1Ev(
    QRemoteObjectDynamicReplica *self) {
  delete self;
}

//  const QMetaObject *QRemoteObjectDynamicReplica::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QRemoteObjectDynamicReplica10metaObjectEv(
    const QRemoteObjectDynamicReplica *self) {
  return self->metaObject();
}

//  QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica()
extern "C" Q_DECL_EXPORT
QRemoteObjectDynamicReplica *ritual_ZN27QRemoteObjectDynamicReplicaC1Ev() {
  return new CuteQRemoteObjectDynamicReplica();
}

//  QRemoteObjectDynamicReplica::QRemoteObjectDynamicReplica(QRemoteObjectNod
//      e *node, const QString &name)
extern "C" Q_DECL_EXPORT
QRemoteObjectDynamicReplica *ritual_ZN27QRemoteObjectDynamicReplicaC1EP17QRemoteObjectNodeRK7QString(
    QRemoteObjectNode *node,
    const QString *name) {
  return new CuteQRemoteObjectDynamicReplica(node, *name);
}

//  a Python function taken by a CuteQRemoteObjectDynamicReplica, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectDynamicReplica(
    QRemoteObjectDynamicReplica *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectDynamicReplica *>(self)->take(key, call);
}
