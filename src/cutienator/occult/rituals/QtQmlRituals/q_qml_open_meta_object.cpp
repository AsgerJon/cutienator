//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  Only a class built on QQmlOpenMetaObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlOpenMetaObject : QQmlOpenMetaObject {
  using QQmlOpenMetaObject::propertyRead;
  using QQmlOpenMetaObject::propertyWrite;
  using QQmlOpenMetaObject::propertyWriteValue;
  using QQmlOpenMetaObject::propertyWritten;
};

//  A QQmlOpenMetaObject that Python can take functions over in. Every QQmlOpenMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQmlOpenMetaObjectCall0)(const void *, int, int *);
typedef void (*CuteQQmlOpenMetaObjectCall1)(const void *, int, int *);
typedef void (*CuteQQmlOpenMetaObjectCall2)(const void *, int, int *);
typedef const QVariant * (*CuteQQmlOpenMetaObjectCall3)(const void *, int, const QVariant *, int *);
typedef void (*CuteQQmlOpenMetaObjectCall4)(const void *, int, int *);
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlOpenMetaObjectCall5)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlOpenMetaObjectCall6)(const void *, QObject *, int *);
class CuteQQmlOpenMetaObject : public QQmlOpenMetaObject {
public:
  using QQmlOpenMetaObject::QQmlOpenMetaObject;
  CuteQQmlOpenMetaObject(const QQmlOpenMetaObject & other) : QQmlOpenMetaObject(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12initialValueEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12propertyReadEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject13propertyWriteEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject15propertyWrittenEi")) {
      taken[4] = call;
      return true;
    }
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData19toDynamicMetaObjectEP7QObject")) {
      taken[5] = call;
      return true;
    }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
    if (!std::strcmp(key, "_ZN22QDynamicMetaObjectData15objectDestroyedEP7QObject")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QVariant QQmlOpenMetaObject::initialValue(int a0)
  QVariant initialValue(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall0 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall0>(taken[0]);
      const QVariant * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::initialValue(a0);
  }

  //  void QQmlOpenMetaObject::propertyRead(int a0)
  void propertyRead(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall1 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyRead(a0);
  }

  //  void QQmlOpenMetaObject::propertyWrite(int a0)
  void propertyWrite(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall2 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyWrite(a0);
  }

  //  QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const
  //      QVariant &a1)
  QVariant propertyWriteValue(int a0, const QVariant &a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall3 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall3>(taken[3]);
      const QVariant * given = call(this, a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::propertyWriteValue(a0, a1);
  }

  //  void QQmlOpenMetaObject::propertyWritten(int a0)
  void propertyWritten(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall4 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyWritten(a0);
  }

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
  //  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject
  //      *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall5 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall5>(taken[5]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QMetaObject *>(given);
    }
    return QAbstractDynamicMetaObject::toDynamicMetaObject(a0);
  }
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))

  //  void QDynamicMetaObjectData::objectDestroyed(QObject *a0)
  void objectDestroyed(QObject *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlOpenMetaObjectCall6 call = reinterpret_cast<CuteQQmlOpenMetaObjectCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QQmlOpenMetaObject::QQmlOpenMetaObject(QObject *a0, const QMetaObject
//      *a1)
extern "C" Q_DECL_EXPORT
QQmlOpenMetaObject *ritual_ZN18QQmlOpenMetaObjectC1EP7QObjectPK11QMetaObject(
    QObject *a0,
    const QMetaObject *a1) {
  return new CuteQQmlOpenMetaObject(a0, a1);
}

//  QQmlOpenMetaObject::QQmlOpenMetaObject(QObject *a0, const
//      QQmlRefPointer<QQmlOpenMetaObjectType> &a1)
extern "C" Q_DECL_EXPORT
QQmlOpenMetaObject *ritual_ZN18QQmlOpenMetaObjectC1EP7QObjectRK14QQmlRefPointerI22QQmlOpenMetaObjectTypeE(
    QObject *a0,
    const QQmlRefPointer<QQmlOpenMetaObjectType> *a1) {
  return new CuteQQmlOpenMetaObject(a0, *a1);
}

//  QQmlOpenMetaObject::~QQmlOpenMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObjectD1Ev(QQmlOpenMetaObject *self) {
  delete self;
}

//  QVariant QQmlOpenMetaObject::value(const QByteArray &a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQmlOpenMetaObject5valueERK10QByteArray(
    const QQmlOpenMetaObject *self,
    const QByteArray *a0) {
  return new QVariant(self->value(*a0));
}

