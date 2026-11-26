//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtCore/QtDebug>
#include <QtCore/qglobal.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 79, as local:qgraphicslayout_p.cpp:removeLayoutItemFromLayout
static bool removeLayoutItemFromLayout(QGraphicsLayout *lay, QGraphicsLayoutItem *layoutItem)
{
    if (!lay)
        return false;

    for (int i = lay->count() - 1; i >= 0; --i) {
        QGraphicsLayoutItem *child = lay->itemAt(i);
        if (child && child->isLayout()) {
            if (removeLayoutItemFromLayout(static_cast<QGraphicsLayout*>(child), layoutItem))
                return true;
        } else if (child == layoutItem) {
            lay->removeAt(i);
            return true;
        }
    }
    return false;
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 73, as _ZN26QGraphicsLayoutItemPrivateC2EP19QGraphicsLayoutItemb
inline QGraphicsLayoutItemPrivate::QGraphicsLayoutItemPrivate(QGraphicsLayoutItem *par, bool layout)
    : parent(par), userSizeHints(nullptr), isLayout(layout), ownedByLayout(false), graphicsItem(nullptr)
{
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 81, as _ZN26QGraphicsLayoutItemPrivateD2Ev
inline QGraphicsLayoutItemPrivate::~QGraphicsLayoutItemPrivate()
{
    // Remove any lazily allocated data
    delete[] userSizeHints;
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

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 19, as _ZN22QGraphicsLayoutPrivate18reparentChildItemsEP13QGraphicsItem
inline void QGraphicsLayoutPrivate::reparentChildItems(QGraphicsItem *newParent)
{
    Q_Q(QGraphicsLayout);
    int n =  q->count();
    //bool mwVisible = mw && mw->isVisible();
    for (int i = 0; i < n; ++i) {
        QGraphicsLayoutItem *layoutChild = q->itemAt(i);
        if (!layoutChild) {
            // Skip stretch items
            continue;
        }
        if (layoutChild->isLayout()) {
            QGraphicsLayout *l = static_cast<QGraphicsLayout*>(layoutChild);
            l->d_func()->reparentChildItems(newParent);
        } else if (QGraphicsItem *itemChild = layoutChild->graphicsItem()){
            QGraphicsItem *childParent = itemChild->parentItem();
#ifdef QT_DEBUG
            if (childParent && childParent != newParent && itemChild->isWidget() && qt_graphicsLayoutDebug()) {
                QGraphicsWidget *w = static_cast<QGraphicsWidget*>(layoutChild);
                qWarning("QGraphicsLayout::addChildLayout: widget %s \"%s\" in wrong parent; moved to correct parent",
                         w->metaObject()->className(), w->objectName().toLocal8Bit().constData());
            }
#endif
            if (childParent != newParent)
                itemChild->setParentItem(newParent);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 48, as _ZNK22QGraphicsLayoutPrivate9getMarginEPddN6QStyle11PixelMetricE
inline void QGraphicsLayoutPrivate::getMargin(qreal *result, qreal userMargin, QStyle::PixelMetric pm) const
{
    if (!result)
        return;
    Q_Q(const QGraphicsLayout);

    QGraphicsLayoutItem *parent = q->parentLayoutItem();
    if (userMargin >= 0.0) {
        *result = userMargin;
    } else if (!parent) {
        *result = 0.0;
    } else if (parent->isLayout()) {    // sublayouts have 0 margin by default
        *result = 0.0;
    } else {
        *result = 0.0;
        if (QGraphicsItem *layoutParentItem = parentItem()) {
            if (layoutParentItem->isWidget())
                *result = (qreal)static_cast<QGraphicsWidget*>(layoutParentItem)->style()->pixelMetric(pm, nullptr);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 70, as _ZNK22QGraphicsLayoutPrivate15visualDirectionEv
inline Qt::LayoutDirection QGraphicsLayoutPrivate::visualDirection() const
{
    if (QGraphicsItem *maybeWidget = parentItem()) {
        if (maybeWidget->isWidget())
            return static_cast<QGraphicsWidget*>(maybeWidget)->layoutDirection();
    }
    return QGuiApplication::layoutDirection();
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 108, as _ZN22QGraphicsLayoutPrivate18addChildLayoutItemEP19QGraphicsLayoutItem
inline void QGraphicsLayoutPrivate::addChildLayoutItem(QGraphicsLayoutItem *layoutItem)
{
    Q_Q(QGraphicsLayout);
    if (QGraphicsLayoutItem *maybeLayout = layoutItem->parentLayoutItem()) {
        if (maybeLayout->isLayout())
            removeLayoutItemFromLayout(static_cast<QGraphicsLayout*>(maybeLayout), layoutItem);
    }
    layoutItem->setParentLayoutItem(q);
    if (layoutItem->isLayout()) {
        if (QGraphicsItem *parItem = parentItem()) {
            static_cast<QGraphicsLayout*>(layoutItem)->d_func()->reparentChildItems(parItem);
        }
    } else {
        if (QGraphicsItem *item = layoutItem->graphicsItem()) {
            QGraphicsItem *newParent = parentItem();
            QGraphicsItem *oldParent = item->parentItem();
            if (oldParent == newParent || !newParent)
                return;

#ifdef QT_DEBUG
            if (oldParent && item->isWidget()) {
                QGraphicsWidget *w = static_cast<QGraphicsWidget*>(item);
                qWarning("QGraphicsLayout::addChildLayoutItem: %s \"%s\" in wrong parent; moved to correct parent",
                    w->metaObject()->className(), w->objectName().toLocal8Bit().constData());
            }
#endif

            item->setParentItem(newParent);
        }
    }
}

//  from src/widgets/graphicsview/qgraphicslayout_p.cpp, line 140, as _ZN22QGraphicsLayoutPrivate17activateRecursiveEP19QGraphicsLayoutItem
inline void QGraphicsLayoutPrivate::activateRecursive(QGraphicsLayoutItem *item)
{
    if (item->isLayout()) {
        QGraphicsLayout *layout = static_cast<QGraphicsLayout *>(item);
        if (layout->d_func()->activated) {
            if (QGraphicsLayout::instantInvalidatePropagation()) {
                return;
            } else {
                layout->invalidate();   // ### LOOKS SUSPICIOUSLY WRONG!!???
            }
        }

        for (int i = layout->count() - 1; i >= 0; --i) {
            QGraphicsLayoutItem *childItem = layout->itemAt(i);
            if (childItem)
                activateRecursive(childItem);
        }
        layout->d_func()->activated = true;
    }
}
//  -----------------------------------------------------------------------

//  QGraphicsLayout *QGraphicsLayoutPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsLayout *ritual_ZN22QGraphicsLayoutPrivate6q_funcEv(
    QGraphicsLayoutPrivate *self) {
  return self->q_func();
}

//  const QGraphicsLayout *QGraphicsLayoutPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsLayout *ritual_ZNK22QGraphicsLayoutPrivate6q_funcEv(
    const QGraphicsLayoutPrivate *self) {
  return self->q_func();
}

//  QGraphicsLayoutPrivate::QGraphicsLayoutPrivate()
extern "C" Q_DECL_EXPORT
QGraphicsLayoutPrivate *ritual_ZN22QGraphicsLayoutPrivateC1Ev() {
  return new QGraphicsLayoutPrivate();
}

//  void QGraphicsLayoutPrivate::reparentChildItems(QGraphicsItem *newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsLayoutPrivate18reparentChildItemsEP13QGraphicsItem(
    QGraphicsLayoutPrivate *self,
    QGraphicsItem *newParent) {
  self->reparentChildItems(newParent);
}

//  void QGraphicsLayoutPrivate::getMargin(qreal *result, qreal userMargin,
//      QStyle::PixelMetric pm) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QGraphicsLayoutPrivate9getMarginEPddN6QStyle11PixelMetricE(
    const QGraphicsLayoutPrivate *self,
    qreal *result,
    qreal userMargin,
    QStyle::PixelMetric pm) {
  self->getMargin(result, userMargin, pm);
}

//  Qt::LayoutDirection QGraphicsLayoutPrivate::visualDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK22QGraphicsLayoutPrivate15visualDirectionEv(
    const QGraphicsLayoutPrivate *self) {
  return self->visualDirection();
}

//  void QGraphicsLayoutPrivate::addChildLayoutItem(QGraphicsLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsLayoutPrivate18addChildLayoutItemEP19QGraphicsLayoutItem(
    QGraphicsLayoutPrivate *self,
    QGraphicsLayoutItem *item) {
  self->addChildLayoutItem(item);
}

//  void QGraphicsLayoutPrivate::activateRecursive(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsLayoutPrivate17activateRecursiveEP19QGraphicsLayoutItem(
    QGraphicsLayoutPrivate *self,
    QGraphicsLayoutItem *item) {
  self->activateRecursive(item);
}

//  QGraphicsLayoutPrivate::~QGraphicsLayoutPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsLayoutPrivateD1Ev(QGraphicsLayoutPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
