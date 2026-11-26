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
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtQmlModels/private/qqmllistcompositor_p.h>
#include <QtCore/qvarlengtharray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 933, as local:qqmldelegatemodel.cpp:isDoneIncubating
static bool isDoneIncubating(QQmlIncubator::Status status)
{
     return status == QQmlIncubator::Ready || status == QQmlIncubator::Error;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2992, as local:qqmldelegatemodel.cpp:GroupEmitterListIt
typedef QQmlDelegateModelGroupEmitterList::iterator GroupEmitterListIt;

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3926, as _ZN14QQmlPartsModel11initPackageEiP13QQuickPackage
inline void QQmlPartsModel::initPackage(int index, QQuickPackage *package)
{
    if (m_modelUpdatePending)
        m_pendingPackageInitializations << index;
    else
        emit initItem(index, package->part(m_part));
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3826, as _ZNK14QQmlPartsModel5countEv
inline int QQmlPartsModel::count() const
{
    QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);
    return model->m_delegate
            ? model->m_compositor.count(m_compositorGroup)
            : 0;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3834, as _ZNK14QQmlPartsModel7isValidEv
inline bool QQmlPartsModel::isValid() const
{
    return m_model->isValid();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3839, as _ZN14QQmlPartsModel6objectEiN13QQmlIncubator14IncubationModeE
inline QObject *QQmlPartsModel::object(int index, QQmlIncubator::IncubationMode incubationMode)
{
    QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);

    if (!model->m_delegate || index < 0 || index >= model->m_compositor.count(m_compositorGroup)) {
        qWarning() << "DelegateModel::item: index out range" << index << model->m_compositor.count(m_compositorGroup);
        return nullptr;
    }

    QObject *object = model->object(m_compositorGroup, index, incubationMode);

    if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object)) {
        QObject *part = package->part(m_part);
        if (!part)
            return nullptr;
        m_packaged.insert(part, package);
        return part;
    }

    model->release(object);
    if (!model->m_delegateValidated) {
        if (object)
            qmlWarning(model->m_delegate) << tr("Delegate component must be Package type.");
        model->m_delegateValidated = true;
    }

    return nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3868, as _ZN14QQmlPartsModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE
inline QQmlInstanceModel::ReleaseFlags QQmlPartsModel::release(QObject *item, ReusableFlag)
{
    QQmlInstanceModel::ReleaseFlags flags;

    auto it = m_packaged.find(item);
    if (it != m_packaged.end()) {
        QQuickPackage *package = *it;
        QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);
        flags = model->release(package);
        m_packaged.erase(it);
        if (!m_packaged.contains(item))
            flags &= ~Referenced;
        if (flags & Destroyed)
            QQmlDelegateModelPrivate::get(m_model)->emitDestroyingPackage(package);
    }
    return flags;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3886, as _ZN14QQmlPartsModel12variantValueEiRK7QString
inline QVariant QQmlPartsModel::variantValue(int index, const QString &role)
{
    return QQmlDelegateModelPrivate::get(m_model)->variantValue(m_compositorGroup, index, role);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3898, as _ZN14QQmlPartsModel16incubationStatusEi
inline QQmlIncubator::Status QQmlPartsModel::incubationStatus(int index)
{
    QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);
    Compositor::iterator it = model->m_compositor.find(model->m_compositorGroup, index);
    if (!it->inCache())
        return QQmlIncubator::Null;

    if (auto incubationTask = model->m_cache.at(it.cacheIndex())->incubationTask())
        return incubationTask->status();

    return QQmlIncubator::Ready;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3911, as _ZNK14QQmlPartsModel7indexOfEP7QObjectS1_
inline int QQmlPartsModel::indexOf(QObject *item, QObject *) const
{
    auto it = m_packaged.find(item);
    if (it != m_packaged.end()) {
        if (QQmlDelegateModelItem *cacheItem = QQmlDelegateModelItem::dataForObject(*it))
            return cacheItem->groupIndex(m_compositorGroup);
    }
    return -1;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3941, as _ZN14QQmlPartsModel16emitModelUpdatedERK13QQmlChangeSetb
inline void QQmlPartsModel::emitModelUpdated(const QQmlChangeSet &changeSet, bool reset)
{
    m_modelUpdatePending = false;
    emit modelUpdated(changeSet, reset);
    if (changeSet.difference() != 0)
        emit countChanged();

    QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);
    QList<int> pendingPackageInitializations;
    qSwap(pendingPackageInitializations, m_pendingPackageInitializations);
    for (int index : pendingPackageInitializations) {
        if (!model->m_delegate || index < 0 || index >= model->m_compositor.count(m_compositorGroup))
            continue;
        QObject *object = model->object(m_compositorGroup, index, QQmlIncubator::Asynchronous);
        if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object))
            emit initItem(index, package->part(m_part));
        model->release(object);
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3921, as _ZN14QQmlPartsModel14createdPackageEiP13QQuickPackage
inline void QQmlPartsModel::createdPackage(int index, QQuickPackage *package)
{
    emit createdItem(index, package->part(m_part));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3934, as _ZN14QQmlPartsModel17destroyingPackageEP13QQuickPackage
inline void QQmlPartsModel::destroyingPackage(QQuickPackage *package)
{
    QObject *item = package->part(m_part);
    Q_ASSERT(!m_packaged.contains(item));
    emit destroyingItem(item);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 316, as _ZNK18QQmlListCompositor5countENS_5GroupE
inline int QQmlListCompositor::count(Group group) const
{
    return m_end.index[group];
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 927, as _ZN24QQmlDelegateModelPrivate21emitDestroyingPackageEP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitDestroyingPackage(QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->destroyingPackage(package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 615, as _ZN24QQmlDelegateModelPrivate7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE
inline QQmlDelegateModel::ReleaseFlags QQmlDelegateModelPrivate::release(QObject *object, QQmlInstanceModel::ReusableFlag reusableFlag)
{
    if (!object)
        return QQmlDelegateModel::ReleaseFlags{};

    QQmlDelegateModelItem *cacheItem = QQmlDelegateModelItem::dataForObject(object);
    if (!cacheItem)
        return QQmlDelegateModel::ReleaseFlags{};

    if (!cacheItem->releaseObjectWeak())
        return QQmlDelegateModel::Referenced;

    if (reusableFlag == QQmlInstanceModel::Reusable && m_reusableItemsPool.insertItem(cacheItem)) {
        removeCacheItem(cacheItem);
        emit q_func()->itemPooled(cacheItem->modelIndex(), cacheItem->object());
        return QQmlInstanceModel::Pooled;
    }

    destroyCacheItem(cacheItem);
    return QQmlInstanceModel::Destroyed;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1414, as _ZN24QQmlDelegateModelPrivate12variantValueEN18QQmlListCompositor5GroupEiRK7QString
inline QVariant QQmlDelegateModelPrivate::variantValue(QQmlListCompositor::Group group, int index, const QString &name)
{
    Compositor::iterator it = m_compositor.find(group, index);
    if (QQmlAdaptorModel *model = it.list<QQmlAdaptorModel>()) {
        QString role = name;
        int dot = name.indexOf(QLatin1Char('.'));
        if (dot > 0)
            role = name.left(dot);
        QVariant value = model->value(it.modelIndex(), role);
        while (dot > 0) {
            const int from = dot + 1;
            dot = name.indexOf(QLatin1Char('.'), from);
            QStringView propertyName = QStringView{name}.mid(from, dot - from);
            if (QObject *obj = qvariant_cast<QObject*>(value)) {
                value = obj->property(propertyName.toUtf8());
            } else if (const QMetaObject *metaObject = QQmlMetaType::metaObjectForValueType(value.metaType())) {
                // Q_GADGET
                const int propertyIndex = metaObject->indexOfProperty(propertyName.toUtf8());
                if (propertyIndex >= 0)
                    value = metaObject->property(propertyIndex).readOnGadget(value.constData());
            } else {
                return QVariant();
            }
        }
        return value;
    }
    return QVariant();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1250, as _ZN24QQmlDelegateModelPrivate6objectEN18QQmlListCompositor5GroupEiN13QQmlIncubator14IncubationModeE
inline QObject *QQmlDelegateModelPrivate::object(Compositor::Group group, int index, QQmlIncubator::IncubationMode incubationMode)
{
    if (!m_delegate || index < 0 || index >= m_compositor.count(group)) {
        qWarning() << "DelegateModel::item: index out range" << index << m_compositor.count(group);
        return nullptr;
    } else if (!m_context || !m_context->isValid()) {
        return nullptr;
    }

    Compositor::iterator it = m_compositor.find(group, index);
    const auto flags = it->flags;
    const auto modelIndex = it.modelIndex();

    QQmlDelegateModelItem *cacheItem = it->inCache() ? m_cache.at(it.cacheIndex()) : 0;

    if (!cacheItem || !cacheItem->delegate()) {
        QQmlComponent *delegate = resolveDelegate(modelIndex);
        if (!delegate)
            return nullptr;

        if (!cacheItem) {
            cacheItem = m_reusableItemsPool.takeItem(delegate, index);
            if (cacheItem) {
                // Move the pooled item back into the cache, update
                // all related properties, and return the object (which
                // has already been incubated, otherwise it wouldn't be in the pool).
                addCacheItem(cacheItem, it);
                reuseItem(cacheItem, index, flags);

                if (index == m_compositor.count(group) - 1)
                    requestMoreIfNecessary();
                return cacheItem->referenceObjectWeak();
            }

            // Since we could't find an available item in the pool, we create a new one
            cacheItem = m_adaptorModel.createItem(m_cacheMetaType, modelIndex);
            if (!cacheItem)
                return nullptr;

            cacheItem->setGroups(flags);
            addCacheItem(cacheItem, it);
        }

        cacheItem->setDelegate(delegate);
    }

    {
        // Bump the reference counts temporarily so neither the content data or the delegate object
        // are deleted if incubatorStatusChanged() is called synchronously.
        QQmlDelegateModelItem::ScriptReference scriptRef(cacheItem);
        QQmlDelegateModelItem::ObjectReference objectRef(cacheItem);

        if (QQDMIncubationTask *incubationTask = cacheItem->incubationTask()) {
            bool sync = (incubationMode == QQmlIncubator::Synchronous
                         || incubationMode == QQmlIncubator::AsynchronousIfNested);
            if (sync && incubationTask->incubationMode() == QQmlIncubator::Asynchronous) {
                // previously requested async - now needed immediately
                incubationTask->forceCompletion();
            }
        } else if (!cacheItem->object()) {
            QQmlContext *creationContext = cacheItem->delegate()->creationContext();

            QQDMIncubationTask *incubationTask = new QQDMIncubationTask(this, incubationMode);
            cacheItem->setIncubationTask(incubationTask);
            incubationTask->incubating = cacheItem;
            incubationTask->clear();

            for (int i = 1; i < m_groupCount; ++i)
                incubationTask->index[i] = it.index[i];

            const QQmlRefPointer<QQmlContextData> componentContext
                    = QQmlContextData::get(creationContext  ? creationContext : m_context.data());
            QQmlComponentPrivate *cp = QQmlComponentPrivate::get(cacheItem->delegate());

            if (cp->isBound()) {
                cacheItem->setContextData(componentContext);

                // Ignore return value of initProxy. We want to know the proxy when assigning required
                // properties, but we don't want it to pollute our context. The context is bound.
                if (m_adaptorModel.hasProxyObject())
                    cacheItem->initProxy();

                cp->incubateObject(
                        incubationTask, cacheItem->delegate(), m_context->engine(),
                        componentContext, QQmlContextData::get(m_context));
            } else {
                QQmlRefPointer<QQmlContextData> ctxt
                        = QQmlContextData::createRefCounted(componentContext);
                ctxt->setContextObject(cacheItem);
                cacheItem->setContextData(ctxt);

                // If the model is read-only we cannot just expose the object as context
                // We actually need a separate model object to moderate access.
                if (m_adaptorModel.hasProxyObject()) {
                    if (m_adaptorModel.delegateModelAccess == QQmlDelegateModel::ReadOnly)
                        cacheItem->initProxy();
                    else
                        ctxt = cacheItem->initProxy();
                }

                cp->incubateObject(
                        cacheItem->incubationTask(), cacheItem->delegate(), m_context->engine(),
                        ctxt, QQmlContextData::get(m_context));
            }
        }

        if (index == m_compositor.count(group) - 1)
            requestMoreIfNecessary();


        if (cacheItem->object()) {
            QQDMIncubationTask *incubationTask = cacheItem->incubationTask();
            if (!incubationTask || isDoneIncubating(incubationTask->status()))
                return cacheItem->referenceObjectWeak();
        }
    }

    if (!cacheItem->isScriptReferenced()) {

        // If it had an object and no incubationTask we would have returned above.
        // If it had an incubationTask it would be referenced, no matter if it has an object.
        Q_ASSERT(!cacheItem->object());

        removeCacheItem(cacheItem);
        delete cacheItem;
    }

    return nullptr;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1180, as _ZN24QQmlDelegateModelPrivate15removeCacheItemEP21QQmlDelegateModelItem
inline void QQmlDelegateModelPrivate::removeCacheItem(QQmlDelegateModelItem *cacheItem)
{
    int cidx = m_cache.lastIndexOf(cacheItem);
    if (cidx >= 0) {
        m_compositor.clearFlags(Compositor::Cache, cidx, 1, Compositor::CacheFlag);
        m_cache.removeAt(cidx);
    }
    Q_ASSERT(m_cache.size() == m_compositor.count(Compositor::Cache));
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3006, as _ZN29QQmlDelegateModelGroupPrivate17destroyingPackageEP13QQuickPackage
inline void QQmlDelegateModelGroupPrivate::destroyingPackage(QQuickPackage *package)
{
    for (GroupEmitterListIt it = emitters.begin(), end = emitters.end(); it != end; ++it)
        it->destroyingPackage(package);
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 28, as _Z27lcItemViewDelegateRecyclingv
inline const QLoggingCategory &lcItemViewDelegateRecycling()
{
    static const QLoggingCategory category("qt.qml.delegatemodel.recycling");
    return category;
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3734, as _ZN14QQmlPartsModelD1Ev
inline QQmlPartsModel::~QQmlPartsModel()
{
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3738, as _ZNK14QQmlPartsModel11filterGroupEv
inline QString QQmlPartsModel::filterGroup() const
{
    if (m_inheritGroup)
        return m_model->filterGroup();
    return m_filterGroup;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3770, as _ZN14QQmlPartsModel17updateFilterGroupEv
inline void QQmlPartsModel::updateFilterGroup()
{
    QQmlDelegateModelPrivate *model = QQmlDelegateModelPrivate::get(m_model);
    if (!model->m_cacheMetaType)
        return;

    if (m_inheritGroup) {
        if (m_filterGroup == model->m_filterGroup)
            return;
        m_filterGroup = model->m_filterGroup;
    }

    QQmlListCompositor::Group previousGroup = m_compositorGroup;
    m_compositorGroup = Compositor::Default;
    QQmlDelegateModelGroupPrivate::get(model->m_groups[Compositor::Default])->emitters.insert(this);
    for (int i = 1; i < model->m_groupCount; ++i) {
        if (m_filterGroup == model->m_cacheMetaType->groupNames.at(i - 1)) {
            m_compositorGroup = Compositor::Group(i);
            break;
        }
    }

    QQmlDelegateModelGroupPrivate::get(model->m_groups[m_compositorGroup])->emitters.insert(this);
    if (m_compositorGroup != previousGroup) {
        QList<QQmlChangeSet::Change> removes;
        QList<QQmlChangeSet::Change> inserts;
        model->m_compositor.transition(previousGroup, m_compositorGroup, &removes, &inserts);

        QQmlChangeSet changeSet;
        changeSet.move(removes, inserts);
        if (!changeSet.isEmpty())
            emit modelUpdated(changeSet, false);

        if (changeSet.difference() != 0)
            emit countChanged();
    }
}
//  -----------------------------------------------------------------------

//  A QQmlPartsModel that Python can take functions over in. Every QQmlPartsModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlPartsModelCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef bool (*CuteQQmlPartsModelCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void * (*CuteQQmlPartsModelCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlPartsModelCall3)(const void *, QObject *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef const QVariant * (*CuteQQmlPartsModelCall4)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlPartsModelCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef int (*CuteQQmlPartsModelCall6)(const void *, QObject *, QObject *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlPartsModelCall7)(const void *, const QQmlChangeSet *, bool, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlPartsModelCall8)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlPartsModelCall9)(const void *, int, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQmlPartsModelCall10)(const void *, QQuickPackage *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQmlPartsModelCall11)(const void *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void (*CuteQQmlPartsModelCall12)(const void *, int, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef int (*CuteQQmlPartsModelCall13)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef void * (*CuteQQmlPartsModelCall14)(const void *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
typedef bool (*CuteQQmlPartsModelCall15)(const void *, int, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlPartsModelCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlPartsModelCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPartsModelCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPartsModelCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPartsModelCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPartsModelCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPartsModelCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlPartsModel : public QQmlPartsModel {
public:
  using QQmlPartsModel::QQmlPartsModel;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel5countEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6objectEiN13QQmlIncubator14IncubationModeE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel7releaseEP7QObjectNS_12ReusableFlagE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel12variantValueEiRK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel16incubationStatusEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel7indexOfEP7QObjectS1_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter16emitModelUpdatedERK13QQmlChangeSetb")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter14createdPackageEiP13QQuickPackage")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter11initPackageEiP13QQuickPackage")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN29QQmlDelegateModelGroupEmitter17destroyingPackageEP13QQuickPackage")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel6cancelEi")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel22drainReusableItemsPoolEi")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel8poolSizeEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZNK17QQmlInstanceModel17abstractItemModelEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_object_model)
    if (!std::strcmp(key, "_ZN17QQmlInstanceModel19setRequiredPropertyEiRK7QStringRK8QVariant")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_object_model)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  int QQmlPartsModel::count() const
  int count() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPartsModelCall0 call = reinterpret_cast<CuteQQmlPartsModelCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlPartsModel::count();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  bool QQmlPartsModel::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlPartsModelCall1 call = reinterpret_cast<CuteQQmlPartsModelCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlPartsModel::isValid();
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QObject *QQmlPartsModel::object(int index,
  //      QQmlIncubator::IncubationMode incubationMode)
  QObject *object(
      int index,
      QQmlIncubator::IncubationMode incubationMode) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlPartsModelCall2 call = reinterpret_cast<CuteQQmlPartsModelCall2>(taken[2]);
      void * given = call(this, index, static_cast<int>(incubationMode), &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QQmlPartsModel::object(index, incubationMode);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  ReleaseFlags QQmlPartsModel::release(QObject *item, ReusableFlag
  //      reusable)
  QQmlInstanceModel::ReleaseFlags release(
      QObject *item,
      QQmlInstanceModel::ReusableFlag reusable) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlPartsModelCall3 call = reinterpret_cast<CuteQQmlPartsModelCall3>(taken[3]);
      int given = call(this, item, static_cast<int>(reusable), &handled);
      if (handled) return QFlags<QQmlInstanceModel::ReleaseFlag>::fromInt(given);
    }
    return QQmlPartsModel::release(item, reusable);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QVariant QQmlPartsModel::variantValue(int index, const QString &role)
  QVariant variantValue(int index, const QString &role) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlPartsModelCall4 call = reinterpret_cast<CuteQQmlPartsModelCall4>(taken[4]);
      const QVariant * given = call(this, index, &role, &handled);
      if (handled && given) return *given;
    }
    return QQmlPartsModel::variantValue(index, role);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  QQmlIncubator::Status QQmlPartsModel::incubationStatus(int index)
  QQmlIncubator::Status incubationStatus(int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlPartsModelCall5 call = reinterpret_cast<CuteQQmlPartsModelCall5>(taken[5]);
      int given = call(this, index, &handled);
      if (handled) return static_cast<QQmlIncubator::Status>(given);
    }
    return QQmlPartsModel::incubationStatus(index);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
#if QT_CONFIG(qml_delegate_model)
  //  int QQmlPartsModel::indexOf(QObject *item, QObject *objectContext)
  //      const
  int indexOf(QObject *item, QObject *objectContext) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlPartsModelCall6 call = reinterpret_cast<CuteQQmlPartsModelCall6>(taken[6]);
      int given = call(this, item, objectContext, &handled);
      if (handled) return given;
    }
    return QQmlPartsModel::indexOf(item, objectContext);
  }
#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlPartsModel::emitModelUpdated(const QQmlChangeSet &changeSet,
  //      bool reset)
  void emitModelUpdated(
      const QQmlChangeSet &changeSet,
      bool reset) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlPartsModelCall7 call = reinterpret_cast<CuteQQmlPartsModelCall7>(taken[7]);
      call(this, &changeSet, reset, &handled);
      if (handled) return;
    }
    QQmlPartsModel::emitModelUpdated(changeSet, reset);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlPartsModel::createdPackage(int index, QQuickPackage
  //      *package)
  void createdPackage(int index, QQuickPackage *package) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlPartsModelCall8 call = reinterpret_cast<CuteQQmlPartsModelCall8>(taken[8]);
      call(this, index, package, &handled);
      if (handled) return;
    }
    QQmlPartsModel::createdPackage(index, package);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlPartsModel::initPackage(int index, QQuickPackage *package)
  void initPackage(int index, QQuickPackage *package) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlPartsModelCall9 call = reinterpret_cast<CuteQQmlPartsModelCall9>(taken[9]);
      call(this, index, package, &handled);
      if (handled) return;
    }
    QQmlPartsModel::initPackage(index, package);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQmlPartsModel::destroyingPackage(QQuickPackage *package)
  void destroyingPackage(QQuickPackage *package) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlPartsModelCall10 call = reinterpret_cast<CuteQQmlPartsModelCall10>(taken[10]);
      call(this, package, &handled);
      if (handled) return;
    }
    QQmlPartsModel::destroyingPackage(package);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_object_model)
  //  void QQmlInstanceModel::cancel(int a0)
  void cancel(int a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlPartsModelCall11 call = reinterpret_cast<CuteQQmlPartsModelCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlInstanceModel::cancel(a0);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  void QQmlInstanceModel::drainReusableItemsPool(int maxPoolTime)
  void drainReusableItemsPool(int maxPoolTime) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlPartsModelCall12 call = reinterpret_cast<CuteQQmlPartsModelCall12>(taken[12]);
      call(this, maxPoolTime, &handled);
      if (handled) return;
    }
    QQmlInstanceModel::drainReusableItemsPool(maxPoolTime);
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  int QQmlInstanceModel::poolSize()
  int poolSize() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlPartsModelCall13 call = reinterpret_cast<CuteQQmlPartsModelCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlInstanceModel::poolSize();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  const QAbstractItemModel *QQmlInstanceModel::abstractItemModel()
  //      const
  const QAbstractItemModel *abstractItemModel() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlPartsModelCall14 call = reinterpret_cast<CuteQQmlPartsModelCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractItemModel *>(given);
    }
    return QQmlInstanceModel::abstractItemModel();
  }
#endif  // QT_CONFIG(qml_object_model)

#if QT_CONFIG(qml_object_model)
  //  bool QQmlInstanceModel::setRequiredProperty(int index, const QString
  //      &name, const QVariant &value)
  bool setRequiredProperty(
      int index,
      const QString &name,
      const QVariant &value) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlPartsModelCall15 call = reinterpret_cast<CuteQQmlPartsModelCall15>(taken[15]);
      bool given = call(this, index, &name, &value, &handled);
      if (handled) return given;
    }
    return QQmlInstanceModel::setRequiredProperty(index, name, value);
  }
#endif  // QT_CONFIG(qml_object_model)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlPartsModelCall16 call = reinterpret_cast<CuteQQmlPartsModelCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlPartsModelCall17 call = reinterpret_cast<CuteQQmlPartsModelCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlPartsModelCall18 call = reinterpret_cast<CuteQQmlPartsModelCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlPartsModelCall19 call = reinterpret_cast<CuteQQmlPartsModelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlPartsModelCall20 call = reinterpret_cast<CuteQQmlPartsModelCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlPartsModelCall21 call = reinterpret_cast<CuteQQmlPartsModelCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlPartsModelCall22 call = reinterpret_cast<CuteQQmlPartsModelCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlPartsModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlPartsModel10metaObjectEv(
    const QQmlPartsModel *self) {
  return self->metaObject();
}

//  void *QQmlPartsModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQmlPartsModel11qt_metacastEPKc(
    QQmlPartsModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlPartsModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQmlPartsModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlPartsModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQmlPartsModel::~QQmlPartsModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModelD1Ev(QQmlPartsModel *self) {
  delete self;
}

//  QString QQmlPartsModel::filterGroup() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlPartsModel11filterGroupEv(
    const QQmlPartsModel *self) {
  return new QString(self->filterGroup());
}

//  void QQmlPartsModel::updateFilterGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel17updateFilterGroupEv(QQmlPartsModel *self) {
  self->updateFilterGroup();
}

//  int QQmlPartsModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlPartsModel5countEv(const QQmlPartsModel *self) {
  return self->count();
}

