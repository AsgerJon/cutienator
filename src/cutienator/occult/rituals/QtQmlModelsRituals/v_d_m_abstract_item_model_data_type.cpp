//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmabstractitemmodeldata_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 95, as _ZN27QQmlDMAbstractItemModelData12get_propertyEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i
inline QV4::ReturnedValue QQmlDMAbstractItemModelData::get_property(const QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value *, int)
{
    QV4::Scope scope(b);
    QV4::Scoped<QQmlDelegateModelItemObject> o(scope, thisObject->as<QQmlDelegateModelItemObject>());
    if (!o)
        return scope.engine->throwTypeError(QStringLiteral("Not a valid DelegateModel object"));

    const qsizetype propertyId = static_cast<const QV4::IndexedBuiltinFunction *>(b)->d()->index;

    QQmlDelegateModelItem *item = o->d()->item();
    QQmlDMAbstractItemModelData *modelData = static_cast<QQmlDMAbstractItemModelData *>(item);
    if (item->modelIndex() == -1) {
        if (!modelData->m_cachedData.isEmpty())
            return scope.engine->fromVariant(modelData->m_cachedData.at(propertyId));
    } else if (*modelData->m_type->model) {
        return scope.engine->fromVariant(
                modelData->value(modelData->m_type->propertyRoles.at(propertyId)));
    }
    return QV4::Encode::undefined();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 116, as _ZN27QQmlDMAbstractItemModelData12set_propertyEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i
inline QV4::ReturnedValue QQmlDMAbstractItemModelData::set_property(const QV4::FunctionObject *b, const QV4::Value *thisObject, const QV4::Value *argv, int argc)
{
    QV4::Scope scope(b);
    QV4::Scoped<QQmlDelegateModelItemObject> o(scope, thisObject->as<QQmlDelegateModelItemObject>());
    if (!o)
        return scope.engine->throwTypeError(QStringLiteral("Not a valid DelegateModel object"));
    if (!argc)
        return scope.engine->throwTypeError();

    const qsizetype propertyId = static_cast<const QV4::IndexedBuiltinFunction *>(b)->d()->index;

    QQmlDelegateModelItem *item = o->d()->item();
    if (item->modelIndex() == -1) {
        QQmlDMAbstractItemModelData *modelData = static_cast<QQmlDMAbstractItemModelData *>(item);
        if (!modelData->m_cachedData.isEmpty()) {
            if (modelData->m_cachedData.size() > 1) {
                modelData->m_cachedData[propertyId]
                        = QV4::ExecutionEngine::toVariant(argv[0], QMetaType {});
                QMetaObject::activate(item, item->metaObject(), propertyId, nullptr);
            } else if (modelData->m_cachedData.size() == 1) {
                modelData->m_cachedData[0] = QV4::ExecutionEngine::toVariant(argv[0], QMetaType {});
                QMetaObject::activate(item, item->metaObject(), 0, nullptr);
            }
            emit modelData->modelDataChanged();
        }
    }
    return QV4::Encode::undefined();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 145, as _ZN27QQmlDMAbstractItemModelData13get_modelDataEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i
inline QV4::ReturnedValue QQmlDMAbstractItemModelData::get_modelData(
        const QV4::FunctionObject *b, const QV4::Value *thisObject,
        const QV4::Value *argv, int argc)
{
    Q_UNUSED(argv)
    Q_UNUSED(argc)

    QV4::Scope scope(b);
    QV4::Scoped<QQmlDelegateModelItemObject> o(
                scope, thisObject->as<QQmlDelegateModelItemObject>());
    if (!o)
        return scope.engine->throwTypeError(QStringLiteral("Not a valid DelegateModel object"));

    return scope.engine->fromVariant(
            static_cast<QQmlDMAbstractItemModelData *>(o->d()->item())->modelData());
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 162, as _ZN27QQmlDMAbstractItemModelData13set_modelDataEPKN3QV414FunctionObjectEPKNS0_5ValueES6_i
inline QV4::ReturnedValue QQmlDMAbstractItemModelData::set_modelData(
        const QV4::FunctionObject *b, const QV4::Value *thisObject,
        const QV4::Value *argv, int argc)
{
    QV4::Scope scope(b);
    QV4::Scoped<QQmlDelegateModelItemObject> o(scope, thisObject->as<QQmlDelegateModelItemObject>());
    if (!o)
        return scope.engine->throwTypeError(QStringLiteral("Not a valid DelegateModel object"));
    if (!argc)
        return scope.engine->throwTypeError();

    static_cast<QQmlDMAbstractItemModelData *>(o->d()->item())->setModelData(
                QV4::ExecutionEngine::toVariant(argv[0], QMetaType()));

    return QV4::Encode::undefined();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 23, as _ZN27QQmlDMAbstractItemModelData8metaCallEN11QMetaObject4CallEiPPv
inline int QQmlDMAbstractItemModelData::metaCall(QMetaObject::Call call, int id, void **arguments)
{
    if (call == QMetaObject::ReadProperty && id >= m_type->propertyOffset) {
        const int propertyIndex = id - m_type->propertyOffset;
        if (!hasValidModelIndex()) {
            if (!m_cachedData.isEmpty())
                *static_cast<QVariant *>(arguments[0]) = m_cachedData.at(propertyIndex);
        } else if (*m_type->model) {
            *static_cast<QVariant *>(arguments[0]) = value(m_type->propertyRoles.at(propertyIndex));
        }
        return -1;
    } else if (call == QMetaObject::WriteProperty && id >= m_type->propertyOffset) {
        const int propertyIndex = id - m_type->propertyOffset;
        const QMetaObject *meta = metaObject();
        if (!hasValidModelIndex()) {
            if (m_cachedData.size() > 1) {
                m_cachedData[propertyIndex] = *static_cast<QVariant *>(arguments[0]);
                QMetaObject::activate(this, meta, propertyIndex, nullptr);
            } else if (m_cachedData.size() == 1) {
                m_cachedData[0] = *static_cast<QVariant *>(arguments[0]);
                QMetaObject::activate(this, meta, 0, nullptr);
            }

            emit modelDataChanged();
        } else if (*m_type->model) {
            setValue(m_type->propertyRoles.at(propertyIndex),
                     *static_cast<QVariant *>(arguments[0]));
        }
        return -1;
    } else {
        return qt_metacall(call, id, arguments);
    }
}
//  -----------------------------------------------------------------------

//  void VDMAbstractItemModelDataType::notifyItems(const
//      QVarLengthArray<QQmlGuard<QQmlDMAbstractItemModelData>>
//      &guardedItems, int index, QQmlDelegateModel::DelegateModelAccess
//      access) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28VDMAbstractItemModelDataType11notifyItemsERK15QVarLengthArrayI9QQmlGuardI27QQmlDMAbstractItemModelDataELx256EEiN17QQmlDelegateModel19DelegateModelAccessE(
    const VDMAbstractItemModelDataType *self,
    const QVarLengthArray<QQmlGuard<QQmlDMAbstractItemModelData>> *guardedItems,
    int index,
    QQmlDelegateModel::DelegateModelAccess access) {
  self->notifyItems(*guardedItems, index, access);
}

//  void VDMAbstractItemModelDataType::replaceWatchedRoles(QQmlAdaptorModel
//      &a0, const QList<QByteArray> &oldRoles, const QList<QByteArray>
//      &newRoles) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28VDMAbstractItemModelDataType19replaceWatchedRolesER16QQmlAdaptorModelRK5QListI10QByteArrayES6_(
    const VDMAbstractItemModelDataType *self,
    QQmlAdaptorModel *a0,
    const QList<QByteArray> *oldRoles,
    const QList<QByteArray> *newRoles) {
  self->replaceWatchedRoles(*a0, *oldRoles, *newRoles);
}

//  void VDMAbstractItemModelDataType::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28VDMAbstractItemModelDataType15objectDestroyedEP7QObject(
    VDMAbstractItemModelDataType *self,
    QObject *a0) {
  self->objectDestroyed(a0);
}

//  int VDMAbstractItemModelDataType::rowCount(const QQmlAdaptorModel &model)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28VDMAbstractItemModelDataType8rowCountERK16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    const QQmlAdaptorModel *model) {
  return self->rowCount(*model);
}

