//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistmodel_p_p.h>
#include <QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmlnotifier_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstack.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/qdatetime.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1872, as _ZN30DynamicRoleModelNodeMetaObjectD1Ev
inline DynamicRoleModelNodeMetaObject::~DynamicRoleModelNodeMetaObject()
{
    for (int i=0 ; i < count() ; ++i) {
        QQmlListModel *subModel = qobject_cast<QQmlListModel *>(value(i).value<QObject *>());
        delete subModel;
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1880, as _ZN30DynamicRoleModelNodeMetaObject13propertyWriteEi
inline void DynamicRoleModelNodeMetaObject::propertyWrite(int index)
{
    if (!m_enabled)
        return;

    QVariant v = value(index);
    QQmlListModel *model = qobject_cast<QQmlListModel *>(v.value<QObject *>());
    delete model;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1890, as _ZN30DynamicRoleModelNodeMetaObject15propertyWrittenEi
inline void DynamicRoleModelNodeMetaObject::propertyWritten(int index)
{
    if (!m_enabled)
        return;

    QQmlListModel *parentModel = m_owner->m_owner;

    QVariant v = value(index);

    // A JS array/object is translated into a (hierarchical) QQmlListModel,
    // so translate to a variant map/list first with toVariant().
    if (v.userType() == qMetaTypeId<QJSValue>())
        v= v.value<QJSValue>().toVariant();

    if (v.userType() == QMetaType::QVariantList) {
        QQmlListModel *subModel = QQmlListModel::createWithOwner(parentModel);

        QVariantList subArray = v.toList();
        QVariantList::const_iterator subIt = subArray.cbegin();
        QVariantList::const_iterator subEnd = subArray.cend();
        while (subIt != subEnd) {
            const QVariantMap &subObject = subIt->toMap();
            subModel->m_modelObjects.append(DynamicRoleModelNode::create(subObject, subModel));
            ++subIt;
        }

        QObject *subModelObject = subModel;
        v = QVariant::fromValue(subModelObject);

        setValue(index, v);
    }

    int elementIndex = parentModel->m_modelObjects.indexOf(m_owner);
    if (elementIndex != -1) {
        int roleIndex = parentModel->m_roles.indexOf(QString::fromLatin1(name(index).constData()));
        if (roleIndex != -1)
            parentModel->emitItemsChanged(elementIndex, 1, QList<int>(1, roleIndex));
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on DynamicRoleModelNodeMetaObject may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnDynamicRoleModelNodeMetaObject : DynamicRoleModelNodeMetaObject {
  using DynamicRoleModelNodeMetaObject::propertyWrite;
};

//  A DynamicRoleModelNodeMetaObject that Python can take functions over in. Every DynamicRoleModelNodeMetaObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_list_model)
typedef void (*CuteDynamicRoleModelNodeMetaObjectCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
typedef void (*CuteDynamicRoleModelNodeMetaObjectCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_list_model)
typedef const QVariant * (*CuteDynamicRoleModelNodeMetaObjectCall2)(const void *, int, int *);
typedef void (*CuteDynamicRoleModelNodeMetaObjectCall3)(const void *, int, int *);
typedef const QVariant * (*CuteDynamicRoleModelNodeMetaObjectCall4)(const void *, int, const QVariant *, int *);
#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void * (*CuteDynamicRoleModelNodeMetaObjectCall5)(const void *, QObject *, int *);
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
typedef void (*CuteDynamicRoleModelNodeMetaObjectCall6)(const void *, QObject *, int *);
class CuteDynamicRoleModelNodeMetaObject : public DynamicRoleModelNodeMetaObject {
public:
  using DynamicRoleModelNodeMetaObject::DynamicRoleModelNodeMetaObject;
  CuteDynamicRoleModelNodeMetaObject(const DynamicRoleModelNodeMetaObject &other) : DynamicRoleModelNodeMetaObject(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_list_model)
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject13propertyWriteEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject15propertyWrittenEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_list_model)
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12initialValueEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject12propertyReadEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant")) {
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

#if QT_CONFIG(qml_list_model)
  //  void DynamicRoleModelNodeMetaObject::propertyWrite(int index)
  void propertyWrite(int index) override {
    if (taken[0]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall0 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    DynamicRoleModelNodeMetaObject::propertyWrite(index);
  }
#endif  // QT_CONFIG(qml_list_model)

#if QT_CONFIG(qml_list_model)
  //  void DynamicRoleModelNodeMetaObject::propertyWritten(int index)
  void propertyWritten(int index) override {
    if (taken[1]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall1 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall1>(taken[1]);
      call(this, index, &handled);
      if (handled) return;
    }
    DynamicRoleModelNodeMetaObject::propertyWritten(index);
  }
#endif  // QT_CONFIG(qml_list_model)

  //  QVariant QQmlOpenMetaObject::initialValue(int a0)
  QVariant initialValue(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall2 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall2>(taken[2]);
      const QVariant * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::initialValue(a0);
  }

  //  void QQmlOpenMetaObject::propertyRead(int a0)
  void propertyRead(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall3 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlOpenMetaObject::propertyRead(a0);
  }

  //  QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const
  //      QVariant &a1)
  QVariant propertyWriteValue(int a0, const QVariant &a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall4 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall4>(taken[4]);
      const QVariant * given = call(this, a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlOpenMetaObject::propertyWriteValue(a0, a1);
  }

#if !(QT_VERSION >= QT_VERSION_CHECK(7, 0, 0))
  //  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject
  //      *a0)
  QMetaObject *toDynamicMetaObject(QObject *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteDynamicRoleModelNodeMetaObjectCall5 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall5>(taken[5]);
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
      CuteDynamicRoleModelNodeMetaObjectCall6 call = reinterpret_cast<CuteDynamicRoleModelNodeMetaObjectCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDynamicMetaObjectData::objectDestroyed(a0);
  }
};

//  DynamicRoleModelNodeMetaObject::~DynamicRoleModelNodeMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DynamicRoleModelNodeMetaObjectD1Ev(
    DynamicRoleModelNodeMetaObject *self) {
  delete self;
}

//  void DynamicRoleModelNodeMetaObject::propertyWrite(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DynamicRoleModelNodeMetaObject13propertyWriteEi(
    DynamicRoleModelNodeMetaObject *self,
    int index) {
  self->propertyWrite(index);
}

//  void DynamicRoleModelNodeMetaObject::propertyWritten(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DynamicRoleModelNodeMetaObject15propertyWrittenEi(
    DynamicRoleModelNodeMetaObject *self,
    int index) {
  self->propertyWritten(index);
}

//  a Python function taken by a CuteDynamicRoleModelNodeMetaObject, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DynamicRoleModelNodeMetaObject(
    DynamicRoleModelNodeMetaObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteDynamicRoleModelNodeMetaObject *>(self)->take(key, call);
}

//  void DynamicRoleModelNodeMetaObject::propertyWrite(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30DynamicRoleModelNodeMetaObject13propertyWriteEi(
    DynamicRoleModelNodeMetaObject *self,
    int index) {
  static_cast<OwnDynamicRoleModelNodeMetaObject *>(self)->OwnDynamicRoleModelNodeMetaObject::propertyWrite(
      index);
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
