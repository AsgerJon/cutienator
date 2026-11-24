//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qarealegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/qarealegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAreaLegendMarker that Python can take functions over in. Every QAreaLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(charts_area_chart)
typedef int (*CuteQAreaLegendMarkerCall0)(const void *, int *);
#endif  // QT_CONFIG(charts_area_chart)
#if QT_CONFIG(charts_area_chart)
typedef void * (*CuteQAreaLegendMarkerCall1)(const void *, int *);
#endif  // QT_CONFIG(charts_area_chart)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAreaLegendMarker : public QAreaLegendMarker {
public:
  using QAreaLegendMarker::QAreaLegendMarker;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(charts_area_chart)
    if (!std::strcmp(key, "_ZN13QLegendMarker4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(charts_area_chart)
#if QT_CONFIG(charts_area_chart)
    if (!std::strcmp(key, "_ZN13QLegendMarker6seriesEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(charts_area_chart)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(charts_area_chart)
  //  LegendMarkerType QAreaLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall0 call = reinterpret_cast<CuteQAreaLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QAreaLegendMarker::type();
  }
#endif  // QT_CONFIG(charts_area_chart)

#if QT_CONFIG(charts_area_chart)
  //  QAreaSeries *QAreaLegendMarker::series()
  QAreaSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall1 call = reinterpret_cast<CuteQAreaLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAreaSeries *>(given);
    }
    return QAreaLegendMarker::series();
  }
#endif  // QT_CONFIG(charts_area_chart)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall2 call = reinterpret_cast<CuteQAreaLegendMarkerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall3 call = reinterpret_cast<CuteQAreaLegendMarkerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall4 call = reinterpret_cast<CuteQAreaLegendMarkerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall5 call = reinterpret_cast<CuteQAreaLegendMarkerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall6 call = reinterpret_cast<CuteQAreaLegendMarkerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall7 call = reinterpret_cast<CuteQAreaLegendMarkerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAreaLegendMarkerCall8 call = reinterpret_cast<CuteQAreaLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAreaLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAreaLegendMarker10metaObjectEv(
    const QAreaLegendMarker *self) {
  return self->metaObject();
}

//  QString QAreaLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAreaLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAreaLegendMarker::tr(s, c, n));
}

//  QAreaLegendMarker::QAreaLegendMarker(QAreaSeries *series, QLegend
//      *legend, QObject *parent)
extern "C" Q_DECL_EXPORT
QAreaLegendMarker *ritual_ZN17QAreaLegendMarkerC1EP11QAreaSeriesP7QLegendP7QObject(
    QAreaSeries *series,
    QLegend *legend,
    QObject *parent) {
  return new CuteQAreaLegendMarker(series, legend, parent);
}

//  QAreaLegendMarker::~QAreaLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAreaLegendMarkerD1Ev(QAreaLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QAreaLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN17QAreaLegendMarker4typeEv(
    QAreaLegendMarker *self) {
  return self->type();
}

//  QAreaSeries *QAreaLegendMarker::series()
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN17QAreaLegendMarker6seriesEv(QAreaLegendMarker *self) {
  return self->series();
}

//  QAreaLegendMarkerPrivate *QAreaLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QAreaLegendMarkerPrivate *ritual_ZN17QAreaLegendMarker6d_funcEv(
    QAreaLegendMarker *self) {
  return self->d_func();
}

//  const QAreaLegendMarkerPrivate *QAreaLegendMarker::d_func() const
extern "C" Q_DECL_EXPORT
const QAreaLegendMarkerPrivate *ritual_ZNK17QAreaLegendMarker6d_funcEv(
    const QAreaLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAreaLegendMarker, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAreaLegendMarker(
    QAreaLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAreaLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QAreaLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN17QAreaLegendMarker4typeEv(
    QAreaLegendMarker *self) {
  return self->QAreaLegendMarker::type();
}

//  QAreaSeries *QAreaLegendMarker::series()
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_own_ZN17QAreaLegendMarker6seriesEv(
    QAreaLegendMarker *self) {
  return self->QAreaLegendMarker::series();
}

#endif  // QT_CONFIG(charts_area_chart)
