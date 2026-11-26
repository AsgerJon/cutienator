//  Written by hand on 2026-11-25 from
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h, Qt
//  6.12.0, from Qt's source. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name (no export macro on the
//  class line): only its inline functions and its virtual functions are
//  called. The class is final, so for the virtual functions 'self' is taken
//  as the base that declares them (QQmlAdaptorModel::Accessors or
//  QAbstractDynamicMetaObject), and the calls stay virtual. Of the two
//  declarations of 'toDynamicMetaObject' the one Qt 6 builds is written (the
//  other stands under QT_VERSION 7). 'createProperty' is taken from Qt's
//  source as an inline function: 'createMissingProperties' calls it, and as
//  the class is final the compiler calls it by name, which Qt's library does
//  not carry. Not written: the constructor; 'notify' (a QList);
//  'emitAllSignals' (not inline, not exported); the member templates
//  'toQString', 'toUtf8', 'value', 'createPropertyIfMissing' and 'setValue'.
//  Also added by hand on 2026-11-25, instances of templates of the class:
//  15.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  VDMListDelegateDataType::~VDMListDelegateDataType()
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataTypeD1Ev(
    QQmlAdaptorModel::Accessors *self) {
  delete self;
}

//  void VDMListDelegateDataType::cleanup(QQmlAdaptorModel &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23VDMListDelegateDataType7cleanupER16QQmlAdaptorModel(
    const QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *a0) {
  self->cleanup(*a0);
}

//  int VDMListDelegateDataType::rowCount(const QQmlAdaptorModel &model)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23VDMListDelegateDataType8rowCountERK16QQmlAdaptorModel(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *model) {
  return self->rowCount(*model);
}

//  int VDMListDelegateDataType::columnCount(const QQmlAdaptorModel &model)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23VDMListDelegateDataType11columnCountERK16QQmlAdaptorModel(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *model) {
  return self->columnCount(*model);
}

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

//  QVariant VDMListDelegateDataType::value(const QQmlAdaptorModel &model,
//      int index, const QString &role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23VDMListDelegateDataType5valueERK16QQmlAdaptorModeliRK7QString(
    const QQmlAdaptorModel::Accessors *self,
    const QQmlAdaptorModel *model,
    int index,
    const QString *role) {
  return new QVariant(self->value(*model, index, *role));
}

//  QQmlDelegateModelItem *VDMListDelegateDataType::createItem(
//      QQmlAdaptorModel &model, const
//      QQmlRefPointer<QQmlDelegateModelItemMetaType> &metaType, int index,
//      int row, int column)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN23VDMListDelegateDataType10createItemER16QQmlAdaptorModelRK14QQmlRefPointerI29QQmlDelegateModelItemMetaTypeEiii(
    QQmlAdaptorModel::Accessors *self,
    QQmlAdaptorModel *model,
    const QQmlRefPointer<QQmlDelegateModelItemMetaType> *metaType,
    int index,
    int row,
    int column) {
  return self->createItem(*model, *metaType, index, row, column);
}

//  int VDMListDelegateDataType::metaCall(QObject *object,
//      QMetaObject::Call call, int id, void **arguments)
extern "C" Q_DECL_EXPORT
int ritual_ZN23VDMListDelegateDataType8metaCallEP7QObjectN11QMetaObject4CallEiPPv(
    QAbstractDynamicMetaObject *self,
    QObject *object,
    QMetaObject::Call call,
    int id,
    void **arguments) {
  return self->metaCall(object, call, id, arguments);
}

//  int VDMListDelegateDataType::createProperty(const char *name, const char
//      *a1)
extern "C" Q_DECL_EXPORT
int ritual_ZN23VDMListDelegateDataType14createPropertyEPKcS1_(
    QAbstractDynamicMetaObject *self,
    const char *name,
    const char *a1) {
  return self->createProperty(name, a1);
}

//  QMetaObject *VDMListDelegateDataType::toDynamicMetaObject(QObject
//      *accessors)
extern "C" Q_DECL_EXPORT
QMetaObject *ritual_ZN23VDMListDelegateDataType18toDynamicMetaObjectEP7QObject(
    QAbstractDynamicMetaObject *self,
    QObject *accessors) {
  return self->toDynamicMetaObject(accessors);
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

//  static QString VDMListDelegateDataType::toQString<QString>(const QString
//      &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23VDMListDelegateDataType9toQStringI7QStringEES1_RKT_(
    const QString *string) {
  return new QString(VDMListDelegateDataType::toQString<QString>(*string));
}

