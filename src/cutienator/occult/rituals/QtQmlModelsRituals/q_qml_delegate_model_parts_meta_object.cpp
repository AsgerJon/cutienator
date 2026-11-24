//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmldelegatemodel_p_p.h"
#include <QtQml/qqmlinfo.h>
#include <private/qabstractitemmodel_p.h>
#include <private/qcoreapplication_p.h>
#include <private/qjsvalue_p.h>
#include <private/qmetaobjectbuilder_p.h>
#include <private/qqmlabstractdelegatecomponent_p.h>
#include <private/qqmladaptormodel_p.h>
#include <private/qqmlanybinding_p.h>
#include <private/qqmlchangeset_p.h>
#include <private/qqmlcomponent_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlpropertytopropertybinding_p.h>
#include <private/qqmltableinstancemodel_p.h>
#include <private/qquickpackage_p.h>
#include <private/qv4functionobject_p.h>
#include <private/qv4objectiterator_p.h>
#include <private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3718, as _ZN14QQmlPartsModelC1EP17QQmlDelegateModelRK7QStringP7QObject
inline QQmlPartsModel::QQmlPartsModel(QQmlDelegateModel *model, const QString &part, QObject *parent)
    : QQmlInstanceModel(*new QObjectPrivate, parent)
    , m_model(model)
    , m_part(part)
    , m_compositorGroup(Compositor::Cache)
    , m_inheritGroup(true)
{
    QQmlDelegateModelPrivate *d = QQmlDelegateModelPrivate::get(m_model);
    if (d->m_cacheMetaType) {
        QQmlDelegateModelGroupPrivate::get(d->m_groups[1])->emitters.insert(this);
        m_compositorGroup = Compositor::Default;
    } else {
        d->m_pendingParts.insert(this);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 116, as _ZN32QQmlDelegateModelPartsMetaObject15propertyCreatedEiR20QMetaPropertyBuilder
inline void QQmlDelegateModelPartsMetaObject::propertyCreated(int, QMetaPropertyBuilder &prop)
{
    prop.setWritable(false);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 121, as _ZN32QQmlDelegateModelPartsMetaObject12initialValueEi
inline QVariant QQmlDelegateModelPartsMetaObject::initialValue(int id)
{
    QQmlDelegateModelParts *parts = static_cast<QQmlDelegateModelParts *>(object());
    QQmlPartsModel *m = new QQmlPartsModel(
            parts->model, QString::fromUtf8(name(id)), parts);
    parts->models.append(m);
    return QVariant::fromValue(static_cast<QObject *>(m));
}
//  -----------------------------------------------------------------------

//  A QQmlDelegateModelPartsMetaObject that Python can take functions over in. Every QQmlDelegateModelPartsMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef const QVariant * (*CuteQQmlDelegateModelPartsMetaObjectCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelPartsMetaObjectCall1)(const void *, int, int *);
typedef void (*CuteQQmlDelegateModelPartsMetaObjectCall2)(const void *, int, int *);
typedef const QVariant * (*CuteQQmlDelegateModelPartsMetaObjectCall3)(const void *, int, const QVariant *, int *);
typedef void (*CuteQQmlDelegateModelPartsMetaObjectCall4)(const void *, int, int *);
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteQQmlDelegateModelPartsMetaObjectCall5)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteQQmlDelegateModelPartsMetaObjectCall6)(const void *, QObject *, int *);
class CuteQQmlDelegateModelPartsMetaObject : public QQmlDelegateModelPartsMetaObject {
public:
  using QQmlDelegateModelPartsMetaObject::QQmlDelegateModelPartsMetaObject;
  CuteQQmlDelegateModelPartsMetaObject(const QQmlDelegateModelPartsMetaObject &other) : QQmlDelegateModelPartsMetaObject(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12initialValueEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
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

#if QT_CONFIG(qml_delegate_model)
  //  QVariant QQmlDelegateModelPartsMetaObject::initialValue(int a0)
  QVariant initialValue(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsMetaObjectCall0 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall0>(taken[0]);
      const QVariant * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QQmlDelegateModelPartsMetaObject::initialValue(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)

  //  void QQmlOpenMetaObject::propertyRead(int a0)
  void propertyRead(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsMetaObjectCall1 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyRead(a0);
  }

  //  void QQmlOpenMetaObject::propertyWrite(int a0)
  void propertyWrite(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsMetaObjectCall2 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall2>(taken[2]);
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
      CuteQQmlDelegateModelPartsMetaObjectCall3 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall3>(taken[3]);
      const QVariant * given = call(this, a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::propertyWriteValue(a0, a1);
  }

  //  void QQmlOpenMetaObject::propertyWritten(int a0)
  void propertyWritten(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDelegateModelPartsMetaObjectCall4 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall4>(taken[4]);
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
      CuteQQmlDelegateModelPartsMetaObjectCall5 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall5>(taken[5]);
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
      CuteQQmlDelegateModelPartsMetaObjectCall6 call = reinterpret_cast<CuteQQmlDelegateModelPartsMetaObjectCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  QVariant QQmlDelegateModelPartsMetaObject::initialValue(int a0)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN32QQmlDelegateModelPartsMetaObject12initialValueEi(
    QQmlDelegateModelPartsMetaObject *self,
    int a0) {
  return new QVariant(self->initialValue(a0));
}

//  QQmlDelegateModelPartsMetaObject::~QQmlDelegateModelPartsMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQmlDelegateModelPartsMetaObjectD1Ev(
    QQmlDelegateModelPartsMetaObject *self) {
  delete self;
}

//  a Python function taken by a CuteQQmlDelegateModelPartsMetaObject, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelPartsMetaObject(
    QQmlDelegateModelPartsMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelPartsMetaObject *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