//  bool QQmlOpenMetaObject::setValue(const QByteArray &a0, const QVariant
//      &a1, bool force)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlOpenMetaObject8setValueERK10QByteArrayRK8QVariantb(
    QQmlOpenMetaObject *self,
    const QByteArray *a0,
    const QVariant *a1,
    bool force) {
  return self->setValue(*a0, *a1, force);
}

//  void QQmlOpenMetaObject::setValues(const QHash<QByteArray, QVariant> &a0,
//      bool force)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject9setValuesERK5QHashI10QByteArray8QVariantEb(
    QQmlOpenMetaObject *self,
    const QHash<QByteArray, QVariant> *a0,
    bool force) {
  self->setValues(*a0, force);
}

//  QVariant QQmlOpenMetaObject::value(int a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QQmlOpenMetaObject5valueEi(
    const QQmlOpenMetaObject *self,
    int a0) {
  return new QVariant(self->value(a0));
}

//  void QQmlOpenMetaObject::setValue(int a0, const QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject8setValueEiRK8QVariant(
    QQmlOpenMetaObject *self,
    int a0,
    const QVariant *a1) {
  self->setValue(a0, *a1);
}

//  QVariant &QQmlOpenMetaObject::valueRef(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18QQmlOpenMetaObject8valueRefERK10QByteArray(
    QQmlOpenMetaObject *self,
    const QByteArray *a0) {
  return &(self->valueRef(*a0));
}

//  bool QQmlOpenMetaObject::hasValue(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlOpenMetaObject8hasValueEi(
    const QQmlOpenMetaObject *self,
    int a0) {
  return self->hasValue(a0);
}

//  int QQmlOpenMetaObject::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlOpenMetaObject5countEv(const QQmlOpenMetaObject *self) {
  return self->count();
}

//  QByteArray QQmlOpenMetaObject::name(int a0) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QQmlOpenMetaObject4nameEi(
    const QQmlOpenMetaObject *self,
    int a0) {
  return new QByteArray(self->name(a0));
}

//  QObject *QQmlOpenMetaObject::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QQmlOpenMetaObject6objectEv(
    const QQmlOpenMetaObject *self) {
  return self->object();
}

//  QVariant QQmlOpenMetaObject::initialValue(int a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18QQmlOpenMetaObject12initialValueEi(
    QQmlOpenMetaObject *self,
    int a0) {
  return new QVariant(self->initialValue(a0));
}

//  void QQmlOpenMetaObject::setCached(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject9setCachedEb(
    QQmlOpenMetaObject *self,
    bool a0) {
  self->setCached(a0);
}

//  bool QQmlOpenMetaObject::autoCreatesProperties() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlOpenMetaObject21autoCreatesPropertiesEv(
    const QQmlOpenMetaObject *self) {
  return self->autoCreatesProperties();
}

//  void QQmlOpenMetaObject::setAutoCreatesProperties(bool autoCreate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject24setAutoCreatesPropertiesEb(
    QQmlOpenMetaObject *self,
    bool autoCreate) {
  self->setAutoCreatesProperties(autoCreate);
}

//  QQmlOpenMetaObjectType *QQmlOpenMetaObject::type() const
extern "C" Q_DECL_EXPORT
QQmlOpenMetaObjectType *ritual_ZNK18QQmlOpenMetaObject4typeEv(
    const QQmlOpenMetaObject *self) {
  return self->type();
}

//  QDynamicMetaObjectData *QQmlOpenMetaObject::parent() const
extern "C" Q_DECL_EXPORT
QDynamicMetaObjectData *ritual_ZNK18QQmlOpenMetaObject6parentEv(
    const QQmlOpenMetaObject *self) {
  return self->parent();
}

