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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 308, as _ZN19StringOrTranslation5clearEv
inline void StringOrTranslation::clear()
{
    if (arrayData && !arrayData->deref())
        QTypedArrayData<ushort>::deallocate(arrayData);
    arrayData = nullptr;
    stringData = nullptr;
    stringSize = 0;
    binding = nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 742, as _ZN9ListModel6removeEii
inline QList<std::function<void()>> ListModel::remove(int index, int count)
{
    QList<std::function<void()>> toDestroy;
    auto layout = m_layout;
    for (int i=0 ; i < count ; ++i) {
        auto element = elements[index+i];
        toDestroy.append([element, layout](){
            element->destroy(layout);
            delete element;
        });
    }
    elements.remove(index, count);
    updateCacheIndices(index);
    return toDestroy;
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

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
