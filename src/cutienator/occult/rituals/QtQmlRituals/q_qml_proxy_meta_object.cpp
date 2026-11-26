//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlproxymetaobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlproxymetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QQmlProxyMetaObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlProxyMetaObject : QQmlProxyMetaObject {
  using QQmlProxyMetaObject::toDynamicMetaObject;
  using QQmlProxyMetaObject::objectDestroyed;
};

//  A QQmlProxyMetaObject that Python can take functions over in. Every QQmlProxyMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlProxyMetaObjectCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlProxyMetaObjectCall1)(const void *, QObject *, int *);
class CuteQQmlProxyMetaObject : public QQmlProxyMetaObject {
public:
  using QQmlProxyMetaObject::QQmlProxyMetaObject;
  CuteQQmlProxyMetaObject(const QQmlProxyMetaObject & other) : QQmlProxyMetaObject(other) {}
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
  //  QMetaObject *QQmlProxyMetaObject::toDynamicMetaObject(QObject *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlProxyMetaObjectCall0 call = reinterpret_cast<CuteQQmlProxyMetaObjectCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QQmlProxyMetaObject::toDynamicMetaObject(a0);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QQmlProxyMetaObject::objectDestroyed(QObject *object)
  void objectDestroyed(QObject *object) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlProxyMetaObjectCall1 call = reinterpret_cast<CuteQQmlProxyMetaObjectCall1>(taken[1]);
      call(this, object, &handled);
      if (handled) return;
    }
    QQmlProxyMetaObject::objectDestroyed(object);
  }
};

//  QQmlProxyMetaObject::QQmlProxyMetaObject(QObject *a0, const
//      QList<ProxyData> *a1)
extern "C" Q_DECL_EXPORT
QQmlProxyMetaObject *ritual_ZN19QQmlProxyMetaObjectC1EP7QObjectPK5QListINS_9ProxyDataEE(
    QObject *a0,
    const QList<QQmlProxyMetaObject::ProxyData> *a1) {
  return new CuteQQmlProxyMetaObject(a0, a1);
}

//  QQmlProxyMetaObject::~QQmlProxyMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlProxyMetaObjectD1Ev(QQmlProxyMetaObject *self) {
  delete self;
}

//  int QQmlProxyMetaObject::extensionObjectId(int id)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlProxyMetaObject17extensionObjectIdEi(int id) {
  return QQmlProxyMetaObject::extensionObjectId(id);
}

//  int QQmlProxyMetaObject::metaCall(QObject *o, QMetaObject::Call _c, int
//      _id, void **_a)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlProxyMetaObject8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QQmlProxyMetaObject *self,
    QObject *o,
    QMetaObject::Call _c,
    int _id,
    void **_a) {
  return self->metaCall(o, _c, _id, _a);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlProxyMetaObject::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN19QQmlProxyMetaObject19toDynamicMetaObjectEP7QObject(
    QQmlProxyMetaObject *self,
    QObject *a0) {
  return self->toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  void QQmlProxyMetaObject::objectDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlProxyMetaObject15objectDestroyedEP7QObject(
    QQmlProxyMetaObject *self,
    QObject *object) {
  self->objectDestroyed(object);
}

//  QObject *QQmlProxyMetaObject::getProxy(int index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN19QQmlProxyMetaObject8getProxyEi(
    QQmlProxyMetaObject *self,
    int index) {
  return self->getProxy(index);
}

//  a Python function taken by a CuteQQmlProxyMetaObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlProxyMetaObject(
    QQmlProxyMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlProxyMetaObject *>(self)->take(key, call);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlProxyMetaObject::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_own_ZN19QQmlProxyMetaObject19toDynamicMetaObjectEP7QObject(
    QQmlProxyMetaObject *self,
    QObject *a0) {
  return static_cast<OwnQQmlProxyMetaObject *>(self)->OwnQQmlProxyMetaObject::toDynamicMetaObject(
      a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  void QQmlProxyMetaObject::objectDestroyed(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlProxyMetaObject15objectDestroyedEP7QObject(
    QQmlProxyMetaObject *self,
    QObject *object) {
  static_cast<OwnQQmlProxyMetaObject *>(self)->OwnQQmlProxyMetaObject::objectDestroyed(
      object);
}
