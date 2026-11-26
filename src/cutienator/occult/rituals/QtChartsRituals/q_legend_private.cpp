//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qlegend_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qlegend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QLegendPrivate that Python can take functions over in. Every QLegendPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLegendPrivate : public QLegendPrivate {
public:
  using QLegendPrivate::QLegendPrivate;
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
      CuteQLegendPrivateCall0 call = reinterpret_cast<CuteQLegendPrivateCall0>(taken[0]);
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
      CuteQLegendPrivateCall1 call = reinterpret_cast<CuteQLegendPrivateCall1>(taken[1]);
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
      CuteQLegendPrivateCall2 call = reinterpret_cast<CuteQLegendPrivateCall2>(taken[2]);
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
      CuteQLegendPrivateCall3 call = reinterpret_cast<CuteQLegendPrivateCall3>(taken[3]);
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
      CuteQLegendPrivateCall4 call = reinterpret_cast<CuteQLegendPrivateCall4>(taken[4]);
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
      CuteQLegendPrivateCall5 call = reinterpret_cast<CuteQLegendPrivateCall5>(taken[5]);
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
      CuteQLegendPrivateCall6 call = reinterpret_cast<CuteQLegendPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLegendPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QLegendPrivate10metaObjectEv(
    const QLegendPrivate *self) {
  return self->metaObject();
}

//  void *QLegendPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QLegendPrivate11qt_metacastEPKc(
    QLegendPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLegendPrivate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QLegendPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QLegendPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLegendPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QLegendPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLegendPrivate::tr(s, c, n));
}

//  QLegendPrivate::QLegendPrivate(ChartPresenter *presenter, QChart *chart,
//      QLegend *q)
extern "C" Q_DECL_EXPORT
QLegendPrivate *ritual_ZN14QLegendPrivateC1EP14ChartPresenterP6QChartP7QLegend(
    ChartPresenter *presenter,
    QChart *chart,
    QLegend *q) {
  return new CuteQLegendPrivate(presenter, chart, q);
}

//  QLegendPrivate::~QLegendPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivateD1Ev(QLegendPrivate *self) {
  delete self;
}

//  void QLegendPrivate::setOffset(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate9setOffsetERK7QPointF(
    QLegendPrivate *self,
    const QPointF *offset) {
  self->setOffset(*offset);
}

//  QPointF QLegendPrivate::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14QLegendPrivate6offsetEv(const QLegendPrivate *self) {
  return new QPointF(self->offset());
}

//  int QLegendPrivate::roundness(qreal size)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QLegendPrivate9roundnessEd(QLegendPrivate *self, qreal size) {
  return self->roundness(size);
}

//  QGraphicsItemGroup *QLegendPrivate::items()
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN14QLegendPrivate5itemsEv(QLegendPrivate *self) {
  return self->items();
}

//  QList<QLegendMarker *> QLegendPrivate::markers(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
QList<QLegendMarker *> *ritual_ZN14QLegendPrivate7markersEP15QAbstractSeries(
    QLegendPrivate *self,
    QAbstractSeries *series) {
  return new QList<QLegendMarker *>(self->markers(series));
}

//  qreal QLegendPrivate::maxMarkerWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QLegendPrivate14maxMarkerWidthEv(
    const QLegendPrivate *self) {
  return self->maxMarkerWidth();
}

//  QObject *QLegendPrivate::relatedObject(const QLegendMarker *l)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QLegendPrivate13relatedObjectEPK13QLegendMarker(
    const QLegendMarker *l) {
  return QLegendPrivate::relatedObject(l);
}

//  void QLegendPrivate::handleSeriesAdded(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate17handleSeriesAddedEP15QAbstractSeries(
    QLegendPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesAdded(series);
}

//  void QLegendPrivate::handleSeriesRemoved(QAbstractSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate19handleSeriesRemovedEP15QAbstractSeries(
    QLegendPrivate *self,
    QAbstractSeries *series) {
  self->handleSeriesRemoved(series);
}

//  void QLegendPrivate::handleSeriesVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate26handleSeriesVisibleChangedEv(
    QLegendPrivate *self) {
  self->handleSeriesVisibleChanged();
}

//  void QLegendPrivate::handleCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate18handleCountChangedEv(QLegendPrivate *self) {
  self->handleCountChanged();
}

//  void QLegendPrivate::insertMarkerHelper(QLegendMarker *marker)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate18insertMarkerHelperEP13QLegendMarker(
    QLegendPrivate *self,
    QLegendMarker *marker) {
  self->insertMarkerHelper(marker);
}

//  void QLegendPrivate::addMarkers(const QList<QLegendMarker *> &markers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate10addMarkersERK5QListIP13QLegendMarkerE(
    QLegendPrivate *self,
    const QList<QLegendMarker *> *markers) {
  self->addMarkers(*markers);
}

//  void QLegendPrivate::removeMarkerHelper(QLegendMarker *marker)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate18removeMarkerHelperEP13QLegendMarker(
    QLegendPrivate *self,
    QLegendMarker *marker) {
  self->removeMarkerHelper(marker);
}

//  void QLegendPrivate::removeMarkers(const QList<QLegendMarker *> &markers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate13removeMarkersERK5QListIP13QLegendMarkerE(
    QLegendPrivate *self,
    const QList<QLegendMarker *> *markers) {
  self->removeMarkers(*markers);
}

//  void QLegendPrivate::decorateMarker(QLegendMarker *marker)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate14decorateMarkerEP13QLegendMarker(
    QLegendPrivate *self,
    QLegendMarker *marker) {
  self->decorateMarker(marker);
}

//  void QLegendPrivate::decorateMarkers(const QList<QLegendMarker *>
//      &markers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate15decorateMarkersERK5QListIP13QLegendMarkerE(
    QLegendPrivate *self,
    const QList<QLegendMarker *> *markers) {
  self->decorateMarkers(*markers);
}

//  void QLegendPrivate::updateToolTips()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLegendPrivate14updateToolTipsEv(QLegendPrivate *self) {
  self->updateToolTips();
}

//  a Python function taken by a CuteQLegendPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLegendPrivate(
    QLegendPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLegendPrivate *>(self)->take(key, call);
}
