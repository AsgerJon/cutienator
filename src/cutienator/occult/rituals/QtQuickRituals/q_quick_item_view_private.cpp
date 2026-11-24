//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickitemview_p_p.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickitemviewfxitem_p_p.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQml/QQmlInfo>
#include "qplatformdefs.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2463, as _ZN21QQuickItemViewPrivate24prepareRemoveTransitionsEP10QMultiHashIN13QQmlChangeSet7MoveKeyEP10FxViewItemE
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickItemViewPrivate::prepareRemoveTransitions(QMultiHash<QQmlChangeSet::MoveKey, FxViewItem *> *removedItems)
{
    if (!transitioner)
        return;

    if (transitioner->canTransition(QQuickItemViewTransitioner::RemoveTransition, true)
            || transitioner->canTransition(QQuickItemViewTransitioner::RemoveTransition, false)) {
        for (auto it = removedItems->begin(); it != removedItems->end(); ) {
            bool isRemove = it.key().moveId < 0;
            if (isRemove) {
                FxViewItem *item = *it;
                item->trackGeometry(false);
                item->releaseAfterTransition = true;
                releasePendingTransition.append(item);
                item->transitionNextReposition(transitioner, QQuickItemViewTransitioner::RemoveTransition, true);
                it = removedItems->erase(it);
            } else {
                ++it;
            }
        }
    }
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1800, as _ZN21QQuickItemViewPrivate4initEv
inline void QQuickItemViewPrivate::init()
{
    Q_Q(QQuickItemView);
    q->setFlag(QQuickItem::ItemIsFocusScope);
    QObject::connect(q, SIGNAL(movementEnded()), q, SLOT(animStopped()));
    QObject::connect(q, &QQuickFlickable::interactiveChanged, q, &QQuickItemView::keyNavigationEnabledChanged);
    q->setFlickableDirection(QQuickFlickable::VerticalFlick);
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1856, as _ZN21QQuickItemViewPrivate5clearEb
inline void QQuickItemViewPrivate::clear(bool onDestruction)
{
    Q_Q(QQuickItemView);

    isClearing = true;
    auto cleanup = qScopeGuard([this] { isClearing = false; });

    currentChanges.reset();
    bufferedChanges.reset();
    timeline.clear();

    releaseVisibleItems(QQmlInstanceModel::NotReusable);
    visibleIndex = 0;

#if QT_CONFIG(quick_viewtransitions)
    for (FxViewItem *item : std::as_const(releasePendingTransition)) {
        item->releaseAfterTransition = false;
        releaseItem(item, QQmlInstanceModel::NotReusable);
    }
    releasePendingTransition.clear();
#endif

    const bool hadCurrentItem = currentItem != nullptr;
    releaseCurrentItem(QQmlDelegateModel::NotReusable);
    if (hadCurrentItem)
        emit q->currentItemChanged();
    createHighlight(onDestruction);
    trackedItem = nullptr;

    if (requestedIndex >= 0) {
        if (model)
            model->cancel(requestedIndex);
        requestedIndex = -1;
    }

    markExtentsDirty();
    itemCount = 0;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2007, as _ZN21QQuickItemViewPrivate14updateViewportEv
inline void QQuickItemViewPrivate::updateViewport()
{
    Q_Q(QQuickItemView);
    qreal extra = headerSize() + footerSize();
    qreal contentSize = isValid() || !visibleItems.isEmpty() ? (endPosition() - startPosition()) : 0.0;
    if (layoutOrientation() == Qt::Vertical)
        q->setContentHeight(contentSize + extra);
    else
        q->setContentWidth(contentSize + extra);
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2796, as _ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQuickItem
inline void QQuickItemViewPrivate::initializeComponentItem(QQuickItem *item) const
{
    Q_UNUSED(item);
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2397, as _ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePosEP10FxViewItemPNS_12ChangeResultE
inline void QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(FxViewItem *item, ChangeResult *removeResult)
{
    removeResult->sizeChangesBeforeVisiblePos += item->size();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1689, as _ZN21QQuickItemViewPrivateD1Ev
inline QQuickItemViewPrivate::~QQuickItemViewPrivate()
{
#if QT_CONFIG(quick_viewtransitions)
    if (transitioner)
        transitioner->setChangeListener(nullptr);
    delete transitioner;
#endif
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1698, as _ZNK21QQuickItemViewPrivate7isValidEv
inline bool QQuickItemViewPrivate::isValid() const
{
    return model && model->count() && model->isValid();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1703, as _ZNK21QQuickItemViewPrivate8positionEv
inline qreal QQuickItemViewPrivate::position() const
{
    Q_Q(const QQuickItemView);
    return layoutOrientation() == Qt::Vertical ? q->contentY() : q->contentX();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1709, as _ZNK21QQuickItemViewPrivate4sizeEv
inline qreal QQuickItemViewPrivate::size() const
{
    Q_Q(const QQuickItemView);
    return layoutOrientation() == Qt::Vertical ? q->height() : q->width();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1715, as _ZNK21QQuickItemViewPrivate13startPositionEv
inline qreal QQuickItemViewPrivate::startPosition() const
{
    return isContentFlowReversed() ? -lastPosition() : originPosition();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1720, as _ZNK21QQuickItemViewPrivate11endPositionEv
inline qreal QQuickItemViewPrivate::endPosition() const
{
    return isContentFlowReversed() ? -originPosition() : lastPosition();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1725, as _ZNK21QQuickItemViewPrivate18contentStartOffsetEv
inline qreal QQuickItemViewPrivate::contentStartOffset() const
{
    qreal pos = -headerSize();
    if (layoutOrientation() == Qt::Vertical) {
        if (isContentFlowReversed())
            pos -= vData.endMargin;
        else
            pos -= vData.startMargin;
    } else {
        if (isContentFlowReversed())
            pos -= hData.endMargin;
        else
            pos -= hData.startMargin;
    }
    return pos;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1742, as _ZNK21QQuickItemViewPrivate20findLastVisibleIndexEi
inline int QQuickItemViewPrivate::findLastVisibleIndex(int defaultValue) const
{
    for (auto it = visibleItems.rbegin(), end = visibleItems.rend(); it != end; ++it) {
        auto item = *it;
        if (item->index != -1)
            return item->index;
    }
    return defaultValue;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1772, as _ZNK21QQuickItemViewPrivate19findLastIndexInViewEv
inline int QQuickItemViewPrivate::findLastIndexInView() const
{
    const qreal viewEndPos = isContentFlowReversed() ? -position() : position() + size();
    for (auto it = visibleItems.rbegin(), end = visibleItems.rend(); it != end; ++it) {
        auto item = *it;
        if (item->index != -1 && item->position() <= viewEndPos)
            return item->index;
    }
    return -1;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1786, as _ZNK21QQuickItemViewPrivate12mapFromModelEi
inline int QQuickItemViewPrivate::mapFromModel(int modelIndex) const
{
    if (modelIndex < visibleIndex || modelIndex >= visibleIndex + visibleItems.size())
        return -1;
    for (int i = 0; i < visibleItems.size(); ++i) {
        FxViewItem *item = visibleItems.at(i);
        if (item->index == modelIndex)
            return i;
        if (item->index > modelIndex)
            return -1;
    }
    return -1; // Not in visibleList
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1903, as _ZN21QQuickItemViewPrivate17animationFinishedEP21QAbstractAnimationJob
inline void QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob *)
{
    Q_Q(QQuickItemView);
    fillCacheBuffer = true;
    q->polish();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1896, as _ZN21QQuickItemViewPrivate12mirrorChangeEv
inline void QQuickItemViewPrivate::mirrorChange()
{
    Q_Q(QQuickItemView);
    regenerate();
    emit q->effectiveLayoutDirectionChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2705, as _ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickItem
inline void QQuickItemViewPrivate::itemDestroyed(QQuickItem *item)
{
    // We can't check model->indexOf(item, q_func()) here, because the item
    // may not exist there, so we instead check visibleItems.
    FxViewItem *visibleFxItem = nullptr;
    const int indexOfItem = -1;
    for (auto *fxItem : std::as_const(visibleItems)) {
        if (fxItem->item == item) {
            visibleFxItem = fxItem;
            break;
        }
    }

    // Make sure that we don't try to clean up the same FxViewItem twice,
    // as apparently there can be two FxViewItems for the same QQuickItem.
    if (currentItem && visibleFxItem)
        Q_ASSERT(currentItem != visibleFxItem);

    if (visibleFxItem) {
        qCDebug(lcItemViewDelegateLifecycle) << "removing deleted item"
            << item << visibleFxItem << "at index" << indexOfItem << "without running transitions";
        // We need to remove it from visibleItems manually, as we don't want to call
        // removeNonVisibleItems since it won't remove items with transitions.
        const bool removedVisibleFxItem = visibleItems.removeOne(visibleFxItem);
        Q_ASSERT(removedVisibleFxItem);
        releaseItem(visibleFxItem, QQmlDelegateModel::NotReusable);
    }

    if (currentItem && currentItem->item == item) {
        releaseItem(currentItem, QQmlDelegateModel::NotReusable);
        currentItem = nullptr;
    }

    unrequestedItems.remove(item);

    // Update the positioning of the items.
    forceLayoutPolish();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2744, as _ZN21QQuickItemViewPrivate19createHighlightItemEv
inline QQuickItem *QQuickItemViewPrivate::createHighlightItem()
{
    QQuickItem *item = nullptr;
    if (!inRequest) {
        inRequest = true;
        item = createComponentItem(highlightComponent, 0.0, true);
        inRequest = false;
    }
    return item;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2755, as _ZNK21QQuickItemViewPrivate19createComponentItemEP13QQmlComponentdb
inline QQuickItem *QQuickItemViewPrivate::createComponentItem(QQmlComponent *component, qreal zValue, bool createDefault) const
{
    Q_Q(const QQuickItemView);

    QQuickItem *item = nullptr;
    if (component) {
        QQmlContext *context = component->creationContext();
        if (!context)
            context = qmlContext(q);

        if (QObject *nobj = component->beginCreate(context)) {
            item = qobject_cast<QQuickItem *>(nobj);
            if (!item)
                delete nobj;
        }
    } else if (createDefault) {
        item = new QQuickItem;
    }
    if (item) {
        if (qFuzzyIsNull(item->z()))
            item->setZ(zValue);
        QQml_setParent_noEvent(item, q->contentItem());
        item->setParentItem(q->contentItem());

        initializeComponentItem(item);
    }
    if (component)
        component->completeCreate();
    return item;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2801, as _ZN21QQuickItemViewPrivate17updateTrackedItemEv
inline void QQuickItemViewPrivate::updateTrackedItem()
{
    Q_Q(QQuickItemView);
    FxViewItem *item = currentItem;
    if (highlight)
        item = highlight.get();
    trackedItem = item;

    if (trackedItem)
        q->trackedPositionChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2813, as _ZN21QQuickItemViewPrivate24updateUnrequestedIndexesEv
inline void QQuickItemViewPrivate::updateUnrequestedIndexes()
{
    Q_Q(QQuickItemView);
    for (QHash<QQuickItem*,int>::iterator it = unrequestedItems.begin(), end = unrequestedItems.end(); it != end; ++it)
        *it = model->indexOf(it.key(), q);
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2820, as _ZN21QQuickItemViewPrivate26updateUnrequestedPositionsEv
inline void QQuickItemViewPrivate::updateUnrequestedPositions()
{
    for (QHash<QQuickItem*,int>::const_iterator it = unrequestedItems.cbegin(), cend = unrequestedItems.cend(); it != cend; ++it) {
        if (it.value() >= 0)
            repositionPackageItemAt(it.key(), it.value());
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2828, as _ZN21QQuickItemViewPrivate18updateVisibleIndexEv
inline void QQuickItemViewPrivate::updateVisibleIndex()
{
    typedef QList<FxViewItem*>::const_iterator FxViewItemListConstIt;

    visibleIndex = 0;
    for (FxViewItemListConstIt it = visibleItems.constBegin(), cend = visibleItems.constEnd(); it != cend; ++it) {
        if ((*it)->index != -1) {
            visibleIndex = (*it)->index;
            break;
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1120, as _ZNK21QQuickItemViewPrivate19calculatedMinExtentEv
inline qreal QQuickItemViewPrivate::calculatedMinExtent() const
{
    Q_Q(const QQuickItemView);
    qreal minExtent;
    if (layoutOrientation() == Qt::Vertical)
        minExtent = isContentFlowReversed() ? q->maxYExtent() - size(): -q->minYExtent();
    else
        minExtent = isContentFlowReversed() ? q->maxXExtent() - size(): -q->minXExtent();
    return minExtent;

}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1132, as _ZNK21QQuickItemViewPrivate19calculatedMaxExtentEv
inline qreal QQuickItemViewPrivate::calculatedMaxExtent() const
{
    Q_Q(const QQuickItemView);
    qreal maxExtent;
    if (layoutOrientation() == Qt::Vertical)
        maxExtent = isContentFlowReversed() ? q->minYExtent() - size(): -q->maxYExtent();
    else
        maxExtent = isContentFlowReversed() ? q->minXExtent() - size(): -q->maxXExtent();
    return maxExtent;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2324, as _ZN21QQuickItemViewPrivate18applyRemovalChangeERKN13QQmlChangeSet6ChangeEPNS_12ChangeResultEPi
inline bool QQuickItemViewPrivate::applyRemovalChange(const QQmlChangeSet::Change &removal, ChangeResult *removeResult, int *removedCount)
{
    Q_Q(QQuickItemView);
    bool visibleAffected = false;

    if (visibleItems.size() && removal.index + removal.count > visibleItems.constLast()->index) {
        if (removal.index > visibleItems.constLast()->index)
            removeResult->countChangeAfterVisibleItems += removal.count;
        else
            removeResult->countChangeAfterVisibleItems += ((removal.index + removal.count - 1) - visibleItems.constLast()->index);
    }

    QList<FxViewItem*>::Iterator it = visibleItems.begin();
    while (it != visibleItems.end()) {
        FxViewItem *item = *it;
        if (item->index == -1 || item->index < removal.index) {
            // already removed, or before removed items
            if (!visibleAffected && item->index < removal.index)
                visibleAffected = true;
            ++it;
        } else if (item->index >= removal.index + removal.count) {
            // after removed items
            item->index -= removal.count;
#if QT_CONFIG(quick_viewtransitions)
            if (removal.isMove())
                item->transitionNextReposition(transitioner, QQuickItemViewTransitioner::MoveTransition, false);
            else
                item->transitionNextReposition(transitioner, QQuickItemViewTransitioner::RemoveTransition, false);
#endif
            ++it;
        } else {
            // removed item
            visibleAffected = true;
            if (!removal.isMove() && item->item && item->attached)
                item->attached->emitRemove();

            if (item->item && item->attached && item->attached->delayRemove() && !removal.isMove()) {
                item->index = -1;
                QObject::connect(item->attached, SIGNAL(delayRemoveChanged()), q, SLOT(destroyRemoved()), Qt::QueuedConnection);
                ++it;
            } else {
                removeItem(item, removal, removeResult);
                if (!removal.isMove())
                    (*removedCount)++;
                it = visibleItems.erase(it);
            }
        }
    }

    return visibleAffected;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2376, as _ZN21QQuickItemViewPrivate10removeItemEP10FxViewItemRKN13QQmlChangeSet6ChangeEPNS_12ChangeResultE
inline void QQuickItemViewPrivate::removeItem(FxViewItem *item, const QQmlChangeSet::Change &removal, ChangeResult *removeResult)
{
    if (removeResult->visiblePos.isValid()) {
        if (item->position() < removeResult->visiblePos)
            updateSizeChangesBeforeVisiblePos(item, removeResult);
        else
            removeResult->sizeChangesAfterVisiblePos += item->size();
    }
    if (removal.isMove()) {
        currentChanges.removedItems.replace(removal.moveKey(item->index), item);
#if QT_CONFIG(quick_viewtransitions)
        item->transitionNextReposition(transitioner, QQuickItemViewTransitioner::MoveTransition, true);
#endif
    } else {
        // track item so it is released later
        currentChanges.removedItems.insert(QQmlChangeSet::MoveKey(), item);
    }
    if (!removeResult->changedFirstItem && item == *visibleItems.constBegin())
        removeResult->changedFirstItem = true;
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2402, as _ZN21QQuickItemViewPrivate19repositionFirstItemEP10FxViewItemdS1_PNS_12ChangeResultES3_
inline void QQuickItemViewPrivate::repositionFirstItem(FxViewItem *prevVisibleItemsFirst,
                                                   qreal prevVisibleItemsFirstPos,
                                                   FxViewItem *prevFirstVisible,
                                                   ChangeResult *insertionResult,
                                                   ChangeResult *removalResult)
{
    const QQmlNullableValue<qreal> prevViewPos = insertionResult->visiblePos;

    // reposition visibleItems.first() correctly so that the content y doesn't jump
    if (visibleItems.size()) {
        if (prevVisibleItemsFirst && insertionResult->changedFirstItem)
            resetFirstItemPosition(prevVisibleItemsFirstPos);

        if (prevFirstVisible && prevVisibleItemsFirst == prevFirstVisible
                && prevFirstVisible != *visibleItems.constBegin()) {
            // the previous visibleItems.first() was also the first visible item, and it has been
            // moved/removed, so move the new visibleItems.first() to the pos of the previous one
            if (!insertionResult->changedFirstItem)
                resetFirstItemPosition(prevVisibleItemsFirstPos);

        } else if (prevViewPos.isValid()) {
            qreal moveForwardsBy = 0;
            qreal moveBackwardsBy = 0;

            // shift visibleItems.first() relative to the number of added/removed items
            const auto pos = visibleItems.constFirst()->position();
            if (pos > prevViewPos) {
                moveForwardsBy = insertionResult->sizeChangesAfterVisiblePos;
                moveBackwardsBy = removalResult->sizeChangesAfterVisiblePos;
            } else if (pos < prevViewPos) {
                moveForwardsBy = removalResult->sizeChangesBeforeVisiblePos;
                moveBackwardsBy = insertionResult->sizeChangesBeforeVisiblePos;
            }
            adjustFirstItem(moveForwardsBy, moveBackwardsBy, insertionResult->countChangeBeforeVisible - removalResult->countChangeBeforeVisible);
        }
        insertionResult->reset();
        removalResult->reset();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2443, as _ZN21QQuickItemViewPrivate18createTransitionerEv
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickItemViewPrivate::createTransitioner()
{
    if (!transitioner) {
        transitioner = new QQuickItemViewTransitioner;
        transitioner->setChangeListener(this);
    }
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2451, as _ZN21QQuickItemViewPrivate29prepareVisibleItemTransitionsEv
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickItemViewPrivate::prepareVisibleItemTransitions()
{
    Q_Q(QQuickItemView);
    if (!transitioner)
        return;

    // must call for every visible item to init or discard transitions
    QRectF viewBounds(q->contentX(), q->contentY(), q->width(), q->height());
    for (int i=0; i<visibleItems.size(); i++)
        visibleItems[i]->prepareTransition(transitioner, viewBounds);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2486, as _ZN21QQuickItemViewPrivate31prepareNonVisibleItemTransitionEP10FxViewItemRK6QRectF
#if QT_CONFIG(quick_viewtransitions)
inline bool QQuickItemViewPrivate::prepareNonVisibleItemTransition(FxViewItem *item, const QRectF &viewBounds)
{
    // Called for items that have been removed from visibleItems and may now be
    // transitioned out of the view. This applies to items that are being directly
    // removed, or moved to outside of the view, as well as those that are
    // displaced to a position outside of the view due to an insert or move.

    if (!transitioner)
        return false;

    if (item->scheduledTransitionType() == QQuickItemViewTransitioner::MoveTransition)
        repositionItemAt(item, item->index, 0);

    bool success = false;
    ACTION_IF_DELETED(item, success = item->prepareTransition(transitioner, viewBounds), return success);

    if (success) {
        item->releaseAfterTransition = true;
        return true;
    }
    return false;
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 2509, as _ZN21QQuickItemViewPrivate26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickItemViewPrivate::viewItemTransitionFinished(QQuickItemViewTransitionableItem *item)
{
    for (int i=0; i<releasePendingTransition.size(); i++) {
        if (releasePendingTransition.at(i)->transitionableItem == item) {
            releaseItem(releasePendingTransition.takeAt(i), reusableFlag);
            return;
        }
    }
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1253, as _ZNK21QQuickItemViewPrivate12checkVisibleEv
inline void QQuickItemViewPrivate::checkVisible() const
{
    int skip = 0;
    for (int i = 0; i < visibleItems.size(); ++i) {
        FxViewItem *item = visibleItems.at(i);
        if (item->index == -1) {
            ++skip;
        } else if (item->index != visibleIndex + i - skip) {
            qFatal("index %d %d %d", visibleIndex, i, item->index);
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1267, as _ZNK21QQuickItemViewPrivate16showVisibleItemsEv
inline void QQuickItemViewPrivate::showVisibleItems() const
{
    qDebug() << "Visible items:";
    for (FxViewItem *item : visibleItems) {
        qDebug() << "\t" << item->index
                 << item->item->objectName()
                 << item->position();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 1285, as _ZN21QQuickItemViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickItemViewPrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change,
                                                const QRectF &oldGeometry)
{
    Q_Q(QQuickItemView);
    QQuickFlickablePrivate::itemGeometryChanged(item, change, oldGeometry);
    if (!q->isComponentComplete())
        return;

    if (header && header->item == item) {
        updateHeader();
        markExtentsDirty();
        updateViewport();
        if (!q->isMoving() && !q->isFlicking())
            fixupPosition();
    } else if (footer && footer->item == item) {
        updateFooter();
        markExtentsDirty();
        updateViewport();
        if (!q->isMoving() && !q->isFlicking())
            fixupPosition();
    }

    if (currentItem && currentItem->item == item) {
        // don't allow item movement transitions to trigger a re-layout and
        // start new transitions
        bool prevInLayout = inLayout;
#if QT_CONFIG(quick_viewtransitions)
        if (!inLayout) {
            FxViewItem *actualItem = transitioner ? visibleItem(currentIndex) : nullptr;
            if (actualItem && actualItem->transitionRunning())
                inLayout = true;
        }
#endif
        updateHighlight();
        inLayout = prevInLayout;
    }

    if (trackedItem && trackedItem->item == item)
        q->trackedPositionChanged();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickItemViewPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickItemViewPrivate : QQuickItemViewPrivate {
  using QQuickItemViewPrivate::hasStickyHeader;
  using QQuickItemViewPrivate::hasStickyFooter;
  using QQuickItemViewPrivate::movingFromHighlight;
  using QQuickItemViewPrivate::visibleItemsChanged;
  using QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex;
  using QQuickItemViewPrivate::initializeViewItem;
  using QQuickItemViewPrivate::initializeCurrentItem;
  using QQuickItemViewPrivate::updateSectionCriteria;
  using QQuickItemViewPrivate::updateSections;
};

//  A QQuickItemViewPrivate that Python can take functions over in. Every QQuickItemViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall3)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall5)(const void *, FxViewItem *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall6)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall7)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall8)(const void *, FxViewItem *, QQuickItemViewPrivate::ChangeResult *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall9)(const void *, QQuickItemViewTransitionableItem *, int *);
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_itemview)
typedef void * (*CuteQQuickItemViewPrivateCall10)(const void *, const QObject *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef int (*CuteQQuickItemViewPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall13)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall14)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall15)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall16)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall17)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewPrivateCall18)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall19)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall20)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall21)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall22)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall23)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall24)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall25)(const void *, bool, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall26)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall27)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall28)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall29)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall30)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall31)(const void *, qreal, qreal, qreal, qreal, bool, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall32)(const void *, qreal, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall33)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void * (*CuteQQuickItemViewPrivateCall34)(const void *, int, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall35)(const void *, FxViewItem *, int, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall36)(const void *, QQuickItem *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall37)(const void *, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall38)(const void *, qreal, qreal, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall39)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall40)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewPrivateCall41)(const void *, int, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_viewtransitions)
typedef void (*CuteQQuickItemViewPrivateCall42)(const void *, int, const QQuickItemViewPrivate::ChangeResult *, const QQuickItemViewPrivate::ChangeResult *, int *);
#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall43)(const void *, FxViewItem *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall44)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall45)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall46)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall47)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_itemview)
typedef void (*CuteQQuickItemViewPrivateCall48)(const void *, QQuickPointerHandler *, int *);
typedef bool (*CuteQQuickItemViewPrivateCall49)(const void *, const QPointerEvent *, int *);
typedef void (*CuteQQuickItemViewPrivateCall50)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickItemViewPrivateCall51)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickItemViewPrivateCall52)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickItemViewPrivateCall53)(const void *, int, int *);
typedef qreal (*CuteQQuickItemViewPrivateCall54)(const void *, int *);
typedef qreal (*CuteQQuickItemViewPrivateCall55)(const void *, int *);
typedef void (*CuteQQuickItemViewPrivateCall56)(const void *, int *);
typedef void (*CuteQQuickItemViewPrivateCall57)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickItemViewPrivateCall58)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickItemViewPrivateCall59)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickItemViewPrivateCall60)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickItemViewPrivateCall61)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickItemViewPrivateCall62)(const void *, bool, int *);
typedef void * (*CuteQQuickItemViewPrivateCall63)(const void *, int *);
typedef void (*CuteQQuickItemViewPrivateCall64)(const void *, int *);
typedef void (*CuteQQuickItemViewPrivateCall65)(const void *, int, int *);
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickItemViewPrivateCall66)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickItemViewPrivateCall67)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickItemViewPrivateCall68)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickItemViewPrivate : public QQuickItemViewPrivate {
public:
  using QQuickItemViewPrivate::QQuickItemViewPrivate;
  void *taken[69] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate4initEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate5clearEb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate14updateViewportEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate11releaseItemEP10FxViewItemN17QQmlInstanceModel12ReusableFlagE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePosEP10FxViewItemPNS_12ChangeResultE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN38QQuickItemViewTransitionChangeListener26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObject")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate17layoutOrientationEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate21isContentFlowReversedEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate10positionAtEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate13endPositionAtEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate14originPositionEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate12lastPositionEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate10headerSizeEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate10footerSizeEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate18showHeaderForIndexEi")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate18showFooterForIndexEi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate12updateHeaderEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate12updateFooterEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate15hasStickyFooterEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate15createHighlightEb")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate15updateHighlightEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate22resetHighlightPositionEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate19movingFromHighlightEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate11setPositionEd")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate13fixupPositionEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate15addVisibleItemsEddddb")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate21removeNonVisibleItemsEdd")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate19visibleItemsChangedEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate11newViewItemEiP10QQuickItem")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate16repositionItemAtEP10FxViewItemid")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate23repositionPackageItemAtEP10QQuickItemi")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate22resetFirstItemPositionEd")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate15adjustFirstItemEddi")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate18layoutVisibleItemsEi")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate19changedVisibleIndexEi")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemovedIndexEi")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_viewtransitions)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate32translateAndTransitionItemsAfterEiRKNS_12ChangeResultES2_")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxViewItem")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate21initializeCurrentItemEv")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN21QQuickItemViewPrivate14updateSectionsEv")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[57] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[60] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[65] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[66] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[67] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[68] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall0 call = reinterpret_cast<CuteQQuickItemViewPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::init();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::clear(bool onDestruction)
  void clear(bool onDestruction) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall1 call = reinterpret_cast<CuteQQuickItemViewPrivateCall1>(taken[1]);
      call(this, onDestruction, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::clear(onDestruction);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateViewport()
  void updateViewport() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall2 call = reinterpret_cast<CuteQQuickItemViewPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::updateViewport();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(qml_animation)
#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob
  //      *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall3 call = reinterpret_cast<CuteQQuickItemViewPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::animationFinished(a0);
  }
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall4 call = reinterpret_cast<CuteQQuickItemViewPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::mirrorChange();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::releaseItem(FxViewItem *item,
  //      QQmlInstanceModel::ReusableFlag reusableFlag)
  bool releaseItem(
      FxViewItem *item,
      QQmlInstanceModel::ReusableFlag reusableFlag) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall5 call = reinterpret_cast<CuteQQuickItemViewPrivateCall5>(taken[5]);
      bool given = call(this, item, static_cast<int>(reusableFlag), &handled);
      if (handled) return given;
    }
    return QQuickItemViewPrivate::releaseItem(item, reusableFlag);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall6 call = reinterpret_cast<CuteQQuickItemViewPrivateCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::itemDestroyed(item);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::initializeComponentItem(QQuickItem *a0)
  //      const
  void initializeComponentItem(QQuickItem *a0) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall7 call = reinterpret_cast<CuteQQuickItemViewPrivateCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::initializeComponentItem(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void
  //      QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(FxViewIt
  //      em *item, ChangeResult *removeResult)
  void updateSizeChangesBeforeVisiblePos(
      FxViewItem *item,
      QQuickItemViewPrivate::ChangeResult *removeResult) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall8 call = reinterpret_cast<CuteQQuickItemViewPrivateCall8>(taken[8]);
      call(this, item, removeResult, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(item, removeResult);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::viewItemTransitionFinished(QQuickItemView
  //      TransitionableItem *item)
  void viewItemTransitionFinished(
      QQuickItemViewTransitionableItem *item) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall9 call = reinterpret_cast<CuteQQuickItemViewPrivateCall9>(taken[9]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::viewItemTransitionFinished(item);
  }
#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_itemview)
  //  QQuickItemViewAttached
  //      *QQuickItemViewPrivate::getAttachedObject(const QObject *a0)
  //      const
  QQuickItemViewAttached *getAttachedObject(
      const QObject *a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall10 call = reinterpret_cast<CuteQQuickItemViewPrivateCall10>(taken[10]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QQuickItemViewAttached *>(given);
    }
    return QQuickItemViewPrivate::getAttachedObject(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  Qt::Orientation QQuickItemViewPrivate::layoutOrientation() const
  Qt::Orientation layoutOrientation() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall11 call = reinterpret_cast<CuteQQuickItemViewPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::isContentFlowReversed() const
  bool isContentFlowReversed() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall12 call = reinterpret_cast<CuteQQuickItemViewPrivateCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::positionAt(int index) const
  qreal positionAt(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall13 call = reinterpret_cast<CuteQQuickItemViewPrivateCall13>(taken[13]);
      qreal given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::endPositionAt(int index) const
  qreal endPositionAt(int index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall14 call = reinterpret_cast<CuteQQuickItemViewPrivateCall14>(taken[14]);
      qreal given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::originPosition() const
  qreal originPosition() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall15 call = reinterpret_cast<CuteQQuickItemViewPrivateCall15>(taken[15]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::lastPosition() const
  qreal lastPosition() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall16 call = reinterpret_cast<CuteQQuickItemViewPrivateCall16>(taken[16]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::headerSize() const
  qreal headerSize() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall17 call = reinterpret_cast<CuteQQuickItemViewPrivateCall17>(taken[17]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewPrivate::footerSize() const
  qreal footerSize() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall18 call = reinterpret_cast<CuteQQuickItemViewPrivateCall18>(taken[18]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::showHeaderForIndex(int index) const
  bool showHeaderForIndex(int index) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall19 call = reinterpret_cast<CuteQQuickItemViewPrivateCall19>(taken[19]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::showFooterForIndex(int index) const
  bool showFooterForIndex(int index) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall20 call = reinterpret_cast<CuteQQuickItemViewPrivateCall20>(taken[20]);
      bool given = call(this, index, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateHeader()
  void updateHeader() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall21 call = reinterpret_cast<CuteQQuickItemViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateFooter()
  void updateFooter() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall22 call = reinterpret_cast<CuteQQuickItemViewPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::hasStickyHeader() const
  bool hasStickyHeader() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall23 call = reinterpret_cast<CuteQQuickItemViewPrivateCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemViewPrivate::hasStickyHeader();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::hasStickyFooter() const
  bool hasStickyFooter() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall24 call = reinterpret_cast<CuteQQuickItemViewPrivateCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemViewPrivate::hasStickyFooter();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::createHighlight(bool onDestruction)
  void createHighlight(bool onDestruction) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall25 call = reinterpret_cast<CuteQQuickItemViewPrivateCall25>(taken[25]);
      call(this, onDestruction, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateHighlight()
  void updateHighlight() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall26 call = reinterpret_cast<CuteQQuickItemViewPrivateCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::resetHighlightPosition()
  void resetHighlightPosition() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall27 call = reinterpret_cast<CuteQQuickItemViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::movingFromHighlight()
  bool movingFromHighlight() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall28 call = reinterpret_cast<CuteQQuickItemViewPrivateCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemViewPrivate::movingFromHighlight();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::setPosition(qreal pos)
  void setPosition(qreal pos) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall29 call = reinterpret_cast<CuteQQuickItemViewPrivateCall29>(taken[29]);
      call(this, pos, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::fixupPosition()
  void fixupPosition() override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall30 call = reinterpret_cast<CuteQQuickItemViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::addVisibleItems(qreal fillFrom, qreal
  //      fillTo, qreal bufferFrom, qreal bufferTo, bool doBuffer)
  bool addVisibleItems(
      qreal fillFrom,
      qreal fillTo,
      qreal bufferFrom,
      qreal bufferTo,
      bool doBuffer) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall31 call = reinterpret_cast<CuteQQuickItemViewPrivateCall31>(taken[31]);
      bool given = call(this, fillFrom, fillTo, bufferFrom, bufferTo, doBuffer, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::removeNonVisibleItems(qreal bufferFrom,
  //      qreal bufferTo)
  bool removeNonVisibleItems(qreal bufferFrom, qreal bufferTo) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall32 call = reinterpret_cast<CuteQQuickItemViewPrivateCall32>(taken[32]);
      bool given = call(this, bufferFrom, bufferTo, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::visibleItemsChanged()
  void visibleItemsChanged() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall33 call = reinterpret_cast<CuteQQuickItemViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::visibleItemsChanged();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  FxViewItem *QQuickItemViewPrivate::newViewItem(int index, QQuickItem
  //      *item)
  FxViewItem *newViewItem(int index, QQuickItem *item) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall34 call = reinterpret_cast<CuteQQuickItemViewPrivateCall34>(taken[34]);
      void * given = call(this, index, item, &handled);
      if (handled) return static_cast<FxViewItem *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::repositionItemAt(FxViewItem *item, int
  //      index, qreal sizeBuffer)
  void repositionItemAt(
      FxViewItem *item,
      int index,
      qreal sizeBuffer) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall35 call = reinterpret_cast<CuteQQuickItemViewPrivateCall35>(taken[35]);
      call(this, item, index, sizeBuffer, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::repositionPackageItemAt(QQuickItem *item,
  //      int index)
  void repositionPackageItemAt(QQuickItem *item, int index) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall36 call = reinterpret_cast<CuteQQuickItemViewPrivateCall36>(taken[36]);
      call(this, item, index, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::resetFirstItemPosition(qreal pos)
  void resetFirstItemPosition(qreal pos) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall37 call = reinterpret_cast<CuteQQuickItemViewPrivateCall37>(taken[37]);
      call(this, pos, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::adjustFirstItem(qreal forwards, qreal
  //      backwards, int changeBeforeVisible)
  void adjustFirstItem(
      qreal forwards,
      qreal backwards,
      int changeBeforeVisible) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall38 call = reinterpret_cast<CuteQQuickItemViewPrivateCall38>(taken[38]);
      call(this, forwards, backwards, changeBeforeVisible, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::layoutVisibleItems(int fromModelIndex)
  void layoutVisibleItems(int fromModelIndex) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall39 call = reinterpret_cast<CuteQQuickItemViewPrivateCall39>(taken[39]);
      call(this, fromModelIndex, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::changedVisibleIndex(int newIndex)
  void changedVisibleIndex(int newIndex) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall40 call = reinterpret_cast<CuteQQuickItemViewPrivateCall40>(taken[40]);
      call(this, newIndex, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(int a0)
  //      const
  bool needsRefillForAddedOrRemovedIndex(int a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall41 call = reinterpret_cast<CuteQQuickItemViewPrivateCall41>(taken[41]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_viewtransitions)
  //  void QQuickItemViewPrivate::translateAndTransitionItemsAfter(int
  //      afterIndex, const ChangeResult &insertionResult, const
  //      ChangeResult &removalResult)
  void translateAndTransitionItemsAfter(
      int afterIndex,
      const QQuickItemViewPrivate::ChangeResult &insertionResult,
      const QQuickItemViewPrivate::ChangeResult &removalResult) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall42 call = reinterpret_cast<CuteQQuickItemViewPrivateCall42>(taken[42]);
      call(this, afterIndex, &insertionResult, &removalResult, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::initializeViewItem(FxViewItem *a0)
  void initializeViewItem(FxViewItem *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall43 call = reinterpret_cast<CuteQQuickItemViewPrivateCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::initializeViewItem(a0);
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::initializeCurrentItem()
  void initializeCurrentItem() override {
    if (taken[44]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall44 call = reinterpret_cast<CuteQQuickItemViewPrivateCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::initializeCurrentItem();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateSectionCriteria()
  void updateSectionCriteria() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall45 call = reinterpret_cast<CuteQQuickItemViewPrivateCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::updateSectionCriteria();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::updateSections()
  void updateSections() override {
    if (taken[46]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall46 call = reinterpret_cast<CuteQQuickItemViewPrivateCall46>(taken[46]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::updateSections();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  void QQuickItemViewPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall47 call = reinterpret_cast<CuteQQuickItemViewPrivateCall47>(taken[47]);
      call(this, item, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickItemViewPrivate::itemGeometryChanged(item, change, a2);
  }
#endif  // QT_CONFIG(quick_itemview)

  //  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler
  //      *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall48 call = reinterpret_cast<CuteQQuickItemViewPrivateCall48>(taken[48]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickFlickablePrivate::addPointerHandler(h);
  }

  //  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent
  //      *a0)
  bool wantsPointerEvent(const QPointerEvent *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall49 call = reinterpret_cast<CuteQQuickItemViewPrivateCall49>(taken[49]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickFlickablePrivate::wantsPointerEvent(a0);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall50 call = reinterpret_cast<CuteQQuickItemViewPrivateCall50>(taken[50]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall51 call = reinterpret_cast<CuteQQuickItemViewPrivateCall51>(taken[51]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall52 call = reinterpret_cast<CuteQQuickItemViewPrivateCall52>(taken[52]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall53 call = reinterpret_cast<CuteQQuickItemViewPrivateCall53>(taken[53]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[54]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall54 call = reinterpret_cast<CuteQQuickItemViewPrivateCall54>(taken[54]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[55]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall55 call = reinterpret_cast<CuteQQuickItemViewPrivateCall55>(taken[55]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[56]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall56 call = reinterpret_cast<CuteQQuickItemViewPrivateCall56>(taken[56]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[57]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall57 call = reinterpret_cast<CuteQQuickItemViewPrivateCall57>(taken[57]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall58 call = reinterpret_cast<CuteQQuickItemViewPrivateCall58>(taken[58]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall59 call = reinterpret_cast<CuteQQuickItemViewPrivateCall59>(taken[59]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall60 call = reinterpret_cast<CuteQQuickItemViewPrivateCall60>(taken[60]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall61 call = reinterpret_cast<CuteQQuickItemViewPrivateCall61>(taken[61]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall62 call = reinterpret_cast<CuteQQuickItemViewPrivateCall62>(taken[62]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[63]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall63 call = reinterpret_cast<CuteQQuickItemViewPrivateCall63>(taken[63]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[64]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall64 call = reinterpret_cast<CuteQQuickItemViewPrivateCall64>(taken[64]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[65]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall65 call = reinterpret_cast<CuteQQuickItemViewPrivateCall65>(taken[65]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationStateChanged(QAbstractAnim
  //      ationJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall66 call = reinterpret_cast<CuteQQuickItemViewPrivateCall66>(taken[66]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall67 call = reinterpret_cast<CuteQQuickItemViewPrivateCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQuickItemViewPrivateCall68 call = reinterpret_cast<CuteQQuickItemViewPrivateCall68>(taken[68]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickItemView *QQuickItemViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickItemView *ritual_ZN21QQuickItemViewPrivate6q_funcEv(
    QQuickItemViewPrivate *self) {
  return self->q_func();
}

//  const QQuickItemView *QQuickItemViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickItemView *ritual_ZNK21QQuickItemViewPrivate6q_funcEv(
    const QQuickItemViewPrivate *self) {
  return self->q_func();
}

//  QQuickItemViewPrivate::~QQuickItemViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivateD1Ev(QQuickItemViewPrivate *self) {
  delete self;
}

//  QQuickItemViewPrivate *QQuickItemViewPrivate::get(QQuickItemView *o)
extern "C" Q_DECL_EXPORT
QQuickItemViewPrivate *ritual_ZN21QQuickItemViewPrivate3getEP14QQuickItemView(
    QQuickItemView *o) {
  return QQuickItemViewPrivate::get(o);
}

//  bool QQuickItemViewPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate7isValidEv(
    const QQuickItemViewPrivate *self) {
  return self->isValid();
}

//  qreal QQuickItemViewPrivate::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate8positionEv(
    const QQuickItemViewPrivate *self) {
  return self->position();
}

//  qreal QQuickItemViewPrivate::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate4sizeEv(
    const QQuickItemViewPrivate *self) {
  return self->size();
}

//  qreal QQuickItemViewPrivate::startPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate13startPositionEv(
    const QQuickItemViewPrivate *self) {
  return self->startPosition();
}

//  qreal QQuickItemViewPrivate::endPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate11endPositionEv(
    const QQuickItemViewPrivate *self) {
  return self->endPosition();
}

//  qreal QQuickItemViewPrivate::contentStartOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate18contentStartOffsetEv(
    const QQuickItemViewPrivate *self) {
  return self->contentStartOffset();
}

//  int QQuickItemViewPrivate::findLastVisibleIndex(int defaultValue) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickItemViewPrivate20findLastVisibleIndexEi(
    const QQuickItemViewPrivate *self,
    int defaultValue) {
  return self->findLastVisibleIndex(defaultValue);
}

//  int QQuickItemViewPrivate::findLastIndexInView() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickItemViewPrivate19findLastIndexInViewEv(
    const QQuickItemViewPrivate *self) {
  return self->findLastIndexInView();
}

//  int QQuickItemViewPrivate::mapFromModel(int modelIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickItemViewPrivate12mapFromModelEi(
    const QQuickItemViewPrivate *self,
    int modelIndex) {
  return self->mapFromModel(modelIndex);
}

//  void QQuickItemViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate4initEv(QQuickItemViewPrivate *self) {
  self->init();
}

//  void QQuickItemViewPrivate::clear(bool onDestruction)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate5clearEb(
    QQuickItemViewPrivate *self,
    bool onDestruction) {
  self->clear(onDestruction);
}

//  void QQuickItemViewPrivate::updateViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate14updateViewportEv(
    QQuickItemViewPrivate *self) {
  self->updateViewport();
}

//  void QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate17animationFinishedEP21QAbstractAnimationJob(
    QQuickItemViewPrivate *self,
    QAbstractAnimationJob *a0) {
  self->animationFinished(a0);
}

//  void QQuickItemViewPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12mirrorChangeEv(
    QQuickItemViewPrivate *self) {
  self->mirrorChange();
}

//  bool
//      QQuickItemViewPrivate::releaseCurrentItem(QQmlInstanceModel::Reusable
//      Flag reusableFlag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate18releaseCurrentItemEN17QQmlInstanceModel12ReusableFlagE(
    QQuickItemViewPrivate *self,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  return self->releaseCurrentItem(reusableFlag);
}

//  bool QQuickItemViewPrivate::releaseItem(FxViewItem *item,
//      QQmlInstanceModel::ReusableFlag reusableFlag)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate11releaseItemEP10FxViewItemN17QQmlInstanceModel12ReusableFlagE(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  return self->releaseItem(item, reusableFlag);
}

//  void QQuickItemViewPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate13itemDestroyedEP10QQuickItem(
    QQuickItemViewPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QQuickItem *QQuickItemViewPrivate::createHighlightItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN21QQuickItemViewPrivate19createHighlightItemEv(
    QQuickItemViewPrivate *self) {
  return self->createHighlightItem();
}

//  QQuickItem *QQuickItemViewPrivate::createComponentItem(QQmlComponent
//      *component, qreal zValue, bool createDefault) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickItemViewPrivate19createComponentItemEP13QQmlComponentdb(
    const QQuickItemViewPrivate *self,
    QQmlComponent *component,
    qreal zValue,
    bool createDefault) {
  return self->createComponentItem(component, zValue, createDefault);
}

//  void QQuickItemViewPrivate::initializeComponentItem(QQuickItem *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQuickItem(
    const QQuickItemViewPrivate *self,
    QQuickItem *a0) {
  self->initializeComponentItem(a0);
}

//  void QQuickItemViewPrivate::updateTrackedItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate17updateTrackedItemEv(
    QQuickItemViewPrivate *self) {
  self->updateTrackedItem();
}

//  void QQuickItemViewPrivate::updateUnrequestedIndexes()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate24updateUnrequestedIndexesEv(
    QQuickItemViewPrivate *self) {
  self->updateUnrequestedIndexes();
}

//  void QQuickItemViewPrivate::updateUnrequestedPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate26updateUnrequestedPositionsEv(
    QQuickItemViewPrivate *self) {
  self->updateUnrequestedPositions();
}

//  void QQuickItemViewPrivate::updateVisibleIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate18updateVisibleIndexEv(
    QQuickItemViewPrivate *self) {
  self->updateVisibleIndex();
}

//  qreal QQuickItemViewPrivate::calculatedMinExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate19calculatedMinExtentEv(
    const QQuickItemViewPrivate *self) {
  return self->calculatedMinExtent();
}

//  qreal QQuickItemViewPrivate::calculatedMaxExtent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate19calculatedMaxExtentEv(
    const QQuickItemViewPrivate *self) {
  return self->calculatedMaxExtent();
}

//  void QQuickItemViewPrivate::applyDelegateModelAccessChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate30applyDelegateModelAccessChangeEv(
    QQuickItemViewPrivate *self) {
  self->applyDelegateModelAccessChange();
}

//  bool QQuickItemViewPrivate::applyRemovalChange(const
//      QQmlChangeSet::Change &removal, ChangeResult *changeResult, int
//      *removedCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate18applyRemovalChangeERKN13QQmlChangeSet6ChangeEPNS_12ChangeResultEPi(
    QQuickItemViewPrivate *self,
    const QQmlChangeSet::Change *removal,
    QQuickItemViewPrivate::ChangeResult *changeResult,
    int *removedCount) {
  return self->applyRemovalChange(*removal, changeResult, removedCount);
}

//  void QQuickItemViewPrivate::removeItem(FxViewItem *item, const
//      QQmlChangeSet::Change &removal, ChangeResult *removeResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate10removeItemEP10FxViewItemRKN13QQmlChangeSet6ChangeEPNS_12ChangeResultE(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    const QQmlChangeSet::Change *removal,
    QQuickItemViewPrivate::ChangeResult *removeResult) {
  self->removeItem(item, *removal, removeResult);
}

//  void QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(FxViewItem
//      *item, ChangeResult *removeResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePosEP10FxViewItemPNS_12ChangeResultE(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    QQuickItemViewPrivate::ChangeResult *removeResult) {
  self->updateSizeChangesBeforeVisiblePos(item, removeResult);
}

//  void QQuickItemViewPrivate::repositionFirstItem(FxViewItem
//      *prevVisibleItemsFirst, qreal prevVisibleItemsFirstPos, FxViewItem
//      *prevFirstVisible, ChangeResult *insertionResult, ChangeResult
//      *removalResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate19repositionFirstItemEP10FxViewItemdS1_PNS_12ChangeResultES3_(
    QQuickItemViewPrivate *self,
    FxViewItem *prevVisibleItemsFirst,
    qreal prevVisibleItemsFirstPos,
    FxViewItem *prevFirstVisible,
    QQuickItemViewPrivate::ChangeResult *insertionResult,
    QQuickItemViewPrivate::ChangeResult *removalResult) {
  self->repositionFirstItem(
      prevVisibleItemsFirst,
      prevVisibleItemsFirstPos,
      prevFirstVisible,
      insertionResult,
      removalResult);
}

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewPrivate::createTransitioner()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate18createTransitionerEv(
    QQuickItemViewPrivate *self) {
  self->createTransitioner();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewPrivate::prepareVisibleItemTransitions()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate29prepareVisibleItemTransitionsEv(
    QQuickItemViewPrivate *self) {
  self->prepareVisibleItemTransitions();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickItemViewPrivate::prepareNonVisibleItemTransition(FxViewItem
//      *item, const QRectF &viewBounds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate31prepareNonVisibleItemTransitionEP10FxViewItemRK6QRectF(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    const QRectF *viewBounds) {
  return self->prepareNonVisibleItemTransition(item, *viewBounds);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewPrivate::viewItemTransitionFinished(QQuickItemViewTran
//      sitionableItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem(
    QQuickItemViewPrivate *self,
    QQuickItemViewTransitionableItem *item) {
  self->viewItemTransitionFinished(item);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  void QQuickItemViewPrivate::checkVisible() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickItemViewPrivate12checkVisibleEv(
    const QQuickItemViewPrivate *self) {
  self->checkVisible();
}

//  void QQuickItemViewPrivate::showVisibleItems() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickItemViewPrivate16showVisibleItemsEv(
    const QQuickItemViewPrivate *self) {
  self->showVisibleItems();
}

//  void QQuickItemViewPrivate::markExtentsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate16markExtentsDirtyEv(
    QQuickItemViewPrivate *self) {
  self->markExtentsDirty();
}

//  bool QQuickItemViewPrivate::hasPendingChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate17hasPendingChangesEv(
    const QQuickItemViewPrivate *self) {
  return self->hasPendingChanges();
}

//  void QQuickItemViewPrivate::forceLayoutPolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate17forceLayoutPolishEv(
    QQuickItemViewPrivate *self) {
  self->forceLayoutPolish();
}

//  void QQuickItemViewPrivate::releaseVisibleItems(QQmlInstanceModel::Reusab
//      leFlag reusableFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate19releaseVisibleItemsEN17QQmlInstanceModel12ReusableFlagE(
    QQuickItemViewPrivate *self,
    QQmlInstanceModel::ReusableFlag reusableFlag) {
  self->releaseVisibleItems(reusableFlag);
}

//  QQuickItemViewAttached *QQuickItemViewPrivate::getAttachedObject(const
//      QObject *a0) const
extern "C" Q_DECL_EXPORT
QQuickItemViewAttached *ritual_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObject(
    const QQuickItemViewPrivate *self,
    const QObject *a0) {
  return self->getAttachedObject(a0);
}

//  void QQuickItemViewPrivate::storeFirstVisibleItemPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate29storeFirstVisibleItemPositionEv(
    QQuickItemViewPrivate *self) {
  self->storeFirstVisibleItemPosition();
}

//  Qt::Orientation QQuickItemViewPrivate::layoutOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK21QQuickItemViewPrivate17layoutOrientationEv(
    const QQuickItemViewPrivate *self) {
  return self->layoutOrientation();
}

//  bool QQuickItemViewPrivate::isContentFlowReversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate21isContentFlowReversedEv(
    const QQuickItemViewPrivate *self) {
  return self->isContentFlowReversed();
}

//  qreal QQuickItemViewPrivate::positionAt(int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate10positionAtEi(
    const QQuickItemViewPrivate *self,
    int index) {
  return self->positionAt(index);
}

//  qreal QQuickItemViewPrivate::endPositionAt(int index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate13endPositionAtEi(
    const QQuickItemViewPrivate *self,
    int index) {
  return self->endPositionAt(index);
}

//  qreal QQuickItemViewPrivate::originPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate14originPositionEv(
    const QQuickItemViewPrivate *self) {
  return self->originPosition();
}

//  qreal QQuickItemViewPrivate::lastPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate12lastPositionEv(
    const QQuickItemViewPrivate *self) {
  return self->lastPosition();
}

//  qreal QQuickItemViewPrivate::headerSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate10headerSizeEv(
    const QQuickItemViewPrivate *self) {
  return self->headerSize();
}

//  qreal QQuickItemViewPrivate::footerSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickItemViewPrivate10footerSizeEv(
    const QQuickItemViewPrivate *self) {
  return self->footerSize();
}

//  bool QQuickItemViewPrivate::showHeaderForIndex(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate18showHeaderForIndexEi(
    const QQuickItemViewPrivate *self,
    int index) {
  return self->showHeaderForIndex(index);
}

//  bool QQuickItemViewPrivate::showFooterForIndex(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate18showFooterForIndexEi(
    const QQuickItemViewPrivate *self,
    int index) {
  return self->showFooterForIndex(index);
}

//  void QQuickItemViewPrivate::updateHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12updateHeaderEv(
    QQuickItemViewPrivate *self) {
  self->updateHeader();
}

//  void QQuickItemViewPrivate::updateFooter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12updateFooterEv(
    QQuickItemViewPrivate *self) {
  self->updateFooter();
}

//  bool QQuickItemViewPrivate::hasStickyHeader() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv(
    const QQuickItemViewPrivate *self) {
  return self->hasStickyHeader();
}

//  bool QQuickItemViewPrivate::hasStickyFooter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate15hasStickyFooterEv(
    const QQuickItemViewPrivate *self) {
  return self->hasStickyFooter();
}

//  void QQuickItemViewPrivate::createHighlight(bool onDestruction)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate15createHighlightEb(
    QQuickItemViewPrivate *self,
    bool onDestruction) {
  self->createHighlight(onDestruction);
}

//  void QQuickItemViewPrivate::updateHighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate15updateHighlightEv(
    QQuickItemViewPrivate *self) {
  self->updateHighlight();
}

//  void QQuickItemViewPrivate::resetHighlightPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate22resetHighlightPositionEv(
    QQuickItemViewPrivate *self) {
  self->resetHighlightPosition();
}

//  bool QQuickItemViewPrivate::movingFromHighlight()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate19movingFromHighlightEv(
    QQuickItemViewPrivate *self) {
  return self->movingFromHighlight();
}

//  void QQuickItemViewPrivate::setPosition(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate11setPositionEd(
    QQuickItemViewPrivate *self,
    qreal pos) {
  self->setPosition(pos);
}

//  void QQuickItemViewPrivate::fixupPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate13fixupPositionEv(
    QQuickItemViewPrivate *self) {
  self->fixupPosition();
}

//  bool QQuickItemViewPrivate::addVisibleItems(qreal fillFrom, qreal fillTo,
//      qreal bufferFrom, qreal bufferTo, bool doBuffer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate15addVisibleItemsEddddb(
    QQuickItemViewPrivate *self,
    qreal fillFrom,
    qreal fillTo,
    qreal bufferFrom,
    qreal bufferTo,
    bool doBuffer) {
  return self->addVisibleItems(
      fillFrom,
      fillTo,
      bufferFrom,
      bufferTo,
      doBuffer);
}

//  bool QQuickItemViewPrivate::removeNonVisibleItems(qreal bufferFrom, qreal
//      bufferTo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickItemViewPrivate21removeNonVisibleItemsEdd(
    QQuickItemViewPrivate *self,
    qreal bufferFrom,
    qreal bufferTo) {
  return self->removeNonVisibleItems(bufferFrom, bufferTo);
}

//  void QQuickItemViewPrivate::visibleItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate19visibleItemsChangedEv(
    QQuickItemViewPrivate *self) {
  self->visibleItemsChanged();
}

