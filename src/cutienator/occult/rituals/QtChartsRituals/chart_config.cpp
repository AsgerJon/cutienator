//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartconfig_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartconfig_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ChartConfig::ChartConfig()
extern "C" Q_DECL_EXPORT
ChartConfig *ritual_ZN11ChartConfigC1Ev() {
  return new ChartConfig();
}

//  ChartConfig *ChartConfig::instance()
extern "C" Q_DECL_EXPORT
ChartConfig *ritual_ZN11ChartConfig8instanceEv() {
  return ChartConfig::instance();
}

//  ChartConfig::~ChartConfig()
extern "C" Q_DECL_EXPORT
void ritual_ZN11ChartConfigD1Ev(ChartConfig *self) {
  delete self;
}
