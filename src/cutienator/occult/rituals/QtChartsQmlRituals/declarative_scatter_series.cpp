//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativescatterseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_scatter_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativescatterseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *DeclarativeScatterSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24DeclarativeScatterSeries10metaObjectEv(
    const DeclarativeScatterSeries *self) {
  return self->metaObject();
}

//  QString DeclarativeScatterSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24DeclarativeScatterSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeScatterSeries::tr(s, c, n));
}

//  DeclarativeScatterSeries::DeclarativeScatterSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeScatterSeries *ritual_ZN24DeclarativeScatterSeriesC1EP7QObject(
    QObject *parent) {
  return new DeclarativeScatterSeries(parent);
}

//  QXYSeries *DeclarativeScatterSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN24DeclarativeScatterSeries8xySeriesEv(
    DeclarativeScatterSeries *self) {
  return self->xySeries();
}

//  QAbstractAxis *DeclarativeScatterSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries5axisXEv(
    DeclarativeScatterSeries *self) {
  return self->axisX();
}

//  void DeclarativeScatterSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries8setAxisXEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeScatterSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries5axisYEv(
    DeclarativeScatterSeries *self) {
  return self->axisY();
}

//  void DeclarativeScatterSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries8setAxisYEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeScatterSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries8axisXTopEv(
    DeclarativeScatterSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeScatterSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeScatterSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries10axisYRightEv(
    DeclarativeScatterSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeScatterSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QAbstractAxis *DeclarativeScatterSeries::axisAngular()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries11axisAngularEv(
    DeclarativeScatterSeries *self) {
  return self->axisAngular();
}

//  void DeclarativeScatterSeries::setAxisAngular(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries14setAxisAngularEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisAngular(axis);
}

//  QAbstractAxis *DeclarativeScatterSeries::axisRadial()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN24DeclarativeScatterSeries10axisRadialEv(
    DeclarativeScatterSeries *self) {
  return self->axisRadial();
}

//  void DeclarativeScatterSeries::setAxisRadial(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries13setAxisRadialEP13QAbstractAxis(
    DeclarativeScatterSeries *self,
    QAbstractAxis *axis) {
  self->setAxisRadial(axis);
}

//  qreal DeclarativeScatterSeries::borderWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24DeclarativeScatterSeries11borderWidthEv(
    const DeclarativeScatterSeries *self) {
  return self->borderWidth();
}

//  void DeclarativeScatterSeries::setBorderWidth(qreal borderWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries14setBorderWidthEd(
    DeclarativeScatterSeries *self,
    qreal borderWidth) {
  self->setBorderWidth(borderWidth);
}

//  QString DeclarativeScatterSeries::brushFilename() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24DeclarativeScatterSeries13brushFilenameEv(
    const DeclarativeScatterSeries *self) {
  return new QString(self->brushFilename());
}

//  void DeclarativeScatterSeries::setBrushFilename(const QString
//      &brushFilename)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries16setBrushFilenameERK7QString(
    DeclarativeScatterSeries *self,
    const QString *brushFilename) {
  self->setBrushFilename(*brushFilename);
}

//  void DeclarativeScatterSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries8setBrushERK6QBrush(
    DeclarativeScatterSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush DeclarativeScatterSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK24DeclarativeScatterSeries5brushEv(
    const DeclarativeScatterSeries *self) {
  return new QBrush(self->brush());
}

//  void DeclarativeScatterSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries10classBeginEv(
    DeclarativeScatterSeries *self) {
  self->classBegin();
}

//  void DeclarativeScatterSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries17componentCompleteEv(
    DeclarativeScatterSeries *self) {
  self->componentComplete();
}

//  void DeclarativeScatterSeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries6appendEdd(
    DeclarativeScatterSeries *self,
    qreal x,
    qreal y) {
  self->append(x, y);
}

//  void DeclarativeScatterSeries::replace(qreal oldX, qreal oldY, qreal
//      newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries7replaceEdddd(
    DeclarativeScatterSeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void DeclarativeScatterSeries::replace(int index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries7replaceEidd(
    DeclarativeScatterSeries *self,
    int index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void DeclarativeScatterSeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries6removeEdd(
    DeclarativeScatterSeries *self,
    qreal x,
    qreal y) {
  self->remove(x, y);
}

//  void DeclarativeScatterSeries::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries6removeEi(
    DeclarativeScatterSeries *self,
    int index) {
  self->remove(index);
}

//  void DeclarativeScatterSeries::removePoints(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries12removePointsEii(
    DeclarativeScatterSeries *self,
    int index,
    int count) {
  self->removePoints(index, count);
}

//  void DeclarativeScatterSeries::insert(int index, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries6insertEidd(
    DeclarativeScatterSeries *self,
    int index,
    qreal x,
    qreal y) {
  self->insert(index, x, y);
}

//  void DeclarativeScatterSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries5clearEv(
    DeclarativeScatterSeries *self) {
  self->clear();
}

//  QPointF DeclarativeScatterSeries::at(int index)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN24DeclarativeScatterSeries2atEi(
    DeclarativeScatterSeries *self,
    int index) {
  return new QPointF(self->at(index));
}

//  void DeclarativeScatterSeries::handleCountChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries18handleCountChangedEi(
    DeclarativeScatterSeries *self,
    int index) {
  self->handleCountChanged(index);
}

//  void DeclarativeScatterSeries::handleBrushChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24DeclarativeScatterSeries18handleBrushChangedEv(
    DeclarativeScatterSeries *self) {
  self->handleBrushChanged();
}

//  DeclarativeScatterSeries as the DeclarativeXySeries it is built on
extern "C" Q_DECL_EXPORT
DeclarativeXySeries *ritual_cast_DeclarativeScatterSeries_DeclarativeXySeries(
    DeclarativeScatterSeries *self) {
  return static_cast<DeclarativeXySeries *>(self);
}

//  DeclarativeScatterSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeScatterSeries_QQmlParserStatus(
    DeclarativeScatterSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  QXYSeries *DeclarativeScatterSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_own_ZN24DeclarativeScatterSeries8xySeriesEv(
    DeclarativeScatterSeries *self) {
  return self->DeclarativeScatterSeries::xySeries();
}

//  void DeclarativeScatterSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24DeclarativeScatterSeries8setBrushERK6QBrush(
    DeclarativeScatterSeries *self,
    const QBrush *brush) {
  self->DeclarativeScatterSeries::setBrush(*brush);
}

//  void DeclarativeScatterSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24DeclarativeScatterSeries10classBeginEv(
    DeclarativeScatterSeries *self) {
  self->DeclarativeScatterSeries::classBegin();
}

//  void DeclarativeScatterSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24DeclarativeScatterSeries17componentCompleteEv(
    DeclarativeScatterSeries *self) {
  self->DeclarativeScatterSeries::componentComplete();
}

#endif  // QT_CONFIG(charts_scatter_chart)