//  FxViewItem *QQuickItemViewPrivate::newViewItem(int index, QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
FxViewItem *ritual_ZN21QQuickItemViewPrivate11newViewItemEiP10QQuickItem(
    QQuickItemViewPrivate *self,
    int index,
    QQuickItem *item) {
  return self->newViewItem(index, item);
}

//  void QQuickItemViewPrivate::repositionItemAt(FxViewItem *item, int index,
//      qreal sizeBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate16repositionItemAtEP10FxViewItemid(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    int index,
    qreal sizeBuffer) {
  self->repositionItemAt(item, index, sizeBuffer);
}

//  void QQuickItemViewPrivate::repositionPackageItemAt(QQuickItem *item, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate23repositionPackageItemAtEP10QQuickItemi(
    QQuickItemViewPrivate *self,
    QQuickItem *item,
    int index) {
  self->repositionPackageItemAt(item, index);
}

//  void QQuickItemViewPrivate::resetFirstItemPosition(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate22resetFirstItemPositionEd(
    QQuickItemViewPrivate *self,
    qreal pos) {
  self->resetFirstItemPosition(pos);
}

//  void QQuickItemViewPrivate::adjustFirstItem(qreal forwards, qreal
//      backwards, int changeBeforeVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate15adjustFirstItemEddi(
    QQuickItemViewPrivate *self,
    qreal forwards,
    qreal backwards,
    int changeBeforeVisible) {
  self->adjustFirstItem(forwards, backwards, changeBeforeVisible);
}

