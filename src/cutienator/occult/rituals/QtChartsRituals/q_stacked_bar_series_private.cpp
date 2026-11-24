//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qstackedbarseries_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qstackedbarseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qstackedbarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStackedBarSeriesPrivate::QStackedBarSeriesPrivate(QStackedBarSeries *q)
extern "C" Q_DECL_EXPORT
QStackedBarSeriesPrivate *ritual_ZN24QStackedBarSeriesPrivateC1EP17QStackedBarSeries(
    QStackedBarSeries *q) {
  return new QStackedBarSeriesPrivate(q);
}

//  void QStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QStackedBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QStackedBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QStackedBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QStackedBarSeriesPrivate16initializeDomainEv(
    QStackedBarSeriesPrivate *self) {
  self->initializeDomain();
}

//  QStackedBarSeries *QStackedBarSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QStackedBarSeries *ritual_ZN24QStackedBarSeriesPrivate6q_funcEv(
    QStackedBarSeriesPrivate *self) {
  return self->q_func();
}

//  const QStackedBarSeries *QStackedBarSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStackedBarSeries *ritual_ZNK24QStackedBarSeriesPrivate6q_funcEv(
    const QStackedBarSeriesPrivate *self) {
  return self->q_func();
}

//  void QStackedBarSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QStackedBarSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QStackedBarSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QStackedBarSeriesPrivate::initializeGraphics(parent);
}

//  void QStackedBarSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QStackedBarSeriesPrivate16initializeDomainEv(
    QStackedBarSeriesPrivate *self) {
  self->QStackedBarSeriesPrivate::initializeDomain();
}
