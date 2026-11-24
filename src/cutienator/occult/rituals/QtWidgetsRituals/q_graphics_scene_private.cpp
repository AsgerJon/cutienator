//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <private/qgraphicsscene_p.h>
#include <private/qgraphicsscenebsptreeindex_p.h>
#include <private/qgraphicssceneindex_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include "private/qgesturemanager_p.h"
#include "private/qstandardgestures_p.h"
#include "private/qwidget_p.h"
#include "private/qgesture_p.h"
#if QT_CONFIG(graphicsview)
#include "private/qgraphicsitem_p.h"
#include "qgraphicsitem.h"
#endif
#include "private/qevent_p.h"
#include "private/qapplication_p.h"
#include "private/qwidgetwindow_p.h"
#include "qgesture.h"
#include "qevent.h"
#ifdef Q_OS_HARMONY
#include "qohosgesturerecognizer_p.h"
#endif
#ifdef Q_OS_MACOS
#include "qmacgesturerecognizer_p.h"
#endif
#include "qdebug.h"
#include <QtCore/QLoggingCategory>
#include <QtCore/QVarLengthArray>
#include "qplatformdefs.h"
#include "qabstracteventdispatcher.h"
#include "qapplication.h"
#include "qclipboard.h"
#include "qcursor.h"
#include "qdir.h"
#include "qevent.h"
#include "qfile.h"
#include "qfileinfo.h"
#if QT_CONFIG(graphicsview)
#include "qgraphicsscene.h"
#include <QtWidgets/qgraphicsproxywidget.h>
#endif
#include "qhash.h"
#include "qset.h"
#include "qlayout.h"
#include "qpixmapcache.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qstylefactory.h"
#if QT_CONFIG(tooltip)
#include "qtooltip.h"
#endif
#include "qtranslator.h"
#include "qvariant.h"
#include "qwidget.h"
#if QT_CONFIG(draganddrop)
#include <private/qdnd_p.h>
#endif
#include "private/qguiapplication_p.h"
#include "qdebug.h"
#if QT_CONFIG(style_stylesheet)
#include "private/qstylesheetstyle_p.h"
#endif
#include "private/qstyle_p.h"
#if QT_CONFIG(messagebox)
#include "qmessagebox.h"
#endif
#include "qwidgetwindow_p.h"
#include <QtGui/qstylehints.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <qpa/qplatformtheme.h>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/QWhatsThis>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible_base.h>
#include "private/qaccessiblewidgetfactory_p.h"
#endif
#include "private/qkeymapper_p.h"
#include <qthread.h>
#include <private/qthread_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <private/qfont_p.h>
#if QT_CONFIG(action)
#include <private/qaction_p.h>
#endif
#include <stdlib.h>
#include "qapplication_p.h"
#include "qwidget_p.h"
#include "qgesture.h"
#include "private/qgesturemanager_p.h"
#include <qpa/qplatformfontdatabase.h>
#include "qdatetime.h"
#include <qpa/qplatformwindow.h>
#ifdef Q_OS_MACOS
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <algorithm>
#include <iterator>
#include "qglobal.h"
#include <QtCore/qdebug.h>
#include <QtCore/qnumeric.h>
#include "qgraphicswidget_p.h"
#include "qgraphicslayoutitem_p.h"
#include "qgraphicslayout.h"
#include "qgraphicsscene_p.h"
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/QStyleOptionTitleBar>
#include <QtWidgets/QGraphicsSceneMouseEvent>
#include "qgraphicseffect_p.h"
#include "private/qgraphicsitem_p.h"
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <private/qdrawhelper_p.h>
#include "qdebug.h"
#include "qgraphicsscene.h"
#include "qgraphicsitem_p.h"
#include "qgraphicsscene_p.h"
#include "qgraphicswidget.h"
#include "qgraphicssceneindex_p.h"
#include "qgraphicsscenebsptreeindex_p.h"
#include <QtGui/qpainterpath.h>
#include "qgraphicsscene.h"
#include "qgraphicsitem.h"
#include "qgraphicsitem_p.h"
#include "qgraphicslayout.h"
#include "qgraphicsscene_p.h"
#include "qgraphicssceneevent.h"
#include "qgraphicsview.h"
#include "qgraphicsview_p.h"
#include "qgraphicswidget.h"
#include "qgraphicswidget_p.h"
#include "qgraphicssceneindex_p.h"
#include "qgraphicsscenebsptreeindex_p.h"
#include "qgraphicsscenelinearindex_p.h"
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qmath.h>
#include <QtCore/qrect.h>
#include <QtCore/qset.h>
#include <QtCore/qstack.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/QMetaMethod>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmapcache.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qpointingdevice.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtGui/qtransform.h>
#include <QtGui/qinputmethod.h>
#include <private/qapplication_p.h>
#include <private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <private/qobject_p.h>
#if QT_CONFIG(graphicseffect)
#include <private/qgraphicseffect_p.h>
#endif
#include <private/qgesturemanager_p.h>
#include <private/qpathclipper_p.h>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 412, as _ZN26QGraphicsSceneBspTreeIndexC1EP14QGraphicsScene
inline QGraphicsSceneBspTreeIndex::QGraphicsSceneBspTreeIndex(QGraphicsScene *scene)
    : QGraphicsSceneIndex(*new QGraphicsSceneBspTreeIndexPrivate(scene), scene)
{

}