//  bool QQmlPartsModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlPartsModel7isValidEv(const QQmlPartsModel *self) {
  return self->isValid();
}

//  QObject *QQmlPartsModel::object(int index, QQmlIncubator::IncubationMode
//      incubationMode)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QQmlPartsModel6objectEiN13QQmlIncubator14IncubationModeE(
    QQmlPartsModel *self,
    int index,
    QQmlIncubator::IncubationMode incubationMode) {
  return self->object(index, incubationMode);
}

//  ReleaseFlags QQmlPartsModel::release(QObject *item, ReusableFlag
//      reusable)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQmlPartsModel7releaseEP7QObjectN17QQmlInstanceModel12ReusableFlagE(
    QQmlPartsModel *self,
    QObject *item,
    QQmlInstanceModel::ReusableFlag reusable) {
  return static_cast<int>(self->release(item, reusable).toInt());
}

//  QVariant QQmlPartsModel::variantValue(int index, const QString &role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QQmlPartsModel12variantValueEiRK7QString(
    QQmlPartsModel *self,
    int index,
    const QString *role) {
  return new QVariant(self->variantValue(index, *role));
}

//  QList<QByteArray> QQmlPartsModel::watchedRoles() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK14QQmlPartsModel12watchedRolesEv(
    const QQmlPartsModel *self) {
  return new QList<QByteArray>(self->watchedRoles());
}

