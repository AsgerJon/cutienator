//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicstransform_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicstransform.h>
#endif
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicstransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qgraphicstransform.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtWidgets/private/qgraphicstransform_p.h>
#include <QtCore/QDebug>
#include <QtCore/qmath.h>
#include <QtCore/qnumeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicstransform.cpp, line 63, as _ZN25QGraphicsTransformPrivateD1Ev
inline QGraphicsTransformPrivate::~QGraphicsTransformPrivate()
{
}

//  from src/widgets/graphicsview/qgraphicstransform.cpp, line 67, as _ZN25QGraphicsTransformPrivate7setItemEP13QGraphicsItem
inline void QGraphicsTransformPrivate::setItem(QGraphicsItem *i)
{
    if (item == i)
        return;

    if (item) {
        Q_Q(QGraphicsTransform);
        QGraphicsItemPrivate *d_ptr = item->d_ptr.data();

        item->prepareGeometryChange();
        Q_ASSERT(d_ptr->transformData);
        d_ptr->transformData->graphicsTransforms.removeAll(q);
        d_ptr->dirtySceneTransform = 1;
        item = nullptr;
    }

    item = i;
}

//  from src/widgets/graphicsview/qgraphicstransform.cpp, line 86, as _ZN25QGraphicsTransformPrivate10updateItemEP13QGraphicsItem
inline void QGraphicsTransformPrivate::updateItem(QGraphicsItem *item)
{
    item->prepareGeometryChange();
    item->d_ptr->dirtySceneTransform = 1;
}
//  -----------------------------------------------------------------------

//  QGraphicsTransform *QGraphicsTransformPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsTransform *ritual_ZN25QGraphicsTransformPrivate6q_funcEv(
    QGraphicsTransformPrivate *self) {
  return self->q_func();
}

//  const QGraphicsTransform *QGraphicsTransformPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsTransform *ritual_ZNK25QGraphicsTransformPrivate6q_funcEv(
    const QGraphicsTransformPrivate *self) {
  return self->q_func();
}

//  QGraphicsTransformPrivate::QGraphicsTransformPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsTransformPrivate *ritual_ZN25QGraphicsTransformPrivateC1Ev() {
  return new QGraphicsTransformPrivate();
}

//  QGraphicsTransformPrivate::~QGraphicsTransformPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsTransformPrivateD1Ev(
    QGraphicsTransformPrivate *self) {
  delete self;
}

//  void QGraphicsTransformPrivate::setItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsTransformPrivate7setItemEP13QGraphicsItem(
    QGraphicsTransformPrivate *self,
    QGraphicsItem *item) {
  self->setItem(item);
}

//  void QGraphicsTransformPrivate::updateItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsTransformPrivate10updateItemEP13QGraphicsItem(
    QGraphicsItem *item) {
  QGraphicsTransformPrivate::updateItem(item);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
