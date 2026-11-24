//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_scatter_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpolygon.h>

//  StarMarker::StarMarker(qreal x, qreal y, qreal w, qreal h,
//      ScatterChartItem *parent)
extern "C" Q_DECL_EXPORT
StarMarker *ritual_ZN10StarMarkerC1EddddP16ScatterChartItem(
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    ScatterChartItem *parent) {
  return new StarMarker(x, y, w, h, parent);
}

//  QPolygonF StarMarker::polygon(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN10StarMarker7polygonEdddd(
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  return new QPolygonF(StarMarker::polygon(x, y, w, h));
}

#endif  // QT_CONFIG(charts_scatter_chart)
