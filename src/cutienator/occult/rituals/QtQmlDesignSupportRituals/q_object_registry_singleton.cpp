//  Written by dev_tooling.RitualGenerator from the records of QtQmlDesignSup
//  port/6.12.0/QtQmlDesignSupport/private/qobjectregistrysingleton_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistrysingleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QObjectRegistrySingleton that Python can take functions over in. Every QObjectRegistrySingleton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistrySingletonCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistrySingletonCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistrySingletonCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistrySingletonCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistrySingletonCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistrySingletonCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistrySingletonCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQObjectRegistrySingleton : public QObjectRegistrySingleton {
public:
  using QObjectRegistrySingleton::QObjectRegistrySingleton;
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
      CuteQObjectRegistrySingletonCall0 call = reinterpret_cast<CuteQObjectRegistrySingletonCall0>(taken[0]);
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
      CuteQObjectRegistrySingletonCall1 call = reinterpret_cast<CuteQObjectRegistrySingletonCall1>(taken[1]);
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
      CuteQObjectRegistrySingletonCall2 call = reinterpret_cast<CuteQObjectRegistrySingletonCall2>(taken[2]);
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
      CuteQObjectRegistrySingletonCall3 call = reinterpret_cast<CuteQObjectRegistrySingletonCall3>(taken[3]);
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
      CuteQObjectRegistrySingletonCall4 call = reinterpret_cast<CuteQObjectRegistrySingletonCall4>(taken[4]);
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
      CuteQObjectRegistrySingletonCall5 call = reinterpret_cast<CuteQObjectRegistrySingletonCall5>(taken[5]);
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
      CuteQObjectRegistrySingletonCall6 call = reinterpret_cast<CuteQObjectRegistrySingletonCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QObjectRegistrySingleton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QObjectRegistrySingleton10metaObjectEv(
    const QObjectRegistrySingleton *self) {
  return self->metaObject();
}

//  QString QObjectRegistrySingleton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QObjectRegistrySingleton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectRegistrySingleton::tr(s, c, n));
}

//  void QObjectRegistrySingleton::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton22qt_qmlMarker_singletonEv(
    QObjectRegistrySingleton *self) {
  self->qt_qmlMarker_singleton();
}

//  QObjectRegistrySingleton::QObjectRegistrySingleton(QObject *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistrySingleton *ritual_ZN24QObjectRegistrySingletonC1EP7QObject(
    QObject *parent) {
  return new CuteQObjectRegistrySingleton(parent);
}

//  QObjectRegistrySingleton::~QObjectRegistrySingleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingletonD1Ev(
    QObjectRegistrySingleton *self) {
  delete self;
}

//  void
//      QObjectRegistrySingleton::registerRef(QAbstractObjectRegistryRefPriva
//      te *ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton11registerRefEP33QAbstractObjectRegistryRefPrivate(
    QObjectRegistrySingleton *self,
    QAbstractObjectRegistryRefPrivate *ref) {
  self->registerRef(ref);
}

//  void
//      QObjectRegistrySingleton::deregisterRef(QAbstractObjectRegistryRefPri
//      vate *ref)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton13deregisterRefEP33QAbstractObjectRegistryRefPrivate(
    QObjectRegistrySingleton *self,
    QAbstractObjectRegistryRefPrivate *ref) {
  self->deregisterRef(ref);
}

//  void QObjectRegistrySingleton::add(const QString &key, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton3addERK7QStringP7QObject(
    QObjectRegistrySingleton *self,
    const QString *key,
    QObject *obj) {
  self->add(*key, obj);
}

//  void QObjectRegistrySingleton::remove(const QString &key, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton6removeERK7QStringP7QObject(
    QObjectRegistrySingleton *self,
    const QString *key,
    QObject *obj) {
  self->remove(*key, obj);
}

//  QObjectRegistrySingleton
//      *QObjectRegistrySingleton::registryForObject(QObject *obj)
extern "C" Q_DECL_EXPORT
QObjectRegistrySingleton *ritual_ZN24QObjectRegistrySingleton17registryForObjectEP7QObject(
    QObject *obj) {
  return QObjectRegistrySingleton::registryForObject(obj);
}

//  QObjectRegistrySingleton
//      *QObjectRegistrySingleton::registryForEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QObjectRegistrySingleton *ritual_ZN24QObjectRegistrySingleton17registryForEngineEP10QQmlEngine(
    QQmlEngine *engine) {
  return QObjectRegistrySingleton::registryForEngine(engine);
}

//  void QObjectRegistrySingleton::notifyRefs(const QString &key, QObject
//      *obj, Notification notification)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QObjectRegistrySingleton10notifyRefsERK7QStringP7QObjectNS_12NotificationE(
    QObjectRegistrySingleton *self,
    const QString *key,
    QObject *obj,
    QObjectRegistrySingleton::Notification notification) {
  self->notifyRefs(*key, obj, notification);
}

//  a Python function taken by a CuteQObjectRegistrySingleton, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObjectRegistrySingleton(
    QObjectRegistrySingleton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQObjectRegistrySingleton *>(self)->take(key, call);
}
