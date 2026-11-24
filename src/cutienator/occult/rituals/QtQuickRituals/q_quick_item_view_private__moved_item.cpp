//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickItemViewPrivate::MovedItem::MovedItem(FxViewItem *i,
//      QQmlChangeSet::MoveKey k)
extern "C" Q_DECL_EXPORT
QQuickItemViewPrivate::MovedItem *ritual_ZN21QQuickItemViewPrivate9MovedItemC1EP10FxViewItemN13QQmlChangeSet7MoveKeyE(
    FxViewItem *i,
    const QQmlChangeSet::MoveKey *k) {
  return new QQuickItemViewPrivate::MovedItem(i, *k);
}

//  QQuickItemViewPrivate::MovedItem::~MovedItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate9MovedItemD1Ev(
    QQuickItemViewPrivate::MovedItem *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_itemview)
