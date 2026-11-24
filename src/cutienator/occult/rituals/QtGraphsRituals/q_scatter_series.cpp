//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qscatterseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_scatter))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatterseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QScatterSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQScatterSeries : QScatterSeries {
  using QScatterSeries::componentComplete;
};

//  A QScatterSeries that Python can take functions over in. Every QScatterSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQScatterSeriesCall0)(const void *, int *);
typedef void (*CuteQScatterSeriesCall1)(const void *, int *);
typedef void (*CuteQScatterSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatterSeries : public QScatterSeries {
public:
  using QScatterSeries::QScatterSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QScatterSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScatterSeriesCall0 call = reinterpret_cast<CuteQScatterSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QScatterSeries::type();
  }

  //  void QScatterSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQScatterSeriesCall1 call = reinterpret_cast<CuteQScatterSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QScatterSeries::componentComplete();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQScatterSeriesCall2 call = reinterpret_cast<CuteQScatterSeriesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScatterSeriesCall3 call = reinterpret_cast<CuteQScatterSeriesCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQScatterSeriesCall4 call = reinterpret_cast<CuteQScatterSeriesCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScatterSeriesCall5 call = reinterpret_cast<CuteQScatterSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScatterSeriesCall6 call = reinterpret_cast<CuteQScatterSeriesCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScatterSeriesCall7 call = reinterpret_cast<CuteQScatterSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScatterSeriesCall8 call = reinterpret_cast<CuteQScatterSeriesCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScatterSeriesCall9 call = reinterpret_cast<CuteQScatterSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatterSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScatterSeries10metaObjectEv(
    const QScatterSeries *self) {
  return self->metaObject();
}

//  QString QScatterSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QScatterSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScatterSeries::tr(s, c, n));
}

//  QScatterSeries::QScatterSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QScatterSeries *ritual_ZN14QScatterSeriesC1EP7QObject(QObject *parent) {
  return new CuteQScatterSeries(parent);
}

//  QScatterSeries::~QScatterSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeriesD1Ev(QScatterSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QScatterSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK14QScatterSeries4typeEv(
    const QScatterSeries *self) {
  return self->type();
}

//  void QScatterSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries17componentCompleteEv(QScatterSeries *self) {
  self->componentComplete();
}

//  QScatterSeriesPrivate *QScatterSeries::d_func()
extern "C" Q_DECL_EXPORT
QScatterSeriesPrivate *ritual_ZN14QScatterSeries6d_funcEv(
    QScatterSeries *self) {
  return self->d_func();
}

//  const QScatterSeriesPrivate *QScatterSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QScatterSeriesPrivate *ritual_ZNK14QScatterSeries6d_funcEv(
    const QScatterSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQScatterSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatterSeries(
    QScatterSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatterSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QScatterSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK14QScatterSeries4typeEv(
    const QScatterSeries *self) {
  return self->QScatterSeries::type();
}

//  void QScatterSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScatterSeries17componentCompleteEv(
    QScatterSeries *self) {
  static_cast<OwnQScatterSeries *>(self)->OwnQScatterSeries::componentComplete();
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_scatter))
