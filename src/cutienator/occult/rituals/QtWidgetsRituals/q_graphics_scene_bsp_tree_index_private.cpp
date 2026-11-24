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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicsscene_bsp_p.h>
#include <QtCore/qstring.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 13, as _ZN21QGraphicsSceneBspTreeC1Ev
inline QGraphicsSceneBspTree::QGraphicsSceneBspTree()
    : leafCnt(0)
{
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 18, as _ZN21QGraphicsSceneBspTreeD1Ev
inline QGraphicsSceneBspTree::~QGraphicsSceneBspTree()
{
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 179, as _ZN26QGraphicsSceneIndexPrivateC2EP14QGraphicsScene
inline QGraphicsSceneIndexPrivate::QGraphicsSceneIndexPrivate(QGraphicsScene *scene) : scene(scene)
{
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 186, as _ZN26QGraphicsSceneIndexPrivateD2Ev
inline QGraphicsSceneIndexPrivate::~QGraphicsSceneIndexPrivate()
{
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

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 380, as _ZN33QGraphicsSceneBspTreeIndexPrivate9sortItemsEP5QListIP13QGraphicsItemEN2Qt9SortOrderEbb
inline void QGraphicsSceneBspTreeIndexPrivate::sortItems(QList<QGraphicsItem *> *itemList, Qt::SortOrder order,
                                                  bool sortCacheEnabled, bool onlyTopLevelItems)
{
    if (order == Qt::SortOrder(-1))
        return;

    if (onlyTopLevelItems) {
        if (order == Qt::DescendingOrder)
            std::sort(itemList->begin(), itemList->end(), qt_closestLeaf);
        else if (order == Qt::AscendingOrder)
            std::sort(itemList->begin(), itemList->end(), qt_notclosestLeaf);
        return;
    }

    if (sortCacheEnabled) {
        if (order == Qt::DescendingOrder) {
            std::sort(itemList->begin(), itemList->end(), closestItemFirst_withCache);
        } else if (order == Qt::AscendingOrder) {
            std::sort(itemList->begin(), itemList->end(), closestItemLast_withCache);
        }
    } else {
        if (order == Qt::DescendingOrder) {
            std::sort(itemList->begin(), itemList->end(), qt_closestItemFirst);
        } else if (order == Qt::AscendingOrder) {
            std::sort(itemList->begin(), itemList->end(), qt_closestItemLast);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 490, as _ZNK19QGraphicsSceneIndex21estimateTopLevelItemsERK6QRectFN2Qt9SortOrderE
inline QList<QGraphicsItem *> QGraphicsSceneIndex::estimateTopLevelItems(const QRectF &rect, Qt::SortOrder order) const
{
    Q_D(const QGraphicsSceneIndex);
    Q_UNUSED(rect);
    QGraphicsScenePrivate *scened = d->scene->d_func();
    scened->ensureSortedTopLevelItems();
    if (order == Qt::DescendingOrder) {
        QList<QGraphicsItem *> sorted;
        const int numTopLevelItems = scened->topLevelItems.size();
        sorted.reserve(numTopLevelItems);
        for (int i = numTopLevelItems - 1; i >= 0; --i)
            sorted << scened->topLevelItems.at(i);
        return sorted;
    }
    return scened->topLevelItems;
}

//  from src/widgets/graphicsview/qgraphicsscene_bsp.cpp, line 69, as _ZNK21QGraphicsSceneBspTree5itemsERK6QRectFb
inline QList<QGraphicsItem *> QGraphicsSceneBspTree::items(const QRectF &rect, bool onlyTopLevelItems) const
{
    QList<QGraphicsItem *> foundItems;
    climbTree([&foundItems, onlyTopLevelItems](QList<QGraphicsItem *> *items) {
        for (int i = 0; i < items->size(); ++i) {
            QGraphicsItem *item = items->at(i);
            if (onlyTopLevelItems && item->d_ptr->parent)
                item = item->topLevelItem();
            if (!item->d_func()->itemDiscovered && item->d_ptr->visible) {
                item->d_func()->itemDiscovered = 1;
                foundItems.prepend(item);
            }
        }
    }, rect);
    // Reset discovery bits.
    for (const auto &foundItem : std::as_const(foundItems))
        foundItem->d_ptr->itemDiscovered = 0;
    return foundItems;
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

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 260, as _ZN33QGraphicsSceneBspTreeIndexPrivate19invalidateSortCacheEv
inline void QGraphicsSceneBspTreeIndexPrivate::invalidateSortCache()
{
    Q_Q(QGraphicsSceneBspTreeIndex);
    if (!sortCacheEnabled || updatingSortCache)
        return;

    updatingSortCache = true;
    QMetaObject::invokeMethod(q, "_q_updateSortCache", Qt::QueuedConnection);
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 209, as _ZN33QGraphicsSceneBspTreeIndexPrivate9climbTreeEP13QGraphicsItemPi
inline void QGraphicsSceneBspTreeIndexPrivate::climbTree(QGraphicsItem *item, int *stackingOrder)
{
    if (!item->d_ptr->children.isEmpty()) {
        QList<QGraphicsItem *> childList = item->d_ptr->children;
        std::sort(childList.begin(), childList.end(), qt_closestLeaf);
        for (int i = 0; i < childList.size(); ++i) {
            QGraphicsItem *item = childList.at(i);
            if (!(item->flags() & QGraphicsItem::ItemStacksBehindParent))
                climbTree(childList.at(i), stackingOrder);
        }
        item->d_ptr->globalStackingOrder = (*stackingOrder)++;
        for (int i = 0; i < childList.size(); ++i) {
            QGraphicsItem *item = childList.at(i);
            if (item->flags() & QGraphicsItem::ItemStacksBehindParent)
                climbTree(childList.at(i), stackingOrder);
        }
    } else {
        item->d_ptr->globalStackingOrder = (*stackingOrder)++;
    }
}
//  -----------------------------------------------------------------------

//  QGraphicsSceneBspTreeIndex *QGraphicsSceneBspTreeIndexPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneBspTreeIndex *ritual_ZN33QGraphicsSceneBspTreeIndexPrivate6q_funcEv(
    QGraphicsSceneBspTreeIndexPrivate *self) {
  return self->q_func();
}

//  const QGraphicsSceneBspTreeIndex
//      *QGraphicsSceneBspTreeIndexPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneBspTreeIndex *ritual_ZNK33QGraphicsSceneBspTreeIndexPrivate6q_funcEv(
    const QGraphicsSceneBspTreeIndexPrivate *self) {
  return self->q_func();
}

//  void QGraphicsSceneBspTreeIndexPrivate::purgeRemovedItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QGraphicsSceneBspTreeIndexPrivate17purgeRemovedItemsEv(
    QGraphicsSceneBspTreeIndexPrivate *self) {
  self->purgeRemovedItems();
}

//  void QGraphicsSceneBspTreeIndexPrivate::invalidateSortCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QGraphicsSceneBspTreeIndexPrivate19invalidateSortCacheEv(
    QGraphicsSceneBspTreeIndexPrivate *self) {
  self->invalidateSortCache();
}

//  void QGraphicsSceneBspTreeIndexPrivate::climbTree(QGraphicsItem *item,
//      int *stackingOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QGraphicsSceneBspTreeIndexPrivate9climbTreeEP13QGraphicsItemPi(
    QGraphicsItem *item,
    int *stackingOrder) {
  QGraphicsSceneBspTreeIndexPrivate::climbTree(item, stackingOrder);
}

//  bool QGraphicsSceneBspTreeIndexPrivate::closestItemFirst_withCache(const
//      QGraphicsItem *item1, const QGraphicsItem *item2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QGraphicsSceneBspTreeIndexPrivate26closestItemFirst_withCacheEPK13QGraphicsItemS2_(
    const QGraphicsItem *item1,
    const QGraphicsItem *item2) {
  return QGraphicsSceneBspTreeIndexPrivate::closestItemFirst_withCache(
      item1,
      item2);
}

//  bool QGraphicsSceneBspTreeIndexPrivate::closestItemLast_withCache(const
//      QGraphicsItem *item1, const QGraphicsItem *item2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QGraphicsSceneBspTreeIndexPrivate25closestItemLast_withCacheEPK13QGraphicsItemS2_(
    const QGraphicsItem *item1,
    const QGraphicsItem *item2) {
  return QGraphicsSceneBspTreeIndexPrivate::closestItemLast_withCache(
      item1,
      item2);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
