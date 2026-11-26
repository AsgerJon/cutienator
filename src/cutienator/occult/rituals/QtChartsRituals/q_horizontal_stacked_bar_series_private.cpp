//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qhorizontalstackedbarseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qhorizontalstackedbarseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qhorizontalstackedbarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHorizontalStackedBarSeriesPrivate::QHorizontalStackedBarSeriesPrivate(QH
//      orizontalStackedBarSeries *q)
extern "C" Q_DECL_EXPORT
QHorizontalStackedBarSeriesPrivate *ritual_ZN34QHorizontalStackedBarSeriesPrivateC1EP27QHorizontalStackedBarSeries(
    QHorizontalStackedBarSeries *q) {
  return new QHorizontalStackedBarSeriesPrivate(q);
}

//  void QHorizontalStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QHorizontalStackedBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QHorizontalStackedBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QHorizontalStackedBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QHorizontalStackedBarSeriesPrivate16initializeDomainEv(
    QHorizontalStackedBarSeriesPrivate *self) {
  self->initializeDomain();
}

//  QHorizontalStackedBarSeries *QHorizontalStackedBarSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHorizontalStackedBarSeries *ritual_ZN34QHorizontalStackedBarSeriesPrivate6q_funcEv(
    QHorizontalStackedBarSeriesPrivate *self) {
  return self->q_func();
}

//  const QHorizontalStackedBarSeries
//      *QHorizontalStackedBarSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHorizontalStackedBarSeries *ritual_ZNK34QHorizontalStackedBarSeriesPrivate6q_funcEv(
    const QHorizontalStackedBarSeriesPrivate *self) {
  return self->q_func();
}

//  void QHorizontalStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QHorizontalStackedBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QHorizontalStackedBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QHorizontalStackedBarSeriesPrivate::initializeGraphics(parent);
}

//  void QHorizontalStackedBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QHorizontalStackedBarSeriesPrivate16initializeDomainEv(
    QHorizontalStackedBarSeriesPrivate *self) {
  self->QHorizontalStackedBarSeriesPrivate::initializeDomain();
}

#endif  // QT_CONFIG(charts_bar_chart)
