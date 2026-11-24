//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qchartview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qchartview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QChartViewPrivate::QChartViewPrivate(QChartView *q, QChart *chart)
extern "C" Q_DECL_EXPORT
QChartViewPrivate *ritual_ZN17QChartViewPrivateC1EP10QChartViewP6QChart(
    QChartView *q,
    QChart *chart) {
  return new QChartViewPrivate(q, chart);
}

//  QChartViewPrivate::~QChartViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QChartViewPrivateD1Ev(QChartViewPrivate *self) {
  delete self;
}

//  void QChartViewPrivate::setChart(QChart *chart)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QChartViewPrivate8setChartEP6QChart(
    QChartViewPrivate *self,
    QChart *chart) {
  self->setChart(chart);
}

//  void QChartViewPrivate::resize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QChartViewPrivate6resizeEv(QChartViewPrivate *self) {
  self->resize();
}