//  void QQuickItemViewPrivate::layoutVisibleItems(int fromModelIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate18layoutVisibleItemsEi(
    QQuickItemViewPrivate *self,
    int fromModelIndex) {
  self->layoutVisibleItems(fromModelIndex);
}

//  void QQuickItemViewPrivate::changedVisibleIndex(int newIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate19changedVisibleIndexEi(
    QQuickItemViewPrivate *self,
    int newIndex) {
  self->changedVisibleIndex(newIndex);
}

//  bool QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(int a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemovedIndexEi(
    const QQuickItemViewPrivate *self,
    int a0) {
  return self->needsRefillForAddedOrRemovedIndex(a0);
}

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewPrivate::translateAndTransitionItemsAfter(int
//      afterIndex, const ChangeResult &insertionResult, const ChangeResult
//      &removalResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate32translateAndTransitionItemsAfterEiRKNS_12ChangeResultES2_(
    QQuickItemViewPrivate *self,
    int afterIndex,
    const QQuickItemViewPrivate::ChangeResult *insertionResult,
    const QQuickItemViewPrivate::ChangeResult *removalResult) {
  self->translateAndTransitionItemsAfter(
      afterIndex,
      *insertionResult,
      *removalResult);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  void QQuickItemViewPrivate::initializeViewItem(FxViewItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxViewItem(
    QQuickItemViewPrivate *self,
    FxViewItem *a0) {
  self->initializeViewItem(a0);
}

//  void QQuickItemViewPrivate::initializeCurrentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate21initializeCurrentItemEv(
    QQuickItemViewPrivate *self) {
  self->initializeCurrentItem();
}

//  void QQuickItemViewPrivate::updateSectionCriteria()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv(
    QQuickItemViewPrivate *self) {
  self->updateSectionCriteria();
}

