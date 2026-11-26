//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qareaseries_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/qareaseries.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qareaseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QAreaSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAreaSeriesPrivate10metaObjectEv(
    const QAreaSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QAreaSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QAreaSeriesPrivate11qt_metacastEPKc(
    QAreaSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAreaSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QAreaSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAreaSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAreaSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAreaSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAreaSeriesPrivate::tr(s, c, n));
}

//  QAreaSeriesPrivate::QAreaSeriesPrivate(QLineSeries *upperSeries,
//      QLineSeries *lowerSeries, QAreaSeries *q)
extern "C" Q_DECL_EXPORT
QAreaSeriesPrivate *ritual_ZN18QAreaSeriesPrivateC1EP11QLineSeriesS1_P11QAreaSeries(
    QLineSeries *upperSeries,
    QLineSeries *lowerSeries,
    QAreaSeries *q) {
  return new QAreaSeriesPrivate(upperSeries, lowerSeries, q);
}

//  void QAreaSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate16initializeDomainEv(
    QAreaSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QAreaSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate14initializeAxesEv(
    QAreaSeriesPrivate *self) {
  self->initializeAxes();
}

//  void QAreaSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QAreaSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->initializeGraphics(parent);
}

//  void QAreaSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QAreaSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->initializeTheme(index, theme, forced);
}

//  void QAreaSeriesPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QAreaSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
}

//  QList<QLegendMarker *> QAreaSeriesPrivate::createLegendMarkers(QLegend
//      *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN18QAreaSeriesPrivate19createLegendMarkersEP7QLegend(
    QAreaSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType
//      QAreaSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK18QAreaSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QAreaSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis *QAreaSeriesPrivate::createDefaultAxis(Qt::Orientation a0)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK18QAreaSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QAreaSeriesPrivate *self,
    Qt::Orientation a0) {
  return self->createDefaultAxis(a0);
}

//  void QAreaSeriesPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAreaSeriesPrivate7updatedEv(QAreaSeriesPrivate *self) {
  self->updated();
}

//  QAreaSeries *QAreaSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN18QAreaSeriesPrivate6q_funcEv(
    QAreaSeriesPrivate *self) {
  return self->q_func();
}

//  const QAreaSeries *QAreaSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAreaSeries *ritual_ZNK18QAreaSeriesPrivate6q_funcEv(
    const QAreaSeriesPrivate *self) {
  return self->q_func();
}

//  void QAreaSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAreaSeriesPrivate16initializeDomainEv(
    QAreaSeriesPrivate *self) {
  self->QAreaSeriesPrivate::initializeDomain();
}

//  void QAreaSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAreaSeriesPrivate14initializeAxesEv(
    QAreaSeriesPrivate *self) {
  self->QAreaSeriesPrivate::initializeAxes();
}

//  void QAreaSeriesPrivate::initializeGraphics(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAreaSeriesPrivate18initializeGraphicsEP13QGraphicsItem(
    QAreaSeriesPrivate *self,
    QGraphicsItem *parent) {
  self->QAreaSeriesPrivate::initializeGraphics(parent);
}

//  void QAreaSeriesPrivate::initializeTheme(int index, ChartTheme *theme,
//      bool forced)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAreaSeriesPrivate15initializeThemeEiP10ChartThemeb(
    QAreaSeriesPrivate *self,
    int index,
    ChartTheme *theme,
    bool forced) {
  self->QAreaSeriesPrivate::initializeTheme(index, theme, forced);
}

//  QAbstractAxis::AxisType
//      QAreaSeriesPrivate::defaultAxisType(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK18QAreaSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QAreaSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QAreaSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis *QAreaSeriesPrivate::createDefaultAxis(Qt::Orientation a0)
//      const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK18QAreaSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QAreaSeriesPrivate *self,
    Qt::Orientation a0) {
  return self->QAreaSeriesPrivate::createDefaultAxis(a0);
}

#endif  // QT_CONFIG(charts_area_chart)
