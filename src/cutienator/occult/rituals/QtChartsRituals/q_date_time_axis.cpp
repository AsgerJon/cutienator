//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qdatetimeaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_datetime_axis)
#include <QtCharts/qdatetimeaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDateTimeAxis that Python can take functions over in. Every QDateTimeAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQDateTimeAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDateTimeAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDateTimeAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDateTimeAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDateTimeAxis : public QDateTimeAxis {
public:
  using QDateTimeAxis::QDateTimeAxis;
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

  //  AxisType QDateTimeAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDateTimeAxisCall0 call = reinterpret_cast<CuteQDateTimeAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QDateTimeAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDateTimeAxisCall1 call = reinterpret_cast<CuteQDateTimeAxisCall1>(taken[1]);
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
      CuteQDateTimeAxisCall2 call = reinterpret_cast<CuteQDateTimeAxisCall2>(taken[2]);
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
      CuteQDateTimeAxisCall3 call = reinterpret_cast<CuteQDateTimeAxisCall3>(taken[3]);
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
      CuteQDateTimeAxisCall4 call = reinterpret_cast<CuteQDateTimeAxisCall4>(taken[4]);
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
      CuteQDateTimeAxisCall5 call = reinterpret_cast<CuteQDateTimeAxisCall5>(taken[5]);
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
      CuteQDateTimeAxisCall6 call = reinterpret_cast<CuteQDateTimeAxisCall6>(taken[6]);
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
      CuteQDateTimeAxisCall7 call = reinterpret_cast<CuteQDateTimeAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDateTimeAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDateTimeAxis10metaObjectEv(
    const QDateTimeAxis *self) {
  return self->metaObject();
}

//  void *QDateTimeAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QDateTimeAxis11qt_metacastEPKc(
    QDateTimeAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDateTimeAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QDateTimeAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QDateTimeAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDateTimeAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QDateTimeAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDateTimeAxis::tr(s, c, n));
}

//  QDateTimeAxis::QDateTimeAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QDateTimeAxis *ritual_ZN13QDateTimeAxisC1EP7QObject(QObject *parent) {
  return new CuteQDateTimeAxis(parent);
}

//  QDateTimeAxis::~QDateTimeAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxisD1Ev(QDateTimeAxis *self) {
  delete self;
}

//  QDateTimeAxis::QDateTimeAxis(QDateTimeAxisPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QDateTimeAxis *ritual_ZN13QDateTimeAxisC1ER20QDateTimeAxisPrivateP7QObject(
    QDateTimeAxisPrivate *d,
    QObject *parent) {
  return new CuteQDateTimeAxis(*d, parent);
}

//  AxisType QDateTimeAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK13QDateTimeAxis4typeEv(
    const QDateTimeAxis *self) {
  return self->type();
}

//  void QDateTimeAxis::setMin(QDateTime min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis6setMinE9QDateTime(
    QDateTimeAxis *self,
    const QDateTime *min) {
  self->setMin(*min);
}

//  QDateTime QDateTimeAxis::min() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeAxis3minEv(const QDateTimeAxis *self) {
  return new QDateTime(self->min());
}

//  void QDateTimeAxis::setMax(QDateTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis6setMaxE9QDateTime(
    QDateTimeAxis *self,
    const QDateTime *max) {
  self->setMax(*max);
}

//  QDateTime QDateTimeAxis::max() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QDateTimeAxis3maxEv(const QDateTimeAxis *self) {
  return new QDateTime(self->max());
}

//  void QDateTimeAxis::setRange(QDateTime min, QDateTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis8setRangeE9QDateTimeS0_(
    QDateTimeAxis *self,
    const QDateTime *min,
    const QDateTime *max) {
  self->setRange(*min, *max);
}

//  void QDateTimeAxis::setFormat(QString format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis9setFormatE7QString(
    QDateTimeAxis *self,
    const QString *format) {
  self->setFormat(*format);
}

//  QString QDateTimeAxis::format() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDateTimeAxis6formatEv(const QDateTimeAxis *self) {
  return new QString(self->format());
}

//  void QDateTimeAxis::setTickCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis12setTickCountEi(
    QDateTimeAxis *self,
    int count) {
  self->setTickCount(count);
}

//  int QDateTimeAxis::tickCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QDateTimeAxis9tickCountEv(const QDateTimeAxis *self) {
  return self->tickCount();
}

//  void QDateTimeAxis::minChanged(QDateTime min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis10minChangedE9QDateTime(
    QDateTimeAxis *self,
    const QDateTime *min) {
  self->minChanged(*min);
}

//  void QDateTimeAxis::maxChanged(QDateTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis10maxChangedE9QDateTime(
    QDateTimeAxis *self,
    const QDateTime *max) {
  self->maxChanged(*max);
}

//  void QDateTimeAxis::rangeChanged(QDateTime min, QDateTime max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis12rangeChangedE9QDateTimeS0_(
    QDateTimeAxis *self,
    const QDateTime *min,
    const QDateTime *max) {
  self->rangeChanged(*min, *max);
}

//  void QDateTimeAxis::formatChanged(QString format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis13formatChangedE7QString(
    QDateTimeAxis *self,
    const QString *format) {
  self->formatChanged(*format);
}

//  void QDateTimeAxis::tickCountChanged(int tick)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDateTimeAxis16tickCountChangedEi(
    QDateTimeAxis *self,
    int tick) {
  self->tickCountChanged(tick);
}

//  QDateTimeAxisPrivate *QDateTimeAxis::d_func()
extern "C" Q_DECL_EXPORT
QDateTimeAxisPrivate *ritual_ZN13QDateTimeAxis6d_funcEv(
    QDateTimeAxis *self) {
  return self->d_func();
}

//  const QDateTimeAxisPrivate *QDateTimeAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QDateTimeAxisPrivate *ritual_ZNK13QDateTimeAxis6d_funcEv(
    const QDateTimeAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDateTimeAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDateTimeAxis(
    QDateTimeAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDateTimeAxis *>(self)->take(key, call);
}

//  AxisType QDateTimeAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK13QDateTimeAxis4typeEv(
    const QDateTimeAxis *self) {
  return self->QDateTimeAxis::type();
}

#endif  // QT_CONFIG(charts_datetime_axis)
