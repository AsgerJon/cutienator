//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/chartdataset_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/chartdataset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCharts/qabstractseries.h>
#include <QtCharts/qabstractaxis.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A ChartDataSet that Python can take functions over in. Every ChartDataSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartDataSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteChartDataSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDataSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDataSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDataSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDataSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteChartDataSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteChartDataSet : public ChartDataSet {
public:
  using ChartDataSet::ChartDataSet;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteChartDataSetCall0 call = reinterpret_cast<CuteChartDataSetCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteChartDataSetCall1 call = reinterpret_cast<CuteChartDataSetCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteChartDataSetCall2 call = reinterpret_cast<CuteChartDataSetCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteChartDataSetCall3 call = reinterpret_cast<CuteChartDataSetCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteChartDataSetCall4 call = reinterpret_cast<CuteChartDataSetCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteChartDataSetCall5 call = reinterpret_cast<CuteChartDataSetCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteChartDataSetCall6 call = reinterpret_cast<CuteChartDataSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ChartDataSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12ChartDataSet10metaObjectEv(
    const ChartDataSet *self) {
  return self->metaObject();
}

//  QString ChartDataSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12ChartDataSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ChartDataSet::tr(s, c, n));
}

//  ChartDataSet::ChartDataSet(QChart *chart)
extern "C" Q_DECL_EXPORT
ChartDataSet *ritual_ZN12ChartDataSetC1EP6QChart(QChart *chart) {
  return new CuteChartDataSet(chart);
}

//  ChartDataSet::~ChartDataSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSetD1Ev(ChartDataSet *self) {
  delete self;
}

//  void ChartDataSet::addSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet9addSeriesEP15QAbstractSeries(
    ChartDataSet *self,
    QAbstractSeries *series) {
  self->addSeries(series);
}

//  void ChartDataSet::removeSeries(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet12removeSeriesEP15QAbstractSeries(
    ChartDataSet *self,
    QAbstractSeries *series) {
  self->removeSeries(series);
}

//  QList<QAbstractSeries *> ChartDataSet::series() const
extern "C" Q_DECL_EXPORT
QList<QAbstractSeries *> *ritual_ZNK12ChartDataSet6seriesEv(
    const ChartDataSet *self) {
  return new QList<QAbstractSeries *>(self->series());
}

//  void ChartDataSet::addAxis(QAbstractAxis *axis, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet7addAxisEP13QAbstractAxis6QFlagsIN2Qt13AlignmentFlagEE(
    ChartDataSet *self,
    QAbstractAxis *axis,
    int alignment) {
  self->addAxis(axis, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void ChartDataSet::removeAxis(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet10removeAxisEP13QAbstractAxis(
    ChartDataSet *self,
    QAbstractAxis *axis) {
  self->removeAxis(axis);
}

//  QList<QAbstractAxis *> ChartDataSet::axes() const
extern "C" Q_DECL_EXPORT
QList<QAbstractAxis *> *ritual_ZNK12ChartDataSet4axesEv(
    const ChartDataSet *self) {
  return new QList<QAbstractAxis *>(self->axes());
}

//  bool ChartDataSet::attachAxis(QAbstractSeries *series, QAbstractAxis
//      *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12ChartDataSet10attachAxisEP15QAbstractSeriesP13QAbstractAxis(
    ChartDataSet *self,
    QAbstractSeries *series,
    QAbstractAxis *axis) {
  return self->attachAxis(series, axis);
}

//  bool ChartDataSet::detachAxis(QAbstractSeries *series, QAbstractAxis
//      *axis)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12ChartDataSet10detachAxisEP15QAbstractSeriesP13QAbstractAxis(
    ChartDataSet *self,
    QAbstractSeries *series,
    QAbstractAxis *axis) {
  return self->detachAxis(series, axis);
}

//  void ChartDataSet::createDefaultAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet17createDefaultAxesEv(ChartDataSet *self) {
  self->createDefaultAxes();
}

//  void ChartDataSet::zoomInDomain(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet12zoomInDomainERK6QRectF(
    ChartDataSet *self,
    const QRectF *rect) {
  self->zoomInDomain(*rect);
}

//  void ChartDataSet::zoomOutDomain(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet13zoomOutDomainERK6QRectF(
    ChartDataSet *self,
    const QRectF *rect) {
  self->zoomOutDomain(*rect);
}

