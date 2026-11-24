//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpolygon.h>

//  RotatedRectangleMarker::RotatedRectangleMarker(qreal x, qreal y, qreal w,
//      qreal h, ScatterChartItem *parent)
extern "C" Q_DECL_EXPORT
RotatedRectangleMarker *ritual_ZN22RotatedRectangleMarkerC1EddddP16ScatterChartItem(
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    ScatterChartItem *parent) {
  return new RotatedRectangleMarker(x, y, w, h, parent);
}

//  QPolygonF RotatedRectangleMarker::polygon(qreal x, qreal y, qreal w,
//      qreal h)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN22RotatedRectangleMarker7polygonEdddd(
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(RotatedRectangleMarker::polygon(x, y, w, h));
}
