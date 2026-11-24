//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/charttheme_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/charttheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtGui/qpen.h>
#include <QtCore/qlist.h>

//  ChartTheme::ChartTheme(QChart::ChartTheme id)
extern "C" Q_DECL_EXPORT
ChartTheme *ritual_ZN10ChartThemeC1EN6QChart10ChartThemeE(
    QChart::ChartTheme id) {
  return new ChartTheme(id);
}

//  QChart::ChartTheme ChartTheme::id() const
extern "C" Q_DECL_EXPORT
QChart::ChartTheme ritual_ZNK10ChartTheme2idEv(const ChartTheme *self) {
  return self->id();
}

//  QList<QGradient> ChartTheme::seriesGradients() const
extern "C" Q_DECL_EXPORT
QList<QGradient> *ritual_ZNK10ChartTheme15seriesGradientsEv(
    const ChartTheme *self) {
  return new QList<QGradient>(self->seriesGradients());
}

//  QList<QColor> ChartTheme::seriesColors() const
extern "C" Q_DECL_EXPORT
QList<QColor> *ritual_ZNK10ChartTheme12seriesColorsEv(
    const ChartTheme *self) {
  return new QList<QColor>(self->seriesColors());
}

//  QLinearGradient ChartTheme::chartBackgroundGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK10ChartTheme23chartBackgroundGradientEv(
    const ChartTheme *self) {
  return new QLinearGradient(self->chartBackgroundGradient());
}

//  QFont ChartTheme::masterFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10ChartTheme10masterFontEv(const ChartTheme *self) {
  return new QFont(self->masterFont());
}

//  QFont ChartTheme::labelFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK10ChartTheme9labelFontEv(const ChartTheme *self) {
  return new QFont(self->labelFont());
}

//  QBrush ChartTheme::labelBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK10ChartTheme10labelBrushEv(const ChartTheme *self) {
  return new QBrush(self->labelBrush());
}

//  QPen ChartTheme::axisLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK10ChartTheme11axisLinePenEv(const ChartTheme *self) {
  return new QPen(self->axisLinePen());
}

//  QPen ChartTheme::backgroundShadesPen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK10ChartTheme19backgroundShadesPenEv(const ChartTheme *self) {
  return new QPen(self->backgroundShadesPen());
}

//  QPen ChartTheme::outlinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK10ChartTheme10outlinePenEv(const ChartTheme *self) {
  return new QPen(self->outlinePen());
}

//  QBrush ChartTheme::backgroundShadesBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK10ChartTheme21backgroundShadesBrushEv(
    const ChartTheme *self) {
  return new QBrush(self->backgroundShadesBrush());
}

//  BackgroundShadesMode ChartTheme::backgroundShades() const
extern "C" Q_DECL_EXPORT
ChartTheme::BackgroundShadesMode ritual_ZNK10ChartTheme16backgroundShadesEv(
    const ChartTheme *self) {
  return self->backgroundShades();
}

//  bool ChartTheme::isBackgroundDropShadowEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10ChartTheme29isBackgroundDropShadowEnabledEv(
    const ChartTheme *self) {
  return self->isBackgroundDropShadowEnabled();
}

//  QPen ChartTheme::gridLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK10ChartTheme11gridLinePenEv(const ChartTheme *self) {
  return new QPen(self->gridLinePen());
}

//  QPen ChartTheme::minorGridLinePen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK10ChartTheme16minorGridLinePenEv(const ChartTheme *self) {
  return new QPen(self->minorGridLinePen());
}

//  ChartTheme::~ChartTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN10ChartThemeD1Ev(ChartTheme *self) {
  delete self;
}
