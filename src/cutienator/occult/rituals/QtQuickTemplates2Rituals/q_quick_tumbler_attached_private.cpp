//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicktumbler_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickflickable_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquicktumbler_p_p.h>
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquicktumbler.cpp, line 64, as local:qquicktumbler.cpp:delegateHeight
namespace {
static inline qreal delegateHeight(const QQuickTumbler *tumbler)
    {
        return tumbler->availableHeight() / tumbler->visibleItemCount();
    }
}  // namespace

//  from ../qtdeclarative/src/quicktemplates/qquicktumbler.cpp, line 932, as _ZN28QQuickTumblerAttachedPrivate4initEP10QQuickItem
inline void QQuickTumblerAttachedPrivate::init(QQuickItem *delegateItem)
{
    Q_Q(QQuickTumblerAttached);
    if (!delegateItem->parentItem()) {
        qmlWarning(q) << "Tumbler: attached properties must be accessed through a delegate item that has a parent";
        return;
    }

    QVariant indexContextProperty = qmlContext(delegateItem)->contextProperty(QStringLiteral("index"));
    if (!indexContextProperty.isValid()) {
        qmlWarning(q) << "Tumbler: attempting to access attached property on item without an \"index\" property";
        return;
    }

    index = indexContextProperty.toInt();

    QQuickItem *parentItem = delegateItem;
    while ((parentItem = parentItem->parentItem())) {
        if ((tumbler = qobject_cast<QQuickTumbler*>(parentItem)))
            break;
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktumbler.cpp, line 955, as _ZN28QQuickTumblerAttachedPrivate21calculateDisplacementEv
inline void QQuickTumblerAttachedPrivate::calculateDisplacement()
{
    const qreal previousDisplacement = displacement;
    displacement = 0;

    if (!tumbler) {
        // Can happen if the attached properties are accessed on the wrong type of item or the tumbler was destroyed.
        // We don't want to emit the change signal though, as this could cause warnings about Tumbler.tumbler being null.
        return;
    }

    // Can happen if there is no ListView or PathView within the contentItem.
    QQuickTumblerPrivate *tumblerPrivate = QQuickTumblerPrivate::get(tumbler);
    if (!tumblerPrivate->viewContentItem) {
        emitIfDisplacementChanged(previousDisplacement, displacement);
        return;
    }

    // The attached property gets created before our count is updated, so just cheat here
    // to avoid having to listen to count changes.
    const int count = tumblerPrivate->view->property("count").toInt();
    // This can happen in tests, so it may happen in normal usage too.
    if (count == 0) {
        emitIfDisplacementChanged(previousDisplacement, displacement);
        return;
    }

    if (tumblerPrivate->viewContentItemType == QQuickTumblerPrivate::PathViewContentItem) {
        const qreal offset = tumblerPrivate->viewOffset;

        displacement = count > 1 ? count - index - offset : 0;
        // Don't add 1 if count <= visibleItemCount
        const int visibleItems = tumbler->visibleItemCount();
        const int halfVisibleItems = visibleItems / 2 + (visibleItems < count ? 1 : 0);
        if (displacement > halfVisibleItems)
            displacement -= count;
        else if (displacement < -halfVisibleItems)
            displacement += count;
    } else {
        const qreal contentY = tumblerPrivate->viewContentY;
        const qreal delegateH = delegateHeight(tumbler);
        const qreal preferredHighlightBegin = tumblerPrivate->view->property("preferredHighlightBegin").toReal();
        const qreal itemY = qobject_cast<QQuickItem*>(parent)->y();
        qreal currentItemY = 0;
        auto currentItem = tumblerPrivate->view->property("currentItem").value<QQuickItem*>();
        if (currentItem)
            currentItemY = currentItem->y();
        // Start from the y position of the current item.
        const qreal topOfCurrentItemInViewport = currentItemY - contentY;
        // Then, calculate the distance between it and the preferredHighlightBegin.
        const qreal relativePositionToPreferredHighlightBegin = topOfCurrentItemInViewport - preferredHighlightBegin;
        // Next, calculate the distance between us and the current item.
        const qreal distanceFromCurrentItem = currentItemY - itemY;
        const qreal displacementInPixels = distanceFromCurrentItem - relativePositionToPreferredHighlightBegin;
        // Convert it from pixels to a floating point index.
        displacement = displacementInPixels / delegateH;
    }

    emitIfDisplacementChanged(previousDisplacement, displacement);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktumbler.cpp, line 1016, as _ZN28QQuickTumblerAttachedPrivate25emitIfDisplacementChangedEdd
inline void QQuickTumblerAttachedPrivate::emitIfDisplacementChanged(qreal oldDisplacement, qreal newDisplacement)
{
    Q_Q(QQuickTumblerAttached);
    if (newDisplacement != oldDisplacement)
        emit q->displacementChanged();
}
//  -----------------------------------------------------------------------

//  QQuickTumblerAttached *QQuickTumblerAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTumblerAttached *ritual_ZN28QQuickTumblerAttachedPrivate6q_funcEv(
    QQuickTumblerAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickTumblerAttached *QQuickTumblerAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTumblerAttached *ritual_ZNK28QQuickTumblerAttachedPrivate6q_funcEv(
    const QQuickTumblerAttachedPrivate *self) {
  return self->q_func();
}

//  QQuickTumblerAttachedPrivate
//      *QQuickTumblerAttachedPrivate::get(QQuickTumblerAttached *attached)
extern "C" Q_DECL_EXPORT
QQuickTumblerAttachedPrivate *ritual_ZN28QQuickTumblerAttachedPrivate3getEP21QQuickTumblerAttached(
    QQuickTumblerAttached *attached) {
  return QQuickTumblerAttachedPrivate::get(attached);
}

//  void QQuickTumblerAttachedPrivate::init(QQuickItem *delegateItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTumblerAttachedPrivate4initEP10QQuickItem(
    QQuickTumblerAttachedPrivate *self,
    QQuickItem *delegateItem) {
  self->init(delegateItem);
}

//  void QQuickTumblerAttachedPrivate::calculateDisplacement()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTumblerAttachedPrivate21calculateDisplacementEv(
    QQuickTumblerAttachedPrivate *self) {
  self->calculateDisplacement();
}

//  void QQuickTumblerAttachedPrivate::emitIfDisplacementChanged(qreal
//      oldDisplacement, qreal newDisplacement)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickTumblerAttachedPrivate25emitIfDisplacementChangedEdd(
    QQuickTumblerAttachedPrivate *self,
    qreal oldDisplacement,
    qreal newDisplacement) {
  self->emitIfDisplacementChanged(oldDisplacement, newDisplacement);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
