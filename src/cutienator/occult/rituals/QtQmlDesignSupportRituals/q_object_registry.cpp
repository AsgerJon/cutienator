//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistry_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QObjectRegistry that Python can take functions over in. Every QObjectRegistry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQObjectRegistry : public QObjectRegistry {
public:
  using QObjectRegistry::QObjectRegistry;
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
      CuteQObjectRegistryCall0 call = reinterpret_cast<CuteQObjectRegistryCall0>(taken[0]);
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
      CuteQObjectRegistryCall1 call = reinterpret_cast<CuteQObjectRegistryCall1>(taken[1]);
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
      CuteQObjectRegistryCall2 call = reinterpret_cast<CuteQObjectRegistryCall2>(taken[2]);
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
      CuteQObjectRegistryCall3 call = reinterpret_cast<CuteQObjectRegistryCall3>(taken[3]);
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
      CuteQObjectRegistryCall4 call = reinterpret_cast<CuteQObjectRegistryCall4>(taken[4]);
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
      CuteQObjectRegistryCall5 call = reinterpret_cast<CuteQObjectRegistryCall5>(taken[5]);
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
      CuteQObjectRegistryCall6 call = reinterpret_cast<CuteQObjectRegistryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QObjectRegistry::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QObjectRegistry10metaObjectEv(
    const QObjectRegistry *self) {
  return self->metaObject();
}

//  QString QObjectRegistry::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QObjectRegistry2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectRegistry::tr(s, c, n));
}

//  void QObjectRegistry::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QObjectRegistry21qt_qmlMarker_attachedEv(
    QObjectRegistry *self) {
  self->qt_qmlMarker_attached();
}

//  QObjectRegistry::QObjectRegistry(QObject *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistry *ritual_ZN15QObjectRegistryC1EP7QObject(QObject *parent) {
  return new CuteQObjectRegistry(parent);
}

//  QObjectRegistry::~QObjectRegistry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QObjectRegistryD1Ev(QObjectRegistry *self) {
  delete self;
}

//  QObjectRegistryAttachedType
//      *QObjectRegistry::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QObjectRegistryAttachedType *ritual_ZN15QObjectRegistry21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QObjectRegistry::qmlAttachedProperties(object);
}

//  QString QObjectRegistry::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QObjectRegistry3keyEv(const QObjectRegistry *self) {
  return new QString(self->key());
}

//  void QObjectRegistry::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QObjectRegistry6setKeyERK7QString(
    QObjectRegistry *self,
    const QString *key) {
  self->setKey(*key);
}

//  QObject *QObjectRegistry::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QObjectRegistry6targetEv(const QObjectRegistry *self) {
  return self->target();
}

//  void QObjectRegistry::setTarget(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QObjectRegistry9setTargetEP7QObject(
    QObjectRegistry *self,
    QObject *target) {
  self->setTarget(target);
}

//  a Python function taken by a CuteQObjectRegistry, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObjectRegistry(
    QObjectRegistry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQObjectRegistry *>(self)->take(key, call);
}
