//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qxyseries_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qxyseries.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qxyseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QXYSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QXYSeriesPrivate10metaObjectEv(
    const QXYSeriesPrivate *self) {
  return self->metaObject();
}

//  QString QXYSeriesPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QXYSeriesPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYSeriesPrivate::tr(s, c, n));
}

//  void QXYSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate16initializeDomainEv(
    QXYSeriesPrivate *self) {
  self->initializeDomain();
}

//  void QXYSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate14initializeAxesEv(QXYSeriesPrivate *self) {
  self->initializeAxes();
}

//  QList<QLegendMarker *> QXYSeriesPrivate::createLegendMarkers(QLegend
//      *legend)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN16QXYSeriesPrivate19createLegendMarkersEP7QLegend(
    QXYSeriesPrivate *self,
    QLegend *legend) {
  return new QList<QLegendMarker *>(self->createLegendMarkers(legend));
}

//  QAbstractAxis::AxisType QXYSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK16QXYSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QXYSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->defaultAxisType(orientation);
}

//  QAbstractAxis *QXYSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK16QXYSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QXYSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->createDefaultAxis(orientation);
}

//  void QXYSeriesPrivate::drawPointLabels(QPainter *painter, const
//      QList<QPointF> &allPoints, const int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate15drawPointLabelsEP8QPainterRK5QListI7QPointFEi(
    QXYSeriesPrivate *self,
    QPainter *painter,
    const QList<QPointF> *allPoints,
    int offset) {
  self->drawPointLabels(painter, *allPoints, offset);
}

//  void QXYSeriesPrivate::drawBestFitLine(QPainter *painter, const QRectF
//      &clipRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate15drawBestFitLineEP8QPainterRK6QRectF(
    QXYSeriesPrivate *self,
    QPainter *painter,
    const QRectF *clipRect) {
  self->drawBestFitLine(painter, *clipRect);
}

//  void QXYSeriesPrivate::setPointSelected(int index, bool selected, bool
//      &callSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate16setPointSelectedEibRb(
    QXYSeriesPrivate *self,
    int index,
    bool selected,
    bool *callSignal) {
  self->setPointSelected(index, selected, *callSignal);
}

//  bool QXYSeriesPrivate::isPointSelected(int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXYSeriesPrivate15isPointSelectedEi(
    QXYSeriesPrivate *self,
    int index) {
  return self->isPointSelected(index);
}

//  bool QXYSeriesPrivate::isMarkerSizeDefault()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXYSeriesPrivate19isMarkerSizeDefaultEv(
    QXYSeriesPrivate *self) {
  return self->isMarkerSizeDefault();
}

//  void QXYSeriesPrivate::setMarkerSize(qreal markerSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate13setMarkerSizeEd(
    QXYSeriesPrivate *self,
    qreal markerSize) {
  self->setMarkerSize(markerSize);
}

//  QXYSeries *QXYSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN16QXYSeriesPrivate6q_funcEv(QXYSeriesPrivate *self) {
  return self->q_func();
}

//  const QXYSeries *QXYSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXYSeries *ritual_ZNK16QXYSeriesPrivate6q_funcEv(
    const QXYSeriesPrivate *self) {
  return self->q_func();
}

//  void QXYSeriesPrivate::initializeDomain()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXYSeriesPrivate16initializeDomainEv(
    QXYSeriesPrivate *self) {
  self->QXYSeriesPrivate::initializeDomain();
}

//  void QXYSeriesPrivate::initializeAxes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QXYSeriesPrivate14initializeAxesEv(
    QXYSeriesPrivate *self) {
  self->QXYSeriesPrivate::initializeAxes();
}

//  QAbstractAxis::AxisType QXYSeriesPrivate::defaultAxisType(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK16QXYSeriesPrivate15defaultAxisTypeEN2Qt11OrientationE(
    const QXYSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QXYSeriesPrivate::defaultAxisType(orientation);
}

//  QAbstractAxis *QXYSeriesPrivate::createDefaultAxis(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_own_ZNK16QXYSeriesPrivate17createDefaultAxisEN2Qt11OrientationE(
    const QXYSeriesPrivate *self,
    Qt::Orientation orientation) {
  return self->QXYSeriesPrivate::createDefaultAxis(orientation);
}
