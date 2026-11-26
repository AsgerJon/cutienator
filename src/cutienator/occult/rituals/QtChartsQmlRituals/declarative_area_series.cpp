//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeareaseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeareaseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>

//  const QMetaObject *DeclarativeAreaSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21DeclarativeAreaSeries10metaObjectEv(
    const DeclarativeAreaSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeAreaSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21DeclarativeAreaSeries11qt_metacastEPKc(
    DeclarativeAreaSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeAreaSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21DeclarativeAreaSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeAreaSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeAreaSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21DeclarativeAreaSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeAreaSeries::tr(s, c, n));
}

//  DeclarativeAreaSeries::DeclarativeAreaSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeAreaSeries *ritual_ZN21DeclarativeAreaSeriesC1EP7QObject(
    QObject *parent) {
  return new DeclarativeAreaSeries(parent);
}

//  void DeclarativeAreaSeries::setUpperSeries(DeclarativeLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries14setUpperSeriesEP21DeclarativeLineSeries(
    DeclarativeAreaSeries *self,
    DeclarativeLineSeries *series) {
  self->setUpperSeries(series);
}

//  DeclarativeLineSeries *DeclarativeAreaSeries::upperSeries() const
extern "C" Q_DECL_EXPORT
DeclarativeLineSeries *ritual_ZNK21DeclarativeAreaSeries11upperSeriesEv(
    const DeclarativeAreaSeries *self) {
  return self->upperSeries();
}

//  void DeclarativeAreaSeries::setLowerSeries(DeclarativeLineSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries14setLowerSeriesEP21DeclarativeLineSeries(
    DeclarativeAreaSeries *self,
    DeclarativeLineSeries *series) {
  self->setLowerSeries(series);
}

//  DeclarativeLineSeries *DeclarativeAreaSeries::lowerSeries() const
extern "C" Q_DECL_EXPORT
DeclarativeLineSeries *ritual_ZNK21DeclarativeAreaSeries11lowerSeriesEv(
    const DeclarativeAreaSeries *self) {
  return self->lowerSeries();
}

//  QAbstractAxis *DeclarativeAreaSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries5axisXEv(
    DeclarativeAreaSeries *self) {
  return self->axisX();
}

//  void DeclarativeAreaSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries8setAxisXEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeAreaSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries5axisYEv(
    DeclarativeAreaSeries *self) {
  return self->axisY();
}

//  void DeclarativeAreaSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries8setAxisYEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeAreaSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries8axisXTopEv(
    DeclarativeAreaSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeAreaSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeAreaSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries10axisYRightEv(
    DeclarativeAreaSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeAreaSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QAbstractAxis *DeclarativeAreaSeries::axisAngular()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries11axisAngularEv(
    DeclarativeAreaSeries *self) {
  return self->axisAngular();
}

//  void DeclarativeAreaSeries::setAxisAngular(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries14setAxisAngularEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisAngular(axis);
}

//  QAbstractAxis *DeclarativeAreaSeries::axisRadial()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeAreaSeries10axisRadialEv(
    DeclarativeAreaSeries *self) {
  return self->axisRadial();
}

//  void DeclarativeAreaSeries::setAxisRadial(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries13setAxisRadialEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->setAxisRadial(axis);
}

//  qreal DeclarativeAreaSeries::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21DeclarativeAreaSeries11borderWidthEv(
    const DeclarativeAreaSeries *self) {
  return self->borderWidth();
}

//  void DeclarativeAreaSeries::setBorderWidth(qreal borderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries14setBorderWidthEd(
    DeclarativeAreaSeries *self,
    qreal borderWidth) {
  self->setBorderWidth(borderWidth);
}

//  QString DeclarativeAreaSeries::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21DeclarativeAreaSeries13brushFilenameEv(
    const DeclarativeAreaSeries *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeAreaSeries::setBrushFilename(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries16setBrushFilenameERK7QString(
    DeclarativeAreaSeries *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  void DeclarativeAreaSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries8setBrushERK6QBrush(
    DeclarativeAreaSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush DeclarativeAreaSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK21DeclarativeAreaSeries5brushEv(
    const DeclarativeAreaSeries *self) {
  return new QBrush(self->brush());
}

//  void DeclarativeAreaSeries::axisXChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries12axisXChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisXChanged(axis);
}

//  void DeclarativeAreaSeries::axisYChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries12axisYChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisYChanged(axis);
}

//  void DeclarativeAreaSeries::borderWidthChanged(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries18borderWidthChangedEd(
    DeclarativeAreaSeries *self,
    qreal width) {
  self->borderWidthChanged(width);
}

//  void DeclarativeAreaSeries::axisXTopChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries15axisXTopChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisXTopChanged(axis);
}

//  void DeclarativeAreaSeries::axisYRightChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries17axisYRightChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisYRightChanged(axis);
}

//  void DeclarativeAreaSeries::axisAngularChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries18axisAngularChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisAngularChanged(axis);
}

//  void DeclarativeAreaSeries::axisRadialChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries17axisRadialChangedEP13QAbstractAxis(
    DeclarativeAreaSeries *self,
    QAbstractAxis *axis) {
  self->axisRadialChanged(axis);
}

//  void DeclarativeAreaSeries::brushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries12brushChangedEv(
    DeclarativeAreaSeries *self) {
  self->brushChanged();
}

//  void DeclarativeAreaSeries::brushFilenameChanged(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries20brushFilenameChangedERK7QString(
    DeclarativeAreaSeries *self,
    const QString *brushFilename) {
  self->brushFilenameChanged(*brushFilename);
}

//  void DeclarativeAreaSeries::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeAreaSeries18handleBrushChangedEv(
    DeclarativeAreaSeries *self) {
  self->handleBrushChanged();
}

#endif  // QT_CONFIG(charts_area_chart)
