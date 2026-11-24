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
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmladaptormodelenginedata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmladaptormodelenginedata.cpp, line 10, as _ZN26QQmlAdaptorModelEngineDataC1EPN3QV415ExecutionEngineE
inline QQmlAdaptorModelEngineData::QQmlAdaptorModelEngineData(QV4::ExecutionEngine *v4)
    : v4(v4)
{
    QV4::Scope scope(v4);
    QV4::ScopedObject proto(scope, v4->newObject());
    proto->defineAccessorProperty(QStringLiteral("index"), get_index, nullptr);
    proto->defineAccessorProperty(
                QStringLiteral("modelData"),
                QQmlDMListAccessorData::get_modelData, QQmlDMListAccessorData::set_modelData);
    proto->defineAccessorProperty(
                QString(),
                QQmlDMListAccessorData::get_modelData, QQmlDMListAccessorData::set_modelData);
    listItemProto.set(v4, proto);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 214, as _ZNK27QQmlDMAbstractItemModelData16hasModelChildrenEv
inline bool QQmlDMAbstractItemModelData::hasModelChildren() const
{
    if (hasValidModelIndex()) {
        if (const QAbstractItemModel *const model = m_type->model->aim()) {
            return model->hasChildren(
                    model->index(modelRow(), modelColumn(), m_type->model->rootIndex));
        }
    }
    return false;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 238, as _ZN27QQmlDMAbstractItemModelData3getEv
inline QV4::ReturnedValue QQmlDMAbstractItemModelData::get()
{
    QV4::Scope scope(metaType()->v4Engine);
    if (m_type->prototype.isUndefined()) {
        QQmlAdaptorModelEngineData *const data = QQmlAdaptorModelEngineData::get(scope.engine);
        m_type->initializeConstructor(data);
    }
    QV4::ScopedObject proto(scope, m_type->prototype.value());
    QV4::ScopedObject o(scope, proto->engine()->memoryManager->allocate<QQmlDelegateModelItemObject>(this));
    o->setPrototypeOf(proto);
    return o.asReturnedValue();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 57, as _ZN27QQmlDMAbstractItemModelData8setValueERK7QStringRK8QVariant
inline void QQmlDMAbstractItemModelData::setValue(const QString &role, const QVariant &value)
{
    // Used only for initialization of the cached data. Does not have to emit change signals.

    if (m_type->propertyRoles.size() == 1
            && (role.isEmpty() || role == QLatin1String("modelData"))) {
        // If the model has only a single role, the modelData is that role.
        m_cachedData[0] = value;
        return;
    }

    const auto it = m_type->roleNames.constFind(role.toUtf8());
    if (it != m_type->roleNames.cend()) {
        for (int i = 0; i < m_type->propertyRoles.size(); ++i) {
            if (m_type->propertyRoles.at(i) == *it) {
                m_cachedData[i] = value;
                return;
            }
        }
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 225, as _ZNK27QQmlDMAbstractItemModelData5valueEi
inline QVariant QQmlDMAbstractItemModelData::value(int role) const
{
    if (const QAbstractItemModel *aim = m_type->model->aim())
        return aim->index(modelRow(), modelColumn(), m_type->model->rootIndex).data(role);
    return QVariant();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldmabstractitemmodeldata.cpp, line 232, as _ZN27QQmlDMAbstractItemModelData8setValueEiRK8QVariant
inline void QQmlDMAbstractItemModelData::setValue(int role, const QVariant &value)
{
    if (QAbstractItemModel *aim = m_type->model->aim())
        aim->setData(aim->index(modelRow(), modelColumn(), m_type->model->rootIndex), value, role);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlDMAbstractItemModelData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQmlDMAbstractItemModelData10metaObjectEv(
    const QQmlDMAbstractItemModelData *self) {
  return self->metaObject();
}

//  bool QQmlDMAbstractItemModelData::hasModelChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlDMAbstractItemModelData16hasModelChildrenEv(
    const QQmlDMAbstractItemModelData *self) {
  return self->hasModelChildren();
}

//  QV4::ReturnedValue QQmlDMAbstractItemModelData::get()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN27QQmlDMAbstractItemModelData3getEv(
    QQmlDMAbstractItemModelData *self) {
  return self->get();
}

//  void QQmlDMAbstractItemModelData::setValue(const QString &role, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlDMAbstractItemModelData8setValueERK7QStringRK8QVariant(
    QQmlDMAbstractItemModelData *self,
    const QString *role,
    const QVariant *value) {
  self->setValue(*role, *value);
}

//  const VDMAbstractItemModelDataType *QQmlDMAbstractItemModelData::type()
//      const
extern "C" Q_DECL_EXPORT
const VDMAbstractItemModelDataType *ritual_ZNK27QQmlDMAbstractItemModelData4typeEv(
    const QQmlDMAbstractItemModelData *self) {
  return self->type();
}

//  QVariant QQmlDMAbstractItemModelData::value(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QQmlDMAbstractItemModelData5valueEi(
    const QQmlDMAbstractItemModelData *self,
    int role) {
  return new QVariant(self->value(role));
}

//  void QQmlDMAbstractItemModelData::setValue(int role, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlDMAbstractItemModelData8setValueEiRK8QVariant(
    QQmlDMAbstractItemModelData *self,
    int role,
    const QVariant *value) {
  self->setValue(role, *value);
}

//  void QQmlDMAbstractItemModelData::setValue(const QString &role, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQmlDMAbstractItemModelData8setValueERK7QStringRK8QVariant(
    QQmlDMAbstractItemModelData *self,
    const QString *role,
    const QVariant *value) {
  self->QQmlDMAbstractItemModelData::setValue(*role, *value);
}

#endif  // QT_CONFIG(qml_delegate_model)
