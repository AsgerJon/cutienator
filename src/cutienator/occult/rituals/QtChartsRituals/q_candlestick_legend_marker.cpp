//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcandlesticklegendmarker.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qcandlesticklegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCandlestickLegendMarker that Python can take functions over in. Every QCandlestickLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQCandlestickLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQCandlestickLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickLegendMarker : public QCandlestickLegendMarker {
public:
  using QCandlestickLegendMarker::QCandlestickLegendMarker;
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

  //  LegendMarkerType QCandlestickLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerCall0 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QCandlestickLegendMarker::type();
  }

  //  QCandlestickSeries *QCandlestickLegendMarker::series()
  QCandlestickSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerCall1 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCandlestickSeries *>(given);
    }
    return QCandlestickLegendMarker::series();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerCall2 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall2>(taken[2]);
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
      CuteQCandlestickLegendMarkerCall3 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall3>(taken[3]);
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
      CuteQCandlestickLegendMarkerCall4 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall4>(taken[4]);
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
      CuteQCandlestickLegendMarkerCall5 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall5>(taken[5]);
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
      CuteQCandlestickLegendMarkerCall6 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall6>(taken[6]);
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
      CuteQCandlestickLegendMarkerCall7 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall7>(taken[7]);
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
      CuteQCandlestickLegendMarkerCall8 call = reinterpret_cast<CuteQCandlestickLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QCandlestickLegendMarker10metaObjectEv(
    const QCandlestickLegendMarker *self) {
  return self->metaObject();
}

//  QString QCandlestickLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QCandlestickLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickLegendMarker::tr(s, c, n));
}

//  QCandlestickLegendMarker::QCandlestickLegendMarker(QCandlestickSeries
//      *series, QLegend *legend, QObject *parent)
extern "C" Q_DECL_EXPORT
QCandlestickLegendMarker *ritual_ZN24QCandlestickLegendMarkerC1EP18QCandlestickSeriesP7QLegendP7QObject(
    QCandlestickSeries *series,
    QLegend *legend,
    QObject *parent) {
  return new CuteQCandlestickLegendMarker(series, legend, parent);
}

//  QCandlestickLegendMarker::~QCandlestickLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCandlestickLegendMarkerD1Ev(
    QCandlestickLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QCandlestickLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN24QCandlestickLegendMarker4typeEv(
    QCandlestickLegendMarker *self) {
  return self->type();
}

//  QCandlestickSeries *QCandlestickLegendMarker::series()
extern "C" Q_DECL_EXPORT
QCandlestickSeries *ritual_ZN24QCandlestickLegendMarker6seriesEv(
    QCandlestickLegendMarker *self) {
  return self->series();
}

//  QCandlestickLegendMarkerPrivate *QCandlestickLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QCandlestickLegendMarkerPrivate *ritual_ZN24QCandlestickLegendMarker6d_funcEv(
    QCandlestickLegendMarker *self) {
  return self->d_func();
}

//  const QCandlestickLegendMarkerPrivate *QCandlestickLegendMarker::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QCandlestickLegendMarkerPrivate *ritual_ZNK24QCandlestickLegendMarker6d_funcEv(
    const QCandlestickLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCandlestickLegendMarker, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickLegendMarker(
    QCandlestickLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QCandlestickLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN24QCandlestickLegendMarker4typeEv(
    QCandlestickLegendMarker *self) {
  return self->QCandlestickLegendMarker::type();
}

//  QCandlestickSeries *QCandlestickLegendMarker::series()
extern "C" Q_DECL_EXPORT
QCandlestickSeries *ritual_own_ZN24QCandlestickLegendMarker6seriesEv(
    QCandlestickLegendMarker *self) {
  return self->QCandlestickLegendMarker::series();
}