//  void QQuickItemViewPrivate::updateSections()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate14updateSectionsEv(
    QQuickItemViewPrivate *self) {
  self->updateSections();
}

//  void QQuickItemViewPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickItemViewPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(item, *change, *a2);
}

//  QQuickItemViewPrivate as the QQuickItemViewTransitionChangeListener it is
//      built on
extern "C" Q_DECL_EXPORT
QQuickItemViewTransitionChangeListener *ritual_cast_QQuickItemViewPrivate_QQuickItemViewTransitionChangeListener(
    QQuickItemViewPrivate *self) {
  return static_cast<QQuickItemViewTransitionChangeListener *>(self);
}

//  QQuickItemViewPrivate as the QAnimationJobChangeListener it is built on
extern "C" Q_DECL_EXPORT
QAnimationJobChangeListener *ritual_cast_QQuickItemViewPrivate_QAnimationJobChangeListener(
    QQuickItemViewPrivate *self) {
  return static_cast<QAnimationJobChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickItemViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemViewPrivate(
    QQuickItemViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemViewPrivate *>(self)->take(key, call);
}

//  void QQuickItemViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate4initEv(
    QQuickItemViewPrivate *self) {
  self->QQuickItemViewPrivate::init();
}

//  void QQuickItemViewPrivate::clear(bool onDestruction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate5clearEb(
    QQuickItemViewPrivate *self,
    bool onDestruction) {
  self->QQuickItemViewPrivate::clear(onDestruction);
}

