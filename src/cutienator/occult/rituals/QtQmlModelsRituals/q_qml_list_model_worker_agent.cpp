//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodelworkeragent_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistmodelworkeragent_p.h>
#include <QtQmlModels/private/qqmllistmodel_p_p.h>
#include <QtQml/private/qqmldata_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdebug.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 120, as _ZN24QQmlListModelWorkerAgent5eventEP6QEvent
inline bool QQmlListModelWorkerAgent::event(QEvent *e)
{
    if (e->type() == QEvent::User) {
        bool cc = false;
        QMutexLocker locker(&mutex);
        if (m_orig) {
            Sync *s = static_cast<Sync *>(e);

            cc = (m_orig->count() != s->list->count());

            Q_ASSERT(m_orig->m_dynamicRoles == s->list->m_dynamicRoles);
            if (m_orig->m_dynamicRoles)
                QQmlListModel::sync(s->list, m_orig);
            else
                ListModel::sync(s->list->m_listModel, m_orig->m_listModel);
        }

        syncDone.wakeAll();
        locker.unlock();

        if (cc)
            emit m_orig->countChanged();
        return true;
    }

    return QObject::event(e);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 336, as _ZN9ListModel4syncEPS_S0_
inline bool ListModel::sync(ListModel *src, ListModel *target)
{
    // Sanity check

    bool hasChanges = false;

    // Build hash of elements <-> uid for each of the lists
    QHash<int, ElementSync> elementHash;
    for (int i = 0; i < target->elements.count(); ++i) {
        ListElement *e = target->elements.at(i);
        int uid = e->getUid();
        ElementSync sync;
        sync.target = e;
        sync.targetIndex = i;
        elementHash.insert(uid, sync);
    }
    for (int i = 0; i < src->elements.count(); ++i) {
        ListElement *e = src->elements.at(i);
        int uid = e->getUid();

        QHash<int, ElementSync>::iterator it = elementHash.find(uid);
        if (it == elementHash.end()) {
            ElementSync sync;
            sync.src = e;
            sync.srcIndex = i;
            elementHash.insert(uid, sync);
        } else {
            ElementSync &sync = it.value();
            sync.src = e;
            sync.srcIndex = i;
        }
    }

    QQmlListModel *targetModel = target->m_modelCache;

    // Get list of elements that are in the target but no longer in the source. These get deleted first.
    int rowsRemoved = 0;
    for (int i = 0 ; i < target->elements.count() ; ++i) {
        ListElement *element = target->elements.at(i);
        ElementSync &s = elementHash.find(element->getUid()).value();
        Q_ASSERT(s.targetIndex >= 0);
        // need to update the targetIndex, to keep it correct after removals
        s.targetIndex -= rowsRemoved;
        if (s.src == nullptr) {
            Q_ASSERT(s.targetIndex == i);
            hasChanges = true;
            if (targetModel)
                targetModel->beginRemoveRows(QModelIndex(), i, i);
            s.target->destroy(target->m_layout);
            target->elements.removeOne(s.target);
            delete s.target;
            if (targetModel)
                targetModel->endRemoveRows();
            ++rowsRemoved;
            --i;
            continue;
        }
    }

    // Sync the layouts
    ListLayout::sync(src->m_layout, target->m_layout);

    // Clear the target list, and append in correct order from the source
    target->elements.clear();
    for (int i = 0; i < src->elements.count(); ++i) {
        ListElement *srcElement = src->elements.at(i);
        ElementSync &s = elementHash.find(srcElement->getUid()).value();
        Q_ASSERT(s.srcIndex >= 0);
        ListElement *targetElement = s.target;
        if (targetElement == nullptr) {
            targetElement = new ListElement(srcElement->getUid());
        }
        s.changedRoles = ListElement::sync(srcElement, src->m_layout, targetElement, target->m_layout);
        target->elements.append(targetElement);
    }

    target->updateCacheIndices();

    // Update values stored in target meta objects
    for (int i=0 ; i < target->elements.count() ; ++i) {
        ListElement *e = target->elements[i];
        if (ModelNodeMetaObject *mo = e->objectCache())
            mo->updateValues();
    }

    // now emit the change notifications required. This can be safely done, as we're only emitting changes, moves and inserts,
    // so the model indices can't be out of bounds
    //
    // to ensure things are kept in the correct order, emit inserts and moves first. This shouls ensure all persistent
    // model indices are updated correctly
    int rowsInserted = 0;
    const int targetElementCount = target->elements.count();
    for (int i = 0 ; i < targetElementCount ; ++i) {
        ListElement *element = target->elements.at(i);
        ElementSync &s = elementHash.find(element->getUid()).value();
        Q_ASSERT(s.srcIndex >= 0);
        s.srcIndex += rowsInserted;
        if (s.srcIndex != s.targetIndex) {
            if (targetModel) {
                if (s.targetIndex == -1) {
                    targetModel->beginInsertRows(QModelIndex(), i, i);
                    targetModel->endInsertRows();
                    ++rowsInserted;
                } else {
                    bool validMove = targetModel->beginMoveRows(QModelIndex(), s.targetIndex, s.targetIndex, QModelIndex(), i);
                    Q_ASSERT(validMove);
                    targetModel->endMoveRows();
                    // fixup target indices of elements that still need to move
                    for (int j=i+1; j < targetElementCount; ++j) {
                        ListElement *eToFix = target->elements.at(j);
                        ElementSync &sToFix = elementHash.find(eToFix->getUid()).value();
                        if (i < s.targetIndex) {
                            // element was moved down
                            if (sToFix.targetIndex > s.targetIndex || sToFix.targetIndex < i)
                                continue; // unaffected by reordering
                            else
                                sToFix.targetIndex += 1;
                        } else {
                            // element was moved up
                            if (sToFix.targetIndex < s.targetIndex || sToFix.targetIndex > i)
                                continue; // unaffected by reordering
                            else
                                sToFix.targetIndex -= 1;
                        }
                    }
                }
            }
            hasChanges = true;
        }
        if (s.targetIndex != -1 && !s.changedRoles.isEmpty()) {
            QModelIndex idx = targetModel->createIndex(i, 0);
            if (targetModel)
                targetModel->dataChanged(idx, idx, s.changedRoles);
            hasChanges = true;
        }
    }
    return hasChanges;
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 823, as _ZN11ListElement11objectCacheEv
inline ModelNodeMetaObject *ListElement::objectCache()
{
    if (!m_objectCache)
        return nullptr;
    return ModelNodeMetaObject::get(m_objectCache);
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 910, as _ZN11ListElement15getListPropertyERKN10ListLayout4RoleE
inline ListModel *ListElement::getListProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);
    ListModel **value = reinterpret_cast<ListModel **>(mem);
    return *value;
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

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 830, as _ZN11ListElement17getStringPropertyERKN10ListLayout4RoleE
inline StringOrTranslation *ListElement::getStringProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);
    StringOrTranslation *s = reinterpret_cast<StringOrTranslation *>(mem);
    return s;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 837, as _ZN11ListElement18getQObjectPropertyERKN10ListLayout4RoleE
inline QV4::QObjectWrapper *ListElement::getQObjectProperty(const ListLayout::Role &role)
{
    char *mem = getPropertyMemory(role);
    QV4::PersistentValue *g = reinterpret_cast<QV4::PersistentValue *>(mem);
    return g->as<QV4::QObjectWrapper>();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1443, as _ZN11ListElement18setVariantPropertyERKN10ListLayout4RoleERK8QVariant
inline int ListElement::setVariantProperty(const ListLayout::Role &role, const QVariant &d)
{
    int roleIndex = -1;

    switch (role.type) {
        case ListLayout::Role::Number:
            roleIndex = setDoubleProperty(role, d.toDouble());
            break;
        case ListLayout::Role::String:
            if (d.userType() == qMetaTypeId<const QV4::CompiledData::Binding *>())
                roleIndex = setTranslationProperty(role, d.value<const QV4::CompiledData::Binding*>());
            else
                roleIndex = setStringProperty(role, d.toString());
            break;
        case ListLayout::Role::Bool:
            roleIndex = setBoolProperty(role, d.toBool());
            break;
        case ListLayout::Role::List:
            roleIndex = setListProperty(role, d.value<ListModel *>());
            break;
        case ListLayout::Role::VariantMap: {
                QVariantMap map = d.toMap();
                roleIndex = setVariantMapProperty(role, &map);
            }
            break;
        case ListLayout::Role::DateTime:
            roleIndex = setDateTimeProperty(role, d.toDateTime());
            break;
        case ListLayout::Role::Url:
            roleIndex = setUrlProperty(role, d.toUrl());
            break;
        case ListLayout::Role::Function:
            roleIndex = setFunctionProperty(role, d.value<QJSValue>());
            break;
        default:
            break;
    }

    return roleIndex;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodel.cpp, line 1225, as _ZN11ListElement19setListPropertyFastERKN10ListLayout4RoleEP9ListModel
inline void ListElement::setListPropertyFast(const ListLayout::Role &role, ListModel *m)
{
    char *mem = getPropertyMemory(role);
    ListModel **value = new (mem) ListModel *;
    *value = m;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 27, as _ZN24QQmlListModelWorkerAgentD1Ev
inline QQmlListModelWorkerAgent::~QQmlListModelWorkerAgent()
{
    mutex.lock();
    syncDone.wakeAll();
    mutex.unlock();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 34, as _ZNK24QQmlListModelWorkerAgent6engineEv
inline QV4::ExecutionEngine *QQmlListModelWorkerAgent::engine() const
{
    return m_copy->m_engine;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 65, as _ZNK24QQmlListModelWorkerAgent5countEv
inline int QQmlListModelWorkerAgent::count() const
{
    return m_copy->count();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 90, as _ZNK24QQmlListModelWorkerAgent3getEi
inline QJSValue QQmlListModelWorkerAgent::get(int index) const
{
    return m_copy->get(index);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistmodelworkeragent.cpp, line 60, as _ZN24QQmlListModelWorkerAgent14modelDestroyedEv
inline void QQmlListModelWorkerAgent::modelDestroyed()
{
    m_orig = nullptr;
}
//  -----------------------------------------------------------------------

//  A QQmlListModelWorkerAgent that Python can take functions over in. Every QQmlListModelWorkerAgent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_list_model)
typedef bool (*CuteQQmlListModelWorkerAgentCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(qml_list_model)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlListModelWorkerAgentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlListModelWorkerAgentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlListModelWorkerAgentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlListModelWorkerAgentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlListModelWorkerAgentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlListModelWorkerAgentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlListModelWorkerAgent : public QQmlListModelWorkerAgent {
public:
  using QQmlListModelWorkerAgent::QQmlListModelWorkerAgent;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_list_model)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_list_model)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_list_model)
  //  bool QQmlListModelWorkerAgent::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall0 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlListModelWorkerAgent::event(a0);
  }
#endif  // QT_CONFIG(qml_list_model)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall1 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall2 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall3 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall4 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall5 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlListModelWorkerAgentCall6 call = reinterpret_cast<CuteQQmlListModelWorkerAgentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlListModelWorkerAgent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQmlListModelWorkerAgent10metaObjectEv(
    const QQmlListModelWorkerAgent *self) {
  return self->metaObject();
}

//  void *QQmlListModelWorkerAgent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQmlListModelWorkerAgent11qt_metacastEPKc(
    QQmlListModelWorkerAgent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlListModelWorkerAgent::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQmlListModelWorkerAgent11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlListModelWorkerAgent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQmlListModelWorkerAgent::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent22qt_qmlMarker_anonymousEv(
    QQmlListModelWorkerAgent *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlListModelWorkerAgent::~QQmlListModelWorkerAgent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgentD1Ev(
    QQmlListModelWorkerAgent *self) {
  delete self;
}

//  QV4::ExecutionEngine *QQmlListModelWorkerAgent::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK24QQmlListModelWorkerAgent6engineEv(
    const QQmlListModelWorkerAgent *self) {
  return self->engine();
}

//  void QQmlListModelWorkerAgent::addref()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent6addrefEv(
    QQmlListModelWorkerAgent *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "addref()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "addref()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent7releaseEv(
    QQmlListModelWorkerAgent *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "release()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "release()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  int QQmlListModelWorkerAgent::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlListModelWorkerAgent5countEv(
    const QQmlListModelWorkerAgent *self) {
  return self->count();
}

//  void QQmlListModelWorkerAgent::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent5clearEv(
    QQmlListModelWorkerAgent *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::remove(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent6removeEP14QQmlV4Function(
    QQmlListModelWorkerAgent *self,
    QQmlV4FunctionPtr args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remove(QQmlV4FunctionPtr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remove(QQmlV4FunctionPtr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::append(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent6appendEP14QQmlV4Function(
    QQmlListModelWorkerAgent *self,
    QQmlV4FunctionPtr args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "append(QQmlV4FunctionPtr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "append(QQmlV4FunctionPtr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::insert(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent6insertEP14QQmlV4Function(
    QQmlListModelWorkerAgent *self,
    QQmlV4FunctionPtr args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "insert(QQmlV4FunctionPtr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "insert(QQmlV4FunctionPtr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QJSValue QQmlListModelWorkerAgent::get(int index) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK24QQmlListModelWorkerAgent3getEi(
    const QQmlListModelWorkerAgent *self,
    int index) {
  return new QJSValue(self->get(index));
}

//  void QQmlListModelWorkerAgent::move(int from, int to, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent4moveEiii(
    QQmlListModelWorkerAgent *self,
    int from,
    int to,
    int count) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "move(int,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "move(int,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&from)),
      const_cast<void *>(static_cast<const void *>(&to)),
      const_cast<void *>(static_cast<const void *>(&count)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent4syncEv(
    QQmlListModelWorkerAgent *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sync()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sync()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlListModelWorkerAgent::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent14modelDestroyedEv(
    QQmlListModelWorkerAgent *self) {
  self->modelDestroyed();
}

//  void QQmlListModelWorkerAgent::engineChanged(QQmlV4ExecutionEnginePtr
//      engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlListModelWorkerAgent13engineChangedEPN3QV415ExecutionEngineE(
    QQmlListModelWorkerAgent *self,
    QQmlV4ExecutionEnginePtr engine) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlListModelWorkerAgent")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "engineChanged(QQmlV4ExecutionEnginePtr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "engineChanged(QQmlV4ExecutionEnginePtr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&engine)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QQmlListModelWorkerAgent::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlListModelWorkerAgent5eventEP6QEvent(
    QQmlListModelWorkerAgent *self,
    QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQQmlListModelWorkerAgent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlListModelWorkerAgent(
    QQmlListModelWorkerAgent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlListModelWorkerAgent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_list_model)
#endif  // QT_CONFIG(qml_list_model)
