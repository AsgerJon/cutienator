//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartconfig_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '!defined(Q_OS_WIN)'. Qt's header defines the static member
//  'ChartConfig::m_instance' of its exported class in the header itself,
//  which outside QtCharts on Windows is a definition of a member imported
//  from a DLL, and no compiler takes it: the header is broken on Qt's side
//  there. Kept as it is when the generator runs again.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if !defined(Q_OS_WIN)
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

#endif  // !defined(Q_OS_WIN)