//  void QQuickItemViewPrivate::updateViewport()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate14updateViewportEv(
    QQuickItemViewPrivate *self) {
  self->QQuickItemViewPrivate::updateViewport();
}

//  void QQuickItemViewPrivate::animationFinished(QAbstractAnimationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate17animationFinishedEP21QAbstractAnimationJob(
    QQuickItemViewPrivate *self,
    QAbstractAnimationJob *a0) {
  self->QQuickItemViewPrivate::animationFinished(a0);
}

//  void QQuickItemViewPrivate::initializeComponentItem(QQuickItem *a0) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QQuickItemViewPrivate23initializeComponentItemEP10QQuickItem(
    const QQuickItemViewPrivate *self,
    QQuickItem *a0) {
  self->QQuickItemViewPrivate::initializeComponentItem(a0);
}

//  void QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(FxViewItem
//      *item, ChangeResult *removeResult)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate33updateSizeChangesBeforeVisiblePosEP10FxViewItemPNS_12ChangeResultE(
    QQuickItemViewPrivate *self,
    FxViewItem *item,
    QQuickItemViewPrivate::ChangeResult *removeResult) {
  self->QQuickItemViewPrivate::updateSizeChangesBeforeVisiblePos(
      item,
      removeResult);
}

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewPrivate::viewItemTransitionFinished(QQuickItemViewTran
//      sitionableItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem(
    QQuickItemViewPrivate *self,
    QQuickItemViewTransitionableItem *item) {
  self->QQuickItemViewPrivate::viewItemTransitionFinished(item);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  QQuickItemViewAttached *QQuickItemViewPrivate::getAttachedObject(const
//      QObject *a0) const
extern "C" Q_DECL_EXPORT
QQuickItemViewAttached *ritual_own_ZNK21QQuickItemViewPrivate17getAttachedObjectEPK7QObject(
    const QQuickItemViewPrivate *self,
    const QObject *a0) {
  return self->QQuickItemViewPrivate::getAttachedObject(a0);
}

//  bool QQuickItemViewPrivate::hasStickyHeader() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QQuickItemViewPrivate15hasStickyHeaderEv(
    const QQuickItemViewPrivate *self) {
  return static_cast<const OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::hasStickyHeader();
}

//  bool QQuickItemViewPrivate::hasStickyFooter() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QQuickItemViewPrivate15hasStickyFooterEv(
    const QQuickItemViewPrivate *self) {
  return static_cast<const OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::hasStickyFooter();
}

