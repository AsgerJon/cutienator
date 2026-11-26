//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qqmldesignermetaobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qqmldesignermetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qqmldesignermetaobject_p.h>
#include <QtCore/QSharedPointer>
#include <QtCore/QMetaProperty>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QDebug>
#include <QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 19, as local:qqmldesignermetaobject.cpp:MetaPropertyData
struct MetaPropertyData {
    inline std::pair<QVariant, bool> &getDataRef(int idx) {
        while (m_data.size() <= idx)
            m_data << std::pair<QVariant, bool>(QVariant(), false);
        return m_data[idx];
    }

    inline QVariant &getData(int idx) {
        std::pair<QVariant, bool> &prop = getDataRef(idx);
        if (!prop.second) {
            prop.first = QVariant();
            prop.second = true;
        }
        return prop.first;
    }

    inline bool hasData(int idx) const {
        if (idx >= m_data.size())
            return false;
        return m_data[idx].second;
    }

    inline int count() { return m_data.size(); }

    QList<std::pair<QVariant, bool> > m_data;
};

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 115, as _ZN22QQmlDesignerMetaObject8setValueEiRK8QVariant
inline void QQmlDesignerMetaObject::setValue(int id, const QVariant &value)
{
    std::pair<QVariant, bool> &prop = m_data->getDataRef(id);
    prop.first = propertyWriteValue(id, value);
    prop.second = true;
    QMetaObject::activate(myObject(), id + type()->signalOffset(), nullptr);
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 123, as _ZN22QQmlDesignerMetaObject18propertyWriteValueEiRK8QVariant
inline QVariant QQmlDesignerMetaObject::propertyWriteValue(int, const QVariant &value)
{
    return value;
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 92, as _ZN22QQmlDesignerMetaObject24createNewDynamicPropertyERK7QString
inline void QQmlDesignerMetaObject::createNewDynamicProperty(const QString &name)
{
    int id = type()->createProperty(name.toUtf8());
    setValue(id, QVariant());
    Q_ASSERT(id >= 0);

    //Updating cache
    cache()->invalidate(this);

    QQmlProperty property(myObject(), name, m_context);
    Q_ASSERT(property.isValid());
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 128, as _ZNK22QQmlDesignerMetaObject23dynamicMetaObjectParentEv
inline QDynamicMetaObjectData *QQmlDesignerMetaObject::dynamicMetaObjectParent() const
{
    return parent();
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 133, as _ZNK22QQmlDesignerMetaObject14propertyOffsetEv
inline int QQmlDesignerMetaObject::propertyOffset() const
{
    return cache()->propertyOffset();
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 231, as _ZNK22QQmlDesignerMetaObject5countEv
inline int QQmlDesignerMetaObject::count() const
{
    return type()->propertyCount();
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 236, as _ZNK22QQmlDesignerMetaObject4nameEi
inline QByteArray QQmlDesignerMetaObject::name(int idx) const
{
    return type()->propertyName(idx);
}

//  from ../qtdeclarative/src/quick/designer/qqmldesignermetaobject.cpp, line 73, as _ZNK22QQmlDesignerMetaObject5cacheEv
inline QQmlPropertyCache::Ptr QQmlDesignerMetaObject::cache() const
{
    return type()->cache();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQmlDesignerMetaObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlDesignerMetaObject : QQmlDesignerMetaObject {
  using QQmlDesignerMetaObject::propertyWriteValue;
};

//  A QQmlDesignerMetaObject that Python can take functions over in. Every QQmlDesignerMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQmlDesignerMetaObjectCall0)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQQmlDesignerMetaObjectCall1)(const void *, int, int *);
typedef void (*CuteQQmlDesignerMetaObjectCall2)(const void *, int, int *);
typedef void (*CuteQQmlDesignerMetaObjectCall3)(const void *, int, int *);
typedef void (*CuteQQmlDesignerMetaObjectCall4)(const void *, int, int *);
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlDesignerMetaObjectCall5)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlDesignerMetaObjectCall6)(const void *, QObject *, int *);
class CuteQQmlDesignerMetaObject : public QQmlDesignerMetaObject {
public:
  using QQmlDesignerMetaObject::QQmlDesignerMetaObject;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12initialValueEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12propertyReadEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject13propertyWriteEi")) {
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

  //  QVariant QQmlDesignerMetaObject::propertyWriteValue(int a0, const
  //      QVariant &a1)
  QVariant propertyWriteValue(int a0, const QVariant &a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDesignerMetaObjectCall0 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall0>(taken[0]);
      const QVariant * given = call(this, a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlDesignerMetaObject::propertyWriteValue(a0, a1);
  }

  //  QVariant QQmlOpenMetaObject::initialValue(int a0)
  QVariant initialValue(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDesignerMetaObjectCall1 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall1>(taken[1]);
      const QVariant * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::initialValue(a0);
  }

  //  void QQmlOpenMetaObject::propertyRead(int a0)
  void propertyRead(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDesignerMetaObjectCall2 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyRead(a0);
  }

  //  void QQmlOpenMetaObject::propertyWrite(int a0)
  void propertyWrite(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDesignerMetaObjectCall3 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyWrite(a0);
  }

  //  void QQmlOpenMetaObject::propertyWritten(int a0)
  void propertyWritten(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDesignerMetaObjectCall4 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall4>(taken[4]);
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
      CuteQQmlDesignerMetaObjectCall5 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall5>(taken[5]);
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
      CuteQQmlDesignerMetaObjectCall6 call = reinterpret_cast<CuteQQmlDesignerMetaObjectCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  void QQmlDesignerMetaObject::createNewDynamicProperty(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDesignerMetaObject24createNewDynamicPropertyERK7QString(
    QQmlDesignerMetaObject *self,
    const QString *name) {
  self->createNewDynamicProperty(*name);
}

//  int QQmlDesignerMetaObject::createProperty(const char *name, const char
//      *passAlong)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlDesignerMetaObject14createPropertyEPKcS1_(
    QQmlDesignerMetaObject *self,
    const char *name,
    const char *passAlong) {
  return self->createProperty(name, passAlong);
}

//  int QQmlDesignerMetaObject::metaCall(QObject *o, QMetaObject::Call _c,
//      int _id, void **_a)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlDesignerMetaObject8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QQmlDesignerMetaObject *self,
    QObject *o,
    QMetaObject::Call _c,
    int _id,
    void **_a) {
  return self->metaCall(o, _c, _id, _a);
}

//  QVariant QQmlDesignerMetaObject::propertyWriteValue(int a0, const
//      QVariant &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN22QQmlDesignerMetaObject18propertyWriteValueEiRK8QVariant(
    QQmlDesignerMetaObject *self,
    int a0,
    const QVariant *a1) {
  return new QVariant(self->propertyWriteValue(a0, *a1));
}

//  QObject *QQmlDesignerMetaObject::myObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK22QQmlDesignerMetaObject8myObjectEv(
    const QQmlDesignerMetaObject *self) {
  return self->myObject();
}

//  QDynamicMetaObjectData *QQmlDesignerMetaObject::dynamicMetaObjectParent()
//      const
extern "C" Q_DECL_EXPORT
QDynamicMetaObjectData *ritual_ZNK22QQmlDesignerMetaObject23dynamicMetaObjectParentEv(
    const QQmlDesignerMetaObject *self) {
  return self->dynamicMetaObjectParent();
}

//  int QQmlDesignerMetaObject::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlDesignerMetaObject14propertyOffsetEv(
    const QQmlDesignerMetaObject *self) {
  return self->propertyOffset();
}

//  int QQmlDesignerMetaObject::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlDesignerMetaObject5countEv(
    const QQmlDesignerMetaObject *self) {
  return self->count();
}

//  QByteArray QQmlDesignerMetaObject::name(int a0) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QQmlDesignerMetaObject4nameEi(
    const QQmlDesignerMetaObject *self,
    int a0) {
  return new QByteArray(self->name(a0));
}

//  QQmlPropertyCache::Ptr QQmlDesignerMetaObject::cache() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK22QQmlDesignerMetaObject5cacheEv(
    const QQmlDesignerMetaObject *self) {
  return new QQmlPropertyCache::Ptr(self->cache());
}

//  a Python function taken by a CuteQQmlDesignerMetaObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDesignerMetaObject(
    QQmlDesignerMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDesignerMetaObject *>(self)->take(key, call);
}

//  QVariant QQmlDesignerMetaObject::propertyWriteValue(int a0, const
//      QVariant &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN22QQmlDesignerMetaObject18propertyWriteValueEiRK8QVariant(
    QQmlDesignerMetaObject *self,
    int a0,
    const QVariant *a1) {
  return new QVariant(
      static_cast<OwnQQmlDesignerMetaObject *>(self)->OwnQQmlDesignerMetaObject::propertyWriteValue(
          a0,
          *a1));
}

//  a QQmlPropertyCache::Ptr a ritual of QQmlDesignerMetaObject gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDesignerMetaObject__QQmlPropertyCache_Ptr(
    QQmlPropertyCache::Ptr *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_designer)
