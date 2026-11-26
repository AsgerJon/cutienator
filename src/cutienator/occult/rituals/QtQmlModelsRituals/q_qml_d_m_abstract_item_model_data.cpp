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
#include <QtQmlModels/private/qqmldmabstractitemmodeldata_p.h>
#include <QtQmlModels/private/qqmladaptormodelenginedata_p.h>
#include <QtQmlModels/private/qqmldmlistaccessordata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  void *QQmlDMAbstractItemModelData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQmlDMAbstractItemModelData11qt_metacastEPKc(
    QQmlDMAbstractItemModelData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDMAbstractItemModelData::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQmlDMAbstractItemModelData11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDMAbstractItemModelData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  bool QQmlDMAbstractItemModelData::resolveIndex(const QQmlAdaptorModel
//      &model, int idx)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQmlDMAbstractItemModelData12resolveIndexERK16QQmlAdaptorModeli(
    QQmlDMAbstractItemModelData *self,
    const QQmlAdaptorModel *model,
    int idx) {
  return self->resolveIndex(*model, idx);
}

//  const VDMAbstractItemModelDataType *QQmlDMAbstractItemModelData::type()
//      const
extern "C" Q_DECL_EXPORT
const VDMAbstractItemModelDataType *ritual_ZNK27QQmlDMAbstractItemModelData4typeEv(
    const QQmlDMAbstractItemModelData *self) {
  return self->type();
}

//  void QQmlDMAbstractItemModelData::modelDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlDMAbstractItemModelData16modelDataChangedEv(
    QQmlDMAbstractItemModelData *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlDMAbstractItemModelData")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "modelDataChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "modelDataChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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

#endif  // QT_CONFIG(qml_delegate_model)