//  static QString VDMListDelegateDataType::toQString<QByteArray>(const
//      QByteArray &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23VDMListDelegateDataType9toQStringI10QByteArrayEE7QStringRKT_(
    const QByteArray *string) {
  return new QString(VDMListDelegateDataType::toQString<QByteArray>(*string));
}

//  static QString VDMListDelegateDataType::toQString<const char *>(const
//      const char * &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23VDMListDelegateDataType9toQStringIPKcEE7QStringRKT_(
    const char *string) {
  return new QString(VDMListDelegateDataType::toQString<const char *>(string));
}

//  static QByteArray VDMListDelegateDataType::toUtf8<QString>(const QString
//      &string)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN23VDMListDelegateDataType6toUtf8I7QStringEE10QByteArrayRKT_(
    const QString *string) {
  return new QByteArray(VDMListDelegateDataType::toUtf8<QString>(*string));
}

//  static QByteArray VDMListDelegateDataType::toUtf8<QByteArray>(const
//      QByteArray &string)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN23VDMListDelegateDataType6toUtf8I10QByteArrayEES1_RKT_(
    const QByteArray *string) {
  return new QByteArray(VDMListDelegateDataType::toUtf8<QByteArray>(*string));
}

//  static QByteArray VDMListDelegateDataType::toUtf8<const char *>(const
//      const char * &string)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN23VDMListDelegateDataType6toUtf8IPKcEE10QByteArrayRKT_(
    const char *string) {
  return new QByteArray(VDMListDelegateDataType::toUtf8<const char *>(string));
}

//  static QVariant VDMListDelegateDataType::value<QString>(const QVariant
//      *row, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23VDMListDelegateDataType5valueI7QStringEE8QVariantPKS2_RKT_(
    const QVariant *row,
    const QString *role) {
  return new QVariant(VDMListDelegateDataType::value<QString>(row, *role));
}

//  static QVariant VDMListDelegateDataType::value<QByteArray>(const QVariant
//      *row, const QByteArray &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23VDMListDelegateDataType5valueI10QByteArrayEE8QVariantPKS2_RKT_(
    const QVariant *row,
    const QByteArray *role) {
  return new QVariant(VDMListDelegateDataType::value<QByteArray>(row, *role));
}

//  static QVariant VDMListDelegateDataType::value<const char *>(const
//      QVariant *row, const const char * &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23VDMListDelegateDataType5valueIPKcEE8QVariantPKS3_RKT_(
    const QVariant *row,
    const char *role) {
  return new QVariant(VDMListDelegateDataType::value<const char *>(row, role));
}

//  void VDMListDelegateDataType::createPropertyIfMissing<QString>(const
//      QString &string)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType23createPropertyIfMissingI7QStringEEvRKT_(
    VDMListDelegateDataType *self,
    const QString *string) {
  self->createPropertyIfMissing<QString>(*string);
}

//  void VDMListDelegateDataType::createPropertyIfMissing<QByteArray>(const
//      QByteArray &string)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType23createPropertyIfMissingI10QByteArrayEEvRKT_(
    VDMListDelegateDataType *self,
    const QByteArray *string) {
  self->createPropertyIfMissing<QByteArray>(*string);
}

//  void VDMListDelegateDataType::createPropertyIfMissing<const char *>(const
//      const char * &string)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType23createPropertyIfMissingIPKcEEvRKT_(
    VDMListDelegateDataType *self,
    const char *string) {
  self->createPropertyIfMissing<const char *>(string);
}

//  static void VDMListDelegateDataType::setValue<QString>(QVariant *row,
//      const QString &role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType8setValueI7QStringEEvP8QVariantRKT_RKS2_(
    QVariant *row,
    const QString *role,
    const QVariant *value) {
  VDMListDelegateDataType::setValue<QString>(row, *role, *value);
}

//  static void VDMListDelegateDataType::setValue<QByteArray>(QVariant *row,
//      const QByteArray &role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType8setValueI10QByteArrayEEvP8QVariantRKT_RKS2_(
    QVariant *row,
    const QByteArray *role,
    const QVariant *value) {
  VDMListDelegateDataType::setValue<QByteArray>(row, *role, *value);
}

//  static void VDMListDelegateDataType::setValue<const char *>(QVariant
//      *row, const const char * &role, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23VDMListDelegateDataType8setValueIPKcEEvP8QVariantRKT_RKS3_(
    QVariant *row,
    const char *role,
    const QVariant *value) {
  VDMListDelegateDataType::setValue<const char *>(row, role, *value);
}

#endif  // QT_CONFIG(qml_delegate_model)
