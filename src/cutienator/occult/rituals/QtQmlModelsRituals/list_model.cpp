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
#include <QtCore/QList>
#include <functional>
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 45, as local:qqmllistmodel.cpp:isMemoryUsed
template <typename T>
static bool isMemoryUsed(const char *mem)
{
    for (size_t i=0 ; i < sizeof(T) ; ++i) {
        if (mem[i] != 0)
            return true;
    }

    return false;
}

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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 823, as _ZN11ListElement11objectCacheEv
inline ModelNodeMetaObject *ListElement::objectCache()
{
    if (!m_objectCache)
        return nullptr;
    return ModelNodeMetaObject::get(m_objectCache);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1369, as _ZN11ListElement7destroyEP10ListLayout
inline void ListElement::destroy(ListLayout *layout)
{
    if (layout) {
        for (int i=0 ; i < layout->roleCount() ; ++i) {
            const ListLayout::Role &r = layout->getExistingRole(i);

            switch (r.type) {
                case ListLayout::Role::String:
                    {
                        StringOrTranslation *string = getStringProperty(r);
                        if (string)
                            string->~StringOrTranslation();
                    }
                    break;
                case ListLayout::Role::List:
                    {
                        ListModel *model = getListProperty(r);
                        if (model) {
                            model->destroy();
                            delete model;
                        }
                    }
                    break;
                case ListLayout::Role::QObject:
                    {
                        if (QV4::PersistentValue *guard = getGuardProperty(r))
                            guard->~PersistentValue();
                    }
                    break;
                case ListLayout::Role::VariantMap:
                    {
                        QVariantMap *map = getVariantMapProperty(r);
                        if (map)
                            map->~QMap();
                    }
                    break;
                case ListLayout::Role::DateTime:
                    {
                        QDateTime *dt = getDateTimeProperty(r);
                        if (dt)
                            dt->~QDateTime();
                    }
                    break;
                case ListLayout::Role::Url:
                    {
                        QUrl *url = getUrlProperty(r);
                        if (url)
                            url->~QUrl();
                        break;
                    }
                case ListLayout::Role::Function:
                    {
                        QJSValue *f = getFunctionProperty(r);
                        if (f)
                            f->~QJSValue();
                    }
                    break;
                default:
                    // other types don't need explicit cleanup.
                    break;
            }
        }

        if (m_objectCache) {
            m_objectCache->~QObject();
            operator delete(m_objectCache);
        }
    }

    if (next)
        next->destroy(nullptr);
    uid = -1;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1308, as _ZN11ListElementD1Ev
inline ListElement::~ListElement()
{
    delete next;
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 910, as _ZN11ListElement15getListPropertyERKN10ListLayout4RoleE
inline ListModel *ListElement::getListProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);
    ListModel **value = reinterpret_cast<ListModel **>(mem);
    return *value;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1593, as _ZN19ModelNodeMetaObject12updateValuesEv
inline void ModelNodeMetaObject::updateValues()
{
    Q_ALLOCA_INIT();
    const int roleCount = m_model->m_listModel->roleCount();
    if (!m_initialized) {
        if (roleCount) {
            Q_ALLOCA_VAR(int, changedRoles, roleCount * sizeof(int));
            for (int i = 0; i < roleCount; ++i)
                changedRoles[i] = i;
            emitDirectNotifies(changedRoles, roleCount);
        }
        return;
    }
    for (int i=0 ; i < roleCount ; ++i) {
        const ListLayout::Role &role = m_model->m_listModel->getExistingRole(i);
        QByteArray name = role.name.toUtf8();
        const QVariant &data = m_model->data(m_elementIndex, i);
        setValue(name, data, role.type == ListLayout::Role::List);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 174, as _ZN10ListLayout4syncEPS_S0_
inline void ListLayout::sync(ListLayout *src, ListLayout *target)
{
    int roleOffset = target->roles.size();
    int newRoleCount = src->roles.size() - roleOffset;

    for (int i=0 ; i < newRoleCount ; ++i) {
        Role *role = new Role(src->roles[roleOffset + i]);
        target->roles.append(role);
        target->roleHash.insert(role->name, role);
    }

    target->currentBlockOffset = src->currentBlockOffset;
    target->currentBlock = src->currentBlock;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1313, as _ZN11ListElement4syncEPS_P10ListLayoutS0_S2_
inline QList<int> ListElement::sync(ListElement *src, ListLayout *srcLayout, ListElement *target, ListLayout *targetLayout)
{
    QList<int> changedRoles;
    for (int i=0 ; i < srcLayout->roleCount() ; ++i) {
        const ListLayout::Role &srcRole = srcLayout->getExistingRole(i);
        const ListLayout::Role &targetRole = targetLayout->getExistingRole(i);

        int roleIndex = -1;
        switch (srcRole.type) {
            case ListLayout::Role::List:
                {
                    ListModel *srcSubModel = src->getListProperty(srcRole);
                    ListModel *targetSubModel = target->getListProperty(targetRole);

                    if (srcSubModel) {
                        if (targetSubModel == nullptr) {
                            targetSubModel = new ListModel(targetRole.subLayout, nullptr);
                            target->setListPropertyFast(targetRole, targetSubModel);
                        }
                        if (ListModel::sync(srcSubModel, targetSubModel))
                            roleIndex = targetRole.index;
                    }
                }
                break;
            case ListLayout::Role::QObject:
                {
                    QV4::QObjectWrapper *object = src->getQObjectProperty(srcRole);
                    roleIndex = target->setQObjectProperty(targetRole, object);
                }
                break;
            case ListLayout::Role::String:
            case ListLayout::Role::Number:
            case ListLayout::Role::Bool:
            case ListLayout::Role::DateTime:
            case ListLayout::Role::Function:
                {
                    QVariant v = src->getProperty(srcRole, nullptr, nullptr);
                    roleIndex = target->setVariantProperty(targetRole, v);
                }
                break;
            case ListLayout::Role::VariantMap:
                {
                    QVariantMap *map = src->getVariantMapProperty(srcRole);
                    roleIndex = target->setVariantMapProperty(targetRole, map);
                }
                break;
            default:
                break;
        }
        if (roleIndex >= 0)
            changedRoles << roleIndex;
    }

    return changedRoles;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1300, as _ZN11ListElementC1Ei
inline ListElement::ListElement(int existingUid)
{
    m_objectCache = nullptr;
    uid = existingUid;
    next = nullptr;
    memset(data, 0, sizeof(data));
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1551, as _ZN19ModelNodeMetaObjectC1EP7QObjectP13QQmlListModeli
inline ModelNodeMetaObject::ModelNodeMetaObject(QObject *object, QQmlListModel *model, int elementIndex)
: QQmlOpenMetaObject(object), m_enabled(false), m_model(model), m_elementIndex(elementIndex), m_initialized(false)
{}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 866, as _ZN11ListElement14getUrlPropertyERKN10ListLayout4RoleE
inline QUrl *ListElement::getUrlProperty(const ListLayout::Role &role)
{
    QUrl *url = nullptr;

    char *mem = getPropertyMemory(role);
    if (isMemoryUsed<QUrl>(mem))
        url = reinterpret_cast<QUrl *>(mem);

    return url;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 888, as _ZN11ListElement16getGuardPropertyERKN10ListLayout4RoleE
inline QV4::PersistentValue *
ListElement::getGuardProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);

    bool existingGuard = false;
    for (size_t i = 0; i < sizeof(QV4::PersistentValue);
         ++i) {
        if (mem[i] != 0) {
            existingGuard = true;
            break;
        }
    }

    QV4::PersistentValue *g = nullptr;

    if (existingGuard)
        g = reinterpret_cast<QV4::PersistentValue *>(mem);

    return g;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 806, as _ZN11ListElement17getPropertyMemoryERKN10ListLayout4RoleE
inline char *ListElement::getPropertyMemory(const ListLayout::Role &role)
{
    ListElement *e = this;
    int blockIndex = 0;
    while (blockIndex < role.blockIndex) {
        if (e->next == nullptr) {
            e->next = new ListElement;
            e->next->uid = uid;
        }
        e = e->next;
        ++blockIndex;
    }

    char *mem = &e->data[role.blockOffset];
    return mem;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 830, as _ZN11ListElement17getStringPropertyERKN10ListLayout4RoleE
inline StringOrTranslation *ListElement::getStringProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);
    StringOrTranslation *s = reinterpret_cast<StringOrTranslation *>(mem);
    return s;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 855, as _ZN11ListElement19getDateTimePropertyERKN10ListLayout4RoleE
inline QDateTime *ListElement::getDateTimeProperty(const ListLayout::Role &role)
{
    QDateTime *dt = nullptr;

    char *mem = getPropertyMemory(role);
    if (isMemoryUsed<QDateTime>(mem))
        dt = reinterpret_cast<QDateTime *>(mem);

    return dt;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 877, as _ZN11ListElement19getFunctionPropertyERKN10ListLayout4RoleE
inline QJSValue *ListElement::getFunctionProperty(const ListLayout::Role &role)
{
    QJSValue *f = nullptr;

    char *mem = getPropertyMemory(role);
    if (isMemoryUsed<QJSValue>(mem))
        f = reinterpret_cast<QJSValue *>(mem);

    return f;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 844, as _ZN11ListElement21getVariantMapPropertyERKN10ListLayout4RoleE
inline QVariantMap *ListElement::getVariantMapProperty(const ListLayout::Role &role)
{
    QVariantMap *map = nullptr;

    char *mem = getPropertyMemory(role);
    if (isMemoryUsed<QVariantMap>(mem))
        map = reinterpret_cast<QVariantMap *>(mem);

    return map;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1587, as _ZN19ModelNodeMetaObject3getEP7QObject
inline ModelNodeMetaObject *ModelNodeMetaObject::get(QObject *obj)
{
    QObjectPrivate *op = QObjectPrivate::get(obj);
    return static_cast<ModelNodeMetaObject*>(op->metaObject);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 264, as _ZN19StringOrTranslationD1Ev
inline StringOrTranslation::~StringOrTranslation()
{
    clear();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1647, as _ZN19ModelNodeMetaObject18emitDirectNotifiesEPKii
inline void ModelNodeMetaObject::emitDirectNotifies(const int *changedRoles, int roleCount)
{
    Q_ASSERT(!m_initialized);
    QQmlData *ddata = QQmlData::get(object(), /*create*/false);
    if (!ddata)
        return;
    // There's nothing to emit if we're a list model in a worker thread.
    if (!qmlEngine(m_model))
        return;
    for (int i = 0; i < roleCount; ++i) {
        const int changedRole = changedRoles[i];
        QQmlNotifier::notify(ddata, changedRole);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 189, as _ZN10ListLayout4RoleC1EPKS0_
inline ListLayout::Role::Role(const Role *other)
{
    name = other->name;
    type = other->type;
    blockIndex = other->blockIndex;
    blockOffset = other->blockOffset;
    index = other->index;
    if (other->subLayout)
        subLayout = new ListLayout(other->subLayout);
    else
        subLayout = nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1570, as _ZN19ModelNodeMetaObjectD1Ev
inline ModelNodeMetaObject::~ModelNodeMetaObject()
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1630, as _ZN19ModelNodeMetaObject15propertyWrittenEi
inline void ModelNodeMetaObject::propertyWritten(int index)
{
    if (!m_enabled)
        return;

    QString propName = QString::fromUtf8(name(index));
    const QVariant value = this->value(index);

    QV4::Scope scope(m_model->engine());
    QV4::ScopedValue v(scope, scope.engine->fromVariant(value));

    int roleIndex = m_model->m_listModel->setExistingProperty(m_elementIndex, propName, v, scope.engine);
    if (roleIndex != -1)
        m_model->emitItemsChanged(m_elementIndex, 1, QList<int>(1, roleIndex));
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 475, as _ZN9ListModelC1EP10ListLayoutP13QQmlListModel
inline ListModel::ListModel(ListLayout *layout, QQmlListModel *modelCache) : m_layout(layout), m_modelCache(modelCache)
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 560, as _ZN9ListModel18updateTranslationsEv
inline void ListModel::updateTranslations()
{
    for (int index = 0; index != elements.count(); ++index) {
        ListElement *e = elements[index];
        if (ModelNodeMetaObject *cache = e->objectCache()) {
            // TODO: more fine grained tracking?
            cache->updateValues();
        }
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 503, as _ZN9ListModel4moveEiii
inline void ListModel::move(int from, int to, int n)
{
    if (from > to) {
        // Only move forwards - flip if backwards moving
        int tfrom = from;
        int tto = to;
        from = tto;
        to = tto+n;
        n = tfrom-tto;
    }

    QPODVector<ListElement *, 4> store;
    for (int i=0 ; i < (to-from) ; ++i)
        store.append(elements[from+n+i]);
    for (int i=0 ; i < n ; ++i)
        store.append(elements[from+i]);
    for (int i=0 ; i < store.count() ; ++i)
        elements[from+i] = store[i];

    updateCacheIndices(from, to + n);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 531, as _ZN9ListModel18updateCacheIndicesEii
inline void ListModel::updateCacheIndices(int start, int end)
{
    int count = elements.count();

    if (end < 0 || end > count)
        end = count;

    for (int i = start; i < end; ++i) {
        ListElement *e = elements.at(i);
        if (ModelNodeMetaObject *mo = e->objectCache())
            mo->m_elementIndex = i;
    }
}
//  -----------------------------------------------------------------------

//  ListModel::ListModel(ListLayout *layout, QQmlListModel *modelCache)
extern "C" Q_DECL_EXPORT
ListModel *ritual_ZN9ListModelC1EP10ListLayoutP13QQmlListModel(
    ListLayout *layout,
    QQmlListModel *modelCache) {
  return new ListModel(layout, modelCache);
}

//  void ListModel::updateTranslations()
extern "C" Q_DECL_EXPORT
void ritual_ZN9ListModel18updateTranslationsEv(ListModel *self) {
  self->updateTranslations();
}

//  int ListModel::roleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9ListModel9roleCountEv(const ListModel *self) {
  return self->roleCount();
}

//  const ListLayout::Role &ListModel::getExistingRole(int index) const
extern "C" Q_DECL_EXPORT
ListLayout::Role *ritual_ZNK9ListModel15getExistingRoleEi(
    const ListModel *self,
    int index) {
  return new ListLayout::Role(self->getExistingRole(index));
}

//  int ListModel::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9ListModel12elementCountEv(const ListModel *self) {
  return self->elementCount();
}

//  void ListModel::move(int from, int to, int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN9ListModel4moveEiii(ListModel *self, int from, int to, int n) {
  self->move(from, to, n);
}

//  void ListModel::updateCacheIndices(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9ListModel18updateCacheIndicesEii(
    ListModel *self,
    int start,
    int end) {
  self->updateCacheIndices(start, end);
}

//  a QList<std::function<void ()>> a ritual of ListModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ListModel__QList_std_function_void(
    QList<std::function<void ()>> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