//  void QQmlOpenMetaObject::emitPropertyNotification(const QByteArray
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject24emitPropertyNotificationERK10QByteArray(
    QQmlOpenMetaObject *self,
    const QByteArray *propertyName) {
  self->emitPropertyNotification(*propertyName);
}

//  void QQmlOpenMetaObject::unparent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject8unparentEv(QQmlOpenMetaObject *self) {
  self->unparent();
}

//  int QQmlOpenMetaObject::metaCall(QObject *o, QMetaObject::Call _c, int
//      _id, void **_a)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlOpenMetaObject8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QQmlOpenMetaObject *self,
    QObject *o,
    QMetaObject::Call _c,
    int _id,
    void **_a) {
  return self->metaCall(o, _c, _id, _a);
}

//  int QQmlOpenMetaObject::createProperty(const char *a0, const char *a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlOpenMetaObject14createPropertyEPKcS1_(
    QQmlOpenMetaObject *self,
    const char *a0,
    const char *a1) {
  return self->createProperty(a0, a1);
}

//  void QQmlOpenMetaObject::propertyRead(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject12propertyReadEi(
    QQmlOpenMetaObject *self,
    int a0) {
  self->propertyRead(a0);
}

//  void QQmlOpenMetaObject::propertyWrite(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject13propertyWriteEi(
    QQmlOpenMetaObject *self,
    int a0) {
  self->propertyWrite(a0);
}

//  QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant(
    QQmlOpenMetaObject *self,
    int a0,
    const QVariant *a1) {
  return new QVariant(self->propertyWriteValue(a0, *a1));
}

//  void QQmlOpenMetaObject::propertyWritten(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject15propertyWrittenEi(
    QQmlOpenMetaObject *self,
    int a0) {
  self->propertyWritten(a0);
}

//  void QQmlOpenMetaObject::propertyCreated(int a0, QMetaPropertyBuilder
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlOpenMetaObject15propertyCreatedEiR20QMetaPropertyBuilder(
    QQmlOpenMetaObject *self,
    int a0,
    QMetaPropertyBuilder *a1) {
  self->propertyCreated(a0, *a1);
}

//  bool QQmlOpenMetaObject::checkedSetValue(int index, const QVariant
//      &value, bool force)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlOpenMetaObject15checkedSetValueEiRK8QVariantb(
    QQmlOpenMetaObject *self,
    int index,
    const QVariant *value,
    bool force) {
  return self->checkedSetValue(index, *value, force);
}

//  a Python function taken by a CuteQQmlOpenMetaObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlOpenMetaObject(
    QQmlOpenMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlOpenMetaObject *>(self)->take(key, call);
}

//  QVariant QQmlOpenMetaObject::initialValue(int a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN18QQmlOpenMetaObject12initialValueEi(
    QQmlOpenMetaObject *self,
    int a0) {
  return new QVariant(self->QQmlOpenMetaObject::initialValue(a0));
}

//  void QQmlOpenMetaObject::propertyRead(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlOpenMetaObject12propertyReadEi(
    QQmlOpenMetaObject *self,
    int a0) {
  static_cast<OwnQQmlOpenMetaObject *>(self)->OwnQQmlOpenMetaObject::propertyRead(
      a0);
}

//  void QQmlOpenMetaObject::propertyWrite(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlOpenMetaObject13propertyWriteEi(
    QQmlOpenMetaObject *self,
    int a0) {
  static_cast<OwnQQmlOpenMetaObject *>(self)->OwnQQmlOpenMetaObject::propertyWrite(
      a0);
}

//  QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant(
    QQmlOpenMetaObject *self,
    int a0,
    const QVariant *a1) {
  return new QVariant(
      static_cast<OwnQQmlOpenMetaObject *>(self)->OwnQQmlOpenMetaObject::propertyWriteValue(
          a0,
          *a1));
}

//  void QQmlOpenMetaObject::propertyWritten(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlOpenMetaObject15propertyWrittenEi(
    QQmlOpenMetaObject *self,
    int a0) {
  static_cast<OwnQQmlOpenMetaObject *>(self)->OwnQQmlOpenMetaObject::propertyWritten(
      a0);
}
