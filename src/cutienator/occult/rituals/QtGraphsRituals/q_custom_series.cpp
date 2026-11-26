//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qcustomseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustomseries.h>
#include <QtCore/qstring.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QCustomSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCustomSeries : QCustomSeries {
  using QCustomSeries::componentComplete;
  using QCustomSeries::updateDelegate;
  using QCustomSeries::event;
};

//  A QCustomSeries that Python can take functions over in. Every QCustomSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQCustomSeriesCall0)(const void *, int *);
typedef void (*CuteQCustomSeriesCall1)(const void *, int *);
typedef void (*CuteQCustomSeriesCall2)(const void *, QQuickItem *, qsizetype, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustomSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustomSeriesCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustomSeriesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustomSeries : public QCustomSeries {
public:
  using QCustomSeries::QCustomSeries;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCustomSeries14updateDelegateEP10QQuickItemx")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QCustomSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCustomSeriesCall0 call = reinterpret_cast<CuteQCustomSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QCustomSeries::type();
  }

  //  void QCustomSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCustomSeriesCall1 call = reinterpret_cast<CuteQCustomSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QCustomSeries::componentComplete();
  }

  //  void QCustomSeries::updateDelegate(QQuickItem *item, qsizetype index)
  void updateDelegate(QQuickItem *item, qsizetype index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCustomSeriesCall2 call = reinterpret_cast<CuteQCustomSeriesCall2>(taken[2]);
      call(this, item, index, &handled);
      if (handled) return;
    }
    QCustomSeries::updateDelegate(item, index);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QCustomSeries::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCustomSeriesCall3 call = reinterpret_cast<CuteQCustomSeriesCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QCustomSeries::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQCustomSeriesCall4 call = reinterpret_cast<CuteQCustomSeriesCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCustomSeriesCall5 call = reinterpret_cast<CuteQCustomSeriesCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCustomSeriesCall6 call = reinterpret_cast<CuteQCustomSeriesCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCustomSeriesCall7 call = reinterpret_cast<CuteQCustomSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCustomSeriesCall8 call = reinterpret_cast<CuteQCustomSeriesCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCustomSeriesCall9 call = reinterpret_cast<CuteQCustomSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCustomSeriesCall10 call = reinterpret_cast<CuteQCustomSeriesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustomSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCustomSeries10metaObjectEv(
    const QCustomSeries *self) {
  return self->metaObject();
}

//  void *QCustomSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QCustomSeries11qt_metacastEPKc(
    QCustomSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustomSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QCustomSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustomSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustomSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCustomSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustomSeries::tr(s, c, n));
}

//  QCustomSeries::QCustomSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QCustomSeries *ritual_ZN13QCustomSeriesC1EP7QObject(QObject *parent) {
  return new CuteQCustomSeries(parent);
}

//  QCustomSeries::~QCustomSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeriesD1Ev(QCustomSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QCustomSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK13QCustomSeries4typeEv(
    const QCustomSeries *self) {
  return self->type();
}

//  QList<QCustomSeriesData *> QCustomSeries::dataItems() const
extern "C" Q_DECL_EXPORT
QList<QCustomSeriesData *> *ritual_ZNK13QCustomSeries9dataItemsEv(
    const QCustomSeries *self) {
  return new QList<QCustomSeriesData *>(self->dataItems());
}

//  QQmlComponent *QCustomSeries::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK13QCustomSeries8delegateEv(
    const QCustomSeries *self) {
  return self->delegate();
}

//  void QCustomSeries::setDelegate(QQmlComponent *newDelegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries11setDelegateEP13QQmlComponent(
    QCustomSeries *self,
    QQmlComponent *newDelegate) {
  self->setDelegate(newDelegate);
}

