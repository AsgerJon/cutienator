//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGraphicsItemCache::DeviceData::DeviceData()
extern "C" Q_DECL_EXPORT
QGraphicsItemCache::DeviceData *ritual_ZN18QGraphicsItemCache10DeviceDataC1Ev() {
  return new QGraphicsItemCache::DeviceData();
}

//  QGraphicsItemCache::DeviceData::~DeviceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemCache10DeviceDataD1Ev(
    QGraphicsItemCache::DeviceData *self) {
  delete self;
}

#endif  // QT_CONFIG(graphicsview)
