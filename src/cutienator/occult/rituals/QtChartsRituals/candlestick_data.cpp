//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/candlestickdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/candlestickdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  CandlestickData::CandlestickData()
extern "C" Q_DECL_EXPORT
CandlestickData *ritual_ZN15CandlestickDataC1Ev() {
  return new CandlestickData();
}

//  CandlestickData::~CandlestickData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15CandlestickDataD1Ev(CandlestickData *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_candlestick_chart)
