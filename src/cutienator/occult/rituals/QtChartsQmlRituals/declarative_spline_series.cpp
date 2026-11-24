//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativesplineseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativesplineseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *DeclarativeSplineSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23DeclarativeSplineSeries10metaObjectEv(
    const DeclarativeSplineSeries *self) {
  return self->metaObject();
}

//  QString DeclarativeSplineSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23DeclarativeSplineSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeSplineSeries::tr(s, c, n));
}

//  DeclarativeSplineSeries::DeclarativeSplineSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeSplineSeries *ritual_ZN23DeclarativeSplineSeriesC1EP7QObject(
    QObject *parent) {
  return new DeclarativeSplineSeries(parent);
}

//  QXYSeries *DeclarativeSplineSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN23DeclarativeSplineSeries8xySeriesEv(
    DeclarativeSplineSeries *self) {
  return self->xySeries();
}

//  QAbstractAxis *DeclarativeSplineSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries5axisXEv(
    DeclarativeSplineSeries *self) {
  return self->axisX();
}

//  void DeclarativeSplineSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries8setAxisXEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeSplineSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries5axisYEv(
    DeclarativeSplineSeries *self) {
  return self->axisY();
}

//  void DeclarativeSplineSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries8setAxisYEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeSplineSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries8axisXTopEv(
    DeclarativeSplineSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeSplineSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeSplineSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries10axisYRightEv(
    DeclarativeSplineSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeSplineSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QAbstractAxis *DeclarativeSplineSeries::axisAngular()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries11axisAngularEv(
    DeclarativeSplineSeries *self) {
  return self->axisAngular();
}

//  void DeclarativeSplineSeries::setAxisAngular(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries14setAxisAngularEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisAngular(axis);
}

//  QAbstractAxis *DeclarativeSplineSeries::axisRadial()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN23DeclarativeSplineSeries10axisRadialEv(
    DeclarativeSplineSeries *self) {
  return self->axisRadial();
}

//  void DeclarativeSplineSeries::setAxisRadial(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries13setAxisRadialEP13QAbstractAxis(
    DeclarativeSplineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisRadial(axis);
}

//  qreal DeclarativeSplineSeries::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23DeclarativeSplineSeries5widthEv(
    const DeclarativeSplineSeries *self) {
  return self->width();
}

//  void DeclarativeSplineSeries::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries8setWidthEd(
    DeclarativeSplineSeries *self,
    qreal width) {
  self->setWidth(width);
}

//  Qt::PenStyle DeclarativeSplineSeries::style() const
extern "C" Q_DECL_EXPORT
Qt::PenStyle ritual_ZNK23DeclarativeSplineSeries5styleEv(
    const DeclarativeSplineSeries *self) {
  return self->style();
}

//  void DeclarativeSplineSeries::setStyle(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries8setStyleEN2Qt8PenStyleE(
    DeclarativeSplineSeries *self,
    Qt::PenStyle style) {
  self->setStyle(style);
}

//  Qt::PenCapStyle DeclarativeSplineSeries::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK23DeclarativeSplineSeries8capStyleEv(
    const DeclarativeSplineSeries *self) {
  return self->capStyle();
}

//  void DeclarativeSplineSeries::setCapStyle(Qt::PenCapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries11setCapStyleEN2Qt11PenCapStyleE(
    DeclarativeSplineSeries *self,
    Qt::PenCapStyle capStyle) {
  self->setCapStyle(capStyle);
}

//  void DeclarativeSplineSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries10classBeginEv(
    DeclarativeSplineSeries *self) {
  self->classBegin();
}

//  void DeclarativeSplineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries17componentCompleteEv(
    DeclarativeSplineSeries *self) {
  self->componentComplete();
}

//  void DeclarativeSplineSeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries6appendEdd(
    DeclarativeSplineSeries *self,
    qreal x,
    qreal y) {
  self->append(x, y);
}

//  void DeclarativeSplineSeries::replace(qreal oldX, qreal oldY, qreal newX,
//      qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries7replaceEdddd(
    DeclarativeSplineSeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void DeclarativeSplineSeries::replace(int index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries7replaceEidd(
    DeclarativeSplineSeries *self,
    int index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void DeclarativeSplineSeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries6removeEdd(
    DeclarativeSplineSeries *self,
    qreal x,
    qreal y) {
  self->remove(x, y);
}

//  void DeclarativeSplineSeries::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries6removeEi(
    DeclarativeSplineSeries *self,
    int index) {
  self->remove(index);
}

//  void DeclarativeSplineSeries::removePoints(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries12removePointsEii(
    DeclarativeSplineSeries *self,
    int index,
    int count) {
  self->removePoints(index, count);
}

//  void DeclarativeSplineSeries::insert(int index, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries6insertEidd(
    DeclarativeSplineSeries *self,
    int index,
    qreal x,
    qreal y) {
  self->insert(index, x, y);
}

//  void DeclarativeSplineSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries5clearEv(
    DeclarativeSplineSeries *self) {
  self->clear();
}

//  QPointF DeclarativeSplineSeries::at(int index)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN23DeclarativeSplineSeries2atEi(
    DeclarativeSplineSeries *self,
    int index) {
  return new QPointF(self->at(index));
}

//  void DeclarativeSplineSeries::handleCountChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN23DeclarativeSplineSeries18handleCountChangedEi(
    DeclarativeSplineSeries *self,
    int index) {
  self->handleCountChanged(index);
}

//  DeclarativeSplineSeries as the DeclarativeXySeries it is built on
extern "C" Q_DECL_EXPORT
DeclarativeXySeries *ritual_cast_DeclarativeSplineSeries_DeclarativeXySeries(
    DeclarativeSplineSeries *self) {
  return static_cast<DeclarativeXySeries *>(self);
}

//  DeclarativeSplineSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeSplineSeries_QQmlParserStatus(
    DeclarativeSplineSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  QXYSeries *DeclarativeSplineSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_own_ZN23DeclarativeSplineSeries8xySeriesEv(
    DeclarativeSplineSeries *self) {
  return self->DeclarativeSplineSeries::xySeries();
}

//  void DeclarativeSplineSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeSplineSeries10classBeginEv(
    DeclarativeSplineSeries *self) {
  self->DeclarativeSplineSeries::classBegin();
}

//  void DeclarativeSplineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23DeclarativeSplineSeries17componentCompleteEv(
    DeclarativeSplineSeries *self) {
  self->DeclarativeSplineSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_spline_chart)
