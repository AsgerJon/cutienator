//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qaccessiblecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccessibleCache that Python can take functions over in. Every QAccessibleCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibleCacheCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibleCacheCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleCacheCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccessibleCache : public QAccessibleCache {
public:
  using QAccessibleCache::QAccessibleCache;
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
      CuteQAccessibleCacheCall0 call = reinterpret_cast<CuteQAccessibleCacheCall0>(taken[0]);
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
      CuteQAccessibleCacheCall1 call = reinterpret_cast<CuteQAccessibleCacheCall1>(taken[1]);
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
      CuteQAccessibleCacheCall2 call = reinterpret_cast<CuteQAccessibleCacheCall2>(taken[2]);
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
      CuteQAccessibleCacheCall3 call = reinterpret_cast<CuteQAccessibleCacheCall3>(taken[3]);
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
      CuteQAccessibleCacheCall4 call = reinterpret_cast<CuteQAccessibleCacheCall4>(taken[4]);
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
      CuteQAccessibleCacheCall5 call = reinterpret_cast<CuteQAccessibleCacheCall5>(taken[5]);
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
      CuteQAccessibleCacheCall6 call = reinterpret_cast<CuteQAccessibleCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccessibleCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QAccessibleCache10metaObjectEv(
    const QAccessibleCache *self) {
  return self->metaObject();
}

//  void *QAccessibleCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QAccessibleCache11qt_metacastEPKc(
    QAccessibleCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAccessibleCache::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QAccessibleCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QAccessibleCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAccessibleCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QAccessibleCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessibleCache::tr(s, c, n));
}

//  QAccessibleCache::~QAccessibleCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleCacheD1Ev(QAccessibleCache *self) {
  delete self;
}

//  QAccessibleCache *QAccessibleCache::instance()
extern "C" Q_DECL_EXPORT
QAccessibleCache *ritual_ZN16QAccessibleCache8instanceEv() {
  return QAccessibleCache::instance();
}

//  QAccessibleInterface *QAccessibleCache::interfaceForId(QAccessible::Id
//      id) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK16QAccessibleCache14interfaceForIdEj(
    const QAccessibleCache *self,
    QAccessible::Id id) {
  return self->interfaceForId(id);
}

//  QAccessible::Id QAccessibleCache::idForInterface(QAccessibleInterface
//      *iface) const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleCache14idForInterfaceEP20QAccessibleInterface(
    const QAccessibleCache *self,
    QAccessibleInterface *iface) {
  return self->idForInterface(iface);
}

//  QAccessible::Id QAccessibleCache::idForObject(QObject *obj) const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleCache11idForObjectEP7QObject(
    const QAccessibleCache *self,
    QObject *obj) {
  return self->idForObject(obj);
}

//  bool QAccessibleCache::containsObject(QObject *obj) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QAccessibleCache14containsObjectEP7QObject(
    const QAccessibleCache *self,
    QObject *obj) {
  return self->containsObject(obj);
}

//  QAccessible::Id QAccessibleCache::insert(QObject *object,
//      QAccessibleInterface *iface) const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleCache6insertEP7QObjectP20QAccessibleInterface(
    const QAccessibleCache *self,
    QObject *object,
    QAccessibleInterface *iface) {
  return self->insert(object, iface);
}

//  void QAccessibleCache::deleteInterface(QAccessible::Id id, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleCache15deleteInterfaceEjP7QObject(
    QAccessibleCache *self,
    QAccessible::Id id,
    QObject *obj) {
  self->deleteInterface(id, obj);
}

//  void QAccessibleCache::sendObjectDestroyedEvent(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleCache24sendObjectDestroyedEventEP7QObject(
    QAccessibleCache *self,
    QObject *obj) {
  self->sendObjectDestroyedEvent(obj);
}

//  void QAccessibleCache::objectDestroyed(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QAccessibleCache15objectDestroyedEP7QObject(
    QAccessibleCache *self,
    QObject *obj) {
  self->objectDestroyed(obj);
}

//  QAccessible::Id QAccessibleCache::acquireId() const
extern "C" Q_DECL_EXPORT
QAccessible::Id ritual_ZNK16QAccessibleCache9acquireIdEv(
    const QAccessibleCache *self) {
  return self->acquireId();
}

//  a Python function taken by a CuteQAccessibleCache, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleCache(
    QAccessibleCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleCache *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
