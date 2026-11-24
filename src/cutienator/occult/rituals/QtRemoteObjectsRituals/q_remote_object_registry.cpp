//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectregistry.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qremoteobjectregistry.h>
#include <QtCore/qstring.h>
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QRemoteObjectRegistry that Python can take functions over in. Every QRemoteObjectRegistry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRemoteObjectRegistryCall0)(const void *, int *);
typedef void (*CuteQRemoteObjectRegistryCall1)(const void *, QRemoteObjectNode *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRegistryCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectRegistryCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectRegistryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectRegistry : public QRemoteObjectRegistry {
public:
  using QRemoteObjectRegistry::QRemoteObjectRegistry;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica10initializeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRemoteObjectReplica7setNodeEP17QRemoteObjectNode")) {
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

  //  void QRemoteObjectRegistry::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectRegistryCall0 call = reinterpret_cast<CuteQRemoteObjectRegistryCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QRemoteObjectRegistry::initialize();
  }

  //  void QRemoteObjectReplica::setNode(QRemoteObjectNode *node)
  void setNode(QRemoteObjectNode *node) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRemoteObjectRegistryCall1 call = reinterpret_cast<CuteQRemoteObjectRegistryCall1>(taken[1]);
      call(this, node, &handled);
      if (handled) return;
    }
    QRemoteObjectReplica::setNode(node);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRemoteObjectRegistryCall2 call = reinterpret_cast<CuteQRemoteObjectRegistryCall2>(taken[2]);
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
      CuteQRemoteObjectRegistryCall3 call = reinterpret_cast<CuteQRemoteObjectRegistryCall3>(taken[3]);
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
      CuteQRemoteObjectRegistryCall4 call = reinterpret_cast<CuteQRemoteObjectRegistryCall4>(taken[4]);
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
      CuteQRemoteObjectRegistryCall5 call = reinterpret_cast<CuteQRemoteObjectRegistryCall5>(taken[5]);
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
      CuteQRemoteObjectRegistryCall6 call = reinterpret_cast<CuteQRemoteObjectRegistryCall6>(taken[6]);
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
      CuteQRemoteObjectRegistryCall7 call = reinterpret_cast<CuteQRemoteObjectRegistryCall7>(taken[7]);
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
      CuteQRemoteObjectRegistryCall8 call = reinterpret_cast<CuteQRemoteObjectRegistryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectRegistry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QRemoteObjectRegistry10metaObjectEv(
    const QRemoteObjectRegistry *self) {
  return self->metaObject();
}

//  QString QRemoteObjectRegistry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QRemoteObjectRegistry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectRegistry::tr(s, c, n));
}

//  QRemoteObjectRegistry::~QRemoteObjectRegistry()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectRegistryD1Ev(QRemoteObjectRegistry *self) {
  delete self;
}

//  void QRemoteObjectRegistry::registerMetatypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectRegistry17registerMetatypesEv() {
  QRemoteObjectRegistry::registerMetatypes();
}

//  QRemoteObjectSourceLocations QRemoteObjectRegistry::sourceLocations()
//      const
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_ZNK21QRemoteObjectRegistry15sourceLocationsEv(
    const QRemoteObjectRegistry *self) {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>(
      self->sourceLocations());
}

//  void QRemoteObjectRegistry::pushToRegistryIfNeeded()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectRegistry22pushToRegistryIfNeededEv(
    QRemoteObjectRegistry *self) {
  self->pushToRegistryIfNeeded();
}

//  void QRemoteObjectRegistry::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectRegistry10initializeEv(
    QRemoteObjectRegistry *self) {
  self->initialize();
}

//  void QRemoteObjectRegistry::notifySourceLocationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QRemoteObjectRegistry28notifySourceLocationsChangedEv(
    QRemoteObjectRegistry *self) {
  self->notifySourceLocationsChanged();
}

//  QRemoteObjectRegistry::QRemoteObjectRegistry(QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectRegistry *ritual_ZN21QRemoteObjectRegistryC1EP7QObject(
    QObject *parent) {
  return new CuteQRemoteObjectRegistry(parent);
}

//  QRemoteObjectRegistry::QRemoteObjectRegistry(QRemoteObjectNode *node,
//      const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectRegistry *ritual_ZN21QRemoteObjectRegistryC1EP17QRemoteObjectNodeRK7QStringP7QObject(
    QRemoteObjectNode *node,
    const QString *name,
    QObject *parent) {
  return new CuteQRemoteObjectRegistry(node, *name, parent);
}

//  a Python function taken by a CuteQRemoteObjectRegistry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectRegistry(
    QRemoteObjectRegistry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectRegistry *>(self)->take(key, call);
}

//  void QRemoteObjectRegistry::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QRemoteObjectRegistry10initializeEv(
    QRemoteObjectRegistry *self) {
  self->QRemoteObjectRegistry::initialize();
}
