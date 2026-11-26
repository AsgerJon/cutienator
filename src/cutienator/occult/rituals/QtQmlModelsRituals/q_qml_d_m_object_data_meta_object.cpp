//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#include <QtQmlModels/private/qqmllistaccessor_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetasequence.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qurl.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldmobjectdata.cpp, line 9, as _ZN16QQmlDMObjectDataC1ERK14QQmlRefPointerI29QQmlDelegateModelItemMetaTypeEP25VDMObjectDelegateDataTypeiiiP7QObject
inline QQmlDMObjectData::QQmlDMObjectData(const QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType,
        VDMObjectDelegateDataType *dataType,
        int index, int row, int column,
        QObject *object)
    : QQmlDelegateModelItem(metaType, dataType, index, row, column)
    , m_modelData(object)
{
    new QQmlDMObjectDataMetaObject(this, dataType);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 183, as _ZNK16QQmlListAccessor2atEx
inline QVariant QQmlListAccessor::at(qsizetype idx) const
{
    Q_ASSERT(idx >= 0 && idx < count());
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return QVariant::fromValue(reinterpret_cast<const QStringList *>(d.constData())->at(idx));
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QUrl> *>(d.constData())->at(idx));
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->at(idx);
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return QVariant::fromValue(reinterpret_cast<const QList<QObject *> *>(d.constData())->at(idx));
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return QVariant::fromValue(reinterpret_cast<const QQmlListReference *>(d.constData())->at(idx));
    case ValueSequence:
    case ObjectSequence: {
        Q_ASSERT(m_metaSequence != QMetaSequence());
        QVariant result;
        const QMetaType valueMetaType = m_metaSequence.valueMetaType();
        if (valueMetaType == QMetaType::fromType<QVariant>()) {
            m_metaSequence.valueAtIndex(d.constData(), idx, &result);
        } else {
            result = QVariant(valueMetaType);
            m_metaSequence.valueAtIndex(d.constData(), idx, result.data());
        }
        return result;
    }
    case Instance:
        return d;
    case Integer:
        return QVariant(idx);
    case Invalid:
        return QVariant();
    }
    Q_UNREACHABLE_RETURN(QVariant());
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistaccessor.cpp, line 151, as _ZNK16QQmlListAccessor5countEv
inline qsizetype QQmlListAccessor::count() const
{
    switch(m_type) {
    case StringList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QStringList>());
        return reinterpret_cast<const QStringList *>(d.constData())->size();
    case UrlList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QUrl>>());
        return reinterpret_cast<const QList<QUrl> *>(d.constData())->size();
    case VariantList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QVariantList>());
        return reinterpret_cast<const QVariantList *>(d.constData())->size();
    case ObjectList:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QList<QObject *>>());
        return reinterpret_cast<const QList<QObject *> *>(d.constData())->size();
    case ListProperty:
        Q_ASSERT(d.metaType() == QMetaType::fromType<QQmlListReference>());
        return reinterpret_cast<const QQmlListReference *>(d.constData())->count();
    case ValueSequence:
    case ObjectSequence:
        Q_ASSERT(m_metaSequence != QMetaSequence());
        return m_metaSequence.size(d.constData());
    case Instance:
        return 1;
    case Integer:
        return *reinterpret_cast<const int *>(d.constData());
    case Invalid:
        return 0;
    }
    Q_UNREACHABLE_RETURN(0);
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
  CuteQQmlDMObjectDataMetaObject(const QQmlDMObjectDataMetaObject & other) : QQmlDMObjectDataMetaObject(other) {}
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

//  QQmlDMObjectDataMetaObject::QQmlDMObjectDataMetaObject(QQmlDMObjectData
//      *data, VDMObjectDelegateDataType *type)
extern "C" Q_DECL_EXPORT
QQmlDMObjectDataMetaObject *ritual_ZN26QQmlDMObjectDataMetaObjectC1EP16QQmlDMObjectDataP25VDMObjectDelegateDataType(
    QQmlDMObjectData *data,
    VDMObjectDelegateDataType *type) {
  return new CuteQQmlDMObjectDataMetaObject(data, type);
}

//  QQmlDMObjectDataMetaObject::~QQmlDMObjectDataMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlDMObjectDataMetaObjectD1Ev(
    QQmlDMObjectDataMetaObject *self) {
  delete self;
}

//  int QQmlDMObjectDataMetaObject::metaCall(QObject *o, QMetaObject::Call
//      call, int id, void **arguments)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQmlDMObjectDataMetaObject8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QQmlDMObjectDataMetaObject *self,
    QObject *o,
    QMetaObject::Call call,
    int id,
    void **arguments) {
  return self->metaCall(o, call, id, arguments);
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

#endif  // QT_CONFIG(qml_delegate_model)