//  void QQmlPartsModel::setWatchedRoles(const QList<QByteArray> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel15setWatchedRolesERK5QListI10QByteArrayE(
    QQmlPartsModel *self,
    const QList<QByteArray> *roles) {
  self->setWatchedRoles(*roles);
}

//  QQmlIncubator::Status QQmlPartsModel::incubationStatus(int index)
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZN14QQmlPartsModel16incubationStatusEi(
    QQmlPartsModel *self,
    int index) {
  return self->incubationStatus(index);
}

//  int QQmlPartsModel::indexOf(QObject *item, QObject *objectContext) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlPartsModel7indexOfEP7QObjectS1_(
    const QQmlPartsModel *self,
    QObject *item,
    QObject *objectContext) {
  return self->indexOf(item, objectContext);
}

//  void QQmlPartsModel::emitModelUpdated(const QQmlChangeSet &changeSet,
//      bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel16emitModelUpdatedERK13QQmlChangeSetb(
    QQmlPartsModel *self,
    const QQmlChangeSet *changeSet,
    bool reset) {
  self->emitModelUpdated(*changeSet, reset);
}

//  void QQmlPartsModel::createdPackage(int index, QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel14createdPackageEiP13QQuickPackage(
    QQmlPartsModel *self,
    int index,
    QQuickPackage *package) {
  self->createdPackage(index, package);
}

