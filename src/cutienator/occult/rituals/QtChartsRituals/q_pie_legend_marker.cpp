//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qpielegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qpielegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPieLegendMarker that Python can take functions over in. Every QPieLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPieLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQPieLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieLegendMarker : public QPieLegendMarker {
public:
  using QPieLegendMarker::QPieLegendMarker;
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

  //  LegendMarkerType QPieLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPieLegendMarkerCall0 call = reinterpret_cast<CuteQPieLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QPieLegendMarker::type();
  }

  //  QPieSeries *QPieLegendMarker::series()
  QPieSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPieLegendMarkerCall1 call = reinterpret_cast<CuteQPieLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPieSeries *>(given);
    }
    return QPieLegendMarker::series();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPieLegendMarkerCall2 call = reinterpret_cast<CuteQPieLegendMarkerCall2>(taken[2]);
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
      CuteQPieLegendMarkerCall3 call = reinterpret_cast<CuteQPieLegendMarkerCall3>(taken[3]);
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
      CuteQPieLegendMarkerCall4 call = reinterpret_cast<CuteQPieLegendMarkerCall4>(taken[4]);
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
      CuteQPieLegendMarkerCall5 call = reinterpret_cast<CuteQPieLegendMarkerCall5>(taken[5]);
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
      CuteQPieLegendMarkerCall6 call = reinterpret_cast<CuteQPieLegendMarkerCall6>(taken[6]);
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
      CuteQPieLegendMarkerCall7 call = reinterpret_cast<CuteQPieLegendMarkerCall7>(taken[7]);
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
      CuteQPieLegendMarkerCall8 call = reinterpret_cast<CuteQPieLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPieLegendMarker10metaObjectEv(
    const QPieLegendMarker *self) {
  return self->metaObject();
}

//  QString QPieLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPieLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieLegendMarker::tr(s, c, n));
}

//  QPieLegendMarker::QPieLegendMarker(QPieSeries *series, QPieSlice *slice,
//      QLegend *legend, QObject *parent)
extern "C" Q_DECL_EXPORT
QPieLegendMarker *ritual_ZN16QPieLegendMarkerC1EP10QPieSeriesP9QPieSliceP7QLegendP7QObject(
    QPieSeries *series,
    QPieSlice *slice,
    QLegend *legend,
    QObject *parent) {
  return new CuteQPieLegendMarker(series, slice, legend, parent);
}

//  QPieLegendMarker::~QPieLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPieLegendMarkerD1Ev(QPieLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QPieLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN16QPieLegendMarker4typeEv(
    QPieLegendMarker *self) {
  return self->type();
}

//  QPieSeries *QPieLegendMarker::series()
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN16QPieLegendMarker6seriesEv(QPieLegendMarker *self) {
  return self->series();
}

//  QPieSlice *QPieLegendMarker::slice()
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZN16QPieLegendMarker5sliceEv(QPieLegendMarker *self) {
  return self->slice();
}

//  QPieLegendMarkerPrivate *QPieLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QPieLegendMarkerPrivate *ritual_ZN16QPieLegendMarker6d_funcEv(
    QPieLegendMarker *self) {
  return self->d_func();
}

//  const QPieLegendMarkerPrivate *QPieLegendMarker::d_func() const
extern "C" Q_DECL_EXPORT
const QPieLegendMarkerPrivate *ritual_ZNK16QPieLegendMarker6d_funcEv(
    const QPieLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPieLegendMarker, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieLegendMarker(
    QPieLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPieLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QPieLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN16QPieLegendMarker4typeEv(
    QPieLegendMarker *self) {
  return self->QPieLegendMarker::type();
}

//  QPieSeries *QPieLegendMarker::series()
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_own_ZN16QPieLegendMarker6seriesEv(
    QPieLegendMarker *self) {
  return self->QPieLegendMarker::series();
}
