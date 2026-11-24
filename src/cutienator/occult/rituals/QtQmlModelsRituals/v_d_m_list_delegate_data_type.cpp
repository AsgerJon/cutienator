//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmladaptormodel_p.h"
#include <private/qqmldmabstractitemmodeldata_p.h>
#include <private/qqmldmlistaccessordata_p.h>
#include <private/qqmldmobjectdata_p.h>
#include <private/qqmldmlistaccessordata_p.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldmlistaccessordata.cpp, line 115, as _ZN23VDMListDelegateDataType14createPropertyEPKcS1_
inline int VDMListDelegateDataType::createProperty(const char *name, const char *)
{
    const int propertyIndex = propertyCount() - propertyOffset;

    // We use QVariant because the types may be different in the different objects.
    QQmlAdaptorModelEngineData::addProperty(
            &builder, propertyIndex, name, QByteArrayLiteral("QVariant"),
            model->delegateModelAccess != QQmlDelegateModel::ReadOnly);

    metaObject.reset(builder.toMetaObject());
    *static_cast<QMetaObject *>(this) = *metaObject;
    return propertyIndex + propertyOffset;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *VDMListDelegateDataType::metaObjectFromType(QMetaType
//      type)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN23VDMListDelegateDataType18metaObjectFromTypeE9QMetaType(
    const QMetaType *type) {
  return VDMListDelegateDataType::metaObjectFromType(*type);
}

//  void VDMListDelegateDataType::createMissingProperties(const QVariant
//      *row)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType23createMissingPropertiesEPK8QVariant(
    VDMListDelegateDataType *self,
    const QVariant *row) {
  self->createMissingProperties(row);
}

//  int VDMListDelegateDataType::createProperty(const char *name, const char
//      *a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN23VDMListDelegateDataType14createPropertyEPKcS1_(
    VDMListDelegateDataType *self,
    const char *name,
    const char *a1) {
  return self->createProperty(name, a1);
}

//  VDMListDelegateDataType as the QQmlAdaptorModel::Accessors it is built on
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel::Accessors *ritual_cast_VDMListDelegateDataType_QQmlAdaptorModel_Accessors(
    VDMListDelegateDataType *self) {
  return static_cast<QQmlAdaptorModel::Accessors *>(self);
}

//  VDMListDelegateDataType as the QAbstractDynamicMetaObject it is built on
extern "C" Q_DECL_EXPORT
QAbstractDynamicMetaObject *ritual_cast_VDMListDelegateDataType_QAbstractDynamicMetaObject(
    VDMListDelegateDataType *self) {
  return static_cast<QAbstractDynamicMetaObject *>(self);
}