//  void QQmlPartsModel::initPackage(int index, QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel11initPackageEiP13QQuickPackage(
    QQmlPartsModel *self,
    int index,
    QQuickPackage *package) {
  self->initPackage(index, package);
}

//  void QQmlPartsModel::destroyingPackage(QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel17destroyingPackageEP13QQuickPackage(
    QQmlPartsModel *self,
    QQuickPackage *package) {
  self->destroyingPackage(package);
}

//  void QQmlPartsModel::filterGroupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlPartsModel18filterGroupChangedEv(QQmlPartsModel *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlPartsModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filterGroupChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filterGroupChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQmlPartsModel as the QQmlDelegateModelGroupEmitter it is built on
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroupEmitter *ritual_cast_QQmlPartsModel_QQmlDelegateModelGroupEmitter(
    QQmlPartsModel *self) {
  return static_cast<QQmlDelegateModelGroupEmitter *>(self);
}

//  a Python function taken by a CuteQQmlPartsModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPartsModel(
    QQmlPartsModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPartsModel *>(self)->take(key, call);
}

//  int QQmlPartsModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQmlPartsModel5countEv(const QQmlPartsModel *self) {
  return self->QQmlPartsModel::count();
}

//  bool QQmlPartsModel::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQmlPartsModel7isValidEv(const QQmlPartsModel *self) {
  return self->QQmlPartsModel::isValid();
}

//  int QQmlPartsModel::indexOf(QObject *item, QObject *objectContext) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQmlPartsModel7indexOfEP7QObjectS1_(
    const QQmlPartsModel *self,
    QObject *item,
    QObject *objectContext) {
  return self->QQmlPartsModel::indexOf(item, objectContext);
}

//  void QQmlPartsModel::createdPackage(int index, QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlPartsModel14createdPackageEiP13QQuickPackage(
    QQmlPartsModel *self,
    int index,
    QQuickPackage *package) {
  self->QQmlPartsModel::createdPackage(index, package);
}

//  void QQmlPartsModel::initPackage(int index, QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlPartsModel11initPackageEiP13QQuickPackage(
    QQmlPartsModel *self,
    int index,
    QQuickPackage *package) {
  self->QQmlPartsModel::initPackage(index, package);
}

//  void QQmlPartsModel::destroyingPackage(QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlPartsModel17destroyingPackageEP13QQuickPackage(
    QQmlPartsModel *self,
    QQuickPackage *package) {
  self->QQmlPartsModel::destroyingPackage(package);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