//  from src/widgets/kernel/qgesturemanager.cpp, line 140, as _ZN15QGestureManager21cleanupCachedGesturesEP7QObjectN2Qt11GestureTypeE
#if !defined(QT_NO_GESTURES)
inline void QGestureManager::cleanupCachedGestures(QObject *target, Qt::GestureType type)
{
    const auto iter = m_objectGestures.find({target, type});
    if (iter == m_objectGestures.end())
        return;

    const QList<QGesture *> &gestures = iter.value();
    for (auto &e : m_obsoleteGestures) {
        for (QGesture *g : gestures)
            e -= g;
    }
    for (QGesture *g : gestures) {
        m_deletedRecognizers.remove(g);
        m_gestureToRecognizer.remove(g);
        m_maybeGestures.remove(g);
        m_activeGestures.remove(g);
        m_gestureOwners.remove(g);
        m_gestureTargets.remove(g);
        m_gesturesToDelete.insert(g);
    }

    m_objectGestures.erase(iter);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qapplication.cpp, line 3952, as _ZN15QGestureManager8instanceENS_16InstanceCreationE
#if !defined(QT_NO_GESTURES)
inline QGestureManager* QGestureManager::instance(InstanceCreation ic)
{
    QApplicationPrivate *qAppPriv = QApplicationPrivate::instance();
    if (!qAppPriv)
        return nullptr;
    if (!qAppPriv->gestureManager && ic == ForceCreation)
        qAppPriv->gestureManager = new QGestureManager(qApp);
    return qAppPriv->gestureManager;
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 719, as _ZN22QGraphicsWidgetPrivate30fixFocusChainBeforeReparentingEP15QGraphicsWidgetP14QGraphicsSceneS3_
inline void QGraphicsWidgetPrivate::fixFocusChainBeforeReparenting(QGraphicsWidget *newParent, QGraphicsScene *oldScene, QGraphicsScene *newScene)
{
    Q_Q(QGraphicsWidget);
    Q_ASSERT(focusNext && focusPrev);

    if (q_ptr->isPanel()) {
        // panels are never a part of their parent's or ancestors' focus
        // chains. so reparenting a panel is easy; there's nothing to
        // do.
        return;
    }

    // we're not a panel, so find the first widget in the focus chain
    // (this), and the last (this, or the last widget that is still
    // a descendent of this). also find the widgets that currently /
    // before reparenting point to this widgets' focus chain.
    QGraphicsWidget *focusFirst = q;
    QGraphicsWidget *focusBefore = focusPrev;
    QGraphicsWidget *focusLast = focusFirst;
    QGraphicsWidget *focusAfter = focusNext;
    do {
        if (!q->isAncestorOf(focusAfter))
            break;
        focusLast = focusAfter;
    } while ((focusAfter = focusAfter->d_func()->focusNext));

    if (!parent && oldScene && oldScene != newScene && oldScene->d_func()->tabFocusFirst == q) {
        // detach from old scene's top level focus chain.
        oldScene->d_func()->tabFocusFirst = (focusAfter != q) ? focusAfter : nullptr;
    }

    // detach from current focus chain; skip this widget subtree.
    focusBefore->d_func()->focusNext = focusAfter;
    if (focusAfter)
        focusAfter->d_func()->focusPrev = focusBefore;

    if (newParent) {
        // attach to new parent's focus chain as the last element
        // in its chain.
        QGraphicsWidget *newFocusFirst = newParent;
        QGraphicsWidget *newFocusLast = newFocusFirst;
        QGraphicsWidget *newFocusAfter = newFocusFirst->d_func()->focusNext;
        do {
            if (!newParent->isAncestorOf(newFocusAfter))
                break;
            newFocusLast = newFocusAfter;
        } while ((newFocusAfter = newFocusAfter->d_func()->focusNext));

        newFocusLast->d_func()->focusNext = q;
        focusLast->d_func()->focusNext = newFocusAfter;
        if (newFocusAfter)
            newFocusAfter->d_func()->focusPrev = focusLast;
        focusPrev = newFocusLast;
    } else {
        // no new parent, so just link up our own prev->last widgets.
        focusPrev = focusLast;
        focusLast->d_func()->focusNext = q;
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 711, as _ZNK22QGraphicsWidgetPrivate13hasDecorationEv
inline bool QGraphicsWidgetPrivate::hasDecoration() const
{
    return (windowFlags & Qt::Window) && (windowFlags & Qt::WindowTitleHint);
}

//  from src/widgets/effects/qgraphicseffect.cpp, line 355, as _ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16InvalidateReasonE
inline void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason reason) const
{
    if (m_cachedMode != QGraphicsEffect::PadToEffectiveBoundingRect
        && (reason == EffectRectChanged
            || (reason == TransformChanged && m_cachedSystem == Qt::LogicalCoordinates))) {
        return;
    }

    QPixmapCache::remove(m_cacheKey);
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 327, as _ZN19QGraphicsSceneIndexC2ER26QGraphicsSceneIndexPrivateP14QGraphicsScene
inline QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsSceneIndexPrivate &dd, QGraphicsScene *scene)
    : QObject(dd, scene)
{
    d_func()->init();
}

//  from src/widgets/graphicsview/qgraphicsscenebsptreeindex.cpp, line 67, as _ZN33QGraphicsSceneBspTreeIndexPrivateC1EP14QGraphicsScene
inline QGraphicsSceneBspTreeIndexPrivate::QGraphicsSceneBspTreeIndexPrivate(QGraphicsScene *scene)
    : QGraphicsSceneIndexPrivate(scene),
    bspTreeDepth(0),
    restartIndexTimer(false),
    regenerateIndex(true),
    lastItemCount(0),
    purgePending(false),
    sortCacheEnabled(false),
    updatingSortCache(false)
{
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 248, as _ZN21QGraphicsScenePrivateC1Ev
inline QGraphicsScenePrivate::QGraphicsScenePrivate()
    : indexMethod(QGraphicsScene::BspTreeIndex),
      index(nullptr),
      lastItemCount(0),
      hasSceneRect(false),
      dirtyGrowingItemsBoundingRect(true),
      updateAll(false),
      calledEmitUpdated(false),
      processDirtyItemsEmitted(false),
      needSortTopLevelItems(true),
      holesInTopLevelSiblingIndex(false),
      topLevelSequentialOrdering(true),
      scenePosDescendantsUpdatePending(false),
      stickyFocus(false),
      hasFocus(false),
      lastMouseGrabberItemHasImplicitMouseGrab(false),
      allItemsIgnoreHoverEvents(true),
      allItemsUseDefaultCursor(true),
      painterStateProtection(true),
      sortCacheEnabled(false),
      allItemsIgnoreTouchEvents(true),
      focusOnTouch(true),
      minimumRenderSize(0.0),
      selectionChanging(0),
      rectAdjust(2),
      focusItem(nullptr),
      lastFocusItem(nullptr),
      passiveFocusItem(nullptr),
      tabFocusFirst(nullptr),
      activePanel(nullptr),
      lastActivePanel(nullptr),
      activationRefCount(0),
      childExplicitActivation(0),
      lastMouseGrabberItem(nullptr),
      dragDropItem(nullptr),
      enterWidget(nullptr),
      lastDropAction(Qt::IgnoreAction),
      style(nullptr)
{
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 310, as _ZN21QGraphicsScenePrivate3getEP14QGraphicsScene
inline QGraphicsScenePrivate *QGraphicsScenePrivate::get(QGraphicsScene *q)
{
    return q->d_func();
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 315, as _ZN21QGraphicsScenePrivate14_q_emitUpdatedEv
inline void QGraphicsScenePrivate::_q_emitUpdated()
{
    Q_Q(QGraphicsScene);
    calledEmitUpdated = false;

    if (dirtyGrowingItemsBoundingRect) {
        if (!hasSceneRect) {
            const QRectF oldGrowingItemsBoundingRect = growingItemsBoundingRect;
            growingItemsBoundingRect |= q->itemsBoundingRect();
            if (oldGrowingItemsBoundingRect != growingItemsBoundingRect)
                emit q->sceneRectChanged(growingItemsBoundingRect);
        }
        dirtyGrowingItemsBoundingRect = false;
    }

    // Ensure all views are connected if anything is connected. This disables
    // the optimization that items send updates directly to the views, but it
    // needs to happen in order to keep compatibility with the behavior from
    // Qt 4.4 and backward.
    if (isSignalConnected(changedSignalIndex)) {
        for (auto view : std::as_const(views)) {
            if (!view->d_func()->connectedToScene) {
                view->d_func()->connectedToScene = true;
                q->connect(q, SIGNAL(changed(QList<QRectF>)),
                           view, SLOT(updateScene(QList<QRectF>)));
            }
        }
    } else {
        if (views.isEmpty()) {
            updateAll = false;
            return;
        }
        for (auto view : std::as_const(views))
            view->d_func()->processPendingUpdates();
        // It's important that we update all views before we dispatch, hence two for-loops.
        for (auto view : std::as_const(views))
            view->d_func()->dispatchPendingUpdateRequests();
        return;
    }

    // Notify the changes to anybody interested.
    QList<QRectF> oldUpdatedRects;
    if (updateAll) {
        oldUpdatedRects << q->sceneRect();
    } else {
        // Switch to a ranged constructor in Qt 6...
        oldUpdatedRects.reserve(int(updatedRects.size()));
        std::copy(updatedRects.cbegin(), updatedRects.cend(),
                  std::back_inserter(oldUpdatedRects));
    }

    updateAll = false;
    updatedRects.clear();
    emit q->changed(oldUpdatedRects);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 376, as _ZN21QGraphicsScenePrivate20registerTopLevelItemEP13QGraphicsItem
inline void QGraphicsScenePrivate::registerTopLevelItem(QGraphicsItem *item)
{
    ensureSequentialTopLevelSiblingIndexes();
    needSortTopLevelItems = true; // ### maybe false
    item->d_ptr->siblingIndex = topLevelItems.size();
    topLevelItems.append(item);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 389, as _ZN21QGraphicsScenePrivate22unregisterTopLevelItemEP13QGraphicsItem
inline void QGraphicsScenePrivate::unregisterTopLevelItem(QGraphicsItem *item)
{
    if (!holesInTopLevelSiblingIndex)
        holesInTopLevelSiblingIndex = item->d_ptr->siblingIndex != topLevelItems.size() - 1;
    if (topLevelSequentialOrdering && !holesInTopLevelSiblingIndex)
        topLevelItems.removeAt(item->d_ptr->siblingIndex);
    else
        topLevelItems.removeOne(item);
    // NB! Do not use topLevelItems.removeAt(item->d_ptr->siblingIndex) because
    // the item is not guaranteed to be at the index after the list is sorted
    // (see ensureSortedTopLevelItems()).
    item->d_ptr->siblingIndex = -1;
    if (topLevelSequentialOrdering)
        topLevelSequentialOrdering = !holesInTopLevelSiblingIndex;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 408, as _ZN21QGraphicsScenePrivate14_q_polishItemsEv
inline void QGraphicsScenePrivate::_q_polishItems()
{
    if (unpolishedItems.isEmpty())
        return;

    const QVariant booleanTrueVariant(true);
    QGraphicsItem *item = nullptr;
    QGraphicsItemPrivate *itemd = nullptr;
    const int oldUnpolishedCount = unpolishedItems.size();

    for (int i = 0; i < oldUnpolishedCount; ++i) {
        item = unpolishedItems.at(i);
        if (!item)
            continue;
        itemd = item->d_ptr.data();
        itemd->pendingPolish = false;
        if (!itemd->explicitlyHidden) {
            item->itemChange(QGraphicsItem::ItemVisibleChange, booleanTrueVariant);
            item->itemChange(QGraphicsItem::ItemVisibleHasChanged, booleanTrueVariant);
        }
        if (itemd->isWidget) {
            QEvent event(QEvent::Polish);
            QCoreApplication::sendEvent((QGraphicsWidget *)item, &event);
        }
    }

    if (unpolishedItems.size() == oldUnpolishedCount) {
        // No new items were added to the vector.
        unpolishedItems.clear();
    } else {
        // New items were appended; keep them and remove the old ones.
        unpolishedItems.remove(0, oldUnpolishedCount);
        unpolishedItems.squeeze();
        QMetaObject::invokeMethod(q_ptr, "_q_polishItems", Qt::QueuedConnection);
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 490, as _ZN21QGraphicsScenePrivate22setScenePosItemEnabledEP13QGraphicsItemb
inline void QGraphicsScenePrivate::setScenePosItemEnabled(QGraphicsItem *item, bool enabled)
{
    QGraphicsItem *p = item->d_ptr->parent;
    while (p) {
        p->d_ptr->scenePosDescendants = enabled;
        p = p->d_ptr->parent;
    }
    if (!enabled && !scenePosDescendantsUpdatePending) {
        scenePosDescendantsUpdatePending = true;
        QMetaObject::invokeMethod(q_func(), "_q_updateScenePosDescendants", Qt::QueuedConnection);
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 506, as _ZN21QGraphicsScenePrivate20registerScenePosItemEP13QGraphicsItem
inline void QGraphicsScenePrivate::registerScenePosItem(QGraphicsItem *item)
{
    scenePosItems.insert(item);
    setScenePosItemEnabled(item, true);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 515, as _ZN21QGraphicsScenePrivate22unregisterScenePosItemEP13QGraphicsItem
inline void QGraphicsScenePrivate::unregisterScenePosItem(QGraphicsItem *item)
{
    scenePosItems.remove(item);
    setScenePosItemEnabled(item, false);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 524, as _ZN21QGraphicsScenePrivate28_q_updateScenePosDescendantsEv
inline void QGraphicsScenePrivate::_q_updateScenePosDescendants()
{
    for (QGraphicsItem *item : std::as_const(scenePosItems)) {
        QGraphicsItem *p = item->d_ptr->parent;
        while (p) {
            p->d_ptr->scenePosDescendants = 1;
            p = p->d_ptr->parent;
        }
    }
    scenePosDescendantsUpdatePending = false;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1006, as _ZN21QGraphicsScenePrivate17clearMouseGrabberEv
inline void QGraphicsScenePrivate::clearMouseGrabber()
{
    if (!mouseGrabberItems.isEmpty())
        mouseGrabberItems.constFirst()->ungrabMouse();
    lastMouseGrabberItem = nullptr;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1083, as _ZN21QGraphicsScenePrivate26enableMouseTrackingOnViewsEv
inline void QGraphicsScenePrivate::enableMouseTrackingOnViews()
{
    for (QGraphicsView *view : std::as_const(views))
        view->viewport()->setMouseTracking(true);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1098, as _ZNK21QGraphicsScenePrivate15itemsAtPositionERK6QPointRK7QPointFP7QWidget
inline QList<QGraphicsItem *> QGraphicsScenePrivate::itemsAtPosition(const QPoint &screenPos,
                                                              const QPointF &scenePos,
                                                              QWidget *widget) const
{
    Q_Q(const QGraphicsScene);
    QGraphicsView *view = widget ? qobject_cast<QGraphicsView *>(widget->parentWidget()) : 0;
    if (!view)
        return q->items(scenePos, Qt::IntersectsItemShape, Qt::DescendingOrder, QTransform());

    const QRectF pointRect(QPointF(widget->mapFromGlobal(screenPos)), QSizeF(1, 1));
    if (!view->isTransformed())
        return q->items(pointRect, Qt::IntersectsItemShape, Qt::DescendingOrder);

    const QTransform viewTransform = view->viewportTransform();
    if (viewTransform.type() <= QTransform::TxScale) {
        return q->items(viewTransform.inverted().mapRect(pointRect), Qt::IntersectsItemShape,
                        Qt::DescendingOrder, viewTransform);
    }
    return q->items(viewTransform.inverted().map(pointRect), Qt::IntersectsItemShape,
                    Qt::DescendingOrder, viewTransform);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1123, as _ZN21QGraphicsScenePrivate32storeMouseButtonsForMouseGrabberEP24QGraphicsSceneMouseEvent
inline void QGraphicsScenePrivate::storeMouseButtonsForMouseGrabber(QGraphicsSceneMouseEvent *event)
{
    for (int i = 0x1; i <= 0x10; i <<= 1) {
        if (event->buttons() & i) {
            mouseGrabberButtonDownPos.insert(Qt::MouseButton(i),
                                             mouseGrabberItems.constLast()->d_ptr->genericMapFromScene(event->scenePos(),
                                                                                                       event->widget()));
            mouseGrabberButtonDownScenePos.insert(Qt::MouseButton(i), event->scenePos());
            mouseGrabberButtonDownScreenPos.insert(Qt::MouseButton(i), event->screenPos());
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5796, as _ZN21QGraphicsScenePrivate7addViewEP13QGraphicsView
inline void QGraphicsScenePrivate::addView(QGraphicsView *view)
{
    views << view;
#ifndef QT_NO_GESTURES
    for (auto it = grabbedGestures.constBegin();
              it != grabbedGestures.constEnd(); ++it)
        view->viewport()->grabGesture(it.key());
#endif
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5806, as _ZN21QGraphicsScenePrivate10removeViewEP13QGraphicsView
inline void QGraphicsScenePrivate::removeView(QGraphicsView *view)
{
    views.removeAll(view);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1139, as _ZN21QGraphicsScenePrivate23installSceneEventFilterEP13QGraphicsItemS1_
inline void QGraphicsScenePrivate::installSceneEventFilter(QGraphicsItem *watched, QGraphicsItem *filter)
{
    sceneEventFilters.insert(watched, filter);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1147, as _ZN21QGraphicsScenePrivate22removeSceneEventFilterEP13QGraphicsItemS1_
inline void QGraphicsScenePrivate::removeSceneEventFilter(QGraphicsItem *watched, QGraphicsItem *filter)
{
    if (!sceneEventFilters.contains(watched))
        return;

    QMultiMap<QGraphicsItem *, QGraphicsItem *>::Iterator it = sceneEventFilters.lowerBound(watched);
    QMultiMap<QGraphicsItem *, QGraphicsItem *>::Iterator end = sceneEventFilters.upperBound(watched);
    do {
        if (it.value() == filter)
            it = sceneEventFilters.erase(it);
        else
            ++it;
    } while (it != end);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1165, as _ZN21QGraphicsScenePrivate21filterDescendantEventEP13QGraphicsItemP6QEvent
inline bool QGraphicsScenePrivate::filterDescendantEvent(QGraphicsItem *item, QEvent *event)
{
    if (item && (item->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorFiltersChildEvents)) {
        QGraphicsItem *parent = item->parentItem();
        while (parent) {
            if (parent->d_ptr->filtersDescendantEvents && parent->sceneEventFilter(item, event))
                return true;
            if (!(parent->d_ptr->ancestorFlags & QGraphicsItemPrivate::AncestorFiltersChildEvents))
                return false;
            parent = parent->parentItem();
        }
    }
    return false;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1183, as _ZN21QGraphicsScenePrivate11filterEventEP13QGraphicsItemP6QEvent
inline bool QGraphicsScenePrivate::filterEvent(QGraphicsItem *item, QEvent *event)
{
    if (item && !sceneEventFilters.contains(item))
        return false;

    QMultiMap<QGraphicsItem *, QGraphicsItem *>::Iterator it = sceneEventFilters.lowerBound(item);
    QMultiMap<QGraphicsItem *, QGraphicsItem *>::Iterator end = sceneEventFilters.upperBound(item);
    while (it != end) {
        // ### The filterer and filteree might both be deleted.
        if (it.value()->sceneEventFilter(it.key(), event))
            return true;
        ++it;
    }
    return false;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 3748, as _ZNK21QGraphicsScenePrivate29itemAcceptsHoverEvents_helperEPK13QGraphicsItem
inline bool QGraphicsScenePrivate::itemAcceptsHoverEvents_helper(const QGraphicsItem *item) const
{
    return (item->d_ptr->acceptsHover
            || (item->d_ptr->isWidget
                && static_cast<const QGraphicsWidget *>(item)->d_func()->hasDecoration()))
           && !item->isBlockedByModalPanel();
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1238, as _ZN21QGraphicsScenePrivate18cloneDragDropEventEP27QGraphicsSceneDragDropEventS1_
inline void QGraphicsScenePrivate::cloneDragDropEvent(QGraphicsSceneDragDropEvent *dest,
                                               QGraphicsSceneDragDropEvent *source)
{
    dest->setWidget(source->widget());
    dest->setPos(source->pos());
    dest->setScenePos(source->scenePos());
    dest->setScreenPos(source->screenPos());
    dest->setButtons(source->buttons());
    dest->setModifiers(source->modifiers());
    dest->setPossibleActions(source->possibleActions());
    dest->setProposedAction(source->proposedAction());
    dest->setDropAction(source->dropAction());
    dest->setSource(source->source());
    dest->setMimeData(source->mimeData());
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4918, as _ZN21QGraphicsScenePrivate9markDirtyEP13QGraphicsItemRK6QRectFbbbbb
inline void QGraphicsScenePrivate::markDirty(QGraphicsItem *item, const QRectF &rect, bool invalidateChildren,
                                      bool force, bool ignoreOpacity, bool removingItemFromScene,
                                      bool updateBoundingRect)
{
    Q_ASSERT(item);
    if (updateAll)
        return;

    if (removingItemFromScene && !ignoreOpacity && !item->d_ptr->ignoreOpacity) {
        // If any of the item's ancestors ignore opacity, it means that the opacity
        // was set to 0 (and the update request has not yet been processed). That
        // also means that we have to ignore the opacity for the item itself; otherwise
        // things like: parent->setOpacity(0); scene->removeItem(child) won't work.
        // Note that we only do this when removing items from the scene. In all other
        // cases the ignoreOpacity bit propagates properly in processDirtyItems, but
        // since the item is removed immediately it won't be processed there.
        QGraphicsItem *p = item->d_ptr->parent;
        while (p) {
            if (p->d_ptr->ignoreOpacity) {
                item->d_ptr->ignoreOpacity = true;
                break;
            }
            p = p->d_ptr->parent;
        }
    }

    if (item->d_ptr->discardUpdateRequest(/*ignoreVisibleBit=*/force,
                                          /*ignoreDirtyBit=*/removingItemFromScene || invalidateChildren,
                                          /*ignoreOpacity=*/ignoreOpacity)) {
        if (item->d_ptr->dirty) {
            // The item is already marked as dirty and will be processed later. However,
            // we have to make sure ignoreVisible and ignoreOpacity are set properly;
            // otherwise things like: item->update(); item->hide() (force is now true)
            // won't work as expected.
            if (force)
                item->d_ptr->ignoreVisible = 1;
            if (ignoreOpacity)
                item->d_ptr->ignoreOpacity = 1;
        }
        return;
    }

    const bool fullItemUpdate = rect.isNull();
    if (!fullItemUpdate && rect.isEmpty())
        return;

    if (!processDirtyItemsEmitted) {
        QMetaMethod method = q_ptr->metaObject()->method(processDirtyItemsIndex);
        method.invoke(q_ptr, Qt::QueuedConnection);
//        QMetaObject::invokeMethod(q_ptr, "_q_processDirtyItems", Qt::QueuedConnection);
        processDirtyItemsEmitted = true;
    }

    if (removingItemFromScene) {
        // Note that this function can be called from the item's destructor, so
        // do NOT call any virtual functions on it within this block.
        if (isSignalConnected(changedSignalIndex) || views.isEmpty()) {
            // This block of code is kept for compatibility. Since 4.5, by default
            // QGraphicsView does not connect the signal and we use the below
            // method of delivering updates.
            q_func()->update();
            return;
        }

        for (auto view : std::as_const(views)) {
            QGraphicsViewPrivate *viewPrivate = view->d_func();
            QRect rect = item->d_ptr->paintedViewBoundingRects.value(viewPrivate->viewport);
            rect.translate(viewPrivate->dirtyScrollOffset);
            viewPrivate->updateRect(rect);
        }
        return;
    }

    bool hasNoContents = item->d_ptr->flags & QGraphicsItem::ItemHasNoContents;
    if (!hasNoContents) {
        item->d_ptr->dirty = 1;
        if (fullItemUpdate)
            item->d_ptr->fullUpdatePending = 1;
        else if (!item->d_ptr->fullUpdatePending)
            item->d_ptr->needsRepaint |= rect;
    } else if (item->d_ptr->graphicsEffect) {
        invalidateChildren = true;
    }

    if (invalidateChildren) {
        item->d_ptr->allChildrenDirty = 1;
        item->d_ptr->dirtyChildren = 1;
    }

    if (force)
        item->d_ptr->ignoreVisible = 1;
    if (ignoreOpacity)
        item->d_ptr->ignoreOpacity = 1;

    if (!updateBoundingRect)
        item->d_ptr->markParentDirty();
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1486, as _ZN21QGraphicsScenePrivate38ensureSequentialTopLevelSiblingIndexesEv
inline void QGraphicsScenePrivate::ensureSequentialTopLevelSiblingIndexes()
{
    if (!topLevelSequentialOrdering) {
        std::sort(topLevelItems.begin(), topLevelItems.end(), QGraphicsItemPrivate::insertionOrder);
        topLevelSequentialOrdering = true;
        needSortTopLevelItems = 1;
    }
    if (holesInTopLevelSiblingIndex) {
        holesInTopLevelSiblingIndex = 0;
        for (int i = 0; i < topLevelItems.size(); ++i)
            topLevelItems[i]->d_ptr->siblingIndex = i;
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1506, as _ZN21QGraphicsScenePrivate14setFont_helperERK5QFont
inline void QGraphicsScenePrivate::setFont_helper(const QFont &font)
{
    if (this->font == font && this->font.resolveMask() == font.resolveMask())
        return;
    updateFont(font);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1519, as _ZN21QGraphicsScenePrivate11resolveFontEv
inline void QGraphicsScenePrivate::resolveFont()
{
    QFont naturalFont = QApplication::font();
    naturalFont.setResolveMask(0);
    QFont resolvedFont = font.resolve(naturalFont);
    updateFont(resolvedFont);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1533, as _ZN21QGraphicsScenePrivate10updateFontERK5QFont
inline void QGraphicsScenePrivate::updateFont(const QFont &font)
{
    Q_Q(QGraphicsScene);

    // Update local font setting.
    this->font = font;

    // Resolve the fonts of all top-level widget items, or widget items
    // whose parent is not a widget.
    const auto items = q->items();
    for (QGraphicsItem *item : items) {
        if (!item->parentItem()) {
            // Resolvefont for an item is a noop operation, but
            // every item can be a widget, or can have a widget
            // childre.
            item->d_ptr->resolveFont(font.resolveMask());
        }
    }

    // Send the scene a FontChange event.
    QEvent event(QEvent::FontChange);
    QCoreApplication::sendEvent(q, &event);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1563, as _ZN21QGraphicsScenePrivate17setPalette_helperERK8QPalette
inline void QGraphicsScenePrivate::setPalette_helper(const QPalette &palette)
{
    if (this->palette == palette && this->palette.resolveMask() == palette.resolveMask())
        return;
    updatePalette(palette);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1576, as _ZN21QGraphicsScenePrivate14resolvePaletteEv
inline void QGraphicsScenePrivate::resolvePalette()
{
    QPalette naturalPalette = QGuiApplication::palette();
    naturalPalette.setResolveMask(0);
    QPalette resolvedPalette = palette.resolve(naturalPalette);
    updatePalette(resolvedPalette);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 1590, as _ZN21QGraphicsScenePrivate13updatePaletteERK8QPalette
inline void QGraphicsScenePrivate::updatePalette(const QPalette &palette)
{
    Q_Q(QGraphicsScene);

    // Update local palette setting.
    this->palette = palette;

    // Resolve the palettes of all top-level widget items, or widget items
    // whose parent is not a widget.
    const auto items = q->items();
    for (QGraphicsItem *item : items) {
        if (!item->parentItem()) {
            // ResolvePalette for an item is a noop operation, but
            // every item can be a widget, or can have a widget
            // children.
            item->d_ptr->resolvePalette(palette.resolveMask());
        }
    }

    // Send the scene a PaletteChange event.
    QEvent event(QEvent::PaletteChange);
    QCoreApplication::sendEvent(q, &event);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5811, as _ZN21QGraphicsScenePrivate24updateTouchPointsForItemEP13QGraphicsItemP11QTouchEvent
inline void QGraphicsScenePrivate::updateTouchPointsForItem(QGraphicsItem *item, QTouchEvent *touchEvent)
{
    const QTransform mapFromScene =
        item->d_ptr->genericMapFromSceneTransform(static_cast<const QWidget *>(touchEvent->target()));

    for (int i = 0; i < touchEvent->pointCount(); ++i) {
        auto &pt = touchEvent->point(i);
        QMutableEventPoint::setPosition(pt, mapFromScene.map(pt.scenePosition()));
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5822, as _ZN21QGraphicsScenePrivate23findClosestTouchPointIdERK7QPointF
inline int QGraphicsScenePrivate::findClosestTouchPointId(const QPointF &scenePos)
{
    int closestTouchPointId = -1;
    qreal closestDistance = qreal(0.);
    for (const QEventPoint &touchPoint : std::as_const(sceneCurrentTouchPoints)) {
        qreal distance = QLineF(scenePos, touchPoint.scenePosition()).length();
        if (closestTouchPointId == -1|| distance < closestDistance) {
            closestTouchPointId = touchPoint.id();
            closestDistance = distance;
        }
    }
    return closestTouchPointId;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 6033, as _ZN21QGraphicsScenePrivate24enableTouchEventsOnViewsEv
inline void QGraphicsScenePrivate::enableTouchEventsOnViews()
{
    for (QGraphicsView *view : std::as_const(views))
        view->viewport()->setAttribute(Qt::WA_AcceptTouchEvents, true);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 6039, as _ZN21QGraphicsScenePrivate35updateInputMethodSensitivityInViewsEv
inline void QGraphicsScenePrivate::updateInputMethodSensitivityInViews()
{
    for (auto view : std::as_const(views))
        view->d_func()->updateInputMethodSensitivity();
}
//  -----------------------------------------------------------------------

//  QGraphicsScene *QGraphicsScenePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN21QGraphicsScenePrivate6q_funcEv(
    QGraphicsScenePrivate *self) {
  return self->q_func();
}

//  const QGraphicsScene *QGraphicsScenePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsScene *ritual_ZNK21QGraphicsScenePrivate6q_funcEv(
    const QGraphicsScenePrivate *self) {
  return self->q_func();
}

//  QGraphicsScenePrivate::QGraphicsScenePrivate()
extern "C" Q_DECL_EXPORT
QGraphicsScenePrivate *ritual_ZN21QGraphicsScenePrivateC1Ev() {
  return new QGraphicsScenePrivate();
}

//  QGraphicsScenePrivate *QGraphicsScenePrivate::get(QGraphicsScene *q)
extern "C" Q_DECL_EXPORT
QGraphicsScenePrivate *ritual_ZN21QGraphicsScenePrivate3getEP14QGraphicsScene(
    QGraphicsScene *q) {
  return QGraphicsScenePrivate::get(q);
}

//  void QGraphicsScenePrivate::_q_emitUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate14_q_emitUpdatedEv(
    QGraphicsScenePrivate *self) {
  self->_q_emitUpdated();
}

//  void QGraphicsScenePrivate::registerTopLevelItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate20registerTopLevelItemEP13QGraphicsItem(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item) {
  self->registerTopLevelItem(item);
}

//  void QGraphicsScenePrivate::unregisterTopLevelItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate22unregisterTopLevelItemEP13QGraphicsItem(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item) {
  self->unregisterTopLevelItem(item);
}

//  void QGraphicsScenePrivate::_q_polishItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate14_q_polishItemsEv(
    QGraphicsScenePrivate *self) {
  self->_q_polishItems();
}

//  void QGraphicsScenePrivate::setScenePosItemEnabled(QGraphicsItem *item,
//      bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate22setScenePosItemEnabledEP13QGraphicsItemb(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    bool enabled) {
  self->setScenePosItemEnabled(item, enabled);
}

//  void QGraphicsScenePrivate::registerScenePosItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate20registerScenePosItemEP13QGraphicsItem(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item) {
  self->registerScenePosItem(item);
}

//  void QGraphicsScenePrivate::unregisterScenePosItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate22unregisterScenePosItemEP13QGraphicsItem(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item) {
  self->unregisterScenePosItem(item);
}

//  void QGraphicsScenePrivate::_q_updateScenePosDescendants()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate28_q_updateScenePosDescendantsEv(
    QGraphicsScenePrivate *self) {
  self->_q_updateScenePosDescendants();
}

//  void QGraphicsScenePrivate::clearMouseGrabber()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate17clearMouseGrabberEv(
    QGraphicsScenePrivate *self) {
  self->clearMouseGrabber();
}

//  void QGraphicsScenePrivate::enableMouseTrackingOnViews()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate26enableMouseTrackingOnViewsEv(
    QGraphicsScenePrivate *self) {
  self->enableMouseTrackingOnViews();
}

//  QList<QGraphicsItem *> QGraphicsScenePrivate::itemsAtPosition(const
//      QPoint &screenPos, const QPointF &scenePos, QWidget *widget) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK21QGraphicsScenePrivate15itemsAtPositionERK6QPointRK7QPointFP7QWidget(
    const QGraphicsScenePrivate *self,
    const QPoint *screenPos,
    const QPointF *scenePos,
    QWidget *widget) {
  return new QList<QGraphicsItem *>(
      self->itemsAtPosition(
          *screenPos,
          *scenePos,
          widget));
}

//  void QGraphicsScenePrivate::storeMouseButtonsForMouseGrabber(QGraphicsSce
//      neMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate32storeMouseButtonsForMouseGrabberEP24QGraphicsSceneMouseEvent(
    QGraphicsScenePrivate *self,
    QGraphicsSceneMouseEvent *event) {
  self->storeMouseButtonsForMouseGrabber(event);
}

//  void QGraphicsScenePrivate::addView(QGraphicsView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate7addViewEP13QGraphicsView(
    QGraphicsScenePrivate *self,
    QGraphicsView *view) {
  self->addView(view);
}

//  void QGraphicsScenePrivate::removeView(QGraphicsView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate10removeViewEP13QGraphicsView(
    QGraphicsScenePrivate *self,
    QGraphicsView *view) {
  self->removeView(view);
}

//  void QGraphicsScenePrivate::installSceneEventFilter(QGraphicsItem
//      *watched, QGraphicsItem *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate23installSceneEventFilterEP13QGraphicsItemS1_(
    QGraphicsScenePrivate *self,
    QGraphicsItem *watched,
    QGraphicsItem *filter) {
  self->installSceneEventFilter(watched, filter);
}

//  void QGraphicsScenePrivate::removeSceneEventFilter(QGraphicsItem
//      *watched, QGraphicsItem *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate22removeSceneEventFilterEP13QGraphicsItemS1_(
    QGraphicsScenePrivate *self,
    QGraphicsItem *watched,
    QGraphicsItem *filter) {
  self->removeSceneEventFilter(watched, filter);
}

//  bool QGraphicsScenePrivate::filterDescendantEvent(QGraphicsItem *item,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGraphicsScenePrivate21filterDescendantEventEP13QGraphicsItemP6QEvent(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    QEvent *event) {
  return self->filterDescendantEvent(item, event);
}

//  bool QGraphicsScenePrivate::filterEvent(QGraphicsItem *item, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QGraphicsScenePrivate11filterEventEP13QGraphicsItemP6QEvent(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    QEvent *event) {
  return self->filterEvent(item, event);
}

//  bool QGraphicsScenePrivate::itemAcceptsHoverEvents_helper(const
//      QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGraphicsScenePrivate29itemAcceptsHoverEvents_helperEPK13QGraphicsItem(
    const QGraphicsScenePrivate *self,
    const QGraphicsItem *item) {
  return self->itemAcceptsHoverEvents_helper(item);
}

//  void
//      QGraphicsScenePrivate::cloneDragDropEvent(QGraphicsSceneDragDropEvent
//      *dest, QGraphicsSceneDragDropEvent *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate18cloneDragDropEventEP27QGraphicsSceneDragDropEventS1_(
    QGraphicsScenePrivate *self,
    QGraphicsSceneDragDropEvent *dest,
    QGraphicsSceneDragDropEvent *source) {
  self->cloneDragDropEvent(dest, source);
}

//  void QGraphicsScenePrivate::markDirty(QGraphicsItem *item, const QRectF
//      &rect, bool invalidateChildren, bool force, bool ignoreOpacity, bool
//      removingItemFromScene, bool updateBoundingRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate9markDirtyEP13QGraphicsItemRK6QRectFbbbbb(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    const QRectF *rect,
    bool invalidateChildren,
    bool force,
    bool ignoreOpacity,
    bool removingItemFromScene,
    bool updateBoundingRect) {
  self->markDirty(
      item,
      *rect,
      invalidateChildren,
      force,
      ignoreOpacity,
      removingItemFromScene,
      updateBoundingRect);
}

//  void QGraphicsScenePrivate::resetDirtyItem(QGraphicsItem *item, bool
//      recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate14resetDirtyItemEP13QGraphicsItemb(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    bool recursive) {
  self->resetDirtyItem(item, recursive);
}

//  void QGraphicsScenePrivate::ensureSortedTopLevelItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate25ensureSortedTopLevelItemsEv(
    QGraphicsScenePrivate *self) {
  self->ensureSortedTopLevelItems();
}

//  void QGraphicsScenePrivate::ensureSequentialTopLevelSiblingIndexes()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate38ensureSequentialTopLevelSiblingIndexesEv(
    QGraphicsScenePrivate *self) {
  self->ensureSequentialTopLevelSiblingIndexes();
}

//  void QGraphicsScenePrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate14setFont_helperERK5QFont(
    QGraphicsScenePrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

//  void QGraphicsScenePrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate11resolveFontEv(
    QGraphicsScenePrivate *self) {
  self->resolveFont();
}

//  void QGraphicsScenePrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate10updateFontERK5QFont(
    QGraphicsScenePrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  void QGraphicsScenePrivate::setPalette_helper(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate17setPalette_helperERK8QPalette(
    QGraphicsScenePrivate *self,
    const QPalette *palette) {
  self->setPalette_helper(*palette);
}

//  void QGraphicsScenePrivate::resolvePalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate14resolvePaletteEv(
    QGraphicsScenePrivate *self) {
  self->resolvePalette();
}

//  void QGraphicsScenePrivate::updatePalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate13updatePaletteERK8QPalette(
    QGraphicsScenePrivate *self,
    const QPalette *palette) {
  self->updatePalette(*palette);
}

//  void QGraphicsScenePrivate::updateTouchPointsForItem(QGraphicsItem *item,
//      QTouchEvent *touchEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate24updateTouchPointsForItemEP13QGraphicsItemP11QTouchEvent(
    QGraphicsItem *item,
    QTouchEvent *touchEvent) {
  QGraphicsScenePrivate::updateTouchPointsForItem(item, touchEvent);
}

//  int QGraphicsScenePrivate::findClosestTouchPointId(const QPointF
//      &scenePos)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QGraphicsScenePrivate23findClosestTouchPointIdERK7QPointF(
    QGraphicsScenePrivate *self,
    const QPointF *scenePos) {
  return self->findClosestTouchPointId(*scenePos);
}

//  void QGraphicsScenePrivate::enableTouchEventsOnViews()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate24enableTouchEventsOnViewsEv(
    QGraphicsScenePrivate *self) {
  self->enableTouchEventsOnViews();
}

//  void QGraphicsScenePrivate::updateInputMethodSensitivityInViews()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate35updateInputMethodSensitivityInViewsEv(
    QGraphicsScenePrivate *self) {
  self->updateInputMethodSensitivityInViews();
}

#endif  // QT_CONFIG(graphicsview)