#if QT_CONFIG(graphs_2d_high_performance_backend) || defined(Q_QDOC)
//  void QCustomSeries::setCustomSeriesPainter(QCustomSeriesCanvasRenderer
//      *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries22setCustomSeriesPainterEP27QCustomSeriesCanvasRenderer(
    QCustomSeries *self,
    QCustomSeriesCanvasRenderer *painter) {
  self->setCustomSeriesPainter(painter);
}
#endif  // QT_CONFIG(graphs_2d_high_performance_backend) || defined(Q_QDOC)

//  qreal QCustomSeries::mapX(qreal x)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN13QCustomSeries4mapXEd(QCustomSeries *self, qreal x) {
  return self->mapX(x);
}

//  qreal QCustomSeries::mapY(qreal y)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN13QCustomSeries4mapYEd(QCustomSeries *self, qreal y) {
  return self->mapY(y);
}

//  void QCustomSeries::append(const QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries6appendERK4QMapI7QString8QVariantE(
    QCustomSeries *self,
    const QMap<QString, QVariant> *data) {
  self->append(*data);
}

//  void QCustomSeries::append()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries6appendEv(QCustomSeries *self) {
  self->append();
}

//  void QCustomSeries::insert(qsizetype index, const QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries6insertExRK4QMapI7QString8QVariantE(
    QCustomSeries *self,
    qsizetype index,
    const QMap<QString, QVariant> *data) {
  self->insert(index, *data);
}

//  void QCustomSeries::insert(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries6insertEx(
    QCustomSeries *self,
    qsizetype index) {
  self->insert(index);
}

//  void QCustomSeries::remove(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries6removeEx(
    QCustomSeries *self,
    qsizetype index) {
  self->remove(index);
}

//  void QCustomSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries5clearEv(QCustomSeries *self) {
  self->clear();
}

//  void QCustomSeries::delegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries15delegateChangedEv(QCustomSeries *self) {
  self->delegateChanged();
}

//  QCustomSeries::QCustomSeries(QCustomSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QCustomSeries *ritual_ZN13QCustomSeriesC1ER20QCustomSeriesPrivateP7QObject(
    QCustomSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQCustomSeries(*dd, parent);
}

//  void QCustomSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries17componentCompleteEv(QCustomSeries *self) {
  self->componentComplete();
}

//  void QCustomSeries::updateDelegate(QQuickItem *item, qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCustomSeries14updateDelegateEP10QQuickItemx(
    QCustomSeries *self,
    QQuickItem *item,
    qsizetype index) {
  self->updateDelegate(item, index);
}

//  bool QCustomSeries::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCustomSeries5eventEP6QEvent(
    QCustomSeries *self,
    QEvent *event) {
  return self->event(event);
}

//  QCustomSeriesPrivate *QCustomSeries::d_func()
extern "C" Q_DECL_EXPORT
QCustomSeriesPrivate *ritual_ZN13QCustomSeries6d_funcEv(
    QCustomSeries *self) {
  return self->d_func();
}

//  const QCustomSeriesPrivate *QCustomSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QCustomSeriesPrivate *ritual_ZNK13QCustomSeries6d_funcEv(
    const QCustomSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCustomSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustomSeries(
    QCustomSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustomSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QCustomSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK13QCustomSeries4typeEv(
    const QCustomSeries *self) {
  return self->QCustomSeries::type();
}

//  void QCustomSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QCustomSeries17componentCompleteEv(QCustomSeries *self) {
  static_cast<OwnQCustomSeries *>(self)->OwnQCustomSeries::componentComplete();
}

//  void QCustomSeries::updateDelegate(QQuickItem *item, qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QCustomSeries14updateDelegateEP10QQuickItemx(
    QCustomSeries *self,
    QQuickItem *item,
    qsizetype index) {
  static_cast<OwnQCustomSeries *>(self)->OwnQCustomSeries::updateDelegate(
      item,
      index);
}

//  bool QCustomSeries::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QCustomSeries5eventEP6QEvent(
    QCustomSeries *self,
    QEvent *event) {
  return static_cast<OwnQCustomSeries *>(self)->OwnQCustomSeries::event(
      event);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
