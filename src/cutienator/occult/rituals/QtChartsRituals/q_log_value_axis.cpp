//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qlogvalueaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qlogvalueaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLogValueAxis that Python can take functions over in. Every QLogValueAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQLogValueAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValueAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLogValueAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLogValueAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLogValueAxis : public QLogValueAxis {
public:
  using QLogValueAxis::QLogValueAxis;
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

  //  AxisType QLogValueAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLogValueAxisCall0 call = reinterpret_cast<CuteQLogValueAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QLogValueAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLogValueAxisCall1 call = reinterpret_cast<CuteQLogValueAxisCall1>(taken[1]);
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
      CuteQLogValueAxisCall2 call = reinterpret_cast<CuteQLogValueAxisCall2>(taken[2]);
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
      CuteQLogValueAxisCall3 call = reinterpret_cast<CuteQLogValueAxisCall3>(taken[3]);
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
      CuteQLogValueAxisCall4 call = reinterpret_cast<CuteQLogValueAxisCall4>(taken[4]);
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
      CuteQLogValueAxisCall5 call = reinterpret_cast<CuteQLogValueAxisCall5>(taken[5]);
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
      CuteQLogValueAxisCall6 call = reinterpret_cast<CuteQLogValueAxisCall6>(taken[6]);
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
      CuteQLogValueAxisCall7 call = reinterpret_cast<CuteQLogValueAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLogValueAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QLogValueAxis10metaObjectEv(
    const QLogValueAxis *self) {
  return self->metaObject();
}

//  void *QLogValueAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QLogValueAxis11qt_metacastEPKc(
    QLogValueAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLogValueAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QLogValueAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QLogValueAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLogValueAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QLogValueAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLogValueAxis::tr(s, c, n));
}

//  QLogValueAxis::QLogValueAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QLogValueAxis *ritual_ZN13QLogValueAxisC1EP7QObject(QObject *parent) {
  return new CuteQLogValueAxis(parent);
}

//  QLogValueAxis::~QLogValueAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxisD1Ev(QLogValueAxis *self) {
  delete self;
}

//  QLogValueAxis::QLogValueAxis(QLogValueAxisPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QLogValueAxis *ritual_ZN13QLogValueAxisC1ER20QLogValueAxisPrivateP7QObject(
    QLogValueAxisPrivate *d,
    QObject *parent) {
  return new CuteQLogValueAxis(*d, parent);
}

//  AxisType QLogValueAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK13QLogValueAxis4typeEv(
    const QLogValueAxis *self) {
  return self->type();
}

//  void QLogValueAxis::setMin(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis6setMinEd(QLogValueAxis *self, qreal min) {
  self->setMin(min);
}

//  qreal QLogValueAxis::min() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QLogValueAxis3minEv(const QLogValueAxis *self) {
  return self->min();
}

//  void QLogValueAxis::setMax(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis6setMaxEd(QLogValueAxis *self, qreal max) {
  self->setMax(max);
}

//  qreal QLogValueAxis::max() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QLogValueAxis3maxEv(const QLogValueAxis *self) {
  return self->max();
}

//  void QLogValueAxis::setRange(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis8setRangeEdd(
    QLogValueAxis *self,
    qreal min,
    qreal max) {
  self->setRange(min, max);
}

//  void QLogValueAxis::setLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis14setLabelFormatERK7QString(
    QLogValueAxis *self,
    const QString *format) {
  self->setLabelFormat(*format);
}

//  QString QLogValueAxis::labelFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QLogValueAxis11labelFormatEv(
    const QLogValueAxis *self) {
  return new QString(self->labelFormat());
}

//  void QLogValueAxis::setBase(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis7setBaseEd(QLogValueAxis *self, qreal base) {
  self->setBase(base);
}

//  qreal QLogValueAxis::base() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QLogValueAxis4baseEv(const QLogValueAxis *self) {
  return self->base();
}

//  int QLogValueAxis::tickCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLogValueAxis9tickCountEv(const QLogValueAxis *self) {
  return self->tickCount();
}

//  void QLogValueAxis::setMinorTickCount(int minorTickCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis17setMinorTickCountEi(
    QLogValueAxis *self,
    int minorTickCount) {
  self->setMinorTickCount(minorTickCount);
}

//  int QLogValueAxis::minorTickCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLogValueAxis14minorTickCountEv(const QLogValueAxis *self) {
  return self->minorTickCount();
}

//  void QLogValueAxis::minChanged(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis10minChangedEd(QLogValueAxis *self, qreal min) {
  self->minChanged(min);
}

//  void QLogValueAxis::maxChanged(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis10maxChangedEd(QLogValueAxis *self, qreal max) {
  self->maxChanged(max);
}

//  void QLogValueAxis::rangeChanged(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis12rangeChangedEdd(
    QLogValueAxis *self,
    qreal min,
    qreal max) {
  self->rangeChanged(min, max);
}

//  void QLogValueAxis::labelFormatChanged(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis18labelFormatChangedERK7QString(
    QLogValueAxis *self,
    const QString *format) {
  self->labelFormatChanged(*format);
}

//  void QLogValueAxis::baseChanged(qreal base)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis11baseChangedEd(
    QLogValueAxis *self,
    qreal base) {
  self->baseChanged(base);
}

//  void QLogValueAxis::tickCountChanged(int tickCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis16tickCountChangedEi(
    QLogValueAxis *self,
    int tickCount) {
  self->tickCountChanged(tickCount);
}

//  void QLogValueAxis::minorTickCountChanged(int minorTickCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLogValueAxis21minorTickCountChangedEi(
    QLogValueAxis *self,
    int minorTickCount) {
  self->minorTickCountChanged(minorTickCount);
}

//  QLogValueAxisPrivate *QLogValueAxis::d_func()
extern "C" Q_DECL_EXPORT
QLogValueAxisPrivate *ritual_ZN13QLogValueAxis6d_funcEv(
    QLogValueAxis *self) {
  return self->d_func();
}

//  const QLogValueAxisPrivate *QLogValueAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QLogValueAxisPrivate *ritual_ZNK13QLogValueAxis6d_funcEv(
    const QLogValueAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLogValueAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLogValueAxis(
    QLogValueAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLogValueAxis *>(self)->take(key, call);
}

//  AxisType QLogValueAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK13QLogValueAxis4typeEv(
    const QLogValueAxis *self) {
  return self->QLogValueAxis::type();
}
