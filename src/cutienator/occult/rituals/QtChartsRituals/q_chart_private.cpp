//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qchart_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qchart_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QChartPrivate::QChartPrivate(QChart *q, QChart::ChartType type)
extern "C" Q_DECL_EXPORT
QChartPrivate *ritual_ZN13QChartPrivateC1EP6QChartNS0_9ChartTypeE(
    QChart *q,
    QChart::ChartType type) {
  return new QChartPrivate(q, type);
}

//  QChartPrivate::~QChartPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivateD1Ev(QChartPrivate *self) {
  delete self;
}

//  QPen &QChartPrivate::defaultPen()
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN13QChartPrivate10defaultPenEv() {
  return &(QChartPrivate::defaultPen());
}

//  QBrush &QChartPrivate::defaultBrush()
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN13QChartPrivate12defaultBrushEv() {
  return &(QChartPrivate::defaultBrush());
}

//  QFont &QChartPrivate::defaultFont()
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN13QChartPrivate11defaultFontEv() {
  return &(QChartPrivate::defaultFont());
}

//  void QChartPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate4initEv(QChartPrivate *self) {
  self->init();
}

//  void QChartPrivate::zoomIn(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate6zoomInEd(QChartPrivate *self, qreal factor) {
  self->zoomIn(factor);
}

//  void QChartPrivate::zoomOut(qreal factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate7zoomOutEd(QChartPrivate *self, qreal factor) {
  self->zoomOut(factor);
}

//  void QChartPrivate::zoomIn(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate6zoomInERK6QRectF(
    QChartPrivate *self,
    const QRectF *rect) {
  self->zoomIn(*rect);
}

//  void QChartPrivate::zoomReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate9zoomResetEv(QChartPrivate *self) {
  self->zoomReset();
}

//  bool QChartPrivate::isZoomed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QChartPrivate8isZoomedEv(QChartPrivate *self) {
  return self->isZoomed();
}

//  void QChartPrivate::scroll(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QChartPrivate6scrollEdd(
    QChartPrivate *self,
    qreal dx,
    qreal dy) {
  self->scroll(dx, dy);
}
