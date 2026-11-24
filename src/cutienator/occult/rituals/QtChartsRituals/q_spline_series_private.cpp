//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qsplineseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qsplineseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qsplineseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QSplineSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QSplineSeriesPrivate10metaObjectEv(
    const QSplineSeriesPrivate *self) {
  return self->metaObject();
}

//  QString QSplineSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QSplineSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplineSeriesPrivate::tr(s, c, n));
}

//  QSplineSeriesPrivate::QSplineSeriesPrivate(QSplineSeries *q)
extern "C" Q_DECL_EXPORT
QSplineSeriesPrivate *ritual_ZN20QSplineSeriesPrivateC1EP13QSplineSeries(
    QSplineSeries *q) {
  return new QSplineSeriesPrivate(q);
}

//  void QSplineSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSplineSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QSplineSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  void QSplineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSplineSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QSplineSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  QSplineSeries *QSplineSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSplineSeries *ritual_ZN20QSplineSeriesPrivate6q_funcEv(
    QSplineSeriesPrivate *self) {
  return self->q_func();
}

//  const QSplineSeries *QSplineSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSplineSeries *ritual_ZNK20QSplineSeriesPrivate6q_funcEv(
    const QSplineSeriesPrivate *self) {
  return self->q_func();
}

//  void QSplineSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSplineSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QSplineSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QSplineSeriesPrivate::initializeTheme(index, theme, forced);
}

//  void QSplineSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSplineSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QSplineSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QSplineSeriesPrivate::initializeGraphics(parent);
}
