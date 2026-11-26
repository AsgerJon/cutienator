//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qboxplotlegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qboxplotlegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBoxPlotLegendMarker that Python can take functions over in. Every QBoxPlotLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBoxPlotLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQBoxPlotLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxPlotLegendMarker : public QBoxPlotLegendMarker {
public:
  using QBoxPlotLegendMarker::QBoxPlotLegendMarker;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QLegendMarker4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QLegendMarker6seriesEv")) {
      taken[1] = call;
      return true;
    }
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

  //  LegendMarkerType QBoxPlotLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerCall0 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QBoxPlotLegendMarker::type();
  }

  //  QBoxPlotSeries *QBoxPlotLegendMarker::series()
  QBoxPlotSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerCall1 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QBoxPlotSeries *>(given);
    }
    return QBoxPlotLegendMarker::series();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerCall2 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall2>(taken[2]);
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
      CuteQBoxPlotLegendMarkerCall3 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall3>(taken[3]);
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
      CuteQBoxPlotLegendMarkerCall4 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall4>(taken[4]);
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
      CuteQBoxPlotLegendMarkerCall5 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall5>(taken[5]);
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
      CuteQBoxPlotLegendMarkerCall6 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall6>(taken[6]);
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
      CuteQBoxPlotLegendMarkerCall7 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall7>(taken[7]);
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
      CuteQBoxPlotLegendMarkerCall8 call = reinterpret_cast<CuteQBoxPlotLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxPlotLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QBoxPlotLegendMarker10metaObjectEv(
    const QBoxPlotLegendMarker *self) {
  return self->metaObject();
}

//  void *QBoxPlotLegendMarker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QBoxPlotLegendMarker11qt_metacastEPKc(
    QBoxPlotLegendMarker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBoxPlotLegendMarker::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QBoxPlotLegendMarker11qt_metacallEN11QMetaObject4CallEiPPv(
    QBoxPlotLegendMarker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBoxPlotLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QBoxPlotLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotLegendMarker::tr(s, c, n));
}

//  QBoxPlotLegendMarker::QBoxPlotLegendMarker(QBoxPlotSeries *series,
//      QLegend *legend, QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxPlotLegendMarker *ritual_ZN20QBoxPlotLegendMarkerC1EP14QBoxPlotSeriesP7QLegendP7QObject(
    QBoxPlotSeries *series,
    QLegend *legend,
    QObject *parent) {
  return new CuteQBoxPlotLegendMarker(series, legend, parent);
}

//  QBoxPlotLegendMarker::~QBoxPlotLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBoxPlotLegendMarkerD1Ev(QBoxPlotLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QBoxPlotLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN20QBoxPlotLegendMarker4typeEv(
    QBoxPlotLegendMarker *self) {
  return self->type();
}

//  QBoxPlotSeries *QBoxPlotLegendMarker::series()
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZN20QBoxPlotLegendMarker6seriesEv(
    QBoxPlotLegendMarker *self) {
  return self->series();
}

//  QBoxPlotLegendMarker::QBoxPlotLegendMarker(QBoxPlotLegendMarkerPrivate
//      &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxPlotLegendMarker *ritual_ZN20QBoxPlotLegendMarkerC1ER27QBoxPlotLegendMarkerPrivateP7QObject(
    QBoxPlotLegendMarkerPrivate *d,
    QObject *parent) {
  return new CuteQBoxPlotLegendMarker(*d, parent);
}

//  QBoxPlotLegendMarkerPrivate *QBoxPlotLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QBoxPlotLegendMarkerPrivate *ritual_ZN20QBoxPlotLegendMarker6d_funcEv(
    QBoxPlotLegendMarker *self) {
  return self->d_func();
}

//  const QBoxPlotLegendMarkerPrivate *QBoxPlotLegendMarker::d_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotLegendMarkerPrivate *ritual_ZNK20QBoxPlotLegendMarker6d_funcEv(
    const QBoxPlotLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBoxPlotLegendMarker, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxPlotLegendMarker(
    QBoxPlotLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxPlotLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QBoxPlotLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN20QBoxPlotLegendMarker4typeEv(
    QBoxPlotLegendMarker *self) {
  return self->QBoxPlotLegendMarker::type();
}

//  QBoxPlotSeries *QBoxPlotLegendMarker::series()
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_own_ZN20QBoxPlotLegendMarker6seriesEv(
    QBoxPlotLegendMarker *self) {
  return self->QBoxPlotLegendMarker::series();
}

#endif  // QT_CONFIG(charts_boxplot_chart)
