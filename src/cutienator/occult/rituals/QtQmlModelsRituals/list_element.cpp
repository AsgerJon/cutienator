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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 917, as _ZN11ListElement11getPropertyERKN10ListLayout4RoleEPK13QQmlListModelPN3QV415ExecutionEngineE
inline QVariant ListElement::getProperty(const ListLayout::Role &role, const QQmlListModel *owner, QV4::ExecutionEngine *eng)
{
    char *mem = getPropertyMemory(role);

    QVariant data;

    switch (role.type) {
        case ListLayout::Role::Number:
            {
                double *value = reinterpret_cast<double *>(mem);
                data = *value;
            }
            break;
        case ListLayout::Role::String:
            {
                StringOrTranslation *value = reinterpret_cast<StringOrTranslation *>(mem);
                if (value->isSet())
                    data = value->toString(owner);
                else
                    data = QString();
            }
            break;
        case ListLayout::Role::Bool:
            {
                bool *value = reinterpret_cast<bool *>(mem);
                data = *value;
            }
            break;
        case ListLayout::Role::List:
            {
                ListModel **value = reinterpret_cast<ListModel **>(mem);
                ListModel *model = *value;

                if (model) {
                    if (model->m_modelCache == nullptr) {
                        model->m_modelCache = new QQmlListModel(owner, model, eng);
                        QQmlEngine::setContextForObject(model->m_modelCache, QQmlEngine::contextForObject(owner));
                    }

                    QObject *object = model->m_modelCache;
                    data = QVariant::fromValue(object);
                }
            }
            break;
        case ListLayout::Role::QObject:
            {
                QV4::PersistentValue *guard = reinterpret_cast<QV4::PersistentValue *>(mem);
                data = QVariant::fromValue(guard->as<QV4::QObjectWrapper>()->object());
            }
            break;
        case ListLayout::Role::VariantMap:
            {
                if (isMemoryUsed<QVariantMap>(mem)) {
                    QVariantMap *map = reinterpret_cast<QVariantMap *>(mem);
                    data = *map;
                }
            }
            break;
        case ListLayout::Role::DateTime:
            {
                if (isMemoryUsed<QDateTime>(mem)) {
                    QDateTime *dt = reinterpret_cast<QDateTime *>(mem);
                    data = *dt;
                }
            }
            break;
        case ListLayout::Role::Url:
            {
                if (isMemoryUsed<QUrl>(mem)) {
                    QUrl *url = reinterpret_cast<QUrl *>(mem);
                    data = *url;
                }
            }
            break;
        case ListLayout::Role::Function:
            {
                if (isMemoryUsed<QJSValue>(mem)) {
                    QJSValue *func = reinterpret_cast<QJSValue *>(mem);
                    data = QVariant::fromValue(*func);
                }
            }
            break;
        default:
            break;
    }

    return data;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1150, as _ZN11ListElement14setUrlPropertyERKN10ListLayout4RoleERK4QUrl
inline int ListElement::setUrlProperty(const ListLayout::Role &role, const QUrl &url)
{
    int roleIndex = -1;

    if (role.type == ListLayout::Role::Url) {
        char *mem = getPropertyMemory(role);
        if (isMemoryUsed<QUrl>(mem)) {
            QUrl *qurl = reinterpret_cast<QUrl *>(mem);
            qurl->~QUrl();
        }
        new (mem) QUrl(url);
        roleIndex = role.index;
    }

    return roleIndex;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1133, as _ZN11ListElement19setDateTimePropertyERKN10ListLayout4RoleERK9QDateTime
inline int ListElement::setDateTimeProperty(const ListLayout::Role &role, const QDateTime &dt)
{
    int roleIndex = -1;

    if (role.type == ListLayout::Role::DateTime) {
        char *mem = getPropertyMemory(role);
        if (isMemoryUsed<QDateTime>(mem)) {
            QDateTime *dt = reinterpret_cast<QDateTime *>(mem);
            dt->~QDateTime();
        }
        new (mem) QDateTime(dt);
        roleIndex = role.index;
    }

    return roleIndex;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1167, as _ZN11ListElement19setFunctionPropertyERKN10ListLayout4RoleERK8QJSValue
inline int ListElement::setFunctionProperty(const ListLayout::Role &role, const QJSValue &f)
{
    int roleIndex = -1;

    if (role.type == ListLayout::Role::Function) {
        char *mem = getPropertyMemory(role);
        if (isMemoryUsed<QJSValue>(mem)) {
            QJSValue *f = reinterpret_cast<QJSValue *>(mem);
            f->~QJSValue();
        }
        new (mem) QJSValue(f);
        roleIndex = role.index;
    }

    return roleIndex;
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 866, as _ZN11ListElement14getUrlPropertyERKN10ListLayout4RoleE
inline QUrl *ListElement::getUrlProperty(const ListLayout::Role &role)
{
    QUrl *url = nullptr;

    char *mem = getPropertyMemory(role);
    if (isMemoryUsed<QUrl>(mem))
        url = reinterpret_cast<QUrl *>(mem);

    return url;
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 264, as _ZN19StringOrTranslationD1Ev
inline StringOrTranslation::~StringOrTranslation()
{
    clear();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 479, as _ZN9ListModel7destroyEv
inline void ListModel::destroy()
{
    for (const auto &destroyer : remove(0, elements.count()))
        destroyer();

    m_layout = nullptr;
    if (m_modelCache && m_modelCache->m_primary == false)
        delete m_modelCache;
    m_modelCache = nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 269, as _ZN19StringOrTranslation9setStringERK7QString
inline void StringOrTranslation::setString(const QString &s)
{
    clear();
    if (s.isEmpty())
        return;
    QString::DataPointer dataPointer = s.data_ptr();
    arrayData = dataPointer.d_ptr();
    stringData = dataPointer.data();
    stringSize = dataPointer.size;
    if (arrayData)
        arrayData->ref();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 300, as _ZNK19StringOrTranslation8asStringEv
inline QString StringOrTranslation::asString() const
{
    if (!arrayData)
        return QString();
    arrayData->ref();
    return QString(QStringPrivate(arrayData, stringData, stringSize));
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 282, as _ZN19StringOrTranslation14setTranslationEPKN3QV412CompiledData7BindingE
inline void StringOrTranslation::setTranslation(const QV4::CompiledData::Binding *binding)
{
    clear();
    this->binding = binding;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1587, as _ZN19ModelNodeMetaObject3getEP7QObject
inline ModelNodeMetaObject *ModelNodeMetaObject::get(QObject *obj)
{
    QObjectPrivate *op = QObjectPrivate::get(obj);
    return static_cast<ModelNodeMetaObject*>(op->metaObject);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1300, as _ZN11ListElementC1Ei
inline ListElement::ListElement(int existingUid)
{
    m_objectCache = nullptr;
    uid = existingUid;
    next = nullptr;
    memset(data, 0, sizeof(data));
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1308, as _ZN11ListElementD1Ev
inline ListElement::~ListElement()
{
    delete next;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 823, as _ZN11ListElement11objectCacheEv
inline ModelNodeMetaObject *ListElement::objectCache()
{
    if (!m_objectCache)
        return nullptr;
    return ModelNodeMetaObject::get(m_objectCache);
}
//  -----------------------------------------------------------------------

//  ListElement::ListElement(int existingUid)
extern "C" Q_DECL_EXPORT
ListElement *ritual_ZN11ListElementC1Ei(int existingUid) {
  return new ListElement(existingUid);
}

//  ListElement::~ListElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN11ListElementD1Ev(ListElement *self) {
  delete self;
}

//  int ListElement::getUid() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11ListElement6getUidEv(const ListElement *self) {
  return self->getUid();
}

//  ModelNodeMetaObject *ListElement::objectCache()
extern "C" Q_DECL_EXPORT
ModelNodeMetaObject *ritual_ZN11ListElement11objectCacheEv(
    ListElement *self) {
  return self->objectCache();
}

//  a QList<int> a ritual of ListElement gave
extern "C" Q_DECL_EXPORT
void ritual_drop_ListElement__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
