//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartelement_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartelement_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ChartAnimation *ChartElement::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZNK12ChartElement9animationEv(
    const ChartElement *self) {
  return self->animation();
}

//  void ChartElement::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartElement12setPresenterEP14ChartPresenter(
    ChartElement *self,
    ChartPresenter *presenter) {
  self->setPresenter(presenter);
}

//  ChartPresenter *ChartElement::presenter() const
extern "C" Q_DECL_EXPORT
ChartPresenter *ritual_ZNK12ChartElement9presenterEv(
    const ChartElement *self) {
  return self->presenter();
}

//  void ChartElement::setThemeManager(ChartThemeManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartElement15setThemeManagerEP17ChartThemeManager(
    ChartElement *self,
    ChartThemeManager *manager) {
  self->setThemeManager(manager);
}

//  ChartThemeManager *ChartElement::themeManager() const
extern "C" Q_DECL_EXPORT
ChartThemeManager *ritual_ZNK12ChartElement12themeManagerEv(
    const ChartElement *self) {
  return self->themeManager();
}

//  void ChartElement::setDataSet(ChartDataSet *dataSet)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartElement10setDataSetEP12ChartDataSet(
    ChartElement *self,
    ChartDataSet *dataSet) {
  self->setDataSet(dataSet);
}

//  ChartDataSet *ChartElement::dataSet() const
extern "C" Q_DECL_EXPORT
ChartDataSet *ritual_ZNK12ChartElement7dataSetEv(const ChartElement *self) {
  return self->dataSet();
}

//  ChartAnimation *ChartElement::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_own_ZNK12ChartElement9animationEv(
    const ChartElement *self) {
  return self->ChartElement::animation();
}

//  void ChartElement::setPresenter(ChartPresenter *presenter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12ChartElement12setPresenterEP14ChartPresenter(
    ChartElement *self,
    ChartPresenter *presenter) {
  self->ChartElement::setPresenter(presenter);
}

//  void ChartElement::setThemeManager(ChartThemeManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12ChartElement15setThemeManagerEP17ChartThemeManager(
    ChartElement *self,
    ChartThemeManager *manager) {
  self->ChartElement::setThemeManager(manager);
}

//  void ChartElement::setDataSet(ChartDataSet *dataSet)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12ChartElement10setDataSetEP12ChartDataSet(
    ChartElement *self,
    ChartDataSet *dataSet) {
  self->ChartElement::setDataSet(dataSet);
}
