//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickItemPrivate::ChangeListener::ChangeListener(QQuickItemChangeListene
//      r *l, ChangeTypes t)
extern "C" Q_DECL_EXPORT
QQuickItemPrivate::ChangeListener *ritual_ZN17QQuickItemPrivate14ChangeListenerC1EP24QQuickItemChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuickItemChangeListener *l,
    int t) {
  return new QQuickItemPrivate::ChangeListener(
      l,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(t));
}

//  QQuickItemPrivate::ChangeListener::ChangeListener(QQuickItemChangeListene
//      r *l, QQuickGeometryChange gt)
extern "C" Q_DECL_EXPORT
QQuickItemPrivate::ChangeListener *ritual_ZN17QQuickItemPrivate14ChangeListenerC1EP24QQuickItemChangeListener20QQuickGeometryChange(
    QQuickItemChangeListener *l,
    const QQuickGeometryChange *gt) {
  return new QQuickItemPrivate::ChangeListener(l, *gt);
}

//  bool QQuickItemPrivate::ChangeListener::operator==(const ChangeListener
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate14ChangeListenereqERKS0_(
    const QQuickItemPrivate::ChangeListener *self,
    const QQuickItemPrivate::ChangeListener *other) {
  return self->operator==(*other);
}

//  QQuickItemPrivate::ChangeListener::~ChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate14ChangeListenerD1Ev(
    QQuickItemPrivate::ChangeListener *self) {
  delete self;
}
