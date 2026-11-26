//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscene_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
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
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtWidgets/private/qstandardgestures_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qgesture_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#endif
#include <QtGui/private/qevent_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtWidgets/qgesture.h>
#include <QtGui/qevent.h>
#ifdef Q_OS_HARMONY
#include <QtWidgets/private/qohosgesturerecognizer_p.h>
#endif
#ifdef Q_OS_MACOS
#include <QtWidgets/private/qmacgesturerecognizer_p.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/QVarLengthArray>
#include "qplatformdefs.h"
#include <QtCore/qabstracteventdispatcher.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qcursor.h>
#include <QtCore/qdir.h>
#include <QtGui/qevent.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#endif
#include <QtCore/qhash.h>
#include <QtCore/qset.h>
#include <QtWidgets/qlayout.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylefactory.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtCore/qtranslator.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/qwidget.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/private/qdnd_p.h>
#endif
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(style_stylesheet)
#include <QtWidgets/private/qstylesheetstyle_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qwindow_p.h>
#include <QtGui/qpointingdevice.h>
#include <QtGui/private/qpointingdevice_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/QWhatsThis>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible_base.h>
#include <QtWidgets/private/qaccessiblewidgetfactory_p.h>
#endif
#include <QtGui/private/qkeymapper_p.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/private/qfont_p.h>
#if QT_CONFIG(action)
#include <QtGui/private/qaction_p.h>
#endif
#include <stdlib.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/qgesture.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtGui/qpa/qplatformfontdatabase.h>
#include <QtCore/qdatetime.h>
#include <QtGui/qpa/qplatformwindow.h>
#ifdef Q_OS_MACOS
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <algorithm>
#include <iterator>
#include <QtCore/qglobal.h>
#include <QtCore/qdebug.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/QStyleOptionTitleBar>
#include <QtWidgets/QGraphicsSceneMouseEvent>
#include <QtWidgets/private/qgraphicseffect_p.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpaintengine.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtWidgets/private/qgraphicsview_p.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtWidgets/private/qgraphicsscenelinearindex_p.h>
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
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qevent_p.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtCore/private/qobject_p.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/private/qgraphicseffect_p.h>
#endif
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtGui/private/qpathclipper_p.h>
#include <QtCore/qpointer.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstack.h>
#include <QtCore/qvariant.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpixmapcache.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#endif
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtCore/private/qdebug_p.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicssceneindex_p.h>
#include <QtWidgets/private/qgraphicsscenebsptreeindex_p.h>
#include <QtGui/qpainterpath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 223, as local:qgraphicsscene.cpp:DEBUG
#if !defined(GESTURE_DEBUG)
# define DEBUG if (0) qDebug
#endif  // !defined(GESTURE_DEBUG)

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4188, as local:qgraphicsscene.cpp:_q_paintItem
static void _q_paintItem(QGraphicsItem *item, QPainter *painter,
                         const QStyleOptionGraphicsItem *option, QWidget *widget,
                         bool useWindowOpacity, bool painterStateProtection)
{
    if (!item->isWidget()) {
        item->paint(painter, option, widget);
        return;
    }
    QGraphicsWidget *widgetItem = static_cast<QGraphicsWidget *>(item);
    QGraphicsProxyWidget *proxy = qobject_cast<QGraphicsProxyWidget *>(widgetItem);
    const qreal windowOpacity = (proxy && proxy->widget() && useWindowOpacity)
                                ? proxy->widget()->windowOpacity() : 1.0;
    const qreal oldPainterOpacity = painter->opacity();

    if (qFuzzyIsNull(windowOpacity))
        return;
    // Set new painter opacity.
    if (windowOpacity < 1.0)
        painter->setOpacity(oldPainterOpacity * windowOpacity);

    // set layoutdirection on the painter
    Qt::LayoutDirection oldLayoutDirection = painter->layoutDirection();
    painter->setLayoutDirection(widgetItem->layoutDirection());

    if (widgetItem->isWindow() && widgetItem->windowType() != Qt::Popup && widgetItem->windowType() != Qt::ToolTip
        && !(widgetItem->windowFlags() & Qt::FramelessWindowHint)) {
        if (painterStateProtection)
            painter->save();
        widgetItem->paintWindowFrame(painter, option, widget);
        if (painterStateProtection)
            painter->restore();
    } else if (widgetItem->autoFillBackground()) {
        painter->fillRect(option->exposedRect, widgetItem->palette().window());
    }

    widgetItem->paint(painter, option, widget);

    // Restore layoutdirection on the painter.
    painter->setLayoutDirection(oldLayoutDirection);
    // Restore painter opacity.
    if (windowOpacity < 1.0)
        painter->setOpacity(oldPainterOpacity);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4232, as local:qgraphicsscene.cpp:_q_paintIntoCache
static void _q_paintIntoCache(QPixmap *pix, QGraphicsItem *item, const QRegion &pixmapExposed,
                              const QTransform &itemToPixmap, QPainter::RenderHints renderHints,
                              const QStyleOptionGraphicsItem *option, bool painterStateProtection)
{
    QPixmap subPix;
    QPainter pixmapPainter;
    QRect br = pixmapExposed.boundingRect();

    // Don't use subpixmap if we get a full update.
    if (pixmapExposed.isEmpty() || (pixmapExposed.rectCount() == 1 && br.contains(pix->rect()))) {
        pix->fill(Qt::transparent);
        pixmapPainter.begin(pix);
    } else {
        subPix = QPixmap(br.size() * pix->devicePixelRatio());
        subPix.setDevicePixelRatio(pix->devicePixelRatio());
        subPix.fill(Qt::transparent);
        pixmapPainter.begin(&subPix);
        pixmapPainter.translate(-br.topLeft());
        if (!pixmapExposed.isEmpty()) {
            // Applied to subPix; paint is adjusted to the coordinate space is
            // correct.
            pixmapPainter.setClipRegion(pixmapExposed);
        }
    }

    pixmapPainter.setRenderHints(pixmapPainter.renderHints(), false);
    pixmapPainter.setRenderHints(renderHints, true);
    pixmapPainter.setWorldTransform(itemToPixmap, true);

    // Render.
    _q_paintItem(item, &pixmapPainter, option, nullptr, false, painterStateProtection);
    pixmapPainter.end();

    if (!subPix.isNull()) {
        // Blit the subpixmap into the main pixmap.
        pixmapPainter.begin(pix);
        pixmapPainter.setCompositionMode(QPainter::CompositionMode_Source);
        pixmapPainter.setClipRegion(pixmapExposed);
        pixmapPainter.drawPixmap(br.topLeft(), subPix);
        pixmapPainter.end();
    }
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4277, as local:qgraphicsscene.cpp:transformIsSimple
static inline bool transformIsSimple(const QTransform& transform)
{
    QTransform::TransformationType type = transform.type();
    if (type <= QTransform::TxScale) {
        return true;
    } else if (type == QTransform::TxRotate) {
        // Check for 90, and 270 degree rotations.
        qreal m11 = transform.m11();
        qreal m12 = transform.m12();
        qreal m21 = transform.m21();
        qreal m22 = transform.m22();
        if (m11 == 0.0f && m22 == 0.0f) {
            if (m12 == 1.0f && m21 == -1.0f)
                return true; // 90 degrees.
            else if (m12 == -1.0f && m21 == 1.0f)
                return true; // 270 degrees.
            else if (m12 == -1.0f && m21 == -1.0f)
                return true; // 90 degrees inverted y.
            else if (m12 == 1.0f && m21 == 1.0f)
                return true; // 270 degrees inverted y.
        }
    }
    return false;
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4772, as local:qgraphicsscene.cpp:setClip
static inline void setClip(QPainter *painter, QGraphicsItem *item)
{
    painter->save();
    QRectF clipRect;
    const QPainterPath clipPath(item->shape());
    if (QPathClipper::pathToRect(clipPath, &clipRect))
        painter->setClipRect(clipRect.normalized(), Qt::IntersectClip);
    else
        painter->setClipPath(clipPath, Qt::IntersectClip);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4783, as local:qgraphicsscene.cpp:setWorldTransform
static inline void setWorldTransform(QPainter *painter, const QTransform *const transformPtr,
                                     const QTransform *effectTransform)
{
    Q_ASSERT(transformPtr);
    if (effectTransform)
        painter->setWorldTransform(*transformPtr * *effectTransform);
    else
        painter->setWorldTransform(*transformPtr);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5016, as local:qgraphicsscene.cpp:updateHelper
static inline bool updateHelper(QGraphicsViewPrivate *view, QGraphicsItemPrivate *item,
                                const QRectF &rect, bool itemIsUntransformable)
{
    Q_ASSERT(view);
    Q_ASSERT(item);

    QGraphicsItem *itemq = static_cast<QGraphicsItem *>(item->q_ptr);
    QGraphicsView *viewq = static_cast<QGraphicsView *>(view->q_ptr);

    if (itemIsUntransformable) {
        const QTransform xform = itemq->deviceTransform(viewq->viewportTransform());
        if (!item->hasBoundingRegionGranularity)
            return view->updateRectF(xform.mapRect(rect));
        return view->updateRegion(rect, xform);
    }

    if (item->sceneTransformTranslateOnly && view->identityMatrix) {
        const qreal dx = item->sceneTransform.dx();
        const qreal dy = item->sceneTransform.dy();
        QRectF r(rect);
        r.translate(dx - view->horizontalScroll(), dy - view->verticalScroll());
        return view->updateRectF(r);
    }

    if (!viewq->isTransformed()) {
        if (!item->hasBoundingRegionGranularity)
            return view->updateRectF(item->sceneTransform.mapRect(rect));
        return view->updateRegion(rect, item->sceneTransform);
    }

    QTransform xform = item->sceneTransform;
    xform *= viewq->viewportTransform();
    if (!item->hasBoundingRegionGranularity)
        return view->updateRectF(xform.mapRect(rect));
    return view->updateRegion(rect, xform);
}

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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4793, as _ZN21QGraphicsScenePrivate4drawEP13QGraphicsItemP8QPainterPK10QTransformS6_P7QRegionP7QWidgetdS6_bb
inline void QGraphicsScenePrivate::draw(QGraphicsItem *item, QPainter *painter, const QTransform *const viewTransform,
                                 const QTransform *const transformPtr, QRegion *exposedRegion, QWidget *widget,
                                 qreal opacity, const QTransform *effectTransform,
                                 bool wasDirtyParentSceneTransform, bool drawItem)
{
    const auto &children = item->d_ptr->children;

    const bool itemIsFullyTransparent = QGraphicsItemPrivate::isOpacityNull(opacity);
    const bool itemClipsChildrenToShape = (item->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape);
    const bool itemHasChildren = !children.isEmpty();
    bool setChildClip = itemClipsChildrenToShape;
    bool itemHasChildrenStackedBehind = false;

    int i = 0;
    if (itemHasChildren) {
        if (itemClipsChildrenToShape)
            setWorldTransform(painter, transformPtr, effectTransform);

        item->d_ptr->ensureSortedChildren();
        // Items with the 'ItemStacksBehindParent' flag are put in front of the list
        // so all we have to do is to check the first item.
        itemHasChildrenStackedBehind = (children.at(0)->d_ptr->flags
                                        & QGraphicsItem::ItemStacksBehindParent);

        if (itemHasChildrenStackedBehind) {
            if (itemClipsChildrenToShape) {
                setClip(painter, item);
                setChildClip = false;
            }

            // Draw children behind
            for (i = 0; i < children.size(); ++i) {
                QGraphicsItem *child = children.at(i);
                if (wasDirtyParentSceneTransform)
                    child->d_ptr->dirtySceneTransform = 1;
                if (!(child->d_ptr->flags & QGraphicsItem::ItemStacksBehindParent))
                    break;
                if (itemIsFullyTransparent && !(child->d_ptr->flags & QGraphicsItem::ItemIgnoresParentOpacity))
                    continue;
                drawSubtreeRecursive(child, painter, viewTransform, exposedRegion, widget, opacity, effectTransform);
            }
        }
    }

    // Draw item
    if (drawItem) {
        Q_ASSERT(!itemIsFullyTransparent);
        Q_ASSERT(!(item->d_ptr->flags & QGraphicsItem::ItemHasNoContents));
        Q_ASSERT(transformPtr);
        item->d_ptr->initStyleOption(&styleOptionTmp, *transformPtr, exposedRegion
                                     ? *exposedRegion : QRegion(), exposedRegion == nullptr);

        const bool itemClipsToShape = item->d_ptr->flags & QGraphicsItem::ItemClipsToShape;
        bool restorePainterClip = false;

        if (!itemHasChildren || !itemClipsChildrenToShape) {
            // Item does not have children or clip children to shape.
            setWorldTransform(painter, transformPtr, effectTransform);
            if ((restorePainterClip = itemClipsToShape))
                setClip(painter, item);
        } else if (itemHasChildrenStackedBehind){
            // Item clips children to shape and has children stacked behind, which means
            // the painter is already clipped to the item's shape.
            if (itemClipsToShape) {
                // The clip is already correct. Ensure correct world transform.
                setWorldTransform(painter, transformPtr, effectTransform);
            } else {
                // Remove clip (this also ensures correct world transform).
                painter->restore();
                setChildClip = true;
            }
        } else if (itemClipsToShape) {
            // Item clips children and itself to shape. It does not have hildren stacked
            // behind, which means the clip has not yet been set. We set it now and re-use it
            // for the children.
            setClip(painter, item);
            setChildClip = false;
        }

        if (painterStateProtection && !restorePainterClip)
            painter->save();

        painter->setOpacity(opacity);
        if (!item->d_ptr->cacheMode && !item->d_ptr->isWidget)
            item->paint(painter, &styleOptionTmp, widget);
        else
            drawItemHelper(item, painter, &styleOptionTmp, widget, painterStateProtection);

        if (painterStateProtection || restorePainterClip)
            painter->restore();

        static int drawRect = qEnvironmentVariableIntValue("QT_DRAW_SCENE_ITEM_RECTS");
        if (drawRect) {
            QPen oldPen = painter->pen();
            QBrush oldBrush = painter->brush();
            quintptr ptr = reinterpret_cast<quintptr>(item);
            const QColor color = QColor::fromHsv(ptr % 255, 255, 255);
            painter->setPen(color);
            painter->setBrush(Qt::NoBrush);
            painter->drawRect(adjustedItemBoundingRect(item));
            painter->setPen(oldPen);
            painter->setBrush(oldBrush);
        }
    }

    // Draw children in front
    if (itemHasChildren) {
        if (setChildClip)
            setClip(painter, item);

        for (; i < children.size(); ++i) {
            QGraphicsItem *child = children.at(i);
            if (wasDirtyParentSceneTransform)
                child->d_ptr->dirtySceneTransform = 1;
            if (itemIsFullyTransparent && !(child->d_ptr->flags & QGraphicsItem::ItemIgnoresParentOpacity))
                continue;
            drawSubtreeRecursive(child, painter, viewTransform, exposedRegion, widget, opacity, effectTransform);
        }

        // Restore child clip
        if (itemClipsChildrenToShape)
            painter->restore();
    }
}

//  from src/widgets/effects/qgraphicseffect.cpp, line 350, as _ZN28QGraphicsEffectSourcePrivate15setCachedOffsetERK6QPoint
inline void QGraphicsEffectSourcePrivate::setCachedOffset(const QPoint &offset)
{
    m_cachedOffset = offset;
}

//  from src/widgets/graphicsview/qgraphicsitem.cpp, line 11062, as _ZNK32QGraphicsItemEffectSourcePrivate16paddedEffectRectEN2Qt16CoordinateSystemEN15QGraphicsEffect13PixmapPadModeERK6QRectFPb
#if QT_CONFIG(graphicseffect)
inline QRectF QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSystem system, QGraphicsEffect::PixmapPadMode mode, const QRectF &sourceRect, bool *unpadded) const
{
    QRectF effectRectF;

    if (unpadded)
        *unpadded = false;

    if (mode == QGraphicsEffect::PadToEffectiveBoundingRect) {
        if (info) {
            QRectF deviceRect = system == Qt::DeviceCoordinates ? sourceRect : info->painter->worldTransform().mapRect(sourceRect);
            effectRectF = item->graphicsEffect()->boundingRectFor(deviceRect);
            if (unpadded)
                *unpadded = (effectRectF.size() == sourceRect.size());
            if (info && system == Qt::LogicalCoordinates)
                effectRectF = info->painter->worldTransform().inverted().mapRect(effectRectF);
        } else {
            // no choice but to send a logical coordinate bounding rect to boundingRectFor
            effectRectF = item->graphicsEffect()->boundingRectFor(sourceRect);
        }
    } else if (mode == QGraphicsEffect::PadToTransparentBorder) {
        // adjust by 1.5 to account for cosmetic pens
        effectRectF = sourceRect.adjusted(-1.5, -1.5, 1.5, 1.5);
    } else {
        effectRectF = sourceRect;
        if (unpadded)
            *unpadded = true;
    }

    return effectRectF;
}
#endif  // QT_CONFIG(graphicseffect)

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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4307, as _ZN21QGraphicsScenePrivate14drawItemHelperEP13QGraphicsItemP8QPainterPK24QStyleOptionGraphicsItemP7QWidgetb
inline void QGraphicsScenePrivate::drawItemHelper(QGraphicsItem *item, QPainter *painter,
                                           const QStyleOptionGraphicsItem *option, QWidget *widget,
                                           bool painterStateProtection)
{
    QGraphicsItemPrivate *itemd = item->d_ptr.data();
    QGraphicsItem::CacheMode cacheMode = QGraphicsItem::CacheMode(itemd->cacheMode);

    // Render directly, using no cache.
    if (cacheMode == QGraphicsItem::NoCache) {
        _q_paintItem(static_cast<QGraphicsWidget *>(item), painter, option, widget, true, painterStateProtection);
        return;
    }

    const qreal devicePixelRatio = painter->device()->devicePixelRatio();
    const qreal oldPainterOpacity = painter->opacity();
    qreal newPainterOpacity = oldPainterOpacity;
    QGraphicsProxyWidget *proxy = item->isWidget() ? qobject_cast<QGraphicsProxyWidget *>(static_cast<QGraphicsWidget *>(item)) : 0;
    if (proxy && proxy->widget()) {
        const qreal windowOpacity = proxy->widget()->windowOpacity();
        if (windowOpacity < 1.0)
            newPainterOpacity *= windowOpacity;
    }

    // Item's (local) bounding rect
    QRectF brect = item->boundingRect();
    QRectF adjustedBrect(brect);
    _q_adjustRect(&adjustedBrect);
    if (adjustedBrect.isEmpty())
        return;

    // Fetch the off-screen transparent buffer and exposed area info.
    QPixmapCache::Key pixmapKey;
    QPixmap pix;

    bool pixmapFound;
    QGraphicsItemCache *itemCache = itemd->extraItemCache();
    if (cacheMode == QGraphicsItem::ItemCoordinateCache) {
        pixmapKey = itemCache->key;
    } else {
        pixmapKey = itemCache->deviceData.value(widget).key;
    }

    // Find pixmap in cache.
    pixmapFound = QPixmapCache::find(pixmapKey, &pix);

    // Render using item coordinate cache mode.
    if (cacheMode == QGraphicsItem::ItemCoordinateCache) {
        QSize pixmapSize;
        bool fixedCacheSize = itemCache->fixedSize.isValid();
        QRect br = brect.toAlignedRect();
        if (fixedCacheSize) {
            pixmapSize = itemCache->fixedSize;
        } else {
            pixmapSize = br.size();
        }

        pixmapSize *= devicePixelRatio;

        // Create or recreate the pixmap.
        int adjust = itemCache->fixedSize.isValid() ? 0 : 2;
        QSize adjustSize(adjust*2, adjust*2);
        br.adjust(-adjust / devicePixelRatio, -adjust / devicePixelRatio, adjust / devicePixelRatio, adjust / devicePixelRatio);
        if (pix.isNull() || (!fixedCacheSize && (pixmapSize + adjustSize) != pix.size())) {
            pix = QPixmap(pixmapSize + adjustSize);
            itemCache->boundingRect = br;
            itemCache->exposed.clear();
            itemCache->allExposed = true;
        } else if (itemCache->boundingRect != br) {
            itemCache->boundingRect = br;
            itemCache->exposed.clear();
            itemCache->allExposed = true;
        }

        // Redraw any newly exposed areas.
        if (itemCache->allExposed || !itemCache->exposed.isEmpty()) {

            //We know that we will modify the pixmap, removing it from the cache
            //will detach the one we have and avoid a deep copy
            if (pixmapFound)
                QPixmapCache::remove(pixmapKey);

            // Fit the item's bounding rect into the pixmap's coordinates.
            QTransform itemToPixmap;
            if (fixedCacheSize) {
                const QPointF scale((pixmapSize.width() / devicePixelRatio) / brect.width(),
                                    (pixmapSize.height() / devicePixelRatio) / brect.height());
                itemToPixmap.scale(scale.x(), scale.y());
            }
            itemToPixmap.translate(-br.x(), -br.y());

            // Generate the item's exposedRect and map its list of expose
            // rects to device coordinates.
            styleOptionTmp = *option;
            QRegion pixmapExposed;
            QRectF exposedRect;
            if (!itemCache->allExposed) {
                for (const auto &rect : std::as_const(itemCache->exposed)) {
                    exposedRect |= rect;
                    pixmapExposed += itemToPixmap.mapRect(rect).toAlignedRect();
                }
            } else {
                exposedRect = brect;
            }
            styleOptionTmp.exposedRect = exposedRect;

            // Render.
            pix.setDevicePixelRatio(devicePixelRatio);
            _q_paintIntoCache(&pix, item, pixmapExposed, itemToPixmap, painter->renderHints(),
                              &styleOptionTmp, painterStateProtection);

            // insert this pixmap into the cache.
            itemCache->key = QPixmapCache::insert(pix);

            // Reset expose data.
            itemCache->allExposed = false;
            itemCache->exposed.clear();
        }

        // Redraw the exposed area using the transformed painter. Depending on
        // the hardware, this may be a server-side operation, or an expensive
        // qpixmap-image-transform-pixmap roundtrip.
        if (newPainterOpacity != oldPainterOpacity) {
            painter->setOpacity(newPainterOpacity);
            painter->drawPixmap(br.topLeft(), pix);
            painter->setOpacity(oldPainterOpacity);
        } else {
            painter->drawPixmap(br.topLeft(), pix);
        }
        return;
    }

    // Render using device coordinate cache mode.
    if (cacheMode == QGraphicsItem::DeviceCoordinateCache) {
        // Find the item's bounds in device coordinates.
        QRectF deviceBounds = painter->worldTransform().mapRect(brect);
        QRect deviceRect = deviceBounds.toRect().adjusted(-1, -1, 1, 1);
        if (deviceRect.isEmpty())
            return;
        QRect viewRect = widget ? widget->rect() : QRect();
        if (widget && !viewRect.intersects(deviceRect))
            return;

        // Resort to direct rendering if the device rect exceeds the
        // (optional) maximum bounds. (QGraphicsSvgItem uses this).
        QSize maximumCacheSize =
            itemd->extra(QGraphicsItemPrivate::ExtraMaxDeviceCoordCacheSize).toSize();
        if (!maximumCacheSize.isEmpty()
            && (deviceRect.width() > maximumCacheSize.width()
                || deviceRect.height() > maximumCacheSize.height())) {
            _q_paintItem(static_cast<QGraphicsWidget *>(item), painter, option, widget,
                         oldPainterOpacity != newPainterOpacity, painterStateProtection);
            return;
        }

        // Create or reuse offscreen pixmap, possibly scroll/blit from the old one.
        // If the world transform is rotated we always recreate the cache to avoid
        // wrong blending.
        bool pixModified = false;
        QGraphicsItemCache::DeviceData *deviceData = &itemCache->deviceData[widget];
        bool invertable = true;
        QTransform diff = deviceData->lastTransform.inverted(&invertable);
        if (invertable)
            diff *= painter->worldTransform();
        deviceData->lastTransform = painter->worldTransform();
        bool allowPartialCacheExposure = false;
        bool simpleTransform = invertable && diff.type() <= QTransform::TxTranslate
                               && transformIsSimple(painter->worldTransform());
        if (!simpleTransform) {
            pixModified = true;
            itemCache->allExposed = true;
            itemCache->exposed.clear();
            deviceData->cacheIndent = QPoint();
            pix = QPixmap();
        } else if (!viewRect.isNull()) {
            allowPartialCacheExposure = deviceData->cacheIndent != QPoint();
        }

        // Allow partial cache exposure if the device rect isn't fully contained and
        // deviceRect is 20% taller or wider than the viewRect.
        if (!allowPartialCacheExposure && !viewRect.isNull() && !viewRect.contains(deviceRect)) {
            allowPartialCacheExposure = (viewRect.width() * 1.2 < deviceRect.width())
                                         || (viewRect.height() * 1.2 < deviceRect.height());
        }

        QRegion scrollExposure;
        if (allowPartialCacheExposure) {
            // Part of pixmap is drawn. Either device contains viewrect (big
            // item covers whole screen) or parts of device are outside the
            // viewport. In either case the device rect must be the intersect
            // between the two.
            int dx = deviceRect.left() < viewRect.left() ? viewRect.left() - deviceRect.left() : 0;
            int dy = deviceRect.top() < viewRect.top() ? viewRect.top() - deviceRect.top() : 0;
            QPoint newCacheIndent(dx, dy);
            deviceRect &= viewRect;

            if (pix.isNull()) {
                deviceData->cacheIndent = QPoint();
                itemCache->allExposed = true;
                itemCache->exposed.clear();
                pixModified = true;
            }

            // Copy / "scroll" the old pixmap onto the new ole and calculate
            // scrolled exposure.
            if (newCacheIndent != deviceData->cacheIndent || deviceRect.size() != pix.size() / devicePixelRatio) {
                QPoint diff = newCacheIndent - deviceData->cacheIndent;
                QPixmap newPix(deviceRect.size() * devicePixelRatio);
                // ### Investigate removing this fill (test with Plasma and
                // graphicssystem raster).
                newPix.fill(Qt::transparent);
                if (!pix.isNull()) {
                    newPix.setDevicePixelRatio(devicePixelRatio);
                    QPainter newPixPainter(&newPix);
                    newPixPainter.drawPixmap(-diff, pix);
                    newPixPainter.end();
                }
                QRegion exposed;
                exposed += QRect(QPoint(0,0), newPix.size() / devicePixelRatio);
                if (!pix.isNull())
                    exposed -= QRect(-diff, pix.size() / devicePixelRatio);
                scrollExposure = exposed;

                pix = newPix;
                pixModified = true;
            }
            deviceData->cacheIndent = newCacheIndent;
        } else {
            // Full pixmap is drawn.
            deviceData->cacheIndent = QPoint();

            // Auto-adjust the pixmap size.
            if (deviceRect.size() != pix.size() / devicePixelRatio) {
                // exposed needs to cover the whole pixmap
                pix = QPixmap(deviceRect.size() * devicePixelRatio);
                pixModified = true;
                itemCache->allExposed = true;
                itemCache->exposed.clear();
            }
        }

        // Check for newly invalidated areas.
        if (itemCache->allExposed || !itemCache->exposed.isEmpty() || !scrollExposure.isEmpty()) {
            //We know that we will modify the pixmap, removing it from the cache
            //will detach the one we have and avoid a deep copy
            if (pixmapFound)
                QPixmapCache::remove(pixmapKey);

            // Construct an item-to-pixmap transform.
            QPointF p = deviceRect.topLeft();
            QTransform itemToPixmap = painter->worldTransform();
            if (!p.isNull())
                itemToPixmap *= QTransform::fromTranslate(-p.x(), -p.y());

            // Map the item's logical expose to pixmap coordinates.
            QRegion pixmapExposed = scrollExposure;
            if (!itemCache->allExposed) {
                for (const auto &rect : std::as_const(itemCache->exposed))
                    pixmapExposed += itemToPixmap.mapRect(rect).toRect().adjusted(-1, -1, 1, 1);
            }

            // Calculate the style option's exposedRect.
            QRectF br;
            if (itemCache->allExposed) {
                br = item->boundingRect();
            } else {
                for (const auto &rect : std::as_const(itemCache->exposed))
                    br |= rect;
                QTransform pixmapToItem = itemToPixmap.inverted();
                for (const QRect &r : std::as_const(scrollExposure))
                    br |= pixmapToItem.mapRect(r);
            }
            styleOptionTmp = *option;
            styleOptionTmp.exposedRect = br.adjusted(-1, -1, 1, 1);

            // Render the exposed areas.
            pix.setDevicePixelRatio(devicePixelRatio);
            _q_paintIntoCache(&pix, item, pixmapExposed, itemToPixmap, painter->renderHints(),
                              &styleOptionTmp, painterStateProtection);

            // Reset expose data.
            pixModified = true;
            itemCache->allExposed = false;
            itemCache->exposed.clear();
        }

        if (pixModified) {
            // Insert this pixmap into the cache.
            deviceData->key = QPixmapCache::insert(pix);
        }

        // Redraw the exposed area using an untransformed painter. This
        // effectively becomes a bitblit that does not transform the cache.
        QTransform restoreTransform = painter->worldTransform();
        painter->setWorldTransform(QTransform());
        if (newPainterOpacity != oldPainterOpacity) {
            painter->setOpacity(newPainterOpacity);
            painter->drawPixmap(deviceRect.topLeft(), pix);
            painter->setOpacity(oldPainterOpacity);
        } else {
            painter->drawPixmap(deviceRect.topLeft(), pix);
        }
        painter->setWorldTransform(restoreTransform);
        return;
    }
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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 445, as _ZN21QGraphicsScenePrivate20_q_processDirtyItemsEv
inline void QGraphicsScenePrivate::_q_processDirtyItems()
{
    processDirtyItemsEmitted = false;

    if (updateAll) {
        Q_ASSERT(calledEmitUpdated);
        // No need for further processing (except resetting the dirty states).
        // The growingItemsBoundingRect is updated in _q_emitUpdated.
        for (auto topLevelItem : std::as_const(topLevelItems))
            resetDirtyItem(topLevelItem, /*recursive=*/true);
        return;
    }

    const bool wasPendingSceneUpdate = calledEmitUpdated;
    const QRectF oldGrowingItemsBoundingRect = growingItemsBoundingRect;

    // Process items recursively.
    for (auto topLevelItem : std::as_const(topLevelItems))
        processDirtyItemsRecursive(topLevelItem);

    dirtyGrowingItemsBoundingRect = false;
    if (!hasSceneRect && oldGrowingItemsBoundingRect != growingItemsBoundingRect)
        emit q_func()->sceneRectChanged(growingItemsBoundingRect);

    if (wasPendingSceneUpdate)
        return;

    for (auto view : std::as_const(views))
        view->d_func()->processPendingUpdates();

    if (calledEmitUpdated) {
        // We did a compatibility QGraphicsScene::update in processDirtyItemsRecursive
        // and we cannot wait for the control to reach the eventloop before the
        // changed signal is emitted, so we emit it now.
        _q_emitUpdated();
    }

    // Immediately dispatch all pending update requests on the views.
    for (auto view : std::as_const(views))
        view->d_func()->dispatchPendingUpdateRequests();
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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4613, as _ZN21QGraphicsScenePrivate9drawItemsEP8QPainterPK10QTransformP7QRegionP7QWidget
inline void QGraphicsScenePrivate::drawItems(QPainter *painter, const QTransform *const viewTransform,
                                      QRegion *exposedRegion, QWidget *widget)
{
    // Make sure we don't have unpolished items before we draw.
    if (!unpolishedItems.isEmpty())
        _q_polishItems();

    updateAll = false;
    QRectF exposedSceneRect;
    if (exposedRegion && indexMethod != QGraphicsScene::NoIndex) {
        exposedSceneRect = exposedRegion->boundingRect().adjusted(-1, -1, 1, 1);
        if (viewTransform)
            exposedSceneRect = viewTransform->inverted().mapRect(exposedSceneRect);
    }
    const QList<QGraphicsItem *> tli = index->estimateTopLevelItems(exposedSceneRect, Qt::AscendingOrder);
    for (const auto subTree : tli)
        drawSubtreeRecursive(subTree, painter, viewTransform, exposedRegion, widget);
}

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 4632, as _ZN21QGraphicsScenePrivate20drawSubtreeRecursiveEP13QGraphicsItemP8QPainterPK10QTransformP7QRegionP7QWidgetdS6_
inline void QGraphicsScenePrivate::drawSubtreeRecursive(QGraphicsItem *item, QPainter *painter,
                                                 const QTransform *const viewTransform,
                                                 QRegion *exposedRegion, QWidget *widget,
                                                 qreal parentOpacity, const QTransform *const effectTransform)
{
    Q_ASSERT(item);

    if (!item->d_ptr->visible)
        return;

    const bool itemHasContents = !(item->d_ptr->flags & QGraphicsItem::ItemHasNoContents);
    const bool itemHasChildren = !item->d_ptr->children.isEmpty();
    if (!itemHasContents && !itemHasChildren)
        return; // Item has neither contents nor children!(?)

    const qreal opacity = item->d_ptr->combineOpacityFromParent(parentOpacity);
    const bool itemIsFullyTransparent = QGraphicsItemPrivate::isOpacityNull(opacity);
    if (itemIsFullyTransparent && (!itemHasChildren || item->d_ptr->childrenCombineOpacity()))
        return;

    QTransform transform(Qt::Uninitialized);
    QTransform *transformPtr = nullptr;
    bool translateOnlyTransform = false;
#define ENSURE_TRANSFORM_PTR \
    if (!transformPtr) { \
        Q_ASSERT(!itemIsUntransformable); \
        if (viewTransform) { \
            transform = item->d_ptr->sceneTransform; \
            transform *= *viewTransform; \
            transformPtr = &transform; \
        } else { \
            transformPtr = &item->d_ptr->sceneTransform; \
            translateOnlyTransform = item->d_ptr->sceneTransformTranslateOnly; \
        } \
    }

    // Update the item's scene transform if the item is transformable;
    // otherwise calculate the full transform,
    bool wasDirtyParentSceneTransform = false;
    const bool itemIsUntransformable = item->d_ptr->itemIsUntransformable();
    if (itemIsUntransformable) {
        transform = item->deviceTransform(viewTransform ? *viewTransform : QTransform());
        transformPtr = &transform;
    } else if (item->d_ptr->dirtySceneTransform) {
        item->d_ptr->updateSceneTransformFromParent();
        Q_ASSERT(!item->d_ptr->dirtySceneTransform);
        wasDirtyParentSceneTransform = true;
    }

    const bool itemClipsChildrenToShape = (item->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape
                                           || item->d_ptr->flags & QGraphicsItem::ItemContainsChildrenInShape);
    bool drawItem = itemHasContents && !itemIsFullyTransparent;
    if (drawItem || minimumRenderSize > 0.0) {
        const QRectF brect = adjustedItemEffectiveBoundingRect(item);
        ENSURE_TRANSFORM_PTR
        QRectF preciseViewBoundingRect = translateOnlyTransform ? brect.translated(transformPtr->dx(), transformPtr->dy())
                                                                : transformPtr->mapRect(brect);

        bool itemIsTooSmallToRender = false;
        if (minimumRenderSize > 0.0
            && (preciseViewBoundingRect.width() < minimumRenderSize
                || preciseViewBoundingRect.height() < minimumRenderSize)) {
           itemIsTooSmallToRender = true;
           drawItem = false;
        }

        bool itemIsOutsideVisibleRect = false;
        if (drawItem) {
            QRect viewBoundingRect = preciseViewBoundingRect.toAlignedRect();
            viewBoundingRect.adjust(-int(rectAdjust), -int(rectAdjust), rectAdjust, rectAdjust);
            if (widget)
                item->d_ptr->paintedViewBoundingRects.insert(widget, viewBoundingRect);
            drawItem = exposedRegion ? exposedRegion->intersects(viewBoundingRect)
                                     : !viewBoundingRect.normalized().isEmpty();
            itemIsOutsideVisibleRect = !drawItem;
        }

        if (itemIsTooSmallToRender || itemIsOutsideVisibleRect) {
            // We cannot simply use !drawItem here. If we did it is possible
            // to enter the outer if statement with drawItem == false and minimumRenderSize > 0
            // and finally end up inside this inner if, even though none of the above two
            // conditions are met. In that case we should not return from this function
            // but call draw() instead.
            if (!itemHasChildren)
                return;
            if (itemClipsChildrenToShape) {
                if (wasDirtyParentSceneTransform)
                    item->d_ptr->invalidateChildrenSceneTransform();
                return;
            }
        }
    } // else we know for sure this item has children we must process.

    if (itemHasChildren && itemClipsChildrenToShape)
        ENSURE_TRANSFORM_PTR;

#if QT_CONFIG(graphicseffect)
    if (item->d_ptr->graphicsEffect && item->d_ptr->graphicsEffect->isEnabled()) {
        ENSURE_TRANSFORM_PTR;
        QGraphicsItemPaintInfo info(viewTransform, transformPtr, effectTransform, exposedRegion, widget, &styleOptionTmp,
                                    painter, opacity, wasDirtyParentSceneTransform, itemHasContents && !itemIsFullyTransparent);
        QGraphicsEffectSource *source = item->d_ptr->graphicsEffect->d_func()->source;
        QGraphicsItemEffectSourcePrivate *sourced = static_cast<QGraphicsItemEffectSourcePrivate *>
                                                    (source->d_func());
        sourced->info = &info;
        const QTransform restoreTransform = painter->worldTransform();
        if (effectTransform)
            painter->setWorldTransform(*transformPtr * *effectTransform);
        else
            painter->setWorldTransform(*transformPtr);
        painter->setOpacity(opacity);

        if (sourced->currentCachedSystem() != Qt::LogicalCoordinates
            && sourced->lastEffectTransform != painter->worldTransform())
        {
            if (sourced->lastEffectTransform.type() <= QTransform::TxTranslate
                && painter->worldTransform().type() <= QTransform::TxTranslate)
            {
                QRectF sourceRect = sourced->boundingRect(Qt::DeviceCoordinates);
                QRect effectRect = sourced->paddedEffectRect(Qt::DeviceCoordinates, sourced->currentCachedMode(), sourceRect).toAlignedRect();

                sourced->setCachedOffset(effectRect.topLeft());
            } else {
                sourced->invalidateCache(QGraphicsEffectSourcePrivate::TransformChanged);
            }

            sourced->lastEffectTransform = painter->worldTransform();
        }

        item->d_ptr->graphicsEffect->draw(painter);
        painter->setWorldTransform(restoreTransform);
        sourced->info = nullptr;
    } else
#endif // QT_CONFIG(graphicseffect)
    {
        draw(item, painter, viewTransform, transformPtr, exposedRegion, widget, opacity,
             effectTransform, wasDirtyParentSceneTransform, drawItem);
    }
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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 5053, as _ZN21QGraphicsScenePrivate26processDirtyItemsRecursiveEP13QGraphicsItembd
inline void QGraphicsScenePrivate::processDirtyItemsRecursive(QGraphicsItem *item, bool dirtyAncestorContainsChildren,
                                                       qreal parentOpacity)
{
    Q_Q(QGraphicsScene);
    Q_ASSERT(item);
    Q_ASSERT(!updateAll);

    if (!item->d_ptr->dirty && !item->d_ptr->dirtyChildren) {
        resetDirtyItem(item);
        return;
    }

    const bool itemIsHidden = !item->d_ptr->ignoreVisible && !item->d_ptr->visible;
    if (itemIsHidden) {
        resetDirtyItem(item, /*recursive=*/true);
        return;
    }

    bool itemHasContents = !(item->d_ptr->flags & QGraphicsItem::ItemHasNoContents);
    const bool itemHasChildren = !item->d_ptr->children.isEmpty();
    if (!itemHasContents) {
        if (!itemHasChildren) {
            resetDirtyItem(item);
            return; // Item has neither contents nor children!(?)
        }
        if (item->d_ptr->graphicsEffect)
            itemHasContents = true;
    }

    const qreal opacity = item->d_ptr->combineOpacityFromParent(parentOpacity);
    const bool itemIsFullyTransparent = !item->d_ptr->ignoreOpacity
                                        && QGraphicsItemPrivate::isOpacityNull(opacity);
    if (itemIsFullyTransparent && (!itemHasChildren || item->d_ptr->childrenCombineOpacity())) {
        resetDirtyItem(item, /*recursive=*/itemHasChildren);
        return;
    }

    bool wasDirtyParentSceneTransform = item->d_ptr->dirtySceneTransform;
    const bool itemIsUntransformable = item->d_ptr->itemIsUntransformable();
    if (wasDirtyParentSceneTransform && !itemIsUntransformable) {
        item->d_ptr->updateSceneTransformFromParent();
        Q_ASSERT(!item->d_ptr->dirtySceneTransform);
    }

    const bool wasDirtyParentViewBoundingRects = item->d_ptr->paintedViewBoundingRectsNeedRepaint;
    if (itemIsFullyTransparent || !itemHasContents || dirtyAncestorContainsChildren) {
        // Make sure we don't process invisible items or items with no content.
        item->d_ptr->dirty = 0;
        item->d_ptr->fullUpdatePending = 0;
        // Might have a dirty view bounding rect otherwise.
        if (itemIsFullyTransparent || !itemHasContents)
            item->d_ptr->paintedViewBoundingRectsNeedRepaint = 0;
    }

    if (!hasSceneRect && item->d_ptr->geometryChanged && item->d_ptr->visible) {
        // Update growingItemsBoundingRect.
        if (item->d_ptr->sceneTransformTranslateOnly) {
            growingItemsBoundingRect |= item->boundingRect().translated(item->d_ptr->sceneTransform.dx(),
                                                                        item->d_ptr->sceneTransform.dy());
        } else {
            growingItemsBoundingRect |= item->d_ptr->sceneTransform.mapRect(item->boundingRect());
        }
    }

    // Process item.
    if (item->d_ptr->dirty || item->d_ptr->paintedViewBoundingRectsNeedRepaint) {
        const bool useCompatUpdate = views.isEmpty() || isSignalConnected(changedSignalIndex);
        const QRectF itemBoundingRect = adjustedItemEffectiveBoundingRect(item);

        if (useCompatUpdate && !itemIsUntransformable && qFuzzyIsNull(item->boundingRegionGranularity())) {
            // This block of code is kept for compatibility. Since 4.5, by default
            // QGraphicsView does not connect the signal and we use the below
            // method of delivering updates.
            if (item->d_ptr->sceneTransformTranslateOnly) {
                q->update(itemBoundingRect.translated(item->d_ptr->sceneTransform.dx(),
                                                      item->d_ptr->sceneTransform.dy()));
            } else {
                QRectF rect = item->d_ptr->sceneTransform.mapRect(itemBoundingRect);
                if (!rect.isEmpty())
                    q->update(rect);
            }
        } else {
            QRectF dirtyRect;
            bool uninitializedDirtyRect = true;

            for (auto view : std::as_const(views)) {
                QGraphicsViewPrivate *viewPrivate = view->d_func();
                QRect &paintedViewBoundingRect = item->d_ptr->paintedViewBoundingRects[viewPrivate->viewport];
                if (viewPrivate->fullUpdatePending
                    || viewPrivate->viewportUpdateMode == QGraphicsView::NoViewportUpdate) {
                    // Okay, if we have a full update pending or no viewport update, this item's
                    // paintedViewBoundingRect  will be updated correctly in the next paintEvent if
                    // it is inside the viewport, but for now we can pretend that it is outside.
                    paintedViewBoundingRect = QRect(-1, -1, -1, -1);
                    continue;
                }

                if (item->d_ptr->paintedViewBoundingRectsNeedRepaint) {
                    paintedViewBoundingRect.translate(viewPrivate->dirtyScrollOffset);
                    if (!viewPrivate->updateRect(paintedViewBoundingRect))
                        paintedViewBoundingRect = QRect(-1, -1, -1, -1); // Outside viewport.
                }

                if (!item->d_ptr->dirty)
                    continue;

                if (!item->d_ptr->paintedViewBoundingRectsNeedRepaint
                    && paintedViewBoundingRect.x() == -1 && paintedViewBoundingRect.y() == -1
                    && paintedViewBoundingRect.width() == -1 && paintedViewBoundingRect.height() == -1) {
                    continue; // Outside viewport.
                }

                if (uninitializedDirtyRect) {
                    dirtyRect = itemBoundingRect;
                    if (!item->d_ptr->fullUpdatePending) {
                        _q_adjustRect(&item->d_ptr->needsRepaint);
                        dirtyRect &= item->d_ptr->needsRepaint;
                    }
                    uninitializedDirtyRect = false;
                }

                if (dirtyRect.isEmpty())
                    continue; // Discard updates outside the bounding rect.

                if (!updateHelper(viewPrivate, item->d_ptr.data(), dirtyRect, itemIsUntransformable)
                    && item->d_ptr->paintedViewBoundingRectsNeedRepaint) {
                    paintedViewBoundingRect = QRect(-1, -1, -1, -1); // Outside viewport.
                }
            }
        }
    }

    // Process children.
    if (itemHasChildren && item->d_ptr->dirtyChildren) {
        const bool itemClipsChildrenToShape = item->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape
                                              || item->d_ptr->flags & QGraphicsItem::ItemContainsChildrenInShape;
        // Items with no content are threated as 'dummy' items which means they are never drawn and
        // 'processed', so the painted view bounding rect is never up-to-date. This means that whenever
        // such an item changes geometry, its children have to take care of the update regardless
        // of whether the item clips children to shape or not.
        const bool bypassUpdateClip = !itemHasContents && wasDirtyParentViewBoundingRects;
        if (itemClipsChildrenToShape && !bypassUpdateClip) {
            // Make sure child updates are clipped to the item's bounding rect.
            for (auto view : std::as_const(views))
                view->d_func()->setUpdateClip(item);
        }
        if (!dirtyAncestorContainsChildren) {
            dirtyAncestorContainsChildren = item->d_ptr->fullUpdatePending
                                            && itemClipsChildrenToShape;
        }
        const bool allChildrenDirty = item->d_ptr->allChildrenDirty;
        const bool parentIgnoresVisible = item->d_ptr->ignoreVisible;
        const bool parentIgnoresOpacity = item->d_ptr->ignoreOpacity;
        for (auto child : std::as_const(item->d_ptr->children)) {
            if (wasDirtyParentSceneTransform)
                child->d_ptr->dirtySceneTransform = 1;
            if (wasDirtyParentViewBoundingRects)
                child->d_ptr->paintedViewBoundingRectsNeedRepaint = 1;
            if (parentIgnoresVisible)
                child->d_ptr->ignoreVisible = 1;
            if (parentIgnoresOpacity)
                child->d_ptr->ignoreOpacity = 1;
            if (allChildrenDirty) {
                child->d_ptr->dirty = 1;
                child->d_ptr->fullUpdatePending = 1;
                child->d_ptr->dirtyChildren = 1;
                child->d_ptr->allChildrenDirty = 1;
            }
            processDirtyItemsRecursive(child, dirtyAncestorContainsChildren, opacity);
        }

        if (itemClipsChildrenToShape) {
            // Reset updateClip.
            for (auto view : std::as_const(views))
                view->d_func()->setUpdateClip(nullptr);
        }
    } else if (wasDirtyParentSceneTransform) {
        item->d_ptr->invalidateChildrenSceneTransform();
    }

    resetDirtyItem(item);
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

//  from src/widgets/graphicsview/qgraphicsscene.cpp, line 6138, as _ZN21QGraphicsScenePrivate24gestureTargetsAtHotSpotsERK4QSetIP8QGestureEN2Qt11GestureFlagEP5QHashIP15QGraphicsObjectS3_EPS0_ISA_EPS3_SF_
#if !defined(QT_NO_GESTURES)
inline void QGraphicsScenePrivate::gestureTargetsAtHotSpots(const QSet<QGesture *> &gestures,
                                              Qt::GestureFlag flag,
                                              QHash<QGraphicsObject *, QSet<QGesture *> > *targets,
                                              QSet<QGraphicsObject *> *itemsSet,
                                              QSet<QGesture *> *normal,
                                              QSet<QGesture *> *conflicts)
{
    QSet<QGesture *> normalGestures; // that are not in conflicted state.
    for (QGesture *gesture : gestures) {
        if (!gesture->hasHotSpot())
            continue;
        const Qt::GestureType gestureType = gesture->gestureType();
        const QList<QGraphicsItem *> items = itemsAtPosition(QPoint(), gesture->d_func()->sceneHotSpot, nullptr);
        for (int j = 0; j < items.size(); ++j) {
            QGraphicsItem *item = items.at(j);

            // Check if the item is blocked by a modal panel and use it as
            // a target instead of this item.
            (void) item->isBlockedByModalPanel(&item);

            if (QGraphicsObject *itemobj = item->toGraphicsObject()) {
                QGraphicsItemPrivate *d = item->QGraphicsItem::d_func();
                QMap<Qt::GestureType, Qt::GestureFlags>::const_iterator it =
                        d->gestureContext.constFind(gestureType);
                if (it != d->gestureContext.constEnd() && (!flag || (it.value() & flag))) {
                    if (normalGestures.contains(gesture)) {
                        normalGestures.remove(gesture);
                        if (conflicts)
                            conflicts->insert(gesture);
                    } else {
                        normalGestures.insert(gesture);
                    }
                    if (targets)
                        (*targets)[itemobj].insert(gesture);
                    if (itemsSet)
                        (*itemsSet).insert(itemobj);
                }
            }
            // Don't propagate through panels.
            if (item->isPanel())
                break;
        }
    }
    if (normal)
        *normal = normalGestures;
}
#endif  // !defined(QT_NO_GESTURES)

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

//  void QGraphicsScenePrivate::_q_processDirtyItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate20_q_processDirtyItemsEv(
    QGraphicsScenePrivate *self) {
  self->_q_processDirtyItems();
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

#if QT_CONFIG(graphicseffect)
//  void QGraphicsScenePrivate::drawItems(QPainter *painter, const QTransform
//      *const viewTransform, QRegion *exposedRegion, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate9drawItemsEP8QPainterPK10QTransformP7QRegionP7QWidget(
    QGraphicsScenePrivate *self,
    QPainter *painter,
    const QTransform *const viewTransform,
    QRegion *exposedRegion,
    QWidget *widget) {
  self->drawItems(painter, viewTransform, exposedRegion, widget);
}
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
//  void QGraphicsScenePrivate::drawSubtreeRecursive(QGraphicsItem *item,
//      QPainter *painter, const QTransform *const a2, QRegion
//      *exposedRegion, QWidget *widget, qreal parentOpacity, const
//      QTransform *const effectTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate20drawSubtreeRecursiveEP13QGraphicsItemP8QPainterPK10QTransformP7QRegionP7QWidgetdS6_(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    QPainter *painter,
    const QTransform *const a2,
    QRegion *exposedRegion,
    QWidget *widget,
    qreal parentOpacity,
    const QTransform *const effectTransform) {
  self->drawSubtreeRecursive(
      item,
      painter,
      a2,
      exposedRegion,
      widget,
      parentOpacity,
      effectTransform);
}
#endif  // QT_CONFIG(graphicseffect)

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

//  void QGraphicsScenePrivate::processDirtyItemsRecursive(QGraphicsItem
//      *item, bool dirtyAncestorContainsChildren, qreal parentOpacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate26processDirtyItemsRecursiveEP13QGraphicsItembd(
    QGraphicsScenePrivate *self,
    QGraphicsItem *item,
    bool dirtyAncestorContainsChildren,
    qreal parentOpacity) {
  self->processDirtyItemsRecursive(
      item,
      dirtyAncestorContainsChildren,
      parentOpacity);
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

#if !defined(QT_NO_GESTURES)
//  void QGraphicsScenePrivate::gestureTargetsAtHotSpots(const QSet<QGesture
//      *> &gestures, Qt::GestureFlag flag, QHash<QGraphicsObject *,
//      QSet<QGesture *>> *targets, QSet<QGraphicsObject *> *itemsSet,
//      QSet<QGesture *> *normal, QSet<QGesture *> *conflicts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate24gestureTargetsAtHotSpotsERK4QSetIP8QGestureEN2Qt11GestureFlagEP5QHashIP15QGraphicsObjectS3_EPS0_ISA_EPS3_SF_(
    QGraphicsScenePrivate *self,
    const QSet<QGesture *> *gestures,
    Qt::GestureFlag flag,
    QHash<QGraphicsObject *, QSet<QGesture *>> *targets,
    QSet<QGraphicsObject *> *itemsSet,
    QSet<QGesture *> *normal,
    QSet<QGesture *> *conflicts) {
  self->gestureTargetsAtHotSpots(
      *gestures,
      flag,
      targets,
      itemsSet,
      normal,
      conflicts);
}
#endif  // !defined(QT_NO_GESTURES)

//  void QGraphicsScenePrivate::updateInputMethodSensitivityInViews()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsScenePrivate35updateInputMethodSensitivityInViewsEv(
    QGraphicsScenePrivate *self) {
  self->updateInputMethodSensitivityInViews();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
