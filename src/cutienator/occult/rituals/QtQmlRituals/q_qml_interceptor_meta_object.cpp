//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertyindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlInterceptorMetaObject that Python can take functions over in. Every QQmlInterceptorMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlInterceptorMetaObjectCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlInterceptorMetaObjectCall1)(const void *, QObject *, int *);
class CuteQQmlInterceptorMetaObject : public QQmlInterceptorMetaObject {
public:
  using QQmlInterceptorMetaObject::QQmlInterceptorMetaObject;
  CuteQQmlInterceptorMetaObject(const QQmlInterceptorMetaObject &other) : QQmlInterceptorMetaObject(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData19toDynamicMetaObjectEP7QObject")) {
      taken[0] = call;
      return true;
    }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
  //  QMetaObject *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject
  //      *o)
  QMetaObject *toDynamicMetaObject(QObject *o) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlInterceptorMetaObjectCall0 call = reinterpret_cast<CuteQQmlInterceptorMetaObjectCall0>(taken[0]);
      void * given = call(this, o, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QQmlInterceptorMetaObject::toDynamicMetaObject(o);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlInterceptorMetaObjectCall1 call = reinterpret_cast<CuteQQmlInterceptorMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QQmlInterceptorMetaObject::QQmlInterceptorMetaObject(QObject *obj, const
//      QQmlPropertyCache::ConstPtr &cache)
extern "C" Q_DECL_EXPORT
QQmlInterceptorMetaObject *ritual_ZN25QQmlInterceptorMetaObjectC1EP7QObjectRKN17QQmlPropertyCache8ConstPtrE(
    QObject *obj,
    const QQmlPropertyCache::ConstPtr *cache) {
  return new CuteQQmlInterceptorMetaObject(obj, *cache);
}

//  QQmlInterceptorMetaObject::~QQmlInterceptorMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlInterceptorMetaObjectD1Ev(
    QQmlInterceptorMetaObject *self) {
  delete self;
}

//  void QQmlInterceptorMetaObject::registerInterceptor(QQmlPropertyIndex
//      index, QQmlPropertyValueInterceptor *interceptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlInterceptorMetaObject19registerInterceptorE17QQmlPropertyIndexP28QQmlPropertyValueInterceptor(
    QQmlInterceptorMetaObject *self,
    const QQmlPropertyIndex *index,
    QQmlPropertyValueInterceptor *interceptor) {
  self->registerInterceptor(*index, interceptor);
}

//  QQmlInterceptorMetaObject *QQmlInterceptorMetaObject::get(QObject *obj)
extern "C" Q_DECL_EXPORT
QQmlInterceptorMetaObject *ritual_ZN25QQmlInterceptorMetaObject3getEP7QObject(
    QObject *obj) {
  return QQmlInterceptorMetaObject::get(obj);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject *o)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN25QQmlInterceptorMetaObject19toDynamicMetaObjectEP7QObject(
    QQmlInterceptorMetaObject *self,
    QObject *o) {
  return self->toDynamicMetaObject(o);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  QQmlPropertyCache::ConstPtr QQmlInterceptorMetaObject::propertyCache()
//      const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK25QQmlInterceptorMetaObject13propertyCacheEv(
    const QQmlInterceptorMetaObject *self) {
  return new QQmlPropertyCache::ConstPtr(self->propertyCache());
}

//  void QQmlInterceptorMetaObject::setPropertyCache(const
//      QQmlPropertyCache::ConstPtr &newCache)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlInterceptorMetaObject16setPropertyCacheERKN17QQmlPropertyCache8ConstPtrE(
    QQmlInterceptorMetaObject *self,
    const QQmlPropertyCache::ConstPtr *newCache) {
  self->setPropertyCache(*newCache);
}

//  bool QQmlInterceptorMetaObject::intercepts(QQmlPropertyIndex
//      propertyIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlInterceptorMetaObject10interceptsE17QQmlPropertyIndex(
    const QQmlInterceptorMetaObject *self,
    const QQmlPropertyIndex *propertyIndex) {
  return self->intercepts(*propertyIndex);
}

//  void QQmlInterceptorMetaObject::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlInterceptorMetaObject10invalidateEv(
    QQmlInterceptorMetaObject *self) {
  self->invalidate();
}

//  void QQmlInterceptorMetaObject::setInterceptionMode(QObject *object,
//      InterceptionBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlInterceptorMetaObject19setInterceptionModeEP7QObjectNS_20InterceptionBehaviorE(
    QObject *object,
    QQmlInterceptorMetaObject::InterceptionBehavior behavior) {
  QQmlInterceptorMetaObject::setInterceptionMode(object, behavior);
}

//  a Python function taken by a CuteQQmlInterceptorMetaObject, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlInterceptorMetaObject(
    QQmlInterceptorMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlInterceptorMetaObject *>(self)->take(key, call);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlInterceptorMetaObject::toDynamicMetaObject(QObject *o)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_own_ZN25QQmlInterceptorMetaObject19toDynamicMetaObjectEP7QObject(
    QQmlInterceptorMetaObject *self,
    QObject *o) {
  return self->QQmlInterceptorMetaObject::toDynamicMetaObject(o);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
