//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmllistcompositor_p.h>
#include <QtCore/qvarlengtharray.h>
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQmlModels/private/qqmltableinstancemodel_p.h>
#include <QtQmlModels/private/qquickpackage_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4identifierhash_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4identifierhashdata_p.h>
#include <QtQml/private/qprimefornumbits_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 933, as local:qqmldelegatemodel.cpp:isDoneIncubating
static bool isDoneIncubating(QQmlIncubator::Status status)
{
     return status == QQmlIncubator::Ready || status == QQmlIncubator::Error;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 938, as local:qqmldelegatemodel.cpp:RequiredPropertiesInitializer
struct RequiredPropertiesInitializer
{
    Q_DISABLE_COPY_MOVE(RequiredPropertiesInitializer)
public:
    RequiredPropertiesInitializer(
            QQmlEngine *engine, QObject *targetObject, RequiredProperties *requiredProperties,
            QQmlDelegateModel::DelegateModelAccess access)
        : engine(engine)
        , targetObject(targetObject)
        , requiredProperties(requiredProperties)
        , access(access)
    {}

    template<typename ModelObjectType>
    void operator()(const QMetaObject *modelMetaObject, ModelObjectType *modelObject) const
    {
        const int end = modelMetaObject->propertyCount() + modelMetaObject->propertyOffset();
        for (int i = modelMetaObject->propertyOffset(); i < end; ++i) {
            auto prop = modelMetaObject->property(i);
            if (!prop.name())
                continue;
            const QString propName = QString::fromUtf8(prop.name());

            bool wasInRequired = false;
            QQmlProperty targetProp = QQmlComponentPrivate::removePropertyFromRequired(
                    targetObject, propName, requiredProperties,
                    engine, &wasInRequired);
            if (!wasInRequired)
                continue;

            QQmlProperty sourceProp(modelObject, propName);
            QQmlAnyBinding forward = QQmlPropertyToPropertyBinding::create(
                    engine, sourceProp, targetProp);
            if (access != QQmlDelegateModel::Qt5ReadWrite)
                forward.setSticky();
            forward.installOn(targetProp);

            if (access != QQmlDelegateModel::ReadWrite || !sourceProp.isWritable())
                continue;

            QQmlAnyBinding reverse = QQmlPropertyToPropertyBinding::create(
                    engine, targetProp, sourceProp);
            reverse.setSticky();
            if constexpr (std::is_base_of_v<QQmlDelegateModelItem, ModelObjectType>) {
                // Temporarily take away the metaobject so that the property can't actually be
                // written. It shouldn't be written since we've just synchronized it the other way
                // when installing the "forward" binding.
                QQmlDelegateModelReadOnlyMetaObject readonly(modelObject, i);
                reverse.installOn(sourceProp);
            } else {
                // It's only not a QQmlDelegateModelItem if the model is actually an ObjectModel.
                // In that case, we hope that the generic equality check when setting a property
                // is enough to de-bounce it.
                reverse.installOn(sourceProp);
            }
        }
    }

private:
    QQmlEngine *engine = nullptr;
    QObject *targetObject = nullptr;
    RequiredProperties *requiredProperties = nullptr;
    QQmlDelegateModel::DelegateModelAccess access
            = QQmlDelegateModel::DelegateModelAccess::ReadOnly;
};

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1588, as local:qqmldelegatemodel.cpp:incrementIndexes
static void incrementIndexes(QQmlDelegateModelItem *cacheItem, int count, const int *deltas)
{
    if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
        for (int i = 1; i < count; ++i)
            incubationTask->index[i] += deltas[i];
    }
    if (QQmlDelegateModelAttached *attached = cacheItem->attached()) {
        for (int i = 1; i < qMin<int>(count, Compositor::MaximumGroupCount); ++i)
            attached->m_currentIndex[i] += deltas[i];
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2992, as local:qqmldelegatemodel.cpp:GroupEmitterListIt
typedef QQmlDelegateModelGroupEmitterList::iterator GroupEmitterListIt;

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 252, as _ZN18QQmlListCompositorC1Ev
inline QQmlListCompositor::QQmlListCompositor()
    : m_end(m_ranges.next, 0, Default, 2)
    , m_cacheIt(m_end)
    , m_groupCount(2)
    , m_defaultFlags(PrependFlag | DefaultFlag)
    , m_removeFlags(AppendFlag | PrependFlag | GroupMask)
    , m_moveId(0)
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 266, as _ZN18QQmlListCompositorD1Ev
inline QQmlListCompositor::~QQmlListCompositor()
{
    for (Range *next, *range = m_ranges.next; range != &m_ranges; range = next) {
        next = range->next;
        delete range;
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1921, as _ZN24QQmlDelegateModelPrivate16emitModelUpdatedERK13QQmlChangeSetb
inline void QQmlDelegateModelPrivate::emitModelUpdated(const QQmlChangeSet &changeSet, bool reset)
{
    Q_Q(QQmlDelegateModel);
    emit q->modelUpdated(changeSet, reset);
    if (changeSet.difference() != 0)
        emit q->countChanged();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1234, as _ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::initPackage(int, QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1233, as _ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::createdPackage(int, QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1235, as _ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage
inline void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage *) {}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1232, as _ZN29QQmlDelegateModelGroupEmitterD2Ev
inline QQmlDelegateModelGroupEmitter::~QQmlDelegateModelGroupEmitter() = default;

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 4059, as _ZN34QQmlReusableDelegateModelItemsPool5drainEiSt8functionIFvP21QQmlDelegateModelItemEE
inline void QQmlReusableDelegateModelItemsPool::drain(int maxPoolTime, std::function<void(QQmlDelegateModelItem *cacheItem)> releaseItem)
{
    // Rather than releasing all pooled items upon a call to this function, each
    // item has a poolTime. The poolTime specifies for how many loading cycles an item
    // has been resting in the pool. And for each invocation of this function, poolTime
    // will increase. If poolTime is equal to, or exceeds, maxPoolTime, it will be removed
    // from the pool and released. This way, the view can tweak a bit for how long
    // items should stay in "circulation", even if they are not recycled right away.
    qCDebug(lcItemViewDelegateRecycling) << "pool size before drain:" << m_reusableItemsPool.size();

    if (maxPoolTime == 0) {
        // Special-case 0 because it's so common and so easy to handle.
        const std::vector<PoolItem> removed = std::exchange(m_reusableItemsPool, {});
        for (const PoolItem &item : removed)
            releaseItem(item.item);
        qCDebug(lcItemViewDelegateRecycling) << "pool size after drain: 0";
        return;
    }

    const auto begin = m_reusableItemsPool.begin();
    const auto oldEnd = m_reusableItemsPool.end();
    const auto newEnd = std::stable_partition(
            begin, oldEnd,
            [maxPoolTime](const PoolItem &item) { return item.poolTime < maxPoolTime; });
    std::for_each(begin, newEnd, [](PoolItem &item) { ++item.poolTime; });

    QVarLengthArray<PoolItem> removed;
    removed.reserve(oldEnd - newEnd);
    std::move(newEnd, oldEnd, std::back_inserter(removed));
    m_reusableItemsPool.erase(newEnd, oldEnd);

    for (const PoolItem &item : removed)
        releaseItem(item.item);

    qCDebug(lcItemViewDelegateRecycling) << "pool size after drain:" << m_reusableItemsPool.size();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2925, as _ZN25QQmlDelegateModelAttached11emitChangesEv
inline void QQmlDelegateModelAttached::emitChanges()
{
    const int groupChanges = m_previousGroups ^ m_cacheItem->groups();
    m_previousGroups = m_cacheItem->groups();

    int indexChanges = 0;
    const qsizetype groupCount = m_cacheItem->metaType()->groupCount();
    for (qsizetype i = 1; i <= groupCount; ++i) {
        if (m_previousIndex[i] != m_currentIndex[i]) {
            m_previousIndex[i] = m_currentIndex[i];
            indexChanges |= (1 << i);
        }
    }

    // Don't access m_cacheItem anymore once we've started sending signals.
    // We don't own it and someone might delete it.

    int notifierId = 0;
    const QMetaObject *meta = metaObject();
    for (qsizetype i = 1; i <= groupCount; ++i, ++notifierId) {
        if (groupChanges & (1 << i))
            QMetaObject::activate(this, meta, notifierId, nullptr);
    }
    for (qsizetype i = 1; i <= groupCount; ++i, ++notifierId) {
        if (indexChanges & (1 << i))
            QMetaObject::activate(this, meta, notifierId, nullptr);
    }

    if (groupChanges)
        emit groupsChanged();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2736, as _ZN25QQmlDelegateModelAttached17resetCurrentIndexEv
inline void QQmlDelegateModelAttached::resetCurrentIndex()
{
    const auto &metaType = m_cacheItem->metaType();
    if (QQDMIncubationTask *incubationTask = m_cacheItem->incubationTask()) {
        for (qsizetype i = 1, end = metaType->groupCount(); i <= end; ++i)
            m_currentIndex[i] = incubationTask->index[i];
    } else if (QQmlDelegateModel *delegateModel = metaType->delegateModel()) {
        QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(delegateModel);
        Compositor::iterator it = model->m_compositor.find(
                Compositor::Cache, model->m_cache.indexOf(m_cacheItem));
        for (qsizetype i = 1, end = metaType->groupCount(); i <= end; ++i)
            m_currentIndex[i] = it.index[i];
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 4029, as _ZN34QQmlReusableDelegateModelItemsPool8takeItemEPK13QQmlComponenti
inline QQmlDelegateModelItem *QQmlReusableDelegateModelItemsPool::takeItem(const QQmlComponent *delegate, int newIndexHint)
{
    // Find the oldest item in the pool that was made from the same delegate as
    // the given argument, remove it from the pool, and return it.
    for (auto it = m_reusableItemsPool.cbegin(); it != m_reusableItemsPool.cend(); ++it) {
        QQmlDelegateModelItem *modelItem = it->item;
        if (modelItem->delegate() != delegate)
            continue;
        m_reusableItemsPool.erase(it);

        qCDebug(lcItemViewDelegateRecycling)
                << "item:" << modelItem
                << "delegate:" << delegate
                << "old index:" << modelItem->modelIndex()
                << "old row:" << modelItem->modelRow()
                << "old column:" << modelItem->modelColumn()
                << "new index:" << newIndexHint
                << "pool size:" << m_reusableItemsPool.size();

        return modelItem;
    }

    qCDebug(lcItemViewDelegateRecycling)
            << "no available item for delegate:" << delegate
            << "new index:" << newIndexHint
            << "pool size:" << m_reusableItemsPool.size();

    return nullptr;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 120, as _ZN3QV414IdentifierHashD1Ev
inline QV4::IdentifierHash::~IdentifierHash()
{
    if (d && !d->refCount.deref())
        delete d;
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 316, as _ZNK18QQmlListCompositor5countENS_5GroupE
inline int QQmlListCompositor::count(Group group) const
{
    return m_end.index[group];
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1084, as _ZN18QQDMIncubationTask13statusChangedEN13QQmlIncubator6StatusE
inline void QQDMIncubationTask::statusChanged(Status status)
{
    if (vdm) {
        vdm->incubatorStatusChanged(this, status);
    } else if (isDoneIncubating(status)) {
        Q_ASSERT(incubating);
        // The model was deleted from under our feet, cleanup ourselves
        incubating->destroyObject();
        incubating->deleteLater();
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1227, as _ZN18QQDMIncubationTask15setInitialStateEP7QObject
inline void QQDMIncubationTask::setInitialState(QObject *o)
{
    vdm->setInitialState(this, o);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3961, as _ZN34QQmlReusableDelegateModelItemsPool10insertItemEP21QQmlDelegateModelItem
inline bool QQmlReusableDelegateModelItemsPool::insertItem(QQmlDelegateModelItem *modelItem)
{
    // We can only hold INT_MAX items, due to the return type of size().
    if (Q_UNLIKELY(m_reusableItemsPool.size() == QQmlReusableDelegateModelItemsPool::MaxSize))
        return false;

    Q_ASSERT(m_reusableItemsPool.size() < QQmlReusableDelegateModelItemsPool::MaxSize);

    // Currently, the only way for a view to reuse items is to call release()
    // in the model class with the second argument explicitly set to
    // QQmlReuseableDelegateModelItemsPool::Reusable. If the released item is
    // no longer referenced, it will be added to the pool. Reusing of items can
    // be specified per item, in case certain items cannot be recycled. A
    // QQmlDelegateModelItem knows which delegate its object was created from.
    // So when we are about to create a new item, we first check if the pool
    // contains an item based on the same delegate from before. If so, we take
    // it out of the pool (instead of creating a new item), and update all its
    // context properties and attached properties.

    // When a view is recycling items, it should call drain() regularly. As
    // there is currently no logic to 'hibernate' items in the pool, they are
    // only meant to rest there for a short while, ideally only from the time
    // e.g a row is unloaded on one side of the view, and until a new row is
    // loaded on the opposite side. Between these times, the application will
    // see the item as fully functional and 'alive' (just not visible on
    // screen). Since this time is supposed to be short, we don't take any
    // action to notify the application about it, since we don't want to
    // trigger any bindings that can disturb performance.

    // A recommended time for calling drain() is each time a view has finished
    // loading e.g a new row or column. If there are more items in the pool
    // after that, it means that the view most likely doesn't need them anytime
    // soon. Those items should be destroyed to reduce resource consumption.

    // Depending on if a view is a list or a table, it can sometimes be
    // performant to keep items in the pool for a bit longer than one "row
    // out/row in" cycle. E.g for a table, if the number of visible rows in a
    // view is much larger than the number of visible columns. In that case, if
    // you flick out a row, and then flick in a column, you would throw away a
    // lot of items in the pool if completely draining it. The reason is that
    // unloading a row places more items in the pool than what ends up being
    // recycled when loading a new column. And then, when you next flick in a
    // new row, you would need to load all those drained items again from
    // scratch. For that reason, you can specify a maxPoolTime to the
    // drainReusableItemsPool() that allows you to keep items in the pool for a
    // bit longer, effectively keeping more items in circulation. A recommended
    // maxPoolTime would be equal to the number of dimensions in the view,
    // which means 1 for a list view and 2 for a table view. If you specify 0,
    // all items will be drained.

    Q_ASSERT(!modelItem->incubationTask());
    Q_ASSERT(!modelItem->isObjectReferenced());
    Q_ASSERT(modelItem->object());
    Q_ASSERT(modelItem->delegate());

    m_reusableItemsPool.push_back({modelItem, 0});

    qCDebug(lcItemViewDelegateRecycling)
            << "item:" << modelItem
            << "delegate:" << modelItem->delegate()
            << "index:" << modelItem->modelIndex()
            << "row:" << modelItem->modelRow()
            << "column:" << modelItem->modelColumn()
            << "pool size:" << m_reusableItemsPool.size();

    return true;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2994, as _ZN29QQmlDelegateModelGroupPrivate14createdPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupPrivate::createdPackage(int index, QQuickPackage *package)
{
    for (GroupEmitterListIt it = emitters.begin(), end = emitters.end(); it != end; ++it)
        it->createdPackage(index, package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3808, as _ZN14QQmlPartsModel17updateFilterGroupEN18QQmlListCompositor5GroupERK13QQmlChangeSet
inline void QQmlPartsModel::updateFilterGroup(
        Compositor::Group group, const QQmlChangeSet &changeSet)
{
    if (!m_inheritGroup)
        return;

    m_compositorGroup = group;
    QQmlDelegateModelGroupPrivate::get(QQmlDelegateModelPrivate::get(m_model)->m_groups[m_compositorGroup])->emitters.insert(this);

    if (!changeSet.isEmpty())
        emit modelUpdated(changeSet, false);

    if (changeSet.difference() != 0)
        emit countChanged();

    emit filterGroupChanged();
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 1305, as _ZN18QQmlListCompositor10transitionENS_5GroupES0_P5QListIN13QQmlChangeSet6ChangeEES5_
inline void QQmlListCompositor::transition(
        Group from,
        Group to,
        QList<QQmlChangeSet::Change> *removes,
        QList<QQmlChangeSet::Change> *inserts)
{
    int removeCount = 0;
    for (iterator it(m_ranges.next, 0, Default, m_groupCount); *it != &m_ranges; *it = it->next) {
        if (it == from && it != to) {
            removes->append(QQmlChangeSet::Change(it.index[from]- removeCount, it->count));
            removeCount += it->count;
        } else if (it != from && it == to) {
            inserts->append(QQmlChangeSet::Change(it.index[to], it->count));
        }
        it.incrementIndexes(it->count);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1600, as _ZN24QQmlDelegateModelPrivate13itemsInsertedERK5QListIN18QQmlListCompositor6InsertEEP15QVarLengthArrayIS0_IN13QQmlChangeSet6ChangeEELx11EEP5QHashIiS0_IP21QQmlDelegateModelItemEE
inline void QQmlDelegateModelPrivate::itemsInserted(
        const QList<Compositor::Insert> &inserts,
        QVarLengthArray<QList<QQmlChangeSet::Change>, Compositor::MaximumGroupCount> *translatedInserts,
        QHash<int, QList<QQmlDelegateModelItem *> > *movedItems)
{
    int cacheIndex = 0;

    int inserted[Compositor::MaximumGroupCount];
    for (int i = 1; i < m_groupCount; ++i)
        inserted[i] = 0;

    for (const Compositor::Insert &insert : inserts) {
        for (; cacheIndex < insert.cacheIndex(); ++cacheIndex)
            incrementIndexes(m_cache.at(cacheIndex), m_groupCount, inserted);

        for (int i = 1; i < m_groupCount; ++i) {
            if (insert.inGroup(i)) {
                (*translatedInserts)[i].append(
                        QQmlChangeSet::Change(insert.index[i], insert.count, insert.moveId));
                inserted[i] += insert.count;
            }
        }

        if (!insert.inCache())
            continue;

        if (movedItems && insert.isMove()) {
            QList<QQmlDelegateModelItem *> items = movedItems->take(insert.moveId);
            Q_ASSERT(items.size() == insert.count);
            m_cache = m_cache.mid(0, insert.cacheIndex())
                    + items + m_cache.mid(insert.cacheIndex());
        }
        if (insert.inGroup()) {
            for (int offset = 0; cacheIndex < insert.cacheIndex() + insert.count;
                 ++cacheIndex, ++offset) {
                QQmlDelegateModelItem *cacheItem = m_cache.at(cacheIndex);
                cacheItem->addGroups(insert.flags & Compositor::GroupMask);

                if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
                    for (int i = 1; i < m_groupCount; ++i)
                        incubationTask->index[i] = cacheItem->groups() & (1 << i)
                                ? insert.index[i] + offset
                                : insert.index[i];
                }
                if (QQmlDelegateModelAttached *attached = cacheItem->attached()) {
                    for (int i = 1; i < m_groupCount; ++i)
                        attached->m_currentIndex[i] = cacheItem->groups() & (1 << i)
                                ? insert.index[i] + offset
                                : insert.index[i];
                }
            }
        } else {
            cacheIndex = insert.cacheIndex() + insert.count;
        }
    }
    for (const QList<QQmlDelegateModelItem *> cache = m_cache; cacheIndex < cache.size(); ++cacheIndex)
        incrementIndexes(cache.at(cacheIndex), m_groupCount, inserted);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2985, as _ZN29QQmlDelegateModelGroupPrivate16emitModelUpdatedEb
inline void QQmlDelegateModelGroupPrivate::emitModelUpdated(bool reset)
{
    for (QQmlDelegateModelGroupEmitterList::iterator it = emitters.begin(); it != emitters.end(); ++it)
        it->emitModelUpdated(changeSet, reset);
    changeSet.clear();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1709, as _ZN24QQmlDelegateModelPrivate12itemsRemovedERK5QListIN18QQmlListCompositor6RemoveEEP15QVarLengthArrayIS0_IN13QQmlChangeSet6ChangeEELx11EEP5QHashIiS0_IP21QQmlDelegateModelItemEE
inline void QQmlDelegateModelPrivate::itemsRemoved(
        const QList<Compositor::Remove> &removes,
        QVarLengthArray<QList<QQmlChangeSet::Change>, Compositor::MaximumGroupCount> *translatedRemoves,
        QHash<int, QList<QQmlDelegateModelItem *> > *movedItems)
{
    int cacheIndex = 0;
    int removedCache = 0;

    int removed[Compositor::MaximumGroupCount];
    for (int i = 1; i < m_groupCount; ++i)
        removed[i] = 0;

    for (const Compositor::Remove &remove : removes) {
        for (; cacheIndex < remove.cacheIndex() && cacheIndex < m_cache.size(); ++cacheIndex)
            incrementIndexes(m_cache.at(cacheIndex), m_groupCount, removed);

        for (int i = 1; i < m_groupCount; ++i) {
            if (remove.inGroup(i)) {
                (*translatedRemoves)[i].append(
                        QQmlChangeSet::Change(remove.index[i], remove.count, remove.moveId));
                removed[i] -= remove.count;
            }
        }

        if (!remove.inCache())
            continue;

        if (movedItems && remove.isMove()) {
            movedItems->insert(remove.moveId, m_cache.mid(remove.cacheIndex(), remove.count));
            QList<QQmlDelegateModelItem *>::const_iterator begin = m_cache.constBegin() + remove.cacheIndex();
            QList<QQmlDelegateModelItem *>::const_iterator end = begin + remove.count;
            m_cache.erase(begin, end);
        } else {
            for (; cacheIndex < remove.cacheIndex() + remove.count - removedCache; ++cacheIndex) {
                QQmlDelegateModelItem *cacheItem = m_cache.at(cacheIndex);
                if (remove.inGroup(Compositor::Persisted)
                        && cacheItem->objectStrongRef() == 0
                        && cacheItem->objectWeakRef() == 0
                        && cacheItem->object()) {
                    QObject *object = cacheItem->object();
                    cacheItem->destroyObjectLater();
                    if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object))
                        emitDestroyingPackage(package);
                    else
                        emitDestroyingItem(object);
                }
                if (!cacheItem->isScriptReferenced()
                        && !cacheItem->object()
                        && !remove.inGroup(Compositor::Persisted)) {
                    m_compositor.clearFlags(Compositor::Cache, cacheIndex, 1, Compositor::CacheFlag);
                    m_cache.removeAt(cacheIndex);
                    delete cacheItem;
                    --cacheIndex;
                    ++removedCache;
                    Q_ASSERT(m_cache.size() == m_compositor.count(Compositor::Cache));
                } else if (remove.groups() == cacheItem->groups()) {
                    cacheItem->setGroups(0);
                    if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
                        for (int i = 1; i < m_groupCount; ++i)
                            incubationTask->index[i] = -1;
                    }
                    if (QQmlDelegateModelAttached *attached = cacheItem->attached()) {
                        for (int i = 1; i < m_groupCount; ++i)
                            attached->m_currentIndex[i] = -1;
                    }
                } else {
                    if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
                        if (!cacheItem->isObjectReferenced()) {
                            releaseIncubator(incubationTask);
                            cacheItem->clearIncubationTask();
                            if (QObject *object = cacheItem->object()) {
                                cacheItem->destroyObjectLater();
                                if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object))
                                    emitDestroyingPackage(package);
                                else
                                    emitDestroyingItem(object);
                            }
                        } else {
                            for (int i = 1; i < m_groupCount; ++i) {
                                if (remove.inGroup(i))
                                    incubationTask->index[i] = remove.index[i];
                            }
                        }
                    }
                    if (QQmlDelegateModelAttached *attached = cacheItem->attached()) {
                        for (int i = 1; i < m_groupCount; ++i) {
                            if (remove.inGroup(i))
                                attached->m_currentIndex[i] = remove.index[i];
                        }
                    }
                    cacheItem->removeGroups(remove.flags);
                }
            }
        }
    }

    for (const QList<QQmlDelegateModelItem *> cache = m_cache; cacheIndex < cache.size(); ++cacheIndex)
        incrementIndexes(cache.at(cacheIndex), m_groupCount, removed);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 28, as _Z27lcItemViewDelegateRecyclingv
inline const QLoggingCategory &lcItemViewDelegateRecycling()
{
    static const QLoggingCategory category("qt.qml.delegatemodel.recycling");
    return category;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 182, as _ZN24QQmlDelegateModelPrivateD1Ev
inline QQmlDelegateModelPrivate::~QQmlDelegateModelPrivate()
{
    qDeleteAll(m_finishedIncubating);

    // Free up all items in the pool
    drainReusableItemsPool(0);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 207, as _ZN24QQmlDelegateModelPrivate4initEv
inline void QQmlDelegateModelPrivate::init()
{
    Q_Q(QQmlDelegateModel);
    m_compositor.setRemoveGroups(Compositor::GroupMask & ~Compositor::PersistedFlag);

    m_items = new QQmlDelegateModelGroup(QStringLiteral("items"), q, Compositor::Default, q);
    m_items->setDefaultInclude(true);
    m_persistedItems = new QQmlDelegateModelGroup(QStringLiteral("persistedItems"), q, Compositor::Persisted, q);
    QQmlDelegateModelGroupPrivate::get(m_items)->emitters.insert(this);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 338, as _ZN24QQmlDelegateModelPrivate26connectToAbstractItemModelEv
inline void QQmlDelegateModelPrivate::connectToAbstractItemModel()
{
    Q_Q(QQmlDelegateModel);
    if (!m_adaptorModel.adaptsAim())
        return;

    auto aim = m_adaptorModel.aim();

    QObject::connect(aim, &QAbstractItemModel::rowsInserted, q, &QQmlDelegateModel::_q_rowsInserted);
    QObject::connect(aim, &QAbstractItemModel::rowsRemoved, q, &QQmlDelegateModel::_q_rowsRemoved);
    QObject::connect(aim, &QAbstractItemModel::rowsAboutToBeRemoved, q, &QQmlDelegateModel::_q_rowsAboutToBeRemoved);
    QObject::connect(aim, &QAbstractItemModel::columnsInserted, q, &QQmlDelegateModel::_q_columnsInserted);
    QObject::connect(aim, &QAbstractItemModel::columnsRemoved, q, &QQmlDelegateModel::_q_columnsRemoved);
    QObject::connect(aim, &QAbstractItemModel::columnsMoved, q, &QQmlDelegateModel::_q_columnsMoved);
    QObject::connect(aim, &QAbstractItemModel::dataChanged, q, &QQmlDelegateModel::_q_dataChanged);
    QObject::connect(aim, &QAbstractItemModel::rowsMoved, q, &QQmlDelegateModel::_q_rowsMoved);
    QObject::connect(aim, &QAbstractItemModel::modelAboutToBeReset, q, &QQmlDelegateModel::_q_modelAboutToBeReset);
    QObject::connect(aim, &QAbstractItemModel::layoutChanged, q, &QQmlDelegateModel::_q_layoutChanged);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 358, as _ZN24QQmlDelegateModelPrivate31disconnectFromAbstractItemModelEv
inline void QQmlDelegateModelPrivate::disconnectFromAbstractItemModel()
{
    Q_Q(QQmlDelegateModel);
    if (!m_adaptorModel.adaptsAim())
        return;

    auto aim = m_adaptorModel.aim();

    QObject::disconnect(aim, &QAbstractItemModel::rowsInserted, q, &QQmlDelegateModel::_q_rowsInserted);
    QObject::disconnect(aim, &QAbstractItemModel::rowsAboutToBeRemoved, q, &QQmlDelegateModel::_q_rowsAboutToBeRemoved);
    QObject::disconnect(aim, &QAbstractItemModel::rowsRemoved, q, &QQmlDelegateModel::_q_rowsRemoved);
    QObject::disconnect(aim, &QAbstractItemModel::columnsInserted, q, &QQmlDelegateModel::_q_columnsInserted);
    QObject::disconnect(aim, &QAbstractItemModel::columnsRemoved, q, &QQmlDelegateModel::_q_columnsRemoved);
    QObject::disconnect(aim, &QAbstractItemModel::columnsMoved, q, &QQmlDelegateModel::_q_columnsMoved);
    QObject::disconnect(aim, &QAbstractItemModel::dataChanged, q, &QQmlDelegateModel::_q_dataChanged);
    QObject::disconnect(aim, &QAbstractItemModel::rowsMoved, q, &QQmlDelegateModel::_q_rowsMoved);
    QObject::disconnect(aim, &QAbstractItemModel::modelAboutToBeReset, q, &QQmlDelegateModel::_q_modelAboutToBeReset);
    QObject::disconnect(aim, &QAbstractItemModel::layoutChanged, q, &QQmlDelegateModel::_q_layoutChanged);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 198, as _ZN24QQmlDelegateModelPrivate22requestMoreIfNecessaryEv
inline void QQmlDelegateModelPrivate::requestMoreIfNecessary()
{
    Q_Q(QQmlDelegateModel);
    if (!m_waitingToFetchMore && m_adaptorModel.canFetchMore()) {
        m_waitingToFetchMore = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::UpdateRequest));
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 915, as _ZN24QQmlDelegateModelPrivate18emitCreatedPackageEP18QQDMIncubationTaskP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitCreatedPackage(QQDMIncubationTask *incubationTask, QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->createdPackage(incubationTask->index[i], package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 637, as _ZN24QQmlDelegateModelPrivate16destroyCacheItemEP21QQmlDelegateModelItem
inline void QQmlDelegateModelPrivate::destroyCacheItem(QQmlDelegateModelItem *cacheItem)
{
    if (QObject *object = cacheItem->object()) {
        emitDestroyingItem(object);
        cacheItem->destroyObjectLater();
    }

    if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
        releaseIncubator(incubationTask);
        cacheItem->clearIncubationTask();
    }
    cacheItem->dispose();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1142, as _ZN24QQmlDelegateModelPrivate22drainReusableItemsPoolEi
inline void QQmlDelegateModelPrivate::drainReusableItemsPool(int maxPoolTime)
{
    m_reusableItemsPool.drain(maxPoolTime, [this](QQmlDelegateModelItem *cacheItem){ destroyCacheItem(cacheItem); });
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1157, as _ZN24QQmlDelegateModelPrivate15resolveDelegateEi
inline QQmlComponent *QQmlDelegateModelPrivate::resolveDelegate(int index)
{
    if (!m_delegateChooser)
        return m_delegate;

    QQmlComponent *delegate = nullptr;
    QQmlAbstractDelegateComponent *chooser = m_delegateChooser;

    do {
        delegate = chooser->delegate(&m_adaptorModel, index);
        chooser = qobject_cast<QQmlAbstractDelegateComponent *>(delegate);
    } while (chooser);

    return delegate;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1659, as _ZN24QQmlDelegateModelPrivate13itemsInsertedERK5QListIN18QQmlListCompositor6InsertEE
inline void QQmlDelegateModelPrivate::itemsInserted(const QList<Compositor::Insert> &inserts)
{
    QVarLengthArray<QList<QQmlChangeSet::Change>, Compositor::MaximumGroupCount> translatedInserts(m_groupCount);
    itemsInserted(inserts, &translatedInserts);
    Q_ASSERT(m_cache.size() == m_compositor.count(Compositor::Cache));
    if (!m_delegate)
        return;

    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->changeSet.insert(translatedInserts.at(i));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1512, as _ZN24QQmlDelegateModelPrivate12itemsChangedERK5QListIN18QQmlListCompositor6ChangeEE
inline void QQmlDelegateModelPrivate::itemsChanged(const QList<Compositor::Change> &changes)
{
    if (!m_delegate)
        return;

    QVarLengthArray<QList<QQmlChangeSet::Change>, Compositor::MaximumGroupCount> translatedChanges(m_groupCount);

    for (const Compositor::Change &change : changes) {
        for (int i = 1; i < m_groupCount; ++i) {
            if (change.inGroup(i)) {
                translatedChanges[i].append(QQmlChangeSet::Change(change.index[i], change.count));
            }
        }
    }

    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->changeSet.change(translatedChanges.at(i));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 190, as _ZNK24QQmlDelegateModelPrivate17adaptorModelCountEv
inline int QQmlDelegateModelPrivate::adaptorModelCount() const
{
    // QQmlDelegateModel currently only support list models.
    // So even if a model is a table model, only the first
    // column will be used.
    return m_adaptorModel.rowCount();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 695, as _ZN24QQmlDelegateModelPrivate12group_appendEP16QQmlListPropertyI22QQmlDelegateModelGroupEPS1_
inline void QQmlDelegateModelPrivate::group_append(
        QQmlListProperty<QQmlDelegateModelGroup> *property, QQmlDelegateModelGroup *group)
{
    QQmlDelegateModelPrivate *d = static_cast<QQmlDelegateModelPrivate *>(property->data);
    if (d->m_complete)
        return;
    if (d->m_groupCount == Compositor::MaximumGroupCount) {
        qmlWarning(d->q_func()) << QQmlDelegateModel::tr("The maximum number of supported DelegateModelGroups is 8");
        return;
    }
    d->m_groups[d->m_groupCount] = group;
    d->m_groupCount += 1;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 709, as _ZN24QQmlDelegateModelPrivate11group_countEP16QQmlListPropertyI22QQmlDelegateModelGroupE
inline qsizetype QQmlDelegateModelPrivate::group_count(
        QQmlListProperty<QQmlDelegateModelGroup> *property)
{
    QQmlDelegateModelPrivate *d = static_cast<QQmlDelegateModelPrivate *>(property->data);
    return d->m_groupCount - 1;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 716, as _ZN24QQmlDelegateModelPrivate8group_atEP16QQmlListPropertyI22QQmlDelegateModelGroupEx
inline QQmlDelegateModelGroup *QQmlDelegateModelPrivate::group_at(
        QQmlListProperty<QQmlDelegateModelGroup> *property, qsizetype index)
{
    QQmlDelegateModelPrivate *d = static_cast<QQmlDelegateModelPrivate *>(property->data);
    return index >= 0 && index < d->m_groupCount - 1
            ? d->m_groups[index + 1]
            : nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1096, as _ZN24QQmlDelegateModelPrivate16releaseIncubatorEP18QQDMIncubationTask
inline void QQmlDelegateModelPrivate::releaseIncubator(QQDMIncubationTask *incubationTask)
{
    Q_Q(QQmlDelegateModel);
    if (!incubationTask->isError())
        incubationTask->clear();
    m_finishedIncubating.append(incubationTask);
    if (!m_incubatorCleanupScheduled) {
        m_incubatorCleanupScheduled = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}
//  -----------------------------------------------------------------------

//  A QQmlDelegateModelPrivate that Python can take functions over in. Every QQmlDelegateModelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelPrivateCall0)(const void *, const QQmlChangeSet *, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelPrivateCall1)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelPrivateCall2)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlDelegateModelPrivateCall3)(const void *, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
class CuteQQmlDelegateModelPrivate : public QQmlDelegateModelPrivate {
public:
  using QQmlDelegateModelPrivate::QQmlDelegateModelPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQmlChangeSetb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelPrivate::emitModelUpdated(const QQmlChangeSet
  //      &changeSet, bool reset)
  void emitModelUpdated(
      const QQmlChangeSet &changeSet,
      bool reset) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelegateModelPrivateCall0 call = reinterpret_cast<CuteQQmlDelegateModelPrivateCall0>(taken[0]);
      call(this, &changeSet, reset, &handled);
      if (handled) return;
    }
    QQmlDelegateModelPrivate::emitModelUpdated(changeSet, reset);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::createdPackage(int a0,
  //      QQuickPackage *a1)
  void createdPackage(int a0, QQuickPackage *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelegateModelPrivateCall1 call = reinterpret_cast<CuteQQmlDelegateModelPrivateCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::createdPackage(a0, a1);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::initPackage(int a0, QQuickPackage
  //      *a1)
  void initPackage(int a0, QQuickPackage *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelegateModelPrivateCall2 call = reinterpret_cast<CuteQQmlDelegateModelPrivateCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::initPackage(a0, a1);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlDelegateModelGroupEmitter::destroyingPackage(QQuickPackage
  //      *a0)
  void destroyingPackage(QQuickPackage *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelegateModelPrivateCall3 call = reinterpret_cast<CuteQQmlDelegateModelPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDelegateModelGroupEmitter::destroyingPackage(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)
};

//  QQmlDelegateModel *QQmlDelegateModelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZN24QQmlDelegateModelPrivate6q_funcEv(
    QQmlDelegateModelPrivate *self) {
  return self->q_func();
}

//  const QQmlDelegateModel *QQmlDelegateModelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlDelegateModel *ritual_ZNK24QQmlDelegateModelPrivate6q_funcEv(
    const QQmlDelegateModelPrivate *self) {
  return self->q_func();
}

//  QQmlDelegateModelPrivate::~QQmlDelegateModelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivateD1Ev(
    QQmlDelegateModelPrivate *self) {
  delete self;
}

//  QQmlDelegateModelPrivate *QQmlDelegateModelPrivate::get(QQmlDelegateModel
//      *m)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPrivate *ritual_ZN24QQmlDelegateModelPrivate3getEP17QQmlDelegateModel(
    QQmlDelegateModel *m) {
  return QQmlDelegateModelPrivate::get(m);
}

//  void QQmlDelegateModelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate4initEv(
    QQmlDelegateModelPrivate *self) {
  self->init();
}

//  void QQmlDelegateModelPrivate::connectToAbstractItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate26connectToAbstractItemModelEv(
    QQmlDelegateModelPrivate *self) {
  self->connectToAbstractItemModel();
}

//  void QQmlDelegateModelPrivate::disconnectFromAbstractItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate31disconnectFromAbstractItemModelEv(
    QQmlDelegateModelPrivate *self) {
  self->disconnectFromAbstractItemModel();
}

//  void QQmlDelegateModelPrivate::requestMoreIfNecessary()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate22requestMoreIfNecessaryEv(
    QQmlDelegateModelPrivate *self) {
  self->requestMoreIfNecessary();
}

//  void QQmlDelegateModelPrivate::emitCreatedPackage(QQDMIncubationTask
//      *incubationTask, QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate18emitCreatedPackageEP18QQDMIncubationTaskP13QQuickPackage(
    QQmlDelegateModelPrivate *self,
    QQDMIncubationTask *incubationTask,
    QQuickPackage *package) {
  self->emitCreatedPackage(incubationTask, package);
}

//  void QQmlDelegateModelPrivate::emitCreatedItem(QQDMIncubationTask
//      *incubationTask, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate15emitCreatedItemEP18QQDMIncubationTaskP7QObject(
    QQmlDelegateModelPrivate *self,
    QQDMIncubationTask *incubationTask,
    QObject *item) {
  self->emitCreatedItem(incubationTask, item);
}

//  void QQmlDelegateModelPrivate::emitInitItem(QQDMIncubationTask
//      *incubationTask, QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate12emitInitItemEP18QQDMIncubationTaskP7QObject(
    QQmlDelegateModelPrivate *self,
    QQDMIncubationTask *incubationTask,
    QObject *item) {
  self->emitInitItem(incubationTask, item);
}

//  void QQmlDelegateModelPrivate::emitDestroyingItem(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate18emitDestroyingItemEP7QObject(
    QQmlDelegateModelPrivate *self,
    QObject *item) {
  self->emitDestroyingItem(item);
}

//  void QQmlDelegateModelPrivate::destroyCacheItem(QQmlDelegateModelItem
//      *cacheItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate16destroyCacheItemEP21QQmlDelegateModelItem(
    QQmlDelegateModelPrivate *self,
    QQmlDelegateModelItem *cacheItem) {
  self->destroyCacheItem(cacheItem);
}

//  void QQmlDelegateModelPrivate::drainReusableItemsPool(int maxPoolTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate22drainReusableItemsPoolEi(
    QQmlDelegateModelPrivate *self,
    int maxPoolTime) {
  self->drainReusableItemsPool(maxPoolTime);
}

//  QQmlComponent *QQmlDelegateModelPrivate::resolveDelegate(int index)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN24QQmlDelegateModelPrivate15resolveDelegateEi(
    QQmlDelegateModelPrivate *self,
    int index) {
  return self->resolveDelegate(index);
}

//  void QQmlDelegateModelPrivate::itemsInserted(const
//      QList<Compositor::Insert> &inserts)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate13itemsInsertedERK5QListIN18QQmlListCompositor6InsertEE(
    QQmlDelegateModelPrivate *self,
    const QList<Compositor::Insert> *inserts) {
  self->itemsInserted(*inserts);
}

//  void QQmlDelegateModelPrivate::itemsChanged(const
//      QList<Compositor::Change> &changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate12itemsChangedERK5QListIN18QQmlListCompositor6ChangeEE(
    QQmlDelegateModelPrivate *self,
    const QList<Compositor::Change> *changes) {
  self->itemsChanged(*changes);
}

//  void QQmlDelegateModelPrivate::emitModelUpdated(const QQmlChangeSet
//      &changeSet, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate16emitModelUpdatedERK13QQmlChangeSetb(
    QQmlDelegateModelPrivate *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->emitModelUpdated(*changeSet, reset);
}

//  int QQmlDelegateModelPrivate::adaptorModelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlDelegateModelPrivate17adaptorModelCountEv(
    const QQmlDelegateModelPrivate *self) {
  return self->adaptorModelCount();
}

//  void QQmlDelegateModelPrivate::group_append(QQmlListProperty<QQmlDelegate
//      ModelGroup> *property, QQmlDelegateModelGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate12group_appendEP16QQmlListPropertyI22QQmlDelegateModelGroupEPS1_(
    QQmlListProperty<QQmlDelegateModelGroup> *property,
    QQmlDelegateModelGroup *group) {
  QQmlDelegateModelPrivate::group_append(property, group);
}

//  qsizetype QQmlDelegateModelPrivate::group_count(QQmlListProperty<QQmlDele
//      gateModelGroup> *property)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QQmlDelegateModelPrivate11group_countEP16QQmlListPropertyI22QQmlDelegateModelGroupE(
    QQmlListProperty<QQmlDelegateModelGroup> *property) {
  return QQmlDelegateModelPrivate::group_count(property);
}

//  QQmlDelegateModelGroup *QQmlDelegateModelPrivate::group_at(QQmlListProper
//      ty<QQmlDelegateModelGroup> *property, qsizetype index)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN24QQmlDelegateModelPrivate8group_atEP16QQmlListPropertyI22QQmlDelegateModelGroupEx(
    QQmlListProperty<QQmlDelegateModelGroup> *property,
    qsizetype index) {
  return QQmlDelegateModelPrivate::group_at(property, index);
}

//  void QQmlDelegateModelPrivate::releaseIncubator(QQDMIncubationTask
//      *incubationTask)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPrivate16releaseIncubatorEP18QQDMIncubationTask(
    QQmlDelegateModelPrivate *self,
    QQDMIncubationTask *incubationTask) {
  self->releaseIncubator(incubationTask);
}

//  QQmlDelegateModelPrivate as the QQmlDelegateModelGroupEmitter it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroupEmitter *ritual_cast_QQmlDelegateModelPrivate_QQmlDelegateModelGroupEmitter(
    QQmlDelegateModelPrivate *self) {
  return static_cast<QQmlDelegateModelGroupEmitter *>(self);
}

//  a Python function taken by a CuteQQmlDelegateModelPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelPrivate(
    QQmlDelegateModelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelPrivate *>(self)->take(key, call);
}

//  void QQmlDelegateModelPrivate::emitModelUpdated(const QQmlChangeSet
//      &changeSet, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlDelegateModelPrivate16emitModelUpdatedERK13QQmlChangeSetb(
    QQmlDelegateModelPrivate *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->QQmlDelegateModelPrivate::emitModelUpdated(*changeSet, reset);
}

//  a QQmlDelegateModel::ReleaseFlags a ritual of QQmlDelegateModelPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDelegateModelPrivate__QQmlDelegateModel_ReleaseFlags(
    QQmlDelegateModel::ReleaseFlags *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
