//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qlineseries_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_line_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_line_chart)
#include <QtCharts/qlineseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qlineseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLineSeriesPrivate::QLineSeriesPrivate(QLineSeries *q)
extern "C" Q_DECL_EXPORT
QLineSeriesPrivate *ritual_ZN18QLineSeriesPrivateC1EP11QLineSeries(
    QLineSeries *q) {
  return new QLineSeriesPrivate(q);
}

//  void QLineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QLineSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QLineSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QLineSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QLineSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QLineSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  QLineSeries *QLineSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLineSeries *ritual_ZN18QLineSeriesPrivate6q_funcEv(
    QLineSeriesPrivate *self) {
  return self->q_func();
}

//  const QLineSeries *QLineSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLineSeries *ritual_ZNK18QLineSeriesPrivate6q_funcEv(
    const QLineSeriesPrivate *self) {
  return self->q_func();
}

//  void QLineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QLineSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QLineSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QLineSeriesPrivate::initializeGraphics(parent);
}

//  void QLineSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QLineSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QLineSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QLineSeriesPrivate::initializeTheme(index, theme, forced);
}

#endif  // QT_CONFIG(charts_line_chart)