//  void ChartDataSet::zoomResetDomain()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet15zoomResetDomainEv(ChartDataSet *self) {
  self->zoomResetDomain();
}

//  bool ChartDataSet::isZoomedDomain()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12ChartDataSet14isZoomedDomainEv(ChartDataSet *self) {
  return self->isZoomedDomain();
}

//  void ChartDataSet::scrollDomain(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet12scrollDomainEdd(
    ChartDataSet *self,
    qreal dx,
    qreal dy) {
  self->scrollDomain(dx, dy);
}

//  QPointF ChartDataSet::mapToValue(const QPointF &position, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12ChartDataSet10mapToValueERK7QPointFP15QAbstractSeries(
    ChartDataSet *self,
    const QPointF *position,
    QAbstractSeries *series) {
  return new QPointF(self->mapToValue(*position, series));
}

//  QPointF ChartDataSet::mapToPosition(const QPointF &value, QAbstractSeries
//      *series)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12ChartDataSet13mapToPositionERK7QPointFP15QAbstractSeries(
    ChartDataSet *self,
    const QPointF *value,
    QAbstractSeries *series) {
  return new QPointF(self->mapToPosition(*value, series));
}

//  GLXYSeriesDataManager *ChartDataSet::glXYSeriesDataManager()
extern "C" Q_DECL_EXPORT
GLXYSeriesDataManager *ritual_ZN12ChartDataSet21glXYSeriesDataManagerEv(
    ChartDataSet *self) {
  return self->glXYSeriesDataManager();
}

//  AbstractDomain *ChartDataSet::createDomain(AbstractDomain::DomainType
//      type)
extern "C" Q_DECL_EXPORT
AbstractDomain *ritual_ZN12ChartDataSet12createDomainEN14AbstractDomain10DomainTypeE(
    ChartDataSet *self,
    AbstractDomain::DomainType type) {
  return self->createDomain(type);
}

//  AbstractDomain *ChartDataSet::domainForSeries(QAbstractSeries *series)
//      const
extern "C" Q_DECL_EXPORT
AbstractDomain *ritual_ZNK12ChartDataSet15domainForSeriesEP15QAbstractSeries(
    const ChartDataSet *self,
    QAbstractSeries *series) {
  return self->domainForSeries(series);
}

//  void ChartDataSet::reverseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet14reverseChangedEv(ChartDataSet *self) {
  self->reverseChanged();
}

//  void ChartDataSet::createAxes(QAbstractAxis::AxisTypes type,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet10createAxesE6QFlagsIN13QAbstractAxis8AxisTypeEEN2Qt11OrientationE(
    ChartDataSet *self,
    int type,
    Qt::Orientation orientation) {
  self->createAxes(
      QFlags<QAbstractAxis::AxisType>::fromInt(type),
      orientation);
}

//  AbstractDomain::DomainType ChartDataSet::selectDomain(const
//      QList<QAbstractAxis *> &axes)
extern "C" Q_DECL_EXPORT
AbstractDomain::DomainType ritual_ZN12ChartDataSet12selectDomainERK5QListIP13QAbstractAxisE(
    ChartDataSet *self,
    const QList<QAbstractAxis *> *axes) {
  return self->selectDomain(*axes);
}

//  void ChartDataSet::deleteAllAxes()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet13deleteAllAxesEv(ChartDataSet *self) {
  self->deleteAllAxes();
}

//  void ChartDataSet::deleteAllSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet15deleteAllSeriesEv(ChartDataSet *self) {
  self->deleteAllSeries();
}

//  void ChartDataSet::findMinMaxForSeries(const QList<QAbstractSeries *>
//      &series, Qt::Orientations orientation, qreal &min, qreal &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ChartDataSet19findMinMaxForSeriesERK5QListIP15QAbstractSeriesE6QFlagsIN2Qt11OrientationEERdSA_(
    ChartDataSet *self,
    const QList<QAbstractSeries *> *series,
    int orientation,
    qreal *min,
    qreal *max) {
  self->findMinMaxForSeries(
      *series,
      QFlags<Qt::Orientation>::fromInt(orientation),
      *min,
      *max);
}

//  a Python function taken by a CuteChartDataSet, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ChartDataSet(
    ChartDataSet *self,
    const char *key,
    void *call) {
  return static_cast<CuteChartDataSet *>(self)->take(key, call);
}
