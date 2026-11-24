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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmobjectdata_p.h>
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

//  void VDMAbstractItemModelDataType::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28VDMAbstractItemModelDataType15objectDestroyedEP7QObject(
    VDMAbstractItemModelDataType *self,
    QObject *a0) {
  self->objectDestroyed(a0);
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
