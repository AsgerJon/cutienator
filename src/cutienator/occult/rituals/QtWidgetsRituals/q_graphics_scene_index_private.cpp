//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicssceneindex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
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

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
