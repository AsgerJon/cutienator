//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickItemPrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickItemPrivate::ExtraData *ritual_ZN17QQuickItemPrivate9ExtraDataC1Ev() {
  return new QQuickItemPrivate::ExtraData();
}

//  QQuickItemPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate9ExtraDataD1Ev(
    QQuickItemPrivate::ExtraData *self) {
  delete self;
}
