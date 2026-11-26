//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <cstring>

//  A QQmlValueType that Python can take functions over in. Every QQmlValueType
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlValueTypeCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlValueTypeCall1)(const void *, QObject *, int *);
class CuteQQmlValueType : public QQmlValueType {
public:
  using QQmlValueType::QQmlValueType;
  CuteQQmlValueType(const QQmlValueType & other) : QQmlValueType(other) {}
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
  //  QMetaObject *QQmlValueType::toDynamicMetaObject(QObject *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlValueTypeCall0 call = reinterpret_cast<CuteQQmlValueTypeCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QQmlValueType::toDynamicMetaObject(a0);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QQmlValueType::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlValueTypeCall1 call = reinterpret_cast<CuteQQmlValueTypeCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlValueType::objectDestroyed(a0);
  }
};

//  QQmlValueType::QQmlValueType()
extern "C" Q_DECL_EXPORT
QQmlValueType *ritual_ZN13QQmlValueTypeC1Ev() {
  return new CuteQQmlValueType();
}

//  QQmlValueType::QQmlValueType(QMetaType type, const QMetaObject
//      *staticMetaObject)
extern "C" Q_DECL_EXPORT
QQmlValueType *ritual_ZN13QQmlValueTypeC1E9QMetaTypePK11QMetaObject(
    const QMetaType *type,
    const QMetaObject *staticMetaObject) {
  return new CuteQQmlValueType(*type, staticMetaObject);
}

//  QQmlValueType::~QQmlValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlValueTypeD1Ev(QQmlValueType *self) {
  delete self;
}

//  void *QQmlValueType::create() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK13QQmlValueType6createEv(const QQmlValueType *self) {
  return self->create();
}

//  void QQmlValueType::destroy(void *gadgetPtr) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QQmlValueType7destroyEPv(
    const QQmlValueType *self,
    void *gadgetPtr) {
  self->destroy(gadgetPtr);
}

//  void QQmlValueType::construct(void *gadgetPtr, const void *copy) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QQmlValueType9constructEPvPKv(
    const QQmlValueType *self,
    void *gadgetPtr,
    const void *copy) {
  self->construct(gadgetPtr, copy);
}

//  void QQmlValueType::destruct(void *gadgetPtr) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QQmlValueType8destructEPv(
    const QQmlValueType *self,
    void *gadgetPtr) {
  self->destruct(gadgetPtr);
}

//  QMetaType QQmlValueType::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK13QQmlValueType8metaTypeEv(const QQmlValueType *self) {
  return new QMetaType(self->metaType());
}

//  const QMetaObject *QQmlValueType::staticMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQmlValueType16staticMetaObjectEv(
    const QQmlValueType *self) {
  return self->staticMetaObject();
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlValueType::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN13QQmlValueType19toDynamicMetaObjectEP7QObject(
    QQmlValueType *self,
    QObject *a0) {
  return self->toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  void QQmlValueType::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlValueType15objectDestroyedEP7QObject(
    QQmlValueType *self,
    QObject *a0) {
  self->objectDestroyed(a0);
}

//  int QQmlValueType::metaCall(QObject *obj, QMetaObject::Call type, int
//      _id, void **argv)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QQmlValueType8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QQmlValueType *self,
    QObject *obj,
    QMetaObject::Call type,
    int _id,
    void **argv) {
  return self->metaCall(obj, type, _id, argv);
}

//  a Python function taken by a CuteQQmlValueType, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlValueType(
    QQmlValueType *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlValueType *>(self)->take(key, call);
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
//  QMetaObject *QQmlValueType::toDynamicMetaObject(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_own_ZN13QQmlValueType19toDynamicMetaObjectEP7QObject(
    QQmlValueType *self,
    QObject *a0) {
  return self->QQmlValueType::toDynamicMetaObject(a0);
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

//  void QQmlValueType::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlValueType15objectDestroyedEP7QObject(
    QQmlValueType *self,
    QObject *a0) {
  self->QQmlValueType::objectDestroyed(a0);
}
