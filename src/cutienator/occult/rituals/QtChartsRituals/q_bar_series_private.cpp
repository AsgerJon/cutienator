//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qbarseries_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qbarseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qbarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBarSeriesPrivate::QBarSeriesPrivate(QBarSeries *q)
extern "C" Q_DECL_EXPORT
QBarSeriesPrivate *ritual_ZN17QBarSeriesPrivateC1EP10QBarSeries(
    QBarSeries *q) {
  return new QBarSeriesPrivate(q);
}

//  void QBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBarSeriesPrivate16initializeDomainEv(
    QBarSeriesPrivate *self) {
  self->initializeDomain();
}

//  QBarSeries *QBarSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarSeries *ritual_ZN17QBarSeriesPrivate6q_funcEv(QBarSeriesPrivate *self) {
  return self->q_func();
}

//  const QBarSeries *QBarSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarSeries *ritual_ZNK17QBarSeriesPrivate6q_funcEv(
    const QBarSeriesPrivate *self) {
  return self->q_func();
}

//  void QBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QBarSeriesPrivate::initializeGraphics(parent);
}

//  void QBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QBarSeriesPrivate16initializeDomainEv(
    QBarSeriesPrivate *self) {
  self->QBarSeriesPrivate::initializeDomain();
}

#endif  // QT_CONFIG(charts_bar_chart)
