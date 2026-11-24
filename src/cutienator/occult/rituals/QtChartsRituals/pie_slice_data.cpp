//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/pieslicedata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_pie_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/pieslicedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  PieSliceData::PieSliceData()
extern "C" Q_DECL_EXPORT
PieSliceData *ritual_ZN12PieSliceDataC1Ev() {
  return new PieSliceData();
}

//  bool PieSliceData::operator!=(const PieSliceData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12PieSliceDataneERKS_(
    const PieSliceData *self,
    const PieSliceData *other) {
  return self->operator!=(*other);
}

//  PieSliceData::~PieSliceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12PieSliceDataD1Ev(PieSliceData *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_pie_chart)
