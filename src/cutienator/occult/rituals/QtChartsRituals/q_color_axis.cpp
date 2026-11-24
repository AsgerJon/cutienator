//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcoloraxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qcoloraxis.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QColorAxis that Python can take functions over in. Every QColorAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQColorAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColorAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQColorAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQColorAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQColorAxis : public QColorAxis {
public:
  using QColorAxis::QColorAxis;
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

  //  AxisType QColorAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQColorAxisCall0 call = reinterpret_cast<CuteQColorAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QColorAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColorAxisCall1 call = reinterpret_cast<CuteQColorAxisCall1>(taken[1]);
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
      CuteQColorAxisCall2 call = reinterpret_cast<CuteQColorAxisCall2>(taken[2]);
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
      CuteQColorAxisCall3 call = reinterpret_cast<CuteQColorAxisCall3>(taken[3]);
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
      CuteQColorAxisCall4 call = reinterpret_cast<CuteQColorAxisCall4>(taken[4]);
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
      CuteQColorAxisCall5 call = reinterpret_cast<CuteQColorAxisCall5>(taken[5]);
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
      CuteQColorAxisCall6 call = reinterpret_cast<CuteQColorAxisCall6>(taken[6]);
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
      CuteQColorAxisCall7 call = reinterpret_cast<CuteQColorAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QColorAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QColorAxis10metaObjectEv(
    const QColorAxis *self) {
  return self->metaObject();
}

//  QString QColorAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QColorAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColorAxis::tr(s, c, n));
}

//  QColorAxis::QColorAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QColorAxis *ritual_ZN10QColorAxisC1EP7QObject(QObject *parent) {
  return new CuteQColorAxis(parent);
}

//  QColorAxis::~QColorAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxisD1Ev(QColorAxis *self) {
  delete self;
}

//  AxisType QColorAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK10QColorAxis4typeEv(
    const QColorAxis *self) {
  return self->type();
}

//  void QColorAxis::setMin(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis6setMinEd(QColorAxis *self, qreal min) {
  self->setMin(min);
}

//  qreal QColorAxis::min() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QColorAxis3minEv(const QColorAxis *self) {
  return self->min();
}

//  void QColorAxis::setMax(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis6setMaxEd(QColorAxis *self, qreal max) {
  self->setMax(max);
}

//  qreal QColorAxis::max() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QColorAxis3maxEv(const QColorAxis *self) {
  return self->max();
}

//  void QColorAxis::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis8setRangeEdd(
    QColorAxis *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QColorAxis::setTickCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis12setTickCountEi(QColorAxis *self, int count) {
  self->setTickCount(count);
}

//  int QColorAxis::tickCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QColorAxis9tickCountEv(const QColorAxis *self) {
  return self->tickCount();
}

//  void QColorAxis::setSize(const qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis7setSizeEd(QColorAxis *self, qreal size) {
  self->setSize(size);
}

//  qreal QColorAxis::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QColorAxis4sizeEv(const QColorAxis *self) {
  return self->size();
}

//  void QColorAxis::setGradient(const QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis11setGradientERK15QLinearGradient(
    QColorAxis *self,
    const QLinearGradient *gradient) {
  self->setGradient(*gradient);
}

//  QLinearGradient QColorAxis::gradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK10QColorAxis8gradientEv(const QColorAxis *self) {
  return new QLinearGradient(self->gradient());
}

//  void QColorAxis::setAutoRange(bool autoRange)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QColorAxis12setAutoRangeEb(
    QColorAxis *self,
    bool autoRange) {
  self->setAutoRange(autoRange);
}

//  bool QColorAxis::autoRange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QColorAxis9autoRangeEv(const QColorAxis *self) {
  return self->autoRange();
}

//  QColorAxisPrivate *QColorAxis::d_func()
extern "C" Q_DECL_EXPORT
QColorAxisPrivate *ritual_ZN10QColorAxis6d_funcEv(QColorAxis *self) {
  return self->d_func();
}

//  const QColorAxisPrivate *QColorAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QColorAxisPrivate *ritual_ZNK10QColorAxis6d_funcEv(
    const QColorAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQColorAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColorAxis(QColorAxis *self, const char *key, void *call) {
  return static_cast<CuteQColorAxis *>(self)->take(key, call);
}

//  AxisType QColorAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK10QColorAxis4typeEv(
    const QColorAxis *self) {
  return self->QColorAxis::type();
}
