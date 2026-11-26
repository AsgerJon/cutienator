//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodelenginedata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodelenginedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldmlistaccessordata.cpp, line 27, as _ZN22QQmlDMListAccessorData12setModelDataERK8QVariant
inline void QQmlDMListAccessorData::setModelData(const QVariant &data) {
    if (data == cachedData)
        return;

    cachedData = data;
    cachedDataClean = false;
    static_cast<const VDMListDelegateDataType *>(QObjectPrivate::get(this)->metaObject)
            ->emitAllSignals(this);
}
//  -----------------------------------------------------------------------

//  void QQmlAdaptorModelEngineData::addProperty(QMetaObjectBuilder *builder,
//      int propertyId, const QByteArray &propertyName, const QByteArray
//      &propertyType, bool isWritable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlAdaptorModelEngineData11addPropertyEP18QMetaObjectBuilderiRK10QByteArrayS4_b(
    QMetaObjectBuilder *builder,
    int propertyId,
    const QByteArray *propertyName,
    const QByteArray *propertyType,
    bool isWritable) {
  QQmlAdaptorModelEngineData::addProperty(
      builder,
      propertyId,
      *propertyName,
      *propertyType,
      isWritable);
}

//  QQmlAdaptorModelEngineData::~QQmlAdaptorModelEngineData()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlAdaptorModelEngineDataD1Ev(
    QQmlAdaptorModelEngineData *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
