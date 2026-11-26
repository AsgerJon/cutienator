//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 179, as _ZN26QGraphicsSceneIndexPrivateC1EP14QGraphicsScene
inline QGraphicsSceneIndexPrivate::QGraphicsSceneIndexPrivate(QGraphicsScene *scene) : scene(scene)
{
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 186, as _ZN26QGraphicsSceneIndexPrivateD1Ev
inline QGraphicsSceneIndexPrivate::~QGraphicsSceneIndexPrivate()
{
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 306, as _ZN26QGraphicsSceneIndexPrivate4initEv
inline void QGraphicsSceneIndexPrivate::init()
{
    if (!scene)
        return;

    QObject::connect(scene, SIGNAL(sceneRectChanged(QRectF)),
                     q_func(), SLOT(updateSceneRect(QRectF)));
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 196, as _ZN26QGraphicsSceneIndexPrivate20itemCollidesWithPathEPK13QGraphicsItemRK12QPainterPathN2Qt17ItemSelectionModeE
inline bool QGraphicsSceneIndexPrivate::itemCollidesWithPath(const QGraphicsItem *item,
                                                      const QPainterPath &path,
                                                      Qt::ItemSelectionMode mode)
{
    if (item->collidesWithPath(path, mode))
        return true;
    if (item->isWidget()) {
        // Check if this is a window, and if its frame rect collides.
        const QGraphicsWidget *widget = static_cast<const QGraphicsWidget *>(item);
        if (widget->isWindow()) {
            QRectF frameRect = widget->windowFrameRect();
            QPainterPath framePath;
            framePath.addRect(frameRect);
            bool intersects = path.intersects(frameRect);
            if (mode == Qt::IntersectsItemShape || mode == Qt::IntersectsItemBoundingRect)
                return intersects || path.contains(frameRect.topLeft())
                    || framePath.contains(path.elementAt(0));
            return !intersects && path.contains(frameRect.topLeft());
        }
    }
    return false;
}

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 223, as _ZNK26QGraphicsSceneIndexPrivate22recursive_items_helperEP13QGraphicsItem6QRectFPFbPKS0_RKS2_N2Qt17ItemSelectionModeERK10QTransformPKvEP5QListIS1_ESB_S8_dSD_
inline void QGraphicsSceneIndexPrivate::recursive_items_helper(QGraphicsItem *item, QRectF exposeRect,
                                                        QGraphicsSceneIndexIntersector intersect,
                                                        QList<QGraphicsItem *> *items,
                                                        const QTransform &viewTransform,
                                                        Qt::ItemSelectionMode mode,
                                                        qreal parentOpacity, const void *intersectData) const
{
    Q_ASSERT(item);
    if (!item->d_ptr->visible)
        return;

    const qreal opacity = item->d_ptr->combineOpacityFromParent(parentOpacity);
    const bool itemIsFullyTransparent = QGraphicsItemPrivate::isOpacityNull(opacity);
    const bool itemHasChildren = !item->d_ptr->children.isEmpty();
    if (itemIsFullyTransparent && (!itemHasChildren || item->d_ptr->childrenCombineOpacity()))
        return;

    // Update the item's scene transform if dirty.
    const bool itemIsUntransformable = item->d_ptr->itemIsUntransformable();
    const bool wasDirtyParentSceneTransform = item->d_ptr->dirtySceneTransform && !itemIsUntransformable;
    if (wasDirtyParentSceneTransform) {
        item->d_ptr->updateSceneTransformFromParent();
        Q_ASSERT(!item->d_ptr->dirtySceneTransform);
    }

    const bool itemClipsChildrenToShape = (item->d_ptr->flags & QGraphicsItem::ItemClipsChildrenToShape
                                           || item->d_ptr->flags & QGraphicsItem::ItemContainsChildrenInShape);
    bool processItem = !itemIsFullyTransparent;
    if (processItem) {
        processItem = intersect(item, exposeRect, mode, viewTransform, intersectData);
        if (!processItem && (!itemHasChildren || itemClipsChildrenToShape)) {
            if (wasDirtyParentSceneTransform)
                item->d_ptr->invalidateChildrenSceneTransform();
            return;
        }
    } // else we know for sure this item has children we must process.

    int i = 0;
    if (itemHasChildren) {
        // Sort children.
        item->d_ptr->ensureSortedChildren();

        // Clip to shape.
        if (itemClipsChildrenToShape && !itemIsUntransformable) {
            QPainterPath mappedShape = item->d_ptr->sceneTransformTranslateOnly
                                     ? item->shape().translated(item->d_ptr->sceneTransform.dx(),
                                                                item->d_ptr->sceneTransform.dy())
                                     : item->d_ptr->sceneTransform.map(item->shape());
            exposeRect &= mappedShape.controlPointRect();
        }

        // Process children behind
        for (i = 0; i < item->d_ptr->children.size(); ++i) {
            QGraphicsItem *child = item->d_ptr->children.at(i);
            if (wasDirtyParentSceneTransform)
                child->d_ptr->dirtySceneTransform = 1;
            if (!(child->d_ptr->flags & QGraphicsItem::ItemStacksBehindParent))
                break;
            if (itemIsFullyTransparent && !(child->d_ptr->flags & QGraphicsItem::ItemIgnoresParentOpacity))
                continue;
            recursive_items_helper(child, exposeRect, intersect, items, viewTransform,
                                   mode, opacity, intersectData);
        }
    }

    // Process item
    if (processItem)
        items->append(item);

    // Process children in front
    if (itemHasChildren) {
        for (; i < item->d_ptr->children.size(); ++i) {
            QGraphicsItem *child = item->d_ptr->children.at(i);
            if (wasDirtyParentSceneTransform)
                child->d_ptr->dirtySceneTransform = 1;
            if (itemIsFullyTransparent && !(child->d_ptr->flags & QGraphicsItem::ItemIgnoresParentOpacity))
                continue;
            recursive_items_helper(child, exposeRect, intersect, items, viewTransform,
                                   mode, opacity, intersectData);
        }
    }
}
//  -----------------------------------------------------------------------

//  QGraphicsSceneIndex *QGraphicsSceneIndexPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneIndex *ritual_ZN26QGraphicsSceneIndexPrivate6q_funcEv(
    QGraphicsSceneIndexPrivate *self) {
  return self->q_func();
}

//  const QGraphicsSceneIndex *QGraphicsSceneIndexPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneIndex *ritual_ZNK26QGraphicsSceneIndexPrivate6q_funcEv(
    const QGraphicsSceneIndexPrivate *self) {
  return self->q_func();
}

//  QGraphicsSceneIndexPrivate::QGraphicsSceneIndexPrivate(QGraphicsScene
//      *scene)
extern "C" Q_DECL_EXPORT
QGraphicsSceneIndexPrivate *ritual_ZN26QGraphicsSceneIndexPrivateC1EP14QGraphicsScene(
    QGraphicsScene *scene) {
  return new QGraphicsSceneIndexPrivate(scene);
}

//  QGraphicsSceneIndexPrivate::~QGraphicsSceneIndexPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneIndexPrivateD1Ev(
    QGraphicsSceneIndexPrivate *self) {
  delete self;
}

//  void QGraphicsSceneIndexPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsSceneIndexPrivate4initEv(
    QGraphicsSceneIndexPrivate *self) {
  self->init();
}

//  bool QGraphicsSceneIndexPrivate::itemCollidesWithPath(const QGraphicsItem
//      *item, const QPainterPath &path, Qt::ItemSelectionMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QGraphicsSceneIndexPrivate20itemCollidesWithPathEPK13QGraphicsItemRK12QPainterPathN2Qt17ItemSelectionModeE(
    const QGraphicsItem *item,
    const QPainterPath *path,
    Qt::ItemSelectionMode mode) {
  return QGraphicsSceneIndexPrivate::itemCollidesWithPath(item, *path, mode);
}

//  void QGraphicsSceneIndexPrivate::recursive_items_helper(QGraphicsItem
//      *item, QRectF exposeRect, QGraphicsSceneIndexIntersector intersect,
//      QList<QGraphicsItem *> *items, const QTransform &viewTransform,
//      Qt::ItemSelectionMode mode, qreal parentOpacity, const void
//      *intersectData) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QGraphicsSceneIndexPrivate22recursive_items_helperEP13QGraphicsItem6QRectFPFbPKS0_RKS2_N2Qt17ItemSelectionModeERK10QTransformPKvEP5QListIS1_ESB_S8_dSD_(
    const QGraphicsSceneIndexPrivate *self,
    QGraphicsItem *item,
    const QRectF *exposeRect,
    void *intersect,
    QList<QGraphicsItem *> *items,
    const QTransform *viewTransform,
    Qt::ItemSelectionMode mode,
    qreal parentOpacity,
    const void *intersectData) {
  self->recursive_items_helper(
      item,
      *exposeRect,
      reinterpret_cast<QGraphicsSceneIndexIntersector>(intersect),
      items,
      *viewTransform,
      mode,
      parentOpacity,
      intersectData);
}

//  void QGraphicsSceneIndexPrivate::items_helper(const QRectF &rect,
//      QGraphicsSceneIndexIntersector intersect, QList<QGraphicsItem *>
//      *items, const QTransform &viewTransform, Qt::ItemSelectionMode mode,
//      Qt::SortOrder order, const void *intersectData) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QGraphicsSceneIndexPrivate12items_helperERK6QRectFPFbPK13QGraphicsItemS2_N2Qt17ItemSelectionModeERK10QTransformPKvEP5QListIPS3_ESA_S7_NS6_9SortOrderESC_(
    const QGraphicsSceneIndexPrivate *self,
    const QRectF *rect,
    void *intersect,
    QList<QGraphicsItem *> *items,
    const QTransform *viewTransform,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const void *intersectData) {
  self->items_helper(
      *rect,
      reinterpret_cast<QGraphicsSceneIndexIntersector>(intersect),
      items,
      *viewTransform,
      mode,
      order,
      intersectData);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
