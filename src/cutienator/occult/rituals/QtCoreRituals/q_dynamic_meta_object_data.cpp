//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QDynamicMetaObjectData that Python can take functions over in. Every QDynamicMetaObjectData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDynamicMetaObjectDataCall0)(const void *, QObject *, int *);
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQDynamicMetaObjectDataCall1)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
class CuteQDynamicMetaObjectData : public QDynamicMetaObjectData {
public:
  using QDynamicMetaObjectData::QDynamicMetaObjectData;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject")) {
      taken[0] = call;
      return true;
    }
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData19toDynamicMetaObjectEP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    return false;
  }

  //  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDynamicMetaObjectDataCall0 call = reinterpret_cast<CuteQDynamicMetaObjectDataCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
  //  QMetaObject *QDynamicMetaObjectData::toDynamicMetaObject(QObject *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDynamicMetaObjectDataCall1 call = reinterpret_cast<CuteQDynamicMetaObjectDataCall1>(taken[1]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return {};
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
};

//  QDynamicMetaObjectData::~QDynamicMetaObjectData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDynamicMetaObjectDataD1Ev(QDynamicMetaObjectData *self) {
  delete self;
}

//  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject(
    QDynamicMetaObjectData *self,
    QObject *a0) {
  self->objectDestroyed(a0);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QDynamicMetaObjectData::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN22QDynamicMetaObjectData19toDynamicMetaObjectEP7QObject(
    QDynamicMetaObjectData *self,
    QObject *a0) {
  return self->toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  int QDynamicMetaObjectData::metaCall(QObject *a0, QMetaObject::Call a1,
//      int _id, void **a3)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDynamicMetaObjectData8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QDynamicMetaObjectData *self,
    QObject *a0,
    QMetaObject::Call a1,
    int _id,
    void **a3) {
  return self->metaCall(a0, a1, _id, a3);
}

//  a Python function taken by a CuteQDynamicMetaObjectData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDynamicMetaObjectData(
    QDynamicMetaObjectData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDynamicMetaObjectData *>(self)->take(key, call);
}

//  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject(
    QDynamicMetaObjectData *self,
    QObject *a0) {
  self->QDynamicMetaObjectData::objectDestroyed(a0);
}
