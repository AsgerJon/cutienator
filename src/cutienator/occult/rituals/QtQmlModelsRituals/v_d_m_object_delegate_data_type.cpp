//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
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
//  -----------------------------------------------------------------------

//  int VDMObjectDelegateDataType::rowCount(const QQmlAdaptorModel &model)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25VDMObjectDelegateDataType8rowCountERK16QQmlAdaptorModel(
    const VDMObjectDelegateDataType *self,
    const QQmlAdaptorModel *model) {
  return self->rowCount(*model);
}

//  int VDMObjectDelegateDataType::columnCount(const QQmlAdaptorModel &a0)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25VDMObjectDelegateDataType11columnCountERK16QQmlAdaptorModel(
    const VDMObjectDelegateDataType *self,
    const QQmlAdaptorModel *a0) {
  return self->columnCount(*a0);
}

//  QVariant VDMObjectDelegateDataType::value(const QQmlAdaptorModel &model,
//      int index, const QString &role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25VDMObjectDelegateDataType5valueERK16QQmlAdaptorModeliRK7QString(
    const VDMObjectDelegateDataType *self,
    const QQmlAdaptorModel *model,
    int index,
    const QString *role) {
  return new QVariant(self->value(*model, index, *role));
}

//  void VDMObjectDelegateDataType::cleanup(QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25VDMObjectDelegateDataType7cleanupER16QQmlAdaptorModel(
    const VDMObjectDelegateDataType *self,
    QQmlAdaptorModel *a0) {
  self->cleanup(*a0);
}

//  VDMObjectDelegateDataType::~VDMObjectDelegateDataType()
extern "C" Q_DECL_EXPORT
void ritual_ZN25VDMObjectDelegateDataTypeD1Ev(
    VDMObjectDelegateDataType *self) {
  delete self;
}

//  VDMObjectDelegateDataType as the QQmlAdaptorModel::Accessors it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlAdaptorModel::Accessors *ritual_cast_VDMObjectDelegateDataType_QQmlAdaptorModel_Accessors(
    VDMObjectDelegateDataType *self) {
  return static_cast<QQmlAdaptorModel::Accessors *>(self);
}

#endif  // QT_CONFIG(qml_delegate_model)
