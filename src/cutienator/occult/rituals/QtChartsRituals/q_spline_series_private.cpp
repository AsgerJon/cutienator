//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qsplineseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtCharts/qsplineseries.h>
#endif
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

//  void *QSplineSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QSplineSeriesPrivate11qt_metacastEPKc(
    QSplineSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSplineSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QSplineSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QSplineSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QSplineSeriesPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSplineSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QSplineSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
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

#endif  // QT_CONFIG(charts_spline_chart)
