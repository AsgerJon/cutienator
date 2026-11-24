//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qscatterseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_scatter_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qscatterseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qscatterseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScatterSeriesPrivate::QScatterSeriesPrivate(QScatterSeries *q)
extern "C" Q_DECL_EXPORT
QScatterSeriesPrivate *ritual_ZN21QScatterSeriesPrivateC1EP14QScatterSeries(
    QScatterSeries *q) {
  return new QScatterSeriesPrivate(q);
}

//  void QScatterSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScatterSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QScatterSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QScatterSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScatterSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QScatterSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  QScatterSeries *QScatterSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScatterSeries *ritual_ZN21QScatterSeriesPrivate6q_funcEv(
    QScatterSeriesPrivate *self) {
  return self->q_func();
}

//  const QScatterSeries *QScatterSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScatterSeries *ritual_ZNK21QScatterSeriesPrivate6q_funcEv(
    const QScatterSeriesPrivate *self) {
  return self->q_func();
}

//  void QScatterSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScatterSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QScatterSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QScatterSeriesPrivate::initializeGraphics(parent);
}

//  void QScatterSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScatterSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QScatterSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QScatterSeriesPrivate::initializeTheme(index, theme, forced);
}

#endif  // QT_CONFIG(charts_scatter_chart)
