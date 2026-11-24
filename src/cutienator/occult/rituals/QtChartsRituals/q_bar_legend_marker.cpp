//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qbarlegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qbarlegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBarLegendMarker that Python can take functions over in. Every QBarLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBarLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQBarLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarLegendMarker : public QBarLegendMarker {
public:
  using QBarLegendMarker::QBarLegendMarker;
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

  //  LegendMarkerType QBarLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarLegendMarkerCall0 call = reinterpret_cast<CuteQBarLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QBarLegendMarker::type();
  }

  //  QAbstractBarSeries *QBarLegendMarker::series()
  QAbstractBarSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarLegendMarkerCall1 call = reinterpret_cast<CuteQBarLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractBarSeries *>(given);
    }
    return QBarLegendMarker::series();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQBarLegendMarkerCall2 call = reinterpret_cast<CuteQBarLegendMarkerCall2>(taken[2]);
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
      CuteQBarLegendMarkerCall3 call = reinterpret_cast<CuteQBarLegendMarkerCall3>(taken[3]);
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
      CuteQBarLegendMarkerCall4 call = reinterpret_cast<CuteQBarLegendMarkerCall4>(taken[4]);
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
      CuteQBarLegendMarkerCall5 call = reinterpret_cast<CuteQBarLegendMarkerCall5>(taken[5]);
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
      CuteQBarLegendMarkerCall6 call = reinterpret_cast<CuteQBarLegendMarkerCall6>(taken[6]);
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
      CuteQBarLegendMarkerCall7 call = reinterpret_cast<CuteQBarLegendMarkerCall7>(taken[7]);
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
      CuteQBarLegendMarkerCall8 call = reinterpret_cast<CuteQBarLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QBarLegendMarker10metaObjectEv(
    const QBarLegendMarker *self) {
  return self->metaObject();
}

//  QString QBarLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QBarLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarLegendMarker::tr(s, c, n));
}

//  QBarLegendMarker::QBarLegendMarker(QAbstractBarSeries *series, QBarSet
//      *barset, QLegend *legend, QObject *parent)
extern "C" Q_DECL_EXPORT
QBarLegendMarker *ritual_ZN16QBarLegendMarkerC1EP18QAbstractBarSeriesP7QBarSetP7QLegendP7QObject(
    QAbstractBarSeries *series,
    QBarSet *barset,
    QLegend *legend,
    QObject *parent) {
  return new CuteQBarLegendMarker(series, barset, legend, parent);
}

//  QBarLegendMarker::~QBarLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarLegendMarkerD1Ev(QBarLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QBarLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN16QBarLegendMarker4typeEv(
    QBarLegendMarker *self) {
  return self->type();
}

//  QAbstractBarSeries *QBarLegendMarker::series()
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZN16QBarLegendMarker6seriesEv(
    QBarLegendMarker *self) {
  return self->series();
}

//  QBarSet *QBarLegendMarker::barset()
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN16QBarLegendMarker6barsetEv(QBarLegendMarker *self) {
  return self->barset();
}

//  QBarLegendMarkerPrivate *QBarLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QBarLegendMarkerPrivate *ritual_ZN16QBarLegendMarker6d_funcEv(
    QBarLegendMarker *self) {
  return self->d_func();
}

//  const QBarLegendMarkerPrivate *QBarLegendMarker::d_func() const
extern "C" Q_DECL_EXPORT
const QBarLegendMarkerPrivate *ritual_ZNK16QBarLegendMarker6d_funcEv(
    const QBarLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBarLegendMarker, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarLegendMarker(
    QBarLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QBarLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN16QBarLegendMarker4typeEv(
    QBarLegendMarker *self) {
  return self->QBarLegendMarker::type();
}

//  QAbstractBarSeries *QBarLegendMarker::series()
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_own_ZN16QBarLegendMarker6seriesEv(
    QBarLegendMarker *self) {
  return self->QBarLegendMarker::series();
}
