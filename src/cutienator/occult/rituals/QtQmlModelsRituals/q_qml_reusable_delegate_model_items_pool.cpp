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
#include <functional>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 28, as _Z27lcItemViewDelegateRecyclingv
inline const QLoggingCategory &lcItemViewDelegateRecycling()
{
    static const QLoggingCategory category("qt.qml.delegatemodel.recycling");
    return category;
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
//  -----------------------------------------------------------------------

//  bool QQmlReusableDelegateModelItemsPool::insertItem(QQmlDelegateModelItem
//      *modelItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QQmlReusableDelegateModelItemsPool10insertItemEP21QQmlDelegateModelItem(
    QQmlReusableDelegateModelItemsPool *self,
    QQmlDelegateModelItem *modelItem) {
  return self->insertItem(modelItem);
}

//  QQmlDelegateModelItem *QQmlReusableDelegateModelItemsPool::takeItem(const
//      QQmlComponent *delegate, int newIndexHint)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZN34QQmlReusableDelegateModelItemsPool8takeItemEPK13QQmlComponenti(
    QQmlReusableDelegateModelItemsPool *self,
    const QQmlComponent *delegate,
    int newIndexHint) {
  return self->takeItem(delegate, newIndexHint);
}

//  void QQmlReusableDelegateModelItemsPool::drain(int maxPoolTime,
//      std::function<void (QQmlDelegateModelItem *)> releaseItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQmlReusableDelegateModelItemsPool5drainEiSt8functionIFvP21QQmlDelegateModelItemEE(
    QQmlReusableDelegateModelItemsPool *self,
    int maxPoolTime,
    const std::function<void (QQmlDelegateModelItem *)> *releaseItem) {
  self->drain(maxPoolTime, *releaseItem);
}

//  int QQmlReusableDelegateModelItemsPool::size()
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQmlReusableDelegateModelItemsPool4sizeEv(
    QQmlReusableDelegateModelItemsPool *self) {
  return self->size();
}

//  QQmlReusableDelegateModelItemsPool::~QQmlReusableDelegateModelItemsPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQmlReusableDelegateModelItemsPoolD1Ev(
    QQmlReusableDelegateModelItemsPool *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
