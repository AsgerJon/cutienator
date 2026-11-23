//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenelinearindex_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsscenelinearindex_p.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#include "qdebug.h"
#include "qgraphicsscene.h"
#include "qgraphicsitem_p.h"
#include "qgraphicsscene_p.h"
#include "qgraphicswidget.h"
#include "qgraphicssceneindex_p.h"
#include "qgraphicsscenebsptreeindex_p.h"
#include <QtGui/qpainterpath.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/graphicsview/qgraphicssceneindex.cpp, line 318, as _ZN19QGraphicsSceneIndexC2EP14QGraphicsScene
inline QGraphicsSceneIndex::QGraphicsSceneIndex(QGraphicsScene *scene)
: QObject(*new QGraphicsSceneIndexPrivate(scene), scene)
{
    d_func()->init();
}
//  -----------------------------------------------------------------------

//  Only a class built on QGraphicsSceneLinearIndex may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsSceneLinearIndex : QGraphicsSceneLinearIndex {
  using QGraphicsSceneLinearIndex::clear;
  using QGraphicsSceneLinearIndex::addItem;
  using QGraphicsSceneLinearIndex::removeItem;
};

//  const QMetaObject *QGraphicsSceneLinearIndex::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QGraphicsSceneLinearIndex10metaObjectEv(
    const QGraphicsSceneLinearIndex *self) {
  return self->metaObject();
}

//  QList<QGraphicsItem *> QGraphicsSceneLinearIndex::items(Qt::SortOrder
//      order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK25QGraphicsSceneLinearIndex5itemsEN2Qt9SortOrderE(
    const QGraphicsSceneLinearIndex *self,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->items(order));
}

//  QList<QGraphicsItem *> QGraphicsSceneLinearIndex::estimateItems(const
//      QRectF &rect, Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK25QGraphicsSceneLinearIndex13estimateItemsERK6QRectFN2Qt9SortOrderE(
    const QGraphicsSceneLinearIndex *self,
    const QRectF *rect,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->estimateItems(*rect, order));
}

//  void QGraphicsSceneLinearIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneLinearIndex5clearEv(
    QGraphicsSceneLinearIndex *self) {
  self->clear();
}

//  void QGraphicsSceneLinearIndex::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneLinearIndex7addItemEP13QGraphicsItem(
    QGraphicsSceneLinearIndex *self,
    QGraphicsItem *item) {
  self->addItem(item);
}

//  void QGraphicsSceneLinearIndex::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneLinearIndex10removeItemEP13QGraphicsItem(
    QGraphicsSceneLinearIndex *self,
    QGraphicsItem *item) {
  self->removeItem(item);
}

//  void QGraphicsSceneLinearIndex::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGraphicsSceneLinearIndex5clearEv(
    QGraphicsSceneLinearIndex *self) {
  static_cast<OwnQGraphicsSceneLinearIndex *>(self)->OwnQGraphicsSceneLinearIndex::clear();
}

//  void QGraphicsSceneLinearIndex::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGraphicsSceneLinearIndex7addItemEP13QGraphicsItem(
    QGraphicsSceneLinearIndex *self,
    QGraphicsItem *item) {
  static_cast<OwnQGraphicsSceneLinearIndex *>(self)->OwnQGraphicsSceneLinearIndex::addItem(
      item);
}

//  void QGraphicsSceneLinearIndex::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGraphicsSceneLinearIndex10removeItemEP13QGraphicsItem(
    QGraphicsSceneLinearIndex *self,
    QGraphicsItem *item) {
  static_cast<OwnQGraphicsSceneLinearIndex *>(self)->OwnQGraphicsSceneLinearIndex::removeItem(
      item);
}