//  bool QQuickItemViewPrivate::movingFromHighlight()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickItemViewPrivate19movingFromHighlightEv(
    QQuickItemViewPrivate *self) {
  return static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::movingFromHighlight();
}

//  void QQuickItemViewPrivate::visibleItemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate19visibleItemsChangedEv(
    QQuickItemViewPrivate *self) {
  static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::visibleItemsChanged();
}

//  bool QQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(int a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QQuickItemViewPrivate33needsRefillForAddedOrRemovedIndexEi(
    const QQuickItemViewPrivate *self,
    int a0) {
  return static_cast<const OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::needsRefillForAddedOrRemovedIndex(
      a0);
}

//  void QQuickItemViewPrivate::initializeViewItem(FxViewItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate18initializeViewItemEP10FxViewItem(
    QQuickItemViewPrivate *self,
    FxViewItem *a0) {
  static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::initializeViewItem(
      a0);
}

//  void QQuickItemViewPrivate::initializeCurrentItem()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate21initializeCurrentItemEv(
    QQuickItemViewPrivate *self) {
  static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::initializeCurrentItem();
}

//  void QQuickItemViewPrivate::updateSectionCriteria()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate21updateSectionCriteriaEv(
    QQuickItemViewPrivate *self) {
  static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::updateSectionCriteria();
}

//  void QQuickItemViewPrivate::updateSections()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickItemViewPrivate14updateSectionsEv(
    QQuickItemViewPrivate *self) {
  static_cast<OwnQQuickItemViewPrivate *>(self)->OwnQQuickItemViewPrivate::updateSections();
}

#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_itemview)
