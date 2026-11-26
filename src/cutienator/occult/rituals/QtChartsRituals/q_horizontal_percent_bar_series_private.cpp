//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qhorizontalpercentbarseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qhorizontalpercentbarseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qhorizontalpercentbarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHorizontalPercentBarSeriesPrivate::QHorizontalPercentBarSeriesPrivate(QH
//      orizontalPercentBarSeries *q)
extern "C" Q_DECL_EXPORT
QHorizontalPercentBarSeriesPrivate *ritual_ZN34QHorizontalPercentBarSeriesPrivateC1EP27QHorizontalPercentBarSeries(
    QHorizontalPercentBarSeries *q) {
  return new QHorizontalPercentBarSeriesPrivate(q);
}

//  void QHorizontalPercentBarSeriesPrivate::initializeGraphics(QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QHorizontalPercentBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QHorizontalPercentBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QHorizontalPercentBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QHorizontalPercentBarSeriesPrivate16initializeDomainEv(
    QHorizontalPercentBarSeriesPrivate *self) {
  self->initializeDomain();
}

//  QHorizontalPercentBarSeries *QHorizontalPercentBarSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHorizontalPercentBarSeries *ritual_ZN34QHorizontalPercentBarSeriesPrivate6q_funcEv(
    QHorizontalPercentBarSeriesPrivate *self) {
  return self->q_func();
}

//  const QHorizontalPercentBarSeries
//      *QHorizontalPercentBarSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHorizontalPercentBarSeries *ritual_ZNK34QHorizontalPercentBarSeriesPrivate6q_funcEv(
    const QHorizontalPercentBarSeriesPrivate *self) {
  return self->q_func();
}

//  void QHorizontalPercentBarSeriesPrivate::initializeGraphics(QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QHorizontalPercentBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QHorizontalPercentBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QHorizontalPercentBarSeriesPrivate::initializeGraphics(parent);
}

//  void QHorizontalPercentBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN34QHorizontalPercentBarSeriesPrivate16initializeDomainEv(
    QHorizontalPercentBarSeriesPrivate *self) {
  self->QHorizontalPercentBarSeriesPrivate::initializeDomain();
}

#endif  // QT_CONFIG(charts_bar_chart)
