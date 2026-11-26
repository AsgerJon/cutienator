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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 56, as local:qqmllistmodel.cpp:roleTypeName
static QString roleTypeName(ListLayout::Role::DataType t)
{
    static const QString roleTypeNames[] = {
        QStringLiteral("String"), QStringLiteral("Number"), QStringLiteral("Bool"),
        QStringLiteral("List"), QStringLiteral("QObject"), QStringLiteral("VariantMap"),
        QStringLiteral("DateTime"), QStringLiteral("Url"), QStringLiteral("Function")
    };

    if (t > ListLayout::Role::Invalid && t < ListLayout::Role::MaxDataType)
        return roleTypeNames[t];

    return QString();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1722, as local:qqmllistmodel.cpp:ModelObjectOwnPropertyKeyIterator
namespace QV4 {
struct ModelObjectOwnPropertyKeyIterator : ObjectOwnPropertyKeyIterator
{
    int roleNameIndex = 0;
    ~ModelObjectOwnPropertyKeyIterator() override = default;
    PropertyKey next(const Object *o, Property *pd = nullptr, PropertyAttributes *attrs = nullptr) override;

};
}  // namespace QV4

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1730, as local:qqmllistmodel.cpp:ModelObjectOwnPropertyKeyIterator::next
namespace QV4 {
inline PropertyKey ModelObjectOwnPropertyKeyIterator::next(const Object *o, Property *pd, PropertyAttributes *attrs)
{
    const ModelObject *that = static_cast<const ModelObject *>(o);

    ExecutionEngine *v4 = that->engine();

    QQmlListModel *model = that->d()->m_model;
    ListModel *listModel = model ? model->listModel() : nullptr;
    if (listModel && roleNameIndex < listModel->roleCount()) {
        Scope scope(that->engine());
        const ListLayout::Role &role = listModel->getExistingRole(roleNameIndex);
        ++roleNameIndex;
        ScopedString roleName(scope, v4->newString(role.name));
        if (attrs)
            *attrs = QV4::Attr_Data;
        if (pd) {

            QVariant value = model->data(that->d()->elementIndex(), role.index);
            if (auto recursiveListModel = qvariant_cast<QQmlListModel*>(value)) {
                auto size = recursiveListModel->count();
                auto array = ScopedArrayObject{scope, v4->newArrayObject(size)};
                QV4::ScopedValue val(scope);
                for (auto i = 0; i < size; i++) {
                    val = QJSValuePrivate::convertToReturnedValue(
                            v4, recursiveListModel->get(i));
                    array->arrayPut(i, val);
                }
                pd->value = array;
            } else {
                pd->value = v4->fromVariant(value);
            }
        }
        return roleName->toPropertyKey();
    }

    // Fall back to QV4::Object as opposed to QV4::QObjectWrapper otherwise it will add
    // unnecessary entries that relate to the roles used. These just create extra work
    // later on as they will just be ignored.
    return ObjectOwnPropertyKeyIterator::next(o, pd, attrs);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1587, as _ZN19ModelNodeMetaObject3getEP7QObject
inline ModelNodeMetaObject *ModelNodeMetaObject::get(QObject *obj)
{
    QObjectPrivate *op = QObjectPrivate::get(obj);
    return static_cast<ModelNodeMetaObject*>(op->metaObject);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 792, as _ZN9ListModel19setExistingPropertyEiRK7QStringRKN3QV45ValueEPNS3_15ExecutionEngineE
inline int ListModel::setExistingProperty(int elementIndex, const QString &key, const QV4::Value &data, QV4::ExecutionEngine *eng)
{
    int roleIndex = -1;

    if (elementIndex >= 0 && elementIndex < elements.count()) {
        ListElement *e = elements[elementIndex];
        const ListLayout::Role *r = m_layout->getExistingRole(key);
        if (r)
            roleIndex = e->setJsProperty(*r, data, eng);
    }

    return roleIndex;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1484, as _ZN11ListElement13setJsPropertyERKN10ListLayout4RoleERKN3QV45ValueEPNS4_15ExecutionEngineE
inline int ListElement::setJsProperty(const ListLayout::Role &role, const QV4::Value &d, QV4::ExecutionEngine *eng)
{
    // Check if this key exists yet
    int roleIndex = -1;

    QV4::Scope scope(eng);

    // Add the value now
    if (d.isString()) {
        QString qstr = d.toQString();
        roleIndex = setStringProperty(role, qstr);
    } else if (d.isNumber()) {
        roleIndex = setDoubleProperty(role, d.asDouble());
    } else if (d.as<QV4::ArrayObject>()) {
        QV4::ScopedArrayObject a(scope, d);
        if (role.type == ListLayout::Role::List) {
            QV4::Scope scope(a->engine());
            QV4::ScopedObject o(scope);

            ListModel *subModel = new ListModel(role.subLayout, nullptr);
            int arrayLength = a->getLength();
            for (int j=0 ; j < arrayLength ; ++j) {
                o = a->get(j);
                subModel->append(o);
            }
            roleIndex = setListProperty(role, subModel);
        } else {
            qmlWarning(nullptr) << QStringLiteral("Can't assign to existing role '%1' of different type [%2 -> %3]").arg(role.name).arg(roleTypeName(role.type)).arg(roleTypeName(ListLayout::Role::List));
        }
    } else if (d.isBoolean()) {
        roleIndex = setBoolProperty(role, d.booleanValue());
    } else if (d.as<QV4::DateObject>()) {
        QV4::Scoped<QV4::DateObject> dd(scope, d);
        QDateTime dt = dd->toQDateTime();
        roleIndex = setDateTimeProperty(role, dt);
    } else if (d.as<QV4::UrlObject>()) {
        QV4::Scoped<QV4::UrlObject> url(scope, d);
        QUrl qurl = QUrl(url->href());
        roleIndex = setUrlProperty(role, qurl);
    } else if (d.as<QV4::FunctionObject>()) {
        QV4::ScopedFunctionObject f(scope, d);
        QJSValue jsv;
        QJSValuePrivate::setValue(&jsv, f);
        roleIndex = setFunctionProperty(role, jsv);
    } else if (d.isObject()) {
        QV4::ScopedObject o(scope, d);
        QV4::QObjectWrapper *wrapper = o->as<QV4::QObjectWrapper>();
        if (role.type == ListLayout::Role::QObject && wrapper) {
            roleIndex = setQObjectProperty(role, wrapper);
        } else if (role.type == ListLayout::Role::VariantMap) {
            roleIndex = setVariantMapProperty(role, o);
        } else if (role.type == ListLayout::Role::Url) {
            QVariant maybeUrl = QV4::ExecutionEngine::toVariant(
                        // gc will hold on to o via the scoped propertyValue; fromReturnedValue is safe
                        QV4::Value::fromReturnedValue(o.asReturnedValue()),
                        QMetaType::fromType<QUrl>(), true);
            if (maybeUrl.metaType() == QMetaType::fromType<QUrl>()) {
                roleIndex = setUrlProperty(role, maybeUrl.toUrl());
            }
        }
    } else if (d.isNullOrUndefined()) {
        clearProperty(role);
    }

    return roleIndex;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1716, as _ZN3QV411ModelObject26virtualResolveLookupGetterEPKNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE
namespace QV4 {
inline ReturnedValue ModelObject::virtualResolveLookupGetter(const Object *object, ExecutionEngine *engine, Lookup *lookup)
{
    lookup->call = Lookup::Call::GetterQObjectPropertyFallback;
    return lookup->getter(engine, *object);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1771, as _ZN3QV411ModelObject22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE
namespace QV4 {
inline OwnPropertyKeyIterator *ModelObject::virtualOwnPropertyKeys(const Object *m, Value *target)
{
    *target = *m;
    return new ModelObjectOwnPropertyKeyIterator;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ModelObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ModelObject10__dataTestEv(QV4::ModelObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ModelObject *QV4::ModelObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ModelObject *ritual_ZNK3QV411ModelObject11d_uncheckedEv(
    const QV4::ModelObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ModelObject *QV4::ModelObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ModelObject *ritual_ZNK3QV411ModelObject1dEv(
    const QV4::ModelObject *self) {
  return self->d();
}

//  void QV4::ModelObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ModelObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ModelObject::virtualDestroy(b);
}

//  ReturnedValue QV4::ModelObject::virtualResolveLookupGetter(const Object
//      *object, ExecutionEngine *engine, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411ModelObject26virtualResolveLookupGetterEPKNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return QV4::ModelObject::virtualResolveLookupGetter(
      object,
      engine,
      lookup);
}

//  OwnPropertyKeyIterator *QV4::ModelObject::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV411ModelObject22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::ModelObject::virtualOwnPropertyKeys(m, target);
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
