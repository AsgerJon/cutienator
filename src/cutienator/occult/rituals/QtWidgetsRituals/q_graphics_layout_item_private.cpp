//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qglobal.h"
#include "qgraphicslayout.h"
#include "qgraphicsscene.h"
#include "qgraphicslayoutitem.h"
#include "qgraphicslayoutitem_p.h"
#include "qwidget.h"
#include "qgraphicswidget.h"
#include "qgraphicsitem_p.h"
#include <QtDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 90, as _ZN26QGraphicsLayoutItemPrivate4initEv
inline void QGraphicsLayoutItemPrivate::init()
{
    sizeHintCacheDirty = true;
    sizeHintWithConstraintCacheDirty = true;
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 175, as _ZNK26QGraphicsLayoutItemPrivate10parentItemEv
inline QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem() const
{
    Q_Q(const QGraphicsLayoutItem);

    const QGraphicsLayoutItem *parent = q;
    while (parent && parent->isLayout()) {
        parent = parent->parentLayoutItem();
    }
    return parent ? parent->graphicsItem() : nullptr;
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 192, as _ZN26QGraphicsLayoutItemPrivate19ensureUserSizeHintsEv
inline void QGraphicsLayoutItemPrivate::ensureUserSizeHints()
{
    if (!userSizeHints)
        userSizeHints = new QSizeF[Qt::NSizeHints];
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 203, as _ZN26QGraphicsLayoutItemPrivate7setSizeEN2Qt8SizeHintERK6QSizeF
inline void QGraphicsLayoutItemPrivate::setSize(Qt::SizeHint which, const QSizeF &size)
{
    Q_Q(QGraphicsLayoutItem);

    if (userSizeHints) {
        if (size == userSizeHints[which])
            return;
    } else if (size.width() < 0 && size.height() < 0) {
        return;
    }

    ensureUserSizeHints();
    userSizeHints[which] = size;
    q->updateGeometry();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 224, as _ZN26QGraphicsLayoutItemPrivate16setSizeComponentEN2Qt8SizeHintENS_13SizeComponentEd
inline void QGraphicsLayoutItemPrivate::setSizeComponent(
    Qt::SizeHint which, SizeComponent component, qreal value)
{
    Q_Q(QGraphicsLayoutItem);
    ensureUserSizeHints();
    qreal &userValue = (component == Width)
        ? userSizeHints[which].rwidth()
        : userSizeHints[which].rheight();
    if (value == userValue)
        return;
    userValue = value;
    q->updateGeometry();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 239, as _ZNK26QGraphicsLayoutItemPrivate17hasHeightForWidthEv
inline bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasHeightForWidth())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasHeightForWidth();
            }
        }
    }
    return q->sizePolicy().hasHeightForWidth();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 259, as _ZNK26QGraphicsLayoutItemPrivate17hasWidthForHeightEv
inline bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasWidthForHeight())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasWidthForHeight();
            }
        }
    }
    return q->sizePolicy().hasWidthForHeight();
}
//  -----------------------------------------------------------------------

//  QGraphicsLayoutItem *QGraphicsLayoutItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZN26QGraphicsLayoutItemPrivate6q_funcEv(
    QGraphicsLayoutItemPrivate *self) {
  return self->q_func();
}

//  const QGraphicsLayoutItem *QGraphicsLayoutItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsLayoutItem *ritual_ZNK26QGraphicsLayoutItemPrivate6q_funcEv(
    const QGraphicsLayoutItemPrivate *self) {
  return self->q_func();
}

//  QGraphicsLayoutItemPrivate::~QGraphicsLayoutItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsLayoutItemPrivateD1Ev(
    QGraphicsLayoutItemPrivate *self) {
  delete self;
}

//  QGraphicsLayoutItemPrivate
//      *QGraphicsLayoutItemPrivate::get(QGraphicsLayoutItem *q)
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItemPrivate *ritual_ZN26QGraphicsLayoutItemPrivate3getEP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *q) {
  return QGraphicsLayoutItemPrivate::get(q);
}

//  const QGraphicsLayoutItemPrivate *QGraphicsLayoutItemPrivate::get(const
//      QGraphicsLayoutItem *q)
extern "C" Q_DECL_EXPORT
const QGraphicsLayoutItemPrivate *ritual_ZN26QGraphicsLayoutItemPrivate3getEPK19QGraphicsLayoutItem(
    const QGraphicsLayoutItem *q) {
  return QGraphicsLayoutItemPrivate::get(q);
}

//  void QGraphicsLayoutItemPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsLayoutItemPrivate4initEv(
    QGraphicsLayoutItemPrivate *self) {
  self->init();
}

//  QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK26QGraphicsLayoutItemPrivate10parentItemEv(
    const QGraphicsLayoutItemPrivate *self) {
  return self->parentItem();
}

//  void QGraphicsLayoutItemPrivate::ensureUserSizeHints()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsLayoutItemPrivate19ensureUserSizeHintsEv(
    QGraphicsLayoutItemPrivate *self) {
  self->ensureUserSizeHints();
}

//  void QGraphicsLayoutItemPrivate::setSize(Qt::SizeHint which, const QSizeF
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsLayoutItemPrivate7setSizeEN2Qt8SizeHintERK6QSizeF(
    QGraphicsLayoutItemPrivate *self,
    Qt::SizeHint which,
    const QSizeF *size) {
  self->setSize(which, *size);
}

//  void QGraphicsLayoutItemPrivate::setSizeComponent(Qt::SizeHint which,
//      SizeComponent component, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGraphicsLayoutItemPrivate16setSizeComponentEN2Qt8SizeHintENS_13SizeComponentEd(
    QGraphicsLayoutItemPrivate *self,
    Qt::SizeHint which,
    QGraphicsLayoutItemPrivate::SizeComponent component,
    qreal value) {
  self->setSizeComponent(which, component, value);
}

//  bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QGraphicsLayoutItemPrivate17hasHeightForWidthEv(
    const QGraphicsLayoutItemPrivate *self) {
  return self->hasHeightForWidth();
}

//  bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QGraphicsLayoutItemPrivate17hasWidthForHeightEv(
    const QGraphicsLayoutItemPrivate *self) {
  return self->hasWidthForHeight();
}

#endif  // QT_CONFIG(graphicsview)
