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
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/QPair>
#include <QtCore/QList>
#include <QtCharts/QXYSeries>
#include <QtCore/QVariant>

//  const QMetaObject *QXYSeriesPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QXYSeriesPrivate10metaObjectEv(
    const QXYSeriesPrivate *self) {
  return self->metaObject();
}

//  void *QXYSeriesPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QXYSeriesPrivate11qt_metacastEPKc(
    QXYSeriesPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QXYSeriesPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYSeriesPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QXYSeriesPrivate::initializeAnimations(QChart::AnimationOptions
//      options, int duration, QEasingCurve &curve)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate20initializeAnimationsE6QFlagsIN6QChart15AnimationOptionEEiR12QEasingCurve(
    QXYSeriesPrivate *self,
    int options,
    int duration,
    QEasingCurve *curve) {
  self->initializeAnimations(
      QFlags<QChart::AnimationOption>::fromInt(options),
      duration,
      *curve);
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

//  void QXYSeriesPrivate::drawSeriesPointLabels(QPainter *painter, const
//      QList<QPointF> &points, const int offset, const QHash<int, int>
//      &offsets, const QList<int> &indexesToSkip, const QHash<int, QString>
//      &customLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate21drawSeriesPointLabelsEP8QPainterRK5QListI7QPointFEiRK5QHashIiiERKS2_IiERKS7_Ii7QStringE(
    QXYSeriesPrivate *self,
    QPainter *painter,
    const QList<QPointF> *points,
    int offset,
    const QHash<int, int> *offsets,
    const QList<int> *indexesToSkip,
    const QHash<int, QString> *customLabels) {
  self->drawSeriesPointLabels(
      painter,
      *points,
      offset,
      *offsets,
      *indexesToSkip,
      *customLabels);
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

//  QPair<qreal, qreal> QXYSeriesPrivate::bestFitLineEquation(bool &ok) const
extern "C" Q_DECL_EXPORT
QPair<qreal, qreal> *ritual_ZNK16QXYSeriesPrivate19bestFitLineEquationERb(
    const QXYSeriesPrivate *self,
    bool *ok) {
  return new QPair<qreal, qreal>(self->bestFitLineEquation(*ok));
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

//  QList<qreal> QXYSeriesPrivate::colorByData() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK16QXYSeriesPrivate11colorByDataEv(
    const QXYSeriesPrivate *self) {
  return new QList<qreal>(self->colorByData());
}

//  bool QXYSeriesPrivate::setPointConfiguration(const int index, const
//      QXYSeries::PointConfiguration key, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QXYSeriesPrivate21setPointConfigurationEiN9QXYSeries18PointConfigurationERK8QVariant(
    QXYSeriesPrivate *self,
    int index,
    const QXYSeries::PointConfiguration *key,
    const QVariant *value) {
  return self->setPointConfiguration(index, *key, *value);
}

//  void QXYSeriesPrivate::seriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QXYSeriesPrivate13seriesUpdatedEv(QXYSeriesPrivate *self) {
  self->seriesUpdated();
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

//  a QPair<qreal, qreal> a ritual of QXYSeriesPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXYSeriesPrivate__QPair_qreal_qreal(
    QPair<qreal, qreal> *self) {
  delete self;
}

//  a QList<qreal> a ritual of QXYSeriesPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXYSeriesPrivate__QList_qreal(QList<qreal> *self) {
  delete self;
}
