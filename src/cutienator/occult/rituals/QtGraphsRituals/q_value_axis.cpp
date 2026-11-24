//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qvalueaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qvalueaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QValueAxis that Python can take functions over in. Every QValueAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQValueAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValueAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQValueAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQValueAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQValueAxis : public QValueAxis {
public:
  using QValueAxis::QValueAxis;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QAbstractAxis4typeEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  AxisType QValueAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQValueAxisCall0 call = reinterpret_cast<CuteQValueAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QValueAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQValueAxisCall1 call = reinterpret_cast<CuteQValueAxisCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQValueAxisCall2 call = reinterpret_cast<CuteQValueAxisCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQValueAxisCall3 call = reinterpret_cast<CuteQValueAxisCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQValueAxisCall4 call = reinterpret_cast<CuteQValueAxisCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQValueAxisCall5 call = reinterpret_cast<CuteQValueAxisCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQValueAxisCall6 call = reinterpret_cast<CuteQValueAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQValueAxisCall7 call = reinterpret_cast<CuteQValueAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QValueAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QValueAxis10metaObjectEv(
    const QValueAxis *self) {
  return self->metaObject();
}

//  QString QValueAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QValueAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValueAxis::tr(s, c, n));
}

//  QValueAxis::QValueAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QValueAxis *ritual_ZN10QValueAxisC1EP7QObject(QObject *parent) {
  return new CuteQValueAxis(parent);
}

//  QValueAxis::~QValueAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxisD1Ev(QValueAxis *self) {
  delete self;
}

//  AxisType QValueAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK10QValueAxis4typeEv(
    const QValueAxis *self) {
  return self->type();
}

//  void QValueAxis::setMin(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis6setMinEd(QValueAxis *self, qreal min) {
  self->setMin(min);
}

//  qreal QValueAxis::min() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis3minEv(const QValueAxis *self) {
  return self->min();
}

//  void QValueAxis::setMax(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis6setMaxEd(QValueAxis *self, qreal max) {
  self->setMax(max);
}

//  qreal QValueAxis::max() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis3maxEv(const QValueAxis *self) {
  return self->max();
}

//  void QValueAxis::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis8setRangeEdd(
    QValueAxis *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QValueAxis::setSubTickCount(qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis15setSubTickCountEx(
    QValueAxis *self,
    qsizetype count) {
  self->setSubTickCount(count);
}

//  qsizetype QValueAxis::subTickCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QValueAxis12subTickCountEv(const QValueAxis *self) {
  return self->subTickCount();
}

//  void QValueAxis::setTickAnchor(qreal anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis13setTickAnchorEd(QValueAxis *self, qreal anchor) {
  self->setTickAnchor(anchor);
}

//  qreal QValueAxis::tickAnchor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis10tickAnchorEv(const QValueAxis *self) {
  return self->tickAnchor();
}

//  void QValueAxis::setTickInterval(qreal interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis15setTickIntervalEd(
    QValueAxis *self,
    qreal interval) {
  self->setTickInterval(interval);
}

//  qreal QValueAxis::tickInterval() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis12tickIntervalEv(const QValueAxis *self) {
  return self->tickInterval();
}

//  void QValueAxis::setLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis14setLabelFormatERK7QString(
    QValueAxis *self,
    const QString *format) {
  self->setLabelFormat(*format);
}

//  QString QValueAxis::labelFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QValueAxis11labelFormatEv(const QValueAxis *self) {
  return new QString(self->labelFormat());
}

//  void QValueAxis::setLabelPostFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis18setLabelPostFormatERK7QString(
    QValueAxis *self,
    const QString *format) {
  self->setLabelPostFormat(*format);
}

//  QString QValueAxis::labelPostFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QValueAxis15labelPostFormatEv(const QValueAxis *self) {
  return new QString(self->labelPostFormat());
}

//  void QValueAxis::setLabelDecimals(int decimals)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis16setLabelDecimalsEi(
    QValueAxis *self,
    int decimals) {
  self->setLabelDecimals(decimals);
}

//  int QValueAxis::labelDecimals() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QValueAxis13labelDecimalsEv(const QValueAxis *self) {
  return self->labelDecimals();
}

//  void QValueAxis::setZoom(qreal zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis7setZoomEd(QValueAxis *self, qreal zoom) {
  self->setZoom(zoom);
}

//  qreal QValueAxis::zoom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis4zoomEv(const QValueAxis *self) {
  return self->zoom();
}

//  void QValueAxis::setPan(qreal pan)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValueAxis6setPanEd(QValueAxis *self, qreal pan) {
  self->setPan(pan);
}

//  qreal QValueAxis::pan() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis3panEv(const QValueAxis *self) {
  return self->pan();
}

//  qreal QValueAxis::visualMin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis9visualMinEv(const QValueAxis *self) {
  return self->visualMin();
}

//  qreal QValueAxis::visualMax() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QValueAxis9visualMaxEv(const QValueAxis *self) {
  return self->visualMax();
}

//  QValueAxisPrivate *QValueAxis::d_func()
extern "C" Q_DECL_EXPORT
QValueAxisPrivate *ritual_ZN10QValueAxis6d_funcEv(QValueAxis *self) {
  return self->d_func();
}

//  const QValueAxisPrivate *QValueAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QValueAxisPrivate *ritual_ZNK10QValueAxis6d_funcEv(
    const QValueAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQValueAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QValueAxis(QValueAxis *self, const char *key, void *call) {
  return static_cast<CuteQValueAxis *>(self)->take(key, call);
}

//  AxisType QValueAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK10QValueAxis4typeEv(
    const QValueAxis *self) {
  return self->QValueAxis::type();
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
