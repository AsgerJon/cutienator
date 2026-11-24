//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QAbstractDynamicMetaObject that Python can take functions over in. Every QAbstractDynamicMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQAbstractDynamicMetaObjectCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQAbstractDynamicMetaObjectCall1)(const void *, QObject *, int *);
class CuteQAbstractDynamicMetaObject : public QAbstractDynamicMetaObject {
public:
  using QAbstractDynamicMetaObject::QAbstractDynamicMetaObject;
  CuteQAbstractDynamicMetaObject(const QAbstractDynamicMetaObject &other) : QAbstractDynamicMetaObject(other) {}
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
  //  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject
  //      *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractDynamicMetaObjectCall0 call = reinterpret_cast<CuteQAbstractDynamicMetaObjectCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QAbstractDynamicMetaObject::toDynamicMetaObject(a0);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractDynamicMetaObjectCall1 call = reinterpret_cast<CuteQAbstractDynamicMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QAbstractDynamicMetaObject::~QAbstractDynamicMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractDynamicMetaObjectD1Ev(
    QAbstractDynamicMetaObject *self) {
  delete self;
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN26QAbstractDynamicMetaObject19toDynamicMetaObjectEP7QObject(
    QAbstractDynamicMetaObject *self,
    QObject *a0) {
  return self->toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  int QAbstractDynamicMetaObject::createProperty(const char *a0, const char
//      *a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QAbstractDynamicMetaObject14createPropertyEPKcS1_(
    QAbstractDynamicMetaObject *self,
    const char *a0,
    const char *a1) {
  return self->createProperty(a0, a1);
}

//  QAbstractDynamicMetaObject as the QMetaObject it is built on
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_cast_QAbstractDynamicMetaObject_QMetaObject(
    QAbstractDynamicMetaObject *self) {
  return static_cast<QMetaObject *>(self);
}

//  a Python function taken by a CuteQAbstractDynamicMetaObject, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractDynamicMetaObject(
    QAbstractDynamicMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractDynamicMetaObject *>(self)->take(key, call);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_own_ZN26QAbstractDynamicMetaObject19toDynamicMetaObjectEP7QObject(
    QAbstractDynamicMetaObject *self,
    QObject *a0) {
  return self->QAbstractDynamicMetaObject::toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
