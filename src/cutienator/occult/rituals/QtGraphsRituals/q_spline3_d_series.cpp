//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qspline3dseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qspline3dseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSpline3DSeries that Python can take functions over in. Every QSpline3DSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpline3DSeriesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSpline3DSeriesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpline3DSeriesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpline3DSeriesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpline3DSeriesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpline3DSeriesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSpline3DSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSpline3DSeries : public QSpline3DSeries {
public:
  using QSpline3DSeries::QSpline3DSeries;
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
      CuteQSpline3DSeriesCall0 call = reinterpret_cast<CuteQSpline3DSeriesCall0>(taken[0]);
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
      CuteQSpline3DSeriesCall1 call = reinterpret_cast<CuteQSpline3DSeriesCall1>(taken[1]);
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
      CuteQSpline3DSeriesCall2 call = reinterpret_cast<CuteQSpline3DSeriesCall2>(taken[2]);
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
      CuteQSpline3DSeriesCall3 call = reinterpret_cast<CuteQSpline3DSeriesCall3>(taken[3]);
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
      CuteQSpline3DSeriesCall4 call = reinterpret_cast<CuteQSpline3DSeriesCall4>(taken[4]);
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
      CuteQSpline3DSeriesCall5 call = reinterpret_cast<CuteQSpline3DSeriesCall5>(taken[5]);
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
      CuteQSpline3DSeriesCall6 call = reinterpret_cast<CuteQSpline3DSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSpline3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QSpline3DSeries10metaObjectEv(
    const QSpline3DSeries *self) {
  return self->metaObject();
}

//  QString QSpline3DSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QSpline3DSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSpline3DSeries::tr(s, c, n));
}

//  void QSpline3DSeries::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries24qt_qmlMarker_uncreatableEv(
    QSpline3DSeries *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QSpline3DSeries::QSpline3DSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QSpline3DSeries *ritual_ZN15QSpline3DSeriesC1EP7QObject(QObject *parent) {
  return new CuteQSpline3DSeries(parent);
}

//  QSpline3DSeries::QSpline3DSeries(QScatterDataProxy *dataProxy, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSpline3DSeries *ritual_ZN15QSpline3DSeriesC1EP17QScatterDataProxyP7QObject(
    QScatterDataProxy *dataProxy,
    QObject *parent) {
  return new CuteQSpline3DSeries(dataProxy, parent);
}

//  QSpline3DSeries::~QSpline3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeriesD1Ev(QSpline3DSeries *self) {
  delete self;
}

//  void QSpline3DSeries::setSplineVisible(bool draw)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries16setSplineVisibleEb(
    QSpline3DSeries *self,
    bool draw) {
  self->setSplineVisible(draw);
}

//  bool QSpline3DSeries::isSplineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSpline3DSeries15isSplineVisibleEv(
    const QSpline3DSeries *self) {
  return self->isSplineVisible();
}

//  void QSpline3DSeries::setSplineTension(qreal tension)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries16setSplineTensionEd(
    QSpline3DSeries *self,
    qreal tension) {
  self->setSplineTension(tension);
}

//  qreal QSpline3DSeries::splineTension() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QSpline3DSeries13splineTensionEv(
    const QSpline3DSeries *self) {
  return self->splineTension();
}

//  void QSpline3DSeries::setSplineKnotting(qreal knotting)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries17setSplineKnottingEd(
    QSpline3DSeries *self,
    qreal knotting) {
  self->setSplineKnotting(knotting);
}

//  qreal QSpline3DSeries::splineKnotting() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QSpline3DSeries14splineKnottingEv(
    const QSpline3DSeries *self) {
  return self->splineKnotting();
}

//  void QSpline3DSeries::setSplineLooping(bool looping)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries16setSplineLoopingEb(
    QSpline3DSeries *self,
    bool looping) {
  self->setSplineLooping(looping);
}

//  bool QSpline3DSeries::isSplineLooping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSpline3DSeries15isSplineLoopingEv(
    const QSpline3DSeries *self) {
  return self->isSplineLooping();
}

//  void QSpline3DSeries::setSplineColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries14setSplineColorE6QColor(
    QSpline3DSeries *self,
    const QColor *color) {
  self->setSplineColor(*color);
}

//  QColor QSpline3DSeries::splineColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QSpline3DSeries11splineColorEv(
    const QSpline3DSeries *self) {
  return new QColor(self->splineColor());
}

//  void QSpline3DSeries::setSplineResolution(int resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSpline3DSeries19setSplineResolutionEi(
    QSpline3DSeries *self,
    int resolution) {
  self->setSplineResolution(resolution);
}

//  int QSpline3DSeries::splineResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSpline3DSeries16splineResolutionEv(
    const QSpline3DSeries *self) {
  return self->splineResolution();
}

//  a Python function taken by a CuteQSpline3DSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpline3DSeries(
    QSpline3DSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpline3DSeries *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
