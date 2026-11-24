//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmladaptormodel_p.h"
#include <private/qqmldmabstractitemmodeldata_p.h>
#include <private/qqmldmlistaccessordata_p.h>
#include <private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodel.cpp, line 13, as _ZN16QQmlAdaptorModel9AccessorsD2Ev
inline QQmlAdaptorModel::Accessors::~Accessors()
{
}
//  -----------------------------------------------------------------------

//  A QQmlDMObjectDataMetaObject that Python can take functions over in. Every QQmlDMObjectDataMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlDMObjectDataMetaObjectCall0)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlDMObjectDataMetaObjectCall1)(const void *, QObject *, int *);
class CuteQQmlDMObjectDataMetaObject : public QQmlDMObjectDataMetaObject {
public:
  using QQmlDMObjectDataMetaObject::QQmlDMObjectDataMetaObject;
  CuteQQmlDMObjectDataMetaObject(const QQmlDMObjectDataMetaObject &other) : QQmlDMObjectDataMetaObject(other) {}
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
      CuteQQmlDMObjectDataMetaObjectCall0 call = reinterpret_cast<CuteQQmlDMObjectDataMetaObjectCall0>(taken[0]);
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
      CuteQQmlDMObjectDataMetaObjectCall1 call = reinterpret_cast<CuteQQmlDMObjectDataMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QQmlDMObjectDataMetaObject::~QQmlDMObjectDataMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlDMObjectDataMetaObjectD1Ev(
    QQmlDMObjectDataMetaObject *self) {
  delete self;
}

//  int QQmlDMObjectDataMetaObject::createProperty(const char *name, const
//      char *a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQmlDMObjectDataMetaObject14createPropertyEPKcS1_(
    QQmlDMObjectDataMetaObject *self,
    const char *name,
    const char *a1) {
  return self->createProperty(name, a1);
}

//  a Python function taken by a CuteQQmlDMObjectDataMetaObject, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDMObjectDataMetaObject(
    QQmlDMObjectDataMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDMObjectDataMetaObject *>(self)->take(key, call);
}