//  int VDMAbstractItemModelDataType::columnCount(const QQmlAdaptorModel
//      &model) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28VDMAbstractItemModelDataType11columnCountERK16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    const QQmlAdaptorModel *model) {
  return self->columnCount(*model);
}

//  void VDMAbstractItemModelDataType::cleanup(QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28VDMAbstractItemModelDataType7cleanupER16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    QQmlAdaptorModel *a0) {
  self->cleanup(*a0);
}

//  QVariant VDMAbstractItemModelDataType::parentModelIndex(const
//      QQmlAdaptorModel &model) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28VDMAbstractItemModelDataType16parentModelIndexERK16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    const QQmlAdaptorModel *model) {
  return new QVariant(self->parentModelIndex(*model));
}

//  QVariant VDMAbstractItemModelDataType::modelIndex(const QQmlAdaptorModel
//      &model, int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28VDMAbstractItemModelDataType10modelIndexERK16QQmlAdaptorModeli(
    const VDMAbstractItemModelDataType *self,
    const QQmlAdaptorModel *model,
    int index) {
  return new QVariant(self->modelIndex(*model, index));
}

//  bool VDMAbstractItemModelDataType::canFetchMore(const QQmlAdaptorModel
//      &model) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28VDMAbstractItemModelDataType12canFetchMoreERK16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    const QQmlAdaptorModel *model) {
  return self->canFetchMore(*model);
}

//  void VDMAbstractItemModelDataType::fetchMore(QQmlAdaptorModel &model)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28VDMAbstractItemModelDataType9fetchMoreER16QQmlAdaptorModel(
    const VDMAbstractItemModelDataType *self,
    QQmlAdaptorModel *model) {
  self->fetchMore(*model);
}

//  VDMAbstractItemModelDataType as the QQmlAdaptorModel::Accessors it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel::Accessors *ritual_cast_VDMAbstractItemModelDataType_QQmlAdaptorModel_Accessors(
    VDMAbstractItemModelDataType *self) {
  return static_cast<QQmlAdaptorModel::Accessors *>(self);
}

//  VDMAbstractItemModelDataType as the QAbstractDynamicMetaObject it is
//      built on
extern "C" Q_DECL_EXPORT
QAbstractDynamicMetaObject *ritual_cast_VDMAbstractItemModelDataType_QAbstractDynamicMetaObject(
    VDMAbstractItemModelDataType *self) {
  return static_cast<QAbstractDynamicMetaObject *>(self);
}

#endif  // QT_CONFIG(qml_delegate_model)
