//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qxylegendmarker.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qxylegendmarker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QXYLegendMarker that Python can take functions over in. Every QXYLegendMarker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQXYLegendMarkerCall0)(const void *, int *);
typedef void * (*CuteQXYLegendMarkerCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYLegendMarkerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYLegendMarkerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYLegendMarker : public QXYLegendMarker {
public:
  using QXYLegendMarker::QXYLegendMarker;
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

  //  LegendMarkerType QXYLegendMarker::type()
  QLegendMarker::LegendMarkerType type() override {
    if (taken[0]) {
      int handled = 0;
      CuteQXYLegendMarkerCall0 call = reinterpret_cast<CuteQXYLegendMarkerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLegendMarker::LegendMarkerType>(given);
    }
    return QXYLegendMarker::type();
  }

  //  QXYSeries *QXYLegendMarker::series()
  QXYSeries *series() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXYLegendMarkerCall1 call = reinterpret_cast<CuteQXYLegendMarkerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXYSeries *>(given);
    }
    return QXYLegendMarker::series();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXYLegendMarkerCall2 call = reinterpret_cast<CuteQXYLegendMarkerCall2>(taken[2]);
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
      CuteQXYLegendMarkerCall3 call = reinterpret_cast<CuteQXYLegendMarkerCall3>(taken[3]);
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
      CuteQXYLegendMarkerCall4 call = reinterpret_cast<CuteQXYLegendMarkerCall4>(taken[4]);
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
      CuteQXYLegendMarkerCall5 call = reinterpret_cast<CuteQXYLegendMarkerCall5>(taken[5]);
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
      CuteQXYLegendMarkerCall6 call = reinterpret_cast<CuteQXYLegendMarkerCall6>(taken[6]);
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
      CuteQXYLegendMarkerCall7 call = reinterpret_cast<CuteQXYLegendMarkerCall7>(taken[7]);
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
      CuteQXYLegendMarkerCall8 call = reinterpret_cast<CuteQXYLegendMarkerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYLegendMarker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QXYLegendMarker10metaObjectEv(
    const QXYLegendMarker *self) {
  return self->metaObject();
}

//  void *QXYLegendMarker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QXYLegendMarker11qt_metacastEPKc(
    QXYLegendMarker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXYLegendMarker::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QXYLegendMarker11qt_metacallEN11QMetaObject4CallEiPPv(
    QXYLegendMarker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QXYLegendMarker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QXYLegendMarker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYLegendMarker::tr(s, c, n));
}

//  QXYLegendMarker::QXYLegendMarker(QXYSeries *series, QLegend *legend,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QXYLegendMarker *ritual_ZN15QXYLegendMarkerC1EP9QXYSeriesP7QLegendP7QObject(
    QXYSeries *series,
    QLegend *legend,
    QObject *parent) {
  return new CuteQXYLegendMarker(series, legend, parent);
}

//  QXYLegendMarker::~QXYLegendMarker()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QXYLegendMarkerD1Ev(QXYLegendMarker *self) {
  delete self;
}

//  LegendMarkerType QXYLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_ZN15QXYLegendMarker4typeEv(
    QXYLegendMarker *self) {
  return self->type();
}

//  QXYSeries *QXYLegendMarker::series()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN15QXYLegendMarker6seriesEv(QXYLegendMarker *self) {
  return self->series();
}

//  QXYLegendMarker::QXYLegendMarker(QXYLegendMarkerPrivate &d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QXYLegendMarker *ritual_ZN15QXYLegendMarkerC1ER22QXYLegendMarkerPrivateP7QObject(
    QXYLegendMarkerPrivate *d,
    QObject *parent) {
  return new CuteQXYLegendMarker(*d, parent);
}

//  QXYLegendMarkerPrivate *QXYLegendMarker::d_func()
extern "C" Q_DECL_EXPORT
QXYLegendMarkerPrivate *ritual_ZN15QXYLegendMarker6d_funcEv(
    QXYLegendMarker *self) {
  return self->d_func();
}

//  const QXYLegendMarkerPrivate *QXYLegendMarker::d_func() const
extern "C" Q_DECL_EXPORT
const QXYLegendMarkerPrivate *ritual_ZNK15QXYLegendMarker6d_funcEv(
    const QXYLegendMarker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQXYLegendMarker, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYLegendMarker(
    QXYLegendMarker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXYLegendMarker *>(self)->take(key, call);
}

//  LegendMarkerType QXYLegendMarker::type()
extern "C" Q_DECL_EXPORT
QLegendMarker::LegendMarkerType ritual_own_ZN15QXYLegendMarker4typeEv(
    QXYLegendMarker *self) {
  return self->QXYLegendMarker::type();
}

//  QXYSeries *QXYLegendMarker::series()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_own_ZN15QXYLegendMarker6seriesEv(QXYLegendMarker *self) {
  return self->QXYLegendMarker::series();
}
