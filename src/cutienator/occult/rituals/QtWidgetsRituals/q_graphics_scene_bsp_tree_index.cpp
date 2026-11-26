//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenebsptreeindex_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qglobal.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <QtWidgets/private/qgraphicsscene_bsp_p.h>
#include <QtCore/qstring.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 55, as local:qgraphicsscenebsptreeindex.cpp:intmaxlog
static inline int intmaxlog(int n)
{
    return  (n > 0 ? qMax(qCeil(qLn(qreal(n)) / qLn(qreal(2))), 5) : 0);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 561, as _ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem
inline void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
{
    removeItem(item);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 327, as _ZN19QGraphicsSceneIndexC2ER26QGraphicsSceneIndexPrivateP14QGraphicsScene
inline QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsSceneIndexPrivate &dd, QGraphicsScene *scene)
    : QObject(dd, scene)
{
    d_func()->init();
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 336, as _ZN19QGraphicsSceneIndexD2Ev
inline QGraphicsSceneIndex::~QGraphicsSceneIndex()
{

}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 599, as _ZN26QGraphicsSceneBspTreeIndex10itemChangeEPK13QGraphicsItemNS0_18GraphicsItemChangeEPKv
inline void QGraphicsSceneBspTreeIndex::itemChange(const QGraphicsItem *item, QGraphicsItem::GraphicsItemChange change, const void *const value)
{
    Q_D(QGraphicsSceneBspTreeIndex);
    switch (change) {
    case QGraphicsItem::ItemFlagsChange: {
        // Handle ItemIgnoresTransformations
        QGraphicsItem::GraphicsItemFlags newFlags = *static_cast<const QGraphicsItem::GraphicsItemFlags *>(value);
        bool ignoredTransform = item->d_ptr->flags & QGraphicsItem::ItemIgnoresTransformations;
        bool willIgnoreTransform = newFlags & QGraphicsItem::ItemIgnoresTransformations;
        bool clipsChildren = item->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape
                             || item->d_ptr->flags & QGraphicsItem::ItemContainsChildrenInShape;
        bool willClipChildren = newFlags & QGraphicsItem::ItemClipsChildrenToShape
                                || newFlags & QGraphicsItem::ItemContainsChildrenInShape;
        if ((ignoredTransform != willIgnoreTransform) || (clipsChildren != willClipChildren)) {
            QGraphicsItem *thatItem = const_cast<QGraphicsItem *>(item);
            // Remove item and its descendants from the index and append
            // them to the list of unindexed items. Then, when the index
            // is updated, they will be put into the bsp-tree or the list
            // of untransformable items.
            d->removeItem(thatItem, /*recursive=*/true, /*moveToUnidexedItems=*/true);
        }
        break;
    }
    case QGraphicsItem::ItemZValueChange:
        d->invalidateSortCache();
        break;
    case QGraphicsItem::ItemParentChange: {
        d->invalidateSortCache();
        // Handle ItemIgnoresTransformations
        const QGraphicsItem *newParent = static_cast<const QGraphicsItem *>(value);
        bool ignoredTransform = item->d_ptr->itemIsUntransformable();
        bool willIgnoreTransform = (item->d_ptr->flags & QGraphicsItem::ItemIgnoresTransformations)
                                   || (newParent && newParent->d_ptr->itemIsUntransformable());
        bool ancestorClippedChildren = item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorClipsChildren
                                       || item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorContainsChildren;
        bool ancestorWillClipChildren = newParent
                            && ((newParent->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape
                                 || newParent->d_ptr->flags & QGraphicsItem::ItemContainsChildrenInShape)
                                || (newParent->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorClipsChildren
                                    || newParent->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorContainsChildren));
        if ((ignoredTransform != willIgnoreTransform) || (ancestorClippedChildren != ancestorWillClipChildren)) {
            QGraphicsItem *thatItem = const_cast<QGraphicsItem *>(item);
            // Remove item and its descendants from the index and append
            // them to the list of unindexed items. Then, when the index
            // is updated, they will be put into the bsp-tree or the list
            // of untransformable items.
            d->removeItem(thatItem, /*recursive=*/true, /*moveToUnidexedItems=*/true);
        }
        break;
    }
    default:
        break;
    }
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 465, as _ZN26QGraphicsSceneBspTreeIndex10removeItemEP13QGraphicsItem
inline void QGraphicsSceneBspTreeIndex::removeItem(QGraphicsItem *item)
{
    Q_D(QGraphicsSceneBspTreeIndex);
    d->removeItem(item);
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 189, as _ZN33QGraphicsSceneBspTreeIndexPrivate10resetIndexEv
inline void QGraphicsSceneBspTreeIndexPrivate::resetIndex()
{
    purgeRemovedItems();
    for (int i = 0; i < indexedItems.size(); ++i) {
        if (QGraphicsItem *item = indexedItems.at(i)) {
            item->d_ptr->index = -1;
            Q_ASSERT(!item->d_ptr->itemDiscovered);
            unindexedItems << item;
        }
    }
    indexedItems.clear();
    freeItemIndexes.clear();
    untransformableItems.clear();
    regenerateIndex = true;
    startIndexTimer();
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 586, as _ZN26QGraphicsSceneBspTreeIndex15updateSceneRectERK6QRectF
inline void QGraphicsSceneBspTreeIndex::updateSceneRect(const QRectF &rect)
{
    Q_D(QGraphicsSceneBspTreeIndex);
    d->sceneRect = rect;
    d->resetIndex();
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 660, as _ZN26QGraphicsSceneBspTreeIndex5eventEP6QEvent
inline bool QGraphicsSceneBspTreeIndex::event(QEvent *event)
{
    Q_D(QGraphicsSceneBspTreeIndex);
    if (event->type() == QEvent::Timer) {
            if (d->indexTimer.isActive() && static_cast<QTimerEvent *>(event)->id() == d->indexTimer.id()) {
                if (d->restartIndexTimer) {
                    d->restartIndexTimer = false;
                } else {
                    // this call will kill the timer
                    d->_q_updateIndex();
                }
            }
    }
    return QObject::event(event);
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 434, as _ZN26QGraphicsSceneBspTreeIndex5clearEv
inline void QGraphicsSceneBspTreeIndex::clear()
{
    Q_D(QGraphicsSceneBspTreeIndex);
    d->bsp.clear();
    d->lastItemCount = 0;
    d->freeItemIndexes.clear();
    for (int i = 0; i < d->indexedItems.size(); ++i) {
        // Ensure item bits are reset properly.
        if (QGraphicsItem *item = d->indexedItems.at(i)) {
            Q_ASSERT(!item->d_ptr->itemDiscovered);
            item->d_ptr->index = -1;
        }
    }
    d->indexedItems.clear();
    d->unindexedItems.clear();
    d->untransformableItems.clear();
    d->regenerateIndex = true;
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 456, as _ZN26QGraphicsSceneBspTreeIndex7addItemEP13QGraphicsItem
inline void QGraphicsSceneBspTreeIndex::addItem(QGraphicsItem *item)
{
    Q_D(QGraphicsSceneBspTreeIndex);
    d->addItem(item);
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 475, as _ZN26QGraphicsSceneBspTreeIndex25prepareBoundingRectChangeEPK13QGraphicsItem
inline void QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(const QGraphicsItem *item)
{
    if (!item)
        return;

    if (item->d_ptr->index == -1 || item->d_ptr->itemIsUntransformable()
        || (item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorClipsChildren
            || item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorContainsChildren)) {
        return; // Item is not in BSP tree; nothing to do.
    }

    Q_D(QGraphicsSceneBspTreeIndex);
    QGraphicsItem *thatItem = const_cast<QGraphicsItem *>(item);
    d->removeItem(thatItem, /*recursive=*/false, /*moveToUnindexedItems=*/true);
    for (int i = 0; i < item->d_ptr->children.size(); ++i)  // ### Do we really need this?
        prepareBoundingRectChange(item->d_ptr->children.at(i));
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 154, as _ZN33QGraphicsSceneBspTreeIndexPrivate17purgeRemovedItemsEv
inline void QGraphicsSceneBspTreeIndexPrivate::purgeRemovedItems()
{
    if (!purgePending && removedItems.isEmpty())
        return;

    // Remove stale items from the BSP tree.
    bsp.removeItems(removedItems);
    // Purge this list.
    removedItems.clear();
    freeItemIndexes.clear();
    for (int i = 0; i < indexedItems.size(); ++i) {
        if (!indexedItems.at(i))
            freeItemIndexes << i;
    }
    purgePending = false;
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 34, as _ZN21QGraphicsSceneBspTree5clearEv
inline void QGraphicsSceneBspTree::clear()
{
    leafCnt = 0;
    nodes.clear();
    leaves.clear();
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 270, as _ZN33QGraphicsSceneBspTreeIndexPrivate7addItemEP13QGraphicsItemb
inline void QGraphicsSceneBspTreeIndexPrivate::addItem(QGraphicsItem *item, bool recursive)
{
    if (!item)
        return;

    // Prevent reusing a recently deleted pointer: purge all removed item from our lists.
    purgeRemovedItems();

    // Invalidate any sort caching; arrival of a new item means we need to resort.
    // Update the scene's sort cache settings.
    item->d_ptr->globalStackingOrder = -1;
    invalidateSortCache();

    // Indexing requires sceneBoundingRect(), but because \a item might
    // not be completely constructed at this point, we need to store it in
    // a temporary list and schedule an indexing for later.
    if (item->d_ptr->index == -1) {
        Q_ASSERT(!unindexedItems.contains(item));
        unindexedItems << item;
        startIndexTimer(0);
    } else {
        Q_ASSERT(indexedItems.contains(item));
        qWarning("QGraphicsSceneBspTreeIndex::addItem: item has already been added to this BSP");
    }

    if (recursive) {
        for (int i = 0; i < item->d_ptr->children.size(); ++i)
            addItem(item->d_ptr->children.at(i), recursive);
    }
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 301, as _ZN33QGraphicsSceneBspTreeIndexPrivate10removeItemEP13QGraphicsItembb
inline void QGraphicsSceneBspTreeIndexPrivate::removeItem(QGraphicsItem *item, bool recursive,
                                                   bool moveToUnindexedItems)
{
    if (!item)
        return;

    if (item->d_ptr->index != -1) {
        Q_ASSERT(item->d_ptr->index < indexedItems.size());
        Q_ASSERT(indexedItems.at(item->d_ptr->index) == item);
        Q_ASSERT(!item->d_ptr->itemDiscovered);
        freeItemIndexes << item->d_ptr->index;
        indexedItems[item->d_ptr->index] = 0;
        item->d_ptr->index = -1;

        if (item->d_ptr->itemIsUntransformable()) {
            untransformableItems.removeOne(item);
        } else if (item->d_ptr->inDestructor) {
            // Avoid virtual function calls from the destructor.
            purgePending = true;
            removedItems << item;
        } else if (!(item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorClipsChildren
                     || item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorContainsChildren)) {
            bsp.removeItem(item, item->d_ptr->sceneEffectiveBoundingRect());
        }
    } else {
        unindexedItems.removeOne(item);
    }
    invalidateSortCache(); // ### Only do this when removing from BSP?

    Q_ASSERT(item->d_ptr->index == -1);
    Q_ASSERT(!indexedItems.contains(item));
    Q_ASSERT(!unindexedItems.contains(item));
    Q_ASSERT(!untransformableItems.contains(item));

    if (moveToUnindexedItems)
        addItem(item);

    if (recursive) {
        for (int i = 0; i < item->d_ptr->children.size(); ++i)
            removeItem(item->d_ptr->children.at(i), recursive, moveToUnindexedItems);
    }
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 55, as _ZN21QGraphicsSceneBspTree11removeItemsERK4QSetIP13QGraphicsItemE
inline void QGraphicsSceneBspTree::removeItems(const QSet<QGraphicsItem *> &items)
{
    for (int i = 0; i < leaves.size(); ++i) {
        QList<QGraphicsItem *> newItemList;
        const QList<QGraphicsItem *> &oldItemList = leaves[i];
        for (int j = 0; j < oldItemList.size(); ++j) {
            QGraphicsItem *item = oldItemList.at(j);
            if (!items.contains(item))
                newItemList << item;
        }
        leaves[i] = newItemList;
    }
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 48, as _ZN21QGraphicsSceneBspTree10removeItemEP13QGraphicsItemRK6QRectF
inline void QGraphicsSceneBspTree::removeItem(QGraphicsItem *item, const QRectF &rect)
{
    climbTree([item](QList<QGraphicsItem *> *items){
        items->removeAll(item);
    }, rect);
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 418, as _ZN26QGraphicsSceneBspTreeIndexD1Ev
inline QGraphicsSceneBspTreeIndex::~QGraphicsSceneBspTreeIndex()
{
    Q_D(QGraphicsSceneBspTreeIndex);
    for (int i = 0; i < d->indexedItems.size(); ++i) {
        // Ensure item bits are reset properly.
        if (QGraphicsItem *item = d->indexedItems.at(i)) {
            Q_ASSERT(!item->d_ptr->itemDiscovered);
            item->d_ptr->index = -1;
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 565, as _ZNK26QGraphicsSceneBspTreeIndex12bspTreeDepthEv
inline int QGraphicsSceneBspTreeIndex::bspTreeDepth() const
{
    Q_D(const QGraphicsSceneBspTreeIndex);
    return d->bspTreeDepth;
}
//  -----------------------------------------------------------------------

//  Only a class built on QGraphicsSceneBspTreeIndex may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsSceneBspTreeIndex : QGraphicsSceneBspTreeIndex {
  using QGraphicsSceneBspTreeIndex::clear;
};

//  A QGraphicsSceneBspTreeIndex that Python can take functions over in. Every QGraphicsSceneBspTreeIndex
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsSceneBspTreeIndexCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall3)(const void *, QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall4)(const void *, QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall5)(const void *, const QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall6)(const void *, QGraphicsItem *, int *);
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsSceneBspTreeIndexCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsSceneBspTreeIndexCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsSceneBspTreeIndex : public QGraphicsSceneBspTreeIndex {
public:
  using QGraphicsSceneBspTreeIndex::QGraphicsSceneBspTreeIndex;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex15updateSceneRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex5clearEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex7addItemEP13QGraphicsItem")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex10removeItemEP13QGraphicsItem")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex25prepareBoundingRectChangeEPK13QGraphicsItem")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN19QGraphicsSceneIndex10deleteItemEP13QGraphicsItem")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneBspTreeIndex::updateSceneRect(const QRectF &rect)
  void updateSceneRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall0 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsSceneBspTreeIndex::updateSceneRect(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(graphicsview)
  //  bool QGraphicsSceneBspTreeIndex::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall1 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsSceneBspTreeIndex::event(event);
  }
#endif  // QT_CONFIG(graphicsview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneBspTreeIndex::clear()
  void clear() override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall2 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsSceneBspTreeIndex::clear();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneBspTreeIndex::addItem(QGraphicsItem *item)
  void addItem(QGraphicsItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall3 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneBspTreeIndex::addItem(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneBspTreeIndex::removeItem(QGraphicsItem *item)
  void removeItem(QGraphicsItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall4 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneBspTreeIndex::removeItem(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(const
  //      QGraphicsItem *item)
  void prepareBoundingRectChange(const QGraphicsItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall5 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsSceneIndex::deleteItem(QGraphicsItem *item)
  void deleteItem(QGraphicsItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall6 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QGraphicsSceneIndex::deleteItem(item);
  }
#endif  // QT_CONFIG(graphicsview)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall7 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall8 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall9 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall10 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall11 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsSceneBspTreeIndexCall12 call = reinterpret_cast<CuteQGraphicsSceneBspTreeIndexCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsSceneBspTreeIndex::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QGraphicsSceneBspTreeIndex10metaObjectEv(
    const QGraphicsSceneBspTreeIndex *self) {
  return self->metaObject();
}

//  void *QGraphicsSceneBspTreeIndex::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QGraphicsSceneBspTreeIndex11qt_metacastEPKc(
    QGraphicsSceneBspTreeIndex *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphicsSceneBspTreeIndex::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QGraphicsSceneBspTreeIndex11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphicsSceneBspTreeIndex *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QGraphicsSceneBspTreeIndex::~QGraphicsSceneBspTreeIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndexD1Ev(
    QGraphicsSceneBspTreeIndex *self) {
  delete self;
}

//  QList<QGraphicsItem *> QGraphicsSceneBspTreeIndex::estimateItems(const
//      QRectF &rect, Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK26QGraphicsSceneBspTreeIndex13estimateItemsERK6QRectFN2Qt9SortOrderE(
    const QGraphicsSceneBspTreeIndex *self,
    const QRectF *rect,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->estimateItems(*rect, order));
}

//  QList<QGraphicsItem *>
//      QGraphicsSceneBspTreeIndex::estimateTopLevelItems(const QRectF &rect,
//      Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK26QGraphicsSceneBspTreeIndex21estimateTopLevelItemsERK6QRectFN2Qt9SortOrderE(
    const QGraphicsSceneBspTreeIndex *self,
    const QRectF *rect,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(
      self->estimateTopLevelItems(
          *rect,
          order));
}

//  QList<QGraphicsItem *> QGraphicsSceneBspTreeIndex::items(Qt::SortOrder
//      order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK26QGraphicsSceneBspTreeIndex5itemsEN2Qt9SortOrderE(
    const QGraphicsSceneBspTreeIndex *self,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->items(order));
}

//  int QGraphicsSceneBspTreeIndex::bspTreeDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QGraphicsSceneBspTreeIndex12bspTreeDepthEv(
    const QGraphicsSceneBspTreeIndex *self) {
  return self->bspTreeDepth();
}

//  void QGraphicsSceneBspTreeIndex::updateSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex15updateSceneRectERK6QRectF(
    QGraphicsSceneBspTreeIndex *self,
    const QRectF *rect) {
  self->updateSceneRect(*rect);
}

//  bool QGraphicsSceneBspTreeIndex::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QGraphicsSceneBspTreeIndex5eventEP6QEvent(
    QGraphicsSceneBspTreeIndex *self,
    QEvent *event) {
  return self->event(event);
}

//  void QGraphicsSceneBspTreeIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex5clearEv(
    QGraphicsSceneBspTreeIndex *self) {
  self->clear();
}

//  void QGraphicsSceneBspTreeIndex::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex7addItemEP13QGraphicsItem(
    QGraphicsSceneBspTreeIndex *self,
    QGraphicsItem *item) {
  self->addItem(item);
}

//  void QGraphicsSceneBspTreeIndex::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex10removeItemEP13QGraphicsItem(
    QGraphicsSceneBspTreeIndex *self,
    QGraphicsItem *item) {
  self->removeItem(item);
}

//  void QGraphicsSceneBspTreeIndex::prepareBoundingRectChange(const
//      QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex25prepareBoundingRectChangeEPK13QGraphicsItem(
    QGraphicsSceneBspTreeIndex *self,
    const QGraphicsItem *item) {
  self->prepareBoundingRectChange(item);
}

//  void QGraphicsSceneBspTreeIndex::itemChange(const QGraphicsItem *item,
//      QGraphicsItem::GraphicsItemChange change, const void *const value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneBspTreeIndex10itemChangeEPK13QGraphicsItemNS0_18GraphicsItemChangeEPKv(
    QGraphicsSceneBspTreeIndex *self,
    const QGraphicsItem *item,
    QGraphicsItem::GraphicsItemChange change,
    const void *const value) {
  self->itemChange(item, change, value);
}

//  QGraphicsSceneBspTreeIndexPrivate *QGraphicsSceneBspTreeIndex::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneBspTreeIndexPrivate *ritual_ZN26QGraphicsSceneBspTreeIndex6d_funcEv(
    QGraphicsSceneBspTreeIndex *self) {
  return self->d_func();
}

//  const QGraphicsSceneBspTreeIndexPrivate
//      *QGraphicsSceneBspTreeIndex::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneBspTreeIndexPrivate *ritual_ZNK26QGraphicsSceneBspTreeIndex6d_funcEv(
    const QGraphicsSceneBspTreeIndex *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsSceneBspTreeIndex, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneBspTreeIndex(
    QGraphicsSceneBspTreeIndex *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneBspTreeIndex *>(self)->take(key, call);
}

//  void QGraphicsSceneBspTreeIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGraphicsSceneBspTreeIndex5clearEv(
    QGraphicsSceneBspTreeIndex *self) {
  static_cast<OwnQGraphicsSceneBspTreeIndex *>(self)->OwnQGraphicsSceneBspTreeIndex::clear();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
